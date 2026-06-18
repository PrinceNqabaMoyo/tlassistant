import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const DepositSlipInput = ({ initialData, onChange, isSubmitted }) => {
    const [depositData, setDepositData] = useState(initialData || {
        bankName: '',
        businessName: '',
        accountNumber: ['', '', '', '', '', '', '', '', '', '', '', ''],
        date: '',
        depositReference: '',
        detailsOfDepositor: {
            name: '',
            signature: '',
            telephone: ''
        },
        chequesDeposited: [
            { cheque: '', drawer: '', bank: '' },
            { cheque: '', drawer: '', bank: '' },
            { cheque: '', drawer: '', bank: '' }
        ],
        cashDeposited: [
            { label: 'R200', r: '', c: '' },
            { label: 'R100', r: '', c: '' },
            { label: 'R50', r: '', c: '' },
            { label: 'R20', r: '', c: '' },
            { label: 'R10', r: '', c: '' },
            { label: 'R5', r: '', c: '' },
            { label: 'R2', r: '', c: '' },
            { label: 'R1', r: '', c: '' },
            { label: '50c', r: '', c: '' },
            { label: '20c', r: '', c: '' },
            { label: '10c', r: '', c: '' },
            { label: '5c', r: '', c: '' },
            { label: '2c', r: '', c: '' },
            { label: '1c', r: '', c: '' }
        ],
        bankStamp: '',
        totalR: ''
    });

    useEffect(() => {
        onChange(depositData);
    }, [depositData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setDepositData(prev => ({ ...prev, [field]: value }));
    };

    const handleAccountNumberChange = (idx, value) => {
        if (isSubmitted) return;
        const updated = [...depositData.accountNumber];
        updated[idx] = value.replace(/[^0-9]/g, "").slice(0, 1);
        setDepositData(prev => ({ ...prev, accountNumber: updated }));
    };

    const handleDepositorChange = (field, value) => {
        if (isSubmitted) return;
        setDepositData(prev => ({
            ...prev,
            detailsOfDepositor: { ...prev.detailsOfDepositor, [field]: value }
        }));
    };

    const handleChequeChange = (idx, field, value) => {
        if (isSubmitted) return;
        const updated = depositData.chequesDeposited.map((row, i) =>
            i === idx ? { ...row, [field]: value } : row
        );
        setDepositData(prev => ({ ...prev, chequesDeposited: updated }));
    };

    const handleCashChange = (idx, field, value) => {
        if (isSubmitted) return;
        const updated = depositData.cashDeposited.map((row, i) =>
            i === idx ? { ...row, [field]: value.replace(/[^0-9]/g, "") } : row
        );
        setDepositData(prev => ({ ...prev, cashDeposited: updated }));
    };

    const addChequeRow = () => {
        if (isSubmitted) return;
        const newCheque = { cheque: '', drawer: '', bank: '' };
        setDepositData(prev => ({
            ...prev,
            chequesDeposited: [...prev.chequesDeposited, newCheque]
        }));
    };

    const removeChequeRow = (idx) => {
        if (isSubmitted) return;
        const updated = depositData.chequesDeposited.filter((_, i) => i !== idx);
        setDepositData(prev => ({ ...prev, chequesDeposited: updated }));
    };

    // Calculate total cash deposited
    const calculateTotalCash = () => {
        return depositData.cashDeposited.reduce((total, row) => {
            const rands = parseInt(row.r) || 0;
            const cents = parseInt(row.c) || 0;
            return total + rands + (cents / 100);
        }, 0);
    };

    const totalCash = calculateTotalCash();

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            <div className="space-y-6">
                {/* Header Information */}
                <div className="flex flex-wrap gap-4">
                    <div>
                        <label className="block font-semibold text-sm text-gray-700">Bank Name</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={depositData.bankName} 
                            onChange={e => handleFieldChange("bankName", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Enter bank name"
                        />
                    </div>
                    <div>
                        <label className="block font-semibold text-sm text-gray-700">Business Name</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={depositData.businessName} 
                            onChange={e => handleFieldChange("businessName", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Enter business name"
                        />
                    </div>
                    <div>
                        <label className="block font-semibold text-sm text-gray-700">Account Number</label>
                        <div className="flex gap-1">
                            {depositData.accountNumber.map((num, i) => (
                                <input
                                    key={i}
                                    className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-8 text-center"
                                    maxLength={1}
                                    value={num}
                                    onChange={e => handleAccountNumberChange(i, e.target.value)}
                                    disabled={isSubmitted}
                                />
                            ))}
                        </div>
                    </div>
                    <div>
                        <label className="block font-semibold text-sm text-gray-700">Date</label>
                        <input 
                            type="date" 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                            value={depositData.date} 
                            onChange={e => handleFieldChange("date", e.target.value)}
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block font-semibold text-sm text-gray-700">Deposit Reference</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={depositData.depositReference} 
                            onChange={e => handleFieldChange("depositReference", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Enter reference"
                        />
                    </div>
                </div>

                {/* Depositor Details */}
                <div className="border rounded-lg p-4 bg-white">
                    <div className="font-bold mb-3 text-gray-800">Details of Depositor</div>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div>
                            <label className="block text-xs font-medium text-gray-600">Name</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={depositData.detailsOfDepositor.name} 
                                onChange={e => handleDepositorChange("name", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Depositor name"
                            />
                        </div>
                        <div>
                            <label className="block text-xs font-medium text-gray-600">Signature</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={depositData.detailsOfDepositor.signature} 
                                onChange={e => handleDepositorChange("signature", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Signature"
                            />
                        </div>
                        <div>
                            <label className="block text-xs font-medium text-gray-600">Telephone</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={depositData.detailsOfDepositor.telephone} 
                                onChange={e => handleDepositorChange("telephone", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Phone number"
                            />
                        </div>
                    </div>
                </div>

                {/* Cheques and Cash Tables */}
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                    {/* Cheques Deposited */}
                    <div className="bg-white border rounded-lg p-4">
                        <div className="flex justify-between items-center mb-3">
                            <div className="font-bold text-gray-800">Cheques Deposited</div>
                            {!isSubmitted && (
                                <button
                                    onClick={addChequeRow}
                                    className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600 text-sm"
                                >
                                    Add Cheque
                                </button>
                            )}
                        </div>
                        <div className="overflow-x-auto">
                            <table className="w-full border border-gray-300">
                                <thead>
                                    <tr className="bg-gray-100">
                                        <th className="border border-gray-300 px-2 py-1 text-sm font-medium">Cheque Number</th>
                                        <th className="border border-gray-300 px-2 py-1 text-sm font-medium">Drawer's Name</th>
                                        <th className="border border-gray-300 px-2 py-1 text-sm font-medium">Bank</th>
                                        {!isSubmitted && <th className="border border-gray-300 px-2 py-1 text-sm font-medium">Action</th>}
                                    </tr>
                                </thead>
                                <tbody>
                                    {depositData.chequesDeposited.map((row, i) => (
                                        <tr key={i}>
                                            <td className="border border-gray-300 px-2 py-1">
                                                <input 
                                                    className="w-full p-1 border-none focus:outline-none focus:ring-1 focus:ring-blue-500"
                                                    value={row.cheque} 
                                                    onChange={e => handleChequeChange(i, "cheque", e.target.value)}
                                                    disabled={isSubmitted}
                                                    placeholder="Cheque number"
                                                />
                                            </td>
                                            <td className="border border-gray-300 px-2 py-1">
                                                <input 
                                                    className="w-full p-1 border-none focus:outline-none focus:ring-1 focus:ring-blue-500"
                                                    value={row.drawer} 
                                                    onChange={e => handleChequeChange(i, "drawer", e.target.value)}
                                                    disabled={isSubmitted}
                                                    placeholder="Drawer name"
                                                />
                                            </td>
                                            <td className="border border-gray-300 px-2 py-1">
                                                <input 
                                                    className="w-full p-1 border-none focus:outline-none focus:ring-1 focus:ring-blue-500"
                                                    value={row.bank} 
                                                    onChange={e => handleChequeChange(i, "bank", e.target.value)}
                                                    disabled={isSubmitted}
                                                    placeholder="Bank name"
                                                />
                                            </td>
                                            {!isSubmitted && (
                                                <td className="border border-gray-300 px-2 py-1">
                                                    <button
                                                        onClick={() => removeChequeRow(i)}
                                                        className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600 text-xs"
                                                    >
                                                        Remove
                                                    </button>
                                                </td>
                                            )}
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                    </div>

                    {/* Cash Deposited */}
                    <div className="bg-white border rounded-lg p-4">
                        <div className="font-bold mb-3 text-gray-800">Cash Deposited</div>
                        <div className="overflow-x-auto">
                            <table className="w-full border border-gray-300">
                                <thead>
                                    <tr className="bg-gray-100">
                                        <th className="border border-gray-300 px-2 py-1 text-sm font-medium">Denomination</th>
                                        <th className="border border-gray-300 px-2 py-1 text-sm font-medium">R</th>
                                        <th className="border border-gray-300 px-2 py-1 text-sm font-medium">c</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {depositData.cashDeposited.map((row, i) => (
                                        <tr key={i}>
                                            <td className="border border-gray-300 px-2 py-1 text-sm">{row.label}</td>
                                            <td className="border border-gray-300 px-2 py-1">
                                                <input 
                                                    className="w-16 p-1 border-none focus:outline-none focus:ring-1 focus:ring-blue-500 text-center"
                                                    value={row.r} 
                                                    onChange={e => handleCashChange(i, "r", e.target.value)}
                                                    disabled={isSubmitted}
                                                    placeholder="0"
                                                />
                                            </td>
                                            <td className="border border-gray-300 px-2 py-1">
                                                <input 
                                                    className="w-12 p-1 border-none focus:outline-none focus:ring-1 focus:ring-blue-500 text-center"
                                                    value={row.c} 
                                                    onChange={e => handleCashChange(i, "c", e.target.value)}
                                                    disabled={isSubmitted}
                                                    placeholder="0"
                                                />
                                            </td>
                                        </tr>
                                    ))}
                                </tbody>
                            </table>
                        </div>
                        <div className="mt-3 p-2 bg-gray-100 rounded">
                            <span className="font-semibold">Total Cash: R{totalCash.toFixed(2)}</span>
                        </div>
                    </div>
                </div>

                {/* Footer Information */}
                <div className="flex flex-col md:flex-row gap-6">
                    <div className="flex-1">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">Bank Stamp (for office use)</label>
                        <textarea 
                            className="w-full p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                            rows={2} 
                            value={depositData.bankStamp} 
                            onChange={e => handleFieldChange("bankStamp", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Bank stamp information"
                        />
                    </div>
                    <div>
                        <label className="block font-semibold text-sm text-gray-700 mb-2">Total R</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-32"
                            value={depositData.totalR} 
                            onChange={e => handleFieldChange("totalR", e.target.value.replace(/[^0-9.]/g, ""))}
                            disabled={isSubmitted}
                            placeholder="0.00"
                        />
                    </div>
                </div>
            </div>
        </div>
    );
};

export default DepositSlipInput;
