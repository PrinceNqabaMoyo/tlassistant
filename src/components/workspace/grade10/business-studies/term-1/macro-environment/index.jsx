import React from 'react';
import { useGrade10BSMacroEnvironmentController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSMacroEnvironmentVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    The Macro Environment
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'pestle_factors'].map((tab) => (
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
                            The Macro Environment refers to the broader, global forces that affect a business. The business has NO control over this environment, but must adapt to it to survive.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> To analyse the macro environment, businesses use the <strong>PESTLE</strong> framework. This helps them identify threats and opportunities coming from the outside world.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'pestle_factors' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">PESTLE Analysis</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-red-50 border border-red-200 rounded-md">
                                <h5 className="font-semibold text-red-800">Political</h5>
                                <p className="text-xs mt-1">Government policies, political stability, trade agreements, and foreign relations. Example: A change in government leadership might lead to different business policies.</p>
                            </div>
                            
                            <div className="p-3 bg-amber-50 border border-amber-200 rounded-md">
                                <h5 className="font-semibold text-amber-800">Economic</h5>
                                <p className="text-xs mt-1">Inflation rates, interest rates, exchange rates, economic growth/recession, and unemployment. Example: High inflation reduces consumers' purchasing power.</p>
                            </div>

                            <div className="p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800">Social</h5>
                                <p className="text-xs mt-1">Demographics, cultural trends, lifestyle changes, education levels, and health trends. Example: An aging population changes the types of products demanded.</p>
                            </div>

                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Technological</h5>
                                <p className="text-xs mt-1">Innovation, automation, research and development (R&D), and tech infrastructure. Example: AI replacing certain manual tasks or e-commerce replacing physical stores.</p>
                            </div>

                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800">Legal</h5>
                                <p className="text-xs mt-1">Labour laws (BCEA, LRA), Consumer Protection Act, health and safety regulations, and tax laws. Example: A new minimum wage law increases labour costs.</p>
                            </div>

                            <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-md">
                                <h5 className="font-semibold text-emerald-800">Environmental (Physical)</h5>
                                <p className="text-xs mt-1">Climate change, weather conditions, natural disasters, pollution, and resource scarcity. Example: A severe drought negatively affects agricultural businesses.</p>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSMacroEnvironmentController,
    Grade10BSMacroEnvironmentVisualAids
};
