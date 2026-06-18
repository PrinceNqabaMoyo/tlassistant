import React from 'react';
import { useGrade10BSConceptOfQualityController } from './controller';
import { Target, AlertCircle } from 'lucide-react';

const Grade10BSConceptOfQualityVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <Target className="w-5 h-5" />
                    Concept of Quality
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'control_vs_assurance', 'tqm', 'quality_indicators'].map((tab) => (
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
                            <strong>Quality</strong> refers to the ability of a good or service to satisfy a specific need of the consumer. It is measured against the expectations of the customer.
                        </p>
                        <ul className="list-disc list-inside space-y-1 mt-2">
                            <li>A product must do what it is supposed to do (fit for purpose).</li>
                            <li>It must be durable and safe.</li>
                            <li>Services must be delivered reliably, courteously, and on time.</li>
                        </ul>
                        
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Why is Quality Important?</strong><br />
                            High quality leads to satisfied customers, positive word-of-mouth, repeat sales, and a strong brand image. Poor quality leads to returns, complaints, lower sales, and a damaged reputation.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'control_vs_assurance' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Quality Control vs Quality Assurance</h4>
                        
                        <div className="grid grid-cols-1 gap-3 mt-2">
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800 text-xs">Quality Control (QC)</h5>
                                <p className="text-[11px] mt-1 text-slate-600 mb-2">Finding defects in the final product.</p>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li>Done at the <em>end</em> of the production process.</li>
                                    <li>Involves inspecting, testing, and sampling products.</li>
                                    <li>Goal: Identify and remove defective items before they reach the customer.</li>
                                    <li>Reactive approach.</li>
                                </ul>
                            </div>
                            <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-md">
                                <h5 className="font-semibold text-emerald-800 text-xs">Quality Assurance (QA)</h5>
                                <p className="text-[11px] mt-1 text-slate-600 mb-2">Preventing defects from happening in the first place.</p>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li>Done <em>during and before</em> the production process.</li>
                                    <li>Involves setting up systems, procedures, and training.</li>
                                    <li>Goal: Ensure the process is perfect so the product is automatically perfect.</li>
                                    <li>Proactive approach.</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'tqm' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Total Quality Management (TQM)</h4>
                        <p className="text-xs">An ongoing, company-wide commitment to excellence that involves every employee at every level.</p>
                        
                        <div className="space-y-3 mt-2">
                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800 text-xs">Key Elements of TQM</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1">
                                    <li><strong>Continuous Improvement:</strong> Always looking for better ways to do things.</li>
                                    <li><strong>Customer Focus:</strong> Understanding and exceeding customer expectations.</li>
                                    <li><strong>Employee Involvement:</strong> Empowering workers to take ownership of quality (e.g., using Quality Circles).</li>
                                    <li><strong>Teamwork:</strong> Different departments working together to improve processes.</li>
                                </ul>
                            </div>

                            <div className="p-3 bg-amber-50 border border-amber-200 rounded-md">
                                <h5 className="font-semibold text-amber-800 text-xs">Quality Circles</h5>
                                <p className="text-[11px] mt-1">A small group of employees who meet regularly to discuss, analyze, and solve quality-related problems in their specific work area.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'quality_indicators' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Quality Indicators for Business Functions</h4>
                        <p className="text-xs">How do we know if a specific department is performing well?</p>
                        
                        <div className="space-y-3 mt-2">
                            <div className="p-3 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800 text-xs">Human Resources Function</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1 text-slate-600">
                                    <li>Low staff turnover and low absenteeism.</li>
                                    <li>Hiring the best candidates for the job.</li>
                                    <li>Effective training programs leading to highly skilled workers.</li>
                                </ul>
                            </div>

                            <div className="p-3 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800 text-xs">Marketing Function</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1 text-slate-600">
                                    <li>Increasing market share and sales volume.</li>
                                    <li>Positive customer reviews and brand loyalty.</li>
                                    <li>Effective advertising campaigns that reach the target market.</li>
                                </ul>
                            </div>

                            <div className="p-3 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800 text-xs">Production Function</h5>
                                <ul className="list-disc list-inside mt-1 text-[11px] space-y-1 text-slate-600">
                                    <li>Low number of defective products.</li>
                                    <li>Efficient use of raw materials (low wastage).</li>
                                    <li>Meeting production targets and deadlines.</li>
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
    useGrade10BSConceptOfQualityController,
    Grade10BSConceptOfQualityVisualAids
};
