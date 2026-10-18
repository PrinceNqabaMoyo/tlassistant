import React, { useState, useEffect } from 'react';
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
    const [revealedModel, setRevealedModel] = useState(false);
    const [savedSelection, setSavedSelection] = useState(null);

    const diagramSpec = question.diagram_spec || question.diagram;
    const targetElement = question.correct_edge || question.correct_element || question.correct_answer || question.target_element;

    useEffect(() => {
        setSelectedElement(null);
        setRevealedModel(false);
        setSavedSelection(null);
    }, [question?.id]);

    const handleSelectEdge = (edgeKey) => {
        if (revealedModel) return;
        setSelectedElement(edgeKey);
        if (onCheck) {
            onCheck(edgeKey);
        }
    };

    const handleToggleRevealModel = () => {
        if (!revealedModel) {
            setSavedSelection(selectedElement);
            if (targetElement) {
                setSelectedElement(targetElement);
            }
            setRevealedModel(true);
        } else {
            setSelectedElement(savedSelection);
            setRevealedModel(false);
        }
    };

    return (
        <div className="space-y-6">
            {/* Model Target Element Active Banner */}
            {revealedModel && (
                <div data-testid="banner-diagram-model-active" className="p-2.5 rounded-xl bg-amber-50 border border-amber-300 text-xs text-amber-900 flex items-center justify-between shadow-2xs font-sans">
                    <div className="flex items-center gap-2">
                        <span className="font-bold">📖 Target Element Highlighted:</span>
                        <span>Showing expected geometric element on diagram. Click &quot;Restore My Selection&quot; to continue.</span>
                    </div>
                    <button
                        type="button"
                        onClick={handleToggleRevealModel}
                        className="text-amber-800 font-bold underline cursor-pointer text-xs shrink-0 ml-2"
                    >
                        Restore My Selection
                    </button>
                </div>
            )}

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
                        data-testid="btn-toggle-diagram-scaffold"
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
                <div className="flex flex-col items-center gap-4 p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs" data-testid="diagram-canvas-container">
                    <DiagramRenderer
                        spec={diagramSpec}
                        selectedEdge={selectedElement}
                        onSelectEdge={handleSelectEdge}
                    />
                    <div className="flex flex-wrap items-center justify-between w-full pt-2 border-t border-slate-100 gap-2">
                        <div className="flex items-center gap-3">
                            <span className="text-xs text-slate-500 font-medium">
                                {selectedElement ? `Selected: ${selectedElement}` : 'Click an edge or angle to select'}
                            </span>
                            {Boolean(result) && targetElement && (
                                <button
                                    type="button"
                                    data-testid="btn-reveal-diagram-model"
                                    onClick={handleToggleRevealModel}
                                    className={`px-3 py-1.5 rounded-xl text-xs font-bold transition shadow-xs cursor-pointer flex items-center gap-1.5 font-sans ${
                                        revealedModel
                                            ? 'bg-amber-600 hover:bg-amber-700 text-white'
                                            : 'bg-white text-[#13519C] border border-[#13519C]/40 hover:bg-blue-50'
                                    }`}
                                >
                                    <span>{revealedModel ? '↩ Restore My Selection' : '👁️ Highlight Target Element'}</span>
                                </button>
                            )}
                        </div>
                        <button
                            type="button"
                            data-testid="btn-check-answer"
                            onClick={() => onCheck && onCheck(selectedElement)}
                            disabled={isChecking || !selectedElement}
                            className="px-5 py-2 rounded-xl text-xs font-bold bg-[#13519C] hover:bg-blue-800 text-white transition shadow-xs cursor-pointer disabled:opacity-50 active:scale-98 font-sans"
                        >
                            {isChecking ? 'Checking...' : 'Check Selection'}
                        </button>
                    </div>
                </div>
            )}
        </div>
    );
}
