import React, { useState, useEffect } from 'react';

const CircleInput = ({ initialData, onChange, isSubmitted }) => {
    const [h, setH] = useState(initialData.h || '');
    const [k, setK] = useState(initialData.k || '');
    const [r, setR] = useState(initialData.r || '');
    const [xMin, setXMin] = useState(initialData.x_range ? initialData.x_range[0] : '-10');
    const [xMax, setXMax] = useState(initialData.x_range ? initialData.x_range[1] : '10');
    const [title, setTitle] = useState(initialData.title || '');
    const [showPreview, setShowPreview] = useState(false);
    const [lineColor, setLineColor] = useState(initialData.lineColor || '#3B82F6');
    const [showGrid, setShowGrid] = useState(initialData.showGrid !== false);
    const [showCenter, setShowCenter] = useState(initialData.showCenter !== false);
    const [showRadius, setShowRadius] = useState(initialData.showRadius !== false);

    // Calculate circle properties
    const hNum = Number(h) || 0;
    const kNum = Number(k) || 0;
    const rNum = Number(r) || 0;
    
    // Mathematical properties
    const area = Math.PI * rNum * rNum;
    const circumference = 2 * Math.PI * rNum;
    const diameter = 2 * rNum;
    const hasValidCircle = rNum > 0;

    useEffect(() => {
        const formattedData = {
            type: "circle",
            title: title,
            h: hNum,
            k: kNum,
            r: rNum,
            x_range: [Number(xMin) || -10, Number(xMax) || 10],
            lineColor: lineColor,
            showGrid: showGrid,
            showCenter: showCenter,
            showRadius: showRadius
        };
        onChange(formattedData);
    }, [h, k, r, xMin, xMax, title, lineColor, showGrid, showCenter, showRadius, onChange]);

    const generatePoints = () => {
        const points = [];
        const step = (Number(xMax) - Number(xMin)) / 200;
        for (let x = Number(xMin); x <= Number(xMax); x += step) {
            // Calculate y values for the circle equation: (x-h)² + (y-k)² = r²
            const discriminant = rNum * rNum - (x - hNum) * (x - hNum);
            if (discriminant >= 0) {
                const y1 = kNum + Math.sqrt(discriminant);
                const y2 = kNum - Math.sqrt(discriminant);
                if (isFinite(y1)) points.push({ x: x, y: y1 });
                if (isFinite(y2)) points.push({ x: x, y: y2 });
            }
        }
        return points;
    };

    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            <div className="flex items-center justify-between mb-6">
                <h3 className="text-lg font-semibold text-gray-800">Circle Builder</h3>
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
                        placeholder="e.g., Circle Analysis" 
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

            {/* Function Parameters */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <h4 className="text-md font-medium text-gray-800 mb-4">Circle Parameters: (x - h)² + (y - k)² = r²</h4>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">h (X-coordinate of center):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={h} 
                            onChange={(e) => !isSubmitted && setH(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 0" 
                        />
                        <p className="text-xs text-gray-500 mt-1">X-coordinate of the circle's center</p>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">k (Y-coordinate of center):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={k} 
                            onChange={(e) => !isSubmitted && setK(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 0" 
                        />
                        <p className="text-xs text-gray-500 mt-1">Y-coordinate of the circle's center</p>
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">r (Radius):</label>
                        <input 
                            type="number" 
                            step="0.1"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={r} 
                            onChange={(e) => !isSubmitted && setR(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="e.g., 5" 
                        />
                        <p className="text-xs text-gray-500 mt-1">Radius of the circle (must be positive)</p>
                    </div>
                </div>
            </div>

            {/* Display Range */}
            <div className="bg-gray-50 rounded-lg p-4 mb-6">
                <h4 className="text-md font-medium text-gray-800 mb-4">Display Range</h4>
                <div className="grid grid-cols-2 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">X-Range Minimum:</label>
                        <input 
                            type="number" 
                            step="0.5"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMin} 
                            onChange={(e) => !isSubmitted && setXMin(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="-10" 
                        />
                    </div>
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-2">X-Range Maximum:</label>
                        <input 
                            type="number" 
                            step="0.5"
                            className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors" 
                            value={xMax} 
                            onChange={(e) => !isSubmitted && setXMax(e.target.value)} 
                            disabled={isSubmitted} 
                            placeholder="10" 
                        />
                    </div>
                </div>
                <p className="text-xs text-blue-600 mt-2 font-medium">💡 Tip: Adjust range to see the entire circle clearly.</p>
            </div>

            {/* Display Options */}
            <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
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
                            checked={showCenter} 
                            onChange={(e) => !isSubmitted && setShowCenter(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Center</span>
                    </label>
                </div>
                <div className="flex items-center space-x-3">
                    <label className="flex items-center">
                        <input 
                            type="checkbox" 
                            className="mr-2 h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded" 
                            checked={showRadius} 
                            onChange={(e) => !isSubmitted && setShowRadius(e.target.checked)} 
                            disabled={isSubmitted} 
                        />
                        <span className="text-sm text-gray-700">Radius</span>
                    </label>
                </div>
            </div>

            {/* Mathematical Analysis */}
            {hasValidCircle && (
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6 p-4 bg-green-50 rounded-lg">
                    <div className="text-center">
                        <div className="text-2xl font-bold text-green-600">{rNum.toFixed(2)}</div>
                        <div className="text-sm text-green-700">Radius</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-blue-600">{diameter.toFixed(2)}</div>
                        <div className="text-sm text-blue-700">Diameter</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-purple-600">{area.toFixed(2)}</div>
                        <div className="text-sm text-purple-700">Area</div>
                    </div>
                    <div className="text-center">
                        <div className="text-2xl font-bold text-orange-600">{circumference.toFixed(2)}</div>
                        <div className="text-sm text-orange-700">Circumference</div>
                    </div>
                </div>
            )}

            {/* Detailed Analysis */}
            {hasValidCircle && (
                <div className="bg-gray-50 rounded-lg p-4 mb-6">
                    <h4 className="text-md font-medium text-gray-800 mb-3">Detailed Analysis</h4>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
                        <div>
                            <p><strong>Standard Form:</strong> (x - {hNum})² + (y - {kNum})² = {rNum}²</p>
                            <p><strong>Center:</strong> ({hNum}, {kNum})</p>
                            <p><strong>Radius:</strong> {rNum}</p>
                            <p><strong>Diameter:</strong> {diameter}</p>
                        </div>
                        <div>
                            <p><strong>Area:</strong> π × {rNum}² = {area.toFixed(2)}</p>
                            <p><strong>Circumference:</strong> 2π × {rNum} = {circumference.toFixed(2)}</p>
                            <p><strong>Domain:</strong> [{hNum - rNum}, {hNum + rNum}]</p>
                            <p><strong>Range:</strong> [{kNum - rNum}, {kNum + rNum}]</p>
                        </div>
                    </div>
                </div>
            )}

            {/* Interactive Chart Preview */}
            {showPreview && hasValidCircle && (
                <div className="border border-gray-200 rounded-lg p-6 bg-white">
                    <h4 className="text-lg font-medium text-gray-800 mb-4">Circle Preview</h4>
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
                        
                        {/* Circle */}
                        <svg className="w-full h-full absolute inset-0" viewBox="0 0 100 100" preserveAspectRatio="none">
                            {(() => {
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                const centerX = ((hNum - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                const centerY = 50; // Center vertically
                                const radiusPixels = (rNum / (xMaxNum - xMinNum)) * 100;
                                
                                return (
                                    <circle
                                        cx={centerX}
                                        cy={centerY}
                                        r={radiusPixels}
                                        fill="none"
                                        stroke={lineColor}
                                        strokeWidth="2"
                                    />
                                );
                            })()}
                            
                            {/* Center Point */}
                            {showCenter && (() => {
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                const centerX = ((hNum - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                const centerY = 50;
                                
                                if (centerX >= 0 && centerX <= 100) {
                                    return (
                                        <circle
                                            cx={centerX}
                                            cy={centerY}
                                            r="3"
                                            fill="red"
                                            stroke="white"
                                            strokeWidth="1"
                                        />
                                    );
                                }
                                return null;
                            })()}
                            
                            {/* Radius Line */}
                            {showRadius && (() => {
                                const xMinNum = Number(xMin);
                                const xMaxNum = Number(xMax);
                                const centerX = ((hNum - xMinNum) / (xMaxNum - xMinNum)) * 100;
                                const centerY = 50;
                                const radiusPixels = (rNum / (xMaxNum - xMinNum)) * 100;
                                
                                if (centerX >= 0 && centerX <= 100) {
                                    return (
                                        <line
                                            x1={centerX}
                                            y1={centerY}
                                            x2={centerX + radiusPixels}
                                            y2={centerY}
                                            stroke="orange"
                                            strokeWidth="2"
                                            strokeDasharray="3,3"
                                        />
                                    );
                                }
                                return null;
                            })()}
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
                    <li>• The center coordinates (h, k) determine where the circle is located</li>
                    <li>• The radius must be positive for a valid circle</li>
                    <li>• The standard form shows the relationship between any point (x, y) and the center</li>
                    <li>• Use the preview to visualize how parameters affect the circle</li>
                </ul>
            </div>
        </div>
    );
};

export default CircleInput;
