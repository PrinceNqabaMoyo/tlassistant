import React from 'react';
import { BookOpen, X } from 'lucide-react';
import { useGrade11BSInfluencesController } from './controller';

const Grade11BSInfluencesVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Influences on Business Environments
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <X className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'internal-external', 'pestle', 'response'].map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setVisualAidsTab(tab)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            visualAidsTab === tab
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab.charAt(0).toUpperCase() + tab.slice(1).replace('-', ' ')}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar text-sm text-slate-700 space-y-4">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-4">
                        <p>
                            Businesses are influenced by factors inside the organisation and by forces outside the organisation.
                            Managers need to understand these influences so they can protect performance, respond to change and plan effectively.
                        </p>
                        <div className="rounded-xl border border-indigo-100 bg-indigo-50 p-4 space-y-2">
                            <p className="font-semibold text-indigo-800">Core idea</p>
                            <p>
                                The business environment includes internal influences such as leadership, resources and goals, and external influences such as legislation, competition, technology and economic conditions.
                            </p>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'internal-external' && (
                    <div className="space-y-4">
                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                            <p className="font-semibold text-slate-800 mb-2">Internal influences</p>
                            <ul className="space-y-2 list-disc list-inside">
                                <li>Leadership and management style</li>
                                <li>Mission, vision, goals and objectives</li>
                                <li>Resources, systems and organisational culture</li>
                                <li>Structure and decision-making processes</li>
                            </ul>
                        </div>
                        <div className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                            <p className="font-semibold text-slate-800 mb-2">External influences</p>
                            <ul className="space-y-2 list-disc list-inside">
                                <li>Competitors, customers and suppliers</li>
                                <li>Legislation and labour requirements</li>
                                <li>Technology and innovation</li>
                                <li>Economic conditions such as inflation and interest rates</li>
                            </ul>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'pestle' && (
                    <div className="space-y-3">
                        {[
                            ['Political', 'Government policy, trade rules and regulation.'],
                            ['Economic', 'Inflation, interest rates, unemployment and exchange rates.'],
                            ['Social', 'Consumer lifestyles, population trends and social values.'],
                            ['Technological', 'Innovation, automation, data systems and digital platforms.'],
                            ['Legal', 'Labour law, consumer protection and compliance demands.'],
                            ['Environmental', 'Sustainability expectations and the use of resources.'],
                        ].map(([title, text]) => (
                            <div key={title} className="rounded-xl border border-slate-200 bg-slate-50 p-4">
                                <p className="font-semibold text-slate-800">{title}</p>
                                <p className="mt-1">{text}</p>
                            </div>
                        ))}
                    </div>
                )}

                {visualAidsTab === 'response' && (
                    <div className="space-y-4">
                        <p className="font-semibold text-slate-800">How managers respond</p>
                        <ul className="space-y-2 list-disc list-inside">
                            <li>Monitor internal and external changes regularly.</li>
                            <li>Identify risks, constraints and opportunities early.</li>
                            <li>Adjust plans, budgets, staffing or operations where needed.</li>
                            <li>Use strategy, communication and training to support adaptation.</li>
                        </ul>
                        <div className="rounded-xl border border-emerald-200 bg-emerald-50 p-4 text-emerald-900">
                            Strong Business Studies answers usually classify the influence, explain its effect and then show how management should respond.
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade11BSInfluencesController,
    Grade11BSInfluencesVisualAids,
};
