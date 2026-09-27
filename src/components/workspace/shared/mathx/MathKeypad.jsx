import React, { useState } from 'react';
import MathText from './MathText';
import { KEYPAD_CATEGORY_TABS, getKeysForCategory } from './mathKeypadRegistry';

/**
 * MathKeypad — registry-driven symbol palette.
 *
 * Calls ``onInsert(text, caretOffset)`` so the parent input can splice the token
 * at the caret. Purely presentational; the parent owns the input + caret.
 */
const MathKeypad = ({
    topic,
    onInsert,
    disabled = false,
    showTabs = true,
    defaultTab = 'topic',
    className = '',
}) => {
    const [activeTab, setActiveTab] = useState(defaultTab);
    const keys = getKeysForCategory(activeTab, topic);

    return (
        <div className={`space-y-2.5 ${className}`}>
            {/* Category Switcher Tabs */}
            {showTabs && (
                <div className="flex items-center gap-1.5 overflow-x-auto pb-1 scrollbar-thin">
                    {KEYPAD_CATEGORY_TABS.map((tab) => (
                        <button
                            key={tab.id}
                            type="button"
                            onClick={() => setActiveTab(tab.id)}
                            className={`px-2.5 py-1 rounded-md text-[11px] font-semibold whitespace-nowrap transition-colors cursor-pointer ${
                                activeTab === tab.id
                                    ? 'bg-brand-blue text-white shadow-xs font-bold'
                                    : 'bg-slate-100 hover:bg-slate-200 text-slate-600'
                            }`}
                        >
                            {tab.label}
                        </button>
                    ))}
                </div>
            )}

            {/* Symbol Buttons Grid */}
            <div className="flex flex-wrap gap-1.5 sm:gap-2 max-h-48 overflow-y-auto p-0.5">
                {keys.map((k) => (
                    <button
                        key={k.insert + k.label}
                        type="button"
                        disabled={disabled}
                        title={k.title || k.label}
                        onClick={(e) => {
                            e.preventDefault();
                            onInsert?.(k.insert, k.offset || 0);
                        }}
                        className="min-w-[2.5rem] sm:min-w-[2.75rem] h-9 sm:h-10 px-2.5 sm:px-3 rounded-lg border border-slate-200 bg-white hover:bg-blue-50 hover:border-brand-blue/40 hover:text-brand-blue text-slate-800 shadow-2xs transition-all active:scale-95 disabled:opacity-50 flex items-center justify-center text-sm font-medium cursor-pointer"
                    >
                        <MathText latex={k.label} />
                    </button>
                ))}
            </div>
        </div>
    );
};

export default MathKeypad;

