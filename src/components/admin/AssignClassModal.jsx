import React from 'react';

const AssignClassModal = ({ isOpen, onClose, onConfirm, classes, setSelectedClassId }) => {
    if (!isOpen) return null;

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 z-50 flex justify-center items-center">
            <div className="bg-white p-8 rounded-xl shadow-2xl w-full max-w-md">
                <h2 className="text-2xl font-bold text-gray-800 mb-4">Assign to Class</h2>
                <p className="text-gray-600 mb-6">Select a class to assign this assessment to.</p>
                
                <div className="mb-6">
                    <label htmlFor="classSelect" className="block text-sm font-medium text-gray-700 mb-1">Class</label>
                    <select
                        id="classSelect"
                        onChange={(e) => setSelectedClassId(e.target.value)}
                        className="w-full p-2 border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500"
                        defaultValue=""
                    >
                        <option value="" disabled>-- Select a class --</option>
                        {classes.map(c => (
                            <option key={c.id} value={c.id}>{c.name}</option>
                        ))}
                    </select>
                </div>

                <div className="flex justify-end space-x-4">
                    <button onClick={onClose} className="px-6 py-2 border border-gray-300 text-base font-medium rounded-md text-gray-700 bg-white hover:bg-gray-50">
                        Cancel
                    </button>
                    <button onClick={onConfirm} className="px-6 py-2 border border-transparent text-base font-medium rounded-md shadow-sm text-white bg-green-600 hover:bg-green-700">
                        Confirm Assignment
                    </button>
                </div>
            </div>
        </div>
    );
};

export default AssignClassModal;
