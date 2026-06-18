import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const ChequeInput = ({ initialData, onChange, isSubmitted }) => {
    const [chequeData, setChequeData] = useState(initialData || {
        // First Section (Left side - Counterfoil)
        counterfoil: {
            date: '',
            to: '',
            for: '',
            balance: { main: '', cents: '' },
            deposit: { main: '', cents: '' },
            subtotal: { main: '', cents: '' },
            otherDebit: { main: '', cents: '' },
            thisCheque: { main: '', cents: '' },
            balanceAfter: { main: '', cents: '' }
        },
        // Second Section (Right side - Main Cheque)
        mainCheque: {
            bankName: '',
            branchName: '',
            notTransferrable: true,
            date: '',
            payTo: '',
            orBearer: true,
            amountInWords: '',
            amountNumeric: { main: '', cents: '' },
            cents: '00',
            accountHolderName: '',
            businessName: ''
        }
    });

    useEffect(() => {
        onChange(chequeData);
    }, [chequeData, onChange]);

    const handleCounterfoilChange = (field, value) => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            counterfoil: { ...prev.counterfoil, [field]: value }
        }));
    };

    const handleMainChequeChange = (field, value) => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            mainCheque: { ...prev.mainCheque, [field]: value }
        }));
    };

    const handleMoneyChange = (section, field, value) => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            [section]: { ...prev[section], [field]: value }
        }));
    };

    const handleAmountInWordsChange = (value) => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            mainCheque: { ...prev.mainCheque, amountInWords: value }
        }));
    };

    const handleNumericAmountChange = (field, value) => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            mainCheque: { 
                ...prev.mainCheque, 
                amountNumeric: { ...prev.mainCheque.amountNumeric, [field]: value }
            }
        }));
    };

    const handleCentsChange = (value) => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            mainCheque: { ...prev.mainCheque, cents: value }
        }));
    };

    const toggleOrBearer = () => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            mainCheque: { ...prev.mainCheque, orBearer: !prev.mainCheque.orBearer }
        }));
    };

    const toggleNotTransferrable = () => {
        if (isSubmitted) return;
        setChequeData(prev => ({
            ...prev,
            mainCheque: { ...prev.mainCheque, notTransferrable: !prev.mainCheque.notTransferrable }
        }));
    };

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            <div className="text-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Cheque / Cheque Counterfoil</h3>
            </div>
            
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* First Section - Counterfoil (Left Side) */}
                <div className="border-2 border-gray-400 rounded-lg p-4 bg-white">
                    <div className="text-center mb-4">
                        <h4 className="font-bold text-gray-800 text-lg">COUNTERFOIL</h4>
                    </div>
                    
                    <div className="space-y-4">
                        {/* Date */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Date</label>
                            <input 
                                type="date" 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.counterfoil.date} 
                                onChange={e => handleCounterfoilChange("date", e.target.value)}
                                disabled={isSubmitted}
                            />
                        </div>

                        {/* To */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">To:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.counterfoil.to} 
                                onChange={e => handleCounterfoilChange("to", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Name of business or person being paid"
                            />
                        </div>

                        {/* For */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">For:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.counterfoil.for} 
                                onChange={e => handleCounterfoilChange("for", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Services or items being paid for"
                            />
                        </div>

                        {/* Balance */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Balance: R</label>
                            <MoneyInput
                                value={chequeData.counterfoil.balance}
                                onChange={(value) => handleMoneyChange("counterfoil", "balance", value)}
                                disabled={isSubmitted}
                                placeholder="0.00"
                            />
                        </div>

                        {/* Deposit */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Deposit: R</label>
                            <MoneyInput
                                value={chequeData.counterfoil.deposit}
                                onChange={(value) => handleMoneyChange("counterfoil", "deposit", value)}
                                disabled={isSubmitted}
                                placeholder="0.00"
                            />
                        </div>

                        {/* Subtotal */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Subtotal: R</label>
                            <MoneyInput
                                value={chequeData.counterfoil.subtotal}
                                onChange={(value) => handleMoneyChange("counterfoil", "subtotal", value)}
                                disabled={isSubmitted}
                                placeholder="0.00"
                            />
                        </div>

                        {/* Other Debit */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Other Debit: R</label>
                            <MoneyInput
                                value={chequeData.counterfoil.otherDebit}
                                onChange={(value) => handleMoneyChange("counterfoil", "otherDebit", value)}
                                disabled={isSubmitted}
                                placeholder="0.00"
                            />
                        </div>

                        {/* This Cheque */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">This Cheque: R</label>
                            <MoneyInput
                                value={chequeData.counterfoil.thisCheque}
                                onChange={(value) => handleMoneyChange("counterfoil", "thisCheque", value)}
                                disabled={isSubmitted}
                                placeholder="0.00"
                            />
                        </div>

                        {/* Balance After */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Balance: R</label>
                            <MoneyInput
                                value={chequeData.counterfoil.balanceAfter}
                                onChange={(value) => handleMoneyChange("counterfoil", "balanceAfter", value)}
                                disabled={isSubmitted}
                                placeholder="0.00"
                            />
                        </div>
                    </div>
                </div>

                {/* Second Section - Main Cheque (Right Side) */}
                <div className="border-2 border-gray-400 rounded-lg p-4 bg-white">
                    <div className="text-center mb-4">
                        <h4 className="font-bold text-gray-800 text-lg">CHEQUE</h4>
                    </div>
                    
                    <div className="space-y-4">
                        {/* Bank Name */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Bank Name</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.mainCheque.bankName} 
                                onChange={e => handleMainChequeChange("bankName", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Enter bank name"
                            />
                        </div>

                        {/* Not Transferrable */}
                        <div className="flex items-center space-x-2">
                            <input 
                                type="checkbox" 
                                id="notTransferrable"
                                checked={chequeData.mainCheque.notTransferrable}
                                onChange={toggleNotTransferrable}
                                disabled={isSubmitted}
                                className="rounded"
                            />
                            <label htmlFor="notTransferrable" className="font-semibold text-sm text-gray-700">
                                Not Transferrable
                            </label>
                        </div>

                        {/* Branch Name */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Branch Name</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.mainCheque.branchName} 
                                onChange={e => handleMainChequeChange("branchName", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Enter branch name"
                            />
                        </div>

                        {/* Date */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Date</label>
                            <input 
                                type="date" 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.mainCheque.date} 
                                onChange={e => handleMainChequeChange("date", e.target.value)}
                                disabled={isSubmitted}
                            />
                        </div>

                        {/* Pay To and OR BEARER */}
                        <div className="flex items-center space-x-2">
                            <div className="flex-1">
                                <label className="block font-semibold text-sm text-gray-700">Pay:</label>
                                <input 
                                    className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                    value={chequeData.mainCheque.payTo} 
                                    onChange={e => handleMainChequeChange("payTo", e.target.value)}
                                    disabled={isSubmitted}
                                    placeholder="Name of business or person being paid"
                                />
                            </div>
                            <div className="flex items-center space-x-2">
                                <span className="font-semibold text-sm text-gray-700">OR</span>
                                <div className="flex items-center space-x-1">
                                    <input 
                                        type="checkbox" 
                                        id="orBearer"
                                        checked={chequeData.mainCheque.orBearer}
                                        onChange={toggleOrBearer}
                                        disabled={isSubmitted}
                                        className="rounded"
                                    />
                                    <label htmlFor="orBearer" className="font-semibold text-sm text-gray-700">
                                        BEARER
                                    </label>
                                </div>
                            </div>
                        </div>

                        {/* Amount in Words */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">The amount of:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.mainCheque.amountInWords} 
                                onChange={e => handleAmountInWordsChange(e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Amount in words (e.g., One thousand rand only)"
                            />
                        </div>

                        {/* Numeric Amount */}
                        <div className="flex items-center space-x-2">
                            <span className="font-semibold text-sm text-gray-700">rand</span>
                            <div className="flex-1">
                                <MoneyInput
                                    value={chequeData.mainCheque.amountNumeric}
                                    onChange={(value) => handleMoneyChange("mainCheque", "amountNumeric", value)}
                                    disabled={isSubmitted}
                                    placeholder="0.00"
                                />
                            </div>
                        </div>

                        {/* Cents */}
                        <div className="flex items-center space-x-2">
                            <span className="font-semibold text-sm text-gray-700">cents</span>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-20 text-center"
                                value={chequeData.mainCheque.cents} 
                                onChange={e => handleCentsChange(e.target.value)}
                                disabled={isSubmitted}
                                placeholder="00"
                                maxLength={2}
                            />
                        </div>

                        {/* Account Holder Name */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Account Holder Name</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.mainCheque.accountHolderName} 
                                onChange={e => handleMainChequeChange("accountHolderName", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Name of person whose account is cutting the cheque"
                            />
                        </div>

                        {/* Business Name */}
                        <div>
                            <label className="block font-semibold text-sm text-gray-700">Business Name</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={chequeData.mainCheque.businessName} 
                                onChange={e => handleMainChequeChange("businessName", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Name of business that owns the account"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ChequeInput;
