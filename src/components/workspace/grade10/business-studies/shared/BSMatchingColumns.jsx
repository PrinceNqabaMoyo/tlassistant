import React, { useState, useEffect } from 'react';

export const BSMatchingColumns = ({ question, answer, setAnswer, readOnly }) => {
    const columnA = question?.column_a || [];
    const columnB = question?.column_b || [];
    const correctPairs = question?.correct_pairs || {};

    // answer shape: { columnA_label: columnB_label }
    const userPairs = answer || {};

    const [selectedA, setSelectedA] = useState(null);

    useEffect(() => {
        if (readOnly) setSelectedA(null);
    }, [readOnly]);

    const handleSelectA = (aKey) => {
        if (readOnly) return;
        setSelectedA((prev) => (prev === aKey ? null : aKey));
    };

    const handleSelectB = (bKey) => {
        if (readOnly || !selectedA) return;
        const next = { ...userPairs, [selectedA]: bKey };
        setAnswer(next);
        setSelectedA(null);
    };

    const handleRemovePair = (aKey) => {
        if (readOnly) return;
        const next = { ...userPairs };
        delete next[aKey];
        setAnswer(next);
        setSelectedA(null);
    };

    const usedB = new Set(Object.values(userPairs));

    return (
        <div className="space-y-6">
            <div className="text-sm font-semibold text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-200">
                {readOnly
                    ? 'Memo: correct pairings shown below.'
                    : 'Tap an item from Column A, then tap its matching item from Column B.'}
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
                {/* Column A */}
                <div className="space-y-2">
                    <h4 className="text-xs font-bold uppercase tracking-wide text-slate-500">Column A</h4>
                    <div className="space-y-2">
                        {columnA.map((aItem) => {
                            const aKey = String(aItem);
                            const isSelected = selectedA === aKey;
                            const isPaired = Object.prototype.hasOwnProperty.call(userPairs, aKey);

                            let boxStyle = 'w-full text-left p-3 rounded-xl border-2 transition-all text-sm font-medium ';
                            if (readOnly) {
                                const correctB = correctPairs[aKey];
                                const userB = userPairs[aKey];
                                if (userB === correctB) {
                                    boxStyle += 'bg-emerald-50 border-emerald-300 text-emerald-800';
                                } else {
                                    boxStyle += 'bg-red-50 border-red-300 text-red-800';
                                }
                            } else if (isSelected) {
                                boxStyle += 'bg-indigo-50 border-indigo-500 text-indigo-800 ring-2 ring-indigo-200';
                            } else if (isPaired) {
                                boxStyle += 'bg-slate-100 border-slate-300 text-slate-600';
                            } else {
                                boxStyle += 'bg-white border-slate-200 text-slate-700 hover:border-indigo-300 hover:bg-slate-50';
                            }

                            return (
                                <button
                                    key={aKey}
                                    className={boxStyle}
                                    onClick={() => handleSelectA(aKey)}
                                    disabled={readOnly}
                                >
                                    <span className="font-bold mr-2">{aKey}.</span>
                                    {aItem}
                                    {isPaired && !readOnly && (
                                        <span className="ml-2 text-xs text-slate-400">
                                            → {userPairs[aKey]}
                                        </span>
                                    )}
                                </button>
                            );
                        })}
                    </div>
                </div>

                {/* Column B */}
                <div className="space-y-2">
                    <h4 className="text-xs font-bold uppercase tracking-wide text-slate-500">Column B</h4>
                    <div className="space-y-2">
                        {columnB.map((bItem) => {
                            const bKey = String(bItem);
                            const isUsed = usedB.has(bKey);

                            let boxStyle = 'w-full text-left p-3 rounded-xl border-2 transition-all text-sm font-medium ';
                            if (readOnly) {
                                boxStyle += 'bg-white border-slate-200 text-slate-700';
                            } else if (isUsed) {
                                boxStyle += 'bg-slate-100 border-slate-200 text-slate-400 cursor-not-allowed';
                            } else if (selectedA) {
                                boxStyle += 'bg-white border-indigo-200 text-indigo-700 hover:bg-indigo-50 hover:border-indigo-400 cursor-pointer';
                            } else {
                                boxStyle += 'bg-white border-slate-200 text-slate-700';
                            }

                            return (
                                <button
                                    key={bKey}
                                    className={boxStyle}
                                    onClick={() => handleSelectB(bKey)}
                                    disabled={readOnly || isUsed}
                                >
                                    <span className="font-bold mr-2">{bKey}.</span>
                                    {bItem}
                                </button>
                            );
                        })}
                    </div>
                </div>
            </div>

            {/* Active pairings summary */}
            {!readOnly && Object.keys(userPairs).length > 0 && (
                <div className="p-4 bg-slate-50 border border-slate-200 rounded-xl">
                    <h4 className="text-xs font-bold uppercase tracking-wide text-slate-500 mb-2">Your Pairings</h4>
                    <div className="flex flex-wrap gap-2">
                        {Object.entries(userPairs).map(([aKey, bKey]) => (
                            <button
                                key={aKey}
                                onClick={() => handleRemovePair(aKey)}
                                className="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-indigo-100 text-indigo-800 text-sm font-medium hover:bg-red-100 hover:text-red-700 transition-colors"
                            >
                                {aKey} ↔ {bKey}
                                <span className="text-xs ml-1">×</span>
                            </button>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
};

export default BSMatchingColumns;
