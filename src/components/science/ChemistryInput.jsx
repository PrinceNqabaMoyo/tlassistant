import React, { useState } from 'react';
import { Beaker } from 'lucide-react';

const ChemistryInput = ({ onSubmit }) => {
    const [smiles, setSmiles] = useState('');

    const handleSubmit = () => {
        if (smiles.trim() && onSubmit) {
            onSubmit(smiles.trim());
        }
    };

    return (
        <div className="border-2 border-dashed border-gray-300 p-6 rounded-xl bg-gray-50 flex flex-col items-center justify-center text-center">
            <div className="bg-blue-100 p-3 rounded-full text-blue-600 mb-4">
                <Beaker size={32} />
            </div>
            <h3 className="text-lg font-bold text-gray-800 mb-2">Molecular Input</h3>
            <p className="text-gray-600 text-sm mb-4 max-w-md">
                Draw your chemical structure here. 
                <br/><span className="text-xs text-gray-500">(Ketcher iframe integration requires hosted assets. Fallback to SMILES string input.)</span>
            </p>
            
            <div className="flex w-full max-w-md gap-2">
                <input 
                    type="text" 
                    value={smiles}
                    onChange={(e) => setSmiles(e.target.value)}
                    placeholder="Enter SMILES string (e.g. CCO for ethanol)" 
                    className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none"
                />
                <button 
                    onClick={handleSubmit}
                    className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg font-medium transition-colors"
                >
                    Submit
                </button>
            </div>
        </div>
    );
};

export default ChemistryInput;
