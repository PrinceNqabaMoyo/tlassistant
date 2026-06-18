import React, { useState, useEffect } from 'react';

const TrigonometricFunctionInput = ({ initialData, onChange, isSubmitted }) => {
    const [funcType, setFuncType] = useState(initialData.func_type || 'sin');
    const [A, setA] = useState(initialData.A || '');
    const [B, setB] = useState(initialData.B || '');
    const [C, setC] = useState(initialData.C || '');
    const [D, setD] = useState(initialData.D || '');
    const [xMin, setXMin] = useState(initialData.x_range ? initialData.x_range[0] : '0');
    const [xMax, setXMax] = useState(initialData.x_range ? initialData.x_range[1] : '360');
    const [title, setTitle] = useState(initialData.title || '');
    const [showPreview, setShowPreview] = useState(false);
    const [lineColor, setLineColor] = useState(initialData.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData.showGrid !== false);
    const [showPoints, setShowPoints] = useState(initialData.showPoints !== false);
    const [showAmplitude, setShowAmplitude] = useState(initialData.showAmplitude !== false);
    const [showPeriod, setShowPeriod] = useState(initialData.showPeriod !== false);
    const [angleUnit, setAngleUnit] = useState(initialData.angleUnit || 'degrees'); // 'degrees' or 'pi'

    // Calculate trigonometric properties
    const aNum = Number(A) || 0;
    const bNum = Number(B) || 1;
    const cNum = Number(C) || 0;
    const dNum = Number(D) || 0;
    
    // Mathematical properties
    const amplitude = Math.abs(aNum);
    const period = bNum !== 0 ? (angleUnit === 'degrees' ? 360 / Math.abs(bNum) : (2 * Math.PI) / Math.abs(bNum)) : 0;
    const phaseShift = bNum !== 0 ? -cNum / bNum : 0;
    const verticalShift = dNum;
    const frequency = bNum !== 0 ? Math.abs(bNum) / (angleUnit === 'degrees' ? 360 : 2 * Math.PI) : 0;
    const hasValidFunction = bNum !== 0;

    useEffect(() => {
        const formattedData = {
            type: "trigonometric_function",
            title: title,
            func_type: funcType,
            A: aNum,
            B: bNum,
            C: cNum,
            D: dNum,
            x_range: [Number(xMin) || 0, Number(xMax) || (angleUnit === 'degrees' ? 360 : 2 * Math.PI)],
            lineColor: lineColor,
            showGrid: showGrid,
            showPoints: showPoints,
            showAmplitude: showAmplitude,
            showPeriod: showPeriod,
            angleUnit: angleUnit
        };
        onChange(formattedData);
    }, [funcType, A, B, C, D, xMin, xMax, title, lineColor, showGrid, showPoints, showAmplitude, showPeriod, angleUnit, onChange]);

    const generatePoints = () => {
        const points = [];
        const step = (Number(xMax) - Number(xMin)) / 200;
        for (let x = Number(xMin); x <= Number(xMax); x += step) {
            let y;
            // Convert to radians if using degrees
            const xRad = angleUnit === 'degrees' ? (x * Math.PI) / 180 : x;
            const cRad = angleUnit === 'degrees' ? (cNum * Math.PI) / 180 : cNum;
            
            switch (funcType) {
                case 'sin':
                    y = aNum * Math.sin(bNum * xRad + cRad) + dNum;
                    break;
                case 'cos':
                    y = aNum * Math.cos(bNum * xRad + cRad) + dNum;
                    break;
                case 'tan':
                    y = aNum * Math.tan(bNum * xRad + cRad) + dNum;
                    break;
                default:
                    y = 0;
            }
            if (isFinite(y) && Math.abs(y) < 1000) { // Filter out extreme values
                points.push({ x: x, y: y });
            }
        }
        return points;
    };

    const getFunctionBehavior = () => {
        if (aNum === 0) return 'Constant function (horizontal line)';
        if (funcType === 'tan' && bNum !== 0) return 'Tangent function with asymptotes';
        return `${funcType.charAt(0).toUpperCase() + funcType.slice(1)} function`;
    };

    const getSymmetry = () => {
        if (aNum === 0) return 'None (constant function)';
        if (funcType === 'sin') return 'Origin symmetry (odd function)';
        if (funcType === 'cos') return 'Y-axis symmetry (even function)';
        if (funcType === 'tan') return 'Origin symmetry (odd function)';
        return 'Varies by function type';
    };

    const getDomain = () => {
        if (funcType === 'tan') {
            if (angleUnit === 'degrees') {
                return `x ≠ ${phaseShift.toFixed(2)} + 90° + n·180° (n ∈ ℤ)`;
            } else {
                return `x ≠ ${phaseShift.toFixed(2)} + π/2 + nπ (n ∈ ℤ)`;
            }
        }
        return 'All real numbers';
    };

    const getRange = () => {
        if (aNum === 0) return `y = ${dNum}`;
        if (funcType === 'tan') return 'All real numbers';
        return `[${dNum - amplitude}, ${dNum + amplitude}]`;
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Trigonometric Function Builder</h3>
                <button
                    onClick={() => setShowPreview(!showPreview)}
                    className={`px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
                        showPreview 
                            ? 'bg-blue-100 text-blue-700 hover:bg-blue-200' 
                            : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                    }`}
                >
                    {showPreview ? 'Hide Preview' : 'Show Preview'}
                </button>
            </div>

            {/* Chart Configuration */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-6">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Chart Title:</label>
                    <input 
                        type="text" 
                        className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                        value={title} 
                        onChange={(e) => !isSubmitted && setTitle(e.target.value)} 
                        disabled={isSubmitted} 
                        placeholder="e.g., Trigonometric Function Analysis" 
                    />
                </div>
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">Line Color:</label>
                    <input 
                        type="color" 
                        className="w-full h-12 border border-gray-300 rounded-lg cursor-pointer" 
                        value={lineColor} 
                        onChange={(e) => !isSubmitted && setLineColor(e.target.value)} 
                        disabled={isSubmitted} 
                    />
                </div>
            </div>

            {/* Function Type Selection */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <h4 className="text-md font-medium text-gray-800 mb-4">Function Type</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">Function Type:</label>
                        <select 
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={funcType} 
                            onChange={e => !isSubmitted && setFuncType(e.target.value)} 
                            disabled={isSubmitted}
                        >
                            <option value="sin">Sine (sin)</option>
                            <option value="cos">Cosine (cos)</option>
                            <option value="tan">Tangent (tan)</option>
                        </select>
                        <p className="text-xs text-gray-500 mt-1">Choose the base function</p>
                    </div>
                </div>
            </div>

            {/* Function Parameters */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <h4 className="text-md font-medium text-gray-800 mb-4">Function Parameters: y = A·func(Bx + C) + D</h4>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">A (Amplitude):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={A} 
                            onChange={e => !isSubmitted && setA(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 1" 
                        />
                        <p className="text-xs text-gray-500 mt-1">Controls the height of the wave</p>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">B (Frequency):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={B} 
                            onChange={e => !isSubmitted && setB(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 1" 
                        />
                        <p className="text-xs text-gray-500 mt-1">Controls the period (must be non-zero)</p>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">C (Phase Shift):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={C} 
                            onChange={e => !isSubmitted && setC(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 0" 
                        />
                        <p className="text-xs text-gray-500 mt-1">Shifts the function horizontally</p>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">D (Vertical Shift):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={D} 
                            onChange={e => !isSubmitted && setD(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 0" 
                        />
                        <p className="text-xs text-gray-500 mt-1">Shifts the function vertically</p>
                    </div>
                </div>
            </div>

            {/* Display Range */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <h4 className="text-md font-medium text-gray-800 mb-4">Display Range</h4>
                
                {/* Angle Unit Toggle */}
                <div className="mb-4">
                    <label className="block text-sm font-medium text-gray-700 mb-2">X-Axis Angle Unit:</label>
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input 
                                type="radio" 
                                name="angleUnit" 
                                value="degrees"
                                checked={angleUnit === 'degrees'} 
                                onChange={(e) => !isSubmitted && setAngleUnit(e.target.value)} 
                                disabled={isSubmitted}
                                className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300"
                            />
                            <span className="text-sm text-gray-700">Degrees (0° to 360°)</span>
                        </label>
                        <label className="flex items-center">
                            <input 
                                type="radio" 
                                name="angleUnit" 
                                value="pi"
                                checked={angleUnit === 'pi'} 
                                onChange={(e) => !isSubmitted && setAngleUnit(e.target.value)} 
                                disabled={isSubmitted}
                                className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300"
                            />
                            <span className="text-sm text-gray-700">Radians (0 to 2π)</span>
                        </label>
                    </div>
                </div>
                
                <div className="grid grid-cols-2 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">X-Range Minimum:</label>
                        <input 
                            type="number" 
                            step={angleUnit === 'degrees' ? '1' : '0.5'}
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMin} 
                            onChange={e => !isSubmitted && setXMin(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder={angleUnit === 'degrees' ? '0' : '0'} 
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">X-Range Maximum:</label>
                        <input 
                            type="number" 
                            step={angleUnit === 'degrees' ? '1' : '0.5'}
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMax} 
                            onChange={e => !isSubmitted && setXMax(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder={angleUnit === 'degrees' ? '360' : `${2 * Math.PI}`} 
                        />
                    </div>
                </div>
                <p className="text-xs text-blue-600 mt-2 font-medium">
                    💡 Tip: {angleUnit === 'degrees' 
                        ? 'Use multiples of 90° for better visualization of periodic behavior.' 
                        : 'Use multiples of π for better visualization of periodic behavior.'}
                </p>
            </div>

            {/* Display Options */}
            <div className="grid grid-cols-2 md:grid-cols-5 gap-4 mb-6">
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showGrid} 
                            onChange={(e) => !isSubmitted && setShowGrid(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Grid</span>
                    </label>
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showPoints} 
                            onChange={(e) => !isSubmitted && setShowPoints(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Points</span>
                    </label>
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showAmplitude} 
                            onChange={(e) => !isSubmitted && setShowAmplitude(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Amplitude</span>
                    </label>
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showPeriod} 
                            onChange={(e) => !isSubmitted && setShowPeriod(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Period</span>
                    </label>
                </div>
            </div>

            {/* Mathematical Analysis */}
            {hasValidFunction && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6 p-4 bg-purple-50 rounded-lg">
                    <div className="text-center">
                        <div className="text-2xl font-bold text-purple-600">{amplitude.toFixed(2)}</div>
                        <div className="text-sm text-purple-700">Amplitude</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{period.toFixed(2)}</div>
                        <div className="text-sm text-blue-700">Period</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-green-600">{phaseShift.toFixed(2)}</div>
                        <div className="text-sm text-green-700">Phase Shift</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-orange-600">{frequency.toFixed(2)}</div>
                        <div className="text-sm text-orange-700">Frequency</div>
                    </div>
                </div>
            )}

            {/* Detailed Analysis */}
            {hasValidFunction && (
                <div className="bg-gray-50 rounded-lg p-4 mb-6">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Detailed Analysis</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                        <div>
                            <p><strong>Function Behavior:</strong> {getFunctionBehavior()}</p>
                            <p><strong>Symmetry:</strong> {getSymmetry()}</p>
                            <p><strong>Domain:</strong> {getDomain()}</p>
                            <p><strong>Range:</strong> {getRange()}</p>
                        </div>
                        <div>
                            <p><strong>Function:</strong> y = {aNum !== 1 ? aNum : ''}{funcType}({bNum !== 1 ? bNum : ''}x {cNum >= 0 ? '+' : ''}{cNum !== 0 ? cNum : ''}) {dNum >= 0 ? '+' : ''}{dNum !== 0 ? dNum : ''}</p>
                            <p><strong>Vertical Shift:</strong> {verticalShift}</p>
                            <p><strong>Horizontal Shift:</strong> {phaseShift.toFixed(2)}</p>
                            <p><strong>Cycles in Range:</strong> {((Number(xMax) - Number(xMin)) / period).toFixed(1)}</p>
                        </div>
                    </div>
                </div>
            )}

            {/* Interactive Chart Preview */}
            {showPreview && hasValidFunction && (
                <div className="border border-gray-200 rounded-lg p-6 bg-white">
                    <h4 className="text-lg font-medium text-gray-800 mb-4">Function Preview</h4>
                    <div className="h-64 border border-gray-200 rounded-lg bg-gray-50 p-4 relative">
                        {/* Grid Lines */}
                        {showGrid && (
                            <div className="absolute inset-0 pointer-events-none">
                                {Array.from({ length: 11 }, (_, i) => (
                                    <div key={i} className="absolute w-full h-px bg-gray-200" style={{ top: `${i * 10}%` }}></div>
                                ))}
                                {Array.from({ length: 11 }, (_, i) => (
                                    <div key={i} className="absolute h-full w-px bg-gray-200" style={{ left: `${i * 10}%` }}></div>
                                ))}
                            </div>
                        )}
                        
                        {/* Trigonometric Function */}
                        <svg className="w-full h-full absolute inset-0" viewBox="0 0 100 100" preserveAspectRatio="none">
                            {(() => {
                                const points = generatePoints();
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                const yValues = points.map(p => p.y);
                                const yMin = Math.min(...yValues);
                                const yMax = Math.max(...yValues);
                                
                                const pathData = points.map((point, index) => {
                                    const x = ((point.x - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                    const y = 100 - ((point.y - yMin) / (yMax - yMin)) * 100;
                                    return `${index === 0 ? 'M' : 'L'} ${x} ${y}`;
                                }).join(' ');
                                
                                return (
                                    <path
                                        d={pathData}
                                        fill="none"
                                        stroke={lineColor}
                                        strokeWidth="2"
                                    />
                                );
                            })()}
                            
                            {/* Amplitude Lines */}
                            {showAmplitude && amplitude > 0 && (() => {
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                const yValues = generatePoints().map(p => p.y);
                                const yMin = Math.min(...yValues);
                                const yMax = Math.max(...yValues);
                                
                                const upperY = 100 - ((verticalShift + amplitude - yMin) / (yMax - yMin)) * 100;
                                const lowerY = 100 - ((verticalShift - amplitude - yMin) / (yMax - yMin)) * 100;
                                
                                return (
                                    <>
                                        <line
                                            x1="0"
                                            y1={upperY}
                                            x2="100"
                                            y2={upperY}
                                            stroke="green"
                                            strokeWidth="1"
                                            strokeDasharray="3,3"
                                        />
                                        <line
                                            x1="0"
                                            y1={lowerY}
                                            x2="100"
                                            y2={lowerY}
                                            stroke="green"
                                            strokeWidth="1"
                                            strokeDasharray="3,3"
                                        />
                                    </>
                                );
                            })()}
                            
                            {/* Period Lines */}
                            {showPeriod && period > 0 && (() => {
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                
                                // Show one complete period
                                const periodStart = phaseShift;
                                const periodEnd = phaseShift + period;
                                
                                const startX = ((periodStart - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                const endX = ((periodEnd - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                
                                if (startX >= 0 && startX <= 100) {
                                    return (
                                        <line
                                            x1={startX}
                                            y1="0"
                                            x2={startX}
                                            y2="100"
                                            stroke="orange"
                                            strokeWidth="1"
                                            strokeDasharray="5,5"
                                        />
                                    );
                                }
                                if (endX >= 0 && endX <= 100) {
                                    return (
                                        <line
                                            x1={endX}
                                            y1="0"
                                            x2={endX}
                                            y2="100"
                                            stroke="orange"
                                            strokeWidth="1"
                                            strokeDasharray="5,5"
                                        />
                                    );
                                }
                                return null;
                            })()}
                            
                            {/* Data Points */}
                            {showPoints && generatePoints().map((point, index) => {
                                if (index % 20 !== 0) return null; // Show every 20th point to avoid clutter
                                
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                const yValues = generatePoints().map(p => p.y);
                                const yMin = Math.min(...yValues);
                                const yMax = Math.max(...yValues);
                                
                                const x = ((point.x - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                const y = 100 - ((point.y - yMin) / (yMax - yMin)) * 100;
                                
                                if (x >= 0 && x <= 100 && y >= 0 && y <= 100) {
                                    return (
                                        <circle
                                            key={index}
                                            cx={x}
                                            cy={y}
                                            r="1.5"
                                            fill={lineColor}
                                            stroke="white"
                                            strokeWidth="0.5"
                                        />
                                    );
                                }
                                return null;
                            })}
                        </svg>
                        
                        {/* Axis Labels */}
                        <div className="absolute bottom-0 left-0 right-0 text-center text-xs text-gray-500">
                            X-Axis
                        </div>
                        <div className="absolute top-0 bottom-0 left-0 text-center text-xs text-gray-500 transform -rotate-90 origin-center">
                            Y-Axis
                        </div>
                    </div>
                </div>
            )}

            {/* Help Text */}
            <div className="mt-6 p-4 bg-gray-50 rounded-lg">
                <h4 className="text-sm font-medium text-gray-800 mb-2">💡 Tips:</h4>
                <ul className="text-sm text-gray-600 space-y-1">
                    <li>• Amplitude (A) controls the height of the wave</li>
                    <li>• Frequency (B) controls how many cycles occur in {angleUnit === 'degrees' ? '360°' : '2π'} units</li>
                    <li>• Phase shift (C) moves the function left or right</li>
                    <li>• Vertical shift (D) moves the function up or down</li>
                    <li>• Toggle between degrees and radians for the x-axis</li>
                    <li>• Use the preview to see how parameters affect the graph</li>
                </ul>
            </div>
        </div>
    );
};

export default TrigonometricFunctionInput;
