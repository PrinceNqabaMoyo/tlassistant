import React from 'react';
import { useGrade10BSBusinessFunctionsController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSBusinessFunctionsVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Business Functions
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'leadership_vs_management', 'levels_tasks', 'structures'].map((tab) => (
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
                            Business functions are the activities carried out by an enterprise. General management usually oversees all other business functions.
                        </p>
                        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 mt-4">
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>General Management:</strong> Oversees everything, sets strategy, leads, organises, controls.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Administration:</strong> Collects, processes, and stores information for decision-making. Handles IT.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Financial:</strong> Acquires and utilizes funds for efficient operations.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Purchasing:</strong> Buys goods/services needed to operate and manufacture.
                            </div>
                            <div className="p-2 bg-slate-50 border border-slate-200 rounded-md text-xs">
                                <strong>Public Relations:</strong> Continuous maintenance of a public image.
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'leadership_vs_management' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Leadership vs Management</h4>
                        
                        <div className="flex flex-col sm:flex-row gap-4">
                            <div className="flex-1 p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800 border-b border-blue-200 pb-2 mb-2">Leadership</h5>
                                <ul className="list-disc list-inside space-y-1 text-xs">
                                    <li>Creates a vision / sets direction.</li>
                                    <li>Creates the team and inspires subordinates.</li>
                                    <li>Influences human behaviour.</li>
                                    <li>Communicates using vision/charisma.</li>
                                    <li>Born with natural/instinctive skills.</li>
                                </ul>
                            </div>
                            
                            <div className="flex-1 p-3 bg-green-50 border border-green-200 rounded-md">
                                <h5 className="font-semibold text-green-800 border-b border-green-200 pb-2 mb-2">Management</h5>
                                <ul className="list-disc list-inside space-y-1 text-xs">
                                    <li>Understands the goals of the business.</li>
                                    <li>Ensures given tasks are completed.</li>
                                    <li>Guides human behaviour.</li>
                                    <li>Communicates through management functions.</li>
                                    <li>Appointed to the position.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'levels_tasks' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Levels of Management & Tasks</h4>
                        
                        <div className="space-y-2">
                            <div className="p-2 bg-purple-50 border border-purple-200 rounded-md">
                                <strong className="text-purple-800">Top Level:</strong> Long-term strategic decisions (CEOs, directors). Gives direction to vision/mission.
                            </div>
                            <div className="p-2 bg-purple-50 border border-purple-200 rounded-md">
                                <strong className="text-purple-800">Middle Level:</strong> Medium-term tactical decisions (Department managers). Executes plans, passes info downwards.
                            </div>
                            <div className="p-2 bg-purple-50 border border-purple-200 rounded-md">
                                <strong className="text-purple-800">Lower Level:</strong> Short-term operational decisions (Foreman, supervisor). Implements objectives, guides workers.
                            </div>
                        </div>

                        <h5 className="font-semibold text-slate-800 mt-4">5 Management Tasks:</h5>
                        <ul className="list-disc list-inside space-y-1 text-xs">
                            <li><strong>Planning:</strong> Setting goals, formulating strategies/tactics.</li>
                            <li><strong>Organising:</strong> Bringing resources together, delegating, coordinating.</li>
                            <li><strong>Leading/Directing:</strong> Motivating staff, supervising, guiding direction.</li>
                            <li><strong>Controlling:</strong> Establishing standards, measuring actual vs planned, corrective action.</li>
                            <li><strong>Risk Management:</strong> Identifying, assessing, handling risks (contingency plans).</li>
                        </ul>
                    </div>
                )}

                {visualAidsTab === 'structures' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Organisational Structures</h4>
                        <p className="text-xs mb-2">Factors influencing structure: Size, Strategy, Technology, Resources.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Functional Structure</h5>
                                <p className="text-xs mt-1">Employees get instructions from more than one manager based on the plan being executed. Can confuse employees.</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Project Structure</h5>
                                <p className="text-xs mt-1">Temporary structure built around specific project teams drawn from different departments.</p>
                            </div>
                            
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Matrix Structure</h5>
                                <p className="text-xs mt-1">Structured around projects but employees remain in their departments. Passed from team to team for different phases.</p>
                            </div>
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export {
    useGrade10BSBusinessFunctionsController,
    Grade10BSBusinessFunctionsVisualAids
};
