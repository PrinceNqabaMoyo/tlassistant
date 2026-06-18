import React, { useState, useEffect } from 'react';

const EnergyCalculator = ({ initialData, onChange, isSubmitted }) => {
    const [energyType, setEnergyType] = useState(initialData.energyType || 'kinetic');
    const [mass, setMass] = useState(initialData.mass || 1);
    const [velocity, setVelocity] = useState(initialData.velocity || 10);
    const [height, setHeight] = useState(initialData.height || 5);
    const [springConstant, setSpringConstant] = useState(initialData.springConstant || 100);
    const [displacement, setDisplacement] = useState(initialData.displacement || 0.1);
    const [gravity, setGravity] = useState(initialData.gravity || 9.81);
    const [showEnergyGraph, setShowEnergyGraph] = useState(false);
    const [showConservation, setShowConservation] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);

    useEffect(() => {
        const formattedData = {
            type: "energy_calculator",
            energyType: energyType,
            mass: mass,
            velocity: velocity,
            height: height,
            springConstant: springConstant,
            displacement: displacement,
            gravity: gravity,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [energyType, mass, velocity, height, springConstant, displacement, gravity, onChange]);

    const calculateResults = () => {
        const results = {};
        
        if (energyType === 'kinetic') {
            results.kineticEnergy = calculateKineticEnergy();
            results.momentum = calculateMomentum();
            results.velocityFromEnergy = calculateVelocityFromEnergy();
        } else if (energyType === 'potential') {
            results.gravitationalPotential = calculateGravitationalPotential();
            results.springPotential = calculateSpringPotential();
            results.totalPotential = results.gravitationalPotential + results.springPotential;
        } else if (energyType === 'conservation') {
            results.initialEnergy = calculateInitialEnergy();
            results.finalEnergy = calculateFinalEnergy();
            results.energyConserved = Math.abs(results.initialEnergy - results.finalEnergy) < 0.01;
            results.energyChange = results.finalEnergy - results.initialEnergy;
        }
        
        return results;
    };

    const calculateKineticEnergy = () => {
        return 0.5 * mass * velocity * velocity;
    };

    const calculateMomentum = () => {
        return mass * velocity;
    };

    const calculateVelocityFromEnergy = () => {
        const kineticEnergy = calculateKineticEnergy();
        return Math.sqrt((2 * kineticEnergy) / mass);
    };

    const calculateGravitationalPotential = () => {
        return mass * gravity * height;
    };

    const calculateSpringPotential = () => {
        return 0.5 * springConstant * displacement * displacement;
    };

    const calculateInitialEnergy = () => {
        const kineticInitial = 0.5 * mass * velocity * velocity;
        const potentialInitial = mass * gravity * height;
        return kineticInitial + potentialInitial;
    };

    const calculateFinalEnergy = () => {
        // For conservation example: object falls from height to ground
        const finalHeight = 0;
        const finalVelocity = Math.sqrt(2 * gravity * height); // From energy conservation
        const kineticFinal = 0.5 * mass * finalVelocity * finalVelocity;
        const potentialFinal = mass * gravity * finalHeight;
        return kineticFinal + potentialFinal;
    };

    const generateEnergyData = () => {
        const data = [];
        const maxHeight = Math.max(height, 10);
        const step = maxHeight / 50;
        
        for (let h = 0; h <= maxHeight; h += step) {
            const potential = mass * gravity * h;
            const velocityAtHeight = Math.sqrt(2 * gravity * (maxHeight - h));
            const kinetic = 0.5 * mass * velocityAtHeight * velocityAtHeight;
            const total = potential + kinetic;
            
            data.push({ height: h, potential, kinetic, total });
        }
        
        return data;
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
                <h3 className="text-lg font-semibold text-gray-800">Energy Calculator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowEnergyGraph(!showEnergyGraph)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showEnergyGraph 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showEnergyGraph ? 'Hide Energy Graph' : 'Show Energy Graph'}
                    </button>
                    <button
                        onClick={() => setShowConservation(!showConservation)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showConservation 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showConservation ? 'Hide Conservation' : 'Show Conservation'}
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

            {/* Energy Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Energy Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={energyType} 
                    onChange={(e) => !isSubmitted && setEnergyType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="kinetic">Kinetic Energy</option>
                    <option value="potential">Potential Energy</option>
                    <option value="conservation">Energy Conservation</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {energyType === 'kinetic' 
                        ? 'Calculate kinetic energy and related quantities'
                        : energyType === 'potential'
                        ? 'Calculate gravitational and spring potential energy'
                        : 'Analyze energy conservation in a system'
                    }
                </p>
            </div>

            {/* Input Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Basic Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Mass (kg):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={mass} 
                                onChange={(e) => !isSubmitted && setMass(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Velocity (m/s):</label>
                            <input 
                                type="number" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={velocity} 
                                onChange={(e) => !isSubmitted && setVelocity(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Height (m):</label>
                            <input 
                                type="number" 
                                min="0" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={height} 
                                onChange={(e) => !isSubmitted && setHeight(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Advanced Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Spring Constant (N/m):</label>
                            <input 
                                type="number" 
                                min="1" 
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={springConstant} 
                                onChange={(e) => !isSubmitted && setSpringConstant(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Displacement (m):</label>
                            <input 
                                type="number" 
                                step="0.01"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={displacement} 
                                onChange={(e) => !isSubmitted && setDisplacement(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Gravity (m/s²):</label>
                            <input 
                                type="number" 
                                min="1" 
                                max="50"
                                step="0.01"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={gravity} 
                                onChange={(e) => !isSubmitted && setGravity(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Energy Results:</h4>
                {energyType === 'kinetic' && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Kinetic Energy</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.kineticEnergy)} J</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Momentum</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.momentum)} kg·m/s</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Velocity from Energy</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.velocityFromEnergy)} m/s</div>
                        </div>
                    </div>
                )}
                
                {energyType === 'potential' && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Gravitational PE</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.gravitationalPotential)} J</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Spring PE</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.springPotential)} J</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total PE</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.totalPotential)} J</div>
                        </div>
                    </div>
                )}
                
                {energyType === 'conservation' && (
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Initial Energy</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.initialEnergy)} J</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Final Energy</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.finalEnergy)} J</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Energy Change</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.energyChange)} J</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Conserved?</div>
                            <div className={`text-lg font-semibold ${
                                results.energyConserved ? 'text-green-600' : 'text-red-600'
                            }`}>
                                {results.energyConserved ? '✓ Yes' : '✗ No'}
                            </div>
                        </div>
                    </div>
                )}
            </div>

            {/* Energy Conservation Analysis */}
            {showConservation && energyType === 'conservation' && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Energy Conservation Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Initial State:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Height:</strong> {formatNumber(height)} m</div>
                                <div><strong>Velocity:</strong> {formatNumber(velocity)} m/s</div>
                                <div><strong>Kinetic Energy:</strong> {formatNumber(0.5 * mass * velocity * velocity)} J</div>
                                <div><strong>Potential Energy:</strong> {formatNumber(mass * gravity * height)} J</div>
                                <div><strong>Total Energy:</strong> {formatNumber(results.initialEnergy)} J</div>
                            </div>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Final State:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Height:</strong> 0 m (ground level)</div>
                                <div><strong>Velocity:</strong> {formatNumber(Math.sqrt(2 * gravity * height))} m/s</div>
                                <div><strong>Kinetic Energy:</strong> {formatNumber(0.5 * mass * Math.sqrt(2 * gravity * height) * Math.sqrt(2 * gravity * height))} J</div>
                                <div><strong>Potential Energy:</strong> 0 J</div>
                                <div><strong>Total Energy:</strong> {formatNumber(results.finalEnergy)} J</div>
                            </div>
                        </div>
                    </div>
                    <div className="mt-3 p-3 bg-white rounded border">
                        <h5 className="font-medium text-gray-800 mb-2">Conservation Check:</h5>
                        <div className="text-sm text-gray-600">
                            <div><strong>Initial Energy:</strong> {formatNumber(results.initialEnergy)} J</div>
                            <div><strong>Final Energy:</strong> {formatNumber(results.finalEnergy)} J</div>
                            <div><strong>Difference:</strong> {formatNumber(results.energyChange)} J</div>
                            <div><strong>Conservation Status:</strong> 
                                <span className={`ml-2 font-semibold ${
                                    results.energyConserved ? 'text-green-600' : 'text-red-600'
                                }`}>
                                    {results.energyConserved ? 'Energy is conserved' : 'Energy is not conserved'}
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Energy Graph */}
            {showEnergyGraph && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Energy vs Height Graph:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Graph axes */}
                            <line x1="20" y1="20" x2="20" y2="280" stroke="black" strokeWidth="2" />
                            <line x1="20" y1="280" x2="380" y2="280" stroke="black" strokeWidth="2" />
                            
                            {/* Labels */}
                            <text x="10" y="150" transform="rotate(-90 10 150)" className="text-xs">Energy (J)</text>
                            <text x="200" y="295" className="text-xs">Height (m)</text>
                            
                            {/* Plot energy data */}
                            {generateEnergyData().map((point, i) => {
                                const x = 20 + (point.height / Math.max(...generateEnergyData().map(p => p.height))) * 360;
                                const maxEnergy = Math.max(...generateEnergyData().map(p => p.total));
                                const y = 280 - (point.total / maxEnergy) * 260;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="purple" />;
                                
                                const prevPoint = generateEnergyData()[i - 1];
                                const prevX = 20 + (prevPoint.height / Math.max(...generateEnergyData().map(p => p.height))) * 360;
                                const prevY = 280 - (prevPoint.total / maxEnergy) * 260;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="purple" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="purple" />
                                    </g>
                                );
                            })}
                            
                            {/* Plot potential energy */}
                            {generateEnergyData().map((point, i) => {
                                const x = 20 + (point.height / Math.max(...generateEnergyData().map(p => p.height))) * 360;
                                const maxEnergy = Math.max(...generateEnergyData().map(p => p.total));
                                const y = 280 - (point.potential / maxEnergy) * 260;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="blue" />;
                                
                                const prevPoint = generateEnergyData()[i - 1];
                                const prevX = 20 + (prevPoint.height / Math.max(...generateEnergyData().map(p => p.height))) * 360;
                                const prevY = 280 - (prevPoint.potential / maxEnergy) * 260;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="blue" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="blue" />
                                    </g>
                                );
                            })}
                            
                            {/* Plot kinetic energy */}
                            {generateEnergyData().map((point, i) => {
                                const x = 20 + (point.height / Math.max(...generateEnergyData().map(p => p.height))) * 360;
                                const maxEnergy = Math.max(...generateEnergyData().map(p => p.total));
                                const y = 280 - (point.kinetic / maxEnergy) * 260;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="red" />;
                                
                                const prevPoint = generateEnergyData()[i - 1];
                                const prevX = 20 + (prevPoint.height / Math.max(...generateEnergyData().map(p => p.height))) * 360;
                                const prevY = 280 - (prevPoint.kinetic / maxEnergy) * 260;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="red" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="red" />
                                    </g>
                                );
                            })}
                            
                            {/* Legend */}
                            <text x="300" y="30" className="text-xs font-bold">Legend</text>
                            <line x1="300" y1="35" x2="320" y2="35" stroke="purple" strokeWidth="2" />
                            <text x="325" y="38" className="text-xs">Total Energy</text>
                            <line x1="300" y1="45" x2="320" y2="45" stroke="blue" strokeWidth="2" />
                            <text x="325" y="48" className="text-xs">Potential Energy</text>
                            <line x1="300" y1="55" x2="320" y2="55" stroke="red" strokeWidth="2" />
                            <text x="325" y="58" className="text-xs">Kinetic Energy</text>
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        {energyType === 'kinetic' && (
                            <>
                                <div><strong>Kinetic Energy:</strong> KE = ½mv²</div>
                                <div>• Where: m = {formatNumber(mass)} kg, v = {formatNumber(velocity)} m/s</div>
                                <div>• KE = ½ × {formatNumber(mass)} × {formatNumber(velocity)}² = {formatNumber(results.kineticEnergy)} J</div>
                                <div><strong>Momentum:</strong> p = mv</div>
                                <div>• p = {formatNumber(mass)} × {formatNumber(velocity)} = {formatNumber(results.momentum)} kg·m/s</div>
                                <div><strong>Velocity from Energy:</strong> v = √(2KE/m)</div>
                                <div>• v = √(2 × {formatNumber(results.kineticEnergy)} / {formatNumber(mass)}) = {formatNumber(results.velocityFromEnergy)} m/s</div>
                            </>
                        )}
                        
                        {energyType === 'potential' && (
                            <>
                                <div><strong>Gravitational Potential Energy:</strong> PEg = mgh</div>
                                <div>• Where: m = {formatNumber(mass)} kg, g = {formatNumber(gravity)} m/s², h = {formatNumber(height)} m</div>
                                <div>• PEg = {formatNumber(mass)} × {formatNumber(gravity)} × {formatNumber(height)} = {formatNumber(results.gravitationalPotential)} J</div>
                                <div><strong>Spring Potential Energy:</strong> PEs = ½kx²</div>
                                <div>• Where: k = {formatNumber(springConstant)} N/m, x = {formatNumber(displacement)} m</div>
                                <div>• PEs = ½ × {formatNumber(springConstant)} × {formatNumber(displacement)}² = {formatNumber(results.springPotential)} J</div>
                                <div><strong>Total Potential Energy:</strong> PEtotal = PEg + PEs</div>
                                <div>• PEtotal = {formatNumber(results.gravitationalPotential)} + {formatNumber(results.springPotential)} = {formatNumber(results.totalPotential)} J</div>
                            </>
                        )}
                        
                        {energyType === 'conservation' && (
                            <>
                                <div><strong>Energy Conservation Principle:</strong> Einitial = Efinal</div>
                                <div><strong>Initial Energy:</strong></div>
                                <div>• Kinetic: KE = ½mv² = ½ × {formatNumber(mass)} × {formatNumber(velocity)}² = {formatNumber(0.5 * mass * velocity * velocity)} J</div>
                                <div>• Potential: PE = mgh = {formatNumber(mass)} × {formatNumber(gravity)} × {formatNumber(height)} = {formatNumber(mass * gravity * height)} J</div>
                                <div>• Total: Einitial = {formatNumber(0.5 * mass * velocity * velocity)} + {formatNumber(mass * gravity * height)} = {formatNumber(results.initialEnergy)} J</div>
                                <div><strong>Final Energy (at ground):</strong></div>
                                <div>• Final velocity: v = √(2gh) = √(2 × {formatNumber(gravity)} × {formatNumber(height)}) = {formatNumber(Math.sqrt(2 * gravity * height))} m/s</div>
                                <div>• Kinetic: KE = ½mv² = ½ × {formatNumber(mass)} × {formatNumber(Math.sqrt(2 * gravity * height))}² = {formatNumber(0.5 * mass * Math.sqrt(2 * gravity * height) * Math.sqrt(2 * gravity * height))} J</div>
                                <div>• Potential: PE = 0 J (at ground level)</div>
                                <div>• Total: Efinal = {formatNumber(0.5 * mass * Math.sqrt(2 * gravity * height) * Math.sqrt(2 * gravity * height))} + 0 = {formatNumber(results.finalEnergy)} J</div>
                            </>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Kinetic energy depends on mass and velocity squared</li>
                    <li>• Gravitational potential energy depends on mass, height, and gravity</li>
                    <li>• Spring potential energy depends on spring constant and displacement squared</li>
                    <li>• In a closed system, total mechanical energy is conserved</li>
                    <li>• Energy can transform between kinetic and potential forms</li>
                </ul>
            </div>
        </div>
    );
};

export default EnergyCalculator;
