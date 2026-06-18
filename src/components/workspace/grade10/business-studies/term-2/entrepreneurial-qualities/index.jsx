import React from 'react';
import { useGrade10BSEntrepreneurialQualitiesController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSEntrepreneurialQualitiesVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Entrepreneurial Qualities
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'key_qualities', 'entrepreneur_vs_intrapreneur', 'success_factors'].map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setVisualAidsTab(tab)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            visualAidsTab === tab
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab === 'entrepreneur_vs_intrapreneur' ? 'Entrep vs Intrap' : tab.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <p>
                            An entrepreneur is someone who identifies a business opportunity and takes on the financial risk to start and run a business in the hope of making a profit.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> Not everyone is suited to be an entrepreneur. It requires specific personal characteristics (qualities) to handle the stress, uncertainty, and hard work involved.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'key_qualities' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Essential Qualities of an Entrepreneur</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800">Risk-taker</h5>
                                <p className="text-xs mt-1">Willing to invest time and money without a guaranteed return. They take <em>calculated</em> risks, not foolish ones.</p>
                            </div>
                            
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Innovative & Creative</h5>
                                <p className="text-xs mt-1">Always looking for new ways to do things, solve problems, or create new products to satisfy consumer needs.</p>
                            </div>

                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800">Perseverance</h5>
                                <p className="text-xs mt-1">They do not give up easily. When they face failure or setbacks, they keep trying until they succeed.</p>
                            </div>

                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800">Leadership & Vision</h5>
                                <p className="text-xs mt-1">They have a clear idea of where they want the business to go and can motivate others (employees) to help them get there.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'entrepreneur_vs_intrapreneur' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Entrepreneur vs. Intrapreneur</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-orange-50 border border-orange-200 rounded-md">
                                <h5 className="font-semibold text-orange-800">Entrepreneur</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Starts their own business.</li>
                                    <li>Takes on all the personal and financial <strong>risk</strong>.</li>
                                    <li>Reaps all the profits (or suffers the losses).</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-teal-50 border border-teal-200 rounded-md">
                                <h5 className="font-semibold text-teal-800">Intrapreneur</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Works <strong>inside</strong> an existing business as an employee.</li>
                                    <li>Uses entrepreneurial qualities (innovation, creativity) to improve the business.</li>
                                    <li>The business takes the financial risk, not the intrapreneur.</li>
                                    <li>Receives a salary/bonus, not the direct profits of the business.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'success_factors' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Factors Contributing to Success</h4>
                        <p className="text-xs mb-2">Besides personal qualities, entrepreneurs need:</p>
                        
                        <ul className="list-disc list-inside space-y-2 text-xs">
                            <li><strong>Good Management Skills:</strong> Being able to plan, organize, lead, and control the business effectively.</li>
                            <li><strong>Financial Knowledge:</strong> Understanding cash flow, budgeting, and how to price products correctly.</li>
                            <li><strong>Market Knowledge:</strong> Knowing who their customers are, what they want, and who the competitors are.</li>
                            <li><strong>Adaptability:</strong> Being able to change strategies quickly when the market environment changes.</li>
                        </ul>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSEntrepreneurialQualitiesController,
    Grade10BSEntrepreneurialQualitiesVisualAids
};
