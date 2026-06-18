import React from 'react';
import { X } from 'lucide-react';

// Import all math components
import AlgebraicExpressionBuilder from '../math/AlgebraicExpressionBuilder';
import ComplexNumbersInput from '../math/ComplexNumbersInput';
import GeometryStudio from '../math/GeometryStudio';

const ComponentOverlay = ({ 
    selectedComponent, 
    isVisible, 
    isFullscreen, 
    onClose, 
    onToggleFullscreen,
    setView 
}) => {
    if (!isVisible || !selectedComponent) return null;

    const renderComponent = () => {
        switch (selectedComponent.type) {
            case 'algebraic_expression_builder':
                return (
                    <AlgebraicExpressionBuilder 
                        initialData={{
                            title: "Algebraic Expression",
                            expression: "2x + 3y",
                            variables: ["x", "y"],
                            showSteps: true
                        }}
                        onChange={() => {}}
                        isSubmitted={false}
                        aiInput={{
                            expression: "2x + 3y",
                            operation: "simplify",
                            instructions: "Simplify the expression step by step",
                            steps: "First, identify the terms in the expression. Then, combine like terms. Finally, write the simplified result."
                        }}
                    />
                );

            case 'complex_numbers':
                return (
                    <ComplexNumbersInput 
                        initialData={{
                            title: "Complex Numbers Calculator",
                            operation: 'add',
                            viewMode: 'calculator',
                            z1_real: 3,
                            z1_imag: 2,
                            z2_real: 1,
                            z2_imag: -1,
                            simplifyExpression: 'sqrt(-16) + sqrt(-4) - sqrt(-1)',
                            equationInput: '2x - 15i = 3 + 5yi',
                            showGrid: true,
                            showAxes: true,
                            showUnitCircle: false,
                            showPolarForm: false
                        }}
                        onChange={() => {}}
                        isSubmitted={false}
                    />
                );

            case 'geometry_studio':
                return (
                    <GeometryStudio 
                        initialData={{
                            title: "Geometry Studio",
                            mode: '2d',
                            viewMode: 'construction',
                            showGrid: true,
                            showAxes: true,
                            showLabels: true,
                            gridSize: 20,
                            unitScale: 1,
                            backgroundColor: '#ffffff',
                            gridColor: '#e5e7eb',
                            axisColor: '#374151',
                            shapeColor: '#3B82F6',
                            pointColor: '#EF4444',
                            lineColor: '#10B981',
                            points: [],
                            lines: [],
                            shapes: [],
                            shapes3D: [],
                            circles: [],
                            angles: [],
                            sectors: []
                        }}
                        onChange={() => {}}
                        isSubmitted={false}
                        setView={setView}
                    />
                );

            default:
                return (
                    <div className="text-center text-gray-500 py-8">
                        <p>Component: {selectedComponent.name}</p>
                        <p className="text-sm mt-2">Type: {selectedComponent.type}</p>
                        <p className="text-sm">Category: {selectedComponent.category}</p>
                        <p className="text-sm mt-4 text-gray-400">Component not yet implemented</p>
                    </div>
                );
        }
    };

    return (
        <div className={`fixed inset-0 z-50 flex items-center justify-center ${(selectedComponent.type === 'algebraic_expression_builder' || selectedComponent.type === 'complex_numbers') ? 'bg-white' : (isFullscreen ? 'bg-white' : 'bg-slate-900/20 backdrop-blur-sm')}`}>
            <div className={`relative ${(selectedComponent.type === 'algebraic_expression_builder' || selectedComponent.type === 'complex_numbers') ? 'w-full h-full' : (isFullscreen ? 'w-full h-full' : 'w-11/12 max-w-4xl h-5/6')} bg-white rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-slate-200`}>
                {/* Header */}
                <div className="flex items-center justify-between p-4 border-b border-slate-100 bg-slate-50/50">
                    <h3 className="text-lg font-bold text-slate-800 px-2">
                        {selectedComponent.name}
                    </h3>
                    <div className="flex items-center space-x-2">
                        {(selectedComponent.type !== 'algebraic_expression_builder' && selectedComponent.type !== 'complex_numbers') && (
                            <button
                                onClick={onToggleFullscreen}
                                className="p-2 text-slate-500 hover:text-slate-800 hover:bg-white rounded-xl transition-colors border border-transparent hover:border-slate-200 shadow-sm"
                                title={isFullscreen ? 'Exit Fullscreen' : 'Fullscreen'}
                            >
                                {isFullscreen ? (
                                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
                                    </svg>
                                ) : (
                                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                        <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 8V4m0 0h4M4 4l5 5m11-1V4m0 0h-4m4 0l-5 5M4 16v4m0 0h4m-4 0l5-5m11 5l-5-5m5 5v-4m0 4h-4" />
                                    </svg>
                                )}
                            </button>
                        )}
                        <button
                            onClick={onClose}
                            className="p-2 text-slate-500 hover:text-red-600 hover:bg-red-50 rounded-xl transition-colors border border-transparent hover:border-red-100 shadow-sm"
                            title="Close"
                        >
                            <X className="h-5 w-5" />
                        </button>
                    </div>
                </div>

                {/* Component Content */}
                <div className={`flex-1 ${(selectedComponent.type === 'algebraic_expression_builder' || selectedComponent.type === 'complex_numbers') ? 'px-6 pb-6 pt-[18px]' : 'p-6'} overflow-y-auto bg-white`}>
                    {renderComponent()}
                </div>
            </div>
        </div>
    );
};

export default ComponentOverlay;
