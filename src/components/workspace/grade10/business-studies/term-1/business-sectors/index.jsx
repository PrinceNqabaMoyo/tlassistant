import React from 'react';
import { useGrade10BSBusinessSectorsController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSBusinessSectorsVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Business Sectors
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'primary_sector', 'secondary_sector', 'tertiary_sector'].map((tab) => (
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
                            The economy is divided into three main business sectors. Each sector plays a vital role in the production and distribution of goods and services.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> The sectors are interdependent. The primary sector extracts resources, the secondary sector manufactures them into products, and the tertiary sector sells and distributes them.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'primary_sector' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">The Primary Sector</h4>
                        <p>This sector involves the extraction and harvesting of raw materials from nature.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800">Examples of Industries</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Agriculture (Farming)</li>
                                    <li>Mining</li>
                                    <li>Fishing</li>
                                    <li>Forestry</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Characteristics</h5>
                                <p className="text-xs mt-1">Labour-intensive, provides raw materials for the secondary sector, and is highly dependent on natural resources and weather conditions.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'secondary_sector' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">The Secondary Sector</h4>
                        <p>This sector processes and manufactures raw materials into finished or semi-finished goods.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-orange-50 border border-orange-200 rounded-md">
                                <h5 className="font-semibold text-orange-800">Examples of Industries</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Manufacturing (e.g. car factories, clothing factories)</li>
                                    <li>Construction (e.g. building houses, roads)</li>
                                    <li>Energy generation (e.g. power plants)</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Characteristics</h5>
                                <p className="text-xs mt-1">Capital-intensive (uses heavy machinery), adds value to raw materials, and relies on the primary sector for inputs.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'tertiary_sector' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">The Tertiary Sector</h4>
                        <p>This sector provides services to other businesses and consumers. It also distributes goods from the secondary sector.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Examples of Industries</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Retail and Wholesale (shops, supermarkets)</li>
                                    <li>Financial Services (banks, insurance)</li>
                                    <li>Transport and Logistics</li>
                                    <li>Education, Healthcare, Tourism</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Characteristics</h5>
                                <p className="text-xs mt-1">Service-oriented, bridges the gap between producers and consumers, and is often the largest contributor to a country's GDP.</p>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSBusinessSectorsController,
    Grade10BSBusinessSectorsVisualAids
};
