import React, { useState, useEffect, useRef, useCallback } from 'react';
import { Maximize2, RotateCcw, Grid3X3, TrendingUp, FunctionSquare } from 'lucide-react';
import FullScreenModal from '../ui/FullScreenModal';

const IntegratedExponentialLogarithmicFunction = ({ 
    initialData, 
    onChange, 
    isSubmitted 
}) => {
    // Core state management - simplified and organized
    const [functionType, setFunctionType] = useState(initialData?.functionType || 'exponential');
    const [parameters, setParameters] = useState({
        a: initialData?.a || 1,
        b: initialData?.b || 2,
        c: initialData?.c || 0,
        d: initialData?.d || 0
    });
    const [base, setBase] = useState(initialData?.base || 'e');
    const [customBase, setCustomBase] = useState(initialData?.customBase || 2);
    
    // View and display settings
    const [viewSettings, setViewSettings] = useState({
        xRange: initialData?.x_range || [-5, 5],
        yRange: initialData?.y_range || [-2, 10],
        showGrid: initialData?.showGrid !== false,
        showPoints: initialData?.showPoints !== false,
        showAsymptotes: initialData?.showAsymptotes !== false,
        lineColor: initialData?.lineColor || '#3B82F6'
    });
    
    // Inverse function settings
    const [inverseSettings, setInverseSettings] = useState({
        showInverse: initialData?.showInverse || false,
        showReflectionLine: initialData?.showReflectionLine || false,
        inverseLineColor: initialData?.inverseLineColor || '#10B981'
    });
    
    // Educational features
    const [educationalFeatures, setEducationalFeatures] = useState({
        showLawsDemonstrator: initialData?.showLawsDemonstrator || false,
        showFunctionProperties: initialData?.showFunctionProperties !== false,
        showInverseVisualizer: initialData?.showInverseVisualizer || false,
        currentLaw: initialData?.currentLaw || 'product'
    });

    // Advanced parameter controls
    const [showAdvancedParameters, setShowAdvancedParameters] = useState(false);
    

    
    // UI state
    const [editMode, setEditMode] = useState(initialData?.editMode || 'parameters');
    const [isFullScreenOpen, setIsFullScreenOpen] = useState(false);
    const [isFullScreen, setIsFullScreen] = useState(false);
    
    // Refs
    const canvasRef = useRef(null);
    const fullScreenCanvasRef = useRef(null);
    
    // Convert parameters to numbers for calculations
    const aNum = Number(parameters.a) || 0;
    const bNum = Number(parameters.b) || 0;
    const cNum = Number(parameters.c) || 0;
    const dNum = Number(parameters.d) || 0;
    const customBaseNum = Number(customBase) || 2;
    

    

    
    // Mathematical core functions
    const calculateFunctionValue = useCallback((x) => {
        if (functionType === 'exponential') {
            // y = a × b^(x + c) + d (or simplified when advanced params disabled)
            if (bNum <= 0) return null; // Invalid base
            const effectiveC = showAdvancedParameters ? cNum : 0;
            const effectiveD = showAdvancedParameters ? dNum : 0;
            return aNum * Math.pow(bNum, x + effectiveC) + effectiveD;
        } else {
            // y = a × log_b(x + c) + d (or simplified when advanced params disabled)
            const effectiveC = showAdvancedParameters ? cNum : 0;
            const effectiveD = showAdvancedParameters ? dNum : 0;
            if (x + effectiveC <= 0) return null; // Domain restriction
            
            let logValue;
            if (base === 'e') {
                logValue = Math.log(x + effectiveC);
            } else if (base === '2') {
                logValue = Math.log2(x + effectiveC);
            } else if (base === '10') {
                logValue = Math.log10(x + effectiveC);
            } else {
                logValue = Math.log(x + effectiveC) / Math.log(customBaseNum);
            }
            
            return aNum * logValue + effectiveD;
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, showAdvancedParameters]);
    
    // Calculate inverse function value
    const calculateInverseFunctionValue = useCallback((y) => {
        if (functionType === 'exponential') {
            // Original: y = a × b^(x + c) + d (or simplified when advanced params disabled)
            // Inverse: x = log_b((y - d) / a) - c
            const effectiveD = showAdvancedParameters ? dNum : 0;
            const effectiveC = showAdvancedParameters ? cNum : 0;
            if (aNum === 0 || (y - effectiveD) / aNum <= 0) return null;
            return Math.log((y - effectiveD) / aNum) / Math.log(bNum) - effectiveC;
        } else {
            // Original: y = a × log_b(x + c) + d (or simplified when advanced params disabled)
            // Inverse: x = b^((y - d) / a) - c
            const effectiveD = showAdvancedParameters ? dNum : 0;
            const effectiveC = showAdvancedParameters ? cNum : 0;
            if (aNum === 0) return null;
            const baseValue = base === 'e' ? Math.E : base === '2' ? 2 : base === '10' ? 10 : customBaseNum;
            return Math.pow(baseValue, (y - effectiveD) / aNum) - effectiveC;
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, showAdvancedParameters]);
    
    // Calculate function properties
    const calculateFunctionProperties = useCallback(() => {
        if (functionType === 'exponential') {
            const effectiveD = showAdvancedParameters ? dNum : 0;
            const effectiveC = showAdvancedParameters ? cNum : 0;
            return {
                domain: { min: -Infinity, max: Infinity },
                range: { 
                    min: bNum > 1 ? effectiveD : -Infinity, 
                    max: bNum > 1 ? Infinity : effectiveD 
                },
                asymptote: { 
                    horizontal: showAdvancedParameters && effectiveD !== 0 ? `y = ${effectiveD}` : null, 
                    vertical: null 
                },
                yIntercept: [0, aNum * Math.pow(bNum, effectiveC) + effectiveD],
                behavior: bNum > 1 ? 'Growth' : bNum > 0 ? 'Decay' : 'Invalid'
            };
        } else {
            const baseValue = base === 'e' ? Math.E : base === '2' ? 2 : base === '10' ? 10 : customBaseNum;
            const effectiveC = showAdvancedParameters ? cNum : 0;
            const effectiveD = showAdvancedParameters ? dNum : 0;
            return {
                domain: { min: -effectiveC, max: Infinity },
                range: { min: -Infinity, max: Infinity },
                asymptote: { 
                    horizontal: null, 
                    vertical: showAdvancedParameters && effectiveC !== 0 ? `x = ${-effectiveC}` : null 
                },
                yIntercept: effectiveC < 1 ? null : [1, aNum * Math.log(1 + effectiveC) / Math.log(baseValue) + effectiveD],
                behavior: aNum > 0 ? 'Increasing' : aNum < 0 ? 'Decreasing' : 'Constant'
            };
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, showAdvancedParameters]);
    
    // Get function string representation
    const getFunctionString = useCallback(() => {
        if (functionType === 'exponential') {
            let result = '';
            if (aNum !== 1) result += `${aNum} × `;
            result += `${bNum}<sup>x`;
            if (showAdvancedParameters && cNum !== 0) result += cNum > 0 ? ` + ${cNum}` : ` - ${Math.abs(cNum)}`;
            result += '</sup>';
            if (showAdvancedParameters && dNum !== 0) result += dNum > 0 ? ` + ${dNum}` : ` - ${Math.abs(dNum)}`;
            return result;
        } else {
            let result = '';
            if (aNum !== 1) result += `${aNum} × `;
            const baseText = base === 'e' ? 'e' : base === '2' ? '2' : base === '10' ? '10' : customBaseNum;
            result += `log<sub>${baseText}</sub>(x`;
            if (showAdvancedParameters && cNum !== 0) result += cNum > 0 ? ` + ${cNum}` : ` - ${Math.abs(cNum)}`;
            result += ')';
            if (showAdvancedParameters && dNum !== 0) result += dNum > 0 ? ` + ${dNum}` : ` - ${Math.abs(dNum)}`;
            return result;
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, showAdvancedParameters]);
    

    

    
    // Canvas drawing system
    const drawGraph = useCallback((targetCanvas = null) => {
        const canvas = targetCanvas || canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!ctx) return;

        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        const xRange = viewSettings.xRange;
        const yRange = viewSettings.yRange;

        // Calculate scale factors
        const xScale = width / (xRange[1] - xRange[0]);
        const yScale = height / (yRange[1] - yRange[0]);

        // Helper functions for coordinate conversion
        const toCanvasX = (x) => (x - xRange[0]) * xScale;
        const toCanvasY = (y) => height - (y - yRange[0]) * yScale;

        // Draw grid
        if (viewSettings.showGrid) {
            ctx.strokeStyle = '#D1D5DB';
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = xRange[0]; x <= xRange[1]; x += 0.5) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = yRange[0]; y <= yRange[1]; y += 1) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;

        // X-axis
        const xAxisY = toCanvasY(0);
        if (xAxisY >= 0 && xAxisY <= height) {
            ctx.beginPath();
            ctx.moveTo(0, xAxisY);
            ctx.lineTo(width, xAxisY);
            ctx.stroke();
        }

        // Y-axis
        const yAxisX = toCanvasX(0);
        if (yAxisX >= 0 && yAxisX <= width) {
            ctx.beginPath();
            ctx.moveTo(yAxisX, 0);
            ctx.lineTo(yAxisX, height);
            ctx.stroke();
        }

        // Draw main function
        ctx.strokeStyle = viewSettings.lineColor;
        ctx.lineWidth = 2;
        ctx.beginPath();

        let firstPoint = true;
        for (let x = xRange[0]; x <= xRange[1]; x += 0.01) {
            const y = calculateFunctionValue(x);
            
            if (y !== null && isFinite(y) && y >= yRange[0] && y <= yRange[1]) {
                const canvasX = toCanvasX(x);
                const canvasY = toCanvasY(y);
                
                if (firstPoint) {
                    ctx.moveTo(canvasX, canvasY);
                    firstPoint = false;
                } else {
                    ctx.lineTo(canvasX, canvasY);
                }
            }
        }
        
        ctx.stroke();

        // Draw inverse function if enabled
        if (inverseSettings.showInverse) {
            ctx.strokeStyle = inverseSettings.inverseLineColor;
            ctx.lineWidth = 2;
            ctx.setLineDash([3, 3]);
            ctx.beginPath();

            let firstInversePoint = true;
            for (let y = yRange[0]; y <= yRange[1]; y += 0.01) {
                const x = calculateInverseFunctionValue(y);
                
                if (x !== null && isFinite(x) && x >= xRange[0] && x <= xRange[1]) {
                    const canvasX = toCanvasX(x);
                    const canvasY = toCanvasY(y);
                    
                    if (firstInversePoint) {
                        ctx.moveTo(canvasX, canvasY);
                        firstInversePoint = false;
                    } else {
                        ctx.lineTo(canvasX, canvasY);
                    }
                }
            }
            
            ctx.stroke();
            ctx.setLineDash([]);
        }

        // Draw y=x reflection line if enabled
        if (inverseSettings.showReflectionLine) {
            ctx.strokeStyle = '#FFD700';
            ctx.lineWidth = 1;
            ctx.setLineDash([2, 2]);
            
            const startX = Math.max(xRange[0], yRange[0]);
            const endX = Math.min(xRange[1], yRange[1]);
            
            if (startX <= endX) {
                const startCanvasX = toCanvasX(startX);
                const startCanvasY = toCanvasY(startX);
                const endCanvasX = toCanvasX(endX);
                const endCanvasY = toCanvasY(endX);
                
                ctx.beginPath();
                ctx.moveTo(startCanvasX, startCanvasY);
                ctx.lineTo(endCanvasX, endCanvasY);
                ctx.stroke();
            }
            ctx.setLineDash([]);
        }

        // Draw asymptotes
        const properties = calculateFunctionProperties();
        if (properties.asymptote.horizontal) {
            ctx.strokeStyle = '#FF6B6B';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            const asymptoteY = toCanvasY(parseFloat(properties.asymptote.horizontal.split('=')[1]));
            if (asymptoteY >= 0 && asymptoteY <= height) {
                ctx.beginPath();
                ctx.moveTo(0, asymptoteY);
                ctx.lineTo(width, asymptoteY);
                ctx.stroke();
            }
            ctx.setLineDash([]);
        }

        if (properties.asymptote.vertical) {
            ctx.strokeStyle = '#FF6B6B';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            const asymptoteX = toCanvasX(parseFloat(properties.asymptote.vertical.split('=')[1]));
            if (asymptoteX >= 0 && asymptoteX <= width) {
                ctx.beginPath();
                ctx.moveTo(asymptoteX, 0);
                ctx.lineTo(asymptoteX, height);
                ctx.stroke();
            }
            ctx.setLineDash([]);
        }
    }, [functionType, aNum, bNum, cNum, dNum, base, customBaseNum, viewSettings, inverseSettings, calculateFunctionValue, calculateInverseFunctionValue, calculateFunctionProperties]);

    // Redraw graph when data changes
    useEffect(() => {
        const timer = setTimeout(() => {
            drawGraph();
        }, 100);
        return () => clearTimeout(timer);
    }, [functionType, parameters, base, customBase, viewSettings, inverseSettings, drawGraph]);

    // Initial draw
    useEffect(() => {
        drawGraph();
    }, [drawGraph]);

    // Draw on full-screen canvas when it opens or data changes
    useEffect(() => {
        if (isFullScreenOpen && fullScreenCanvasRef.current) {
            const timer = setTimeout(() => {
                drawGraph(fullScreenCanvasRef.current);
            }, 100);
            return () => clearTimeout(timer);
        }
    }, [isFullScreenOpen, functionType, parameters, base, customBase, viewSettings, inverseSettings, drawGraph]);
    
    // Update parent component when data changes
    useEffect(() => {
        if (onChange) {
            onChange({
                functionType,
                a: parameters.a,
                b: parameters.b,
                c: parameters.c,
                d: parameters.d,
                base,
                customBase,
                editMode,
                showInverse: inverseSettings.showInverse,
                showReflectionLine: inverseSettings.showReflectionLine,
                x_range: viewSettings.xRange,
                y_range: viewSettings.yRange,
                lineColor: viewSettings.lineColor,
                showGrid: viewSettings.showGrid,
                showPoints: viewSettings.showPoints,
                showAsymptotes: viewSettings.showAsymptotes,
                inverseLineColor: inverseSettings.inverseLineColor
            });
        }
    }, [functionType, parameters, base, customBase, editMode, inverseSettings, viewSettings, educationalFeatures, onChange]);
    
    // Update internal state when initialData changes (only on mount)
    useEffect(() => {
        if (initialData) {
            setFunctionType(initialData.functionType || 'exponential');
            setParameters({
                a: initialData.a || 1,
                b: initialData.b || 2,
                c: initialData.c || 0,
                d: initialData.d || 0
            });
            setBase(initialData.base || 'e');
            setCustomBase(initialData.customBase || 2);
            setEditMode(initialData.editMode || 'parameters');
            setViewSettings({
                xRange: initialData.x_range || [-5, 5],
                yRange: initialData.y_range || [-2, 10],
                showGrid: initialData.showGrid !== false,
                showPoints: initialData.showPoints !== false,
                showAsymptotes: initialData.showAsymptotes !== false,
                lineColor: initialData.lineColor || '#3B82F6'
            });
            setInverseSettings({
                showInverse: initialData.showInverse || false,
                showReflectionLine: initialData.showReflectionLine || false,
                inverseLineColor: initialData.inverseLineColor || '#10B981'
            });
            setEducationalFeatures({
                showLawsDemonstrator: initialData.showLawsDemonstrator || false,
                showFunctionProperties: initialData.showFunctionProperties !== false,
                showInverseVisualizer: initialData.showInverseVisualizer || false,
                currentLaw: initialData.currentLaw || 'product'
            });
        }
    }, []); // Only run once on mount
    
    // Handle parameter updates
    const handleParameterChange = (param, value) => {
        setParameters(prev => ({
            ...prev,
            [param]: value
        }));
    };
    
    // Handle view setting updates
    const handleViewSettingChange = (setting, value) => {
        setViewSettings(prev => ({
            ...prev,
            [setting]: value
        }));
    };
    
    // Handle inverse setting updates
    const handleInverseSettingChange = (setting, value) => {
        setInverseSettings(prev => ({
            ...prev,
            [setting]: value
        }));
    };
    
    // Handle educational feature updates
    const handleEducationalFeatureChange = (feature, value) => {
        setEducationalFeatures(prev => ({
            ...prev,
            [feature]: value
        }));
    };
    

    

    
    // Handle function type change
    const handleFunctionTypeChange = (newType) => {
        setFunctionType(newType);
        // Reset parameters to sensible defaults for new function type
        if (newType === 'exponential') {
            setParameters({ a: 1, b: 2, c: 0, d: 0 });
            // Keep exponential default ranges
            setViewSettings(prev => ({
                ...prev,
                xRange: [-5, 5],
                yRange: [-2, 10]
            }));
        } else {
            setParameters({ a: 1, b: 1, c: 0, d: 0 });
            setBase('e');
            // Set logarithmic default ranges: x: -4 to 20, y: -4 to 4
            setViewSettings(prev => ({
                ...prev,
                xRange: [-4, 20],
                yRange: [-4, 4]
            }));
        }
    };
    
    // Full screen handlers
    const handleOpenFullScreen = () => setIsFullScreenOpen(true);
    const handleCloseFullScreen = () => setIsFullScreenOpen(false);
    const handleToggleFullScreen = () => setIsFullScreen(!isFullScreen);
    
    // Reset to defaults
    const handleReset = () => {
        setFunctionType('exponential');
        setParameters({ a: 1, b: 2, c: 0, d: 0 });
        setBase('e');
        setCustomBase(2);
        setViewSettings({
            xRange: [-5, 5],
            yRange: [-2, 10],
            showGrid: true,
            showPoints: true,
            showAsymptotes: true,
            lineColor: '#3B82F6'
        });
        setInverseSettings({
            showInverse: false,
            showReflectionLine: false,
            inverseLineColor: '#10B981'
        });
        setEducationalFeatures({
            showLawsDemonstrator: false,
            showFunctionProperties: true,
            showInverseVisualizer: false,
            currentLaw: 'product'
        });

    };
    
    // Parameter Panel Component for Full Screen Mode
    const ParameterPanel = () => (
        <div className="space-y-4">
            <h3 className="font-semibold text-gray-800 mb-4">Integrated Exponential & Logarithmic Function Parameters</h3>
            
            {/* Function Type Selector */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Function Type</h4>
                <div className="flex space-x-2">
                    <button
                        onClick={() => setFunctionType('exponential')}
                        className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                            functionType === 'exponential'
                                ? 'bg-blue-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                        disabled={isSubmitted}
                    >
                        Exponential
                    </button>
                    <button
                        onClick={() => setFunctionType('logarithmic')}
                        className={`px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                            functionType === 'logarithmic'
                                ? 'bg-green-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                        disabled={isSubmitted}
                    >
                        Logarithmic
                    </button>
                </div>
            </div>

            {/* Parameter Editor */}
            <div className="space-y-4">
                <h4 className="font-medium text-gray-700">Parameters</h4>
                
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        {functionType === 'exponential' ? 'Coefficient a (stretch):' : 'Coefficient a (coefficient):'}
                    </label>
                    <input
                        type="number"
                        step="0.1"
                        value={parameters.a}
                        onChange={(e) => handleParameterChange('a', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        {functionType === 'exponential' ? 'Base b:' : 'Coefficient b (linear):'}
                    </label>
                    <input
                        type="number"
                        step="0.1"
                        value={parameters.b}
                        onChange={(e) => handleParameterChange('b', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                        disabled={isSubmitted}
                    />
                </div>

                {/* Advanced Parameters Toggle */}
                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-md">
                    <span className="text-sm font-medium text-gray-700">Advanced Parameters</span>
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={showAdvancedParameters}
                            onChange={(e) => setShowAdvancedParameters(e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-600">Enable Shifts</span>
                    </label>
                </div>

                {showAdvancedParameters && (
                    <>
                                        {/* Advanced Parameters Toggle */}
                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-md mb-4">
                    <span className="text-sm font-medium text-gray-700">Advanced Parameters</span>
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={showAdvancedParameters}
                            onChange={(e) => setShowAdvancedParameters(e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-600">Enable Shifts</span>
                    </label>
                </div>

                {showAdvancedParameters && (
                    <>
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">
                                {functionType === 'exponential' ? 'Horizontal shift c:' : 'Coefficient c (constant):'}
                            </label>
                            <input
                                type="number"
                                step="0.1"
                                value={parameters.c}
                                onChange={(e) => handleParameterChange('c', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>

                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Vertical shift d:</label>
                            <input
                                type="number"
                                step="0.1"
                                value={parameters.d}
                                onChange={(e) => handleParameterChange('d', e.target.value)}
                                className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                disabled={isSubmitted}
                            />
                        </div>
                    </>
                )}
                    </>
                )}

                {/* Base selection for logarithmic functions */}
                {functionType === 'logarithmic' && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Base:</label>
                        <select
                            value={base}
                            onChange={(e) => setBase(e.target.value)}
                            className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                            disabled={isSubmitted}
                        >
                            <option value="e">Natural (e)</option>
                            <option value="2">Binary (2)</option>
                            <option value="10">Decimal (10)</option>
                            <option value="custom">Custom</option>
                        </select>
                        
                        {base === 'custom' && (
                            <div className="mt-2">
                                <label className="block text-sm font-medium text-gray-700 mb-1">Custom Base:</label>
                                <input
                                    type="number"
                                    step="0.1"
                                    min="0.1"
                                    value={customBase}
                                    onChange={(e) => setCustomBase(e.target.value)}
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md text-sm"
                                    disabled={isSubmitted}
                                />
                            </div>
                        )}
                    </div>
                )}
            </div>

            {/* View Settings */}
            <div className="space-y-4">
                <h4 className="font-medium text-gray-700">View Settings</h4>
                
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Min:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={viewSettings.xRange[0]}
                            onChange={(e) => handleViewSettingChange('xRange', [Number(e.target.value), viewSettings.xRange[1]])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">X Max:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={viewSettings.xRange[1]}
                            onChange={(e) => handleViewSettingChange('xRange', [viewSettings.xRange[0], Number(e.target.value)])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
                
                <div className="grid grid-cols-2 gap-2">
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Y Min:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={viewSettings.yRange[0]}
                            onChange={(e) => handleViewSettingChange('yRange', [Number(e.target.value), viewSettings.yRange[1]])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                    <div>
                        <label className="block text-sm text-gray-600 mb-1">Y Max:</label>
                        <input
                            type="number"
                            step="0.5"
                            value={viewSettings.yRange[1]}
                            onChange={(e) => handleViewSettingChange('yRange', [viewSettings.xRange[0], Number(e.target.value)])}
                            className="w-full px-2 py-1 border border-gray-300 rounded text-sm"
                            disabled={isSubmitted}
                        />
                    </div>
                </div>
            </div>

            {/* Display Options */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Display Options</h4>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={viewSettings.showGrid}
                        onChange={(e) => handleViewSettingChange('showGrid', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Grid</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={viewSettings.showPoints}
                        onChange={(e) => handleViewSettingChange('showPoints', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Points</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={viewSettings.showAsymptotes}
                        onChange={(e) => handleViewSettingChange('showAsymptotes', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Asymptotes</span>
                </label>
            </div>

            {/* Line Color */}
            <div>
                <label className="block text-sm font-medium text-gray-700 mb-1">Line Color:</label>
                <input
                    type="color"
                    value={viewSettings.lineColor}
                    onChange={(e) => handleViewSettingChange('lineColor', e.target.value)}
                    className="w-full h-10 border border-gray-300 rounded-md"
                    disabled={isSubmitted}
                />
            </div>

            {/* Inverse Function Settings */}
            <div className="space-y-2">
                <h4 className="font-medium text-gray-700">Inverse Function</h4>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={inverseSettings.showInverse}
                        onChange={(e) => handleInverseSettingChange('showInverse', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Inverse Function</span>
                </label>
                <label className="flex items-center">
                    <input
                        type="checkbox"
                        checked={inverseSettings.showReflectionLine}
                        onChange={(e) => handleInverseSettingChange('showReflectionLine', e.target.checked)}
                        className="mr-2"
                        disabled={isSubmitted}
                    />
                    <span className="text-sm text-gray-700">Show Reflection Line (y = x)</span>
                </label>
                
                {inverseSettings.showInverse && (
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">Inverse Line Color:</label>
                        <input
                            type="color"
                            value={inverseSettings.inverseLineColor}
                            onChange={(e) => handleInverseSettingChange('inverseLineColor', e.target.value)}
                            className="w-full h-10 border border-gray-300 rounded-md"
                            disabled={isSubmitted}
                        />
                    </div>
                )}
            </div>

            {/* Function Information */}
            <div className="p-3 bg-blue-50 border border-blue-200 rounded">
                <h4 className="font-medium text-blue-800 mb-2">Current Function</h4>
                <div className="space-y-1 text-sm">
                    <div><strong>Type:</strong> {functionType.charAt(0).toUpperCase() + functionType.slice(1)}</div>
                    <div><strong>Equation:</strong> {getFunctionString()}</div>
                    <div><strong>Behavior:</strong> {calculateFunctionProperties().behavior}</div>
                </div>
            </div>

            {/* Function Properties */}
            <div className="p-3 bg-green-50 border border-green-200 rounded">
                <h4 className="font-medium text-green-800 mb-2">Function Properties</h4>
                <div className="space-y-1 text-sm">
                    <div><strong>Domain:</strong> {calculateFunctionProperties().domain.min === -Infinity ? '(-∞, ∞)' : `[${calculateFunctionProperties().domain.min}, ∞)`}</div>
                    <div><strong>Range:</strong> {calculateFunctionProperties().range.min === -Infinity ? '(-∞, ∞)' : `[${calculateFunctionProperties().range.min}, ∞)`}</div>
                    {calculateFunctionProperties().asymptote.horizontal && (
                        <div><strong>Horizontal Asymptote:</strong> {calculateFunctionProperties().asymptote.horizontal}</div>
                    )}
                    {calculateFunctionProperties().asymptote.vertical && (
                        <div><strong>Vertical Asymptote:</strong> {calculateFunctionProperties().asymptote.vertical}</div>
                    )}
                    <div><strong>Y-Intercept:</strong> {calculateFunctionProperties().yIntercept ? 
                        `(${calculateFunctionProperties().yIntercept[0]}, ${calculateFunctionProperties().yIntercept[1].toFixed(3)})` : 
                        'None'}</div>
                </div>
            </div>

            {/* Inverse Function Settings */}
            <div className="p-3 bg-purple-50 border border-purple-200 rounded">
                <h4 className="font-medium text-purple-800 mb-2">Inverse Function</h4>
                <div className="space-y-2">
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={inverseSettings.showInverse}
                            onChange={(e) => handleInverseSettingChange('showInverse', e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Show Inverse Function</span>
                    </label>
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={inverseSettings.showReflectionLine}
                            onChange={(e) => handleInverseSettingChange('showReflectionLine', e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Show Reflection Line (y = x)</span>
                    </label>
                    
                    {inverseSettings.showInverse && (
                        <div>
                            <label className="block text-sm font-medium text-gray-700 mb-1">Inverse Line Color:</label>
                            <input
                                type="color"
                                value={inverseSettings.inverseLineColor}
                                onChange={(e) => handleInverseSettingChange('inverseLineColor', e.target.value)}
                                className="w-full h-8 border border-gray-300 rounded"
                                disabled={isSubmitted}
                            />
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
    
    return (
        <div className="bg-white rounded-lg shadow-lg p-6">
            <div className="flex items-center justify-between mb-6">
                <h2 className="text-2xl font-bold text-gray-800">
                    Integrated Exponential & Logarithmic Functions
                </h2>
                <div className="flex space-x-2">
                    <button
                        onClick={handleReset}
                        className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors"
                        title="Reset to defaults"
                    >
                        <RotateCcw size={20} />
                    </button>
                    <button
                        onClick={handleOpenFullScreen}
                        className="p-2 text-gray-600 hover:text-gray-800 hover:bg-gray-100 rounded-lg transition-colors"
                        title="Full screen mode"
                    >
                        <Maximize2 size={20} />
                    </button>
                </div>
            </div>
            
            {/* Function Type Selector with Inline Containers */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">
                    Function Type
                </label>
                <div className="flex space-x-4">
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="exponential"
                            checked={functionType === 'exponential'}
                            onChange={(e) => handleFunctionTypeChange(e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Exponential</span>
                    </label>
                    <label className="flex items-center">
                        <input
                            type="radio"
                            value="logarithmic"
                            checked={functionType === 'logarithmic'}
                            onChange={(e) => handleFunctionTypeChange(e.target.value)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-700">Logarithmic</span>
                    </label>
                </div>
                
                {/* Inline containers with reduced horizontal lengths */}
                <div className="flex flex-col md:flex-row gap-4 mt-4">
                    {/* Current Function Display - Reduced horizontal length by 2/5 */}
                    <div className="w-full md:w-12/25 p-4 bg-blue-50 rounded-lg">
                        <h3 className="text-lg font-semibold text-blue-800 mb-2">Current Function</h3>
                        <div className="flex items-center gap-3">
                            <div className="text-2xl font-mono text-blue-900" 
                                 dangerouslySetInnerHTML={{ __html: getFunctionString() }} />
                            <div className="text-sm text-blue-700">
                                Behavior: {calculateFunctionProperties().behavior}
                            </div>
                        </div>
                    </div>
                    
                </div>
            </div>
            

            
            {/* Parameter Controls */}
            <div className="mb-6">
                <h3 className="text-lg font-semibold text-gray-800 mb-4">Function Parameters</h3>
                
                {/* Advanced Parameters Toggle */}
                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-md mb-4">
                    <span className="text-sm font-medium text-gray-700">Advanced Parameters</span>
                    <label className="flex items-center">
                        <input
                            type="checkbox"
                            checked={showAdvancedParameters}
                            onChange={(e) => setShowAdvancedParameters(e.target.checked)}
                            className="mr-2"
                            disabled={isSubmitted}
                        />
                        <span className="text-sm text-gray-600">Enable Shifts</span>
                    </label>
                </div>
                
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            {functionType === 'exponential' ? 'Coefficient (a)' : 'Coefficient (a)'}
                        </label>
                        <input
                            type="number"
                            value={parameters.a}
                            onChange={(e) => handleParameterChange('a', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            disabled={isSubmitted}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                            {functionType === 'exponential' ? 'Multiplier for the function' : 'Multiplier for the function'}
                        </p>
                    </div>
                    
                    <div>
                        <label className="block text-sm font-medium text-gray-700 mb-1">
                            {functionType === 'exponential' ? 'Base (b)' : 'Base (b)'}
                        </label>
                        <input
                            type="number"
                            value={parameters.b}
                            onChange={(e) => handleParameterChange('b', e.target.value)}
                            step="0.1"
                            className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                            disabled={isSubmitted}
                        />
                        <p className="text-xs text-gray-500 mt-1">
                            {functionType === 'exponential' ? 'Base of the exponential' : 'Base of the logarithm'}
                        </p>
                    </div>
                    
                    {showAdvancedParameters && (
                        <>
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">
                                    Horizontal Shift (c)
                                </label>
                                <input
                                    type="number"
                                    value={parameters.c}
                                    onChange={(e) => handleParameterChange('c', e.target.value)}
                                    step="0.1"
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    disabled={isSubmitted}
                                />
                                <p className="text-xs text-gray-500 mt-1">
                                    Left/right shift of the function
                                </p>
                            </div>
                            
                            <div>
                                <label className="block text-sm font-medium text-gray-700 mb-1">
                                    Vertical Shift (d)
                                </label>
                                <input
                                    type="number"
                                    value={parameters.d}
                                    onChange={(e) => handleParameterChange('d', e.target.value)}
                                    step="0.1"
                                    className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    disabled={isSubmitted}
                                />
                                <p className="text-xs text-gray-500 mt-1">
                                    Up/down shift of the function
                                </p>
                            </div>
                        </>
                    )}
                </div>
                
                {/* Base Selection for Logarithmic Functions */}
                {functionType === 'logarithmic' && (
                    <div className="mt-4">
                        <label className="block text-sm font-medium text-gray-700 mb-2">
                            Logarithm Base
                        </label>
                        <div className="flex space-x-4">
                            <label className="flex items-center">
                                <input
                                    type="radio"
                                    value="e"
                                    checked={base === 'e'}
                                    onChange={(e) => setBase(e.target.value)}
                                    className="mr-2"
                                    disabled={isSubmitted}
                                />
                                <span className="text-sm text-gray-700">Natural (e)</span>
                            </label>
                            <label className="flex items-center">
                                <input
                                    type="radio"
                                    value="2"
                                    checked={base === '2'}
                                    onChange={(e) => setBase(e.target.value)}
                                    className="mr-2"
                                    disabled={isSubmitted}
                                />
                                <span className="text-sm text-gray-700">Binary (2)</span>
                            </label>
                            <label className="flex items-center">
                                <input
                                    type="radio"
                                    value="10"
                                    checked={base === '10'}
                                    onChange={(e) => setBase(e.target.value)}
                                    className="mr-2"
                                    disabled={isSubmitted}
                                />
                                <span className="text-sm text-gray-700">Decimal (10)</span>
                            </label>
                            <label className="flex items-center">
                                <input
                                    type="radio"
                                    value="custom"
                                    checked={base === 'custom'}
                                    onChange={(e) => setBase(e.target.value)}
                                    className="mr-2"
                                    disabled={isSubmitted}
                                />
                                <span className="text-sm text-gray-700">Custom</span>
                            </label>
                        </div>
                        
                        {base === 'custom' && (
                            <div className="mt-2">
                                <input
                                    type="number"
                                    value={customBase}
                                    onChange={(e) => setCustomBase(e.target.value)}
                                    step="0.1"
                                    min="0.1"
                                    className="w-24 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                                    disabled={isSubmitted}
                                />
                            </div>
                        )}
                    </div>
                )}
            </div>
            

            

            

            
            {/* Graph Canvas */}
            <div className="mb-6 border border-gray-300 rounded-lg overflow-hidden">
                <div className="bg-gray-50 px-4 py-2 border-b border-gray-300">
                    <div className="flex items-center justify-between">
                        <span className="text-sm font-medium text-gray-700">Function Graph</span>
                        <div className="flex items-center space-x-2">
                            <button
                                onClick={() => handleViewSettingChange('showGrid', !viewSettings.showGrid)}
                                className={`p-1 rounded ${viewSettings.showGrid ? 'bg-blue-100 text-blue-700' : 'bg-gray-100 text-gray-500'}`}
                                title="Toggle Grid"
                            >
                                <Grid3X3 size={16} />
                            </button>
                            <button
                                onClick={() => handleInverseSettingChange('showInverse', !inverseSettings.showInverse)}
                                className={`p-1 rounded ${inverseSettings.showInverse ? 'bg-green-100 text-green-700' : 'bg-gray-100 text-gray-500'}`}
                                title="Toggle Inverse Function"
                            >
                                <TrendingUp size={16} />
                            </button>
                        </div>
                    </div>
                </div>
                <canvas
                    ref={canvasRef}
                    width={600}
                    height={400}
                    className="w-full h-auto cursor-crosshair"
                />
            </div>
            
            {/* Educational Features */}
            <div className="mb-6">
                <h3 className="text-lg font-semibold text-gray-800 mb-4">Educational Tools</h3>
                

                
                {/* Inverse Relationship Visualizer */}
                <div className="mb-6 p-4 bg-orange-50 rounded-lg">
                    <div className="flex items-center justify-between mb-3">
                        <h4 className="text-md font-semibold text-orange-800">Inverse Relationship Visualizer</h4>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={educationalFeatures.showInverseVisualizer}
                                onChange={(e) => handleEducationalFeatureChange('showInverseVisualizer', e.target.checked)}
                                className="mr-2"
                                disabled={isSubmitted}
                            />
                            <span className="text-sm text-orange-700">Show Visualizer</span>
                        </label>
                    </div>
                    
                    {educationalFeatures.showInverseVisualizer && (
                        <div className="space-y-4">
                            <div className="p-3 bg-white rounded border border-orange-200">
                                <h5 className="font-medium text-orange-700 mb-2">Inverse Function Relationship</h5>
                                <p className="text-sm text-orange-600 mb-3" 
                                   dangerouslySetInnerHTML={{ __html: 
                                     functionType === 'exponential' 
                                       ? `If y = ${parameters.a} × ${parameters.b}<sup>x</sup>, then x = log<sub>${parameters.b}</sub>(y / ${parameters.a})`
                                       : (() => {
                                           const baseStr = base === 'e' ? 'e' : base === '2' ? '2' : base === '10' ? '10' : customBase;
                                           return `If y = ${parameters.a} × log<sub>${baseStr}</sub>(x), then x = ${baseStr}<sup>y / ${parameters.a}</sup>`;
                                         })()
                                   }}
                                />
                                
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                    <div>
                                        <h6 className="font-medium text-orange-600 mb-2">Key Properties</h6>
                                        <ul className="text-sm text-orange-600 space-y-1">
                                            <li>• Domain of f(x) = Range of f⁻¹(x)</li>
                                            <li>• Range of f(x) = Domain of f⁻¹(x)</li>
                                            <li>• f(f⁻¹(x)) = x and f⁻¹(f(x)) = x</li>
                                            <li>• Graphs are reflections across y = x</li>
                                        </ul>
                                    </div>
                                    
                                    <div>
                                        <h6 className="font-medium text-orange-600 mb-2">Interactive Test</h6>
                                        <div className="space-y-2">
                                            <input
                                                type="number"
                                                placeholder="Enter x value"
                                                className="w-full px-2 py-1 text-sm border border-orange-300 rounded focus:outline-none focus:ring-1 focus:ring-orange-500"
                                                onChange={(e) => {
                                                    const x = Number(e.target.value);
                                                    if (!isNaN(x)) {
                                                        const y = calculateFunctionValue(x);
                                                        const inverseX = calculateInverseFunctionValue(y);
                                                        if (y !== null && inverseX !== null) {
                                                            const diff = Math.abs(x - inverseX);
                                                            if (diff < 0.001) {
                                                                alert(`✓ Verified: f(${x}) = ${y.toFixed(3)}, f⁻¹(${y.toFixed(3)}) = ${inverseX.toFixed(3)}`);
                                                            } else {
                                                                alert(`✗ Error: f(${x}) = ${y.toFixed(3)}, f⁻¹(${y.toFixed(3)}) = ${inverseX.toFixed(3)}`);
                                                            }
                                                        }
                                                    }
                                                }}
                                            />
                                            <button
                                                onClick={() => {
                                                    const x = 2; // Test value
                                                    const y = calculateFunctionValue(x);
                                                    const inverseX = calculateInverseFunctionValue(y);
                                                    if (y !== null && inverseX !== null) {
                                                        alert(`Test with x = ${x}:\nf(${x}) = ${y.toFixed(3)}\nf⁻¹(${y.toFixed(3)}) = ${inverseX.toFixed(3)}\nDifference: ${Math.abs(x - inverseX).toFixed(6)}`);
                                                    }
                                                }}
                                                className="w-full px-3 py-1 bg-orange-600 text-white text-sm rounded hover:bg-orange-700 transition-colors"
                                            >
                                                Test Inverse Relationship
                                            </button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    )}
                </div>
            </div>
            

            
            {/* Full Screen Modal */}
            <FullScreenModal
                isOpen={isFullScreenOpen}
                onClose={handleCloseFullScreen}
                title={`${functionType.charAt(0).toUpperCase() + functionType.slice(1)} Function Graph - Full Screen Mode`}
                onToggleFullScreen={handleToggleFullScreen}
                isFullScreen={isFullScreen}
                parameterPanel={<ParameterPanel />}
            >
                <div className="h-full flex items-center justify-center">
                    <div className="border-2 border-gray-300 rounded-lg overflow-hidden">
                        <canvas
                            ref={fullScreenCanvasRef}
                            width={800}
                            height={600}
                            className="w-full h-auto"
                        />
                    </div>
                </div>
            </FullScreenModal>
        </div>
    );
};

export default IntegratedExponentialLogarithmicFunction;
