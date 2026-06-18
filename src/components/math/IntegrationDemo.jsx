import React, { useState } from 'react';
import IntegratedExponentialLogarithmicFunction from './IntegratedExponentialLogarithmicFunction';

const IntegrationDemo = () => {
    const [demoData, setDemoData] = useState({
        functionType: 'exponential',
        a: 1,
        b: 2,
        c: 0,
        d: 0,
        base: 'e',
        customBase: 2
    });

    const handleDataChange = (newData) => {
        setDemoData(newData);
        console.log('Function data updated:', newData);
    };

    return (
        <div className="p-6 bg-gray-50 min-h-screen">
            <div className="max-w-6xl mx-auto">
                <div className="text-center mb-8">
                    <h1 className="text-3xl font-bold text-gray-800 mb-4">
                        Exponential & Logarithmic Functions Integration Demo
                    </h1>
                    <p className="text-lg text-gray-600 max-w-3xl mx-auto">
                        This unified component demonstrates the integration of exponential and logarithmic functions 
                        with adaptive parameter interpretation, real-time graphing, and enhanced mathematical analysis.
                    </p>
                </div>

                <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">Key Features Demonstrated</h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        <div className="space-y-2">
                            <h3 className="font-medium text-blue-600">✅ Function Type Toggle</h3>
                            <p className="text-sm text-gray-600">Switch between exponential and logarithmic functions seamlessly</p>
                            
                            <h3 className="font-medium text-blue-600">✅ Adaptive Parameter Interface</h3>
                            <p className="text-sm text-gray-600">Parameter labels change based on function type (a: stretch vs coefficient)</p>
                            
                            <h3 className="font-medium text-blue-600">✅ Real-time Graphing</h3>
                            <p className="text-sm text-gray-600">Instant visual feedback as parameters change</p>
                        </div>
                        <div className="space-y-2">
                            <h3 className="font-medium text-blue-600">✅ Enhanced Function Properties</h3>
                            <p className="text-sm text-gray-600">Automatic calculation of domain, range, asymptotes, and behavior</p>
                            
                            <h3 className="font-medium text-blue-600">✅ Base Selection (Logarithmic)</h3>
                            <p className="text-sm text-gray-600">Choose from natural (e), binary (2), decimal (10), or custom base</p>
                            
                            <h3 className="font-medium text-blue-600">✅ Full Screen Mode</h3>
                            <p className="text-sm text-gray-600">Enhanced viewing experience for detailed analysis</p>
                        </div>
                    </div>
                </div>

                <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">Current Function Data</h2>
                    <div className="bg-gray-50 p-4 rounded-lg">
                        <pre className="text-sm text-gray-700 overflow-x-auto">
                            {JSON.stringify(demoData, null, 2)}
                        </pre>
                    </div>
                </div>

                {/* The Integrated Component */}
                                        <IntegratedExponentialLogarithmicFunction
                    initialData={demoData}
                    onChange={handleDataChange}
                    isSubmitted={false}
                />

                <div className="bg-white rounded-lg shadow-lg p-6 mt-6">
                    <h2 className="text-xl font-semibold text-gray-800 mb-4">How It Works</h2>
                    <div className="space-y-4">
                        <div>
                            <h3 className="font-medium text-green-600 mb-2">1. Function Type Selection</h3>
                            <p className="text-sm text-gray-600">
                                Click the blue (Exponential) or green (Logarithmic) buttons to switch between function types. 
                                The parameter interface automatically adapts to show the appropriate labels and controls.
                            </p>
                        </div>
                        
                        <div>
                            <h3 className="font-medium text-green-600 mb-2">2. Parameter Interpretation</h3>
                            <p className="text-sm text-gray-600">
                                <strong>Exponential:</strong> a (stretch), b (base), c (horizontal shift), d (vertical shift)<br/>
                                <strong>Logarithmic:</strong> a (coefficient), b (linear), c (constant), d (vertical shift)
                            </p>
                        </div>
                        
                        <div>
                            <h3 className="font-medium text-green-600 mb-2">3. Real-time Analysis</h3>
                            <p className="text-sm text-gray-600">
                                As you adjust parameters, the function display updates automatically, showing the current equation, 
                                behavior, domain, range, and asymptotes. The graph redraws in real-time.
                            </p>
                        </div>
                        
                        <div>
                            <h3 className="font-medium text-green-600 mb-2">4. Mathematical Properties</h3>
                            <p className="text-sm text-gray-600">
                                The component automatically calculates and displays key mathematical properties including 
                                domain restrictions, range analysis, asymptote locations, and function behavior.
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default IntegrationDemo;
