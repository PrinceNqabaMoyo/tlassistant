import React from 'react';
import { useGrade10BSMarketEnvironmentController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSMarketEnvironmentVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    The Market Environment
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'components', 'civil_society', 'strategic_allies'].map((tab) => (
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
                            The Market Environment refers to the external environment situated immediately outside the business. Management has little to NO control over this environment, but they can influence it.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> The market environment consists of elements that directly impact the business's ability to operate, but which the business cannot directly manage like its own internal departments.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'components' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Core Components</h4>
                        
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">1. Customers / Consumers</h5>
                                <p className="text-xs mt-1">People who buy/use the products. The business exists to satisfy their needs.</p>
                            </div>
                            
                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800">2. Suppliers</h5>
                                <p className="text-xs mt-1">Provide raw materials, equipment, or services needed by the business. They must be reliable.</p>
                            </div>

                            <div className="p-3 bg-orange-50 border border-orange-200 rounded-md">
                                <h5 className="font-semibold text-orange-800">3. Intermediaries</h5>
                                <p className="text-xs mt-1">Agents, wholesalers, or retailers who help distribute the product from the producer to the final consumer.</p>
                            </div>

                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800">4. Competitors</h5>
                                <p className="text-xs mt-1">Other businesses selling similar products or services. A business must try to gain a competitive advantage.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'civil_society' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Civil Society & Regulators</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Non-Governmental Organisations (NGOs)</h5>
                                <p className="text-xs mt-1">Non-profit organisations that focus on specific issues (e.g., environmental protection, human rights). They can pressure businesses to act ethically.</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Community Based Organisations (CBOs)</h5>
                                <p className="text-xs mt-1">Local groups formed to address specific community needs. Businesses often interact with CBOs through Corporate Social Responsibility (CSR).</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Regulators</h5>
                                <p className="text-xs mt-1">Organisations that set rules and standards for businesses (e.g., SABS, Advertising Standards Authority). They protect consumers and ensure fair practices.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'strategic_allies' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Strategic Allies</h4>
                        <p className="text-xs mb-2">Businesses that work together for mutual benefit without merging.</p>
                        
                        <ul className="list-disc list-inside space-y-2 text-xs">
                            <li><strong>Joint ventures:</strong> Two businesses pool resources for a specific project.</li>
                            <li><strong>Franchising:</strong> A business (franchisor) allows another (franchisee) to use its name and system.</li>
                            <li><strong>Outsourcing:</strong> Paying another business to perform non-core functions (e.g., hiring a security company).</li>
                        </ul>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSMarketEnvironmentController,
    Grade10BSMarketEnvironmentVisualAids
};
