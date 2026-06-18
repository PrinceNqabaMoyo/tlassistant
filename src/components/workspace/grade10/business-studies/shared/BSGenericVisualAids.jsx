import React from 'react';
import { BookOpen, X } from 'lucide-react';

const VARIANT_STYLES = {
    note: 'bg-slate-50 border-slate-200 text-slate-700',
    green: 'bg-green-50 border-green-200 text-green-800',
    blue: 'bg-blue-50 border-blue-200 text-blue-800',
    orange: 'bg-orange-50 border-orange-200 text-orange-800',
    indigo: 'bg-indigo-50 border-indigo-200 text-indigo-800',
    amber: 'bg-amber-50 border-amber-200 text-amber-800',
};

const Section = ({ section }) => {
    const variantClass = VARIANT_STYLES[section.variant || 'note'];
    return (
        <div className={`p-3 rounded-md border ${variantClass}`}>
            {section.heading && (
                <h5 className="font-semibold mb-1">{section.heading}</h5>
            )}
            {section.text && <p className="text-xs leading-relaxed">{section.text}</p>}
            {Array.isArray(section.bullets) && section.bullets.length > 0 && (
                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                    {section.bullets.map((b, i) => (
                        <li key={i}>{b}</li>
                    ))}
                </ul>
            )}
        </div>
    );
};

/**
 * Data-driven visual aids panel shared across Business Studies topics.
 * `tabs` is an array of { key, label, sections: [{ heading, text, bullets, variant }] }.
 */
export const BSGenericVisualAids = ({ title, tabs = [], visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const activeKey = visualAidsTab && tabs.some((t) => t.key === visualAidsTab)
        ? visualAidsTab
        : tabs[0]?.key;
    const activeTab = tabs.find((t) => t.key === activeKey) || tabs[0];

    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    {title}
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <X className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {tabs.map((tab) => (
                    <button
                        key={tab.key}
                        onClick={() => setVisualAidsTab(tab.key)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            activeKey === tab.key
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab.label}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
                <div className="space-y-3 text-sm text-slate-700">
                    {activeTab?.intro && <p>{activeTab.intro}</p>}
                    {(activeTab?.sections || []).map((section, idx) => (
                        <Section key={idx} section={section} />
                    ))}
                </div>
            </div>
        </div>
    );
};

export default BSGenericVisualAids;
