import React from 'react';
import { CheckCircle2, Eye } from 'lucide-react';
import MathText from './MathText';
import MathKeypad from './MathKeypad';
import WorkingPad from './WorkingPad';
import DiagramRenderer from './DiagramRenderer';
import { latexify } from './mathLatexify';

const insertAtCaret = (el, value, token, offset) => {
    const start = el?.selectionStart ?? value.length;
    const end = el?.selectionEnd ?? value.length;
    const next = value.slice(0, start) + token + value.slice(end);
    const caret = start + token.length + (offset || 0);
    return { next, caret };
};

/**
 * Extracts distinct question parts from sub_parts, parts, or numbered/lettered prompt lines,
 * or multi-blank word equations (e.g. "Acid + Base -> [Part a] + [Part b]").
 */
export function extractQuestionParts(question) {
    if (Array.isArray(question?.sub_parts) && question.sub_parts.length > 1) {
        return question.sub_parts.map((p, idx) => ({
            id: p.id || `part_${String.fromCharCode(97 + idx)}`,
            letter: String.fromCharCode(97 + idx),
            label: p.label || `(${String.fromCharCode(97 + idx)})`,
            marks: p.marks,
            expected_answer: p.expected_answer || p.answer_latex || ''
        }));
    }
    if (Array.isArray(question?.parts) && question.parts.length > 1) {
        return question.parts.map((p, idx) => ({
            id: `part_${String.fromCharCode(97 + idx)}`,
            letter: String.fromCharCode(97 + idx),
            label: typeof p === 'string' ? p : (p.label || p.question || `(${String.fromCharCode(97 + idx)})`),
            marks: p.marks,
            expected_answer: p.expected_answer || ''
        }));
    }
    const prompt = String(question?.prompt || question?.prompt_latex || question?.question_text || '').trim();
    if (prompt) {
        const lines = prompt.split('\n').map(l => l.trim()).filter(Boolean);
        const numberedItems = lines.filter(l => /^(\d+[\.\)]|[a-z][\.\)]|\([a-z\d]+\)|\([ivx]+\))\s+/i.test(l));
        if (numberedItems.length > 1) {
            return numberedItems.map((item, idx) => ({
                id: `part_${String.fromCharCode(97 + idx)}`,
                letter: String.fromCharCode(97 + idx),
                label: item.replace(/^(\d+[\.\)]|[a-z][\.\)]|\([a-z\d]+\))\s+/i, ''),
                marks: undefined,
                expected_answer: ''
            }));
        }
        // Check for 2+ fill-in-the-blank slots (e.g. ____ + ____ or [a] + [b])
        const blankMatches = prompt.match(/_{3,}|\[\s*[a-d1-4]\s*\]/gi);
        if (blankMatches && blankMatches.length >= 2 && blankMatches.length <= 5) {
            return blankMatches.map((_, idx) => ({
                id: `part_${String.fromCharCode(97 + idx)}`,
                letter: String.fromCharCode(97 + idx),
                label: `Blank (${String.fromCharCode(97 + idx)})`,
                marks: 1,
                expected_answer: ''
            }));
        }
    }
    return [];
}

/**
 * Extracts embedded MCQ options if a generator embedded A) ... B) ... C) ... D) ... in the prompt text.
 */
export function extractEmbeddedMcqOptions(question) {
    if (Array.isArray(question?.options) && question.options.length > 0) return question.options;
    if (Array.isArray(question?.options_latex) && question.options_latex.length > 0) return question.options_latex;
    const prompt = String(question?.prompt || question?.prompt_latex || question?.question_text || '');
    if (!prompt) return null;
    const optionLines = prompt
        .split('\n')
        .map((l) => l.trim())
        .filter((l) => /^[A-D][\)\.]\s+\S+/i.test(l));
    if (optionLines.length >= 3 && optionLines.length <= 5) {
        return optionLines.map((l) => l.replace(/^[A-D][\)\.]\s+/i, '').trim());
    }
    return null;
}

