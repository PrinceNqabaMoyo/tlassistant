import React, { useState, useEffect } from 'react';

const ElectrochemistrySimulator = ({ initialData, onChange, isSubmitted }) => {
    const [cellType, setCellType] = useState(initialData.cellType || 'galvanic');
    const [anode, setAnode] = useState(initialData.anode || 'Zn');
    const [cathode, setCathode] = useState(initialData.cathode || 'Cu');
    const [anodeConcentration, setAnodeConcentration] = useState(initialData.anodeConcentration || 1.0);
    const [cathodeConcentration, setCathodeConcentration] = useState(initialData.cathodeConcentration || 1.0);
    const [temperature, setTemperature] = useState(initialData.temperature || 298);
    const [showCellDiagram, setShowCellDiagram] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [showElectrolysis, setShowElectrolysis] = useState(false);

    // Common half-reactions and their standard potentials
    const halfReactions = {
        'Zn': {
            reaction: 'Zn²⁺ + 2e⁻ → Zn',
            E°: -0.76,
            type: 'reduction',
            description: 'Zinc reduction'
        },
        'Cu': {
            reaction: 'Cu²⁺ + 2e⁻ → Cu',
            E°: 0.34,
            type: 'reduction',
            description: 'Copper reduction'
        },
        'Fe': {
            reaction: 'Fe²⁺ + 2e⁻ → Fe',
            E°: -0.44,
            type: 'reduction',
            description: 'Iron reduction'
        },
        'Ag': {
            reaction: 'Ag⁺ + e⁻ → Ag',
            E°: 0.80,
            type: 'reduction',
            description: 'Silver reduction'
        },
        'Al': {
            reaction: 'Al³⁺ + 3e⁻ → Al',
            E°: -1.66,
            type: 'reduction',
            description: 'Aluminum reduction'
        },
        'Ni': {
            reaction: 'Ni²⁺ + 2e⁻ → Ni',
            E°: -0.25,
            type: 'reduction',
            description: 'Nickel reduction'
        },
        'H2': {
            reaction: '2H⁺ + 2e⁻ → H₂',
            E°: 0.00,
            type: 'reduction',
            description: 'Hydrogen reduction'
        },
        'O2': {
            reaction: 'O₂ + 4H⁺ + 4e⁻ → 2H₂O',
            E°: 1.23,
            type: 'reduction',
            description: 'Oxygen reduction'
        }
    };

    // Electrolysis reactions
    const electrolysisReactions = {
        'water': {
            name: 'Water Electrolysis',
            anode: '2H₂O → O₂ + 4H⁺ + 4e⁻',
            cathode: '2H⁺ + 2e⁻ → H₂',
            overall: '2H₂O → 2H₂ + O₂',
            voltage: 1.23,
            description: 'Decomposition of water into hydrogen and oxygen'
        },
        'sodium_chloride': {
            name: 'Sodium Chloride Electrolysis',
            anode: '2Cl⁻ → Cl₂ + 2e⁻',
            cathode: '2H⁺ + 2e⁻ → H₂',
            overall: '2NaCl + 2H₂O → 2NaOH + H₂ + Cl₂',
            voltage: 2.19,
            description: 'Chlor-alkali process'
        },
        'copper_sulfate': {
            name: 'Copper Sulfate Electrolysis',
            anode: 'Cu → Cu²⁺ + 2e⁻',
            cathode: 'Cu²⁺ + 2e⁻ → Cu',
            overall: 'Cu (anode) → Cu (cathode)',
            voltage: 0.0,
            description: 'Copper purification'
        }
    };

    useEffect(() => {
        const formattedData = {
            type: "electrochemistry_simulator",
            cellType: cellType,
            anode: anode,
            cathode: cathode,
            anodeConcentration: anodeConcentration,
            cathodeConcentration: cathodeConcentration,
            temperature: temperature,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [cellType, anode, cathode, anodeConcentration, cathodeConcentration, temperature, onChange]);

    const calculateResults = () => {
        const results = {};
        
        if (cellType === 'galvanic') {
            // Galvanic cell calculations
            results.cellPotential = calculateCellPotential();
            results.anodeReaction = getAnodeReaction();
            results.cathodeReaction = getCathodeReaction();
            results.overallReaction = getOverallReaction();
            results.standardPotential = calculateStandardPotential();
            results.nernstPotential = calculateNernstPotential();
        } else {
            // Electrolysis calculations
            results.requiredVoltage = calculateRequiredVoltage();
            results.electrolysisReaction = getElectrolysisReaction();
        }
        
        return results;
    };

    const calculateCellPotential = () => {
        if (cellType === 'galvanic') {
            const anodePotential = -halfReactions[anode].E°; // Oxidation potential
            const cathodePotential = halfReactions[cathode].E°; // Reduction potential
            return cathodePotential + anodePotential;
        }
        return 0;
    };

    const getAnodeReaction = () => {
        const reaction = halfReactions[anode];
        return reaction.reaction.split('→')[1].trim() + ' → ' + reaction.reaction.split('→')[0].trim();
    };

    const getCathodeReaction = () => {
        return halfReactions[cathode].reaction;
    };

    const getOverallReaction = () => {
        const anodeReaction = getAnodeReaction();
        const cathodeReaction = getCathodeReaction();
        
        // Simplify to show overall reaction
        const anodeProduct = anodeReaction.split('→')[1].trim();
        const cathodeProduct = cathodeReaction.split('→')[1].trim();
        
        return `${anodeProduct} + ${cathodeReaction.split('→')[0].trim()} → ${anodeReaction.split('→')[0].trim()} + ${cathodeProduct}`;
    };

    const calculateStandardPotential = () => {
        return calculateCellPotential();
    };

    const calculateNernstPotential = () => {
        const E° = calculateStandardPotential();
        const R = 8.314; // J/(mol·K)
        const F = 96485; // C/mol
        const T = temperature;
        const n = 2; // Assuming 2 electrons for most reactions
        
        // Simplified Nernst equation for concentration cells
        const Q = cathodeConcentration / anodeConcentration;
        const E = E° - (R * T / (n * F)) * Math.log(Q);
        
        return E;
    };

    const calculateRequiredVoltage = () => {
        if (cellType === 'electrolysis') {
            // For electrolysis, we need to overcome the cell potential
            const cellPotential = calculateCellPotential();
            return Math.abs(cellPotential) + 0.5; // Add overpotential
        }
        return 0;
    };

    const getElectrolysisReaction = () => {
        if (cellType === 'electrolysis') {
            // Return appropriate electrolysis reaction based on selected elements
            if (anode === 'H2' && cathode === 'O2') {
                return electrolysisReactions.water;
            } else if (anode === 'Cl' && cathode === 'Na') {
                return electrolysisReactions.sodium_chloride;
            } else {
                return electrolysisReactions.copper_sulfate;
            }
        }
        return null;
    };

    const getCellNotation = () => {
        if (cellType === 'galvanic') {
            return `${anode}(s) | ${anode}²⁺(aq, ${anodeConcentration}M) || ${cathode}²⁺(aq, ${cathodeConcentration}M) | ${cathode}(s)`;
        }
        return '';
    };

    const getSpontaneity = () => {
        const potential = calculateCellPotential();
        if (potential > 0) {
            return { spontaneous: true, description: 'Reaction is spontaneous (galvanic cell)' };
        } else if (potential < 0) {
            return { spontaneous: false, description: 'Reaction is non-spontaneous (electrolysis required)' };
        } else {
            return { spontaneous: null, description: 'Reaction is at equilibrium' };
        }
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        if (Math.abs(num) < 0.001) return num.toExponential(3);
        return num.toFixed(3);
    };

    const results = calculateResults();
    const spontaneity = getSpontaneity();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Electrochemistry Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowCellDiagram(!showCellDiagram)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showCellDiagram 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showCellDiagram ? 'Hide Cell Diagram' : 'Show Cell Diagram'}
                    </button>
                    <button
                        onClick={() => setShowCalculations(!showCalculations)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showCalculations 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showCalculations ? 'Hide Calculations' : 'Show Calculations'}
                    </button>
                    <button
                        onClick={() => setShowElectrolysis(!showElectrolysis)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showElectrolysis 
                                ? 'bg-purple-100 text-purple-700 hover:bg-purple-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showElectrolysis ? 'Hide Electrolysis' : 'Show Electrolysis'}
                    </button>
                </div>
            </div>

            {/* Cell Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Cell Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={cellType} 
                    onChange={(e) => !isSubmitted && setCellType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="galvanic">Galvanic Cell (Voltaic Cell)</option>
                    <option value="electrolysis">Electrolytic Cell</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {cellType === 'galvanic' 
                        ? 'Galvanic cells convert chemical energy to electrical energy through spontaneous redox reactions.'
                        : 'Electrolytic cells use electrical energy to drive non-spontaneous redox reactions.'
                    }
                </p>
            </div>

            {/* Electrode Configuration */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-red-50 rounded-lg border border-red-200">
                    <h4 className="text-md font-medium text-red-800 mb-3">Anode (Oxidation):</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Anode Material:</label>
                            <select 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors" 
                                value={anode} 
                                onChange={(e) => !isSubmitted && setAnode(e.target.value)} 
                                disabled={isSubmitted}
                            >
                                {Object.keys(halfReactions).map(key => (
                                    <option key={key} value={key}>{key} ({halfReactions[key].reaction})</option>
                                ))}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Concentration (M):</label>
                            <input 
                                type="number" 
                                min="0.001" 
                                max="10"
                                step="0.001"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors" 
                                value={anodeConcentration} 
                                onChange={(e) => !isSubmitted && setAnodeConcentration(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Cathode (Reduction):</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Cathode Material:</label>
                            <select 
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={cathode} 
                                onChange={(e) => !isSubmitted && setCathode(e.target.value)} 
                                disabled={isSubmitted}
                            >
                                {Object.keys(halfReactions).map(key => (
                                    <option key={key} value={key}>{key} ({halfReactions[key].reaction})</option>
                                ))}
                            </select>
                        </div>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Concentration (M):</label>
                            <input 
                                type="number" 
                                min="0.001" 
                                max="10"
                                step="0.001"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={cathodeConcentration} 
                                onChange={(e) => !isSubmitted && setCathodeConcentration(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
            </div>

            {/* Temperature */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Temperature (K):</label>
                <input 
                    type="number" 
                    min="273" 
                    max="373"
                    step="1"
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={temperature} 
                    onChange={(e) => !isSubmitted && setTemperature(parseFloat(e.target.value))} 
                    disabled={isSubmitted} 
                />
                <p className="text-xs text-gray-500 mt-1">
                    Range: 273K - 373K ({(temperature - 273.15).toFixed(1)}°C)
                </p>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                <h4 className="text-md font-medium text-green-800 mb-3">Cell Results:</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">
                            {cellType === 'galvanic' ? 'Cell Potential' : 'Required Voltage'}
                        </div>
                        <div className="text-xl text-green-700">
                            {formatNumber(cellType === 'galvanic' ? results.cellPotential : results.requiredVoltage)} V
                        </div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Standard Potential</div>
                        <div className="text-xl text-green-700">
                            {cellType === 'galvanic' ? formatNumber(results.standardPotential) : 'N/A'} V
                        </div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Spontaneity</div>
                        <div className={`text-sm px-2 py-1 rounded-full inline-block ${
                            spontaneity.spontaneous === true 
                                ? 'bg-green-100 text-green-800' 
                                : spontaneity.spontaneous === false
                                ? 'bg-red-100 text-red-800'
                                : 'bg-yellow-100 text-yellow-800'
                        }`}>
                            {spontaneity.spontaneous === true ? 'Spontaneous' : 
                             spontaneity.spontaneous === false ? 'Non-spontaneous' : 'Equilibrium'}
                        </div>
                    </div>
                </div>
            </div>

            {/* Cell Notation */}
            <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                <h4 className="text-md font-medium text-gray-800 mb-3">Cell Notation:</h4>
                <div className="p-3 bg-white rounded border font-mono text-sm">
                    {getCellNotation()}
                </div>
                <p className="text-sm text-gray-600 mt-2">
                    This notation shows the cell structure: anode | anode solution || cathode solution | cathode
                </p>
            </div>

            {/* Half Reactions */}
            <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                <h4 className="text-md font-medium text-yellow-800 mb-3">Half Reactions:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">Anode (Oxidation):</h5>
                        <div className="text-sm text-gray-600 font-mono">
                            {results.anodeReaction}
                        </div>
                        <div className="text-xs text-gray-500 mt-1">
                            E° = {formatNumber(-halfReactions[anode].E°)} V
                        </div>
                    </div>
                    <div className="p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">Cathode (Reduction):</h5>
                        <div className="text-sm text-gray-600 font-mono">
                            {results.cathodeReaction}
                        </div>
                        <div className="text-xs text-gray-500 mt-1">
                            E° = {formatNumber(halfReactions[cathode].E°)} V
                        </div>
                    </div>
                </div>
                <div className="mt-3 p-3 bg-white rounded border">
                    <h5 className="font-medium text-gray-800 mb-2">Overall Reaction:</h5>
                    <div className="text-sm text-gray-600 font-mono">
                        {results.overallReaction}
                    </div>
                </div>
            </div>

            {/* Nernst Equation Results */}
            {cellType === 'galvanic' && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Nernst Equation Results:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Standard Potential (E°):</h5>
                            <div className="text-lg text-blue-700">{formatNumber(results.standardPotential)} V</div>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Nernst Potential (E):</h5>
                            <div className="text-lg text-blue-700">{formatNumber(results.nernstPotential)} V</div>
                        </div>
                    </div>
                    <p className="text-sm text-blue-700 mt-3">
                        <strong>Nernst Equation:</strong> E = E° - (RT/nF) × ln(Q)
                    </p>
                </div>
            )}

            {/* Cell Diagram */}
            {showCellDiagram && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Cell Diagram:</h4>
                    <div className="h-64 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 200">
                            {/* Salt bridge */}
                            <line x1="200" y1="20" x2="200" y2="180" stroke="black" strokeWidth="3" strokeDasharray="5,5" />
                            
                            {/* Left compartment (anode) */}
                            <rect x="20" y="40" width="160" height="120" fill="none" stroke="black" strokeWidth="2" />
                            <text x="100" y="60" className="text-xs text-center">Anode Compartment</text>
                            <text x="100" y="80" className="text-xs text-center">{anode}(s)</text>
                            <text x="100" y="100" className="text-xs text-center">{anode}²⁺({anodeConcentration}M)</text>
                            <text x="100" y="120" className="text-xs text-center">Oxidation</text>
                            
                            {/* Right compartment (cathode) */}
                            <rect x="220" y="40" width="160" height="120" fill="none" stroke="black" strokeWidth="2" />
                            <text x="300" y="60" className="text-xs text-center">Cathode Compartment</text>
                            <text x="300" y="80" className="text-xs text-center">{cathode}(s)</text>
                            <text x="300" y="100" className="text-xs text-center">{cathode}²⁺({cathodeConcentration}M)</text>
                            <text x="300" y="120" className="text-xs text-center">Reduction</text>
                            
                            {/* Electron flow */}
                            <path d="M 180 100 Q 190 90 200 100 Q 210 110 220 100" fill="none" stroke="red" strokeWidth="2" markerEnd="url(#arrowhead)" />
                            <defs>
                                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                                    <polygon points="0 0, 10 3.5, 0 7" fill="red" />
                                </marker>
                            </defs>
                            
                            {/* Labels */}
                            <text x="100" y="180" className="text-xs text-center">e⁻ flow</text>
                            <text x="300" y="180" className="text-xs text-center">Salt Bridge</text>
                        </svg>
                    </div>
                </div>
            )}

            {/* Electrolysis Information */}
            {showElectrolysis && cellType === 'electrolysis' && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Electrolysis Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Required Voltage:</h5>
                            <div className="text-lg text-purple-700">{formatNumber(results.requiredVoltage)} V</div>
                            <p className="text-sm text-gray-600 mt-2">
                                This voltage overcomes the cell potential and provides energy for the reaction.
                            </p>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Process Type:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Anode:</strong> Oxidation (loss of electrons)</div>
                                <div><strong>Cathode:</strong> Reduction (gain of electrons)</div>
                                <div><strong>Energy:</strong> Electrical → Chemical</div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Standard Cell Potential:</strong> E°cell = E°cathode - E°anode</div>
                        <div><strong>Where:</strong></div>
                        <div>• E°cathode = {formatNumber(halfReactions[cathode].E°)} V</div>
                        <div>• E°anode = {formatNumber(-halfReactions[anode].E°)} V</div>
                        <div>• E°cell = {formatNumber(halfReactions[cathode].E°)} - ({formatNumber(-halfReactions[anode].E°)}) = {formatNumber(results.standardPotential)} V</div>
                        <div><strong>Nernst Equation:</strong> E = E° - (RT/nF) × ln(Q)</div>
                        <div><strong>Where:</strong> R = 8.314 J/(mol·K), F = 96485 C/mol, T = {temperature} K, n = 2</div>
                        <div><strong>Reaction Quotient:</strong> Q = [{cathode}²⁺] / [{anode}²⁺] = {formatNumber(cathodeConcentration)} / {formatNumber(anodeConcentration)} = {formatNumber(cathodeConcentration / anodeConcentration)}</div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Galvanic cells: E° > 0 means spontaneous reaction</li>
                    <li>• Electrolytic cells: E° < 0 means external voltage required</li>
                    <li>• Higher concentration difference increases cell potential</li>
                    <li>• Temperature affects Nernst equation calculations</li>
                    <li>• Salt bridge maintains electrical neutrality</li>
                </ul>
            </div>
        </div>
    );
};

export default ElectrochemistrySimulator;
