import React from 'react';

const MCQRenderer = ({ question, answer, setAnswer, feedback }) => {
    if (!question || question.question_type !== 'mcq') return null;

    return (
        <div className="space-y-4">
            <div className="grid grid-cols-1 gap-2">
                {(question.options || []).map((opt, idx) => (
                    <div
                        key={idx}
                        onClick={() => setAnswer(String(idx))}
                        className={`p-3 border rounded-xl cursor-pointer transition-all ${String(answer) === String(idx)
                                ? 'bg-slate-50 border-slate-800 ring-1 ring-slate-800'
                                : 'bg-white border-slate-200 hover:bg-slate-50'
                            }`}
                    >
                        <div className="flex items-center gap-3">
                            <div className={`w-4 h-4 rounded-full border ${String(answer) === String(idx)
                                    ? 'border-slate-800 bg-slate-800'
                                    : 'border-slate-300'
                                }`} />
                            <span className="text-sm text-slate-700">{opt}</span>
                        </div>
                    </div>
                ))}
            </div>
            {feedback && (
                <div className={`mt-3 p-3 rounded-lg text-sm ${feedback.kind === 'success' ? 'bg-green-50 text-green-800 border border-green-200' :
                        feedback.kind === 'error' ? 'bg-red-50 text-red-800 border border-red-200' :
                            'bg-blue-50 text-blue-800 border border-blue-200'
                    }`}>
                    {feedback.message}
                </div>
            )}
        </div>
    );
};

export default MCQRenderer;
