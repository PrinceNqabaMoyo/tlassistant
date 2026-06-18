import React from 'react';
import { useGrade10BSSocioEconomicIssuesController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSSocioEconomicIssuesVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Socio-Economic Issues
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'inequality_poverty', 'unemployment_strikes', 'crime_health'].map((tab) => (
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
                            Socio-economic issues are problems in society that affect the economy, and consequently, the businesses operating within that economy.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> Businesses cannot ignore these issues because they directly affect their operations, productivity, and profitability. Businesses have a social responsibility to help address these challenges.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'inequality_poverty' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Inequality & Poverty</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800">Inequality</h5>
                                <p className="text-xs mt-1">The gap between the rich and the poor. In South Africa, this gap is very wide.</p>
                                <p className="text-xs mt-1 font-semibold">Impact on Business:</p>
                                <ul className="list-disc list-inside text-xs">
                                    <li>Limits the market size (fewer people can afford luxury goods).</li>
                                    <li>Can lead to social unrest and strikes.</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-orange-50 border border-orange-200 rounded-md">
                                <h5 className="font-semibold text-orange-800">Poverty</h5>
                                <p className="text-xs mt-1">When people lack the financial resources to meet basic needs (food, shelter, clothing).</p>
                                <p className="text-xs mt-1 font-semibold">Impact on Business:</p>
                                <ul className="list-disc list-inside text-xs">
                                    <li>Decreased consumer spending power.</li>
                                    <li>Increased crime rates as people become desperate.</li>
                                    <li>Workers may be malnourished, affecting productivity.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'unemployment_strikes' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Unemployment & Strikes</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-amber-50 border border-amber-200 rounded-md">
                                <h5 className="font-semibold text-amber-800">Unemployment</h5>
                                <p className="text-xs mt-1">People who are willing and able to work but cannot find jobs.</p>
                                <p className="text-xs mt-1 font-semibold">Impact on Business:</p>
                                <ul className="list-disc list-inside text-xs">
                                    <li>Reduced demand for goods and services.</li>
                                    <li>Higher taxes (businesses pay more to support government social grants).</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-yellow-50 border border-yellow-200 rounded-md">
                                <h5 className="font-semibold text-yellow-800">Strikes and Labour Disputes</h5>
                                <p className="text-xs mt-1">When workers refuse to work, usually to demand better pay or working conditions.</p>
                                <p className="text-xs mt-1 font-semibold">Impact on Business:</p>
                                <ul className="list-disc list-inside text-xs">
                                    <li>Loss of production time and output.</li>
                                    <li>Loss of profits.</li>
                                    <li>Damage to business property if the strike becomes violent.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'crime_health' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Crime, Piracy & Health</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800">Crime & Security Issues</h5>
                                <p className="text-xs mt-1">Includes theft, hijacking, and vandalism.</p>
                                <p className="text-xs mt-1 font-semibold">Impact:</p>
                                <p className="text-xs">Loss of stock/assets, increased insurance premiums, and high costs for security measures.</p>
                            </div>
                            
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Piracy, Counterfeiting & Bootlegging</h5>
                                <p className="text-xs mt-1">Illegal copying or selling of fake goods.</p>
                                <p className="text-xs mt-1 font-semibold">Impact:</p>
                                <p className="text-xs">Loss of sales for legitimate businesses, damage to brand reputation if fake goods are of poor quality.</p>
                            </div>

                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800">HIV/AIDS</h5>
                                <p className="text-xs mt-1 font-semibold">Impact on Business:</p>
                                <ul className="list-disc list-inside text-xs">
                                    <li>Loss of skilled workers.</li>
                                    <li>Decreased productivity due to absenteeism (illness or attending funerals).</li>
                                    <li>Increased costs for medical aid and training replacement staff.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSSocioEconomicIssuesController,
    Grade10BSSocioEconomicIssuesVisualAids
};
