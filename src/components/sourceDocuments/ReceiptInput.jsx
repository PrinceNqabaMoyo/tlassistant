import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const ReceiptInput = ({ initialData, onChange, isSubmitted }) => {
    const [receiptData, setReceiptData] = useState(initialData || {
        receiptNumber: '',
        date: '',
        receivedFrom: '',
        amountInWords: '',
        amountNumeric: { main: '', cents: '' },
        cents: 'No cents',
        inPaymentOf: '',
        receivedBy: '',
        businessName: ''
    });

    useEffect(() => {
        onChange(receiptData);
    }, [receiptData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setReceiptData(prev => ({ ...prev, [field]: value }));
    };

    const handleMoneyChange = (value) => {
        if (isSubmitted) return;
        setReceiptData(prev => ({ ...prev, amountNumeric: value }));
    };

    const handleCentsChange = (value) => {
        if (isSubmitted) return;
        setReceiptData(prev => ({ ...prev, cents: value }));
    };

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            <div className="text-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">RECEIPT</h3>
            </div>
            
            <div className="border-2 border-gray-400 rounded-lg p-6 bg-white">
                {/* Header Section */}
                <div className="flex justify-between items-start mb-6">
                    <div className="flex-1"></div>
                    <div className="text-center flex-1">
                        <h4 className="font-bold text-gray-800 text-xl mb-2">RECEIPT</h4>
                    </div>
                    <div className="flex-1 text-right">
                        <div className="flex items-center justify-end">
                            <label className="font-semibold text-sm text-gray-700 mr-2">No:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-24"
                                value={receiptData.receiptNumber} 
                                onChange={e => handleFieldChange("receiptNumber", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Receipt number"
                            />
                        </div>
                    </div>
                </div>

                {/* Date */}
                <div className="mb-6">
                    <label className="block font-semibold text-sm text-gray-700 mb-2">Date</label>
                    <input 
                        type="date" 
                        className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                        value={receiptData.date} 
                        onChange={e => handleFieldChange("date", e.target.value)}
                        disabled={isSubmitted}
                    />
                </div>

                {/* Received From */}
                <div className="mb-6">
                    <label className="block font-semibold text-sm text-gray-700 mb-2">Received from:</label>
                    <input 
                        className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                        value={receiptData.receivedFrom} 
                        onChange={e => handleFieldChange("receivedFrom", e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Name of person paying"
                    />
                </div>

                {/* Amount Section */}
                <div className="mb-6">
                    <div className="flex items-start space-x-4">
                        <div className="flex-1">
                            <label className="block font-semibold text-sm text-gray-700 mb-2">The amount of:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={receiptData.amountInWords} 
                                onChange={e => handleFieldChange("amountInWords", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Amount in words (e.g., One thousand rand only)"
                            />
                        </div>
                        <div className="flex-1">
                            <label className="block font-semibold text-sm text-gray-700 mb-2">Amount:</label>
                            <div className="flex items-center">
                                <span className="font-semibold text-gray-700 mr-2">R</span>
                                <div className="flex-1">
                                    <MoneyInput
                                        value={receiptData.amountNumeric}
                                        onChange={handleMoneyChange}
                                        disabled={isSubmitted}
                                        placeholder="0.00"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Cents */}
                <div className="mb-6">
                    <label className="block font-semibold text-sm text-gray-700 mb-2">Cents:</label>
                    <input 
                        className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                        value={receiptData.cents} 
                        onChange={e => handleCentsChange(e.target.value)}
                        disabled={isSubmitted}
                        placeholder="No cents"
                    />
                </div>

                {/* Bottom Section */}
                <div className="flex justify-between items-end">
                    <div className="flex-1 mr-4">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">In payment of:</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={receiptData.inPaymentOf} 
                            onChange={e => handleFieldChange("inPaymentOf", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="What the amount is purchasing"
                        />
                    </div>
                    <div className="flex-1 text-center">
                        <div className="mb-2">
                            <label className="block font-semibold text-sm text-gray-700 mb-2">Received by:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={receiptData.receivedBy} 
                                onChange={e => handleFieldChange("receivedBy", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Name of person receiving money"
                            />
                        </div>
                        <div className="border-t border-gray-400 pt-2">
                            <label className="block font-semibold text-sm text-gray-700 mb-2">Business Name:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                                value={receiptData.businessName} 
                                onChange={e => handleFieldChange("businessName", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Name of business accepting payment"
                            />
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default ReceiptInput;
