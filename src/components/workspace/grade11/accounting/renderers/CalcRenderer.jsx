import React from 'react';

const CalcRenderer = ({ question, answer, setAnswer, feedback, isMarkingEnv = false }) => {
    if (!question || question.question_type !== 'calc') return null;

    return (
        <div className="space-y-4">
            <div className="mt-3">
                <div className="flex items-center gap-2">
                    {question.unit && <span className="text-slate-500 font-medium">{question.unit}</span>}
                    <input
                        type="number"
                        step="0.01"
                        className="w-full max-w-xs p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400"
                        placeholder="0.00"
                        value={answer || ''}
                        onChange={(e) => setAnswer(e.target.value)}
                    />
                </div>
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

export default CalcRenderer;
