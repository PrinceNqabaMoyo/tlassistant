import React, { useState, useEffect } from 'react';

const WaveSimulator = ({ initialData, onChange, isSubmitted }) => {
    const [waveType, setWaveType] = useState(initialData.waveType || 'transverse');
    const [amplitude, setAmplitude] = useState(initialData.amplitude || 2);
    const [wavelength, setWavelength] = useState(initialData.wavelength || 4);
    const [frequency, setFrequency] = useState(initialData.frequency || 1);
    const [phase, setPhase] = useState(initialData.phase || 0);
    const [time, setTime] = useState(initialData.time || 0);
    const [showInterference, setShowInterference] = useState(false);
    const [showDiffraction, setShowDiffraction] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [waveSpeed, setWaveSpeed] = useState(initialData.waveSpeed || 5);

    useEffect(() => {
        const formattedData = {
            type: "wave_simulator",
            waveType: waveType,
            amplitude: amplitude,
            wavelength: wavelength,
            frequency: frequency,
            phase: phase,
            time: time,
            waveSpeed: waveSpeed,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [waveType, amplitude, wavelength, frequency, phase, time, waveSpeed, onChange]);

    const calculateResults = () => {
        const results = {};
        
        results.period = 1 / frequency;
        results.angularFrequency = 2 * Math.PI * frequency;
        results.waveNumber = 2 * Math.PI / wavelength;
        results.velocity = wavelength * frequency;
        results.energy = 0.5 * amplitude * amplitude * frequency * frequency;
        
        if (showInterference) {
            results.interferencePattern = calculateInterferencePattern();
        }
        
        if (showDiffraction) {
            results.diffractionPattern = calculateDiffractionPattern();
        }
        
        return results;
    };

    const calculateInterferencePattern = () => {
        const pattern = [];
        const xStep = 0.1;
        
        for (let x = 0; x <= 20; x += xStep) {
            const wave1 = amplitude * Math.sin(2 * Math.PI * (x / wavelength - frequency * time) + phase);
            const wave2 = amplitude * Math.sin(2 * Math.PI * ((x + wavelength/2) / wavelength - frequency * time) + phase);
            const interference = wave1 + wave2;
            
            pattern.push({ x, wave1, wave2, interference });
        }
        
        return pattern;
    };

    const calculateDiffractionPattern = () => {
        const pattern = [];
        const angleStep = 0.1;
        const slitWidth = wavelength / 2;
        
        for (let angle = -Math.PI/4; angle <= Math.PI/4; angle += angleStep) {
            const beta = (Math.PI * slitWidth * Math.sin(angle)) / wavelength;
            const intensity = beta === 0 ? 1 : Math.pow(Math.sin(beta) / beta, 2);
            
            pattern.push({ angle, intensity });
        }
        
        return pattern;
    };

    const generateWaveData = () => {
        const data = [];
        const xStep = 0.1;
        
        for (let x = 0; x <= 20; x += xStep) {
            let y;
            if (waveType === 'transverse') {
                y = amplitude * Math.sin(2 * Math.PI * (x / wavelength - frequency * time) + phase);
            } else {
                y = amplitude * Math.cos(2 * Math.PI * (x / wavelength - frequency * time) + phase);
            }
            
            data.push({ x, y });
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
                <h3 className="text-lg font-semibold text-gray-800">Wave Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowInterference(!showInterference)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showInterference 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showInterference ? 'Hide Interference' : 'Show Interference'}
                    </button>
                    <button
                        onClick={() => setShowDiffraction(!showDiffraction)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showDiffraction 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showDiffraction ? 'Hide Diffraction' : 'Show Diffraction'}
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

            {/* Wave Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Wave Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={waveType} 
                    onChange={(e) => !isSubmitted && setWaveType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="transverse">Transverse Wave</option>
                    <option value="longitudinal">Longitudinal Wave</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {waveType === 'transverse' 
                        ? 'Wave oscillations perpendicular to propagation direction (e.g., light, water waves)'
                        : 'Wave oscillations parallel to propagation direction (e.g., sound waves)'
                    }
                </p>
            </div>

            {/* Input Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Wave Properties:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Amplitude (m):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={amplitude} 
                                onChange={(e) => !isSubmitted && setAmplitude(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Wavelength (m):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={wavelength} 
                                onChange={(e) => !isSubmitted && setWavelength(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Frequency (Hz):</label>
                            <input 
                                type="number" 
                                min="0.1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={frequency} 
                                onChange={(e) => !isSubmitted && setFrequency(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Advanced Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Phase (rad):</label>
                            <input 
                                type="number" 
                                min="0" 
                                max="6.28"
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={phase} 
                                onChange={(e) => !isSubmitted && setPhase(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Time (s):</label>
                            <input 
                                type="number" 
                                min="0" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={time} 
                                onChange={(e) => !isSubmitted && setTime(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Wave Speed (m/s):</label>
                            <input 
                                type="number" 
                                min="1" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={waveSpeed} 
                                onChange={(e) => !isSubmitted && setWaveSpeed(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Wave Properties:</h4>
                <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Period</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.period)} s</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Angular Frequency</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.angularFrequency)} rad/s</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Wave Number</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.waveNumber)} rad/m</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Velocity</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.velocity)} m/s</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Energy</div>
                        <div className="text-xl text-purple-700">{formatNumber(results.energy)} J</div>
                    </div>
                </div>
            </div>

            {/* Wave Visualization */}
            <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                <h4 className="text-md font-medium text-gray-800 mb-3">Wave Visualization:</h4>
                <div className="h-80 bg-white rounded border p-4">
                    <svg className="w-full h-full" viewBox="0 0 400 300">
                        {/* Graph axes */}
                        <line x1="20" y1="150" x2="380" y2="150" stroke="black" strokeWidth="1" />
                        <line x1="20" y1="20" x2="20" y2="280" stroke="black" strokeWidth="1" />
                        
                        {/* Labels */}
                        <text x="200" y="295" className="text-xs">Position (m)</text>
                        <text x="10" y="150" className="text-xs">Amplitude</text>
                        
                        {/* Plot wave */}
                        {generateWaveData().map((point, i) => {
                            const x = 20 + (point.x / 20) * 360;
                            const y = 150 - (point.y / (amplitude * 2)) * 120;
                            
                            if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="blue" />;
                            
                            const prevPoint = generateWaveData()[i - 1];
                            const prevX = 20 + (prevPoint.x / 20) * 360;
                            const prevY = 150 - (prevPoint.y / (amplitude * 2)) * 120;
                            
                            return (
                                <g key={i}>
                                    <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="blue" strokeWidth="2" />
                                    <circle cx={x} cy={y} r="2" fill="blue" />
                                </g>
                            );
                        })}
                        
                        {/* Wavelength markers */}
                        <line x1="20" y1="140" x2="20 + (wavelength / 20) * 360" y2="140" stroke="red" strokeWidth="2" />
                        <text x="20 + (wavelength / 20) * 180" y="135" className="text-xs text-red-600">λ = {formatNumber(wavelength)} m</text>
                        
                        {/* Amplitude markers */}
                        <line x1="15" y1="150 - (amplitude / (amplitude * 2)) * 120" x2="15" y2="150 + (amplitude / (amplitude * 2)) * 120" stroke="green" strokeWidth="2" />
                        <text x="10" y="150" className="text-xs text-green-600">A = {formatNumber(amplitude)} m</text>
                    </svg>
                </div>
            </div>

            {/* Interference Pattern */}
            {showInterference && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Wave Interference Pattern:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Graph axes */}
                            <line x1="20" y1="150" x2="380" y2="150" stroke="black" strokeWidth="1" />
                            <line x1="20" y1="20" x2="20" y2="280" stroke="black" strokeWidth="1" />
                            
                            {/* Labels */}
                            <text x="200" y="295" className="text-xs">Position (m)</text>
                            <text x="10" y="150" className="text-xs">Amplitude</text>
                            
                            {/* Plot individual waves */}
                            {results.interferencePattern?.map((point, i) => {
                                const x = 20 + (point.x / 20) * 360;
                                const y1 = 150 - (point.wave1 / (amplitude * 2)) * 120;
                                const y2 = 150 - (point.wave2 / (amplitude * 2)) * 120;
                                const y3 = 150 - (point.interference / (amplitude * 4)) * 120;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y3} r="2" fill="purple" />;
                                
                                const prevPoint = results.interferencePattern[i - 1];
                                const prevX = 20 + (prevPoint.x / 20) * 360;
                                const prevY1 = 150 - (prevPoint.wave1 / (amplitude * 2)) * 120;
                                const prevY2 = 150 - (prevPoint.wave2 / (amplitude * 2)) * 120;
                                const prevY3 = 150 - (prevPoint.interference / (amplitude * 4)) * 120;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY1} x2={x} y2={y1} stroke="blue" strokeWidth="1" opacity="0.5" />
                                        <line x1={prevX} y1={prevY2} x2={x} y2={y2} stroke="red" strokeWidth="1" opacity="0.5" />
                                        <line x1={prevX} y1={prevY3} x2={x} y2={y3} stroke="purple" strokeWidth="2" />
                                        <circle cx={x} cy={y3} r="2" fill="purple" />
                                    </g>
                                );
                            })}
                            
                            {/* Legend */}
                            <text x="300" y="30" className="text-xs font-bold">Legend</text>
                            <line x1="300" y1="35" x2="320" y2="35" stroke="blue" strokeWidth="1" opacity="0.5" />
                            <text x="325" y="38" className="text-xs">Wave 1</text>
                            <line x1="300" y1="45" x2="320" y2="45" stroke="red" strokeWidth="1" opacity="0.5" />
                            <text x="325" y="48" className="text-xs">Wave 2</text>
                            <line x1="300" y1="55" x2="320" y2="55" stroke="purple" strokeWidth="2" />
                            <text x="325" y="58" className="text-xs">Interference</text>
                        </svg>
                    </div>
                </div>
            )}

            {/* Diffraction Pattern */}
            {showDiffraction && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Diffraction Pattern:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Graph axes */}
                            <line x1="20" y1="280" x2="380" y2="280" stroke="black" strokeWidth="1" />
                            <line x1="200" y1="20" x2="200" y2="280" stroke="black" strokeWidth="1" />
                            
                            {/* Labels */}
                            <text x="200" y="295" className="text-xs">Angle (rad)</text>
                            <text x="10" y="150" transform="rotate(-90 10 150)" className="text-xs">Intensity</text>
                            
                            {/* Plot diffraction pattern */}
                            {results.diffractionPattern?.map((point, i) => {
                                const x = 200 + (point.angle / (Math.PI/4)) * 180;
                                const y = 280 - point.intensity * 200;
                                
                                if (i === 0) return <circle key={i} cx={x} cy={y} r="2" fill="green" />;
                                
                                const prevPoint = results.diffractionPattern[i - 1];
                                const prevX = 200 + (prevPoint.angle / (Math.PI/4)) * 180;
                                const prevY = 280 - prevPoint.intensity * 200;
                                
                                return (
                                    <g key={i}>
                                        <line x1={prevX} y1={prevY} x2={x} y2={y} stroke="green" strokeWidth="2" />
                                        <circle cx={x} cy={y} r="2" fill="green" />
                                    </g>
                                );
                            })}
                            
                            {/* Central maximum marker */}
                            <line x1="200" y1="80" x2="200" y2="280" stroke="red" strokeWidth="1" strokeDasharray="5,5" />
                            <text x="205" y="90" className="text-xs text-red-600">Central Maximum</text>
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Wave Properties:</strong></div>
                        <div>• Period: T = 1/f = 1/{formatNumber(frequency)} = {formatNumber(results.period)} s</div>
                        <div>• Angular Frequency: ω = 2πf = 2π × {formatNumber(frequency)} = {formatNumber(results.angularFrequency)} rad/s</div>
                        <div>• Wave Number: k = 2π/λ = 2π/{formatNumber(wavelength)} = {formatNumber(results.waveNumber)} rad/m</div>
                        <div>• Wave Velocity: v = λf = {formatNumber(wavelength)} × {formatNumber(frequency)} = {formatNumber(results.velocity)} m/s</div>
                        <div>• Wave Energy: E = ½A²ω² = ½ × {formatNumber(amplitude)}² × {formatNumber(results.angularFrequency)}² = {formatNumber(results.energy)} J</div>
                        
                        {showInterference && (
                            <>
                                <div><strong>Interference Pattern:</strong></div>
                                <div>• Wave 1: y₁ = A sin(kx - ωt + φ) = {formatNumber(amplitude)} sin({formatNumber(results.waveNumber)}x - {formatNumber(results.angularFrequency)}t + {formatNumber(phase)})</div>
                                <div>• Wave 2: y₂ = A sin(k(x + λ/2) - ωt + φ) = {formatNumber(amplitude)} sin({formatNumber(results.waveNumber)}(x + {formatNumber(wavelength/2)}) - {formatNumber(results.angularFrequency)}t + {formatNumber(phase)})</div>
                                <div>• Resultant: y = y₁ + y₂ = 2A cos(kλ/4) sin(kx - ωt + φ + kλ/4)</div>
                            </>
                        )}
                        
                        {showDiffraction && (
                            <>
                                <div><strong>Diffraction Pattern:</strong></div>
                                <div>• Single Slit Diffraction: I(θ) = I₀(sin(β)/β)²</div>
                                <div>• Where: β = πa sin(θ)/λ = π × {formatNumber(wavelength/2)} × sin(θ)/{formatNumber(wavelength)}</div>
                                <div>• Central Maximum: θ = 0, I = I₀</div>
                                <div>• First Minimum: β = π, sin(θ) = λ/a = {formatNumber(wavelength)}/{formatNumber(wavelength/2)} = 2</div>
                            </>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Transverse waves oscillate perpendicular to propagation direction</li>
                    <li>• Longitudinal waves oscillate parallel to propagation direction</li>
                    <li>• Wave speed = wavelength × frequency</li>
                    <li>• Interference occurs when two waves overlap</li>
                    <li>• Diffraction occurs when waves pass through small openings</li>
                    <li>• Constructive interference creates larger amplitudes</li>
                    <li>• Destructive interference creates smaller amplitudes</li>
                </ul>
            </div>
        </div>
    );
};

export default WaveSimulator;
