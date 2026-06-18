import React, { useState, useEffect } from 'react';
import { MoneyInput } from '../forms/TableComponents';

const CashInvoiceInput = ({ initialData, onChange, isSubmitted }) => {
    const [invoiceData, setInvoiceData] = useState(initialData || {
        vatNumber: '',
        invoiceNumber: '',
        to: '',
        date: '',
        boughtFrom: '',
        items: [
            { quantity: '', details: '', price: { main: '', cents: '' }, amount: { main: '', cents: '' } }
        ],
        total: { main: '', cents: '' }
    });

    useEffect(() => {
        onChange(invoiceData);
    }, [invoiceData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setInvoiceData(prev => ({ ...prev, [field]: value }));
    };

    const handleItemChange = (index, field, value) => {
        if (isSubmitted) return;
        const updatedItems = [...invoiceData.items];
        updatedItems[index] = { ...updatedItems[index], [field]: value };
        
        // Calculate amount for this item
        if (field === 'quantity' || field === 'price') {
            const quantity = field === 'quantity' ? parseFloat(value) || 0 : parseFloat(updatedItems[index].quantity) || 0;
            const price = field === 'price' ? 
                (parseFloat(value.main || 0) + parseFloat(value.cents || 0) / 100) : 
                (parseFloat(updatedItems[index].price?.main || 0) + parseFloat(updatedItems[index].price?.cents || 0) / 100);
            
            const amount = quantity * price;
            const amountMain = Math.floor(amount);
            const amountCents = Math.round((amount - amountMain) * 100);
            
            updatedItems[index].amount = { 
                main: amountMain.toString(), 
                cents: amountCents.toString().padStart(2, '0') 
            };
        }
        
        setInvoiceData(prev => ({ ...prev, items: updatedItems }));
        
        // Calculate total
        calculateTotal(updatedItems);
    };

    const calculateTotal = (items) => {
        const total = items.reduce((sum, item) => {
            const amount = parseFloat(item.amount?.main || 0) + parseFloat(item.amount?.cents || 0) / 100;
            return sum + amount;
        }, 0);
        
        const totalMain = Math.floor(total);
        const totalCents = Math.round((total - totalMain) * 100);
        
        setInvoiceData(prev => ({
            ...prev,
            total: { 
                main: totalMain.toString(), 
                cents: totalCents.toString().padStart(2, '0') 
            }
        }));
    };

    const addItem = () => {
        if (isSubmitted) return;
        const newItem = { quantity: '', details: '', price: { main: '', cents: '' }, amount: { main: '', cents: '' } };
        setInvoiceData(prev => ({ ...prev, items: [...prev.items, newItem] }));
    };

    const removeItem = (index) => {
        if (isSubmitted) return;
        const updatedItems = invoiceData.items.filter((_, i) => i !== index);
        setInvoiceData(prev => ({ ...prev, items: updatedItems }));
        calculateTotal(updatedItems);
    };

    return (
        <div className="p-4 my-4 bg-gray-50 border border-gray-300 rounded-lg">
            <div className="text-center mb-4">
                <h3 className="text-lg font-bold text-gray-800">Cash Invoice</h3>
            </div>
            
            <div className="border-2 border-gray-400 rounded-lg p-6 bg-white">
                {/* Header Section */}
                <div className="flex justify-between items-start mb-6">
                    <div className="flex-1">
                        <div className="text-sm text-gray-600 mb-1">Tax Invoice</div>
                        <div className="text-sm text-gray-600">Vat No: 
                            <input 
                                className="ml-2 p-1 border border-gray-300 rounded focus:outline-none focus:ring-1 focus:ring-blue-500 w-32"
                                value={invoiceData.vatNumber} 
                                onChange={e => handleFieldChange("vatNumber", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="VAT registration number"
                            />
                        </div>
                    </div>
                    <div className="flex-1 text-right">
                        <div className="flex items-center justify-end">
                            <label className="font-semibold text-sm text-gray-700 mr-2">No:</label>
                            <input 
                                className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-24"
                                value={invoiceData.invoiceNumber} 
                                onChange={e => handleFieldChange("invoiceNumber", e.target.value)}
                                disabled={isSubmitted}
                                placeholder="Invoice number"
                            />
                        </div>
                    </div>
                </div>

                {/* Title */}
                <div className="text-center mb-6">
                    <h4 className="font-bold text-gray-800 text-xl">CASH INVOICE</h4>
                </div>

                {/* To and Date */}
                <div className="flex justify-between items-center mb-6">
                    <div className="flex-1 mr-4">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">To:</label>
                        <input 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={invoiceData.to} 
                            onChange={e => handleFieldChange("to", e.target.value)}
                            disabled={isSubmitted}
                            placeholder="Name to whom cash was given or 'Cash'"
                        />
                    </div>
                    <div className="flex-1">
                        <label className="block font-semibold text-sm text-gray-700 mb-2">Date:</label>
                        <input 
                            type="date" 
                            className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                            value={invoiceData.date} 
                            onChange={e => handleFieldChange("date", e.target.value)}
                            disabled={isSubmitted}
                        />
                    </div>
                </div>

                {/* Bought From */}
                <div className="mb-6">
                    <label className="block font-semibold text-sm text-gray-700 mb-2">Bought from:</label>
                    <input 
                        className="p-2 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500 w-full"
                        value={invoiceData.boughtFrom} 
                        onChange={e => handleFieldChange("boughtFrom", e.target.value)}
                        disabled={isSubmitted}
                        placeholder="Business where cash was used to purchase goods or services"
                    />
                </div>

                {/* Items Table */}
                <div className="mb-6">
                    <table className="min-w-full border border-gray-300">
                        <thead className="bg-gray-100">
                            <tr>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700">Quantity</th>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700">Details</th>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700">Price</th>
                                <th className="border border-gray-300 px-3 py-2 text-left text-sm font-semibold text-gray-700">Amount</th>
                                {!isSubmitted && <th className="border border-gray-300 px-3 py-2 text-sm font-semibold text-gray-700">Action</th>}
                            </tr>
                        </thead>
                        <tbody>
                            {invoiceData.items.map((item, index) => (
                                <tr key={index}>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <input 
                                            type="number" 
                                            className="w-full p-1 border border-gray-200 rounded focus:outline-none focus:ring-1 focus:ring-blue-500"
                                            value={item.quantity} 
                                            onChange={e => handleItemChange(index, 'quantity', e.target.value)}
                                            disabled={isSubmitted}
                                            placeholder="0"
                                            min="0"
                                            step="1"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <input 
                                            className="w-full p-1 border border-gray-200 rounded focus:outline-none focus:ring-1 focus:ring-blue-500"
                                            value={item.details} 
                                            onChange={e => handleItemChange(index, 'details', e.target.value)}
                                            disabled={isSubmitted}
                                            placeholder="Item description"
                                        />
                                    </td>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <div className="flex items-center">
                                            <span className="text-sm text-gray-600 mr-1">R</span>
                                            <MoneyInput
                                                value={item.price}
                                                onChange={(value) => handleItemChange(index, 'price', value)}
                                                disabled={isSubmitted}
                                                placeholder="0.00"
                                            />
                                        </div>
                                    </td>
                                    <td className="border border-gray-300 px-3 py-2">
                                        <div className="flex items-center">
                                            <span className="text-sm text-gray-600 mr-1">R</span>
                                            <MoneyInput
                                                value={item.amount}
                                                onChange={() => {}} // Read-only, calculated automatically
                                                disabled={true}
                                                placeholder="0.00"
                                            />
                                        </div>
                                    </td>
                                    {!isSubmitted && (
                                        <td className="border border-gray-300 px-3 py-2">
                                            <button 
                                                onClick={() => removeItem(index)}
                                                className="text-red-600 hover:text-red-800 text-lg font-bold"
                                            >
                                                ×
                                            </button>
                                        </td>
                                    )}
                                </tr>
                            ))}
                            {/* Total Row */}
                            <tr className="bg-gray-50">
                                <td colSpan="3" className="border border-gray-300 px-3 py-2 text-right font-semibold text-gray-700">
                                    Total:
                                </td>
                                <td className="border border-gray-300 px-3 py-2">
                                    <div className="flex items-center">
                                        <span className="text-sm text-gray-600 mr-1">R</span>
                                        <MoneyInput
                                            value={invoiceData.total}
                                            onChange={() => {}} // Read-only, calculated automatically
                                            disabled={true}
                                            placeholder="0.00"
                                        />
                                    </div>
                                </td>
                                {!isSubmitted && <td className="border border-gray-300 px-3 py-2"></td>}
                            </tr>
                        </tbody>
                    </table>
                    
                    {!isSubmitted && (
                        <button 
                            onClick={addItem}
                            className="mt-3 px-4 py-2 bg-blue-500 text-white rounded-md text-sm font-semibold hover:bg-blue-600"
                        >
                            Add Item
                        </button>
                    )}
                </div>

                {/* E&OE */}
                <div className="text-left">
                    <span className="text-xs text-gray-500">E&OE</span>
                </div>
            </div>
        </div>
    );
};

export default CashInvoiceInput;
