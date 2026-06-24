import React, { useState, useEffect, useRef } from 'react';

export const BSCrosswordGrid = ({ question, answer, setAnswer, readOnly }) => {
    const words = question?.words || [];
    const clues = question?.clues || {};

    // answer shape: { word: "STUDENT_ANSWER" }
    const userAnswers = answer || {};

    const [localAnswers, setLocalAnswers] = useState({});
    const firstWrongRef = useRef(null);

    useEffect(() => {
        setLocalAnswers(userAnswers);
    }, [question?.id]);

    // Auto-scroll to first incorrect cell when memo is shown
    useEffect(() => {
        if (readOnly && firstWrongRef.current) {
            firstWrongRef.current.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }, [readOnly]);

    const handleChange = (word, value) => {
        if (readOnly) return;
        const next = { ...localAnswers, [word]: value.toUpperCase() };
        setLocalAnswers(next);
        setAnswer(next);
    };

    // Find first incorrect word for scroll target
    const firstWrongWord = readOnly
        ? words.find(w => {
            const val = (userAnswers[w] || '').toUpperCase().trim();
            return val && val !== w.toUpperCase().trim();
        })
        : null;

    return (
        <div className="space-y-6">
            <div className="text-sm font-semibold text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-200">
                Read each clue and type the answer in the box. Answers are checked when you submit.
            </div>

            <div className="space-y-3">
                {words.map((word, idx) => {
                    const clue = clues[word] || `Clue for word ${idx + 1}`;
                    const userVal = localAnswers[word] || '';
                    const isCorrect = readOnly && userVal.toUpperCase().trim() === word.toUpperCase().trim();
                    const isWrong = readOnly && userVal.toUpperCase().trim() !== word.toUpperCase().trim() && userVal.trim() !== '';
                    const isFirstWrong = word === firstWrongWord;

                    return (
                        <div
                            key={word}
                            ref={isFirstWrong ? firstWrongRef : null}
                            className={`flex flex-col sm:flex-row sm:items-center gap-3 p-4 rounded-xl border-2 transition-all duration-300 ${
                                isCorrect
                                    ? 'bg-emerald-50 border-emerald-200'
                                    : isWrong
                                    ? 'bg-red-50 border-red-200'
                                    : 'bg-white border-slate-200'
                            }`}
                        >
                            <div className="flex-1">
                                <div className="text-sm text-slate-700">
                                    <span className="font-bold mr-2">{idx + 1}.</span>
                                    {clue}
                                </div>
                                <div className="text-xs text-slate-400 mt-1">
                                    {word.length} letters
                                </div>
                            </div>
                            <input
                                type="text"
                                disabled={readOnly}
                                value={userVal}
                                onChange={(e) => handleChange(word, e.target.value)}
                                maxLength={word.length}
                                className={`w-full sm:w-48 px-4 py-2 rounded-lg border-2 text-center font-bold tracking-widest uppercase text-lg transition-all duration-300
                                    ${isCorrect
                                        ? 'border-emerald-400 bg-emerald-50 text-emerald-700'
                                        : isWrong
                                        ? 'border-red-400 bg-red-50 text-red-700'
                                        : 'border-slate-200 focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/20'
                                    }
                                    ${readOnly ? 'bg-slate-50 text-slate-500' : 'bg-white text-slate-800'}
                                `}
                            />
                        </div>
                    );
                })}
            </div>
        </div>
    );
};

export default BSCrosswordGrid;
