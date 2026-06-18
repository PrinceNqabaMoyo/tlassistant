import React from 'react';

const InlineFillQuestionUI = ({ question, answer, setAnswer, readOnly, showCheckHighlights }) => {
    // answer is an object mapping blank_id -> word
    const userMap = typeof answer === 'object' && answer !== null ? answer : {};
    
    const parts = question?.text_parts || [];
    const blanks = question?.blanks || [];
    const correctMap = question?.correct_map || {};

    const handleInputChange = (bId, value) => {
        if (readOnly) return;
        setAnswer({ ...userMap, [bId]: value });
    };

    return (
        <div className="space-y-6">
            <div className="text-sm font-semibold text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-200">
                Type directly into the empty spaces below to complete the sentence.
            </div>

            <div className="p-6 bg-white border border-slate-200 rounded-xl shadow-sm leading-10 text-[16px] text-slate-800">
                {parts.map((pText, i) => {
                    const isLast = i === parts.length - 1;
                    const blankItem = !isLast ? blanks[i] : null;
                    const bId = blankItem?.id;
                    const userVal = bId ? (userMap[bId] || '') : '';

                    let inputStyle = "inline-block mx-2 min-w-[120px] max-w-[200px] border-b-2 bg-slate-50 px-2 py-1 text-center font-medium text-indigo-700 focus:outline-none focus:bg-indigo-50 focus:border-indigo-500 transition-colors placeholder:text-slate-300 placeholder:font-normal";
                    
                    if (readOnly) inputStyle += " opacity-90";
                    else inputStyle += " border-slate-300 hover:border-indigo-400 cursor-text";

                    if (showCheckHighlights && bId) {
                        const isCorrect = userVal?.trim()?.toLowerCase() === correctMap[bId]?.trim()?.toLowerCase();
                        if (isCorrect) {
                            inputStyle += " !border-emerald-500 !bg-emerald-50 !text-emerald-700 !ring-1 !ring-emerald-500 rounded-sm";
                        } else if (userVal) {
                            inputStyle += " !border-red-500 !bg-red-50 !text-red-700 !ring-1 !ring-red-500 rounded-sm";
                        }
                    }

                    return (
                        <React.Fragment key={i}>
                            <span>{pText}</span>
                            {!isLast && bId && (
                                <input 
                                    className={inputStyle}
                                    value={readOnly ? (correctMap[bId] || '') : userVal}
                                    onChange={(e) => handleInputChange(bId, e.target.value)}
                                    placeholder="type here"
                                    readOnly={readOnly}
                                />
                            )}
                        </React.Fragment>
                    );
                })}
            </div>
        </div>
    );
};

export default InlineFillQuestionUI;
