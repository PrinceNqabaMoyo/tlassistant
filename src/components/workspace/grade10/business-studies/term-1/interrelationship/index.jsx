import React from 'react';
import { useGrade10BSInterrelationshipController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSInterrelationshipVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Interrelationship of Environments
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'micro_to_market', 'micro_to_macro', 'business_influence'].map((tab) => (
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
                            The three business environments (Micro, Market, and Macro) do not operate in isolation. They are constantly interacting with and influencing each other.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> A change in one environment will have a ripple effect on the others. The business (micro environment) must constantly adapt to changes in the market and macro environments.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'micro_to_market' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Micro & Market Relationship</h4>
                        <p>The business (micro) interacts directly with the market environment components daily.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Consumers</h5>
                                <p className="text-xs mt-1">The business must adapt its products (micro) to meet changing consumer tastes and needs (market).</p>
                            </div>
                            
                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800">Suppliers</h5>
                                <p className="text-xs mt-1">If a supplier raises prices or runs out of stock (market), the business's production and profits (micro) are affected.</p>
                            </div>

                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800">Competitors</h5>
                                <p className="text-xs mt-1">When competitors launch new products or cut prices (market), the business must respond with new strategies or marketing campaigns (micro) to keep market share.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'micro_to_macro' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Micro & Macro Relationship</h4>
                        <p>The business has NO control over the macro environment, but macro changes force the business to adapt.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-amber-50 border border-amber-200 rounded-md">
                                <h5 className="font-semibold text-amber-800">Economic Changes</h5>
                                <p className="text-xs mt-1">If the Reserve Bank increases interest rates (macro), consumer spending drops, forcing the business to lower prices or cut costs (micro).</p>
                            </div>
                            
                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800">Legal Changes</h5>
                                <p className="text-xs mt-1">If the government introduces a new minimum wage law (macro), the business must increase its wage budget (micro) and ensure compliance.</p>
                            </div>
                            
                            <div className="p-3 bg-teal-50 border border-teal-200 rounded-md">
                                <h5 className="font-semibold text-teal-800">Technological Changes</h5>
                                <p className="text-xs mt-1">New technologies (macro) force businesses to update their equipment or IT systems (micro) to remain efficient and competitive.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'business_influence' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Can a business influence its environment?</h4>
                        <p className="text-xs mb-2">While businesses can't control the market or macro environments, they can try to influence them.</p>
                        
                        <ul className="list-disc list-inside space-y-2 text-xs">
                            <li><strong>Influencing Consumers:</strong> Through aggressive marketing, advertising, and loyalty programs.</li>
                            <li><strong>Influencing Suppliers:</strong> By signing long-term contracts, buying in bulk to negotiate discounts, or acquiring the supplier (backward integration).</li>
                            <li><strong>Influencing Competitors:</strong> By engaging in price wars, obtaining patents, or improving product quality.</li>
                            <li><strong>Influencing Regulators/Government:</strong> Large corporations might lobby government officials or participate in industry associations to influence laws.</li>
                        </ul>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSInterrelationshipController,
    Grade10BSInterrelationshipVisualAids
};
