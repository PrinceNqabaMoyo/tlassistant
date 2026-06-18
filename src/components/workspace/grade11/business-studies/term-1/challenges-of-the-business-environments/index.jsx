import React from 'react';
import { AlertTriangle, ShieldAlert, Store, X } from 'lucide-react';
import { useGrade11BSChallengesController } from './controller';

const Grade11BSChallengesVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <AlertTriangle className="w-5 h-5" />
                    Challenges of the Business Environments
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <X className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'micro', 'market', 'macro'].map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setVisualAidsTab(tab)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            visualAidsTab === tab
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab.charAt(0).toUpperCase() + tab.slice(1)}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar text-sm text-slate-700 space-y-4">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-4">
                        <p>
                            Businesses face challenges inside the organisation, from nearby market stakeholders, and from broad external forces.
                            Strong answers classify the challenge correctly, explain its effect, and recommend a practical response where required.
                        </p>
                        <div className="rounded-xl border border-indigo-100 bg-indigo-50 p-4 space-y-2">
                            <p className="font-semibold text-indigo-800">Core classification rule</p>
                            <p>
                                Micro challenges come from inside the business, market challenges come from stakeholders such as suppliers and customers,
                                and macro challenges come from wider political, legal, economic, social, and global forces.
                            </p>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'micro' && (
                    <div className="space-y-4">
                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                            <p className="font-semibold text-slate-800 mb-2 flex items-center gap-2">
                                <ShieldAlert className="w-4 h-4 text-indigo-600" />
                                Common micro challenges
                            </p>
                            <ul className="space-y-2 list-disc list-inside">
                                <li>Difficult employees and poor teamwork</li>
                                <li>Lack of vision and mission</li>
                                <li>Lack of adequate management skills</li>
                                <li>Strikes, go-slows, or internal conflict</li>
                            </ul>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'market' && (
                    <div className="space-y-4">
                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                            <p className="font-semibold text-slate-800 mb-2 flex items-center gap-2">
                                <Store className="w-4 h-4 text-indigo-600" />
                                Common market challenges
                            </p>
                            <ul className="space-y-2 list-disc list-inside">
                                <li>Shortage of suppliers or late deliveries</li>
                                <li>Changes in consumer behaviour</li>
                                <li>Competition from rivals</li>
                                <li>Demographic and psychographic changes</li>
                            </ul>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'macro' && (
                    <div className="space-y-4">
                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                            <p className="font-semibold text-slate-800 mb-2">Common macro challenges</p>
                            <ul className="space-y-2 list-disc list-inside">
                                <li>Changes in income levels and consumer spending</li>
                                <li>Political changes and new legislation</li>
                                <li>Labour restrictions and compliance pressure</li>
                                <li>Crime, HIV/AIDS, corruption, and globalisation</li>
                            </ul>
                        </div>
                        <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-4 text-emerald-900">
                            When a question asks for motivation, quote the exact phrase from the scenario that proves the challenge.
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade11BSChallengesController,
    Grade11BSChallengesVisualAids,
};
