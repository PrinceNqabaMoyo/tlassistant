import React, { useState, useEffect } from 'react';

const AcidBaseTitration = ({ initialData, onChange, isSubmitted }) => {
    const [acidType, setAcidType] = useState(initialData.acidType || 'strong');
    const [baseType, setBaseType] = useState(initialData.baseType || 'strong');
    const [acidConcentration, setAcidConcentration] = useState(initialData.acidConcentration || 0.1);
    const [baseConcentration, setBaseConcentration] = useState(initialData.baseConcentration || 0.1);
    const [acidVolume, setAcidVolume] = useState(initialData.acidVolume || 25);
    const [baseVolume, setBaseVolume] = useState(initialData.baseVolume || 0);
    const [showPHCurve, setShowPHCurve] = useState(false);
    const [showBufferInfo, setShowBufferInfo] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);

    // Acid and base types with their properties
    const acidTypes = {
        'strong': {
            name: 'Strong Acid',
            description: 'Completely dissociates in water',
            examples: ['HCl', 'H₂SO₄', 'HNO₃'],
            dissociation: 1.0
        },
        'weak': {
            name: 'Weak Acid',
            description: 'Partially dissociates in water',
            examples: ['CH₃COOH', 'HF', 'H₂CO₃'],
            dissociation: 0.01
        }
    };

    const baseTypes = {
        'strong': {
            name: 'Strong Base',
            description: 'Completely dissociates in water',
            examples: ['NaOH', 'KOH', 'Ca(OH)₂'],
            dissociation: 1.0
        },
        'weak': {
            name: 'Weak Base',
            description: 'Partially dissociates in water',
            examples: ['NH₃', 'CH₃NH₂', '(CH₃)₂NH'],
            dissociation: 0.01
        }
    };

    // Common indicators and their pH ranges
    const indicators = {
        'phenolphthalein': {
            name: 'Phenolphthalein',
            pHRange: [8.3, 10.0],
            colorChange: 'Colorless → Pink',
            description: 'Good for strong acid-strong base titrations'
        },
        'methyl_orange': {
            name: 'Methyl Orange',
            pHRange: [3.1, 4.4],
            colorChange: 'Red → Yellow',
            description: 'Good for strong acid-strong base titrations'
        },
        'bromothymol_blue': {
            name: 'Bromothymol Blue',
            pHRange: [6.0, 7.6],
            colorChange: 'Yellow → Blue',
            description: 'Good for weak acid-strong base titrations'
        },
        'universal': {
            name: 'Universal Indicator',
            pHRange: [0, 14],
            colorChange: 'Red → Orange → Yellow → Green → Blue → Purple',
            description: 'Shows approximate pH across entire range'
        }
    };

    useEffect(() => {
        const formattedData = {
            type: "acid_base_titration",
            acidType: acidType,
            baseType: baseType,
            acidConcentration: acidConcentration,
            baseConcentration: baseConcentration,
            acidVolume: acidVolume,
            baseVolume: baseVolume,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [acidType, baseType, acidConcentration, baseConcentration, acidVolume, baseVolume, onChange]);

    const calculateResults = () => {
        const results = {};
        
        // Calculate moles of acid and base
        const acidMoles = acidConcentration * acidVolume / 1000;
        const baseMoles = baseConcentration * baseVolume / 1000;
        
        // Calculate equivalence point volume
        results.equivalenceVolume = (acidMoles / baseConcentration) * 1000;
        
        // Calculate pH at different points
        results.pHCurve = calculatePHCurve();
        
        // Calculate buffer region
        results.bufferRegion = calculateBufferRegion();
        
        // Calculate equivalence point pH
        results.equivalencePH = calculateEquivalencePH();
        
        // Calculate half-equivalence point
        results.halfEquivalenceVolume = results.equivalenceVolume / 2;
        results.halfEquivalencePH = calculateHalfEquivalencePH();
        
        return results;
    };

    const calculatePHCurve = () => {
        const points = [];
        const maxVolume = Math.max(baseVolume, 50); // Show at least 50mL
        
        for (let vol = 0; vol <= maxVolume; vol += maxVolume / 100) {
            const pH = calculatePH(vol);
            points.push({ volume: vol, pH: pH });
        }
        
        return points;
    };

    const calculatePH = (baseVol) => {
        const acidMoles = acidConcentration * acidVolume / 1000;
        const baseMoles = baseConcentration * baseVol / 1000;
        const totalVolume = acidVolume + baseVol;
        
        if (baseVol === 0) {
            // Initial pH (only acid)
            if (acidType === 'strong') {
                return -Math.log10(acidConcentration);
            } else {
                // Weak acid - use Ka approximation
                const Ka = 1e-5; // Example Ka value
                const H = Math.sqrt(Ka * acidConcentration);
                return -Math.log10(H);
            }
        } else if (baseVol < (acidMoles / baseConcentration) * 1000) {
            // Before equivalence point
            const remainingAcidMoles = acidMoles - baseMoles;
            const remainingAcidConc = remainingAcidMoles / (totalVolume / 1000);
            
            if (acidType === 'strong') {
                return -Math.log10(remainingAcidConc);
            } else {
                // Buffer region for weak acid
                const Ka = 1e-5;
                const pH = -Math.log10(Ka) + Math.log10(baseMoles / remainingAcidMoles);
                return pH;
            }
        } else if (Math.abs(baseVol - (acidMoles / baseConcentration) * 1000) < 0.1) {
            // At equivalence point
            return calculateEquivalencePH();
        } else {
            // After equivalence point
            const excessBaseMoles = baseMoles - acidMoles;
            const excessBaseConc = excessBaseMoles / (totalVolume / 1000);
            
            if (baseType === 'strong') {
                const pOH = -Math.log10(excessBaseConc);
                return 14 - pOH;
            } else {
                // Weak base in excess
                const Kb = 1e-5;
                const OH = Math.sqrt(Kb * excessBaseConc);
                const pOH = -Math.log10(OH);
                return 14 - pOH;
            }
        }
    };

    const calculateEquivalencePH = () => {
        if (acidType === 'strong' && baseType === 'strong') {
            return 7.0; // Neutral
        } else if (acidType === 'weak' && baseType === 'strong') {
            // Weak acid + strong base → basic solution
            const Ka = 1e-5;
            const Kb = 1e-9; // Kw/Ka
            const saltConc = (acidConcentration * acidVolume) / (acidVolume + (acidConcentration * acidVolume / baseConcentration));
            const OH = Math.sqrt(Kb * saltConc);
            const pOH = -Math.log10(OH);
            return 14 - pOH;
        } else if (acidType === 'strong' && baseType === 'weak') {
            // Strong acid + weak base → acidic solution
            const Kb = 1e-5;
            const Ka = 1e-9; // Kw/Kb
            const saltConc = (baseConcentration * (acidConcentration * acidVolume / baseConcentration)) / (acidVolume + (acidConcentration * acidVolume / baseConcentration));
            const H = Math.sqrt(Ka * saltConc);
            return -Math.log10(H);
        } else {
            // Weak acid + weak base → depends on relative strengths
            return 7.0; // Simplified
        }
    };

    const calculateHalfEquivalencePH = () => {
        if (acidType === 'weak') {
            const Ka = 1e-5;
            return -Math.log10(Ka); // pKa
        } else {
            return 7.0; // For strong acids
        }
    };

    const calculateBufferRegion = () => {
        if (acidType === 'weak' && baseType === 'strong') {
            const startVolume = 0;
            const endVolume = (acidConcentration * acidVolume / baseConcentration) * 1000;
            return {
                start: startVolume,
                end: endVolume,
                description: 'Buffer region exists before equivalence point for weak acid-strong base titrations'
            };
        }
        return null;
    };

    const getIndicatorRecommendation = () => {
        const equivalencePH = calculateEquivalencePH();
        
        if (equivalencePH >= 8.3 && equivalencePH <= 10.0) {
            return indicators.phenolphthalein;
        } else if (equivalencePH >= 3.1 && equivalencePH <= 4.4) {
            return indicators.methyl_orange;
        } else if (equivalencePH >= 6.0 && equivalencePH <= 7.6) {
            return indicators.bromothymol_blue;
        } else {
            return indicators.universal;
        }
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        if (num < 0.001) return num.toExponential(3);
        return num.toFixed(3);
    };

    const results = calculateResults();
    const recommendedIndicator = getIndicatorRecommendation();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Acid-Base Titration Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowPHCurve(!showPHCurve)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showPHCurve 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showPHCurve ? 'Hide pH Curve' : 'Show pH Curve'}
                    </button>
                    <button
                        onClick={() => setShowBufferInfo(!showBufferInfo)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showBufferInfo 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showBufferInfo ? 'Hide Buffer Info' : 'Show Buffer Info'}
                    </button>
                    <button
                        onClick={() => setShowCalculations(!showCalculations)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showCalculations 
                                ? 'bg-yellow-100 text-yellow-700 hover:bg-yellow-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showCalculations ? 'Hide Calculations' : 'Show Calculations'}
                    </button>
                </div>
            </div>

            {/* Acid Configuration */}
            <div className="mb-6 p-4 bg-red-50 rounded-lg border border-red-200">
                <h4 className="text-md font-medium text-red-800 mb-3">Acid Configuration:</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Acid Type:</label>
                        <select 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors" 
                            value={acidType} 
                            onChange={(e) => !isSubmitted && setAcidType(e.target.value)} 
                            disabled={isSubmitted}
                        >
                            {Object.entries(acidTypes).map(([key, acid]) => (
                                <option key={key} value={key}>{acid.name}</option>
                            ))}
                        </select>
                        {acidTypes[acidType] && (
                            <p className="text-sm text-red-600 mt-2">
                                {acidTypes[acidType].description}
                            </p>
                        )}
                    </div>
                    
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Concentration (M):</label>
                        <input 
                            type="number" 
                            min="0.01" 
                            max="2.0"
                            step="0.01"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors" 
                            value={acidConcentration} 
                            onChange={(e) => !isSubmitted && setAcidConcentration(parseFloat(e.target.value))} 
                            disabled={isSubmitted} 
                        />
                    </div>
                    
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Volume (mL):</label>
                        <input 
                            type="number" 
                            min="10" 
                            max="100"
                            step="1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-red-500 focus:border-red-500 transition-colors" 
                            value={acidVolume} 
                            onChange={(e) => !isSubmitted && setAcidVolume(parseFloat(e.target.value))} 
                            disabled={isSubmitted} 
                        />
                    </div>
                </div>
            </div>

            {/* Base Configuration */}
            <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                <h4 className="text-md font-medium text-blue-800 mb-3">Base Configuration:</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Base Type:</label>
                        <select 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={baseType} 
                            onChange={(e) => !isSubmitted && setBaseType(e.target.value)} 
                            disabled={isSubmitted}
                        >
                            {Object.entries(baseTypes).map(([key, base]) => (
                                <option key={key} value={key}>{base.name}</option>
                            ))}
                        </select>
                        {baseTypes[baseType] && (
                            <p className="text-sm text-blue-600 mt-2">
                                {baseTypes[baseType].description}
                            </p>
                        )}
                    </div>
                    
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Concentration (M):</label>
                        <input 
                            type="number" 
                            min="0.01" 
                            max="2.0"
                            step="0.01"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={baseConcentration} 
                            onChange={(e) => !isSubmitted && setBaseConcentration(parseFloat(e.target.value))} 
                            disabled={isSubmitted} 
                        />
                    </div>
                    
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Volume Added (mL):</label>
                        <input 
                            type="number" 
                            min="0" 
                            max="100"
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={baseVolume} 
                            onChange={(e) => !isSubmitted && setBaseVolume(parseFloat(e.target.value))} 
                            disabled={isSubmitted} 
                        />
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                <h4 className="text-md font-medium text-green-800 mb-3">Titration Results:</h4>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Current pH</div>
                        <div className="text-xl text-green-700">{formatNumber(calculatePH(baseVolume))}</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Equivalence Volume</div>
                        <div className="text-xl text-green-700">{formatNumber(results.equivalenceVolume)} mL</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Equivalence pH</div>
                        <div className="text-xl text-green-700">{formatNumber(results.equivalencePH)}</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Half-Equivalence pH</div>
                        <div className="text-xl text-green-700">{formatNumber(results.halfEquivalencePH)}</div>
                    </div>
                </div>
            </div>

            {/* pH Curve */}
            {showPHCurve && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">pH vs Volume Curve:</h4>
                    <div className="h-64 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 200">
                            {/* Graph axes */}
                            <line x1="20" y1="20" x2="20" y2="180" stroke="black" strokeWidth="2" />
                            <line x1="20" y1="180" x2="380" y2="180" stroke="black" strokeWidth="2" />
                            
                            {/* Y-axis label */}
                            <text x="10" y="100" transform="rotate(-90 10 100)" className="text-xs">pH</text>
                            
                            {/* X-axis label */}
                            <text x="200" y="195" className="text-xs">Base Volume (mL)</text>
                            
                            {/* pH scale markers */}
                            <text x="15" y="25" className="text-xs">14</text>
                            <text x="15" y="45" className="text-xs">12</text>
                            <text x="15" y="65" className="text-xs">10</text>
                            <text x="15" y="85" className="text-xs">8</text>
                            <text x="15" y="105" className="text-xs">6</text>
                            <text x="15" y="125" className="text-xs">4</text>
                            <text x="15" y="145" className="text-xs">2</text>
                            <text x="15" y="165" className="text-xs">0</text>
                            
                            {/* Plot pH curve */}
                            {results.pHCurve.map((point, i) => {
                                const x = 20 + (point.volume / Math.max(...results.pHCurve.map(p => p.volume))) * 360;
                                const y = 180 - (point.pH / 14) * 160;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="red" />;
                                
                                const prevPoint = results.pHCurve[i - 1];
                                const prevX = 20 + (prevPoint.volume / Math.max(...results.pHCurve.map(p => p.volume))) * 360;
                                const prevY = 180 - (prevPoint.pH / 14) * 160;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="red" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="red" />
                                    </g>
                                );
                            })}
                            
                            {/* Equivalence point marker */}
                            {results.equivalenceVolume && (
                                <g>
                                    <line 
                                        x1={20 + (results.equivalenceVolume / Math.max(...results.pHCurve.map(p => p.volume))) * 360} 
                                        y1="20" 
                                        x2={20 + (results.equivalenceVolume / Math.max(...results.pHCurve.map(p => p.volume))) * 360} 
                                        y2="180" 
                                        stroke="blue" 
                                        strokeWidth="2" 
                                        strokeDasharray="5,5"
                                    />
                                    <text 
                                        x={25 + (results.equivalenceVolume / Math.max(...results.pHCurve.map(p => p.volume))) * 360} 
                                        y="30" 
                                        className="text-xs fill-blue-600"
                                    >
                                        Equivalence Point
                                    </text>
                                </g>
                            )}
                        </svg>
                    </div>
                </div>
            )}

            {/* Buffer Information */}
            {showBufferInfo && results.bufferRegion && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Buffer Region Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Buffer Region:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Start:</strong> {formatNumber(results.bufferRegion.start)} mL</div>
                                <div><strong>End:</strong> {formatNumber(results.bufferRegion.end)} mL</div>
                                <div><strong>Description:</strong> {results.bufferRegion.description}</div>
                            </div>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Buffer Capacity:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Maximum Buffer Capacity:</strong> At half-equivalence point</div>
                                <div><strong>pH at Half-Equivalence:</strong> {formatNumber(results.halfEquivalencePH)}</div>
                                <div><strong>Buffer Range:</strong> ±1 pH unit from pKa</div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Indicator Recommendation */}
            <div className="mb-6 p-4 bg-indigo-50 rounded-lg border border-indigo-200">
                <h4 className="text-md font-medium text-indigo-800 mb-3">Indicator Recommendation:</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div className="p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">Recommended Indicator:</h5>
                        <div className="text-sm text-gray-600">
                            <div><strong>Name:</strong> {recommendedIndicator.name}</div>
                            <div><strong>pH Range:</strong> {recommendedIndicator.pHRange[0]} - {recommendedIndicator.pHRange[1]}</div>
                            <div><strong>Color Change:</strong> {recommendedIndicator.colorChange}</div>
                            <div><strong>Description:</strong> {recommendedIndicator.description}</div>
                        </div>
                    </div>
                    <div className="p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">All Available Indicators:</h5>
                        <div className="text-sm text-gray-600 space-y-1">
                            {Object.entries(indicators).map(([key, indicator]) => (
                                <div key={key}>
                                    <strong>{indicator.name}:</strong> pH {indicator.pHRange[0]}-{indicator.pHRange[1]}
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </div>

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Initial Acid Moles:</strong> {formatNumber(acidConcentration * acidVolume / 1000)} mol</div>
                        <div><strong>Base Moles Added:</strong> {formatNumber(baseConcentration * baseVolume / 1000)} mol</div>
                        <div><strong>Equivalence Point Volume:</strong> V = (n_acid × M_acid) / M_base = {formatNumber(results.equivalenceVolume)} mL</div>
                        <div><strong>Current pH Calculation:</strong> Based on acid-base equilibrium and buffer equations</div>
                        <div><strong>Buffer Equation:</strong> pH = pKa + log([A⁻]/[HA])</div>
                        <div><strong>Strong Acid/Base:</strong> pH = -log[H⁺] or pOH = -log[OH⁻]</div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Strong acid + strong base → neutral equivalence point (pH = 7)</li>
                    <li>• Weak acid + strong base → basic equivalence point (pH > 7)</li>
                    <li>• Strong acid + weak base → acidic equivalence point (pH < 7)</li>
                    <li>• Buffer region exists before equivalence point for weak acid-strong base</li>
                    <li>• Choose indicator with pH range near equivalence point</li>
                </ul>
            </div>
        </div>
    );
};

export default AcidBaseTitration;
