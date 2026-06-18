import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const CashReceiptsJournalInput = ({ initialData, onChange, isSubmitted }) => {
    const [journalData, setJournalData] = useState(initialData || {
        companyName: '',
        month: '',
        journalNumber: '',
        rows: [{ doc: '', day: '', details: '', fol: '', analysis: { main: '', cents: '' }, bank: { main: '', cents: '' }, income: { main: '', cents: '' }, sales: { main: '', cents: '' }, costOfSales: { main: '', cents: '' }, debtorsControl: { main: '', cents: '' }, sundry_amount: { main: '', cents: '' }, sundry_fol: '', sundry_details: '' }]
    });

    useEffect(() => {
        onChange(journalData);
    }, [journalData, onChange]);

    const handleHeaderChange = (field, value) => {
        if (isSubmitted) return;
        setJournalData(prev => ({ ...prev, [field]: value }));
    };

    const handleCellChange = (rowIndex, field, value) => {
        if (isSubmitted) return;
        const newRows = [...journalData.rows];
        newRows[rowIndex][field] = value;
        setJournalData(prev => ({ ...prev, rows: newRows }));
    };
    
    const handleAddRow = () => {
        if (isSubmitted) return;
        const newRow = { doc: '', day: '', details: '', fol: '', analysis: { main: '', cents: '' }, bank: { main: '', cents: '' }, income: { main: '', cents: '' }, sales: { main: '', cents: '' }, costOfSales: { main: '', cents: '' }, debtorsControl: { main: '', cents: '' }, sundry_amount: { main: '', cents: '' }, sundry_fol: '', sundry_details: '' };
        setJournalData(prev => ({ ...prev, rows: [...prev.rows, newRow] }));
    };



    // Calculate totals for validation
    const calculateTotals = () => {
        const totals = journalData.rows.reduce((acc, row) => {
            const safe = (obj) => obj ? obj : { main: 0, cents: 0 };
            const analysis = parseFloat(safe(row.analysis).main || 0) + parseFloat(safe(row.analysis).cents || 0) / 100;
            const bank = parseFloat(safe(row.bank).main || 0) + parseFloat(safe(row.bank).cents || 0) / 100;
            const income = parseFloat(safe(row.income).main || 0) + parseFloat(safe(row.income).cents || 0) / 100;
            const sales = parseFloat(safe(row.sales).main || 0) + parseFloat(safe(row.sales).cents || 0) / 100;
            const costOfSales = parseFloat(safe(row.costOfSales).main || 0) + parseFloat(safe(row.costOfSales).cents || 0) / 100;
            const debtorsControl = parseFloat(safe(row.debtorsControl).main || 0) + parseFloat(safe(row.debtorsControl).cents || 0) / 100;
            const sundry = parseFloat(safe(row.sundry_amount).main || 0) + parseFloat(safe(row.sundry_amount).cents || 0) / 100;
            return {
                analysis: acc.analysis + analysis,
                bank: acc.bank + bank,
                income: acc.income + income,
                sales: acc.sales + sales,
                costOfSales: acc.costOfSales + costOfSales,
                debtorsControl: acc.debtorsControl + debtorsControl,
                sundry: acc.sundry + sundry
            };
        }, { analysis: 0, bank: 0, income: 0, sales: 0, costOfSales: 0, debtorsControl: 0, sundry: 0 });
        return totals;
    };

    const totals = calculateTotals();

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            <div className="flex justify-between items-center mb-2 flex-wrap">
                <div className="flex items-center space-x-2">
                    <span className="font-bold">Cash Receipts Journal of</span>
                    <input type="text" value={journalData.companyName} onChange={e => handleHeaderChange('companyName', e.target.value)} disabled={isSubmitted} className="p-1 border-b-2 border-gray-400 bg-transparent focus:outline-none focus:border-blue-500 w-48" placeholder="Company Name" />
                    <span className="font-bold">for</span>
                    <input type="text" value={journalData.month} onChange={e => handleHeaderChange('month', e.target.value)} disabled={isSubmitted} className="p-1 border-b-2 border-gray-400 bg-transparent focus:outline-none focus:border-blue-500 w-32" placeholder="Month 20XX" />
                </div>
                <div className="flex items-center space-x-2">
                    <span className="font-bold">CRJ</span>
                     <input type="text" value={journalData.journalNumber} onChange={e => handleHeaderChange('journalNumber', e.target.value)} disabled={isSubmitted} className="p-1 border-b-2 border-gray-400 bg-transparent focus:outline-none focus:border-blue-500 w-12" placeholder="No." />
                </div>
            </div>
            <div className="overflow-x-auto">
                <table className="min-w-full border-2 border-gray-800">
                    <thead className="bg-gray-200">
                        <tr className="border-b-2 border-gray-800">
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Doc. no.</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Day</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Details</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Fol.</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Analysis of receipts</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Bank</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Current income</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Sales</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Cost of sales</th>
                            <th rowSpan="2" className="p-2 border-r-2 border-gray-800">Debtors' control</th>
                            <th colSpan="3" className="p-2">Sundry accounts</th>
                        </tr>
                        <tr className="border-b-2 border-gray-800">
                            <th className="p-2 border-r border-gray-500">Amount</th>
                            <th className="p-2 border-r border-gray-500">Fol.</th>
                            <th className="p-2">Details</th>
                        </tr>
                    </thead>
                    <tbody>
                        {journalData.rows.map((row, rowIndex) => (
                            <tr key={rowIndex} className="border-b border-gray-400">
                                <td className="border-r-2 border-gray-800 p-1"><input type="text" value={row.doc} onChange={e => handleCellChange(rowIndex, 'doc', e.target.value)} disabled={isSubmitted} className="w-full p-1 bg-transparent focus:outline-none" /></td>
                                <td className="border-r-2 border-gray-800 p-1"><input type="text" value={row.day} onChange={e => handleCellChange(rowIndex, 'day', e.target.value)} disabled={isSubmitted} className="w-full p-1 bg-transparent focus:outline-none" /></td>
                                <td className="border-r-2 border-gray-800 p-1"><input type="text" value={row.details} onChange={e => handleCellChange(rowIndex, 'details', e.target.value)} disabled={isSubmitted} className="w-full p-1 bg-transparent focus:outline-none" /></td>
                                <td className="border-r-2 border-gray-800 p-1"><input type="text" value={row.fol} onChange={e => handleCellChange(rowIndex, 'fol', e.target.value)} disabled={isSubmitted} className="w-full p-1 bg-transparent focus:outline-none" /></td>
                                <td className="border-r-2 border-gray-800 p-1"><MoneyInput value={row.analysis} onChange={value => handleCellChange(rowIndex, 'analysis', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r-2 border-gray-800 p-1"><MoneyInput value={row.bank} onChange={value => handleCellChange(rowIndex, 'bank', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r-2 border-gray-800 p-1"><MoneyInput value={row.income} onChange={value => handleCellChange(rowIndex, 'income', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r-2 border-gray-800 p-1"><MoneyInput value={row.sales} onChange={value => handleCellChange(rowIndex, 'sales', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r-2 border-gray-800 p-1"><MoneyInput value={row.costOfSales} onChange={value => handleCellChange(rowIndex, 'costOfSales', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r-2 border-gray-800 p-1"><MoneyInput value={row.debtorsControl} onChange={value => handleCellChange(rowIndex, 'debtorsControl', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r border-gray-500 p-1"><MoneyInput value={row.sundry_amount} onChange={value => handleCellChange(rowIndex, 'sundry_amount', value)} isSubmitted={isSubmitted} /></td>
                                <td className="border-r border-gray-500 p-1"><input type="text" value={row.sundry_fol} onChange={e => handleCellChange(rowIndex, 'sundry_fol', e.target.value)} disabled={isSubmitted} className="w-full p-1 bg-transparent focus:outline-none" /></td>
                                <td className="p-1"><input type="text" value={row.sundry_details} onChange={e => handleCellChange(rowIndex, 'sundry_details', e.target.value)} disabled={isSubmitted} className="w-full p-1 bg-transparent focus:outline-none" /></td>
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>
            
            {/* Validation and Totals Section */}
            {isSubmitted && (
                <div className="mt-4 p-3 bg-blue-50 border border-blue-200 rounded-lg">
                    <h4 className="font-bold text-blue-800 mb-2">Journal Totals:</h4>
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-sm">
                        <div><span className="font-semibold">Analysis of receipts:</span> R{totals.analysis.toFixed(2)}</div>
                        <div><span className="font-semibold">Bank:</span> R{totals.bank.toFixed(2)}</div>
                        <div><span className="font-semibold">Current income:</span> R{totals.income.toFixed(2)}</div>
                        <div><span className="font-semibold">Sales:</span> R{totals.sales.toFixed(2)}</div>
                        <div><span className="font-semibold">Cost of sales:</span> R{totals.costOfSales.toFixed(2)}</div>
                        <div><span className="font-semibold">Debtors' control:</span> R{totals.debtorsControl.toFixed(2)}</div>
                        <div><span className="font-semibold">Sundry accounts:</span> R{totals.sundry.toFixed(2)}</div>
                    </div>
                    <div className="mt-2 text-sm">
                        <span className="font-semibold">Balancing check:</span> 
                        <span className={Math.abs(totals.bank - (totals.income + totals.sundry)) < 0.01 ? 'text-green-600' : 'text-red-600'}>
                            {Math.abs(totals.bank - (totals.income + totals.sundry)) < 0.01 ? ' ✓ Balanced' : ' ✗ Not balanced'}
                        </span>
                    </div>
                </div>
            )}
            
            {!isSubmitted && (
                <div className="mt-3 space-x-2">
                    <button onClick={handleAddRow} className="px-4 py-2 bg-blue-500 text-white rounded-md text-sm font-semibold hover:bg-blue-600">Add Row</button>
                </div>
            )}
        </div>
    );
};

export default CashReceiptsJournalInput;
