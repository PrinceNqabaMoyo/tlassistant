import React, { useState, useEffect } from 'react';

const ElectricCircuitBuilder = ({ initialData, onChange, isSubmitted }) => {
    const [circuitType, setCircuitType] = useState(initialData.circuitType || 'simple');
    const [voltage, setVoltage] = useState(initialData.voltage || 12);
    const [current, setCurrent] = useState(initialData.current || 2);
    const [resistance, setResistance] = useState(initialData.resistance || 6);
    const [power, setPower] = useState(initialData.power || 24);
    const [showSeries, setShowSeries] = useState(false);
    const [showParallel, setShowParallel] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [resistors, setResistors] = useState(initialData.resistors || [
        { id: 1, value: 6, label: 'R₁' },
        { id: 2, value: 4, label: 'R₂' }
    ]);

    useEffect(() => {
        const formattedData = {
            type: "electric_circuit_builder",
            circuitType: circuitType,
            voltage: voltage,
            current: current,
            resistance: resistance,
            power: power,
            resistors: resistors,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [circuitType, voltage, current, resistance, power, resistors, onChange]);

    const calculateResults = () => {
        const results = {};
        
        if (circuitType === 'simple') {
            results.voltageFromOhm = current * resistance;
            results.currentFromOhm = voltage / resistance;
            results.resistanceFromOhm = voltage / current;
            results.powerFromVoltage = voltage * current;
            results.powerFromResistance = current * current * resistance;
        } else if (circuitType === 'series') {
            results.totalResistance = calculateSeriesResistance();
            results.totalCurrent = voltage / results.totalResistance;
            results.voltageDrops = calculateVoltageDrops(results.totalCurrent);
            results.powerDissipated = calculatePowerDissipated(results.totalCurrent);
        } else if (circuitType === 'parallel') {
            results.totalResistance = calculateParallelResistance();
            results.totalCurrent = voltage / results.totalResistance;
            results.currentBranches = calculateCurrentBranches(results.totalCurrent);
            results.powerDissipated = calculatePowerDissipated(results.totalCurrent);
        }
        
        return results;
    };

    const calculateSeriesResistance = () => {
        return resistors.reduce((total, resistor) => total + resistor.value, 0);
    };

    const calculateParallelResistance = () => {
        const reciprocalSum = resistors.reduce((total, resistor) => total + (1 / resistor.value), 0);
        return 1 / reciprocalSum;
    };

    const calculateVoltageDrops = (totalCurrent) => {
        return resistors.map(resistor => ({
            id: resistor.id,
            label: resistor.label,
            voltage: totalCurrent * resistor.value,
            current: totalCurrent,
            power: totalCurrent * totalCurrent * resistor.value
        }));
    };

    const calculateCurrentBranches = (totalCurrent) => {
        const totalResistance = calculateParallelResistance();
        return resistors.map(resistor => ({
            id: resistor.id,
            label: resistor.label,
            current: (voltage / resistor.value),
            voltage: voltage,
            power: (voltage * voltage) / resistor.value
        }));
    };

    const calculatePowerDissipated = (totalCurrent) => {
        if (circuitType === 'series') {
            return totalCurrent * totalCurrent * calculateSeriesResistance();
        } else {
            return (voltage * voltage) / calculateParallelResistance();
        }
    };

    const addResistor = () => {
        const newId = Math.max(...resistors.map(r => r.id)) + 1;
        const newResistor = {
            id: newId,
            value: 10,
            label: `R${newId}`
        };
        setResistors([...resistors, newResistor]);
    };

    const removeResistor = (id) => {
        if (resistors.length > 1) {
            setResistors(resistors.filter(r => r.id !== id));
        }
    };

    const updateResistor = (id, field, value) => {
        setResistors(resistors.map(r => 
            r.id === id ? { ...r, [field]: value } : r
        ));
    };

    const formatNumber = (num) => {
        if (num === 0) return '0';
        if (!num || isNaN(num)) return '';
        if (Math.abs(num) < 0.001) return '0';
        return Math.abs(num) < 0.01 ? num.toExponential(3) : num.toFixed(3);
    };

    const results = calculateResults();

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Electric Circuit Builder</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowSeries(!showSeries)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showSeries 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showSeries ? 'Hide Series' : 'Show Series'}
                    </button>
                    <button
                        onClick={() => setShowParallel(!showParallel)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showParallel 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showParallel ? 'Hide Parallel' : 'Show Parallel'}
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

            {/* Circuit Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Circuit Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={circuitType} 
                    onChange={(e) => !isSubmitted && setCircuitType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="simple">Simple Circuit (Ohm's Law)</option>
                    <option value="series">Series Circuit</option>
                    <option value="parallel">Parallel Circuit</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {circuitType === 'simple' 
                        ? 'Basic circuit with single voltage source and resistor'
                        : circuitType === 'series'
                        ? 'Multiple resistors connected in series (same current)'
                        : 'Multiple resistors connected in parallel (same voltage)'
                    }
                </p>
            </div>

            {/* Input Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Circuit Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Voltage (V):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={voltage} 
                                onChange={(e) => !isSubmitted && setVoltage(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Current (A):</label>
                            <input 
                                type="number" 
                                min="0.01" 
                                step="0.01"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={current} 
                                onChange={(e) => !isSubmitted && setCurrent(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Resistance (Ω):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={resistance} 
                                onChange={(e) => !isSubmitted && setResistance(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Power & Calculations:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Power (W):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={power} 
                                onChange={(e) => !isSubmitted && setPower(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div className="pt-4">
                            <button
                                onClick={addResistor}
                                disabled={isSubmitted}
                                className="w-full px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:opacity-50 transition-colors"
                            >
                                Add Resistor
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            {/* Resistor Management */}
            {(circuitType === 'series' || circuitType === 'parallel') && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Resistor Configuration:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {resistors.map((resistor) => (
                            <div key={resistor.id} className="p-3 bg-white rounded border">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="font-medium text-gray-800">{resistor.label}</span>
                                    {resistors.length > 1 && (
                                        <button
                                            onClick={() => removeResistor(resistor.id)}
                                            disabled={isSubmitted}
                                            className="text-red-600 hover:text-red-800 disabled:opacity-50"
                                        >
                                            ×
                                        </button>
                                    )}
                                </div>
                                <input
                                    type="number"
                                    min="0.1"
                                    step="0.1"
                                    className="w-full p-2 border border-gray-300 rounded focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
                                    value={resistor.value}
                                    onChange={(e) => updateResistor(resistor.id, 'value', parseFloat(e.target.value))}
                                    disabled={isSubmitted}
                                    placeholder="Resistance (Ω)"
                                />
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Circuit Results:</h4>
                {circuitType === 'simple' && (
                    <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Voltage (V)</div>
                            <div className="text-xl text-purple-700">{formatNumber(voltage)} V</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Current (A)</div>
                            <div className="text-xl text-purple-700">{formatNumber(current)} A</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Resistance (Ω)</div>
                            <div className="text-xl text-purple-700">{formatNumber(resistance)} Ω</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Power (W)</div>
                            <div className="text-xl text-purple-700">{formatNumber(power)} W</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Power Check</div>
                            <div className="text-xl text-purple-700">{formatNumber(voltage * current)} W</div>
                        </div>
                    </div>
                )}
                
                {(circuitType === 'series' || circuitType === 'parallel') && (
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total Resistance</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.totalResistance)} Ω</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total Current</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.totalCurrent)} A</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total Power</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.powerDissipated)} W</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Circuit Type</div>
                            <div className="text-xl text-purple-700 capitalize">{circuitType}</div>
                        </div>
                    </div>
                )}
            </div>

            {/* Series Circuit Analysis */}
            {showSeries && circuitType === 'series' && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Series Circuit Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Circuit Properties:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Total Resistance:</strong> Rtotal = {resistors.map(r => r.value).join(' + ')} = {formatNumber(results.totalResistance)} Ω</div>
                                <div><strong>Total Current:</strong> Itotal = V/Rtotal = {formatNumber(voltage)}/{formatNumber(results.totalResistance)} = {formatNumber(results.totalCurrent)} A</div>
                                <div><strong>Total Power:</strong> Ptotal = Itotal² × Rtotal = {formatNumber(results.totalCurrent)}² × {formatNumber(results.totalResistance)} = {formatNumber(results.powerDissipated)} W</div>
                            </div>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Individual Resistors:</h5>
                            <div className="space-y-2">
                                {results.voltageDrops?.map((resistor) => (
                                    <div key={resistor.id} className="text-sm text-gray-600">
                                        <div><strong>{resistor.label}:</strong> V = {formatNumber(resistor.voltage)} V, I = {formatNumber(resistor.current)} A, P = {formatNumber(resistor.power)} W</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Parallel Circuit Analysis */}
            {showParallel && circuitType === 'parallel' && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Parallel Circuit Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Circuit Properties:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Total Resistance:</strong> 1/Rtotal = {resistors.map(r => `1/${r.value}`).join(' + ')} = 1/{formatNumber(results.totalResistance)}</div>
                                <div><strong>Total Current:</strong> Itotal = V/Rtotal = {formatNumber(voltage)}/{formatNumber(results.totalResistance)} = {formatNumber(results.totalCurrent)} A</div>
                                <div><strong>Total Power:</strong> Ptotal = V²/Rtotal = {formatNumber(voltage)}²/{formatNumber(results.totalResistance)} = {formatNumber(results.powerDissipated)} W</div>
                            </div>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Individual Resistors:</h5>
                            <div className="space-y-2">
                                {results.currentBranches?.map((resistor) => (
                                    <div key={resistor.id} className="text-sm text-gray-600">
                                        <div><strong>{resistor.label}:</strong> V = {formatNumber(resistor.voltage)} V, I = {formatNumber(resistor.current)} A, P = {formatNumber(resistor.power)} W</div>
                                    </div>
                                ))}
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Circuit Diagram */}
            <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                <h4 className="text-md font-medium text-gray-800 mb-3">Circuit Diagram:</h4>
                <div className="h-80 bg-white rounded border p-4">
                    <svg className="w-full h-full" viewBox="0 0 400 300">
                        {/* Battery */}
                        <rect x="20" y="120" width="40" height="60" fill="none" stroke="black" strokeWidth="2" />
                        <line x1="40" y1="120" x2="40" y2="180" stroke="black" strokeWidth="2" />
                        <line x1="30" y1="130" x2="30" y2="170" stroke="black" strokeWidth="2" />
                        <text x="60" y="155" className="text-sm">{formatNumber(voltage)}V</text>
                        
                        {circuitType === 'simple' && (
                            <>
                                {/* Single Resistor */}
                                <rect x="120" y="130" width="60" height="40" fill="none" stroke="black" strokeWidth="2" />
                                <text x="150" y="155" className="text-sm">{formatNumber(resistance)}Ω</text>
                                
                                {/* Wires */}
                                <line x1="60" y1="150" x2="120" y2="150" stroke="black" strokeWidth="2" />
                                <line x1="180" y1="150" x2="220" y2="150" stroke="black" strokeWidth="2" />
                                <line x1="220" y1="150" x2="220" y2="180" stroke="black" strokeWidth="2" />
                                <line x1="220" y1="180" x2="20" y2="180" stroke="black" strokeWidth="2" />
                                
                                {/* Current arrow */}
                                <path d="M 80 150 L 85 145 L 85 155 Z" fill="black" />
                                <text x="90" y="140" className="text-xs">I = {formatNumber(current)}A</text>
                            </>
                        )}
                        
                        {circuitType === 'series' && (
                            <>
                                {/* Series Resistors */}
                                {resistors.map((resistor, index) => (
                                    <g key={resistor.id}>
                                        <rect x={120 + index * 80} y="130" width="60" height="40" fill="none" stroke="black" strokeWidth="2" />
                                        <text x={150 + index * 80} y="155" className="text-sm">{formatNumber(resistor.value)}Ω</text>
                                        {index < resistors.length - 1 && (
                                            <line x1={180 + index * 80} y1="150" x2={200 + index * 80} y2="150" stroke="black" strokeWidth="2" />
                                        )}
                                    </g>
                                ))}
                                
                                {/* Wires */}
                                <line x1="60" y1="150" x2="120" y2="150" stroke="black" strokeWidth="2" />
                                <line x1={180 + (resistors.length - 1) * 80} y1="150" x2={220 + (resistors.length - 1) * 80} y2="150" stroke="black" strokeWidth="2" />
                                <line x1={220 + (resistors.length - 1) * 80} y1="150" x2={220 + (resistors.length - 1) * 80} y2="180" stroke="black" strokeWidth="2" />
                                <line x1={220 + (resistors.length - 1) * 80} y1="180" x2="20" y2="180" stroke="black" strokeWidth="2" />
                                
                                {/* Current arrow */}
                                <path d="M 80 150 L 85 145 L 85 155 Z" fill="black" />
                                <text x="90" y="140" className="text-xs">I = {formatNumber(results.totalCurrent)}A</text>
                            </>
                        )}
                        
                        {circuitType === 'parallel' && (
                            <>
                                {/* Parallel Resistors */}
                                {resistors.map((resistor, index) => (
                                    <g key={resistor.id}>
                                        <rect x="120" y={80 + index * 60} width="60" height="40" fill="none" stroke="black" strokeWidth="2" />
                                        <text x="150" y={105 + index * 60} className="text-sm">{formatNumber(resistor.value)}Ω</text>
                                    </g>
                                ))}
                                
                                {/* Wires */}
                                <line x1="60" y1="150" x2="120" y2="150" stroke="black" strokeWidth="2" />
                                <line x1="180" y1="150" x2="220" y2="150" stroke="black" strokeWidth="2" />
                                <line x1="220" y1="150" x2="220" y2="180" stroke="black" strokeWidth="2" />
                                <line x1="220" y1="180" x2="20" y2="180" stroke="black" strokeWidth="2" />
                                
                                {/* Parallel connections */}
                                {resistors.map((resistor, index) => (
                                    <g key={resistor.id}>
                                        <line x1="120" y1="150" x2="120" y2={100 + index * 60} stroke="black" strokeWidth="2" />
                                        <line x1="180" y1={100 + index * 60} x2="180" y2="150" stroke="black" strokeWidth="2" />
                                    </g>
                                ))}
                                
                                {/* Current arrows */}
                                <path d="M 80 150 L 85 145 L 85 155 Z" fill="black" />
                                <text x="90" y="140" className="text-xs">I = {formatNumber(results.totalCurrent)}A</text>
                            </>
                        )}
                    </svg>
                </div>
            </div>

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Ohm's Law:</strong> V = IR, I = V/R, R = V/I</div>
                        <div><strong>Power Equations:</strong> P = VI = I²R = V²/R</div>
                        
                        {circuitType === 'simple' && (
                            <>
                                <div><strong>Simple Circuit Calculations:</strong></div>
                                <div>• Voltage: V = {formatNumber(voltage)} V</div>
                                <div>• Current: I = {formatNumber(current)} A</div>
                                <div>• Resistance: R = {formatNumber(resistance)} Ω</div>
                                <div>• Power: P = VI = {formatNumber(voltage)} × {formatNumber(current)} = {formatNumber(voltage * current)} W</div>
                                <div>• Power Check: P = I²R = {formatNumber(current)}² × {formatNumber(resistance)} = {formatNumber(current * current * resistance)} W</div>
                            </>
                        )}
                        
                        {circuitType === 'series' && (
                            <>
                                <div><strong>Series Circuit Calculations:</strong></div>
                                <div>• Total Resistance: Rtotal = {resistors.map(r => r.value).join(' + ')} = {formatNumber(results.totalResistance)} Ω</div>
                                <div>• Total Current: Itotal = V/Rtotal = {formatNumber(voltage)}/{formatNumber(results.totalResistance)} = {formatNumber(results.totalCurrent)} A</div>
                                <div>• Voltage Drops: Each resistor gets V = IR</div>
                                {results.voltageDrops?.map((resistor) => (
                                    <div key={resistor.id}>• {resistor.label}: V = {formatNumber(results.totalCurrent)} × {formatNumber(resistors.find(r => r.id === resistor.id)?.value)} = {formatNumber(resistor.voltage)} V</div>
                                ))}
                            </>
                        )}
                        
                        {circuitType === 'parallel' && (
                            <>
                                <div><strong>Parallel Circuit Calculations:</strong></div>
                                <div>• Total Resistance: 1/Rtotal = {resistors.map(r => `1/${r.value}`).join(' + ')} = 1/{formatNumber(results.totalResistance)}</div>
                                <div>• Total Current: Itotal = V/Rtotal = {formatNumber(voltage)}/{formatNumber(results.totalResistance)} = {formatNumber(results.totalCurrent)} A</div>
                                <div>• Current Branches: Each resistor gets I = V/R</div>
                                {results.currentBranches?.map((resistor) => (
                                    <div key={resistor.id}>• {resistor.label}: I = {formatNumber(voltage)}/{formatNumber(resistors.find(r => r.id === resistor.id)?.value)} = {formatNumber(resistor.current)} A</div>
                                ))}
                            </>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Ohm's Law: V = IR (Voltage = Current × Resistance)</li>
                    <li>• Power: P = VI = I²R = V²/R</li>
                    <li>• Series: Same current, voltages add up, resistances add up</li>
                    <li>• Parallel: Same voltage, currents add up, resistances add reciprocally</li>
                    <li>• Total power equals sum of individual powers</li>
                    <li>• Current flows from positive to negative terminal</li>
                </ul>
            </div>
        </div>
    );
};

export default ElectricCircuitBuilder;
