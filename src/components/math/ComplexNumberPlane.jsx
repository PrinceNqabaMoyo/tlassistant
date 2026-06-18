import React, { useState, useEffect, useRef } from 'react';

const ComplexNumberPlane = ({ initialData, onChange, isSubmitted }) => {
    const [complexData, setComplexData] = useState(initialData || {
        title: "Complex Number Plane (Argand Diagram)",
        xRange: [-5, 5],
        yRange: [-5, 5],
        showGrid: true,
        showAxes: true,
        showUnitCircle: true,
        showComplexNumbers: true,
        showModulus: true,
        showArgument: true,
        showPolarForm: true,
        showConjugate: true,
        showOperations: true,
        gridSpacing: 1,
        backgroundColor: '#ffffff',
        gridColor: '#e5e7eb',
        axisColor: '#374151',
        unitCircleColor: '#d1d5db',
        pointColor: '#3B82F6',
        conjugateColor: '#10B981',
        modulusColor: '#F59E0B',
        argumentColor: '#EF4444',
        complexNumbers: [
            { real: 3, imaginary: 2, label: 'z₁', color: '#3B82F6' },
            { real: -2, imaginary: 1, label: 'z₂', color: '#10B981' },
            { real: 1, imaginary: -3, label: 'z₃', color: '#F59E0B' }
        ]
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(complexData);
        }
    }, [complexData, onChange]);

    useEffect(() => {
        drawComplexPlane();
    }, [complexData]);

    // Calculate modulus (absolute value) of complex number
    const calculateModulus = (real, imaginary) => {
        return Math.sqrt(real * real + imaginary * imaginary);
    };

    // Calculate argument (angle) of complex number
    const calculateArgument = (real, imaginary) => {
        return Math.atan2(imaginary, real);
    };

    // Convert to polar form
    const toPolarForm = (real, imaginary) => {
        const modulus = calculateModulus(real, imaginary);
        const argument = calculateArgument(real, imaginary);
        return { modulus, argument };
    };

    // Convert from polar form
    const fromPolarForm = (modulus, argument) => {
        const real = modulus * Math.cos(argument);
        const imaginary = modulus * Math.sin(argument);
        return { real, imaginary };
    };

    // Calculate conjugate
    const calculateConjugate = (real, imaginary) => {
        return { real, imaginary: -imaginary };
    };

    // Complex number operations
    const addComplex = (z1, z2) => {
        return {
            real: z1.real + z2.real,
            imaginary: z1.imaginary + z2.imaginary
        };
    };

    const multiplyComplex = (z1, z2) => {
        return {
            real: z1.real * z2.real - z1.imaginary * z2.imaginary,
            imaginary: z1.real * z2.imaginary + z1.imaginary * z2.real
        };
    };

    const divideComplex = (z1, z2) => {
        const denominator = z2.real * z2.real + z2.imaginary * z2.imaginary;
        return {
            real: (z1.real * z2.real + z1.imaginary * z2.imaginary) / denominator,
            imaginary: (z1.imaginary * z2.real - z1.real * z2.imaginary) / denominator
        };
    };

    const drawComplexPlane = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        ctx.fillStyle = complexData.backgroundColor;
        ctx.fillRect(0, 0, width, height);

        const { xRange, yRange, showGrid, showAxes, showUnitCircle, showComplexNumbers, showModulus, showArgument, showPolarForm, showConjugate, showOperations, gridSpacing, gridColor, axisColor, unitCircleColor, pointColor, conjugateColor, modulusColor, argumentColor, complexNumbers } = complexData;

        const margin = 60;
        const plotWidth = width - 2 * margin;
        const plotHeight = height - 2 * margin;

        // Scale factors
        const xScale = plotWidth / (xRange[1] - xRange[0]);
        const yScale = plotHeight / (yRange[1] - yRange[0]);

        const toCanvasX = (x) => margin + (x - xRange[0]) * xScale;
        const toCanvasY = (y) => height - margin - (y - yRange[0]) * yScale;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = gridColor;
            ctx.lineWidth = 1;
            
            // Vertical grid lines
            for (let x = xRange[0]; x <= xRange[1]; x += gridSpacing) {
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, margin);
                ctx.lineTo(canvasX, height - margin);
                ctx.stroke();
            }
            
            // Horizontal grid lines
            for (let y = yRange[0]; y <= yRange[1]; y += gridSpacing) {
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(margin, canvasY);
                ctx.lineTo(width - margin, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        if (showAxes) {
            ctx.strokeStyle = axisColor;
            ctx.lineWidth = 2;
            
            // X-axis (real axis)
            ctx.beginPath();
            ctx.moveTo(margin, toCanvasY(0));
            ctx.lineTo(width - margin, toCanvasY(0));
            ctx.stroke();
            
            // Y-axis (imaginary axis)
            ctx.beginPath();
            ctx.moveTo(toCanvasX(0), margin);
            ctx.lineTo(toCanvasX(0), height - margin);
            ctx.stroke();
        }

        // Draw unit circle
        if (showUnitCircle) {
            ctx.strokeStyle = unitCircleColor;
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            
            const centerX = toCanvasX(0);
            const centerY = toCanvasY(0);
            const radius = 1 * Math.min(xScale, yScale);
            
            ctx.beginPath();
            ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
            ctx.stroke();
            ctx.setLineDash([]);
        }

        // Draw complex numbers
        if (showComplexNumbers) {
            complexNumbers.forEach((complex, index) => {
                const { real, imaginary, label, color } = complex;
                const canvasX = toCanvasX(real);
                const canvasY = toCanvasY(imaginary);

                // Draw point
                ctx.fillStyle = color;
                ctx.beginPath();
                ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
                ctx.fill();
                ctx.strokeStyle = '#1e40af';
                ctx.lineWidth = 2;
                ctx.stroke();

                // Draw label
                ctx.fillStyle = axisColor;
                ctx.font = 'bold 14px Arial';
                ctx.textAlign = 'left';
                ctx.fillText(label, canvasX + 10, canvasY - 10);

                // Draw coordinates
                ctx.font = '12px Arial';
                ctx.fillText(`(${real}, ${imaginary}i)`, canvasX + 10, canvasY + 5);

                // Draw modulus line
                if (showModulus) {
                    const modulus = calculateModulus(real, imaginary);
                    ctx.strokeStyle = modulusColor;
                    ctx.lineWidth = 2;
                    ctx.setLineDash([3, 3]);
                    ctx.beginPath();
                    ctx.moveTo(toCanvasX(0), toCanvasY(0));
                    ctx.lineTo(canvasX, canvasY);
                    ctx.stroke();
                    ctx.setLineDash([]);

                    // Draw modulus label
                    ctx.fillStyle = modulusColor;
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'center';
                    const midX = (toCanvasX(0) + canvasX) / 2;
                    const midY = (toCanvasY(0) + canvasY) / 2;
                    ctx.fillText(`|${label}| = ${modulus.toFixed(2)}`, midX, midY - 10);
                }

                // Draw argument arc
                if (showArgument) {
                    const argument = calculateArgument(real, imaginary);
                    ctx.strokeStyle = argumentColor;
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.arc(toCanvasX(0), toCanvasY(0), 30, 0, argument, false);
                    ctx.stroke();

                    // Draw argument label
                    ctx.fillStyle = argumentColor;
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'center';
                    const argX = toCanvasX(0) + 20 * Math.cos(argument / 2);
                    const argY = toCanvasY(0) - 20 * Math.sin(argument / 2);
                    ctx.fillText(`arg(${label}) = ${(argument * 180 / Math.PI).toFixed(1)}°`, argX, argY);
                }

                // Draw conjugate
                if (showConjugate) {
                    const conjugate = calculateConjugate(real, imaginary);
                    const conjX = toCanvasX(conjugate.real);
                    const conjY = toCanvasY(conjugate.imaginary);

                    ctx.fillStyle = conjugateColor;
                    ctx.beginPath();
                    ctx.arc(conjX, conjY, 4, 0, 2 * Math.PI);
                    ctx.fill();

                    ctx.fillStyle = conjugateColor;
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'left';
                    ctx.fillText(`${label}* = (${conjugate.real}, ${conjugate.imaginary}i)`, conjX + 10, conjY + 5);
                }

                // Draw polar form
                if (showPolarForm) {
                    const polar = toPolarForm(real, imaginary);
                    ctx.fillStyle = axisColor;
                    ctx.font = '12px Arial';
                    ctx.textAlign = 'left';
                    ctx.fillText(`${label} = ${polar.modulus.toFixed(2)}∠${(polar.argument * 180 / Math.PI).toFixed(1)}°`, canvasX + 10, canvasY + 20);
                }
            });
        }

        // Draw axis labels
        ctx.fillStyle = axisColor;
        ctx.font = 'bold 16px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Re(z)', width / 2, height - 10);
        
        ctx.save();
        ctx.translate(20, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Im(z)', 0, 0);
        ctx.restore();

        // Draw title
        ctx.font = 'bold 18px Arial';
        ctx.fillText(complexData.title, width / 2, 25);

        // Draw operations if enabled
        if (showOperations && complexNumbers.length >= 2) {
            const z1 = complexNumbers[0];
            const z2 = complexNumbers[1];
            
            const sum = addComplex(z1, z2);
            const product = multiplyComplex(z1, z2);
            const quotient = divideComplex(z1, z2);

            let yOffset = margin + 20;
            ctx.fillStyle = axisColor;
            ctx.font = 'bold 14px Arial';
            ctx.textAlign = 'left';
            ctx.fillText('Operations:', width - margin, yOffset);
            
            ctx.font = '12px Arial';
            yOffset += 20;
            ctx.fillText(`${z1.label} + ${z2.label} = (${sum.real.toFixed(2)}, ${sum.imaginary.toFixed(2)}i)`, width - margin, yOffset);
            yOffset += 15;
            ctx.fillText(`${z1.label} × ${z2.label} = (${product.real.toFixed(2)}, ${product.imaginary.toFixed(2)}i)`, width - margin, yOffset);
            yOffset += 15;
            ctx.fillText(`${z1.label} ÷ ${z2.label} = (${quotient.real.toFixed(2)}, ${quotient.imaginary.toFixed(2)}i)`, width - margin, yOffset);
        }

        // Draw coordinate labels
        ctx.fillStyle = axisColor;
        ctx.font = '12px Arial';
        ctx.textAlign = 'center';
        
        // X-axis labels
        for (let x = xRange[0]; x <= xRange[1]; x += gridSpacing) {
            if (x !== 0) {
                ctx.fillText(x.toString(), toCanvasX(x), toCanvasY(0) + 20);
            }
        }
        
        // Y-axis labels
        for (let y = yRange[0]; y <= yRange[1]; y += gridSpacing) {
            if (y !== 0) {
                ctx.fillText(y.toString(), toCanvasX(0) - 10, toCanvasY(y) + 4);
            }
        }
    };

    const handleInputChange = (field, value) => {
        setComplexData(prev => ({
            ...prev,
            [field]: field === 'xRange' || field === 'yRange' || field === 'gridSpacing' ? parseFloat(value) || 0 : value
        }));
    };

    const handleRangeChange = (axis, index, value) => {
        setComplexData(prev => ({
            ...prev,
            [axis]: prev[axis].map((val, i) => i === index ? parseFloat(value) || 0 : val)
        }));
    };

    const addComplexNumber = () => {
        const newComplex = {
            real: Math.floor(Math.random() * 6) - 3,
            imaginary: Math.floor(Math.random() * 6) - 3,
            label: `z${complexData.complexNumbers.length + 1}`,
            color: `#${Math.floor(Math.random()*16777215).toString(16)}`
        };
        setComplexData(prev => ({
            ...prev,
            complexNumbers: [...prev.complexNumbers, newComplex]
        }));
    };

    const removeComplexNumber = (index) => {
        setComplexData(prev => ({
            ...prev,
            complexNumbers: prev.complexNumbers.filter((_, i) => i !== index)
        }));
    };

    const setCommonComplexNumbers = () => {
        const commonNumbers = [
            { real: 1, imaginary: 0, label: '1', color: '#3B82F6' },
            { real: 0, imaginary: 1, label: 'i', color: '#10B981' },
            { real: -1, imaginary: 0, label: '-1', color: '#F59E0B' },
            { real: 0, imaginary: -1, label: '-i', color: '#EF4444' },
            { real: 1, imaginary: 1, label: '1+i', color: '#8B5CF6' },
            { real: 1, imaginary: -1, label: '1-i', color: '#06B6D4' }
        ];
        setComplexData(prev => ({
            ...prev,
            complexNumbers: commonNumbers
        }));
    };

    const calculateOperations = () => {
        if (complexData.complexNumbers.length >= 2) {
            const z1 = complexData.complexNumbers[0];
            const z2 = complexData.complexNumbers[1];
            
            const sum = addComplex(z1, z2);
            const product = multiplyComplex(z1, z2);
            const quotient = divideComplex(z1, z2);
            const z1Modulus = calculateModulus(z1.real, z1.imaginary);
            const z2Modulus = calculateModulus(z2.real, z2.imaginary);
            const z1Arg = calculateArgument(z1.real, z1.imaginary);
            const z2Arg = calculateArgument(z2.real, z2.imaginary);

            return {
                sum: `${sum.real.toFixed(2)} + ${sum.imaginary.toFixed(2)}i`,
                product: `${product.real.toFixed(2)} + ${product.imaginary.toFixed(2)}i`,
                quotient: `${quotient.real.toFixed(2)} + ${quotient.imaginary.toFixed(2)}i`,
                z1Modulus: z1Modulus.toFixed(2),
                z2Modulus: z2Modulus.toFixed(2),
                z1Arg: (z1Arg * 180 / Math.PI).toFixed(1),
                z2Arg: (z2Arg * 180 / Math.PI).toFixed(1)
            };
        }
        return null;
    };

    const operations = calculateOperations();

    return (
        <div className="space-y-4">
            {/* Controls */}
            <div className="grid grid-cols-2 gap-4 p-4 bg-gray-50 rounded-lg">
                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Title
                    </label>
                    <input
                        type="text"
                        value={complexData.title}
                        onChange={(e) => handleInputChange('title', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Grid Spacing
                    </label>
                    <input
                        type="number"
                        min="0.5"
                        max="2"
                        step="0.5"
                        value={complexData.gridSpacing}
                        onChange={(e) => handleInputChange('gridSpacing', e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        X Range Min
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={complexData.xRange[0]}
                        onChange={(e) => handleRangeChange('xRange', 0, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        X Range Max
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={complexData.xRange[1]}
                        onChange={(e) => handleRangeChange('xRange', 1, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Y Range Min
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={complexData.yRange[0]}
                        onChange={(e) => handleRangeChange('yRange', 0, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                        Y Range Max
                    </label>
                    <input
                        type="number"
                        step="0.5"
                        value={complexData.yRange[1]}
                        onChange={(e) => handleRangeChange('yRange', 1, e.target.value)}
                        className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                    />
                </div>

                <div className="col-span-2">
                    <div className="flex space-x-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showGrid}
                                onChange={(e) => handleInputChange('showGrid', e.target.checked)}
                                className="mr-2"
                            />
                            Show Grid
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showAxes}
                                onChange={(e) => handleInputChange('showAxes', e.target.checked)}
                                className="mr-2"
                            />
                            Show Axes
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showUnitCircle}
                                onChange={(e) => handleInputChange('showUnitCircle', e.target.checked)}
                                className="mr-2"
                            />
                            Show Unit Circle
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showComplexNumbers}
                                onChange={(e) => handleInputChange('showComplexNumbers', e.target.checked)}
                                className="mr-2"
                            />
                            Show Numbers
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showModulus}
                                onChange={(e) => handleInputChange('showModulus', e.target.checked)}
                                className="mr-2"
                            />
                            Show Modulus
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showArgument}
                                onChange={(e) => handleInputChange('showArgument', e.target.checked)}
                                className="mr-2"
                            />
                            Show Argument
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showPolarForm}
                                onChange={(e) => handleInputChange('showPolarForm', e.target.checked)}
                                className="mr-2"
                            />
                            Show Polar Form
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showConjugate}
                                onChange={(e) => handleInputChange('showConjugate', e.target.checked)}
                                className="mr-2"
                            />
                            Show Conjugate
                        </label>

                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showOperations}
                                onChange={(e) => handleInputChange('showOperations', e.target.checked)}
                                className="mr-2"
                            />
                            Show Operations
                        </label>
                    </div>
                </div>
            </div>

            {/* Complex Number Management */}
            <div className="p-4 bg-blue-50 border border-blue-200 rounded-lg">
                <div className="flex justify-between items-center mb-3">
                    <h4 className="font-semibold text-blue-800">Complex Numbers</h4>
                    <div className="flex space-x-2">
                        <button
                            onClick={addComplexNumber}
                            className="px-3 py-1 bg-blue-600 hover:bg-blue-700 text-white rounded text-sm"
                        >
                            Add Number
                        </button>
                        <button
                            onClick={setCommonComplexNumbers}
                            className="px-3 py-1 bg-green-600 hover:bg-green-700 text-white rounded text-sm"
                        >
                            Common Numbers
                        </button>
                    </div>
                </div>
                <div className="space-y-2">
                    {complexData.complexNumbers.map((complex, index) => (
                        <div key={index} className="flex items-center justify-between p-2 bg-white rounded border">
                            <div>
                                <span className="font-medium">{complex.label}:</span>
                                <span className="text-sm text-gray-600 ml-2">
                                    ({complex.real}, {complex.imaginary}i)
                                </span>
                            </div>
                            <button
                                onClick={() => removeComplexNumber(index)}
                                className="text-red-600 hover:text-red-800 text-sm"
                            >
                                Remove
                            </button>
                        </div>
                    ))}
                </div>
            </div>

            {/* Operations Summary */}
            {operations && (
                <div className="p-4 bg-green-50 border border-green-200 rounded-lg">
                    <h4 className="font-semibold text-green-800 mb-3">Complex Operations</h4>
                    <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                            <strong>z₁ + z₂:</strong> {operations.sum}
                        </div>
                        <div>
                            <strong>z₁ × z₂:</strong> {operations.product}
                        </div>
                        <div>
                            <strong>z₁ ÷ z₂:</strong> {operations.quotient}
                        </div>
                        <div>
                            <strong>|z₁|:</strong> {operations.z1Modulus}
                        </div>
                        <div>
                            <strong>|z₂|:</strong> {operations.z2Modulus}
                        </div>
                        <div>
                            <strong>arg(z₁):</strong> {operations.z1Arg}°
                        </div>
                        <div>
                            <strong>arg(z₂):</strong> {operations.z2Arg}°
                        </div>
                    </div>
                </div>
            )}

            {/* Complex Number Plane Canvas */}
            <div className="border border-gray-300 rounded-lg overflow-hidden">
                <canvas
                    ref={canvasRef}
                    width={800}
                    height={600}
                    className="w-full h-auto"
                />
            </div>
        </div>
    );
};

export default ComplexNumberPlane;
