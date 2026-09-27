import React, { useState } from 'react';
import DiagramRenderer from '../shared/mathx/DiagramRenderer';

export default function DiagramModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
}) {
    if (!question) return null;

    const [selectedElement, setSelectedElement] = useState(null);
    const diagramSpec = question.diagram_spec || question.diagram;

    const handleSelectEdge = (edgeKey) => {
        setSelectedElement(edgeKey);
        if (onCheck) {
            onCheck(edgeKey);
        }
    };

    return (
        <div className="space-y-6">
            {/* Dynamic Diagram Scaffold Guidance */}
            <div className="rounded-2xl border border-blue-200 bg-blue-50/60 p-4 transition-all">
                <div className="flex items-center justify-between">
                    <div className="flex items-center gap-2">
                        <span className="grid place-items-center h-6 w-6 rounded-lg bg-brand-blue text-white text-xs font-bold">
                            📐
                        </span>
                        <span className="text-sm font-bold text-brand-blue">
                            Geometric Properties &amp; Theorems
                        </span>
                    </div>
                    <button
                        type="button"
                        onClick={onToggleScaffold}
                        className="text-xs font-bold text-brand-blue hover:underline cursor-pointer"
                    >
                        {showDynamicScaffold ? 'Hide Guidance ▲' : 'Show Theorem Rules ▼'}
                    </button>
                </div>

                {showDynamicScaffold && (
                    <div className="mt-3 pt-3 border-t border-blue-100 text-xs text-slate-700 space-y-1">
                        <p className="font-semibold text-slate-800">Theorem Prompts:</p>
                        <p>• Identify whether angles are complementary (\(90^\circ\)) or supplementary (\(180^\circ\)).</p>
                        <p>• Exterior angle of a triangle equals the sum of two opposite interior angles.</p>
                        <p>• Corresponding, alternate, and co-interior angles on parallel lines.</p>
                    </div>
                )}
            </div>

            {/* Interactive JSXGraph Diagram Canvas */}
            {diagramSpec && (
                <div className="flex justify-center p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs">
                    <DiagramRenderer
                        spec={diagramSpec}
                        selectedEdge={selectedElement}
                        onSelectEdge={handleSelectEdge}
                    />
                </div>
            )}
        </div>
    );
}
