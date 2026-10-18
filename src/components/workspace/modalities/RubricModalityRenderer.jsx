import React, { useState, useEffect, useMemo } from 'react';
import { CheckCircle2, AlertCircle, Sparkles } from 'lucide-react';

function extractMarkingPoints(question) {
    if (!question) return [];

    // 1. Explicit marking_schema.marking_points
    if (Array.isArray(question.marking_schema?.marking_points) && question.marking_schema.marking_points.length > 0) {
        return question.marking_schema.marking_points.map((mp, i) => ({
            id: mp.id || `mp_${i + 1}`,
            title: mp.title || `Point ${i + 1}`,
            desc: mp.desc || mp.point || mp.description || '',
            marks: Number(mp.marks) || 1,
            concepts: mp.concepts || mp.target_concepts || []
        }));
    }

    // 2. Direct marking_points array
    if (Array.isArray(question.marking_points) && question.marking_points.length > 0) {
        return question.marking_points.map((mp, i) => {
            if (typeof mp === 'string') {
                const markMatch = mp.match(/\[(\d+)\s*(?:marks?|mark)?\]/i);
                const marks = markMatch ? parseInt(markMatch[1], 10) : 1;
                return {
                    id: `mp_${i + 1}`,
                    title: `Point ${i + 1}`,
                    desc: mp.replace(/\[\d+\s*(?:marks?|mark)?\]/i, '').trim(),
                    marks,
                    concepts: []
                };
            }
            return {
                id: mp.id || `mp_${i + 1}`,
                title: mp.title || `Point ${i + 1}`,
                desc: mp.desc || mp.point || mp.description || '',
                marks: Number(mp.marks) || 1,
                concepts: mp.concepts || []
            };
        });
    }

    // 3. Content rubric (e.g. Grade 12 essays)
    if (Array.isArray(question.content_rubric) && question.content_rubric.length > 0) {
        return question.content_rubric.map((cr, i) => ({
            id: `cr_${i + 1}`,
            title: cr.criterion || `Criterion ${i + 1}`,
            desc: Array.isArray(cr.key_concepts) ? `Key aspects: ${cr.key_concepts.join(', ')}` : (cr.desc || ''),
            marks: Number(cr.max_marks) || 2,
            concepts: cr.key_concepts || []
        }));
    }

    // 4. Parts array (e.g. compound questions with sub-parts)
    if (Array.isArray(question.parts) && question.parts.length > 0) {
        return question.parts.map((p, i) => ({
            id: p.id || `p_${i + 1}`,
            title: p.title || `Part ${p.id || i + 1}`,
            desc: p.question || p.rubric || p.desc || '',
            marks: Number(p.marks) || 2,
            concepts: p.concepts || []
        }));
    }

    // 5. Default generated marking points based on marks allocation
    const totalMarks = Number(question.marks) || 6;
    if (totalMarks <= 2) {
        return [{ id: 'mp_1', title: 'Point 1', desc: 'Accurate identification, definition, or statement of core concept', marks: totalMarks, concepts: [] }];
    } else if (totalMarks <= 4) {
        return [
            { id: 'mp_1', title: 'Point 1', desc: 'Identification and definition of statutory / core concept', marks: Math.floor(totalMarks / 2), concepts: [] },
            { id: 'mp_2', title: 'Point 2', desc: 'Applied analysis, impact, or operational explanation', marks: Math.ceil(totalMarks / 2), concepts: [] }
        ];
    } else {
        return [
            { id: 'mp_1', title: 'Point 1', desc: 'Identification of core concept and framework', marks: 2, concepts: [] },
            { id: 'mp_2', title: 'Point 2', desc: 'In-depth impact analysis on relevant stakeholders or system', marks: 2, concepts: [] },
            { id: 'mp_3', title: 'Point 3', desc: 'Practical mitigation, evaluation, or management recommendation', marks: Math.max(1, totalMarks - 4), concepts: [] }
        ];
    }
}

