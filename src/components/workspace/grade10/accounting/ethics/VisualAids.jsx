import React from 'react';

export const Grade10EthicsVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen }) => {
    const tab = visualAidsTab || 'concepts';

    const Card = ({ title, children }) => (
        <div className="bg-white border border-gray-200 rounded-lg p-3">
            <div className="text-sm font-bold text-gray-900 mb-1">{title}</div>
            <div className="text-sm text-gray-800">{children}</div>
        </div>
    );

    return (
        <div className="p-4">
            <div className="flex items-center justify-between mb-3">
                <h3 className="text-lg font-bold text-gray-900">Accounting Visual Aids</h3>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="px-3 py-1 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-md text-sm font-semibold"
                >
                    Close
                </button>
            </div>

            <div className="flex gap-2 mb-4">
                <button
                    onClick={() => setVisualAidsTab('concepts')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'concepts' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Concepts
                </button>
                <button
                    onClick={() => setVisualAidsTab('keywords')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'keywords' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Keywords
                </button>
                <button
                    onClick={() => setVisualAidsTab('exam')}
                    className={`px-3 py-1 rounded-md text-sm font-semibold border ${tab === 'exam' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-indigo-700 border-indigo-200 hover:bg-indigo-50'}`}
                >
                    Exam tips
                </button>
            </div>

            {tab === 'concepts' && (
                <div className="space-y-3">
                    <Card title="Code of ethics (what it is)">
                        <div className="space-y-1">
                            <div>A statement of the business's norms and beliefs.</div>
                            <div>Describes acceptable behaviour in the workplace.</div>
                            <div>Helps people know what is right and wrong in specific situations.</div>
                        </div>
                    </Card>

                    <Card title="Who is responsible?">
                        <div className="space-y-1">
                            <div><span className="font-semibold">Employees:</span> act ethically towards colleagues, clients, and the profession.</div>
                            <div><span className="font-semibold">Employers/managers:</span> set fair rules and model the same behaviour.</div>
                            <div><span className="font-semibold">Best practice:</span> involve employees when creating the code.</div>
                        </div>
                    </Card>

                    <Card title="Responsible management (3 Ps)">
                        <div className="space-y-1">
                            <div><span className="font-semibold">People:</span> treat stakeholders ethically.</div>
                            <div><span className="font-semibold">Planet:</span> respect the environment and resources.</div>
                            <div><span className="font-semibold">Profit:</span> aim for profit using ethical practices.</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'keywords' && (
                <div className="space-y-3">
                    <Card title="Quick memory cards">
                        <div className="space-y-1">
                            <div><span className="font-semibold">Integrity:</span> honesty; upholding values and norms.</div>
                            <div><span className="font-semibold">Accountability:</span> take responsibility; justify actions.</div>
                            <div><span className="font-semibold">Transparency:</span> nothing to hide; actions are clear.</div>
                            <div><span className="font-semibold">Objectivity:</span> unbiased; based on facts not feelings.</div>
                            <div><span className="font-semibold">Confidentiality:</span> keep sensitive business information private.</div>
                            <div><span className="font-semibold">Fairness:</span> reasonable and just; no bias.</div>
                        </div>
                    </Card>
                </div>
            )}

            {tab === 'exam' && (
                <div className="space-y-3 text-sm text-gray-800">
                    <Card title="How to answer ethics questions">
                        <div className="space-y-1">
                            <div>Pretend you work in the business.</div>
                            <div>Name the principle (e.g. integrity) and apply it to the situation.</div>
                            <div>Explain the consequence if the principle is ignored (trust, legal costs, reputation).</div>
                        </div>
                    </Card>

                    <Card title="Unethical business: likely downsides">
                        <div className="space-y-1">
                            <div>Legal costs and extra regulation.</div>
                            <div>Lost trust of suppliers and customers; public backlash.</div>
                            <div>Harder to attract investors and quality staff.</div>
                        </div>
                    </Card>
                </div>
            )}
        </div>
    );
};
