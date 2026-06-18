import React from 'react';

const TypedRenderer = ({ question, answer, setAnswer, feedback }) => {
    if (!question || question.question_type !== 'typed') return null;

    return (
        <div className="space-y-4">
            <div className="mt-3">
                <textarea
                    className="w-full p-3 border border-slate-200 rounded-xl focus:outline-none focus:ring-2 focus:ring-slate-400 min-h-[100px]"
                    placeholder="Type your answer here..."
                    value={answer || ''}
                    onChange={(e) => setAnswer(e.target.value)}
                />
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

export default TypedRenderer;