export default function RubricModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
}) {
    if (!question) return null;

    const [selectedKeywords, setSelectedKeywords] = useState([]);
    const [learnerExplanation, setLearnerExplanation] = useState('');
    const [revealedModel, setRevealedModel] = useState(false);
    const [savedLearnerState, setSavedLearnerState] = useState(null);

    // Dynamic marking points
    const markingPoints = useMemo(() => extractMarkingPoints(question), [question]);

    // Concept keywords (only present if question or marking points explicitly define them)
    const keywords = useMemo(() => {
        if (Array.isArray(question.key_concepts) && question.key_concepts.length > 0) return question.key_concepts;
        if (Array.isArray(question.keywords) && question.keywords.length > 0) return question.keywords;
        if (Array.isArray(question.correct_keywords) && question.correct_keywords.length > 0) return question.correct_keywords;
        
        // Extract unique concepts from marking points if available
        const extracted = [];
        markingPoints.forEach(mp => {
            if (Array.isArray(mp.concepts)) {
                mp.concepts.forEach(c => {
                    if (c && !extracted.includes(c)) extracted.push(c);
                });
            }
        });
        return extracted;
    }, [question, markingPoints]);

    const hasKeywords = keywords.length > 0;
    const modelKeywords = question.correct_keywords || question.model_keywords || keywords;
    const modelExplanation = question.model_answer || question.ideal_answer || question.sample_response || question.solution || question.explanation || '';

    useEffect(() => {
        setSelectedKeywords([]);
        setLearnerExplanation('');
        setRevealedModel(false);
        setSavedLearnerState(null);
    }, [question?.id]);

    const toggleKeyword = (kw) => {
        if (revealedModel) return;
        setSelectedKeywords(prev =>
            prev.includes(kw) ? prev.filter(k => k !== kw) : [...prev, kw]
        );
    };

    const handleToggleRevealModel = () => {
        if (!revealedModel) {
            setSavedLearnerState({
                keywords: [...selectedKeywords],
                explanation: learnerExplanation,
            });
            if (Array.isArray(modelKeywords) && modelKeywords.length > 0) {
                setSelectedKeywords([...modelKeywords]);
            }
            if (modelExplanation) {
                setLearnerExplanation(modelExplanation);
            }
            setRevealedModel(true);
        } else {
            if (savedLearnerState) {
                setSelectedKeywords(savedLearnerState.keywords || []);
                setLearnerExplanation(savedLearnerState.explanation || '');
            }
            setRevealedModel(false);
        }
    };

    const handleCheckSubmission = () => {
        if (onCheck) {
            onCheck({
                keywords: selectedKeywords,
                explanation: learnerExplanation
            });
        }
    };

    // Determine awarded points from result if provided
    const awardedPointIds = useMemo(() => {
        if (!result) return [];
        if (Array.isArray(result.awarded_points)) {
            return result.awarded_points.map(p => (typeof p === 'object' ? p.id : p));
        }
        if (result.is_correct) {
            return markingPoints.map(p => p.id);
        }
        // If partial score, approximate awarded points based on ratio
        const score = result.score || 0;
        const total = result.total || result.max_score || question.marks || 1;
        const count = Math.round((score / total) * markingPoints.length);
        return markingPoints.slice(0, count).map(p => p.id);
    }, [result, markingPoints, question.marks]);

    return (
        <div className="space-y-6">
            {/* Model Response Active Banner */}
            {revealedModel && (
                <div data-testid="banner-rubric-model-active" className="p-2.5 rounded-xl bg-amber-50 border border-amber-300 text-xs text-amber-900 flex items-center justify-between shadow-2xs font-sans">
                    <div className="flex items-center gap-2">
                        <span className="font-bold">📖 Model Response Displayed:</span>
                        <span>Studying expected concept selection and analytical structure. Click &quot;Restore My Response&quot; to continue.</span>
                    </div>
                    <button
                        type="button"
                        onClick={handleToggleRevealModel}
                        className="text-amber-800 font-bold underline cursor-pointer text-xs shrink-0 ml-2"
                    >
                        Restore My Response
                    </button>
                </div>
            )}

            {/* Dynamic Rubric Scaffold Guidance */}
            <div className="rounded-2xl border border-blue-200 bg-blue-50/60 p-4 transition-all">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="grid place-items-center h-6 w-6 rounded-lg bg-brand-blue text-white text-xs font-bold">
                            💡
                        </span>
                        <span className="text-sm font-bold text-brand-blue">
                            Exam Rubric &amp; Marking Points Criteria
                        </span>
                    </div>
                    <button
                        type="button"
                        data-testid="btn-toggle-rubric-scaffold"
                        onClick={onToggleScaffold}
                        className="text-xs font-bold text-brand-blue hover:underline cursor-pointer"
                    >
                        {showDynamicScaffold ? 'Hide Criteria ▲' : 'Show Rubric Criteria ▼'}
                    </button>
                </div>

                {showDynamicScaffold && (
                    <div className="mt-3 pt-3 border-t border-blue-100 text-xs text-slate-700 space-y-2">
                        <p className="font-semibold text-slate-800 uppercase tracking-wider text-[11px]">
                            Official Examination Marking Points Allocation:
                        </p>
                        <div className="space-y-1.5">
                            {markingPoints.map((mp, idx) => (
                                <div
                                    key={mp.id || idx}
                                    className={`flex items-start justify-between gap-3 p-2 rounded-lg border text-xs transition ${
                                        revealedModel
                                            ? 'bg-amber-50/80 border-amber-200 text-amber-900'
                                            : Boolean(result) && awardedPointIds.includes(mp.id)
                                                ? 'bg-emerald-50/80 border-emerald-200 text-emerald-900'
                                                : 'bg-white border-blue-100 text-slate-800'
                                    }`}
                                >
                                    <div className="flex items-start gap-2 flex-1">
                                        <span className="font-bold font-mono text-[#13519C] shrink-0">
                                            {mp.title || `Point ${idx + 1}`}:
                                        </span>
                                        <span>{mp.desc}</span>
                                    </div>
                                    <span className="shrink-0 px-2 py-0.5 rounded-md font-mono font-bold text-[11px] bg-blue-100/80 text-[#13519C] border border-blue-200">
                                        {mp.marks} mark{mp.marks > 1 ? 's' : ''}
                                    </span>
                                </div>
                            ))}
                        </div>
                    </div>
                )}
            </div>

            {/* Keyword Concept Chips (Rendered only when question or topic has explicit concepts) */}
            {hasKeywords && (
                <div className="space-y-2">
                    <label className="block text-xs font-bold text-slate-700 uppercase tracking-wide">
                        Select Applicable Core Concepts:
                    </label>
                    <div className="flex flex-wrap gap-2">
                        {keywords.map((kw, idx) => {
                            const isSelected = selectedKeywords.includes(kw);
                            return (
                                <button
                                    key={idx}
                                    type="button"
                                    data-testid={`btn-rubric-keyword-${idx}`}
                                    data-keyword={kw}
                                    onClick={() => toggleKeyword(kw)}
                                    className={`px-3 py-1.5 rounded-full text-xs font-semibold border transition cursor-pointer ${
                                        revealedModel && modelKeywords.includes(kw)
                                            ? 'bg-amber-500 text-white border-amber-600 shadow-xs'
                                            : isSelected
                                                ? 'bg-brand-blue text-white border-brand-blue shadow-xs'
                                                : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
                                    }`}
                                >
                                    {kw}
                                </button>
                            );
                        })}
                    </div>
                </div>
            )}

            {/* Written Analysis Input */}
            <div className="space-y-2">
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wide">
                    Your Applied Analysis &amp; Explanation:
                </label>
                <textarea
                    rows={4}
                    data-testid="input-rubric-explanation"
                    value={learnerExplanation}
                    onChange={(e) => {
                        if (!revealedModel) setLearnerExplanation(e.target.value);
                    }}
                    placeholder="Formulate your analytical response referencing the required criteria and concepts..."
                    className={`w-full p-3 rounded-xl border text-xs leading-relaxed outline-none transition ${
                        revealedModel
                            ? 'bg-amber-50/90 border-amber-400 text-amber-950 font-medium ring-1 ring-amber-300'
                            : 'bg-white border-slate-200 focus:border-brand-blue focus:ring-1 focus:ring-brand-blue'
                    }`}
                />
            </div>

            {/* Marking Points Achievement Ledger (After Evaluation) */}
            {Boolean(result) && (
                <div className="rounded-xl border border-slate-200 bg-white p-3 space-y-2 text-xs shadow-2xs font-sans">
                    <div className="flex items-center justify-between pb-1.5 border-b border-slate-100">
                        <span className="font-bold text-slate-800 uppercase tracking-wider text-[11px] flex items-center gap-1.5">
                            <Sparkles className="w-3.5 h-3.5 text-brand-blue" />
                            Marking Points Evaluator Breakdown
                        </span>
                        <span className="font-mono font-bold text-[#13519C]">
                            {result.score ?? 0} / {result.total ?? question.marks ?? 6} Marks
                        </span>
                    </div>
                    <div className="space-y-1">
                        {markingPoints.map((mp, idx) => {
                            const isAwarded = awardedPointIds.includes(mp.id);
                            return (
                                <div
                                    key={mp.id || idx}
                                    className={`flex items-start justify-between gap-2 p-1.5 rounded-lg border text-xs ${
                                        isAwarded
                                            ? 'bg-emerald-50/60 border-emerald-200 text-emerald-900'
                                            : 'bg-amber-50/40 border-amber-200 text-amber-900'
                                    }`}
                                >
                                    <div className="flex items-start gap-1.5">
                                        {isAwarded ? (
                                            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                                        ) : (
                                            <AlertCircle className="w-3.5 h-3.5 text-amber-600 shrink-0 mt-0.5" />
                                        )}
                                        <div>
                                            <span className="font-bold font-mono">Point {idx + 1}: </span>
                                            <span>{mp.desc}</span>
                                        </div>
                                    </div>
                                    <span className={`shrink-0 font-bold font-mono text-[11px] ${isAwarded ? 'text-emerald-700' : 'text-amber-700'}`}>
                                        {isAwarded ? `+${mp.marks}` : `0/${mp.marks}`}
                                    </span>
                                </div>
                            );
                        })}
                    </div>
                </div>
            )}

            {/* Actions Bar */}
            <div className="flex flex-wrap items-center justify-between gap-2 pt-1">
                <div>
                    {Boolean(result) && (modelExplanation || modelKeywords.length > 0) && (
                        <button
                            type="button"
                            data-testid="btn-reveal-rubric-model"
                            onClick={handleToggleRevealModel}
                            className={`px-3.5 py-2 rounded-xl text-xs font-bold transition shadow-xs cursor-pointer flex items-center gap-1.5 font-sans ${
                                revealedModel
                                    ? 'bg-amber-600 hover:bg-amber-700 text-white'
                                    : 'bg-white text-[#13519C] border border-[#13519C]/40 hover:bg-blue-50'
                            }`}
                        >
                            <span>{revealedModel ? '↩ Restore My Response' : '👁️ Show Model Response'}</span>
                        </button>
                    )}
                </div>
                <button
                    type="button"
                    data-testid="btn-check-answer"
                    onClick={handleCheckSubmission}
                    disabled={isChecking}
                    className="px-5 py-2 rounded-xl text-xs font-bold bg-[#13519C] hover:bg-blue-800 text-white transition shadow-xs cursor-pointer disabled:opacity-50 active:scale-98 font-sans"
                >
                    {isChecking ? 'Evaluating...' : 'Submit Analysis'}
                </button>
            </div>
        </div>
    );
}

