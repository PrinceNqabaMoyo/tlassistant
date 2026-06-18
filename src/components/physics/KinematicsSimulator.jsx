import React, { useState, useEffect } from 'react';

const KinematicsSimulator = ({ initialData, onChange, isSubmitted }) => {
    const [motionType, setMotionType] = useState(initialData.motionType || 'uniform');
    const [initialPosition, setInitialPosition] = useState(initialData.initialPosition || 0);
    const [initialVelocity, setInitialVelocity] = useState(initialData.initialVelocity || 10);
    const [acceleration, setAcceleration] = useState(initialData.acceleration || 2);
    const [time, setTime] = useState(initialData.time || 5);
    const [angle, setAngle] = useState(initialData.angle || 45);
    const [gravity, setGravity] = useState(initialData.gravity || 9.81);
    const [showMotionGraphs, setShowMotionGraphs] = useState(false);
    const [showProjectilePath, setShowProjectilePath] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);

    useEffect(() => {
        const formattedData = {
            type: "kinematics_simulator",
            motionType: motionType,
            initialPosition: initialPosition,
            initialVelocity: initialVelocity,
            acceleration: acceleration,
            time: time,
            angle: angle,
            gravity: gravity,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [motionType, initialPosition, initialVelocity, acceleration, time, angle, gravity, onChange]);

    const calculateResults = () => {
        const results = {};
        
        if (motionType === 'uniform') {
            results.finalPosition = calculateUniformMotion();
            results.finalVelocity = initialVelocity;
            results.displacement = results.finalPosition - initialPosition;
            results.averageVelocity = results.displacement / time;
        } else if (motionType === 'accelerated') {
            results.finalPosition = calculateAcceleratedMotion();
            results.finalVelocity = calculateFinalVelocity();
            results.displacement = results.finalPosition - initialPosition;
            results.averageVelocity = results.displacement / time;
        } else if (motionType === 'projectile') {
            results.projectileData = calculateProjectileMotion();
        }
        
        return results;
    };

    const calculateUniformMotion = () => {
        return initialPosition + initialVelocity * time;
    };

    const calculateAcceleratedMotion = () => {
        return initialPosition + initialVelocity * time + 0.5 * acceleration * time * time;
    };

    const calculateFinalVelocity = () => {
        return initialVelocity + acceleration * time;
    };

    const calculateProjectileMotion = () => {
        const radianAngle = angle * Math.PI / 180;
        const v0x = initialVelocity * Math.cos(radianAngle);
        const v0y = initialVelocity * Math.sin(radianAngle);
        
        // Time of flight
        const timeOfFlight = (2 * v0y) / gravity;
        
        // Maximum height
        const maxHeight = initialPosition + (v0y * v0y) / (2 * gravity);
        
        // Range
        const range = v0x * timeOfFlight;
        
        // Final velocity components
        const vfx = v0x;
        const vfy = v0y - gravity * timeOfFlight;
        const finalVelocity = Math.sqrt(vfx * vfx + vfy * vfy);
        
        // Position at given time
        const currentTime = Math.min(time, timeOfFlight);
        const x = v0x * currentTime;
        const y = initialPosition + v0y * currentTime - 0.5 * gravity * currentTime * currentTime;
        
        return {
            v0x, v0y, timeOfFlight, maxHeight, range, vfx, vfy, finalVelocity, x, y
        };
    };

    const generateMotionData = () => {
        const data = [];
        const timeStep = time / 100;
        
        for (let t = 0; t <= time; t += timeStep) {
            let position, velocity;
            
            if (motionType === 'uniform') {
                position = initialPosition + initialVelocity * t;
                velocity = initialVelocity;
            } else if (motionType === 'accelerated') {
                position = initialPosition + initialVelocity * t + 0.5 * acceleration * t * t;
                velocity = initialVelocity + acceleration * t;
            }
            
            data.push({ time: t, position, velocity });
        }
        
        return data;
    };

    const generateProjectileData = () => {
        const data = [];
        const timeStep = time / 100;
        const radianAngle = angle * Math.PI / 180;
        const v0x = initialVelocity * Math.cos(radianAngle);
        const v0y = initialVelocity * Math.sin(radianAngle);
        
        for (let t = 0; t <= time; t += timeStep) {
            const x = v0x * t;
            const y = initialPosition + v0y * t - 0.5 * gravity * t * t;
            
            if (y >= 0) { // Only show points above ground
                data.push({ time: t, x, y });
            }
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
                <h3 className="text-lg font-semibold text-gray-800">Kinematics Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowMotionGraphs(!showMotionGraphs)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showMotionGraphs 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showMotionGraphs ? 'Hide Motion Graphs' : 'Show Motion Graphs'}
                    </button>
                    <button
                        onClick={() => setShowProjectilePath(!showProjectilePath)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showProjectilePath 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showProjectilePath ? 'Hide Projectile Path' : 'Show Projectile Path'}
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

            {/* Motion Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Motion Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={motionType} 
                    onChange={(e) => !isSubmitted && setMotionType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="uniform">Uniform Motion (Constant Velocity)</option>
                    <option value="accelerated">Accelerated Motion</option>
                    <option value="projectile">Projectile Motion</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {motionType === 'uniform' 
                        ? 'Motion with constant velocity (no acceleration)'
                        : motionType === 'accelerated'
                        ? 'Motion with constant acceleration'
                        : 'Motion under gravity with initial velocity at an angle'
                    }
                </p>
            </div>

            {/* Input Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Initial Conditions:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Initial Position (m):</label>
                            <input 
                                type="number" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={initialPosition} 
                                onChange={(e) => !isSubmitted && setInitialPosition(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Initial Velocity (m/s):</label>
                            <input 
                                type="number" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={initialVelocity} 
                                onChange={(e) => !isSubmitted && setInitialVelocity(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        {motionType === 'projectile' && (
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">Launch Angle (°):</label>
                                <input 
                                    type="number" 
                                    min="0" 
                                    max="90"
                                    step="1"
                                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                    value={angle} 
                                    onChange={(e) => !isSubmitted && setAngle(parseFloat(e.target.value))} 
                                    disabled={isSubmitted} 
                                />
                            </div>
                        )}
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Motion Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Time (s):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={time} 
                                onChange={(e) => !isSubmitted && setTime(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        {(motionType === 'accelerated' || motionType === 'projectile') && (
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-2">
                                    {motionType === 'accelerated' ? 'Acceleration (m/s²):' : 'Gravity (m/s²):'}
                                </label>
                                <input 
                                    type="number" 
                                    step="0.01"
                                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                    value={motionType === 'accelerated' ? acceleration : gravity} 
                                    onChange={(e) => !isSubmitted && setAcceleration(parseFloat(e.target.value))} 
                                    disabled={isSubmitted} 
                                />
                            </div>
                        )}
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Motion Results:</h4>
                {motionType === 'projectile' ? (
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Range</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.projectileData?.range)} m</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Max Height</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.projectileData?.maxHeight)} m</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Time of Flight</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.projectileData?.timeOfFlight)} s</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Final Velocity</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.projectileData?.finalVelocity)} m/s</div>
                        </div>
                    </div>
                ) : (
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Final Position</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.finalPosition)} m</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Displacement</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.displacement)} m</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Final Velocity</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.finalVelocity)} m/s</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Average Velocity</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.averageVelocity)} m/s</div>
                        </div>
                    </div>
                )}
            </div>

            {/* Motion Graphs */}
            {showMotionGraphs && motionType !== 'projectile' && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Motion Graphs:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        {/* Position vs Time Graph */}
                        <div className="h-64 bg-white rounded border p-4">
                            <h5 className="text-sm font-medium text-gray-700 mb-2 text-center">Position vs Time</h5>
                            <svg className="w-full h-full" viewBox="0 0 400 200">
                                {/* Graph axes */}
                                <line x1="20" y1="20" x2="20" y2="180" stroke="black" strokeWidth="2" />
                                <line x1="20" y1="180" x2="380" y2="180" stroke="black" strokeWidth="2" />
                                
                                {/* Labels */}
                                <text x="10" y="100" transform="rotate(-90 10 100)" className="text-xs">Position (m)</text>
                                <text x="200" y="195" className="text-xs">Time (s)</text>
                                
                                {/* Plot data */}
                                {generateMotionData().map((point, i) => {
                                    const x = 20 + (point.time / time) * 360;
                                    const maxPos = Math.max(...generateMotionData().map(p => p.position));
                                    const minPos = Math.min(...generateMotionData().map(p => p.position));
                                    const y = 180 - ((point.position - minPos) / (maxPos - minPos)) * 160;
                                    
                                    if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="blue" />;
                                    
                                    const prevPoint = generateMotionData()[i - 1];
                                    const prevX = 20 + (prevPoint.time / time) * 360;
                                    const prevY = 180 - ((prevPoint.position - minPos) / (maxPos - minPos)) * 160;
                                    
                                    return (
                                        <g key={i}>
                                            <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="blue" strokeWidth="2" />
                                            <circle cx={x} cy={y} r="2" fill="blue" />
                                        </g>
                                    );
                                })}
                            </svg>
                        </div>
                        
                        {/* Velocity vs Time Graph */}
                        <div className="h-64 bg-white rounded border p-4">
                            <h5 className="text-sm font-medium text-gray-700 mb-2 text-center">Velocity vs Time</h5>
                            <svg className="w-full h-full" viewBox="0 0 400 200">
                                {/* Graph axes */}
                                <line x1="20" y1="20" x2="20" y2="180" stroke="black" strokeWidth="2" />
                                <line x1="20" y1="180" x2="380" y2="180" stroke="black" strokeWidth="2" />
                                
                                {/* Labels */}
                                <text x="10" y="100" transform="rotate(-90 10 100)" className="text-xs">Velocity (m/s)</text>
                                <text x="200" y="195" className="text-xs">Time (s)</text>
                                
                                {/* Plot data */}
                                {generateMotionData().map((point, i) => {
                                    const x = 20 + (point.time / time) * 360;
                                    const maxVel = Math.max(...generateMotionData().map(p => p.velocity));
                                    const minVel = Math.min(...generateMotionData().map(p => p.velocity));
                                    const y = 180 - ((point.velocity - minVel) / (maxVel - minVel)) * 160;
                                    
                                    if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="red" />;
                                    
                                    const prevPoint = generateMotionData()[i - 1];
                                    const prevX = 20 + (prevPoint.time / time) * 360;
                                    const prevY = 180 - ((prevPoint.velocity - minVel) / (maxVel - minVel)) * 160;
                                    
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
                </div>
            )}

            {/* Projectile Path */}
            {showProjectilePath && motionType === 'projectile' && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Projectile Path:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Ground line */}
                            <line x1="20" y1="280" x2="380" y2="280" stroke="black" strokeWidth="2" />
                            <text x="200" y="295" className="text-xs text-center">Ground</text>
                            
                            {/* Plot projectile path */}
                            {generateProjectileData().map((point, i) => {
                                const x = 20 + (point.x / Math.max(...generateProjectileData().map(p => p.x))) * 360;
                                const y = 280 - (point.y / Math.max(...generateProjectileData().map(p => p.y))) * 200;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="3" fill="green" />;
                                
                                const prevPoint = generateProjectileData()[i - 1];
                                const prevX = 20 + (prevPoint.x / Math.max(...generateProjectileData().map(p => p.x))) * 360;
                                const prevY = 280 - (prevPoint.y / Math.max(...generateProjectileData().map(p => p.y))) * 200;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="green" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="green" />
                                    </g>
                                );
                            })}
                            
                            {/* Launch point */}
                            <circle cx="20" cy="280" r="4" fill="red" />
                            <text x="25" y="275" className="text-xs">Launch</text>
                            
                            {/* Landing point */}
                            {results.projectileData && (
                                <g>
                                    <circle 
                                        cx={20 + (results.projectileData.range / Math.max(...generateProjectileData().map(p => p.x))) * 360} 
                                        cy="280" 
                                        r="4" 
                                        fill="red" 
                                    />
                                    <text 
                                        x={25 + (results.projectileData.range / Math.max(...generateProjectileData().map(p => p.x))) * 360} 
                                        y="275" 
                                        className="text-xs"
                                    >
                                        Landing
                                    </text>
                                </g>
                            )}
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        {motionType === 'uniform' && (
                            <>
                                <div><strong>Uniform Motion Equations:</strong></div>
                                <div>• Position: x = x₀ + v₀t</div>
                                <div>• Where: x₀ = {formatNumber(initialPosition)} m, v₀ = {formatNumber(initialVelocity)} m/s, t = {formatNumber(time)} s</div>
                                <div>• Final Position: x = {formatNumber(initialPosition)} + {formatNumber(initialVelocity)} × {formatNumber(time)} = {formatNumber(results.finalPosition)} m</div>
                                <div>• Displacement: Δx = x - x₀ = {formatNumber(results.finalPosition)} - {formatNumber(initialPosition)} = {formatNumber(results.displacement)} m</div>
                            </>
                        )}
                        
                        {motionType === 'accelerated' && (
                            <>
                                <div><strong>Accelerated Motion Equations:</strong></div>
                                <div>• Position: x = x₀ + v₀t + ½at²</div>
                                <div>• Velocity: v = v₀ + at</div>
                                <div>• Where: x₀ = {formatNumber(initialPosition)} m, v₀ = {formatNumber(initialVelocity)} m/s, a = {formatNumber(acceleration)} m/s², t = {formatNumber(time)} s</div>
                                <div>• Final Position: x = {formatNumber(initialPosition)} + {formatNumber(initialVelocity)} × {formatNumber(time)} + ½ × {formatNumber(acceleration)} × {formatNumber(time)}² = {formatNumber(results.finalPosition)} m</div>
                                <div>• Final Velocity: v = {formatNumber(initialVelocity)} + {formatNumber(acceleration)} × {formatNumber(time)} = {formatNumber(results.finalVelocity)} m/s</div>
                            </>
                        )}
                        
                        {motionType === 'projectile' && (
                            <>
                                <div><strong>Projectile Motion Equations:</strong></div>
                                <div>• Horizontal: x = v₀cos(θ)t</div>
                                <div>• Vertical: y = y₀ + v₀sin(θ)t - ½gt²</div>
                                <div>• Where: v₀ = {formatNumber(initialVelocity)} m/s, θ = {formatNumber(angle)}°, g = {formatNumber(gravity)} m/s²</div>
                                <div>• v₀ₓ = {formatNumber(initialVelocity)} × cos({formatNumber(angle)}°) = {formatNumber(results.projectileData?.v0x)} m/s</div>
                                <div>• v₀ᵧ = {formatNumber(initialVelocity)} × sin({formatNumber(angle)}°) = {formatNumber(results.projectileData?.v0y)} m/s</div>
                                <div>• Time of Flight: t = 2v₀ᵧ/g = 2 × {formatNumber(results.projectileData?.v0y)}/{formatNumber(gravity)} = {formatNumber(results.projectileData?.timeOfFlight)} s</div>
                                <div>• Range: R = v₀ₓ × t = {formatNumber(results.projectileData?.v0x)} × {formatNumber(results.projectileData?.timeOfFlight)} = {formatNumber(results.projectileData?.range)} m</div>
                                <div>• Max Height: h = y₀ + v₀ᵧ²/(2g) = {formatNumber(initialPosition)} + {formatNumber(results.projectileData?.v0y)}²/(2 × {formatNumber(gravity)}) = {formatNumber(results.projectileData?.maxHeight)} m</div>
                            </>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Uniform motion: constant velocity, no acceleration</li>
                    <li>• Accelerated motion: constant acceleration, changing velocity</li>
                    <li>• Projectile motion: motion under gravity with initial velocity at an angle</li>
                    <li>• For projectile motion, maximum range occurs at 45° launch angle</li>
                    <li>• The horizontal and vertical motions are independent in projectile motion</li>
                </ul>
            </div>
        </div>
    );
};

export default KinematicsSimulator;
