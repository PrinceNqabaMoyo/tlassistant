import React, { useState, useEffect } from 'react';

const DebtorsJournalInput = ({ data, onChange, isSubmitted }) => {
  const [rows, setRows] = useState(data?.rows || [
    { docNo: '', day: '', debtor: '', fol: '', sales: '', costOfSales: '' }
  ]);

  useEffect(() => {
    if (data?.rows) {
      setRows(data.rows);
    }
  }, [data]);

  const handleRowChange = (index, field, value) => {
    const newRows = [...rows];
    newRows[index][field] = value;
    setRows(newRows);
    onChange({ ...data, rows: newRows });
  };

  const addRow = () => {
    const newRows = [...rows, { docNo: '', day: '', debtor: '', fol: '', sales: '', costOfSales: '' }];
    setRows(newRows);
    onChange({ ...data, rows: newRows });
  };

  const removeRow = (index) => {
    if (rows.length > 1) {
      const newRows = rows.filter((_, i) => i !== index);
      setRows(newRows);
      onChange({ ...data, rows: newRows });
    }
  };

  const calculateTotals = () => {
    const salesTotal = rows.reduce((sum, row) => sum + (parseFloat(row.sales) || 0), 0);
    const costOfSalesTotal = rows.reduce((sum, row) => sum + (parseFloat(row.costOfSales) || 0), 0);
    return { salesTotal, costOfSalesTotal };
  };

  const { salesTotal, costOfSalesTotal } = calculateTotals();

  return (
    <div className="bg-white rounded-lg shadow-md p-6 mb-6">
      <h3 className="text-xl font-semibold text-gray-800 mb-4">Debtors Journal</h3>
      
      <div className="overflow-x-auto">
        <table className="min-w-full border border-gray-300">
          <thead>
            <tr className="bg-gray-100">
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Doc. No.</th>
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Day</th>
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Debtor</th>
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Fol.</th>
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Sales</th>
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Cost of Sales</th>
              <th className="border border-gray-300 px-3 py-2 text-sm font-medium text-gray-700">Actions</th>
            </tr>
          </thead>
          <tbody>
            {rows.map((row, index) => (
              <tr key={index} className="hover:bg-gray-50">
                <td className="border border-gray-300 px-3 py-2">
                  <input
                    type="text"
                    value={row.docNo}
                    onChange={(e) => handleRowChange(index, 'docNo', e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Doc. No."
                  />
                </td>
                <td className="border border-gray-300 px-3 py-2">
                  <input
                    type="text"
                    value={row.day}
                    onChange={(e) => handleRowChange(index, 'day', e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Day"
                  />
                </td>
                <td className="border border-gray-300 px-3 py-2">
                  <input
                    type="text"
                    value={row.debtor}
                    onChange={(e) => handleRowChange(index, 'debtor', e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Debtor Name"
                  />
                </td>
                <td className="border border-gray-300 px-3 py-2">
                  <input
                    type="text"
                    value={row.fol}
                    onChange={(e) => handleRowChange(index, 'fol', e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="Fol."
                  />
                </td>
                <td className="border border-gray-300 px-3 py-2">
                  <input
                    type="number"
                    step="0.01"
                    value={row.sales}
                    onChange={(e) => handleRowChange(index, 'sales', e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="0.00"
                  />
                </td>
                <td className="border border-gray-300 px-3 py-2">
                  <input
                    type="number"
                    step="0.01"
                    value={row.costOfSales}
                    onChange={(e) => handleRowChange(index, 'costOfSales', e.target.value)}
                    className="w-full px-2 py-1 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
                    placeholder="0.00"
                  />
                </td>
                <td className="border border-gray-300 px-3 py-2">
                  <button
                    onClick={() => removeRow(index)}
                    className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-red-500"
                    disabled={rows.length === 1}
                  >
                    Remove
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      <div className="mt-4 flex justify-between items-center">
        <button
          onClick={addRow}
          className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          Add Row
        </button>
      </div>

      {isSubmitted && (
        <div className="mt-6 p-4 bg-gray-100 rounded-lg">
          <h4 className="font-semibold text-gray-800 mb-2">Totals:</h4>
          <div className="grid grid-cols-2 gap-4">
            <div>
              <span className="font-medium">Total Sales: </span>
              <span className="text-green-600">R {salesTotal.toFixed(2)}</span>
            </div>
            <div>
              <span className="font-medium">Total Cost of Sales: </span>
              <span className="text-red-600">R {costOfSalesTotal.toFixed(2)}</span>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default DebtorsJournalInput;
