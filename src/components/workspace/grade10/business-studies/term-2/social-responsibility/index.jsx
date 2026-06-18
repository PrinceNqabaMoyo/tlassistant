import React from 'react';
import { useGrade10BSSocialResponsibilityController } from './controller';
import { BookOpen, AlertCircle } from 'lucide-react';

const Grade10BSSocialResponsibilityVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    return (
        <div className="flex flex-col h-full bg-white text-slate-800">
            <div className="flex-none p-4 border-b border-slate-200 flex justify-between items-center bg-indigo-50">
                <h3 className="font-semibold text-lg text-indigo-900 flex items-center gap-2">
                    <BookOpen className="w-5 h-5" />
                    Social Responsibility
                </h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="p-2 hover:bg-indigo-100 rounded-full transition-colors text-indigo-700"
                >
                    <AlertCircle className="w-5 h-5" />
                </button>
            </div>

            <div className="flex-none flex space-x-1 p-2 bg-slate-50 border-b border-slate-200 overflow-x-auto">
                {['overview', 'csr_vs_csi', 'why_be_responsible', 'initiatives'].map((tab) => (
                    <button
                        key={tab}
                        onClick={() => setVisualAidsTab(tab)}
                        className={`px-3 py-1.5 text-sm font-medium rounded-md whitespace-nowrap transition-colors ${
                            visualAidsTab === tab
                                ? 'bg-indigo-100 text-indigo-700'
                                : 'text-slate-600 hover:bg-slate-200'
                        }`}
                    >
                        {tab === 'csr_vs_csi' ? 'CSR vs CSI' : tab.split('_').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ')}
                    </button>
                ))}
            </div>

            <div className="flex-1 overflow-y-auto p-4 custom-scrollbar">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <p>
                            Social responsibility is the ethical obligation of a business to act in ways that benefit society and the environment, not just its own profits.
                        </p>
                        <div className="bg-slate-50 p-3 rounded border border-slate-200 mt-2 text-xs">
                            <strong>Key Concept:</strong> Businesses operate within a community. They take resources (like labour and raw materials) from the community, so they have a moral obligation to give back and ensure they do no harm.
                        </div>
                    </div>
                )}

                {visualAidsTab === 'csr_vs_csi' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">CSR vs. CSI</h4>
                        <p className="text-xs mb-2">It's important to understand the difference between these two concepts.</p>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-blue-50 border border-blue-200 rounded-md">
                                <h5 className="font-semibold text-blue-800">Corporate Social Responsibility (CSR)</h5>
                                <p className="text-xs mt-1">The <strong>broad concept</strong> or mindset where a business takes responsibility for its impact on society and the environment.</p>
                                <p className="text-xs mt-1 italic">Example: A company policy to reduce carbon emissions and treat workers fairly.</p>
                            </div>
                            
                            <div className="p-3 bg-emerald-50 border border-emerald-200 rounded-md">
                                <h5 className="font-semibold text-emerald-800">Corporate Social Investment (CSI)</h5>
                                <p className="text-xs mt-1">The <strong>actual money or resources</strong> spent on specific projects to uplift the community.</p>
                                <p className="text-xs mt-1 italic">Example: Building a new clinic in the local town or donating computers to a school.</p>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'why_be_responsible' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Why Should Businesses Be Socially Responsible?</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Advantages for the Business</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li><strong>Good PR:</strong> Improves the image and reputation of the business.</li>
                                    <li><strong>Customer Loyalty:</strong> Consumers prefer to buy from ethical companies.</li>
                                    <li><strong>Attracts Talent:</strong> Good employees want to work for caring companies.</li>
                                    <li><strong>Tax Benefits:</strong> Some CSI projects qualify for tax rebates.</li>
                                </ul>
                            </div>

                            <div className="p-3 bg-slate-50 border border-slate-200 rounded-md">
                                <h5 className="font-semibold text-slate-800">Impact on the Community</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Improves the standard of living.</li>
                                    <li>Creates job opportunities or develops skills.</li>
                                    <li>Helps solve socio-economic issues (like poverty or poor education).</li>
                                </ul>
                            </div>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'initiatives' && (
                    <div className="space-y-4 text-sm text-slate-700">
                        <h4 className="font-semibold text-slate-800">Examples of Social Responsibility Initiatives</h4>
                        
                        <div className="space-y-3">
                            <div className="p-3 bg-purple-50 border border-purple-200 rounded-md">
                                <h5 className="font-semibold text-purple-800">For Employees</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Providing wellness programs (e.g., free HIV/AIDS testing).</li>
                                    <li>Offering bursaries for employees' children.</li>
                                    <li>Providing skills development and training.</li>
                                </ul>
                            </div>
                            
                            <div className="p-3 bg-orange-50 border border-orange-200 rounded-md">
                                <h5 className="font-semibold text-orange-800">For the Community & Environment</h5>
                                <ul className="list-disc list-inside mt-1 text-xs space-y-1">
                                    <li>Sponsoring local sports teams.</li>
                                    <li>Starting feeding schemes for local schools.</li>
                                    <li>Recycling programs and reducing waste.</li>
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
    useGrade10BSSocialResponsibilityController,
    Grade10BSSocialResponsibilityVisualAids
};
