import React, { useState, useEffect } from 'react';

const NuclearDecaySimulator = ({ initialData, onChange, isSubmitted }) => {
    const [decayType, setDecayType] = useState(initialData.decayType || 'alpha');
    const [initialAmount, setInitialAmount] = useState(initialData.initialAmount || 1000);
    const [halfLife, setHalfLife] = useState(initialData.halfLife || 5730);
    const [timeElapsed, setTimeElapsed] = useState(initialData.timeElapsed || 1000);
    const [decayConstant, setDecayConstant] = useState(initialData.decayConstant || 0.000121);
    const [showDecayCurve, setShowDecayCurve] = useState(false);
    const [showDecayChain, setShowDecayChain] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [showRadiationTypes, setShowRadiationTypes] = useState(false);

    useEffect(() => {
        const formattedData = {
            type: "nuclear_decay_simulator",
            decayType: decayType,
            initialAmount: initialAmount,
            halfLife: halfLife,
            timeElapsed: timeElapsed,
            decayConstant: decayConstant,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [decayType, initialAmount, halfLife, timeElapsed, decayConstant, onChange]);

    const calculateResults = () => {
        const results = {};
        
        // Calculate decay constant from half-life
        results.calculatedDecayConstant = Math.log(2) / halfLife;
        
        // Calculate remaining amount
        results.remainingAmount = initialAmount * Math.exp(-results.calculatedDecayConstant * timeElapsed);
        
        // Calculate decayed amount
        results.decayedAmount = initialAmount - results.remainingAmount;
        
        // Calculate number of half-lives
        results.halfLives = timeElapsed / halfLife;
        
        // Calculate activity (decay rate)
        results.activity = results.calculatedDecayConstant * results.remainingAmount;
        
        // Calculate mean lifetime
        results.meanLifetime = 1 / results.calculatedDecayConstant;
        
        // Calculate specific activity
        results.specificActivity = results.activity / initialAmount;
        
        return results;
    };

    const generateDecayData = () => {
        const data = [];
        const timeStep = halfLife / 20;
        
        for (let t = 0; t <= halfLife * 4; t += timeStep) {
            const remaining = initialAmount * Math.exp(-results.calculatedDecayConstant * t);
            const decayed = initialAmount - remaining;
            data.push({ time: t, remaining, decayed });
        }
        
        return data;
    };

    const generateDecayChain = () => {
        const chain = [];
        let currentAmount = initialAmount;
        let currentTime = 0;
        const steps = 10;
        
        for (let i = 0; i < steps; i++) {
            const remaining = currentAmount * Math.exp(-results.calculatedDecayConstant * (timeElapsed / steps));
            const decayed = currentAmount - remaining;
            
            chain.push({
                step: i + 1,
                time: currentTime,
                amount: currentAmount,
                remaining: remaining,
                decayed: decayed
            });
            
            currentAmount = remaining;
            currentTime += timeElapsed / steps;
        }
        
        return chain;
    };

    const getRadiationInfo = () => {
        const radiationTypes = {
            alpha: {
                name: 'Alpha Decay',
                symbol: 'α',
                description: 'Emission of helium nucleus (2 protons + 2 neutrons)',
                penetratingPower: 'Low (stopped by paper)',
                ionizingPower: 'High',
                examples: ['Uranium-238 → Thorium-234', 'Radium-226 → Radon-222'],
                equation: 'A → A-4 + 4He',
                energy: '4-9 MeV'
            },
            beta: {
                name: 'Beta Decay',
                symbol: 'β⁻',
                description: 'Emission of electron and antineutrino',
                penetratingPower: 'Medium (stopped by aluminum)',
                ionizingPower: 'Medium',
                examples: ['Carbon-14 → Nitrogen-14', 'Tritium → Helium-3'],
                equation: 'n → p + e⁻ + ν̄',
                energy: '0.5-3 MeV'
            },
            gamma: {
                name: 'Gamma Decay',
                symbol: 'γ',
                description: 'Emission of high-energy electromagnetic radiation',
                penetratingPower: 'High (stopped by lead)',
                ionizingPower: 'Low',
                examples: ['Excited nucleus → Ground state', 'Cobalt-60 → Nickel-60'],
                equation: 'A* → A + γ',
                energy: '0.1-10 MeV'
            },
            positron: {
                name: 'Positron Emission',
                symbol: 'β⁺',
                description: 'Emission of positron and neutrino',
                penetratingPower: 'Medium (stopped by aluminum)',
                ionizingPower: 'Medium',
                examples: ['Carbon-11 → Boron-11', 'Fluorine-18 → Oxygen-18'],
                equation: 'p → n + e⁺ + ν',
                energy: '0.5-3 MeV'
            }
        };
        
        return radiationTypes[decayType] || radiationTypes.alpha;
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        if (Math.abs(num) < 0.001) return '0';
        return Math.abs(num) < 0.01 ? num.toExponential(3) : num.toFixed(3);
    };

    const results = calculateResults();
    const radiationInfo = getRadiationInfo();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Nuclear Decay Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowDecayCurve(!showDecayCurve)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showDecayCurve 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showDecayCurve ? 'Hide Decay Curve' : 'Show Decay Curve'}
                    </button>
                    <button
                        onClick={() => setShowDecayChain(!showDecayChain)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showDecayChain 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showDecayChain ? 'Hide Decay Chain' : 'Show Decay Chain'}
                    </button>
                    <button
                        onClick={() => setShowRadiationTypes(!showRadiationTypes)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showRadiationTypes 
                                ? 'bg-purple-100 text-purple-700 hover:bg-purple-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showRadiationTypes ? 'Hide Radiation' : 'Show Radiation'}
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

            {/* Decay Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Decay Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={decayType} 
                    onChange={(e) => !isSubmitted && setDecayType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="alpha">Alpha Decay (α)</option>
                    <option value="beta">Beta Decay (β⁻)</option>
                    <option value="gamma">Gamma Decay (γ)</option>
                    <option value="positron">Positron Emission (β⁺)</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {radiationInfo.description}
                </p>
            </div>

            {/* Input Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Decay Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Initial Amount (atoms):</label>
                            <input 
                                type="number" 
                                min="1" 
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={initialAmount} 
                                onChange={(e) => !isSubmitted && setInitialAmount(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Half-Life (years):</label>
                            <input 
                                type="number" 
                                min="0.001" 
                                step="0.001"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={halfLife} 
                                onChange={(e) => !isSubmitted && setHalfLife(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Time Elapsed (years):</label>
                            <input 
                                type="number" 
                                min="0" 
                                step="0.001"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={timeElapsed} 
                                onChange={(e) => !isSubmitted && setTimeElapsed(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Advanced Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Decay Constant (1/years):</label>
                            <input 
                                type="number" 
                                min="0.000001" 
                                step="0.000001"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={decayConstant} 
                                onChange={(e) => !isSubmitted && setDecayConstant(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div className="pt-4">
                            <div className="text-sm text-gray-600">
                                <div><strong>Calculated Decay Constant:</strong></div>
                                <div>λ = ln(2)/T₁/₂ = {formatNumber(Math.log(2))}/{formatNumber(halfLife)}</div>
                                <div>= {formatNumber(results.calculatedDecayConstant)} 1/years</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Decay Results:</h4>
                <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Remaining</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.remainingAmount)}</div>
                        <div className="text-sm text-gray-600">atoms</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Decayed</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.decayedAmount)}</div>
                        <div className="text-sm text-gray-600">atoms</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Half-Lives</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.halfLives)}</div>
                        <div className="text-sm text-gray-600">periods</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Activity</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.activity)}</div>
                        <div className="text-sm text-gray-600">decays/year</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Mean Lifetime</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.meanLifetime)}</div>
                        <div className="text-sm text-gray-600">years</div>
                    </div>
                </div>
            </div>

            {/* Decay Curve */}
            {showDecayCurve && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Decay Curve:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Graph axes */}
                            <line x1="50" y1="250" x2="350" y2="250" stroke="black" strokeWidth="1" />
                            <line x1="50" y1="50" x2="50" y2="250" stroke="black" strokeWidth="1" />
                            
                            {/* Labels */}
                            <text x="200" y="270" className="text-xs">Time (years)</text>
                            <text x="30" y="150" transform="rotate(-90 30 150)" className="text-xs">Amount (atoms)</text>
                            
                            {/* Plot decay curve */}
                            {generateDecayData().map((point, i) => {
                                const x = 50 + (point.time / (halfLife * 4)) * 300;
                                const y = 250 - (point.remaining / initialAmount) * 200;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="blue" />;
                                
                                const prevPoint = generateDecayData()[i - 1];
                                const prevX = 50 + (prevPoint.time / (halfLife * 4)) * 300;
                                const prevY = 250 - (prevPoint.remaining / initialAmount) * 200;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="blue" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="blue" />
                                    </g>
                                );
                            })}
                            
                            {/* Half-life markers */}
                            {[1, 2, 3, 4].map((n) => {
                                const x = 50 + (n * halfLife / (halfLife * 4)) * 300;
                                const y = 250 - Math.pow(0.5, n) * 200;
                                
                                return (
                                    <g key={n}>
                                        <line x1={x} y1={y} x2={x} y2="250" stroke="red" strokeWidth="1" strokeDasharray="5,5" />
                                        <text x={x - 10} y="260" className="text-xs text-red-600">{n}T₁/₂</text>
                                    </g>
                                );
                            })}
                            
                            {/* Current time marker */}
                            <line x1={50 + (timeElapsed / (halfLife * 4)) * 300} y1="50" x2={50 + (timeElapsed / (halfLife * 4)) * 300} y2="250" stroke="green" strokeWidth="2" strokeDasharray="5,5" />
                            <text x={55 + (timeElapsed / (halfLife * 4)) * 300} y="60" className="text-xs text-green-600">t = {formatNumber(timeElapsed)} years</text>
                        </svg>
                    </div>
                </div>
            )}

            {/* Decay Chain */}
            {showDecayChain && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Decay Chain Analysis:</h4>
                    <div className="overflow-x-auto">
                        <table className="w-full bg-white rounded border">
                            <thead>
                                <tr className="bg-green-100">
                                    <th className="p-3 text-left border-b">Step</th>
                                    <th className="p-3 text-left border-b">Time (years)</th>
                                    <th className="p-3 text-left border-b">Initial Amount</th>
                                    <th className="p-3 text-left border-b">Remaining</th>
                                    <th className="p-3 text-left border-b">Decayed</th>
                                    <th className="p-3 text-left border-b">Decay %</th>
                                </tr>
                            </thead>
                            <tbody>
                                {generateDecayChain().map((step) => (
                                    <tr key={step.step} className="border-b">
                                        <td className="p-3">{step.step}</td>
                                        <td className="p-3">{formatNumber(step.time)}</td>
                                        <td className="p-3">{formatNumber(step.amount)}</td>
                                        <td className="p-3">{formatNumber(step.remaining)}</td>
                                        <td className="p-3">{formatNumber(step.decayed)}</td>
                                        <td className="p-3">{formatNumber((step.decayed / step.amount) * 100)}%</td>
                                    </tr>
                                ))}
                            </tbody>
                        </table>
                    </div>
                </div>
            )}

            {/* Radiation Types */}
            {showRadiationTypes && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Radiation Information:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div className="p-4 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-3">{radiationInfo.name} ({radiationInfo.symbol})</h5>
                            <div className="space-y-2 text-sm text-gray-600">
                                <div><strong>Description:</strong> {radiationInfo.description}</div>
                                <div><strong>Penetrating Power:</strong> {radiationInfo.penetratingPower}</div>
                                <div><strong>Ionizing Power:</strong> {radiationInfo.ionizingPower}</div>
                                <div><strong>Energy Range:</strong> {radiationInfo.energy}</div>
                                <div><strong>Equation:</strong> {radiationInfo.equation}</div>
                            </div>
                        </div>
                        <div className="p-4 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-3">Examples:</h5>
                            <div className="space-y-2 text-sm text-gray-600">
                                {radiationInfo.examples.map((example, index) => (
                                    <div key={index}>• {example}</div>
                                ))}
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
                        <div><strong>Exponential Decay Law:</strong> N(t) = N₀ × e^(-λt)</div>
                        <div>• Initial Amount: N₀ = {formatNumber(initialAmount)} atoms</div>
                        <div>• Decay Constant: λ = ln(2)/T₁/₂ = {formatNumber(Math.log(2))}/{formatNumber(halfLife)} = {formatNumber(results.calculatedDecayConstant)} 1/years</div>
                        <div>• Time Elapsed: t = {formatNumber(timeElapsed)} years</div>
                        <div>• Remaining Amount: N(t) = {formatNumber(initialAmount)} × e^(-{formatNumber(results.calculatedDecayConstant)} × {formatNumber(timeElapsed)})</div>
                        <div>• N(t) = {formatNumber(initialAmount)} × e^(-{formatNumber(results.calculatedDecayConstant * timeElapsed)})</div>
                        <div>• N(t) = {formatNumber(initialAmount)} × {formatNumber(Math.exp(-results.calculatedDecayConstant * timeElapsed))} = {formatNumber(results.remainingAmount)} atoms</div>
                        
                        <div><strong>Half-Life Relationship:</strong></div>
                        <div>• Number of Half-Lives: n = t/T₁/₂ = {formatNumber(timeElapsed)}/{formatNumber(halfLife)} = {formatNumber(results.halfLives)}</div>
                        <div>• Remaining Fraction: (1/2)^n = (1/2)^{formatNumber(results.halfLives)} = {formatNumber(Math.pow(0.5, results.halfLives))}</div>
                        <div>• Verification: N₀ × (1/2)^n = {formatNumber(initialAmount)} × {formatNumber(Math.pow(0.5, results.halfLives))} = {formatNumber(initialAmount * Math.pow(0.5, results.halfLives))} atoms</div>
                        
                        <div><strong>Activity Calculations:</strong></div>
                        <div>• Activity: A(t) = λ × N(t) = {formatNumber(results.calculatedDecayConstant)} × {formatNumber(results.remainingAmount)} = {formatNumber(results.activity)} decays/year</div>
                        <div>• Mean Lifetime: τ = 1/λ = 1/{formatNumber(results.calculatedDecayConstant)} = {formatNumber(results.meanLifetime)} years</div>
                        <div>• Specific Activity: Aₛ = A(t)/N₀ = {formatNumber(results.activity)}/{formatNumber(initialAmount)} = {formatNumber(results.specificActivity)} decays/(atom×year)</div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Exponential decay: N(t) = N₀ × e^(-λt)</li>
                    <li>• Half-life: T₁/₂ = ln(2)/λ = 0.693/λ</li>
                    <li>• Decay constant: λ = ln(2)/T₁/₂</li>
                    <li>• Activity: A(t) = λ × N(t) (decay rate)</li>
                    <li>• Mean lifetime: τ = 1/λ</li>
                    <li>• After n half-lives: N = N₀ × (1/2)^n</li>
                    <li>• Alpha particles are helium nuclei (2p + 2n)</li>
                    <li>• Beta particles are electrons or positrons</li>
                    <li>• Gamma rays are high-energy photons</li>
                </ul>
            </div>
        </div>
    );
};

export default NuclearDecaySimulator;
