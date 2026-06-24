import React from 'react';
import { CheckCircle2, Eye } from 'lucide-react';
import MathText from './MathText';
import MathKeypad from './MathKeypad';
import WorkingPad from './WorkingPad';
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
    const qType = question?.question_type;
    const [selected, setSelected] = React.useState(null);
    const [value, setValue] = React.useState('');
    const [lines, setLines] = React.useState(['']);
    const [showSolution, setShowSolution] = React.useState(false);
    const inputs = React.useRef({});
    const activeField = React.useRef(qType === 'math_short' ? 'single' : 'line-0');

    React.useEffect(() => {
        setSelected(null);
        setValue('');
        setLines(['']);
        setShowSolution(false);
        activeField.current = qType === 'math_short' ? 'single' : 'line-0';
    }, [question?.id, qType]);

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
        else if (qType === 'math_short') onCheck?.(value);
        else onCheck?.(lines.filter((l) => l.trim()));
    };

    const sol = question?.canonical_solution;

    return (
        <div className="space-y-5">
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
                                onClick={() => setSelected(i)}
                                className={`w-full text-left flex items-center gap-3 rounded-xl border px-4 py-3 transition-colors ${
                                    isSel ? 'border-indigo-400 bg-indigo-50' : 'border-slate-200 bg-white hover:bg-slate-50'
                                }`}
                            >
                                <span className="text-xs font-semibold text-slate-400 w-5">{String.fromCharCode(65 + i)}</span>
                                {optLatex ? <MathText latex={optLatex} /> : <span className="text-slate-800">{opt}</span>}
                            </button>
                        );
                    })}
                </div>
            )}

            {/* Single short answer */}
            {qType === 'math_short' && (
                <div className="space-y-2">
                    <div className="flex items-center gap-3 rounded-lg border border-slate-200 bg-white px-3 py-2">
                        <span className="text-sm text-slate-500 shrink-0">Answer:</span>
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

            {/* Keypad (not for MCQ) */}
            {qType !== 'mcq' && (
                <div className="rounded-xl border border-slate-100 bg-slate-50 p-3">
                    <MathKeypad topic={topic} onInsert={handleInsert} disabled={busy} />
                </div>
            )}

            {/* Check + Solution */}
            <div className="flex flex-wrap gap-3">
                <button
                    type="button"
                    onClick={handleCheck}
                    disabled={busy}
                    className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold bg-indigo-600 text-white hover:bg-indigo-700 disabled:opacity-50 shadow-sm active:scale-95"
                >
                    <CheckCircle2 className="h-4 w-4" />
                    {busy ? 'Checking…' : 'Check'}
                </button>
                {sol?.steps?.length ? (
                    <button
                        type="button"
                        onClick={() => setShowSolution((v) => !v)}
                        className="flex items-center gap-2 px-5 py-2.5 rounded-xl text-sm font-semibold bg-white text-slate-700 border border-slate-300 hover:bg-slate-100 active:scale-95"
                    >
                        <Eye className="h-4 w-4" />
                        {showSolution ? 'Hide solution' : 'Show worked solution'}
                    </button>
                ) : null}
            </div>

            {/* Feedback */}
            {result && <MarkFeedback result={result} />}

            {/* Worked solution */}
            {showSolution && sol?.steps?.length ? (
                <div className="rounded-xl border border-slate-200 bg-white p-4 space-y-2">
                    <p className="text-xs font-semibold uppercase tracking-wide text-slate-500">Worked solution</p>
                    {sol.steps.map((st, i) => (
                        <div key={i} className="flex items-start gap-2 text-sm">
                            <span className="text-slate-400 w-5">{i + 1}.</span>
                            <div>
                                <MathText latex={st.to_latex} />
                                {st.op ? <span className="ml-2 text-xs text-slate-400">({st.op})</span> : null}
                            </div>
                        </div>
                    ))}
                    <div className="pt-2 border-t border-slate-100 text-sm font-semibold text-slate-800">
                        <MathText latex={sol.final_latex} />
                    </div>
                </div>
            ) : null}
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
