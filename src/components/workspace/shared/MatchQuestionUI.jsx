import React, { useState, useEffect, useMemo } from 'react';

const MatchQuestionUI = ({ question, answer, setAnswer, readOnly, showCheckHighlights }) => {
    const left = question?.left_items || [];
    const right = question?.right_items || [];
    const correctMap = question?.correct_map || {};

    // answer is an object mapping leftId -> rightId
    // If readOnly is true (Memo Mode), we force the UI to display the correct answers instead of user answers
    const activeMap = readOnly ? correctMap : (answer || {});
    
    // Setup state for "Tap to Snap" flow
    // User taps a right item to 'pick it up', then taps a left item slot to 'place it'
    const [selectedRightItem, setSelectedRightItem] = useState(null);

    // Shuffle options once on mount so they don't align with correct answers by default
    const [shuffledRightIds, setShuffledRightIds] = useState([]);
    
    useEffect(() => {
        if (right.length > 0 && shuffledRightIds.length === 0) {
            const ids = right.map(r => r.id);
            // Fisher-Yates shuffle
            for (let i = ids.length - 1; i > 0; i--) {
                const j = Math.floor(Math.random() * (i + 1));
                [ids[i], ids[j]] = [ids[j], ids[i]];
            }
            setShuffledRightIds(ids);
        }
    }, [right, shuffledRightIds.length]);

    // Order the available items based on our shuffled array
    const availableRightItems = useMemo(() => {
        const usedIds = Object.values(activeMap);
        const availableDict = {};
        for (const r of right) {
            if (!usedIds.includes(r.id)) availableDict[r.id] = r;
        }
        
        return shuffledRightIds
            .filter(id => !usedIds.includes(id) && availableDict[id])
            .map(id => availableDict[id]);
    }, [right, activeMap, shuffledRightIds]);

    const handleRightClick = (rId) => {
        if (readOnly) return;
        if (selectedRightItem === rId) {
            setSelectedRightItem(null); // deselect
        } else {
            setSelectedRightItem(rId);
        }
    };

    const handleLeftClick = (lId, currentRightId) => {
        if (readOnly) return;

        const newMap = { ...(answer || {}) };

        // If clicking a left slot that already has a right item, and no right item is currently selected in hand
        // -> Remove it back to the pool
        if (!selectedRightItem && currentRightId) {
            delete newMap[lId];
            setAnswer(newMap);
            return;
        }

        // If clicking a left slot and we have a right item selected in hand
        // -> Place it in the slot (and displace any existing one back to pool automatically)
        if (selectedRightItem) {
            newMap[lId] = selectedRightItem;
            setAnswer(newMap);
            setSelectedRightItem(null);
        }
    };

    return (
        <div className="space-y-6">
            <div className="text-sm font-semibold text-slate-700 bg-slate-50 p-3 rounded-xl border border-slate-200">
                Match the options by tapping an item on the right, then tapping the correct row on the left to snap it into place.
            </div>

            <div className="flex flex-col md:flex-row gap-6">
                
                {/* LEFT SIDE (Targets) */}
                <div className="flex-1 space-y-3">
                    <h3 className="font-semibold text-slate-500 uppercase tracking-wider text-xs mb-4">Column A (Definitions/Terms)</h3>
                    {left.map((lItem) => {
                        const matchedRightId = activeMap[lItem.id];
                        const matchedRightObj = matchedRightId ? right.find(r => r.id === matchedRightId) : null;
                        
                        let slotStyle = "flex-1 ml-3 min-h-[50px] p-3 rounded-xl border-2 flex items-center transition-all cursor-pointer ";
                        if (selectedRightItem && !matchedRightId && !readOnly) slotStyle += " border-dashed border-indigo-300 bg-indigo-50/50 hover:bg-indigo-50";
                        else if (!matchedRightId) slotStyle += " border-dashed border-slate-200 bg-slate-50 hover:bg-slate-100";
                        else slotStyle += " border-solid border-indigo-200 bg-white shadow-sm hover:bg-slate-50";

                        // Marking Highlighting
                        if (showCheckHighlights && matchedRightId) {
                            const isCorrect = matchedRightId === correctMap[lItem.id];
                            if (isCorrect) slotStyle += " !border-emerald-500 !bg-emerald-50";
                            else slotStyle += " !border-red-500 !bg-red-50";
                        }

                        return (
                            <div key={lItem.id} className="flex relative">
                                {/* Left Item Block */}
                                <div className="flex-1 p-4 bg-white border border-slate-200 rounded-xl shadow-sm text-sm text-slate-800 flex items-center z-10 relative">
                                    {lItem.text}
                                    {/* Connector Visual Tab */}
                                    <div className="absolute -right-3 top-1/2 -translate-y-1/2 w-3 h-4 bg-slate-200" style={{clipPath: 'polygon(0 0, 100% 50%, 0 100%)'}}></div>
                                </div>
                                
                                {/* Right Target Slot */}
                                <div 
                                    className={slotStyle}
                                    onClick={() => handleLeftClick(lItem.id, matchedRightId)}
                                >
                                    {matchedRightObj ? (
                                        <div className="text-sm font-medium text-indigo-900 w-full">
                                            {matchedRightObj.text}
                                        </div>
                                    ) : (
                                        <div className="text-xs text-slate-400 font-medium tracking-wide w-full text-center">
                                            {selectedRightItem ? "TAP TO PLACE" : "EMPTY"}
                                        </div>
                                    )}
                                </div>
                            </div>
                        );
                    })}
                </div>

                {/* RIGHT SIDE (Bank) */}
                <div className="w-full md:w-1/3 min-w-[250px] bg-indigo-50/50 rounded-2xl p-4 border border-indigo-100">
                    <h3 className="font-semibold text-indigo-400 uppercase tracking-wider text-xs mb-4">Column B (Options Bank)</h3>
                    
                    <div className="space-y-3">
                        {availableRightItems.map((rItem) => {
                            const isSelected = selectedRightItem === rItem.id;
                            return (
                                <div 
                                    key={rItem.id}
                                    onClick={() => handleRightClick(rItem.id)}
                                    className={`p-4 rounded-xl text-sm font-medium transition-all shadow-sm flex items-center
                                        ${readOnly ? 'opacity-50 cursor-not-allowed bg-white border border-slate-200 text-slate-700' : 'cursor-pointer'}
                                        ${isSelected 
                                            ? 'bg-indigo-600 text-white ring-2 ring-indigo-300 ring-offset-2 scale-[1.02] -translate-y-0.5' 
                                            : (!readOnly ? 'bg-white border border-indigo-200 text-indigo-900 hover:border-indigo-400 hover:shadow-md hover:-translate-y-0.5' : '')
                                        }
                                    `}
                                >
                                    <div className="flex-1">{rItem.text}</div>
                                    {isSelected && <div className="ml-2 text-indigo-200">👆</div>}
                                </div>
                            );
                        })}

                        {availableRightItems.length === 0 && (
                            <div className="py-8 text-center text-indigo-300 font-medium text-sm">
                                All options placed!
                            </div>
                        )}
                    </div>
                </div>

            </div>
        </div>
    );
};

export default MatchQuestionUI;
