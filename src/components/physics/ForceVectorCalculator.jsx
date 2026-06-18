import React, { useState, useEffect } from 'react';

const ForceVectorCalculator = ({ initialData, onChange, isSubmitted }) => {
    const [forces, setForces] = useState(initialData.forces || [
        { id: 1, magnitude: 10, angle: 0, label: 'F₁' },
        { id: 2, magnitude: 15, angle: 90, label: 'F₂' }
    ]);
    const [showVectorDiagram, setShowVectorDiagram] = useState(false);
    const [showEquilibrium, setShowEquilibrium] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [coordinateSystem, setCoordinateSystem] = useState('cartesian');

    useEffect(() => {
        const formattedData = {
            type: "force_vector_calculator",
            forces: forces,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [forces, onChange]);

    const calculateResults = () => {
        const results = {};
        
        // Calculate components and resultant
        results.components = calculateComponents();
        results.resultant = calculateResultant();
        results.equilibrium = calculateEquilibrium();
        results.magnitude = Math.sqrt(results.resultant.x ** 2 + results.resultant.y ** 2);
        results.angle = Math.atan2(results.resultant.y, results.resultant.x) * (180 / Math.PI);
        
        return results;
    };

    const calculateComponents = () => {
        return forces.map(force => ({
            id: force.id,
            label: force.label,
            magnitude: force.magnitude,
            angle: force.angle,
            x: force.magnitude * Math.cos(force.angle * Math.PI / 180),
            y: force.magnitude * Math.sin(force.angle * Math.PI / 180)
        }));
    };

    const calculateResultant = () => {
        const components = calculateComponents();
        const x = components.reduce((sum, force) => sum + force.x, 0);
        const y = components.reduce((sum, force) => sum + force.y, 0);
        return { x, y };
    };

    const calculateEquilibrium = () => {
        const resultant = calculateResultant();
        const magnitude = Math.sqrt(resultant.x ** 2 + resultant.y ** 2);
        
        if (magnitude < 0.01) {
            return {
                isEquilibrium: true,
                description: 'System is in equilibrium (ΣF ≈ 0)',
                requiredForce: { magnitude: 0, angle: 0 }
            };
        } else {
            const requiredMagnitude = magnitude;
            const requiredAngle = Math.atan2(-resultant.y, -resultant.x) * (180 / Math.PI);
            return {
                isEquilibrium: false,
                description: 'System is not in equilibrium',
                requiredForce: { 
                    magnitude: requiredMagnitude, 
                    angle: requiredAngle 
                }
            };
        }
    };

    const addForce = () => {
        const newId = Math.max(...forces.map(f => f.id)) + 1;
        const newForce = {
            id: newId,
            magnitude: 10,
            angle: 0,
            label: `F${newId}`
        };
        setForces([...forces, newForce]);
    };

    const removeForce = (id) => {
        if (forces.length > 1) {
            setForces(forces.filter(f => f.id !== id));
        }
    };

    const updateForce = (id, field, value) => {
        setForces(forces.map(f => 
            f.id === id ? { ...f, [field]: value } : f
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
                <h3 className="text-lg font-semibold text-gray-800">Force Vector Calculator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowVectorDiagram(!showVectorDiagram)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showVectorDiagram 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showVectorDiagram ? 'Hide Vector Diagram' : 'Show Vector Diagram'}
                    </button>
                    <button
                        onClick={() => setShowEquilibrium(!showEquilibrium)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showEquilibrium 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showEquilibrium ? 'Hide Equilibrium' : 'Show Equilibrium'}
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

            {/* Force Input Section */}
            <div className="mb-6">
                <div className="flex items-center justify-between mb-4">
                    <h4 className="text-md font-medium text-gray-800">Force Vectors</h4>
                    <button
                        onClick={addForce}
                        disabled={isSubmitted}
                        className="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 transition-colors"
                    >
                        Add Force
                    </button>
                </div>
                
                <div className="space-y-4">
                    {forces.map((force, index) => (
                        <div key={force.id} className="p-4 bg-gray-50 rounded-lg border border-gray-200">
                            <div className="flex items-center justify-between mb-3">
                                <h5 className="text-sm font-medium text-gray-700">{force.label}</h5>
                                {forces.length > 1 && (
                                    <button
                                        onClick={() => removeForce(force.id)}
                                        disabled={isSubmitted}
                                        className="text-red-500 hover:text-red-700 disabled:opacity-50"
                                    >
                                        Remove
                                    </button>
                                )}
                            </div>
                            
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">Magnitude (N):</label>
                                    <input 
                                        type="number" 
                                        min="0.1" 
                                        max="1000"
                                        step="0.1"
                                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                        value={force.magnitude} 
                                        onChange={(e) => !isSubmitted && updateForce(force.id, 'magnitude', parseFloat(e.target.value))} 
                                        disabled={isSubmitted} 
                                    />
                                </div>
                                
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">Angle (°):</label>
                                    <input 
                                        type="number" 
                                        min="-180" 
                                        max="180"
                                        step="1"
                                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                        value={force.angle} 
                                        onChange={(e) => !isSubmitted && updateForce(force.id, 'angle', parseFloat(e.target.value))} 
                                        disabled={isSubmitted} 
                                    />
                                    <p className="text-xs text-gray-500 mt-1">
                                        {force.angle === 0 ? '→' : 
                                         force.angle === 90 ? '↑' : 
                                         force.angle === 180 ? '←' : 
                                         force.angle === -90 ? '↓' : 
                                         force.angle > 0 ? `${force.angle}° CCW from +x` : `${Math.abs(force.angle)}° CW from +x`}
                                    </p>
                                </div>
                                
                                <div>
                                    <label className="block text-sm font-medium text-gray-700 mb-2">Label:</label>
                                    <input 
                                        type="text" 
                                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                        value={force.label} 
                                        onChange={(e) => !isSubmitted && updateForce(force.id, 'label', e.target.value)} 
                                        disabled={isSubmitted} 
                                    />
                                </div>
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                <h4 className="text-md font-medium text-green-800 mb-3">Vector Analysis Results:</h4>
                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Resultant Magnitude</div>
                        <div className="text-xl text-green-700">{formatNumber(results.magnitude)} N</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Resultant Angle</div>
                        <div className="text-xl text-green-700">{formatNumber(results.angle)}°</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">X Component</div>
                        <div className="text-xl text-green-700">{formatNumber(results.resultant.x)} N</div>
                    </div>
                    <div className="text-center p-3 bg-white rounded border">
                        <div className="text-lg font-semibold text-gray-800">Y Component</div>
                        <div className="text-xl text-green-700">{formatNumber(results.resultant.y)} N</div>
                    </div>
                </div>
            </div>

            {/* Force Components Table */}
            <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                <h4 className="text-md font-medium text-blue-800 mb-3">Force Components:</h4>
                <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                        <thead>
                            <tr className="border-b border-gray-200">
                                <th className="text-left p-2">Force</th>
                                <th className="text-left p-2">Magnitude (N)</th>
                                <th className="text-left p-2">Angle (°)</th>
                                <th className="text-left p-2">X Component (N)</th>
                                <th className="text-left p-2">Y Component (N)</th>
                            </tr>
                        </thead>
                        <tbody>
                            {results.components.map((force) => (
                                <tr key={force.id} className="border-b border-gray-100">
                                    <td className="p-2 font-medium">{force.label}</td>
                                    <td className="p-2">{formatNumber(force.magnitude)}</td>
                                    <td className="p-2">{formatNumber(force.angle)}</td>
                                    <td className="p-2">{formatNumber(force.x)}</td>
                                    <td className="p-2">{formatNumber(force.y)}</td>
                                </tr>
                            ))}
                            <tr className="border-t-2 border-gray-300 bg-gray-50">
                                <td className="p-2 font-bold">Resultant</td>
                                <td className="p-2 font-bold">{formatNumber(results.magnitude)}</td>
                                <td className="p-2 font-bold">{formatNumber(results.angle)}</td>
                                <td className="p-2 font-bold">{formatNumber(results.resultant.x)}</td>
                                <td className="p-2 font-bold">{formatNumber(results.resultant.y)}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

            {/* Equilibrium Analysis */}
            {showEquilibrium && (
                <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                    <h4 className="text-md font-medium text-purple-800 mb-3">Equilibrium Analysis:</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">System Status:</h5>
                            <div className={`text-lg font-semibold ${
                                results.equilibrium.isEquilibrium ? 'text-green-600' : 'text-red-600'
                            }`}>
                                {results.equilibrium.isEquilibrium ? '✓ In Equilibrium' : '✗ Not in Equilibrium'}
                            </div>
                            <p className="text-sm text-gray-600 mt-2">
                                {results.equilibrium.description}
                            </p>
                        </div>
                        <div className="p-3 bg-white rounded border">
                            <h5 className="font-medium text-gray-800 mb-2">Required Force for Equilibrium:</h5>
                            <div className="text-sm text-gray-600">
                                <div><strong>Magnitude:</strong> {formatNumber(results.equilibrium.requiredForce.magnitude)} N</div>
                                <div><strong>Angle:</strong> {formatNumber(results.equilibrium.requiredForce.angle)}°</div>
                                <div><strong>Direction:</strong> 
                                    {results.equilibrium.requiredForce.angle === 0 ? ' →' : 
                                     results.equilibrium.requiredForce.angle === 90 ? ' ↑' : 
                                     results.equilibrium.requiredForce.angle === 180 ? ' ←' : 
                                     results.equilibrium.requiredForce.angle === -90 ? ' ↓' : 
                                     results.equilibrium.requiredForce.angle > 0 ? ` ${results.equilibrium.requiredForce.angle}° CCW from +x` : ` ${Math.abs(results.equilibrium.requiredForce.angle)}° CW from +x`}
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            )}

            {/* Vector Diagram */}
            {showVectorDiagram && (
                <div className="mb-6 p-4 bg-gray-50 rounded-lg border border-gray-200">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Vector Diagram:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Coordinate axes */}
                            <line x1="200" y1="50" x2="200" y2="250" stroke="black" strokeWidth="1" />
                            <line x1="50" y1="150" x2="350" y2="150" stroke="black" strokeWidth="1" />
                            
                            {/* Axis labels */}
                            <text x="205" y="45" className="text-xs">+y</text>
                            <text x="355" y="155" className="text-xs">+x</text>
                            <text x="195" y="255" className="text-xs">-y</text>
                            <text x="45" y="155" className="text-xs">-x</text>
                            
                            {/* Origin */}
                            <circle cx="200" cy="150" r="3" fill="black" />
                            <text x="210" y="155" className="text-xs">O</text>
                            
                            {/* Plot force vectors */}
                            {results.components.map((force, index) => {
                                const colors = ['#ef4444', '#3b82f6', '#10b981', '#f59e0b', '#8b5cf6'];
                                const color = colors[index % colors.length];
                                
                                const startX = 200;
                                const startY = 150;
                                const endX = startX + force.x * 10; // Scale factor
                                const endY = startY - force.y * 10; // Invert Y for SVG
                                
                                return (
                                    <g key={force.id}>
                                        {/* Force vector */}
                                        <line 
                                            x1={startX} y1={startY} x2={endX} y2={endY} 
                                            stroke={color} strokeWidth="3" 
                                            markerEnd="url(#arrowhead)"
                                        />
                                        
                                        {/* Force label */}
                                        <text 
                                            x={(startX + endX) / 2 + 10} 
                                            y={(startY + endY) / 2 - 10} 
                                            className="text-xs font-bold"
                                            fill={color}
                                        >
                                            {force.label}
                                        </text>
                                        
                                        {/* Magnitude label */}
                                        <text 
                                            x={(startX + endX) / 2 - 10} 
                                            y={(startY + endY) / 2 + 15} 
                                            className="text-xs"
                                            fill={color}
                                        >
                                            {formatNumber(force.magnitude)}N
                                        </text>
                                    </g>
                                );
                            })}
                            
                            {/* Resultant vector */}
                            {results.magnitude > 0.01 && (
                                <g>
                                    <line 
                                        x1="200" y1="150" 
                                        x2={200 + results.resultant.x * 10} 
                                        y2={150 - results.resultant.y * 10} 
                                        stroke="black" strokeWidth="4" 
                                        strokeDasharray="5,5"
                                        markerEnd="url(#arrowhead)"
                                    />
                                    <text 
                                        x={200 + results.resultant.x * 5 + 15} 
                                        y={150 - results.resultant.y * 5 - 10} 
                                        className="text-xs font-bold"
                                        fill="black"
                                    >
                                        R
                                    </text>
                                </g>
                            )}
                            
                            {/* Arrow marker definition */}
                            <defs>
                                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
                                    <polygon points="0 0, 10 3.5, 0 7" fill="currentColor" />
                                </marker>
                            </defs>
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        <div><strong>Vector Components:</strong> Fx = F × cos(θ), Fy = F × sin(θ)</div>
                        {results.components.map((force) => (
                            <div key={force.id}>
                                <strong>{force.label}:</strong>
                                <div>• Fx = {formatNumber(force.magnitude)} × cos({formatNumber(force.angle)}°) = {formatNumber(force.x)} N</div>
                                <div>• Fy = {formatNumber(force.magnitude)} × sin({formatNumber(force.angle)}°) = {formatNumber(force.y)} N</div>
                            </div>
                        ))}
                        <div><strong>Resultant Components:</strong></div>
                        <div>• Rx = ΣFx = {results.components.map(f => formatNumber(f.x)).join(' + ')} = {formatNumber(results.resultant.x)} N</div>
                        <div>• Ry = ΣFy = {results.components.map(f => formatNumber(f.y)).join(' + ')} = {formatNumber(results.resultant.y)} N</div>
                        <div><strong>Resultant Magnitude:</strong> R = √(Rx² + Ry²) = √({formatNumber(results.resultant.x)}² + {formatNumber(results.resultant.y)}²) = {formatNumber(results.magnitude)} N</div>
                        <div><strong>Resultant Angle:</strong> θ = tan⁻¹(Ry/Rx) = tan⁻¹({formatNumber(results.resultant.y)}/{formatNumber(results.resultant.x)}) = {formatNumber(results.angle)}°</div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Positive angles are measured counterclockwise from the +x axis</li>
                    <li>• Negative angles are measured clockwise from the +x axis</li>
                    <li>• 0° = →, 90° = ↑, 180° = ←, -90° = ↓</li>
                    <li>• For equilibrium, the resultant force must be zero</li>
                    <li>• Use the required force to balance the system</li>
                </ul>
            </div>
        </div>
    );
};

export default ForceVectorCalculator;
