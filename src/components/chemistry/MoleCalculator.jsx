import React, { useState, useEffect } from 'react';

const MoleCalculator = ({ initialData, onChange, isSubmitted }) => {
    const [calculationType, setCalculationType] = useState(initialData.calculationType || 'molar_mass');
    const [formula, setFormula] = useState(initialData.formula || '');
    const [mass, setMass] = useState(initialData.mass || '');
    const [moles, setMoles] = useState(initialData.moles || '');
    const [concentration, setConcentration] = useState(initialData.concentration || '');
    const [volume, setVolume] = useState(initialData.volume || '');
    const [showResults, setShowResults] = useState(false);
    const [showSteps, setShowSteps] = useState(false);

    // Common elements and their atomic masses (g/mol)
    const atomicMasses = {
        'H': 1.008, 'He': 4.003, 'Li': 6.941, 'Be': 9.012, 'B': 10.811,
        'C': 12.011, 'N': 14.007, 'O': 15.999, 'F': 18.998, 'Ne': 20.180,
        'Na': 22.990, 'Mg': 24.305, 'Al': 26.982, 'Si': 28.086, 'P': 30.974,
        'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.098, 'Ca': 40.078,
        'Fe': 55.845, 'Cu': 63.546, 'Zn': 65.38, 'Ag': 107.868, 'Au': 196.967
    };

    // Calculation types
    const calculationTypes = {
        'molar_mass': 'Molar Mass',
        'mass_to_moles': 'Mass to Moles',
        'moles_to_mass': 'Moles to Mass',
        'concentration': 'Concentration (Molarity)',
        'dilution': 'Dilution',
        'stoichiometry': 'Stoichiometry'
    };

    useEffect(() => {
        const formattedData = {
            type: "mole_calculator",
            calculationType: calculationType,
            formula: formula,
            mass: mass,
            moles: moles,
            concentration: concentration,
            volume: volume,
            results: getResults()
        };
        onChange(formattedData);
    }, [calculationType, formula, mass, moles, concentration, volume, onChange]);

    const parseFormula = (formula) => {
        const atoms = {};
        const regex = /([A-Z][a-z]?)(\d*)/g;
        let match;
        
        while ((match = regex.exec(formula)) !== null) {
            const element = match[1];
            const count = match[2] ? parseInt(match[2]) : 1;
            atoms[element] = (atoms[element] || 0) + count;
        }
        
        return atoms;
    };

    const calculateMolarMass = (formula) => {
        if (!formula.trim()) return 0;
        
        const atoms = parseFormula(formula);
        let totalMass = 0;
        
        Object.entries(atoms).forEach(([element, count]) => {
            if (atomicMasses[element]) {
                totalMass += atomicMasses[element] * count;
            }
        });
        
        return totalMass;
    };

    const massToMoles = (mass, molarMass) => {
        if (!mass || !molarMass) return 0;
        return parseFloat(mass) / molarMass;
    };

    const molesToMass = (moles, molarMass) => {
        if (!moles || !molarMass) return 0;
        return parseFloat(moles) * molarMass;
    };

    const calculateConcentration = (moles, volume) => {
        if (!moles || !volume) return 0;
        return parseFloat(moles) / parseFloat(volume);
    };

    const calculateVolume = (moles, concentration) => {
        if (!moles || !concentration) return 0;
        return parseFloat(moles) / parseFloat(concentration);
    };

    const getResults = () => {
        const results = {};
        
        switch (calculationType) {
            case 'molar_mass':
                results.molarMass = calculateMolarMass(formula);
                break;
            case 'mass_to_moles':
                results.molarMass = calculateMolarMass(formula);
                results.moles = massToMoles(mass, results.molarMass);
                break;
            case 'moles_to_mass':
                results.molarMass = calculateMolarMass(formula);
                results.mass = molesToMass(moles, results.molarMass);
                break;
            case 'concentration':
                results.molarity = calculateConcentration(moles, volume);
                break;
            case 'dilution':
                results.finalConcentration = calculateConcentration(moles, volume);
                break;
            case 'stoichiometry':
                results.molarMass = calculateMolarMass(formula);
                results.moles = massToMoles(mass, results.molarMass);
                break;
        }
        
        return results;
    };

    const getCalculationSteps = () => {
        const steps = [];
        
        switch (calculationType) {
            case 'molar_mass':
                steps.push('1. Break down the chemical formula into individual elements');
                steps.push('2. Find the atomic mass of each element from the periodic table');
                steps.push('3. Multiply each atomic mass by the number of atoms');
                steps.push('4. Sum all the masses to get the total molar mass');
                break;
            case 'mass_to_moles':
                steps.push('1. Calculate the molar mass of the compound');
                steps.push('2. Use the formula: moles = mass ÷ molar mass');
                steps.push('3. Ensure units are consistent (grams for mass)');
                break;
            case 'moles_to_mass':
                steps.push('1. Calculate the molar mass of the compound');
                steps.push('2. Use the formula: mass = moles × molar mass');
                steps.push('3. The result will be in grams');
                break;
            case 'concentration':
                steps.push('1. Ensure moles and volume are in correct units');
                steps.push('2. Use the formula: Molarity = moles ÷ volume (L)');
                steps.push('3. Volume must be in liters for molarity');
                break;
            case 'dilution':
                steps.push('1. Use the dilution formula: M₁V₁ = M₂V₂');
                steps.push('2. M₁ = initial concentration, V₁ = initial volume');
                steps.push('3. M₂ = final concentration, V₂ = final volume');
                break;
            case 'stoichiometry':
                steps.push('1. Convert given mass to moles using molar mass');
                steps.push('2. Use the balanced chemical equation');
                steps.push('3. Apply mole ratios to find desired quantities');
                break;
        }
        
        return steps;
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        return num.toFixed(4).replace(/\.?0+$/, '');
    };

    const getUnitLabel = () => {
        switch (calculationType) {
            case 'molar_mass':
                return 'g/mol';
            case 'mass_to_moles':
            case 'moles_to_mass':
                return calculationType === 'mass_to_moles' ? 'mol' : 'g';
            case 'concentration':
            case 'dilution':
                return 'M (mol/L)';
            default:
                return '';
        }
    };

    const handleCalculate = () => {
        if (isSubmitted) return;
        setShowResults(true);
    };

    const resetCalculator = () => {
        if (isSubmitted) return;
        setFormula('');
        setMass('');
        setMoles('');
        setConcentration('');
        setVolume('');
        setShowResults(false);
        setShowSteps(false);
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Mole Calculator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowSteps(!showSteps)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showSteps 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showSteps ? 'Hide Steps' : 'Show Steps'}
                    </button>
                    {!isSubmitted && (
                        <button
                            onClick={resetCalculator}
                            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg text-sm font-medium hover:bg-gray-200 transition-colors"
                        >
                            Reset
                        </button>
                    )}
                </div>
            </div>

            {/* Calculation Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Calculation Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={calculationType} 
                    onChange={(e) => !isSubmitted && setCalculationType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    {Object.entries(calculationTypes).map(([key, value]) => (
                        <option key={key} value={key}>{value}</option>
                    ))}
                </select>
            </div>

            {/* Formula Input */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Chemical Formula:</label>
                <input 
                    type="text" 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={formula} 
                    onChange={(e) => !isSubmitted && setFormula(e.target.value)} 
                    placeholder="e.g., H₂SO₄, NaCl, C₆H₁₂O₆" 
                    disabled={isSubmitted} 
                />
            </div>

            {/* Dynamic Input Fields Based on Calculation Type */}
            {calculationType === 'molar_mass' && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <p className="text-sm text-blue-700">
                        Enter a chemical formula above to calculate its molar mass. The calculator will break down the formula and sum the atomic masses of all elements.
                    </p>
                </div>
            )}

            {calculationType === 'mass_to_moles' && (
                <div className="mb-6">
                    <label className="block text-sm font-medium text-gray-700 mb-2">Mass (g):</label>
                    <input 
                        type="number" 
                        step="0.001"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={mass} 
                        onChange={(e) => !isSubmitted && setMass(e.target.value)} 
                        placeholder="Enter mass in grams" 
                        disabled={isSubmitted} 
                    />
                </div>
            )}

            {calculationType === 'moles_to_mass' && (
                <div className="mb-6">
                    <label className="block text-sm font-medium text-gray-700 mb-2">Moles (mol):</label>
                    <input 
                        type="number" 
                        step="0.001"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={moles} 
                        onChange={(e) => !isSubmitted && setMoles(e.target.value)} 
                        placeholder="Enter number of moles" 
                        disabled={isSubmitted} 
                    />
                </div>
            )}

            {(calculationType === 'concentration' || calculationType === 'dilution') && (
                <>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-gray-700 mb-2">Moles (mol):</label>
                        <input 
                            type="number" 
                            step="0.001"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={moles} 
                            onChange={(e) => !isSubmitted && setMoles(e.target.value)} 
                            placeholder="Enter number of moles" 
                            disabled={isSubmitted} 
                        />
                    </div>
                    <div className="mb-6">
                        <label className="block text-sm font-medium text-gray-700 mb-2">Volume (L):</label>
                        <input 
                            type="number" 
                            step="0.001"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={volume} 
                            onChange={(e) => !isSubmitted && setVolume(e.target.value)} 
                            placeholder="Enter volume in liters" 
                            disabled={isSubmitted} 
                        />
                    </div>
                </>
            )}

            {calculationType === 'stoichiometry' && (
                <div className="mb-6">
                    <label className="block text-sm font-medium text-gray-700 mb-2">Mass (g):</label>
                    <input 
                        type="number" 
                        step="0.001"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={mass} 
                        onChange={(e) => !isSubmitted && setMass(e.target.value)} 
                        placeholder="Enter mass in grams" 
                        disabled={isSubmitted} 
                    />
                </div>
            )}

            {/* Calculate Button */}
            {!isSubmitted && (
                <div className="mb-6 text-center">
                    <button 
                        onClick={handleCalculate}
                        className="px-6 py-3 bg-green-600 text-white rounded-lg text-lg font-medium hover:bg-green-700 transition-colors"
                    >
                        Calculate
                    </button>
                </div>
            )}

            {/* Results Display */}
            {showResults && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Results:</h4>
                    <div className="space-y-3">
                        {calculationType === 'molar_mass' && (
                            <div className="text-center">
                                <div className="text-2xl font-bold text-green-700">
                                    {formatNumber(getResults().molarMass)} g/mol
                                </div>
                                <div className="text-sm text-green-600 mt-1">
                                    Molar Mass of {formula}
                                </div>
                            </div>
                        )}
                        
                        {calculationType === 'mass_to_moles' && (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div className="text-center p-3 bg-white rounded border">
                                    <div className="text-lg font-semibold text-gray-800">Molar Mass</div>
                                    <div className="text-xl text-green-700">{formatNumber(getResults().molarMass)} g/mol</div>
                                </div>
                                <div className="text-center p-3 bg-white rounded border">
                                    <div className="text-lg font-semibold text-gray-800">Moles</div>
                                    <div className="text-xl text-green-700">{formatNumber(getResults().moles)} mol</div>
                                </div>
                            </div>
                        )}
                        
                        {calculationType === 'moles_to_mass' && (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div className="text-center p-3 bg-white rounded border">
                                    <div className="text-lg font-semibold text-gray-800">Molar Mass</div>
                                    <div className="text-xl text-green-700">{formatNumber(getResults().molarMass)} g/mol</div>
                                </div>
                                <div className="text-center p-3 bg-white rounded border">
                                    <div className="text-lg font-semibold text-gray-800">Mass</div>
                                    <div className="text-xl text-green-700">{formatNumber(getResults().mass)} g</div>
                                </div>
                            </div>
                        )}
                        
                        {calculationType === 'concentration' && (
                            <div className="text-center">
                                <div className="text-2xl font-bold text-green-700">
                                    {formatNumber(getResults().molarity)} M
                                </div>
                                <div className="text-sm text-green-600 mt-1">
                                    Concentration (Molarity)
                                </div>
                            </div>
                        )}
                        
                        {calculationType === 'stoichiometry' && (
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                <div className="text-center p-3 bg-white rounded border">
                                    <div className="text-lg font-semibold text-gray-800">Molar Mass</div>
                                    <div className="text-xl text-green-700">{formatNumber(getResults().molarMass)} g/mol</div>
                                </div>
                                <div className="text-center p-3 bg-white rounded border">
                                    <div className="text-lg font-semibold text-gray-800">Moles</div>
                                    <div className="text-xl text-green-700">{formatNumber(getResults().moles)} mol</div>
                                </div>
                            </div>
                        )}
                    </div>
                </div>
            )}

            {/* Calculation Steps */}
            {showSteps && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Calculation Steps:</h4>
                    <div className="space-y-2">
                        {getCalculationSteps().map((step, index) => (
                            <div key={index} className="text-sm text-blue-700">{step}</div>
                        ))}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Use proper chemical formulas (e.g., H₂SO₄, not H2SO4)</li>
                    <li>• Ensure units are consistent (grams for mass, liters for volume)</li>
                    <li>• Molarity (M) = moles ÷ volume (L)</li>
                    <li>• For stoichiometry, start by converting to moles</li>
                    <li>• Always check your units and significant figures</li>
                </ul>
            </div>
        </div>
    );
};

export default MoleCalculator;