const MathAnswerArea = ({ question, topic, onCheck, result, busy = false, hideStimulusDiagram = false }) => {
    const rawType = String(question?.question_type || '').toLowerCase();
    const embeddedOptions = React.useMemo(() => extractEmbeddedMcqOptions(question), [question]);
    const qType = (rawType === 'mcq' || (Array.isArray(embeddedOptions) && embeddedOptions.length > 0))
        ? 'mcq'
        : (rawType === 'diagram_select' || Boolean(question?.correct_edge))
            ? 'diagram_select'
            : (rawType === 'math_steps')
                ? 'math_steps'
                : 'math_short';
    const mathStorageKey = question?.id ? `fundile_draft_math_${question.id}` : null;
    const offlineStorageKey = question?.id ? `fundile_offline_draft_math_${question.id}` : null;

    const questionParts = React.useMemo(() => extractQuestionParts(question), [question]);
    const isMultiPart = qType === 'math_short' && questionParts.length > 1;

    const [isOnline, setIsOnline] = React.useState(() => (typeof navigator !== 'undefined' ? navigator.onLine : true));
    const [draftSaved, setDraftSaved] = React.useState(false);

    // Track online/offline status
    React.useEffect(() => {
        const handleOnline = () => setIsOnline(true);
        const handleOffline = () => setIsOnline(false);
        window.addEventListener('online', handleOnline);
        window.addEventListener('offline', handleOffline);
        return () => {
            window.removeEventListener('online', handleOnline);
            window.removeEventListener('offline', handleOffline);
        };
    }, []);

    const [selected, setSelected] = React.useState(null);
    const [selectedEdge, setSelectedEdge] = React.useState(null);
    const [value, setValue] = React.useState(() => {
        if (typeof window !== 'undefined') {
            try {
                if (mathStorageKey) {
                    const saved = sessionStorage.getItem(mathStorageKey);
                    if (saved) {
                        const parsed = JSON.parse(saved);
                        return parsed.value || '';
                    }
                }
                if (offlineStorageKey) {
                    const savedLocal = localStorage.getItem(offlineStorageKey);
                    if (savedLocal) {
                        const parsed = JSON.parse(savedLocal);
                        return parsed.value || '';
                    }
                }
            } catch (e) {}
        }
        return '';
    });
    const [partValues, setPartValues] = React.useState(() => {
        if (typeof window !== 'undefined') {
            try {
                if (mathStorageKey) {
                    const saved = sessionStorage.getItem(mathStorageKey);
                    if (saved) {
                        const parsed = JSON.parse(saved);
                        if (Array.isArray(parsed.partValues) && parsed.partValues.length > 0) return parsed.partValues;
                    }
                }
            } catch (e) {}
        }
        return questionParts.length > 0 ? questionParts.map(() => '') : [];
    });
    const [lines, setLines] = React.useState(() => {
        if (typeof window !== 'undefined') {
            try {
                if (mathStorageKey) {
                    const saved = sessionStorage.getItem(mathStorageKey);
                    if (saved) {
                        const parsed = JSON.parse(saved);
                        if (Array.isArray(parsed.lines) && parsed.lines.length > 0) return parsed.lines;
                    }
                }
                if (offlineStorageKey) {
                    const savedLocal = localStorage.getItem(offlineStorageKey);
                    if (savedLocal) {
                        const parsed = JSON.parse(savedLocal);
                        if (Array.isArray(parsed.lines) && parsed.lines.length > 0) return parsed.lines;
                    }
                }
            } catch (e) {}
        }
        return [''];
    });
    const [showSolution, setShowSolution] = React.useState(false);
    const [savedLearnerWorking, setSavedLearnerWorking] = React.useState(null);
    const inputs = React.useRef({});
    const activeField = React.useRef(isMultiPart ? 'part-0' : (qType === 'math_short' ? 'single' : 'line-0'));

    React.useEffect(() => {
        setSelected(null);
        setSelectedEdge(null);
        setSavedLearnerWorking(null);
        if (typeof window !== 'undefined') {
            try {
                if (mathStorageKey) {
                    const saved = sessionStorage.getItem(mathStorageKey);
                    if (saved) {
                        const parsed = JSON.parse(saved);
                        setValue(parsed.value || '');
                        setLines(parsed.lines || ['']);
                        if (Array.isArray(parsed.partValues)) setPartValues(parsed.partValues);
                        setShowSolution(false);
                        setDraftSaved(true);
                        activeField.current = isMultiPart ? 'part-0' : (qType === 'math_short' ? 'single' : 'line-0');
                        return;
                    }
                }
                if (offlineStorageKey) {
                    const savedLocal = localStorage.getItem(offlineStorageKey);
                    if (savedLocal) {
                        const parsed = JSON.parse(savedLocal);
                        setValue(parsed.value || '');
                        setLines(parsed.lines || ['']);
                        if (Array.isArray(parsed.partValues)) setPartValues(parsed.partValues);
                        setShowSolution(false);
                        setDraftSaved(true);
                        if (mathStorageKey) {
                            try { sessionStorage.setItem(mathStorageKey, JSON.stringify(parsed)); } catch (e) {}
                        }
                        activeField.current = isMultiPart ? 'part-0' : (qType === 'math_short' ? 'single' : 'line-0');
                        return;
                    }
                }
            } catch (e) {}
        }
        setValue('');
        setLines(['']);
        if (isMultiPart) {
            setPartValues(questionParts.map(() => ''));
            activeField.current = 'part-0';
        } else {
            setPartValues([]);
            activeField.current = qType === 'math_short' ? 'single' : 'line-0';
        }
        setShowSolution(false);
        setDraftSaved(false);
    }, [question?.id, qType, isMultiPart, mathStorageKey, offlineStorageKey]);

    // Persist draft in sessionStorage and localStorage as learner inputs math
    React.useEffect(() => {
        if (typeof window !== 'undefined') {
            const hasContent = Boolean(value || (lines.length > 1 || lines[0]) || partValues.some(p => p.trim()));
            if (hasContent) {
                const payload = JSON.stringify({ value, lines, partValues, updatedAt: Date.now() });
                if (mathStorageKey) {
                    try { sessionStorage.setItem(mathStorageKey, payload); } catch (e) {}
                }
                if (offlineStorageKey) {
                    try { localStorage.setItem(offlineStorageKey, payload); } catch (e) {}
                }
                setDraftSaved(true);
            }
        }
    }, [value, lines, partValues, mathStorageKey, offlineStorageKey]);

    // Clear draft once marked
    React.useEffect(() => {
        if (result) {
            if (mathStorageKey) {
                try { sessionStorage.removeItem(mathStorageKey); } catch (e) {}
            }
            if (offlineStorageKey) {
                try { localStorage.removeItem(offlineStorageKey); } catch (e) {}
            }
            setDraftSaved(false);
        }
    }, [result, mathStorageKey, offlineStorageKey]);

    const registerInput = (id, el) => { if (el) inputs.current[id] = el; };
    const onFocusField = (id) => {
        activeField.current = id;
        inputs.current[id]?.focus();
    };

    const handleInsert = (token, offset) => {
        const id = activeField.current;
        const el = inputs.current[id];
        if (id.startsWith('part-')) {
            const idx = Number(id.split('-')[1]);
            const curVal = partValues[idx] || '';
            const { next, caret } = insertAtCaret(el, curVal, token, offset);
            const nextPartValues = [...partValues];
            nextPartValues[idx] = next;
            setPartValues(nextPartValues);
            setValue(nextPartValues.join('; '));
            requestAnimationFrame(() => { if (el) { el.focus(); el.setSelectionRange(caret, caret); } });
        } else if (id === 'single') {
            const { next, caret } = insertAtCaret(el, value, token, offset);
            setValue(next);
            requestAnimationFrame(() => { if (el) { el.focus(); el.setSelectionRange(caret, caret); } });
        } else {
            const idx = Number(id.split('-')[1]);
            const { next, caret } = insertAtCaret(el, lines[idx] || '', token, offset);
            const nextLines = [...lines];
            nextLines[idx] = next;
            setLines(nextLines);
            requestAnimationFrame(() => { if (el) { el.focus(); el.setSelectionRange(caret, caret); } });
        }
    };

    const [showWorkingPad, setShowWorkingPad] = React.useState(false);

    const handleCheck = () => {
        if (qType === 'mcq') onCheck?.(selected);
        else if (qType === 'diagram_select') onCheck?.(selectedEdge);
        else if (qType === 'math_short') {
            if (isMultiPart) {
                onCheck?.({
                    parts: partValues,
                    value: partValues.join('; '),
                    text: partValues.join('; '),
                    steps: lines.filter((l) => l.trim())
                });
            } else if (showWorkingPad && lines.some((l) => l.trim())) {
                const validLines = lines.filter((l) => l.trim());
                if (value.trim() && validLines[validLines.length - 1] !== value.trim()) {
                    validLines.push(value.trim());
                }
                onCheck?.(validLines.length > 1 ? validLines : (value.trim() || validLines[0] || ''));
            } else {
                onCheck?.(value);
            }
        }
        else onCheck?.(lines.filter((l) => l.trim()));
    };

    const sol = question?.canonical_solution;
    const diagram = question?.diagram_spec || question?.diagram || question?.graph || question?.function_graph;
    const checkDisabled = busy || (qType === 'diagram_select' && !selectedEdge && !result);

    // Hide MathKeypad when the expected answer is purely English words/classification (e.g. "Acute", "Reflex", "Monomial")
    const isPureWordResponse = React.useMemo(() => {
        const exp = String(question?.correct_answer || question?.expected_answer || question?.answer_latex || '').trim();
        if (!exp) return false;
        const hasDigitsOrOps = /[\d=+\-*/^_\\<>]/.test(exp);
        const isOnlyWords = /^[a-zA-Z\s,()-]+$/.test(exp) && exp.length >= 3;
        return !hasDigitsOrOps && isOnlyWords && qType === 'math_short';
    }, [question, qType]);

    const handleToggleRevealSolution = () => {
        if (!showSolution) {
            setSavedLearnerWorking({
                value,
                partValues: [...partValues],
                lines: [...lines],
                selected,
                selectedEdge,
            });
            if (qType === 'math_steps' && sol?.steps?.length) {
                setLines(sol.steps.map((st) => st.to_latex || st.step || ''));
            } else if (qType === 'math_short') {
                if (isMultiPart && question?.sub_parts?.length) {
                    const modelParts = question.sub_parts.map(p => p.expected_answer || p.answer_latex || '');
                    setPartValues(modelParts);
                    setValue(modelParts.join('; '));
                } else {
                    setValue(sol?.final_latex || question?.correct_answer || '');
                }
            } else if (qType === 'mcq' && question?.correct_index !== undefined) {
                setSelected(question.correct_index);
            } else if (qType === 'diagram_select' && (question?.correct_edge || result?.correct_edge)) {
                setSelectedEdge(question?.correct_edge || result?.correct_edge);
            }
            setShowSolution(true);
        } else {
            if (savedLearnerWorking) {
                setValue(savedLearnerWorking.value || '');
                if (Array.isArray(savedLearnerWorking.partValues)) setPartValues(savedLearnerWorking.partValues);
                setLines(savedLearnerWorking.lines || ['']);
                setSelected(savedLearnerWorking.selected ?? null);
                setSelectedEdge(savedLearnerWorking.selectedEdge ?? null);
            }
            setShowSolution(false);
        }
    };

    const mcqOptionsList = embeddedOptions || question?.options || [];

    return (
        <div className="space-y-5">
            {/* Model Working Active Banner */}
            {showSolution && (
                <div data-testid="banner-math-model-active" className="p-2.5 rounded-xl bg-amber-50 border border-amber-300 text-xs text-amber-900 flex items-center justify-between shadow-2xs font-sans">
                    <div className="flex items-center gap-2">
                        <span className="font-bold">📖 Model Working Displayed:</span>
                        <span>Studying expected mathematical steps. Click &quot;Restore My Working&quot; to continue.</span>
                    </div>
                    <button
                        type="button"
                        onClick={handleToggleRevealSolution}
                        className="text-amber-800 font-bold underline cursor-pointer text-xs shrink-0 ml-2"
                    >
                        Restore My Working
                    </button>
                </div>
            )}

            {/* Diagram (only rendered here if not already mounted in Question Card, or if interactive diagram_select) */}
            {diagram && (!hideStimulusDiagram || qType === 'diagram_select') ? (
                <DiagramRenderer
                    spec={diagram}
                    interactive={qType === 'diagram_select'}
                    selectedEdge={selectedEdge}
                    onSelectEdge={setSelectedEdge}
                    graded={qType === 'diagram_select' && !!result}
                    correctEdge={result?.correct_edge || question?.correct_edge}
                />
            ) : null}

            {/* Diagram-select prompt hint */}
            {qType === 'diagram_select' ? (
                <p className="text-sm text-slate-500">
                    {selectedEdge ? `Selected side ${selectedEdge}. ` : 'Click a side of the triangle above. '}
                    Then press Check.
                </p>
            ) : null}
            {/* MCQ */}
            {qType === 'mcq' && (
                <div className="space-y-2">
                    {mcqOptionsList.map((opt, i) => {
                        const optLatex = question.options_latex?.[i];
                        const isSel = String(selected) === String(i);
                        return (
                            <button
                                key={i}
                                type="button"
                                data-testid={`btn-math-option-${i}`}
                                onClick={() => setSelected(i)}
                                className={`w-full text-left flex items-center gap-3 rounded-xl border px-4 py-3 transition-all cursor-pointer ${
                                    isSel ? 'border-brand-blue bg-blue-50/70 ring-1 ring-brand-blue text-slate-950 shadow-xs' : 'border-slate-200 bg-white hover:bg-slate-50 text-slate-800'
                                }`}
                            >
                                <span className={`text-xs font-semibold w-5 ${isSel ? 'text-brand-blue font-bold' : 'text-slate-400'}`}>{String.fromCharCode(65 + i)}</span>
                                <MathText text={optLatex || opt} className="text-slate-800" />
                            </button>
                        );
                    })}
                </div>
            )}

            {/* Multi-part short answer (lettered a, b, c) */}
            {isMultiPart && (
                <div className="space-y-3" data-testid="container-multipart-answers">
                    {questionParts.map((part, idx) => {
                        const partLetter = part.letter || String.fromCharCode(97 + idx);
                        return (
                            <div
                                key={part.id || idx}
                                className="rounded-xl border border-slate-200 bg-white p-3.5 shadow-2xs space-y-2 focus-within:border-brand-blue focus-within:ring-2 focus-within:ring-brand-blue/20"
                            >
                                <div className="flex items-center justify-between text-xs font-semibold text-slate-700">
                                    <span className="flex items-center gap-2">
                                        <span className="inline-flex items-center justify-center w-6 h-5 rounded-md bg-blue-100 text-brand-blue text-xs font-mono font-bold shrink-0">
                                            ({partLetter})
                                        </span>
                                        <MathText text={part.label} />
                                    </span>
                                    {part.marks ? (
                                        <span className="text-slate-400 font-mono text-[11px] shrink-0">[{part.marks} mark{part.marks > 1 ? 's' : ''}]</span>
                                    ) : null}
                                </div>
                                <div className="flex items-center gap-3">
                                    <span className="text-xs font-mono font-bold text-slate-500 shrink-0">({partLetter}):</span>
                                    <input
                                        ref={(el) => registerInput(`part-${idx}`, el)}
                                        data-testid={idx === 0 ? "input-math-answer-part-0" : `input-math-answer-part-${idx}`}
                                        value={partValues[idx] || ''}
                                        onChange={(e) => {
                                            const nextParts = [...partValues];
                                            nextParts[idx] = e.target.value;
                                            setPartValues(nextParts);
                                            setValue(nextParts.join('; '));
                                        }}
                                        onFocus={() => onFocusField(`part-${idx}`)}
                                        placeholder={`Type your answer for (${partLetter})…`}
                                        className="flex-1 min-w-0 font-mono text-sm bg-transparent outline-none text-slate-800"
                                        spellCheck={false}
                                    />
                                    <div className="min-w-[4rem] flex justify-end text-slate-700">
                                        {(partValues[idx] || '').trim() ? <MathText latex={latexify(partValues[idx])} /> : null}
                                    </div>
                                </div>
                            </div>
                        );
                    })}
                </div>
            )}

            {/* Single short answer + optional step-by-step working lines */}
            {qType === 'math_short' && !isMultiPart && (
                <div className="space-y-2.5">
                    {showWorkingPad && (
                        <div className="p-3 rounded-xl border border-blue-200/80 bg-blue-50/30 space-y-2">
                            <div className="flex items-center justify-between text-xs">
                                <span className="font-bold text-slate-700 uppercase tracking-wider text-[11px] font-mono">
                                    Step-by-Step Working Pad (LHS = RHS)
                                </span>
                                <button
                                    type="button"
                                    onClick={() => setShowWorkingPad(false)}
                                    className="text-slate-400 hover:text-slate-600 text-[11px] font-semibold cursor-pointer"
                                >
                                    Hide Working Pad
                                </button>
                            </div>
                            <WorkingPad
                                lines={lines}
                                onChange={setLines}
                                statuses={result?.step_statuses}
                                firstErrorStep={result?.first_error_step}
                                registerInput={registerInput}
                                onFocusField={onFocusField}
                            />
                        </div>
                    )}
                    <div className="flex items-center gap-3 rounded-xl border border-slate-200 bg-white px-4 py-2.5 shadow-2xs focus-within:border-brand-blue focus-within:ring-2 focus-within:ring-brand-blue/20">
                        <span className="text-sm font-medium text-slate-500 shrink-0">
                            {showWorkingPad ? 'Final Answer:' : 'Answer:'}
                        </span>
                        <input
                            ref={(el) => registerInput('single', el)}
                            data-testid="input-math-answer"
                            value={value}
                            onChange={(e) => setValue(e.target.value)}
                            onFocus={() => onFocusField('single')}
                            placeholder="Type your answer…"
                            className="flex-1 min-w-0 font-mono text-sm bg-transparent outline-none text-slate-800"
                            spellCheck={false}
                        />
                        <div className="min-w-[5rem] flex justify-end text-slate-700">
                            {value.trim() ? <MathText latex={latexify(value)} /> : null}
                        </div>
                    </div>
                    {!showWorkingPad && !isPureWordResponse && (
                        <div>
                            <button
                                type="button"
                                data-testid="btn-toggle-working-pad"
                                onClick={() => setShowWorkingPad(true)}
                                className="text-xs font-semibold text-[#13519C] hover:text-blue-800 font-sans cursor-pointer flex items-center gap-1"
                            >
                                <span>+ Add step-by-step working lines</span>
                            </button>
                        </div>
                    )}
                </div>
            )}

            {/* Step-by-step working */}
            {qType === 'math_steps' && (
                <WorkingPad
                    lines={lines}
                    onChange={setLines}
                    statuses={result?.step_statuses}
                    firstErrorStep={result?.first_error_step}
                    registerInput={registerInput}
                    onFocusField={onFocusField}
                />
            )}

            {/* Keypad (hidden for MCQ, diagram-select, and pure English word classification answers) */}
            {qType !== 'mcq' && qType !== 'diagram_select' && !isPureWordResponse && (
                <div className="rounded-xl border border-slate-200 bg-slate-50 p-3">
                    <MathKeypad topic={topic} onInsert={handleInsert} disabled={busy} />
                </div>
            )}

            {/* Check + Solution */}
            <div className="flex flex-wrap items-center gap-3">
                <button
                    type="button"
                    data-testid="btn-check-answer"
                    onClick={handleCheck}
                    disabled={checkDisabled}
                    className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold bg-brand-blue text-white hover:bg-brand-cobalt disabled:opacity-50 shadow-sm active:scale-95 cursor-pointer"
                >
                    <CheckCircle2 className="h-4 w-4" />
                    {busy ? 'Checking…' : 'Check'}
                </button>
                {(sol?.steps?.length || sol?.final_latex || question?.correct_answer) ? (
                    <button
                        type="button"
                        data-testid="btn-reveal-math-model"
                        onClick={handleToggleRevealSolution}
                        className={`flex items-center gap-2 px-4 py-2 rounded-xl text-xs font-bold transition shadow-xs cursor-pointer ${
                            showSolution
                                ? 'bg-amber-600 hover:bg-amber-700 text-white'
                                : 'bg-white text-brand-blue border border-brand-blue/30 hover:bg-blue-50'
                        }`}
                    >
                        <Eye className="h-3.5 w-3.5" />
                        <span>{showSolution ? '↩ Restore My Working' : '👁️ Show Model Steps'}</span>
                    </button>
                ) : null}
                {draftSaved && (
                    <span data-testid="draft-offline-sync-badge" className="inline-flex items-center gap-1 text-[11px] font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-200">
                        💾 Draft saved locally
                    </span>
                )}
                {!isOnline && (
                    <span data-testid="draft-offline-mode-badge" className="inline-flex items-center gap-1 text-[11px] font-semibold text-amber-700 bg-amber-50 px-2.5 py-1 rounded-md border border-amber-200">
                        ⚡ Offline Mode
                    </span>
                )}
            </div>

            {/* Feedback */}
            {result && <MarkFeedback result={result} />}
        </div>
    );
};

