import React, { useState, useEffect } from 'react';
import { LightbulbIcon, CheckCircleIcon, XCircleIcon } from 'lucide-react';

export const BSEssayRenderer = ({ question, answer, setAnswer, readOnly }) => {
    const rubric = question?.rubric || [];
    const minWords = question?.min_words || 150;
    const maxWords = question?.max_words || 400;

    const [showPlan, setShowPlan] = useState(false);
    const [text, setText] = useState(answer || '');

    useEffect(() => {
        if (answer !== text) setText(answer || '');
        // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [question?.id]);

    const wordCount = text.trim().split(/\s+/).filter(Boolean).length;

    const handleChange = (e) => {
        if (readOnly) return;
        const val = e.target.value;
        setText(val);
        setAnswer(val);
    };

    let countColor = 'text-slate-500';
    if (wordCount < minWords) countColor = 'text-amber-600';
    else if (wordCount > maxWords) countColor = 'text-rose-600';
    else countColor = 'text-emerald-600';

    return (
        <div className="space-y-4">
            {/* Meta */}
            <div className="flex flex-wrap items-center justify-between gap-3">
                <div className="text-xs font-semibold text-slate-500 uppercase tracking-wide">
                    Essay • {question?.marks || 20} marks
                </div>
                <div className={`text-xs font-bold ${countColor}`}>
                    {wordCount} / {minWords}–{maxWords} words
                </div>
            </div>

            {/* Planning toggle */}
            {!readOnly && (
                <button
                    onClick={() => setShowPlan((s) => !s)}
                    className="flex items-center gap-2 text-sm font-medium text-indigo-700 hover:text-indigo-800 transition-colors"
                >
                    <LightbulbIcon className="w-4 h-4" />
                    {showPlan ? 'Hide Planning Guide' : 'Show Planning Guide'}
                </button>
            )}

            {showPlan && (
                <div className="p-4 bg-amber-50 border border-amber-200 rounded-xl text-sm text-amber-900 space-y-2 animate-in fade-in slide-in-from-top-2">
                    <p className="font-semibold">Essay structure guide:</p>
                    <ul className="list-disc list-inside space-y-1 text-amber-800">
                        <li><strong>Introduction:</strong> Define key terms and state your main argument.</li>
                        <li><strong>Body:</strong> Develop 2–4 points with examples. Each paragraph = one idea.</li>
                        <li><strong>Conclusion:</strong> Summarise and give a final evaluative statement.</li>
                    </ul>
                </div>
            )}

            {/* Textarea */}
            <textarea
                disabled={readOnly}
                className="w-full p-4 border-2 border-slate-200 rounded-xl focus:border-indigo-500 focus:ring-4 focus:ring-indigo-500/20 transition-all duration-200 text-slate-700 min-h-[250px] disabled:bg-slate-50 disabled:text-slate-500 resize-y"
                placeholder="Type your essay here..."
                value={text}
                onChange={handleChange}
            />

            {/* Keyword-highlighted text display (memo mode) */}
            {readOnly && text && (
                <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl">
                    <div className="text-xs font-semibold text-slate-500 uppercase tracking-wide mb-2">
                        Keyword check
                    </div>
                    <div className="text-sm text-slate-700 leading-relaxed whitespace-pre-wrap">
                        {(() => {
                            // Collect all rubric keywords
                            const allKeywords = new Set();
                            rubric.forEach(crit => {
                                (crit.description || '')
                                    .toLowerCase()
                                    .replace(/[^a-z0-9\s]/g, ' ')
                                    .split(/\s+/)
                                    .filter(w => w.length > 4)
                                    .forEach(w => allKeywords.add(w));
                            });
                            const keywords = Array.from(allKeywords);
                            if (keywords.length === 0) return text;

                            // Build highlighted spans
                            const textLower = text.toLowerCase();
                            const result = [];
                            let lastIndex = 0;
                            // Find all keyword positions
                            const matches = [];
                            keywords.forEach(kw => {
                                let pos = textLower.indexOf(kw);
                                while (pos !== -1) {
                                    matches.push({ start: pos, end: pos + kw.length, kw });
                                    pos = textLower.indexOf(kw, pos + 1);
                                }
                            });
                            // Sort by start, dedupe overlapping
                            matches.sort((a, b) => a.start - b.start || b.end - a.end);
                            const deduped = [];
                            matches.forEach(m => {
                                if (deduped.length === 0 || m.start >= deduped[deduped.length - 1].end) {
                                    deduped.push(m);
                                }
                            });
                            deduped.forEach(m => {
                                if (m.start > lastIndex) {
                                    result.push(<span key={`t${lastIndex}`}>{text.slice(lastIndex, m.start)}</span>);
                                }
                                result.push(
                                    <mark key={`h${m.start}`} className="bg-amber-100 text-amber-900 rounded px-0.5">
                                        {text.slice(m.start, m.end)}
                                    </mark>
                                );
                                lastIndex = m.end;
                            });
                            if (lastIndex < text.length) {
                                result.push(<span key={`t${lastIndex}`}>{text.slice(lastIndex)}</span>);
                            }
                            return result.length > 0 ? result : text;
                        })()}
                    </div>
                </div>
            )}

            {/* Rubric display (read-only / after marking) */}
            {readOnly && rubric.length > 0 && (
                <div className="p-4 bg-white border border-slate-200 rounded-xl space-y-3">
                    <h4 className="text-sm font-semibold text-slate-700">Rubric</h4>
                    <div className="space-y-2">
                        {rubric.map((crit, idx) => {
                            const descWords = (crit.description || '')
                                .toLowerCase()
                                .replace(/[^a-z0-9\s]/g, ' ')
                                .split(/\s+/)
                                .filter(w => w.length > 4);
                            const textLower = text.toLowerCase();
                            const hitCount = descWords.filter(w => textLower.includes(w)).length;
                            const coverage = descWords.length > 0 ? hitCount / descWords.length : 0;
                            const isMet = coverage >= 0.3;
                            return (
                                <div
                                    key={idx}
                                    className={`flex items-start justify-between gap-3 p-3 rounded-lg border transition-all duration-300 ${
                                        isMet
                                            ? 'bg-emerald-50 border-emerald-200'
                                            : 'bg-red-50 border-red-200'
                                    }`}
                                >
                                    <div className="flex-1">
                                        <div className="flex items-center gap-2">
                                            {isMet ? (
                                                <CheckCircleIcon className="w-4 h-4 text-emerald-600" />
                                            ) : (
                                                <XCircleIcon className="w-4 h-4 text-red-500" />
                                            )}
                                            <div className="text-sm font-medium text-slate-800">
                                                {crit.criterion || `Criterion ${idx + 1}`}
                                            </div>
                                        </div>
                                        <div className="text-xs text-slate-500 mt-0.5 ml-6">
                                            {crit.description || ''}
                                        </div>
                                    </div>
                                    <div className={`text-xs font-bold whitespace-nowrap ${isMet ? 'text-emerald-700' : 'text-red-600'}`}>
                                        {crit.marks || 1} mark{crit.marks !== 1 ? 's' : ''}
                                    </div>
                                </div>
                            );
                        })}
                    </div>
                </div>
            )}
        </div>
    );
};

export default BSEssayRenderer;
