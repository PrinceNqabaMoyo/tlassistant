import React, { useState } from 'react';

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
    const keywords = question.key_concepts || question.keywords || ['B-BBEE', 'Macro Environment', 'LRA', 'Corporate Governance', 'Ethics', 'Market Share'];

    const toggleKeyword = (kw) => {
        setSelectedKeywords(prev =>
            prev.includes(kw) ? prev.filter(k => k !== kw) : [...prev, kw]
        );
    };

    const handleCheckSubmission = () => {
        if (onCheck) {
            onCheck({
                keywords: selectedKeywords,
                explanation: learnerExplanation
            });
        }
    };

    return (
        <div className="space-y-6">
            {/* Dynamic Rubric Scaffold Guidance */}
            <div className="rounded-2xl border border-blue-200 bg-blue-50/60 p-4 transition-all">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="grid place-items-center h-6 w-6 rounded-lg bg-brand-blue text-white text-xs font-bold">
                            💡
                        </span>
                        <span className="text-sm font-bold text-brand-blue">
                            Exam Rubric &amp; Concept Criteria
                        </span>
                    </div>
                    <button
                        type="button"
                        onClick={onToggleScaffold}
                        className="text-xs font-bold text-brand-blue hover:underline cursor-pointer"
                    >
                        {showDynamicScaffold ? 'Hide Criteria ▲' : 'Show Rubric Criteria ▼'}
                    </button>
                </div>

                {showDynamicScaffold && (
                    <div className="mt-3 pt-3 border-t border-blue-100 text-xs text-slate-700 space-y-1">
                        <p className="font-semibold text-slate-800">Scoring Criteria:</p>
                        <p>• Identification of core business statutory framework: <strong>2 marks</strong></p>
                        <p>• Impact analysis on relevant stakeholder: <strong>2 marks</strong></p>
                        <p>• Practical mitigation or management recommendation: <strong>2 marks</strong></p>
                    </div>
                )}
            </div>

            {/* Keyword Concept Chips */}
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
                                onClick={() => toggleKeyword(kw)}
                                className={`px-3 py-1.5 rounded-full text-xs font-semibold border transition cursor-pointer ${
                                    isSelected
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

            {/* Written Analysis Input */}
            <div className="space-y-2">
                <label className="block text-xs font-bold text-slate-700 uppercase tracking-wide">
                    Your Applied Analysis &amp; Recommendation:
                </label>
                <textarea
                    rows={4}
                    value={learnerExplanation}
                    onChange={(e) => setLearnerExplanation(e.target.value)}
                    placeholder="Formulate your analytical response referencing the selected concepts..."
                    className="w-full p-3 rounded-xl border border-slate-200 focus:border-brand-blue focus:ring-1 focus:ring-brand-blue outline-none text-xs leading-relaxed"
                />
            </div>

            <div className="flex justify-end">
                <button
                    type="button"
                    onClick={handleCheckSubmission}
                    disabled={isChecking}
                    className="px-5 py-2.5 rounded-xl text-sm font-semibold bg-brand-blue text-white hover:bg-brand-cobalt transition shadow-xs cursor-pointer"
                >
                    {isChecking ? 'Evaluating...' : 'Submit Analysis'}
                </button>
            </div>
        </div>
    );
}
