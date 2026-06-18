import React, { useState, useEffect } from 'react';

const OpticsSimulator = ({ initialData, onChange, isSubmitted }) => {
    const [opticsType, setOpticsType] = useState(initialData.opticsType || 'reflection');
    const [incidentAngle, setIncidentAngle] = useState(initialData.incidentAngle || 30);
    const [refractiveIndex1, setRefractiveIndex1] = useState(initialData.refractiveIndex1 || 1.0);
    const [refractiveIndex2, setRefractiveIndex2] = useState(initialData.refractiveIndex2 || 1.5);
    const [focalLength, setFocalLength] = useState(initialData.focalLength || 20);
    const [objectDistance, setObjectDistance] = useState(initialData.objectDistance || 30);
    const [objectHeight, setObjectHeight] = useState(initialData.objectHeight || 10);
    const [showRayDiagram, setShowRayDiagram] = useState(false);
    const [showCalculations, setShowCalculations] = useState(false);
    const [showLensMirror, setShowLensMirror] = useState(false);

    useEffect(() => {
        const formattedData = {
            type: "optics_simulator",
            opticsType: opticsType,
            incidentAngle: incidentAngle,
            refractiveIndex1: refractiveIndex1,
            refractiveIndex2: refractiveIndex2,
            focalLength: focalLength,
            objectDistance: objectDistance,
            objectHeight: objectHeight,
            results: calculateResults()
        };
        onChange(formattedData);
    }, [opticsType, incidentAngle, refractiveIndex1, refractiveIndex2, focalLength, objectDistance, objectHeight, onChange]);

    const calculateResults = () => {
        const results = {};
        
        if (opticsType === 'reflection') {
            results.reflectedAngle = incidentAngle;
            results.incidentAngleRad = incidentAngle * Math.PI / 180;
            results.reflectedAngleRad = results.incidentAngleRad;
        } else if (opticsType === 'refraction') {
            results.incidentAngleRad = incidentAngle * Math.PI / 180;
            results.refractedAngleRad = Math.asin((refractiveIndex1 * Math.sin(results.incidentAngleRad)) / refractiveIndex2);
            results.refractedAngle = results.refractedAngleRad * 180 / Math.PI;
            results.criticalAngle = Math.asin(refractiveIndex2 / refractiveIndex1) * 180 / Math.PI;
            results.totalInternalReflection = incidentAngle > results.criticalAngle;
        } else if (opticsType === 'lens' || opticsType === 'mirror') {
            results.imageDistance = (objectDistance * focalLength) / (objectDistance - focalLength);
            results.magnification = -results.imageDistance / objectDistance;
            results.imageHeight = objectHeight * results.magnification;
            results.isVirtual = results.imageDistance < 0;
            results.isUpright = results.magnification > 0;
        }
        
        return results;
    };

    const generateRayData = () => {
        const data = [];
        const step = 0.1;
        
        if (opticsType === 'reflection') {
            // Generate incident and reflected rays
            for (let x = -20; x <= 0; x += step) {
                const y = x * Math.tan(incidentAngle * Math.PI / 180);
                data.push({ x, y, type: 'incident' });
            }
            for (let x = 0; x <= 20; x += step) {
                const y = -x * Math.tan(incidentAngle * Math.PI / 180);
                data.push({ x, y, type: 'reflected' });
            }
        } else if (opticsType === 'refraction') {
            // Generate incident and refracted rays
            for (let x = -20; x <= 0; x += step) {
                const y = x * Math.tan(incidentAngle * Math.PI / 180);
                data.push({ x, y, type: 'incident' });
            }
            if (!results.totalInternalReflection) {
                for (let x = 0; x <= 20; x += step) {
                    const y = x * Math.tan(results.refractedAngleRad);
                    data.push({ x, y, type: 'refracted' });
                }
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
                <h3 className="text-lg font-semibold text-gray-800">Optics Simulator</h3>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setShowRayDiagram(!showRayDiagram)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showRayDiagram 
                                ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showRayDiagram ? 'Hide Ray Diagram' : 'Show Ray Diagram'}
                    </button>
                    <button
                        onClick={() => setShowLensMirror(!showLensMirror)}
                        className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                            showLensMirror 
                                ? 'bg-green-100 text-green-700 hover:bg-green-200' 
                                : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                        }`}
                    >
                        {showLensMirror ? 'Hide Lens/Mirror' : 'Show Lens/Mirror'}
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

            {/* Optics Type Selection */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Optics Type:</label>
                <select 
                    className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                    value={opticsType} 
                    onChange={(e) => !isSubmitted && setOpticsType(e.target.value)} 
                    disabled={isSubmitted}
                >
                    <option value="reflection">Reflection</option>
                    <option value="refraction">Refraction</option>
                    <option value="lens">Converging Lens</option>
                    <option value="mirror">Concave Mirror</option>
                </select>
                <p className="text-sm text-gray-600 mt-2">
                    {opticsType === 'reflection' 
                        ? 'Light reflecting off a surface (angle of incidence = angle of reflection)'
                        : opticsType === 'refraction'
                        ? 'Light bending as it passes through different media (Snell\'s Law)'
                        : opticsType === 'lens'
                        ? 'Light converging through a convex lens (real/virtual images)'
                        : 'Light reflecting off a concave mirror (real/virtual images)'
                    }
                </p>
            </div>

            {/* Input Parameters */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div className="p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Basic Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Incident Angle (°):</label>
                            <input 
                                type="number" 
                                min="0" 
                                max="89"
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={incidentAngle} 
                                onChange={(e) => !isSubmitted && setIncidentAngle(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Medium 1 Index:</label>
                            <input 
                                type="number" 
                                min="1.0" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={refractiveIndex1} 
                                onChange={(e) => !isSubmitted && setRefractiveIndex1(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Medium 2 Index:</label>
                            <input 
                                type="number" 
                                min="1.0" 
                                step="0.1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                                value={refractiveIndex2} 
                                onChange={(e) => !isSubmitted && setRefractiveIndex2(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
                
                <div className="p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Lens/Mirror Parameters:</h4>
                    <div className="space-y-3">
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Focal Length (cm):</label>
                            <input 
                                type="number" 
                                min="1" 
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={focalLength} 
                                onChange={(e) => !isSubmitted && setFocalLength(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Object Distance (cm):</label>
                            <input 
                                type="number" 
                                min="1" 
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={objectDistance} 
                                onChange={(e) => !isSubmitted && setObjectDistance(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                        
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-2">Object Height (cm):</label>
                            <input 
                                type="number" 
                                min="1" 
                                step="1"
                                className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-green-500 transition-colors" 
                                value={objectHeight} 
                                onChange={(e) => !isSubmitted && setObjectHeight(parseFloat(e.target.value))} 
                                disabled={isSubmitted} 
                            />
                        </div>
                    </div>
                </div>
            </div>

            {/* Results Display */}
            <div className="mb-6 p-4 bg-purple-50 rounded-lg border border-purple-200">
                <h4 className="text-md font-medium text-purple-800 mb-3">Optics Results:</h4>
                {opticsType === 'reflection' && (
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Incident Angle</div>
                            <div className="text-xl text-purple-700">{formatNumber(incidentAngle)}°</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Reflected Angle</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.reflectedAngle)}°</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Law of Reflection</div>
                            <div className="text-xl text-purple-700">θi = θr</div>
                        </div>
                    </div>
                )}
                
                {opticsType === 'refraction' && (
                    <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Incident Angle</div>
                            <div className="text-xl text-purple-700">{formatNumber(incidentAngle)}°</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Refracted Angle</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.refractedAngle)}°</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Critical Angle</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.criticalAngle)}°</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Total Internal</div>
                            <div className="text-xl text-purple-700">{results.totalInternalReflection ? 'Yes' : 'No'}</div>
                        </div>
                    </div>
                )}
                
                {(opticsType === 'lens' || opticsType === 'mirror') && (
                    <div className="grid grid-cols-1 md:grid-cols-5 gap-4">
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Image Distance</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.imageDistance)} cm</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Magnification</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.magnification)}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Image Height</div>
                            <div className="text-xl text-purple-700">{formatNumber(results.imageHeight)} cm</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Image Type</div>
                            <div className="text-xl text-purple-700">{results.isVirtual ? 'Virtual' : 'Real'}</div>
                        </div>
                        <div className="text-center p-3 bg-white rounded border">
                            <div className="text-lg font-semibold text-gray-800">Orientation</div>
                            <div className="text-xl text-purple-700">{results.isUpright ? 'Upright' : 'Inverted'}</div>
                        </div>
                    </div>
                )}
            </div>

            {/* Ray Diagram */}
            {showRayDiagram && (
                <div className="mb-6 p-4 bg-blue-50 rounded-lg border border-blue-200">
                    <h4 className="text-md font-medium text-blue-800 mb-3">Ray Diagram:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Interface line */}
                            <line x1="200" y1="50" x2="200" y2="250" stroke="black" strokeWidth="2" />
                            <text x="210" y="150" className="text-xs">Interface</text>
                            
                            {/* Medium labels */}
                            <text x="100" y="30" className="text-sm font-bold">Medium 1 (n₁ = {formatNumber(refractiveIndex1)})</text>
                            <text x="250" y="30" className="text-sm font-bold">Medium 2 (n₂ = {formatNumber(refractiveIndex2)})</text>
                            
                            {/* Normal line */}
                            <line x1="200" y1="50" x2="200" y2="250" stroke="red" strokeWidth="1" strokeDasharray="5,5" />
                            <text x="190" y="150" className="text-xs text-red-600">Normal</text>
                            
                            {opticsType === 'reflection' && (
                                <>
                                    {/* Incident ray */}
                                    <line x1="50" y1="150" x2="200" y2="150" stroke="blue" strokeWidth="2" />
                                    <path d="M 180 150 L 185 145 L 185 155 Z" fill="blue" />
                                    <text x="120" y="140" className="text-xs text-blue-600">Incident Ray</text>
                                    
                                    {/* Reflected ray */}
                                    <line x1="200" y1="150" x2="350" y2="150" stroke="green" strokeWidth="2" />
                                    <path d="M 220 150 L 225 145 L 225 155 Z" fill="green" />
                                    <text x="280" y="140" className="text-xs text-green-600">Reflected Ray</text>
                                    
                                    {/* Angle markers */}
                                    <path d="M 200 150 A 30 30 0 0 1 173 135" fill="none" stroke="blue" strokeWidth="1" />
                                    <text x="180" y="130" className="text-xs text-blue-600">θi = {formatNumber(incidentAngle)}°</text>
                                    
                                    <path d="M 200 150 A 30 30 0 0 1 227 135" fill="none" stroke="green" strokeWidth="1" />
                                    <text x="220" y="130" className="text-xs text-green-600">θr = {formatNumber(results.reflectedAngle)}°</text>
                                </>
                            )}
                            
                            {opticsType === 'refraction' && (
                                <>
                                    {/* Incident ray */}
                                    <line x1="50" y1="150" x2="200" y2="150" stroke="blue" strokeWidth="2" />
                                    <path d="M 180 150 L 185 145 L 185 155 Z" fill="blue" />
                                    <text x="120" y="140" className="text-xs text-blue-600">Incident Ray</text>
                                    
                                    {/* Refracted ray */}
                                    {!results.totalInternalReflection ? (
                                        <>
                                            <line x1="200" y1="150" x2="350" y2={150 + 100 * Math.tan(results.refractedAngleRad)} stroke="green" strokeWidth="2" />
                                            <path d="M 220 150 L 225 145 L 225 155 Z" fill="green" />
                                            <text x="280" y="160" className="text-xs text-green-600">Refracted Ray</text>
                                            
                                            {/* Angle markers */}
                                            <path d="M 200 150 A 30 30 0 0 1 173 135" fill="none" stroke="blue" strokeWidth="1" />
                                            <text x="180" y="130" className="text-xs text-blue-600">θi = {formatNumber(incidentAngle)}°</text>
                                            
                                            <path d="M 200 150 A 30 30 0 0 1 227 {135 + 100 * Math.tan(results.refractedAngleRad)}" fill="none" stroke="green" strokeWidth="1" />
                                            <text x="220" y="130" className="text-xs text-green-600">θr = {formatNumber(results.refractedAngle)}°</text>
                                        </>
                                    ) : (
                                        <>
                                            <line x1="200" y1="150" x2="200" y2="50" stroke="red" strokeWidth="2" />
                                            <path d="M 200 70 L 195 75 L 205 75 Z" fill="red" />
                                            <text x="210" y="100" className="text-xs text-red-600">Total Internal Reflection</text>
                                        </>
                                    )}
                                </>
                            )}
                        </svg>
                    </div>
                </div>
            )}

            {/* Lens/Mirror Diagram */}
            {showLensMirror && (opticsType === 'lens' || opticsType === 'mirror') && (
                <div className="mb-6 p-4 bg-green-50 rounded-lg border border-green-200">
                    <h4 className="text-md font-medium text-green-800 mb-3">Lens/Mirror Ray Diagram:</h4>
                    <div className="h-80 bg-white rounded border p-4">
                        <svg className="w-full h-full" viewBox="0 0 400 300">
                            {/* Optical axis */}
                            <line x1="50" y1="150" x2="350" y2="150" stroke="black" strokeWidth="1" />
                            
                            {/* Lens/Mirror */}
                            {opticsType === 'lens' ? (
                                <>
                                    {/* Lens */}
                                    <ellipse cx="200" cy="150" rx="8" ry="80" fill="none" stroke="blue" strokeWidth="3" />
                                    <ellipse cx="200" cy="150" rx="4" ry="40" fill="none" stroke="blue" strokeWidth="3" />
                                    <text x="210" y="80" className="text-sm text-blue-600">Converging Lens</text>
                                </>
                            ) : (
                                <>
                                    {/* Mirror */}
                                    <path d="M 200 70 Q 180 150 200 230" fill="none" stroke="purple" strokeWidth="3" />
                                    <text x="210" y="80" className="text-sm text-purple-600">Concave Mirror</text>
                                </>
                            )}
                            
                            {/* Focal points */}
                            <circle cx={200 - focalLength * 2} cy="150" r="3" fill="red" />
                            <text x={200 - focalLength * 2 - 10} y="140" className="text-xs text-red-600">F</text>
                            <circle cx={200 + focalLength * 2} cy="150" r="3" fill="red" />
                            <text x={200 + focalLength * 2 - 5} y="140" className="text-xs text-red-600">F'</text>
                            
                            {/* Object */}
                            <line x1={200 - objectDistance * 2} y1="150" x2={200 - objectDistance * 2} y2={150 - objectHeight * 2} stroke="black" strokeWidth="2" />
                            <text x={200 - objectDistance * 2 - 15} y="150" className="text-xs">Object</text>
                            
                            {/* Image */}
                            {Math.abs(results.imageDistance) < 100 && (
                                <>
                                    <line x1={200 + results.imageDistance * 2} y1="150" x2={200 + results.imageDistance * 2} y2={150 - results.imageHeight * 2} stroke="green" strokeWidth="2" />
                                    <text x={200 + results.imageDistance * 2 - 15} y="150" className="text-xs text-green-600">Image</text>
                                </>
                            )}
                            
                            {/* Ray 1: Parallel to axis */}
                            <line x1={200 - objectDistance * 2} y1={150 - objectHeight * 2} x2="200" y2={150 - objectHeight * 2} stroke="orange" strokeWidth="1" />
                            <line x1="200" y1={150 - objectHeight * 2} x2={200 + focalLength * 4} y2={150 - objectHeight * 2 - focalLength * 2} stroke="orange" strokeWidth="1" />
                            
                            {/* Ray 2: Through focal point */}
                            <line x1={200 - objectDistance * 2} y1={150 - objectHeight * 2} x2="200" y2={150 - objectHeight * 2 - (objectDistance - focalLength) * 2} stroke="red" strokeWidth="1" />
                            <line x1="200" y1={150 - objectHeight * 2 - (objectDistance - focalLength) * 2} x2={200 + focalLength * 4} y2={150 - objectHeight * 2} stroke="red" strokeWidth="1" />
                            
                            {/* Ray 3: Through center */}
                            <line x1={200 - objectDistance * 2} y1={150 - objectHeight * 2} x2={200 + results.imageDistance * 2} y2={150 - results.imageHeight * 2} stroke="blue" strokeWidth="1" />
                        </svg>
                    </div>
                </div>
            )}

            {/* Detailed Calculations */}
            {showCalculations && (
                <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                    <h4 className="text-md font-medium text-yellow-800 mb-3">Detailed Calculations:</h4>
                    <div className="space-y-3 text-sm text-yellow-700">
                        {opticsType === 'reflection' && (
                            <>
                                <div><strong>Law of Reflection:</strong> θi = θr</div>
                                <div>• Incident Angle: θi = {formatNumber(incidentAngle)}°</div>
                                <div>• Reflected Angle: θr = θi = {formatNumber(incidentAngle)}°</div>
                                <div>• Incident Angle (rad): θi = {formatNumber(incidentAngle)}° × π/180° = {formatNumber(results.incidentAngleRad)} rad</div>
                                <div>• Reflected Angle (rad): θr = {formatNumber(results.reflectedAngleRad)} rad</div>
                            </>
                        )}
                        
                        {opticsType === 'refraction' && (
                            <>
                                <div><strong>Snell's Law:</strong> n₁sin(θi) = n₂sin(θr)</div>
                                <div>• Incident Angle: θi = {formatNumber(incidentAngle)}° = {formatNumber(results.incidentAngleRad)} rad</div>
                                <div>• Medium 1 Index: n₁ = {formatNumber(refractiveIndex1)}</div>
                                <div>• Medium 2 Index: n₂ = {formatNumber(refractiveIndex2)}</div>
                                <div>• sin(θr) = (n₁/n₂) × sin(θi) = ({formatNumber(refractiveIndex1)}/{formatNumber(refractiveIndex2)}) × sin({formatNumber(results.incidentAngleRad)})</div>
                                <div>• sin(θr) = {formatNumber(refractiveIndex1/refractiveIndex2)} × {formatNumber(Math.sin(results.incidentAngleRad))} = {formatNumber((refractiveIndex1/refractiveIndex2) * Math.sin(results.incidentAngleRad))}</div>
                                <div>• Refracted Angle: θr = arcsin({formatNumber((refractiveIndex1/refractiveIndex2) * Math.sin(results.incidentAngleRad))}) = {formatNumber(results.refractedAngle)}°</div>
                                <div>• Critical Angle: θc = arcsin(n₂/n₁) = arcsin({formatNumber(refractiveIndex2/refractiveIndex1)}) = {formatNumber(results.criticalAngle)}°</div>
                                <div>• Total Internal Reflection: {results.totalInternalReflection ? 'Yes (θi > θc)' : 'No (θi < θc)'}</div>
                            </>
                        )}
                        
                        {(opticsType === 'lens' || opticsType === 'mirror') && (
                            <>
                                <div><strong>Thin Lens/Mirror Equation:</strong> 1/f = 1/do + 1/di</div>
                                <div>• Focal Length: f = {formatNumber(focalLength)} cm</div>
                                <div>• Object Distance: do = {formatNumber(objectDistance)} cm</div>
                                <div>• 1/di = 1/f - 1/do = 1/{formatNumber(focalLength)} - 1/{formatNumber(objectDistance)}</div>
                                <div>• 1/di = {formatNumber(1/focalLength)} - {formatNumber(1/objectDistance)} = {formatNumber(1/focalLength - 1/objectDistance)}</div>
                                <div>• Image Distance: di = 1/{formatNumber(1/focalLength - 1/objectDistance)} = {formatNumber(results.imageDistance)} cm</div>
                                <div>• Magnification: M = -di/do = -{formatNumber(results.imageDistance)}/{formatNumber(objectDistance)} = {formatNumber(results.magnification)}</div>
                                <div>• Image Height: hi = ho × M = {formatNumber(objectHeight)} × {formatNumber(results.magnification)} = {formatNumber(results.imageHeight)} cm</div>
                                <div>• Image Type: {results.isVirtual ? 'Virtual (di < 0)' : 'Real (di > 0)'}</div>
                                <div>• Orientation: {results.isUpright ? 'Upright (M > 0)' : 'Inverted (M < 0)'}</div>
                            </>
                        )}
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Reflection: Angle of incidence equals angle of reflection</li>
                    <li>• Refraction: Light bends according to Snell's Law (n₁sin(θi) = n₂sin(θr))</li>
                    <li>• Total internal reflection occurs when light travels from higher to lower index</li>
                    <li>• Lens/Mirror equation: 1/f = 1/do + 1/di</li>
                    <li>• Magnification: M = -di/do = hi/ho</li>
                    <li>• Real images form on opposite side, virtual images on same side</li>
                    <li>• Positive magnification means upright, negative means inverted</li>
                </ul>
            </div>
        </div>
    );
};

export default OpticsSimulator;
