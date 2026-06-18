import React, { useState, useEffect } from 'react';

const ReactionRateSimulator = ({ initialData, onChange, isSubmitted }) => {
    const [reactionType, setReactionType] = useState(initialData.reactionType || 'first_order');
    const [temperature, setTemperature] = useState(initialData.temperature || 298);
    const [concentration, setConcentration] = useState(initialData.concentration || 1.0);
    const [catalyst, setCatalyst] = useState(initialData.catalyst || false);
    const [catalystType, setCatalystType] = useState(initialData.catalystType || 'enzyme');
    const [time, setTime] = useState(initialData.time || 0);
    const [showGraph, setShowGraph] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);

    // Reaction types and their rate laws
    const reactionTypes = {
        'zero_order': {
            name: 'Zero Order',
            rateLaw: 'Rate = k',
            description: 'Reaction rate is independent of reactant concentration',
            examples: ['Catalytic decomposition', 'Surface reactions']
        },
        'first_order': {
            name: 'First Order',
            rateLaw: 'Rate = k[A]',
            description: 'Reaction rate is directly proportional to reactant concentration',
            examples: ['Radioactive decay', 'Many decomposition reactions']
        },
        'second_order': {
            name: 'Second Order',
            rateLaw: 'Rate = k[A]² or Rate = k[A][B]',
            description: 'Reaction rate depends on concentration squared or product of two concentrations',
            examples: ['Dimerization', 'Bimolecular reactions']
        }
    };

    // Catalyst types and their effects
    const catalystTypes = {
        'enzyme': {
            name: 'Enzyme',
            activationEnergyReduction: 0.3,
            description: 'Biological catalysts that lower activation energy significantly',
            examples: ['Amylase', 'Catalase', 'DNA polymerase']
        },
        'metal': {
            name: 'Metal',
            activationEnergyReduction: 0.2,
            description: 'Metallic catalysts that provide surface for reactions',
            examples: ['Platinum', 'Nickel', 'Iron']
        },
        'acid_base': {
            name: 'Acid/Base',
            activationEnergyReduction: 0.15,
            description: 'Proton donors/acceptors that facilitate reactions',
            examples: ['Sulfuric acid', 'Sodium hydroxide', 'Ammonia']
        }
    };

    useEffect(() => {
        const formattedData = {
            type: "reaction_rate_simulator",
            reactionType: reactionType,
            temperature: temperature,
            concentration: concentration,
            catalyst: catalyst,
            catalystType: catalystType,
            time: time,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [reactionType, temperature, concentration, catalyst, catalystType, time, onChange]);

    const calculateResults = () => {
        const results = {};
        
        // Rate constant calculation using Arrhenius equation
        const Ea = 50000; // Activation energy in J/mol (example value)
        const A = 1e13; // Pre-exponential factor (example value)
        const R = 8.314; // Gas constant in J/(mol·K)
        
        let k = A * Math.exp(-Ea / (R * temperature));
        
        // Apply catalyst effect
        if (catalyst && catalystTypes[catalystType]) {
            const reduction = catalystTypes[catalystType].activationEnergyReduction;
            k = A * Math.exp(-(Ea * (1 - reduction)) / (R * temperature));
        }
        
        results.rateConstant = k;
        
        // Calculate reaction rate
        switch (reactionType) {
            case 'zero_order':
                results.reactionRate = k;
                break;
            case 'first_order':
                results.reactionRate = k * concentration;
                break;
            case 'second_order':
                results.reactionRate = k * concentration * concentration;
                break;
            default:
                results.reactionRate = 0;
        }
        
        // Calculate concentration over time
        results.concentrationOverTime = calculateConcentrationOverTime(k, concentration);
        
        // Calculate half-life
        results.halfLife = calculateHalfLife(k, reactionType);
        
        return results;
    };

    const calculateConcentrationOverTime = (k, initialConc) => {
        const timePoints = [];
        const concentrationPoints = [];
        const maxTime = reactionType === 'zero_order' ? initialConc / k : 10 / k;
        
        for (let t = 0; t <= maxTime; t += maxTime / 50) {
            timePoints.push(t);
            
            let conc;
            switch (reactionType) {
                case 'zero_order':
                    conc = Math.max(0, initialConc - k * t);
                    break;
                case 'first_order':
                    conc = initialConc * Math.exp(-k * t);
                    break;
                case 'second_order':
                    conc = initialConc / (1 + k * initialConc * t);
                    break;
                default:
                    conc = initialConc;
            }
            
            concentrationPoints.push(conc);
        }
        
        return { timePoints, concentrationPoints };
    };

    const calculateHalfLife = (k, type) => {
        switch (type) {
            case 'zero_order':
                return 0.5 / k;
            case 'first_order':
                return Math.log(2) / k;
            case 'second_order':
                return 1 / (k * concentration);
            default:
                return 0;
        }
    };

    const getTemperatureEffect = () => {
        const baseTemp = 298; // 25°C
        const baseRate = calculateResults().reactionRate;
        
        // Calculate rate at different temperatures
        const temp1 = baseTemp - 10;
        const temp2 = baseTemp + 10;
        
        const Ea = 50000;
        const A = 1e13;
        const R = 8.314;
        
        let k1 = A * Math.exp(-Ea / (R * temp1));
        let k2 = A * Math.exp(-Ea / (R * temp2));
        
        if (catalyst && catalystTypes[catalystType]) {
            const reduction = catalystTypes[catalystType].activationEnergyReduction;
            k1 = A * Math.exp(-(Ea * (1 - reduction)) / (R * temp1));
            k2 = A * Math.exp(-(Ea * (1 - reduction)) / (R * temp2));
        }
        
        let rate1, rate2;
        switch (reactionType) {
            case 'zero_order':
                rate1 = k1;
                rate2 = k2;
                break;
            case 'first_order':
                rate1 = k1 * concentration;
                rate2 = k2 * concentration;
                break;
            case 'second_order':
                rate1 = k1 * concentration * concentration;
                rate2 = k2 * concentration * concentration;
                break;
            default:
                rate1 = rate2 = 0;
        }
        
        return {
            temp1: temp1 - 273.15, // Convert to Celsius
            temp2: temp2 - 273.15,
            rate1,
            rate2,
            baseRate
        };
    };

    const getCatalystEffect = () => {
        if (!catalyst) return null;
        
        const withoutCatalyst = calculateResults().reactionRate;
        const withCatalyst = calculateResults().reactionRate;
        
        const catalystInfo = catalystTypes[catalystType];
        const activationEnergyReduction = catalystInfo.activationEnergyReduction;
        
        return {
            activationEnergyReduction: activationEnergyReduction * 100,
            rateIncrease: ((withCatalyst - withoutCatalyst) / withoutCatalyst) * 100,
            catalystName: catalystInfo.name,
            examples: catalystInfo.examples
        };
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        if (num < 0.001) return num.toExponential(3);
        return num.toFixed(4).replace(/\.?0+$/, '');
    };

    const results = calculateResults();
    const tempEffect = getTemperatureEffect();
    const catalystEffect = getCatalystEffect();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Reaction Rate Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowGraph(!showGraph)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showGraph 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showGraph ? 'Hide Graph' : 'Show Graph'}
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
                </div>
            </div>

            {/* Reaction Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Reaction Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={reactionType} 
                    onChange={(e) => !isSubmitted && setReactionType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    {Object.entries(reactionTypes).map(([key, type]) => (
                        <option key={key} value={key}>{type.name} - {type.rateLaw}</option>
                    ))}
                </select>
                {reactionTypes[reactionType] && (
                    <p className="text-sm text-gray-600 mt-2">
                        {reactionTypes[reactionType].description}
                    </p>
                )}
            </div>

            {/* Parameters Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Temperature (K):</label>
                    <input 
                        type="number" 
                        min="200" 
                        max="1000"
                        step="1"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={temperature} 
                        onChange={(e) => !isSubmitted && setTemperature(parseFloat(e.target.value))} 
                        disabled={isSubmitted} 
                    />
                    <p className="text-xs text-gray-500 mt-1">
                        Range: 200K - 1000K ({(temperature - 273.15).toFixed(1)}°C)
                    </p>
                </div>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Initial Concentration (M):</label>
                    <input 
                        type="number" 
                        min="0.1" 
                        max="10"
                        step="0.1"
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={concentration} 
                        onChange={(e) => !isSubmitted && setConcentration(parseFloat(e.target.value))} 
                        disabled={isSubmitted} 
                    />
                </div>
            </div>

            {/* Catalyst Options */}
            <div className="mb-6">
                <div className="flex items-center mb-3">
                    <input 
                        type="checkbox" 
                        id="catalyst"
                        className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                        checked={catalyst} 
                        onChange={(e) => !isSubmitted && setCatalyst(e.target.checked)} 
                        disabled={isSubmitted}
                    />
                    <label htmlFor="catalyst" className="text-sm font-medium text-gray-700">Use Catalyst</label>
                </div>
                
                {catalyst && (
                    <div className="ml-6">
                        <label className="block text-sm font-medium text-gray-700 mb-2">Catalyst Type:</label>
                        <select 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={catalystType} 
                            onChange={(e) => !isSubmitted && setCatalystType(e.target.value)} 
                            disabled={isSubmitted}
                        >
                            {Object.entries(catalystTypes).map(([key, cat]) => (
                                <option key={key} value={key}>{cat.name}</option>
                            ))}
                        </select>
                        {catalystTypes[catalystType] && (
                            <p className="text-sm text-gray-600 mt-2">
                                {catalystTypes[catalystType].description}
                            </p>
                        )}
                    </div>
                )}
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                <h4 className="text-md font-medium text-green-800 mb-3">Simulation Results:</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Rate Constant (k)</div>
                        <div className="text-xl text-green-700">{formatNumber(results.rateConstant)}</div>
                        <div className="text-xs text-gray-500">s⁻¹, M⁻¹s⁻¹, or M s⁻¹</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Reaction Rate</div>
                        <div className="text-xl text-green-700">{formatNumber(results.reactionRate)}</div>
                        <div className="text-xs text-gray-500">M s⁻¹</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Half-Life</div>
                        <div className="text-xl text-green-700">{formatNumber(results.halfLife)}</div>
                        <div className="text-xs text-gray-500">seconds</div>
                    </div>
                </div>
            </div>

            {/* Temperature Effect Analysis */}
            {tempEffect && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Temperature Effect Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-sm font-medium text-gray-700">{tempEffect.temp1.toFixed(1)}°C</div>
                            <div className="text-lg text-blue-700">{formatNumber(tempEffect.rate1)}</div>
                            <div className="text-xs text-gray-500">Rate</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-sm font-medium text-gray-700">{(tempEffect.temp1 + 10).toFixed(1)}°C</div>
                            <div className="text-lg text-blue-700">{formatNumber(tempEffect.baseRate)}</div>
                            <div className="text-xs text-gray-500">Rate</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-sm font-medium text-gray-700">{tempEffect.temp2.toFixed(1)}°C</div>
                            <div className="text-lg text-blue-700">{formatNumber(tempEffect.rate2)}</div>
                            <div className="text-xs text-gray-500">Rate</div>
                        </div>
                    </div>
                    <p className="text-sm text-blue-700 mt-3">
                        <strong>Observation:</strong> Reaction rate increases with temperature following the Arrhenius equation.
                    </p>
                </div>
            )}

            {/* Catalyst Effect Analysis */}
            {catalystEffect && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Catalyst Effect Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <div className="text-sm font-medium text-gray-700 mb-2">Catalyst: {catalystEffect.catalystName}</div>
                            <div className="text-sm text-gray-600">
                                <div><strong>Activation Energy Reduction:</strong> {catalystEffect.activationEnergyReduction.toFixed(1)}%</div>
                                <div><strong>Rate Increase:</strong> {catalystEffect.rateIncrease.toFixed(1)}%</div>
                            </div>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <div className="text-sm font-medium text-gray-700 mb-2">Examples:</div>
                            <div className="text-sm text-gray-600">
                                {catalystEffect.examples.map((example, index) => (
                                    <div key={index}>• {example}</div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Concentration vs Time Graph */}
            {showGraph && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Concentration vs Time:</h4>
                    <div className="h-64 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 200">
                            {/* Graph axes */}
                            <line x1="20" y1="20" x2="20" y2="180" stroke="black" strokeWidth="2" />
                            <line x1="20" y1="180" x2="380" y2="180" stroke="black" strokeWidth="2" />
                            
                            {/* Y-axis label */}
                            <text x="10" y="100" transform="rotate(-90 10 100)" className="text-xs">Concentration (M)</text>
                            
                            {/* X-axis label */}
                            <text x="200" y="195" className="text-xs">Time (s)</text>
                            
                            {/* Plot points and line */}
                            {results.concentrationOverTime.timePoints.map((t, i) => {
                                const x = 20 + (t / Math.max(...results.concentrationOverTime.timePoints)) * 360;
                                const y = 180 - (results.concentrationOverTime.concentrationPoints[i] / concentration) * 160;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="red" />;
                                
                                const prevT = results.concentrationOverTime.timePoints[i - 1];
                                const prevConc = results.concentrationOverTime.concentrationPoints[i - 1];
                                const prevX = 20 + (prevT / Math.max(...results.concentrationOverTime.timePoints)) * 360;
                                const prevY = 180 - (prevConc / concentration) * 160;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="red" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="red" />
                                    </g>
                                );
                            })}
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Arrhenius Equation:</strong> k = A × e^(-Ea/RT)</div>
                        <div><strong>Where:</strong></div>
                        <div>• A (Pre-exponential factor) = {formatNumber(1e13)} s⁻¹</div>
                        <div>• Ea (Activation energy) = {catalyst ? '35,000' : '50,000'} J/mol</div>
                        <div>• R (Gas constant) = 8.314 J/(mol·K)</div>
                        <div>• T (Temperature) = {temperature} K</div>
                        <div><strong>Rate Law:</strong> {reactionTypes[reactionType].rateLaw}</div>
                        <div><strong>Half-life Formula:</strong> {reactionType === 'first_order' ? 't₁/₂ = ln(2)/k' : reactionType === 'second_order' ? 't₁/₂ = 1/(k[A]₀)' : 't₁/₂ = [A]₀/(2k)'}</div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Temperature increases reaction rate exponentially (Arrhenius equation)</li>
                    <li>• Catalysts lower activation energy without being consumed</li>
                    <li>• Zero-order reactions have constant rate regardless of concentration</li>
                    <li>• First-order reactions show exponential decay</li>
                    <li>• Second-order reactions show hyperbolic decay</li>
                </ul>
            </div>
        </div>
    );
};

export default ReactionRateSimulator;