const MarkFeedback = ({ result }) => {
    const correct = result.is_correct;
    const marks = result.marks;
    return (
        <div className={`rounded-xl border px-4 py-3 ${correct ? 'border-emerald-200 bg-emerald-50' : 'border-amber-200 bg-amber-50'}`}>
            <div className="flex items-center justify-between">
                <span className={`text-sm font-semibold ${correct ? 'text-emerald-800' : 'text-amber-900'}`}>
                    {correct ? 'Correct!' : 'Not quite yet'}
                </span>
                {marks ? (
                    <span className="text-xs font-medium text-slate-600">
                        Method {marks.method} · Accuracy {marks.accuracy} · {marks.awarded}/{marks.max}
                    </span>
                ) : (
                    <span className="text-xs font-medium text-slate-600">{result.score}/{result.max_score}</span>
                )}
            </div>
            {Number.isInteger(result.first_error_step) && (
                <p className="mt-1 text-sm text-amber-900">
                    First slip on line {result.first_error_step + 1}
                    {result.error_type ? ` — ${String(result.error_type).replace(/_/g, ' ')}` : ''}.
                </p>
            )}
            {!correct && result.feedback ? <p className="mt-1 text-sm text-slate-600">{result.feedback}</p> : null}
        </div>
    );
};

export default MathAnswerArea;
