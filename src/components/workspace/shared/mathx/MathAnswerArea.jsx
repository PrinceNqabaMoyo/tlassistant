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
 * MathAnswerArea — renders the answer interaction for a maths question
 * (mcq / math_short / math_steps), wires the keypad to the focused field, and
 * shows the marking feedback the procedure tracker returns.
 *
 * Props:
 *   question   the generated question
 *   topic      topic key (selects the keypad groups)
 *   onCheck(answer) -> Promise<result>   marks the answer
 *   result     last marking result (for rendering feedback)
 *   busy       marking in flight
 */
const MathAnswerArea = ({ question, topic, onCheck, result, busy = false }) => {
    const qType = question?.question_type ||
        ((question?.options || question?.options_latex) ? 'mcq' :
        (question?.diagram_spec ? 'diagram_select' :
        (question?.canonical_solution?.steps?.length > 1 ? 'math_steps' : 'math_short')));
    const mathStorageKey = question?.id ? `fundile_draft_math_${question.id}` : null;
    const offlineStorageKey = question?.id ? `fundile_offline_draft_math_${question.id}` : null;

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
    const activeField = React.useRef(qType === 'math_short' ? 'single' : 'line-0');

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
                        setShowSolution(false);
                        setDraftSaved(true);
                        activeField.current = qType === 'math_short' ? 'single' : 'line-0';
                        return;
                    }
                }
                if (offlineStorageKey) {
                    const savedLocal = localStorage.getItem(offlineStorageKey);
                    if (savedLocal) {
                        const parsed = JSON.parse(savedLocal);
                        setValue(parsed.value || '');
                        setLines(parsed.lines || ['']);
                        setShowSolution(false);
                        setDraftSaved(true);
                        if (mathStorageKey) {
                            try { sessionStorage.setItem(mathStorageKey, JSON.stringify(parsed)); } catch (e) {}
                        }
                        activeField.current = qType === 'math_short' ? 'single' : 'line-0';
                        return;
                    }
                }
            } catch (e) {}
        }
        setValue('');
        setLines(['']);
        setShowSolution(false);
        setDraftSaved(false);
        activeField.current = qType === 'math_short' ? 'single' : 'line-0';
    }, [question?.id, qType, mathStorageKey, offlineStorageKey]);

    // Persist draft in sessionStorage and localStorage as learner inputs math
    React.useEffect(() => {
        if (typeof window !== 'undefined') {
            const hasContent = Boolean(value || (lines.length > 1 || lines[0]));
            if (hasContent) {
                const payload = JSON.stringify({ value, lines, updatedAt: Date.now() });
                if (mathStorageKey) {
                    try { sessionStorage.setItem(mathStorageKey, payload); } catch (e) {}
                }
                if (offlineStorageKey) {
                    try { localStorage.setItem(offlineStorageKey, payload); } catch (e) {}
                }
                setDraftSaved(true);
            }
        }
    }, [value, lines, mathStorageKey, offlineStorageKey]);

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
        if (id === 'single') {
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

    const handleCheck = () => {
        if (qType === 'mcq') onCheck?.(selected);
        else if (qType === 'diagram_select') onCheck?.(selectedEdge);
        else if (qType === 'math_short') onCheck?.(value);
        else onCheck?.(lines.filter((l) => l.trim()));
    };

    const sol = question?.canonical_solution;
    const diagram = question?.diagram_spec;
    const checkDisabled = busy || (qType === 'diagram_select' && !selectedEdge && !result);

    const handleToggleRevealSolution = () => {
        if (!showSolution) {
            setSavedLearnerWorking({
                value,
                lines: [...lines],
                selected,
                selectedEdge,
            });
            if (qType === 'math_steps' && sol?.steps?.length) {
                setLines(sol.steps.map((st) => st.to_latex || st.step || ''));
            } else if (qType === 'math_short') {
                setValue(sol?.final_latex || question?.correct_answer || '');
            } else if (qType === 'mcq' && question?.correct_index !== undefined) {
                setSelected(question.correct_index);
            } else if (qType === 'diagram_select' && (question?.correct_edge || result?.correct_edge)) {
                setSelectedEdge(question?.correct_edge || result?.correct_edge);
            }
            setShowSolution(true);
        } else {
            if (savedLearnerWorking) {
                setValue(savedLearnerWorking.value || '');
                setLines(savedLearnerWorking.lines || ['']);
                setSelected(savedLearnerWorking.selected ?? null);
                setSelectedEdge(savedLearnerWorking.selectedEdge ?? null);
            }
            setShowSolution(false);
        }
    };

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

            {/* Diagram (the figure is the question/answer surface) */}
            {diagram ? (
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
                    {(question.options || []).map((opt, i) => {
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
                                {optLatex ? <MathText latex={optLatex} /> : <span className="text-slate-800">{opt}</span>}
                            </button>
                        );
                    })}
                </div>
            )}

            {/* Single short answer */}
            {qType === 'math_short' && (
                <div className="space-y-2">
                    <div className="flex items-center gap-3 rounded-xl border border-slate-200 bg-white px-4 py-2.5 shadow-2xs focus-within:border-brand-blue focus-within:ring-2 focus-within:ring-brand-blue/20">
                        <span className="text-sm font-medium text-slate-500 shrink-0">Answer:</span>
                        <input
                            ref={(el) => registerInput('single', el)}
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

            {/* Keypad (not for MCQ / diagram-select) */}
            {qType !== 'mcq' && qType !== 'diagram_select' && (
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
