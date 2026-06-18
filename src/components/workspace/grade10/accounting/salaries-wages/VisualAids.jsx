import React from 'react';

export const Grade10SalariesWagesVisualAids = ({
    visualAidsTab = 'overview',
    setVisualAidsTab,
    setVisualAidsOpen,
}) => {
    const tabs = [
        { key: 'overview', label: 'Overview' },
        { key: 'glossary', label: 'Key Terms' },
        { key: 'formulas', label: 'Formulas' },
        { key: 'deductions', label: 'Deductions' },
    ];

    return (
        <div className="bg-white rounded-xl border border-slate-200 shadow-sm overflow-hidden">
            {/* Header */}
            <div className="flex items-center justify-between px-4 py-3 bg-gradient-to-r from-teal-50 to-emerald-50 border-b border-slate-200">
                <h3 className="text-sm font-semibold text-teal-900">📋 Salaries & Wages Reference</h3>
                {setVisualAidsOpen && (
                    <button onClick={() => setVisualAidsOpen(false)} className="text-slate-400 hover:text-slate-600 text-lg leading-none">&times;</button>
                )}
            </div>

            {/* Tabs */}
            <div className="flex border-b border-slate-100 px-2 pt-1 gap-1 overflow-x-auto">
                {tabs.map(t => (
                    <button
                        key={t.key}
                        className={`px-3 py-1.5 text-xs font-medium rounded-t transition-colors whitespace-nowrap ${visualAidsTab === t.key ? 'bg-teal-100 text-teal-800 border-b-2 border-teal-500' : 'text-slate-500 hover:text-slate-700 hover:bg-slate-50'}`}
                        onClick={() => setVisualAidsTab?.(t.key)}
                    >
                        {t.label}
                    </button>
                ))}
            </div>

            {/* Content */}
            <div className="p-4 text-sm text-slate-700 space-y-3 max-h-[400px] overflow-y-auto">
                {visualAidsTab === 'overview' && (
                    <div className="space-y-2">
                        <p className="font-medium text-teal-800">Salaries & Wages Journals</p>
                        <ul className="list-disc pl-5 space-y-1 text-xs">
                            <li><strong>Salary</strong> — monthly, permanent employees, agreed annual amount ÷ 12</li>
                            <li><strong>Wage</strong> — weekly, hourly rate × hours worked</li>
                            <li><strong>Ordinary time</strong> — 40 hours/week standard</li>
                            <li><strong>Overtime</strong> — hours exceeding 40, at higher rate</li>
                            <li><strong>Gross</strong> = Basic + Overtime (wages) or Annual ÷ 12 (salary)</li>
                            <li><strong>Net</strong> = Gross − Total Deductions</li>
                        </ul>
                    </div>
                )}

                {visualAidsTab === 'glossary' && (
                    <div className="space-y-2">
                        <table className="w-full text-xs">
                            <thead><tr className="bg-slate-50"><th className="text-left p-1.5 font-semibold">Term</th><th className="text-left p-1.5 font-semibold">Definition</th></tr></thead>
                            <tbody>
                                <tr className="border-t"><td className="p-1.5 font-medium">PAYE</td><td className="p-1.5">Pay-As-You-Earn income tax deducted monthly</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">UIF</td><td className="p-1.5">Unemployment Insurance Fund — employee & employer each contribute</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">SDL</td><td className="p-1.5">Skills Development Levy — 1% of gross salary/wages, employer pays</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Pension Fund</td><td className="p-1.5">Retirement savings — % of gross salary, employee + employer contribute</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Medical Aid</td><td className="p-1.5">Health insurance — employee + employer contribute</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Salary Advice</td><td className="p-1.5">Slip showing gross salary, deductions, and net salary</td></tr>
                                <tr className="border-t"><td className="p-1.5 font-medium">Notch/Scale</td><td className="p-1.5">Position on salary scale; annual increments until max</td></tr>
                            </tbody>
                        </table>
                    </div>
                )}

                {visualAidsTab === 'formulas' && (
                    <div className="space-y-3">
                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-3">
                            <p className="font-semibold text-blue-800 text-xs mb-1">Wage Calculation</p>
                            <p className="text-xs">Basic Wage = Ordinary hours × Rate/hour</p>
                            <p className="text-xs">Overtime = Extra hours × Overtime rate</p>
                            <p className="text-xs font-medium mt-1">Gross Wage = Basic Wage + Overtime</p>
                        </div>
                        <div className="bg-green-50 border border-green-200 rounded-lg p-3">
                            <p className="font-semibold text-green-800 text-xs mb-1">Salary Calculation</p>
                            <p className="text-xs">Monthly Salary = Annual Salary ÷ 12</p>
                            <p className="text-xs">Bonus = Monthly Salary × Bonus %</p>
                        </div>
                        <div className="bg-amber-50 border border-amber-200 rounded-lg p-3">
                            <p className="font-semibold text-amber-800 text-xs mb-1">Net Pay</p>
                            <p className="text-xs font-medium">Net Pay = Gross − (PAYE + Pension + Medical + UIF)</p>
                        </div>
                    </div>
                )}

                {visualAidsTab === 'deductions' && (
                    <div className="space-y-2">
                        <p className="font-medium text-teal-800">Employee Deductions</p>
                        <ul className="list-disc pl-5 space-y-1 text-xs">
                            <li>PAYE (income tax) — based on taxable income tables</li>
                            <li>Pension fund — % of gross salary</li>
                            <li>Medical aid — fixed or % amount</li>
                            <li>UIF — 1% of ordinary time earnings</li>
                        </ul>
                        <p className="font-medium text-teal-800 mt-2">Employer Contributions</p>
                        <ul className="list-disc pl-5 space-y-1 text-xs">
                            <li>SDL — 1% of total gross salaries/wages</li>
                            <li>UIF — matches employee's 1%</li>
                            <li>Pension fund — often rand-for-rand match</li>
                            <li>Medical aid — often R1.50 per R1 of employee contribution</li>
                        </ul>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Grade10SalariesWagesVisualAids;
