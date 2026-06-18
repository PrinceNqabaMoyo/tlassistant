import React from 'react';
import { useGrade10BSMicroEnvironmentController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSMicroEnvironmentVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Micro Environment
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'mission', 'culture', 'functions'].map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setVisualAidsTab(tab)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            visualAidsTab === tab
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab.charAt(0).toUpperCase() + tab.slice(1).replace('_', ' ')}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <p>
                            The <strong>micro environment</strong> of a business includes everything inside the business. All internal affairs are managed by the directors or owners. The business has full control over its micro environment.
                        </p>
                        <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                            <h4 className="font-semibold text-blue-800 mb-2">Concentric Circles Model</h4>
                            <ul className="list-disc list-inside space-y-1">
                                <li><strong>Micro Environment:</strong> Innermost circle (full control)</li>
                                <li><strong>Market Environment:</strong> Middle circle (partial control/influence)</li>
                                <li><strong>Macro Environment:</strong> Outermost circle (no control)</li>
                            </ul>
                        </div>
                        <p>
                            <strong>Key Components:</strong>
                        </p>
                        <ul className="list-disc list-inside space-y-1">
                            <li>Vision, mission, goals and objectives</li>
                            <li>Organisational culture</li>
                            <li>Organisational resources</li>
                            <li>Management and leadership</li>
                            <li>Organisational structure</li>
                            <li>The eight business functions</li>
                        </ul>
                    </div>
                )}

                {visualAidsTab === 'mission' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Vision vs Mission vs Goals vs Objectives</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Vision</h5>
                                <p className="text-xs mt-1">Describes the long-term goal, where the business sees itself in the future (the dream).</p>
                                <p className="text-xs mt-1 italic">Example: "To become globally competitive."</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Mission Statement</h5>
                                <p className="text-xs mt-1">Describes what the business provides or produces, and why it exists.</p>
                                <p className="text-xs mt-1 italic">Example: "To provide professional hairdressing services and supply beauty products."</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Goals</h5>
                                <p className="text-xs mt-1">Long-term plans the business wants to accomplish.</p>
                                <p className="text-xs mt-1 italic">Example: "To open five more branches in the next five years."</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Objectives</h5>
                                <p className="text-xs mt-1">Short-term steps describing exactly how goals will be achieved.</p>
                                <p className="text-xs mt-1 italic">Example: "We will upskill our current employees by offering specific training."</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'culture' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Organisational Culture & Resources</h4>
                        
                        <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                            <h5 className="font-semibold text-purple-800">Organisational Culture</h5>
                            <ul className="list-disc list-inside mt-2 space-y-1 text-xs">
                                <li>Defines internal/external identity and core values.</li>
                                <li>Turns employees into ambassadors.</li>
                                <li>Helps retain employees and clients.</li>
                                <li>Includes values, beliefs, norms, and standards.</li>
                            </ul>
                        </div>

                        <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-md mt-4">
                            <h5 className="font-semibold text-emerald-800">Organisational Resources</h5>
                            <ul className="list-disc list-inside mt-2 space-y-1 text-xs">
                                <li><strong>Human:</strong> The workforce.</li>
                                <li><strong>Physical:</strong> Tangible items (buildings, machinery).</li>
                                <li><strong>Financial:</strong> Capital (loans, overdrafts).</li>
                                <li><strong>Technological:</strong> Intangibles (software, patents).</li>
                            </ul>
                        </div>
                        
                        <div className="p-3 bg-orange-50 border border-orange-200 rounded-md mt-4">
                            <h5 className="font-semibold text-orange-800">Organisational Structure (Organogram)</h5>
                            <p className="text-xs mt-1">Shows hierarchical levels of authority and responsibility, helping to ensure smooth coordination between departments.</p>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'functions' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">The Eight Business Functions</h4>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>General Management:</strong> Plans, organises, leads, and controls resources.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Purchasing:</strong> Buys resources needed for production.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Production:</strong> Changes raw materials into finished products.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Marketing:</strong> Undertakes market research and advertising.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Public Relations:</strong> Creates a good public image.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Human Resources:</strong> Attracts and trains employees.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Administration:</strong> Collects, processes, and stores data.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Financial:</strong> Manages funds and financial assets.
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSMicroEnvironmentController,
    Grade10BSMicroEnvironmentVisualAids
};
