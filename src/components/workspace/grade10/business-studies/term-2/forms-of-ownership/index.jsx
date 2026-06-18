import React from 'react';
import { useGrade10BSFormsOfOwnershipController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSFormsOfOwnershipVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Forms of Ownership
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'sole_trader', 'partnership', 'companies', 'other_forms'].map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setVisualAidsTab(tab)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            visualAidsTab === tab
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <p>
                            When starting a business, an entrepreneur must choose a legal structure (form of ownership). This choice affects:
                        </p>
                        <ul className="list-disc list-inside space-y-1 mt-2">
                            <li><strong>Capacity:</strong> Who can enter into contracts?</li>
                            <li><strong>Taxation:</strong> Who pays tax and at what rate?</li>
                            <li><strong>Liability:</strong> Who pays the debts if the business fails?</li>
                            <li><strong>Continuity:</strong> Does the business continue if an owner dies/leaves?</li>
                        </ul>
                        
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept - Liability:</strong><br />
                            <em>Unlimited Liability:</em> The owner's personal assets can be sold to pay business debts.<br />
                            <em>Limited Liability:</em> The owner only loses what they invested in the business. Personal assets are safe.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'sole_trader' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Sole Trader (Sole Proprietorship)</h4>
                        <p className="text-xs">A business owned and managed by one person.</p>
                        
                        <div className="grid grid-cols-2 gap-3 mt-2">
                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800 text-xs">Advantages</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li>Easy and cheap to start.</li>
                                    <li>Owner keeps all profits.</li>
                                    <li>Quick decision making.</li>
                                </ul>
                            </div>
                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800 text-xs">Disadvantages</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li><strong>Unlimited liability.</strong></li>
                                    <li><strong>No continuity</strong> (ends if owner dies).</li>
                                    <li>Capital is limited to one person's wealth.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'partnership' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Partnership</h4>
                        <p className="text-xs">An agreement between 2 or more people (partners) to combine labour, capital, and skills to make a profit.</p>
                        
                        <div className="grid grid-cols-2 gap-3 mt-2">
                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800 text-xs">Advantages</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li>More capital than a sole trader.</li>
                                    <li>Workload and responsibilities are shared.</li>
                                    <li>Partners bring different skills.</li>
                                </ul>
                            </div>
                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800 text-xs">Disadvantages</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li><strong>Unlimited liability</strong> (jointly and severally).</li>
                                    <li><strong>No continuity.</strong></li>
                                    <li>Potential for conflict between partners.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'companies' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Companies</h4>
                        <p className="text-xs">Companies are separate legal entities from their owners (shareholders). Regulated by the Companies Act (71 of 2008).</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Private Company (Pty) Ltd</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li><strong>Liability:</strong> Limited.</li>
                                    <li><strong>Continuity:</strong> Yes.</li>
                                    <li><strong>Capital:</strong> Raises capital by selling shares privately (not to the public).</li>
                                    <li>Requires at least 1 director.</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800">Public Company (Ltd)</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li><strong>Liability:</strong> Limited.</li>
                                    <li><strong>Continuity:</strong> Yes.</li>
                                    <li><strong>Capital:</strong> Raises large amounts of capital by selling shares to the general public on the JSE.</li>
                                    <li>Requires at least 3 directors and has strict auditing requirements.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'other_forms' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Other Forms of Ownership</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-teal-50 border border-teal-200 rounded-md">
                                <h5 className="font-semibold text-teal-800">Personal Liability Company (Inc.)</h5>
                                <p className="text-xs mt-1">Used by professionals (doctors, lawyers). Directors are jointly and severally liable for the debts of the company.</p>
                            </div>

                            <div className="p-3 bg-orange-50 border border-orange-200 rounded-md">
                                <h5 className="font-semibold text-orange-800">State-Owned Company (SOC Ltd)</h5>
                                <p className="text-xs mt-1">Owned by the government (e.g., Eskom, SAA). Aims to provide essential services, not just make a profit.</p>
                            </div>

                            <div className="p-3 bg-amber-50 border border-amber-200 rounded-md">
                                <h5 className="font-semibold text-amber-800">Non-Profit Company (NPC)</h5>
                                <p className="text-xs mt-1">Formed for a public benefit or cultural/social activities. Any profit made must be used to advance the company's goals, not paid to members.</p>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSFormsOfOwnershipController,
    Grade10BSFormsOfOwnershipVisualAids
};
