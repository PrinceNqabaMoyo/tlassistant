import React, { useState, useEffect } from 'react';

const WordBankQuestionUI = ({ question, answer, setAnswer, readOnly, showCheckHighlights }) => {
    // answer is an object mapping blank_id -> word
    const correctMap = question?.correct_map || {};
    // In Memo mode (readOnly), show the correct answers instead of user's answers
    const userMap = readOnly ? correctMap : (answer || {});
    
    // Setup state
    const [selectedPill, setSelectedPill] = useState(null);
    const [availableWords, setAvailableWords] = useState([]);
    
    useEffect(() => {
        if (!question?.word_bank) return;
        
        // In memo mode, all words are placed correctly so nothing is available
        if (readOnly) {
            setAvailableWords([]);
            return;
        }
        // Words that are NOT used in the current userMap
        const usedWords = Object.values(userMap);
        const freeWords = question.word_bank.filter(w => !usedWords.includes(w));
        setAvailableWords(freeWords);
        
        // Clear selected pill if it was used
        if (selectedPill && usedWords.includes(selectedPill)) {
            setSelectedPill(null);
        }
    }, [question, userMap, selectedPill, readOnly]);

    const handleWordClick = (word) => {
        if (readOnly) return;
        // Toggle selection
        if (selectedPill === word) {
            setSelectedPill(null);
        } else {
            setSelectedPill(word);
        }
    };

    const handleBlankClick = (blankId, currentWordInBlank) => {
        if (readOnly) return;
        
        const newMap = { ...userMap };
        
        // If they click a blank that has a word, and they don't have a pill selected, it removes the word
        if (!selectedPill && currentWordInBlank) {
            delete newMap[blankId];
            setAnswer(newMap);
            return;
        }
        
        // If they have a pill selected, map it to the blank
        if (selectedPill) {
            newMap[blankId] = selectedPill;
            setAnswer(newMap);
            setSelectedPill(null);
        }
    };

    const parts = question?.text_parts || [];
    const blanks = question?.blanks || [];

    return (
        <div className="space-y-6">
            <div className="text-sm font-semibold text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-200">
                Tap a word from the bank below, then tap an empty slot to place it. Tap a placed word to remove it.
            </div>

            {/* Word Bank */}
            <div className="p-4 bg-indigo-50 border border-indigo-100 rounded-xl min-h-[4rem] flex flex-wrap gap-2">
                {readOnly ? (
                    /* Memo mode: show all words as correctly placed */
                    question?.word_bank?.map((word, idx) => (
                        <span
                            key={idx}
                            className="px-3 py-1.5 rounded-full text-sm font-medium transition-all duration-500 shadow-sm bg-emerald-50 text-emerald-700 border border-emerald-200 opacity-80"
                        >
                            ✓ {word}
                        </span>
                    ))
                ) : (
                    availableWords.map((word, idx) => (
                        <button
                            key={idx}
                            onClick={() => handleWordClick(word)}
                            className={`px-3 py-1.5 rounded-full text-sm font-medium transition-all duration-500 shadow-sm
                                ${selectedPill === word
                                    ? 'bg-indigo-600 text-white ring-2 ring-indigo-300 ring-offset-1'
                                    : 'bg-white text-indigo-700 hover:bg-indigo-100 border border-indigo-200'
                                }
                            `}
                        >
                            {word}
                        </button>
                    ))
                )}
                {availableWords.length === 0 && !readOnly && (
                    <div className="text-indigo-400 text-sm italic w-full text-center">All words placed.</div>
                )}
            </div>

            {/* Text Flow */}
            <div className="p-6 bg-white border border-slate-200 rounded-xl shadow-sm leading-8 text-[15px] text-slate-800">
                {parts.map((pText, i) => {
                    const isLast = i === parts.length - 1;
                    const blankItem = !isLast ? blanks[i] : null;
                    const bId = blankItem?.id;
                    const placedWord = bId ? userMap[bId] : null;

                    let slotStyle = "inline-flex min-w-[100px] h-8 mx-1 px-3 border-b-2 bg-slate-50 text-slate-700 items-center justify-center cursor-pointer transition-all duration-500";
                    if (selectedPill && !placedWord && !readOnly) slotStyle += " hover:bg-indigo-50 hover:border-indigo-400 border-slate-300 border-dashed";
                    else if (!placedWord) slotStyle += " border-slate-300 border-dashed";
                    else if (placedWord && readOnly) slotStyle += " border-emerald-400 text-emerald-700 font-semibold bg-emerald-50";
                    else if (placedWord) slotStyle += " border-indigo-400 text-indigo-700 font-medium hover:bg-slate-100";

                    if (showCheckHighlights && bId && placedWord) {
                        const isCorrect = placedWord === correctMap[bId];
                        if (isCorrect) {
                            slotStyle += " border-emerald-500 bg-emerald-50 text-emerald-700 ring-1 ring-emerald-500 rounded-sm";
                        } else {
                            slotStyle += " border-red-500 bg-red-50 text-red-700 ring-1 ring-red-500 rounded-sm";
                        }
                    }

                    return (
                        <React.Fragment key={i}>
                            <span>{pText}</span>
                            {!isLast && bId && (
                                <span 
                                    className={slotStyle}
                                    onClick={() => handleBlankClick(bId, placedWord)}
                                >
                                    {placedWord || ''}
                                </span>
                            )}
                        </React.Fragment>
                    );
                })}
            </div>
            
        </div>
    );
};

export default WordBankQuestionUI;
