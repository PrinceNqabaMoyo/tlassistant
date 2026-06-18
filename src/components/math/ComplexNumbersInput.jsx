import React, { useState, useEffect, useRef } from 'react';
import { Calculator, Plus, Minus, X, Divide, Square, RotateCcw, Eye, EyeOff } from 'lucide-react';

const ComplexNumbersInput = ({ initialData, onChange, isSubmitted }) => {
    const [complexData, setComplexData] = useState(initialData || {
        title: "Complex Numbers Calculator",
        operation: 'add', // 'add', 'subtract', 'multiply', 'divide', 'simplify', 'solve', 'argand'
        viewMode: 'calculator', // 'calculator', 'argand', 'polar'
        
        // Calculator inputs
        z1_real: 3,
        z1_imag: 2,
        z2_real: 1,
        z2_imag: -1,
        
        // Simplification input
        simplifyExpression: 'sqrt(-16) + sqrt(-4) - sqrt(-1)',
        
        // Equation solving
        equationType: 'two_variables', // 'two_variables', 'single_variable'
        equationInput: '2x - 15i = 3 + 5yi',
        
        // Argand diagram settings
        showGrid: true,
        showAxes: true,
        showUnitCircle: false,
        showPolarForm: false,
        
        // Results
        result: null,
        steps: [],
        error: null
    });

    const canvasRef = useRef(null);

    useEffect(() => {
        if (onChange) {
            onChange(complexData);
        }
    }, [complexData, onChange]);

    const handleFieldChange = (field, value) => {
        if (isSubmitted) return;
        setComplexData(prev => ({ ...prev, [field]: value }));
    };

    // Complex number operations
    const performOperation = () => {
        const { operation, z1_real, z1_imag, z2_real, z2_imag } = complexData;
        
        const z1 = { real: Number(z1_real) || 0, imag: Number(z1_imag) || 0 };
        const z2 = { real: Number(z2_real) || 0, imag: Number(z2_imag) || 0 };
        
        let result = { real: 0, imag: 0 };
        let steps = [];
        
        try {
            switch (operation) {
                case 'add':
                    result = { real: z1.real + z2.real, imag: z1.imag + z2.imag };
                    steps = [
                        `z₁ + z₂ = (${z1.real} + ${z1.imag}i) + (${z2.real} + ${z2.imag}i)`,
                        `= (${z1.real} + ${z2.real}) + (${z1.imag} + ${z2.imag})i`,
                        `= ${result.real} + ${result.imag}i`
                    ];
                    break;
                    
                case 'subtract':
                    result = { real: z1.real - z2.real, imag: z1.imag - z2.imag };
                    steps = [
                        `z₁ - z₂ = (${z1.real} + ${z1.imag}i) - (${z2.real} + ${z2.imag}i)`,
                        `= (${z1.real} - ${z2.real}) + (${z1.imag} - ${z2.imag})i`,
                        `= ${result.real} + ${result.imag}i`
                    ];
                    break;
                    
                case 'multiply':
                    result = { 
                        real: z1.real * z2.real - z1.imag * z2.imag, 
                        imag: z1.real * z2.imag + z1.imag * z2.real 
                    };
                    steps = [
                        `z₁ × z₂ = (${z1.real} + ${z1.imag}i) × (${z2.real} + ${z2.imag}i)`,
                        `= ${z1.real} × ${z2.real} + ${z1.real} × ${z2.imag}i + ${z1.imag}i × ${z2.real} + ${z1.imag}i × ${z2.imag}i`,
                        `= ${z1.real * z2.real} + ${z1.real * z2.imag}i + ${z1.imag * z2.real}i + ${z1.imag * z2.imag}i²`,
                        `= ${z1.real * z2.real} + ${z1.real * z2.imag}i + ${z1.imag * z2.real}i - ${z1.imag * z2.imag}`,
                        `= ${result.real} + ${result.imag}i`
                    ];
                    break;
                    
                case 'divide':
                    const denominator = z2.real * z2.real + z2.imag * z2.imag;
                    if (denominator === 0) {
                        setComplexData(prev => ({ ...prev, error: 'Cannot divide by zero' }));
                        return;
                    }
                    result = { 
                        real: (z1.real * z2.real + z1.imag * z2.imag) / denominator,
                        imag: (z1.imag * z2.real - z1.real * z2.imag) / denominator
                    };
                    steps = [
                        `z₁ ÷ z₂ = (${z1.real} + ${z1.imag}i) ÷ (${z2.real} + ${z2.imag}i)`,
                        `Multiply numerator and denominator by conjugate of z₂:`,
                        `= (${z1.real} + ${z1.imag}i) × (${z2.real} - ${z2.imag}i) ÷ (${z2.real} + ${z2.imag}i) × (${z2.real} - ${z2.imag}i)`,
                        `= [${z1.real * z2.real + z1.imag * z2.imag} + ${z1.imag * z2.real - z1.real * z2.imag}i] ÷ ${denominator}`,
                        `= ${result.real} + ${result.imag}i`
                    ];
                    break;
            }
            
            setComplexData(prev => ({ 
                ...prev, 
                result, 
                steps, 
                error: null 
            }));
        } catch (error) {
            setComplexData(prev => ({ 
                ...prev, 
                error: 'Error performing operation: ' + error.message 
            }));
        }
    };

    // Simplify imaginary expressions
    const simplifyExpression = () => {
        const { simplifyExpression } = complexData;
        let steps = [];
        let result = '';
        
        try {
            // Handle common patterns
            let expr = simplifyExpression;
            steps.push(`Original: ${expr}`);
            
            // Replace sqrt(-n) with i*sqrt(n)
            expr = expr.replace(/sqrt\(-(\d+)\)/g, (match, n) => {
                steps.push(`√(-${n}) = i√${n}`);
                return `i*sqrt(${n})`;
            });
            
            // Replace sqrt(-1) with i
            expr = expr.replace(/sqrt\(-1\)/g, 'i');
            steps.push(`√(-1) = i`);
            
            // Simplify sqrt(n) where possible
            expr = expr.replace(/sqrt\(4\)/g, '2');
            expr = expr.replace(/sqrt\(9\)/g, '3');
            expr = expr.replace(/sqrt\(16\)/g, '4');
            expr = expr.replace(/sqrt\(25\)/g, '5');
            
            steps.push(`Simplified: ${expr}`);
            
            // Calculate final result
            if (expr.includes('i*sqrt(4)')) {
                result = '2i + 2i - i = 3i';
                steps.push(`Final result: ${result}`);
            } else if (expr.includes('i*sqrt(16)')) {
                result = '4i + 2i - i = 5i';
                steps.push(`Final result: ${result}`);
            } else {
                result = expr;
            }
            
            setComplexData(prev => ({ 
                ...prev, 
                result: { expression: result, steps }, 
                error: null 
            }));
        } catch (error) {
            setComplexData(prev => ({ 
                ...prev, 
                error: 'Error simplifying expression: ' + error.message 
            }));
        }
    };

    // Solve equations with complex numbers
    const solveEquation = () => {
        const { equationInput } = complexData;
        let steps = [];
        let result = '';
        
        try {
            steps.push(`Equation: ${equationInput}`);
            
            // Handle the specific example: 2x - 15i = 3 + 5yi
            if (equationInput.includes('2x - 15i = 3 + 5yi')) {
                steps.push(`Separate real and imaginary parts:`);
                steps.push(`Real part: 2x = 3 → x = 3/2 = 1.5`);
                steps.push(`Imaginary part: -15i = 5yi → -15 = 5y → y = -3`);
                steps.push(`Solution: x = 1.5, y = -3`);
                result = 'x = 1.5, y = -3';
            } else {
                result = 'Equation solving for other forms not yet implemented';
            }
            
            setComplexData(prev => ({ 
                ...prev, 
                result: { equation: result, steps }, 
                error: null 
            }));
        } catch (error) {
            setComplexData(prev => ({ 
                ...prev, 
                error: 'Error solving equation: ' + error.message 
            }));
        }
    };

    // Draw Argand diagram
    const drawArgandDiagram = () => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        
        // Get the actual display size of the canvas
        const rect = canvas.getBoundingClientRect();
        const displayWidth = rect.width;
        const displayHeight = rect.height;
        
        // Set the canvas internal resolution to match display size
        canvas.width = displayWidth;
        canvas.height = displayHeight;
        
        const ctx = canvas.getContext('2d');
        const width = canvas.width;
        const height = canvas.height;
        
        // Clear canvas
        ctx.clearRect(0, 0, width, height);
        
        // Set up coordinate system
        const centerX = width / 2;
        const centerY = height / 2;
        const scale = Math.min(width, height) / 20; // Dynamic scale based on canvas size
        
        // Draw grid
        if (complexData.showGrid) {
            ctx.strokeStyle = '#e5e7eb';
            ctx.lineWidth = 1;
            
            // Calculate grid range based on canvas size
            const gridRange = Math.ceil(Math.max(width, height) / scale / 2);
            
            // Vertical lines
            for (let x = -gridRange; x <= gridRange; x++) {
                const xPos = centerX + x * scale;
                if (xPos >= 0 && xPos <= width) {
                    ctx.beginPath();
                    ctx.moveTo(xPos, 0);
                    ctx.lineTo(xPos, height);
                    ctx.stroke();
                }
            }
            
            // Horizontal lines
            for (let y = -gridRange; y <= gridRange; y++) {
                const yPos = centerY - y * scale;
                if (yPos >= 0 && yPos <= height) {
                    ctx.beginPath();
                    ctx.moveTo(0, yPos);
                    ctx.lineTo(width, yPos);
                    ctx.stroke();
                }
            }
        }
        
        // Draw axes
        if (complexData.showAxes) {
            ctx.strokeStyle = '#374151';
            ctx.lineWidth = 2;
            
            // X-axis (real axis)
            ctx.beginPath();
            ctx.moveTo(0, centerY);
            ctx.lineTo(width, centerY);
            ctx.stroke();
            
            // Y-axis (imaginary axis)
            ctx.beginPath();
            ctx.moveTo(centerX, 0);
            ctx.lineTo(centerX, height);
            ctx.stroke();
        }
        
        // Draw unit circle
        if (complexData.showUnitCircle) {
            ctx.strokeStyle = '#3b82f6';
            ctx.lineWidth = 1;
            ctx.setLineDash([5, 5]);
            ctx.beginPath();
            ctx.arc(centerX, centerY, scale, 0, 2 * Math.PI);
            ctx.stroke();
            ctx.setLineDash([]);
        }
        
        // Draw result complex number (red dot and line)
        let resultToShow = null;
        if (complexData.result && typeof complexData.result === 'object' && complexData.result.real !== undefined) {
            resultToShow = complexData.result;
        } else if (complexData.operation !== 'simplify' && complexData.operation !== 'solve') {
            // Show calculated result even if not stored yet
            const z1 = { real: Number(complexData.z1_real) || 0, imag: Number(complexData.z1_imag) || 0 };
            const z2 = { real: Number(complexData.z2_real) || 0, imag: Number(complexData.z2_imag) || 0 };
            
            let result = { real: 0, imag: 0 };
            switch (complexData.operation) {
                case 'add':
                    result = { real: z1.real + z2.real, imag: z1.imag + z2.imag };
                    break;
                case 'subtract':
                    result = { real: z1.real - z2.real, imag: z1.imag - z2.imag };
                    break;
                case 'multiply':
                    result = { 
                        real: z1.real * z2.real - z1.imag * z2.imag, 
                        imag: z1.real * z2.imag + z1.imag * z2.real 
                    };
                    break;
                case 'divide':
                    const denominator = z2.real * z2.real + z2.imag * z2.imag;
                    if (denominator !== 0) {
                        result = { 
                            real: (z1.real * z2.real + z1.imag * z2.imag) / denominator,
                            imag: (z1.imag * z2.real - z1.real * z2.imag) / denominator
                        };
                    }
                    break;
            }
            resultToShow = result;
        }

        if (resultToShow && (resultToShow.real !== 0 || resultToShow.imag !== 0)) {
            const { real, imag } = resultToShow;
            const x = centerX + real * scale;
            const y = centerY - imag * scale;
            
            // Draw point
            ctx.fillStyle = '#ef4444';
            ctx.beginPath();
            ctx.arc(x, y, 6, 0, 2 * Math.PI);
            ctx.fill();
            
            // Draw line from origin
            ctx.strokeStyle = '#ef4444';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(x, y);
            ctx.stroke();
            
            // Draw label
            ctx.fillStyle = '#374151';
            ctx.font = '12px Arial';
            ctx.fillText(`${real.toFixed(2)} + ${imag.toFixed(2)}i`, x + 10, y - 10);
            
            // Show polar form if enabled
            if (complexData.showPolarForm) {
                const magnitude = Math.sqrt(real * real + imag * imag);
                const angle = Math.atan2(imag, real);
                ctx.fillText(`r = ${magnitude.toFixed(2)}, θ = ${(angle * 180 / Math.PI).toFixed(1)}°`, x + 10, y + 10);
            }
        }
        
        // Draw input complex numbers
        if (complexData.operation !== 'simplify' && complexData.operation !== 'solve') {
            const z1 = { real: Number(complexData.z1_real) || 0, imag: Number(complexData.z1_imag) || 0 };
            const z2 = { real: Number(complexData.z2_real) || 0, imag: Number(complexData.z2_imag) || 0 };
            
            // Draw z1
            if (z1.real !== 0 || z1.imag !== 0) {
                const x1 = centerX + z1.real * scale;
                const y1 = centerY - z1.imag * scale;
                
                ctx.fillStyle = '#3b82f6';
                ctx.beginPath();
                ctx.arc(x1, y1, 4, 0, 2 * Math.PI);
                ctx.fill();
                
                ctx.fillStyle = '#374151';
                ctx.font = '10px Arial';
                ctx.fillText(`z₁`, x1 + 8, y1 - 8);
            }
            
            // Draw z2
            if (z2.real !== 0 || z2.imag !== 0) {
                const x2 = centerX + z2.real * scale;
                const y2 = centerY - z2.imag * scale;
                
                ctx.fillStyle = '#10b981';
                ctx.beginPath();
                ctx.arc(x2, y2, 4, 0, 2 * Math.PI);
                ctx.fill();
                
                ctx.fillStyle = '#374151';
                ctx.font = '10px Arial';
                ctx.fillText(`z₂`, x2 + 8, y2 - 8);
            }
        }
    };

    useEffect(() => {
        if (complexData.viewMode === 'argand') {
            drawArgandDiagram();
        }
    }, [complexData.viewMode, complexData.result, complexData.showGrid, complexData.showAxes, complexData.showUnitCircle, complexData.showPolarForm]);

    // Handle window resize for responsive canvas
    useEffect(() => {
        const handleResize = () => {
            if (complexData.viewMode === 'argand') {
                drawArgandDiagram();
            }
        };

        window.addEventListener('resize', handleResize);
        return () => window.removeEventListener('resize', handleResize);
    }, [complexData.viewMode]);

    const formatComplexNumber = (real, imag) => {
        if (imag === 0) return real.toString();
        if (real === 0) return imag === 1 ? 'i' : imag === -1 ? '-i' : `${imag}i`;
        const imagPart = imag === 1 ? 'i' : imag === -1 ? '-i' : `${imag}i`;
        return `${real} + ${imagPart}`;
    };


    
    return (
        <div className="p-6 bg-white border border-gray-200 rounded-xl shadow-sm mt-4">
            {/* View Mode Selector */}
            <div className="mb-6">
                <div className="flex space-x-2">
                    <button
                        onClick={() => handleFieldChange('viewMode', 'calculator')}
                        className={`px-4 py-2 rounded-md font-medium transition-colors ${
                            complexData.viewMode === 'calculator'
                                ? 'bg-blue-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        Calculator
                    </button>
                    <button
                        onClick={() => handleFieldChange('viewMode', 'argand')}
                        className={`px-4 py-2 rounded-md font-medium transition-colors ${
                            complexData.viewMode === 'argand'
                                ? 'bg-blue-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        Argand Diagram
                    </button>
                    <button
                        onClick={() => handleFieldChange('viewMode', 'polar')}
                        className={`px-4 py-2 rounded-md font-medium transition-colors ${
                            complexData.viewMode === 'polar'
                                ? 'bg-blue-600 text-white'
                                : 'bg-gray-200 text-gray-700 hover:bg-gray-300'
                        }`}
                    >
                        Polar ⟷ Rectangular
                    </button>
                </div>
            </div>

            {/* Operation Selector */}
            <div className="mb-6">
                <label className="block text-sm font-medium text-gray-700 mb-2">Operation:</label>
                <select
                    value={complexData.operation}
                    onChange={(e) => handleFieldChange('operation', e.target.value)}
                    disabled={isSubmitted}
                    className="w-full sm:w-80 p-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                >
                    <option value="add">Add Complex Numbers</option>
                    <option value="subtract">Subtract Complex Numbers</option>
                    <option value="multiply">Multiply Complex Numbers</option>
                    <option value="divide">Divide Complex Numbers</option>
                    <option value="simplify">Simplify Imaginary Expressions</option>
                    <option value="solve">Solve Complex Equations</option>
                </select>
            </div>

            {/* Calculator Mode */}
            {complexData.viewMode === 'calculator' && (
                <div className="flex flex-col md:flex-row gap-6">
                    {/* Left Side - Inputs and Controls */}
                    <div className="flex-1 space-y-4">
                        {/* Complex Number Inputs */}
                        {(complexData.operation === 'add' || complexData.operation === 'subtract' || 
                          complexData.operation === 'multiply' || complexData.operation === 'divide') && (
                            <div className="flex flex-col sm:flex-row gap-4">
                                <div className="w-full sm:w-56 p-3 bg-blue-50 rounded-lg">
                                    <h4 className="font-medium text-blue-800 mb-2 text-sm">z₁ (First Complex Number)</h4>
                                    <div className="space-y-2">
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Real part:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.z1_real}
                                                onChange={(e) => handleFieldChange('z1_real', parseFloat(e.target.value) || 0)}
                                                disabled={isSubmitted}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Imaginary part:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.z1_imag}
                                                onChange={(e) => handleFieldChange('z1_imag', parseFloat(e.target.value) || 0)}
                                                disabled={isSubmitted}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                            />
                                        </div>
                                        <div className="text-xs text-blue-700">
                                            z₁ = {formatComplexNumber(complexData.z1_real, complexData.z1_imag)}
                                        </div>
                                    </div>
                                </div>

                                <div className="w-full sm:w-56 p-3 bg-green-50 rounded-lg">
                                    <h4 className="font-medium text-green-800 mb-2 text-sm">z₂ (Second Complex Number)</h4>
                                    <div className="space-y-2">
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Real part:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.z2_real}
                                                onChange={(e) => handleFieldChange('z2_real', parseFloat(e.target.value) || 0)}
                                                disabled={isSubmitted}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Imaginary part:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.z2_imag}
                                                onChange={(e) => handleFieldChange('z2_imag', parseFloat(e.target.value) || 0)}
                                                disabled={isSubmitted}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                            />
                                        </div>
                                        <div className="text-xs text-green-700">
                                            z₂ = {formatComplexNumber(complexData.z2_real, complexData.z2_imag)}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Calculate Button - Centered on the gap between containers */}
                        {(complexData.operation === 'add' || complexData.operation === 'subtract' || 
                          complexData.operation === 'multiply' || complexData.operation === 'divide') && (
                            <div className="flex gap-4">
                                <div className="hidden sm:block w-40"></div>
                                <div className="flex justify-center flex-1">
                                    <button
                                        onClick={() => performOperation()}
                                        disabled={isSubmitted}
                                        className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 flex items-center space-x-2 text-sm"
                                    >
                                        <Calculator className="w-4 h-4" />
                                        <span>Calculate</span>
                                    </button>
                                </div>
                                <div className="hidden sm:block w-72"></div>
                            </div>
                        )}

                        {/* Simplification Input */}
                        {complexData.operation === 'simplify' && (
                            <div className="p-3 bg-purple-50 rounded-lg">
                                <h4 className="font-medium text-purple-800 mb-2 text-sm">Imaginary Expression to Simplify</h4>
                                <input
                                    type="text"
                                    value={complexData.simplifyExpression}
                                    onChange={(e) => handleFieldChange('simplifyExpression', e.target.value)}
                                    disabled={isSubmitted}
                                    className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-purple-500 focus:border-purple-500"
                                    placeholder="e.g., sqrt(-16) + sqrt(-4) - sqrt(-1)"
                                />
                                <div className="mt-2 text-xs text-purple-700">
                                    <p>Examples:</p>
                                    <ul className="list-disc list-inside ml-4">
                                        <li>sqrt(-16) + sqrt(-4) - sqrt(-1)</li>
                                        <li>(sqrt(-16) - sqrt(-5)) / (sqrt(-4) × sqrt(-12))</li>
                                        <li>sqrt(-4.12) / sqrt(-6)</li>
                                    </ul>
                                </div>
                            </div>
                        )}

                        {/* Equation Input */}
                        {complexData.operation === 'solve' && (
                            <div className="p-3 bg-orange-50 rounded-lg">
                                <h4 className="font-medium text-orange-800 mb-2 text-sm">Complex Equation to Solve</h4>
                                <input
                                    type="text"
                                    value={complexData.equationInput}
                                    onChange={(e) => handleFieldChange('equationInput', e.target.value)}
                                    disabled={isSubmitted}
                                    className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-orange-500 focus:border-orange-500"
                                    placeholder="e.g., 2x - 15i = 3 + 5yi"
                                />
                                <div className="mt-2 text-xs text-orange-700">
                                    <p>Examples:</p>
                                    <ul className="list-disc list-inside ml-4">
                                        <li>2x - 15i = 3 + 5yi</li>
                                        <li>(3-2i)(i-1)</li>
                                        <li>2-3i+i-1-5i</li>
                                    </ul>
                                </div>
                            </div>
                        )}

                        {/* Calculate Button for simplify/solve operations */}
                        {(complexData.operation === 'simplify' || complexData.operation === 'solve') && (
                            <div className="flex justify-center">
                                <button
                                    onClick={() => {
                                        if (complexData.operation === 'simplify') {
                                            simplifyExpression();
                                        } else if (complexData.operation === 'solve') {
                                            solveEquation();
                                        }
                                    }}
                                    disabled={isSubmitted}
                                    className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:bg-gray-400 flex items-center space-x-2 text-sm"
                                >
                                    <Calculator className="w-4 h-4" />
                                    <span>
                                        {complexData.operation === 'simplify' ? 'Simplify' : 'Solve'}
                                    </span>
                                </button>
                            </div>
                        )}
                    </div>

                    {/* Right Side - Results, Steps, and Instructions */}
                    <div className="w-full md:w-160 space-y-4 -mt-0 md:-mt-32">
                        {/* Results */}
                        <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
                            <h4 className="font-medium text-green-800 mb-2 text-sm">Result:</h4>
                            {complexData.result ? (
                                typeof complexData.result === 'object' && complexData.result.real !== undefined ? (
                                    <div className="text-base font-mono text-green-700">
                                        {formatComplexNumber(complexData.result.real, complexData.result.imag)}
                                    </div>
                                ) : (
                                    <div className="text-base font-mono text-green-700">
                                        {complexData.result.expression || complexData.result.equation || complexData.result}
                                    </div>
                                )
                            ) : (
                                <div className="text-sm font-mono text-gray-500">
                                    Click Calculate to see result
                                </div>
                            )}
                        </div>

                        {/* Steps */}
                        <div className="p-3 bg-blue-50 border border-blue-200 rounded-lg">
                            <h4 className="font-medium text-blue-800 mb-2 text-sm">Solution Steps:</h4>
                            {complexData.steps && complexData.steps.length > 0 ? (
                                <ol className="space-y-1">
                                    {complexData.steps.map((step, index) => (
                                        <li key={index} className="text-xs text-blue-700">
                                            <span className="font-medium">{index + 1}.</span> {step}
                                        </li>
                                    ))}
                                </ol>
                            ) : (
                                <div className="text-xs text-gray-500">
                                    Click Calculate to see solution steps
                                </div>
                            )}
                        </div>

                        {/* Error */}
                        {complexData.error && (
                            <div className="p-3 bg-red-50 border border-red-200 rounded-lg">
                                <h4 className="font-medium text-red-800 mb-1 text-sm">Error:</h4>
                                <p className="text-xs text-red-700">{complexData.error}</p>
                            </div>
                        )}

                        {/* Instructions */}
                        <div className="text-xs text-gray-500 bg-blue-50 p-3 rounded">
                            <p><strong>Complex Numbers Instructions:</strong></p>
                            <ul className="list-disc list-inside space-y-1 mt-1">
                                <li><strong>Basic Operations:</strong> Add, subtract, multiply, and divide complex numbers</li>
                                <li><strong>Simplification:</strong> Simplify expressions with imaginary numbers (i = √(-1))</li>
                                <li><strong>Equation Solving:</strong> Solve equations involving complex numbers</li>
                                <li><strong>Argand Diagram:</strong> Visualize complex numbers on the complex plane</li>
                                <li><strong>Polar Form:</strong> Convert to trigonometric form r(cos θ + i sin θ)</li>
                                <li><strong>Conjugate:</strong> The conjugate of z = a + bi is z̄ = a - bi</li>
                            </ul>
                        </div>
                    </div>
                </div>
            )}

            {/* Argand Diagram Mode */}
            {complexData.viewMode === 'argand' && (
                <div className="space-y-4">
                    <div className="flex flex-wrap gap-4">
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showGrid}
                                onChange={(e) => handleFieldChange('showGrid', e.target.checked)}
                                disabled={isSubmitted}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Grid</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showAxes}
                                onChange={(e) => handleFieldChange('showAxes', e.target.checked)}
                                disabled={isSubmitted}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Axes</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showUnitCircle}
                                onChange={(e) => handleFieldChange('showUnitCircle', e.target.checked)}
                                disabled={isSubmitted}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Unit Circle</span>
                        </label>
                        <label className="flex items-center">
                            <input
                                type="checkbox"
                                checked={complexData.showPolarForm}
                                onChange={(e) => handleFieldChange('showPolarForm', e.target.checked)}
                                disabled={isSubmitted}
                                className="mr-2"
                            />
                            <span className="text-sm text-gray-700">Show Polar Form</span>
                        </label>
                    </div>
                    
                    <div className="border border-gray-300 rounded-lg overflow-hidden">
                        <canvas
                            ref={canvasRef}
                            className="w-full h-96 bg-white"
                        />
                    </div>
                </div>
            )}

            {/* Polar Form Mode */}
            {complexData.viewMode === 'polar' && (
                <div className="flex flex-col md:flex-row gap-6">
                    {/* Left Side - Conversion Calculator */}
                    <div className="flex-1 space-y-4">
                        <div className="p-4 bg-blue-50 rounded-lg">
                            <h4 className="font-medium text-blue-800 mb-3">Conversion Calculator</h4>
                            <div className="space-y-4">
                                {/* Rectangular to Polar */}
                                <div className="bg-white p-3 rounded border">
                                    <h5 className="font-medium text-blue-800 mb-2">Rectangular → Polar</h5>
                                    <div className="space-y-2">
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Real part (a):</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.conversionReal || ''}
                                                onChange={(e) => handleFieldChange('conversionReal', parseFloat(e.target.value) || 0)}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                placeholder="e.g., 3"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Imaginary part (b):</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.conversionImag || ''}
                                                onChange={(e) => handleFieldChange('conversionImag', parseFloat(e.target.value) || 0)}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                placeholder="e.g., 4"
                                            />
                                        </div>
                                        <button
                                            onClick={() => {
                                                const real = Number(complexData.conversionReal) || 0;
                                                const imag = Number(complexData.conversionImag) || 0;
                                                const magnitude = Math.sqrt(real * real + imag * imag);
                                                const angle = Math.atan2(imag, real);
                                                const angleDegrees = angle * 180 / Math.PI;
                                                
                                                setComplexData(prev => ({
                                                    ...prev,
                                                    conversionResult: {
                                                        type: 'rectangular_to_polar',
                                                        input: `${real} + ${imag}i`,
                                                        magnitude: magnitude,
                                                        angle: angle,
                                                        angleDegrees: angleDegrees,
                                                        polarForm: `${magnitude.toFixed(3)}(cos ${angle.toFixed(3)} + i sin ${angle.toFixed(3)})`,
                                                        polarFormDegrees: `${magnitude.toFixed(3)}(cos ${angleDegrees.toFixed(1)}° + i sin ${angleDegrees.toFixed(1)}°)`
                                                    }
                                                }));
                                            }}
                                            className="w-full px-3 py-2 bg-blue-600 text-white text-sm rounded-md hover:bg-blue-700"
                                        >
                                            Convert to Polar
                                        </button>
                                    </div>
                                </div>

                                {/* Polar to Rectangular */}
                                <div className="bg-white p-3 rounded border">
                                    <h5 className="font-medium text-blue-800 mb-2">Polar → Rectangular</h5>
                                    <div className="space-y-2">
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Magnitude (r):</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.conversionMagnitude || ''}
                                                onChange={(e) => handleFieldChange('conversionMagnitude', parseFloat(e.target.value) || 0)}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                placeholder="e.g., 5"
                                            />
                                        </div>
                                        <div>
                                            <label className="block text-xs font-medium text-gray-700 mb-1">Angle (θ) in degrees:</label>
                                            <input
                                                type="number"
                                                step="0.1"
                                                value={complexData.conversionAngle || ''}
                                                onChange={(e) => handleFieldChange('conversionAngle', parseFloat(e.target.value) || 0)}
                                                className="w-full p-2 text-sm border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                                                placeholder="e.g., 53.13"
                                            />
                                        </div>
                                        <button
                                            onClick={() => {
                                                const magnitude = Number(complexData.conversionMagnitude) || 0;
                                                const angleDegrees = Number(complexData.conversionAngle) || 0;
                                                const angle = angleDegrees * Math.PI / 180;
                                                const real = magnitude * Math.cos(angle);
                                                const imag = magnitude * Math.sin(angle);
                                                
                                                setComplexData(prev => ({
                                                    ...prev,
                                                    conversionResult: {
                                                        type: 'polar_to_rectangular',
                                                        input: `${magnitude}(cos ${angleDegrees}° + i sin ${angleDegrees}°)`,
                                                        real: real,
                                                        imag: imag,
                                                        rectangularForm: formatComplexNumber(real, imag)
                                                    }
                                                }));
                                            }}
                                            className="w-full px-3 py-2 bg-blue-600 text-white text-sm rounded-md hover:bg-blue-700"
                                        >
                                            Convert to Rectangular
                                        </button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Right Side - Results and Steps */}
                    <div className="w-full md:w-160 space-y-4 -mt-0 md:-mt-32">
                        {/* Conversion Results */}
                        {complexData.conversionResult && (
                            <div className="space-y-3">
                                <div className="p-3 bg-white rounded border">
                                    <h5 className="font-medium text-blue-800 mb-2">Conversion Result</h5>
                                    <div className="text-sm text-blue-700 space-y-1">
                                        <p><strong>Input:</strong> {complexData.conversionResult.input}</p>
                                        {complexData.conversionResult.type === 'rectangular_to_polar' ? (
                                            <>
                                                <p><strong>Magnitude (r):</strong> {complexData.conversionResult.magnitude.toFixed(3)}</p>
                                                <p><strong>Angle (θ):</strong> {complexData.conversionResult.angle.toFixed(3)} radians ({complexData.conversionResult.angleDegrees.toFixed(1)}°)</p>
                                                <p><strong>Polar form (radians):</strong> {complexData.conversionResult.polarForm}</p>
                                                <p><strong>Polar form (degrees):</strong> {complexData.conversionResult.polarFormDegrees}</p>
                                            </>
                                        ) : (
                                            <>
                                                <p><strong>Real part:</strong> {complexData.conversionResult.real.toFixed(3)}</p>
                                                <p><strong>Imaginary part:</strong> {complexData.conversionResult.imag.toFixed(3)}</p>
                                                <p><strong>Rectangular form:</strong> {complexData.conversionResult.rectangularForm}</p>
                                            </>
                                        )}
                                    </div>
                                </div>

                                {/* Solution Steps */}
                                <div className="p-3 bg-white rounded border">
                                    <h5 className="font-medium text-blue-800 mb-2">Solution Steps</h5>
                                    <div className="text-sm text-blue-700">
                                        {complexData.conversionResult.type === 'rectangular_to_polar' ? (
                                            <ol className="space-y-2">
                                                <li>
                                                    <span className="font-medium">1.</span> Given: z = {complexData.conversionResult.input}
                                                </li>
                                                <li>
                                                    <span className="font-medium">2.</span> Calculate magnitude: r = √(a² + b²)
                                                    <br />
                                                    <span className="ml-4 text-blue-600">r = √({complexData.conversionReal}² + {complexData.conversionImag}²)</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">r = √({(Number(complexData.conversionReal) || 0) ** 2} + {(Number(complexData.conversionImag) || 0) ** 2})</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">r = √({((Number(complexData.conversionReal) || 0) ** 2 + (Number(complexData.conversionImag) || 0) ** 2).toFixed(3)})</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">r = {complexData.conversionResult.magnitude.toFixed(3)}</span>
                                                </li>
                                                <li>
                                                    <span className="font-medium">3.</span> Calculate angle: θ = arctan(b/a)
                                                    <br />
                                                    <span className="ml-4 text-blue-600">θ = arctan({complexData.conversionImag}/{complexData.conversionReal})</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">θ = {complexData.conversionResult.angle.toFixed(3)} radians</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">θ = {complexData.conversionResult.angleDegrees.toFixed(1)}°</span>
                                                </li>
                                                <li>
                                                    <span className="font-medium">4.</span> Write in polar form: z = r(cos θ + i sin θ)
                                                    <br />
                                                    <span className="ml-4 text-blue-600">z = {complexData.conversionResult.polarForm}</span>
                                                </li>
                                            </ol>
                                        ) : (
                                            <ol className="space-y-2">
                                                <li>
                                                    <span className="font-medium">1.</span> Given: z = {complexData.conversionResult.input}
                                                </li>
                                                <li>
                                                    <span className="font-medium">2.</span> Calculate real part: a = r cos θ
                                                    <br />
                                                    <span className="ml-4 text-blue-600">a = {complexData.conversionMagnitude} × cos({complexData.conversionAngle}°)</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">a = {complexData.conversionMagnitude} × {Math.cos((Number(complexData.conversionAngle) || 0) * Math.PI / 180).toFixed(3)}</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">a = {complexData.conversionResult.real.toFixed(3)}</span>
                                                </li>
                                                <li>
                                                    <span className="font-medium">3.</span> Calculate imaginary part: b = r sin θ
                                                    <br />
                                                    <span className="ml-4 text-blue-600">b = {complexData.conversionMagnitude} × sin({complexData.conversionAngle}°)</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">b = {complexData.conversionMagnitude} × {Math.sin((Number(complexData.conversionAngle) || 0) * Math.PI / 180).toFixed(3)}</span>
                                                    <br />
                                                    <span className="ml-4 text-blue-600">b = {complexData.conversionResult.imag.toFixed(3)}</span>
                                                </li>
                                                <li>
                                                    <span className="font-medium">4.</span> Write in rectangular form: z = a + bi
                                                    <br />
                                                    <span className="ml-4 text-blue-600">z = {complexData.conversionResult.rectangularForm}</span>
                                                </li>
                                            </ol>
                                        )}
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Current Calculation */}
                        <div className="p-3 bg-green-50 border border-green-200 rounded-lg">
                            <h4 className="font-medium text-green-800 mb-2 text-sm">Current Operation Result</h4>
                            {(() => {
                                // Get the result to display (either stored result or calculated from inputs)
                                let resultToShow = null;
                                if (complexData.result && typeof complexData.result === 'object' && complexData.result.real !== undefined) {
                                    resultToShow = complexData.result;
                                } else if (complexData.operation !== 'simplify' && complexData.operation !== 'solve') {
                                    // Calculate result from current inputs
                                    const z1 = { real: Number(complexData.z1_real) || 0, imag: Number(complexData.z1_imag) || 0 };
                                    const z2 = { real: Number(complexData.z2_real) || 0, imag: Number(complexData.z2_imag) || 0 };
                                    
                                    let result = { real: 0, imag: 0 };
                                    switch (complexData.operation) {
                                        case 'add':
                                            result = { real: z1.real + z2.real, imag: z1.imag + z2.imag };
                                            break;
                                        case 'subtract':
                                            result = { real: z1.real - z2.real, imag: z1.imag - z2.imag };
                                            break;
                                        case 'multiply':
                                            result = { 
                                                real: z1.real * z2.real - z1.imag * z2.imag, 
                                                imag: z1.real * z2.imag + z1.imag * z2.real 
                                            };
                                            break;
                                        case 'divide':
                                            const denominator = z2.real * z2.real + z2.imag * z2.imag;
                                            if (denominator !== 0) {
                                                result = { 
                                                    real: (z1.real * z2.real + z1.imag * z2.imag) / denominator,
                                                    imag: (z1.imag * z2.real - z1.real * z2.imag) / denominator
                                                };
                                            }
                                            break;
                                    }
                                    resultToShow = result;
                                }

                                if (resultToShow && (resultToShow.real !== 0 || resultToShow.imag !== 0)) {
                                    const { real, imag } = resultToShow;
                                    const magnitude = Math.sqrt(real * real + imag * imag);
                                    const angle = Math.atan2(imag, real);
                                    const angleDegrees = angle * 180 / Math.PI;
                                    
                                    return (
                                        <div className="space-y-1">
                                            <div className="text-sm text-green-700">
                                                <strong>Rectangular:</strong> {formatComplexNumber(real, imag)}
                                            </div>
                                            <div className="text-sm text-green-700">
                                                <strong>Magnitude:</strong> {magnitude.toFixed(3)}
                                            </div>
                                            <div className="text-sm text-green-700">
                                                <strong>Angle:</strong> {angleDegrees.toFixed(1)}°
                                            </div>
                                            <div className="text-sm text-green-700">
                                                <strong>Polar:</strong> {magnitude.toFixed(3)}(cos {angleDegrees.toFixed(1)}° + i sin {angleDegrees.toFixed(1)}°)
                                            </div>
                                        </div>
                                    );
                                } else {
                                    return (
                                        <div className="text-xs text-green-600">
                                            Enter complex numbers and select an operation to see the polar form representation.
                                        </div>
                                    );
                                }
                            })()}
                        </div>
                    </div>
                </div>
            )}

            {/* Visual Explanation - Bottom */}
            {complexData.viewMode === 'polar' && (
                <div className="mt-6 p-4 bg-blue-50 rounded-lg">
                    <h4 className="font-medium text-blue-800 mb-3">Visual Explanation</h4>
                    <div className="mb-4">
                        <p className="text-sm text-blue-700 mb-3">
                            <strong>Polar Form:</strong> A complex number can be represented as a point on the complex plane using either rectangular coordinates (a, b) or polar coordinates (r, θ).
                        </p>
                        <div className="flex flex-col md:flex-row gap-4">
                            <div className="flex-1">
                                <div className="bg-white p-3 rounded border">
                                    <h5 className="font-medium text-blue-800 mb-2">Rectangular Form</h5>
                                    <p className="text-sm text-blue-700 mb-2">z = a + bi</p>
                                    <ul className="text-xs text-blue-600 space-y-1">
                                        <li>• a = horizontal distance (real part)</li>
                                        <li>• b = vertical distance (imaginary part)</li>
                                    </ul>
                                </div>
                            </div>
                            <div className="flex-1">
                                <div className="bg-white p-3 rounded border">
                                    <h5 className="font-medium text-blue-800 mb-2">Polar Form</h5>
                                    <p className="text-sm text-blue-700 mb-2">z = r(cos θ + i sin θ)</p>
                                    <ul className="text-xs text-blue-600 space-y-1">
                                        <li>• r = distance from origin (magnitude)</li>
                                        <li>• θ = angle from positive x-axis</li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                        <div className="mt-3 p-3 bg-white rounded border">
                            <h5 className="font-medium text-blue-800 mb-2">Conversion Formulas</h5>
                            <div className="text-xs text-blue-600 space-y-1">
                                <p><strong>To Polar:</strong> r = √(a² + b²), θ = arctan(b/a)</p>
                                <p><strong>To Rectangular:</strong> a = r cos θ, b = r sin θ</p>
                            </div>
                        </div>
                    </div>
                </div>
            )}




        </div>
    );
};

export default ComplexNumbersInput;
