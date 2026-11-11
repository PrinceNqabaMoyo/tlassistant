import React, { useState, useEffect } from 'react';
import DiagramRenderer from '../shared/mathx/DiagramRenderer';
import MathText from '../shared/mathx/MathText';

export default function DiagramModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
    hideStimulusDiagram = false,
}) {
    if (!question) return null;

    const [selectedElement, setSelectedElement] = useState(null);
    const [typedAnswer, setTypedAnswer] = useState('');
    const [revealedModel, setRevealedModel] = useState(false);
    const [savedSelection, setSavedSelection] = useState(null);

    const diagramSpec = question.diagram_spec || question.diagram || question.graph || question.function_graph;
    const targetElement =
        question.correct_edge ||
        question.correct_element ||
        question.correct_answer ||
        question.answer_latex ||
        question.sample_answer ||
        question.target_element;

    const hasSelectableEdges =
        question.question_type === 'diagram_select' ||
        Boolean(question.correct_edge) ||
        (Array.isArray(diagramSpec?.sides) && diagramSpec.sides.length > 0);

    const mcqOptions = question.options_latex || question.options;

    useEffect(() => {
        setSelectedElement(null);
        setTypedAnswer('');
        setRevealedModel(false);
        setSavedSelection(null);
    }, [question?.id]);

    const handleSelectEdge = (edgeKey) => {
        if (revealedModel) return;
        setSelectedElement(edgeKey);
    };

    const handleToggleRevealModel = () => {
        if (!revealedModel) {
            setSavedSelection(selectedElement || typedAnswer);
            if (targetElement) {
                setSelectedElement(String(targetElement));
                setTypedAnswer(String(targetElement));
            }
            setRevealedModel(true);
        } else {
            setSelectedElement(savedSelection);
            setTypedAnswer(savedSelection || '');
            setRevealedModel(false);
        }
    };

    const activeAnswer = selectedElement || typedAnswer.trim();

    return (
        <div className="space-y-6">
            {/* Model Target Element Active Banner */}
            {revealedModel && (
                <div data-testid="banner-diagram-model-active" className="p-2.5 rounded-xl bg-amber-50 border border-amber-300 text-xs text-amber-900 flex items-center justify-between shadow-2xs font-sans">
                    <div className="flex items-center gap-2">
                        <span className="font-bold">📖 Target Element Highlighted:</span>
                        <span>Showing expected geometric/graphical solution. Click &quot;Restore My Selection&quot; to continue.</span>
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
                            Geometric &amp; Graphical Properties
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
                        <p className="font-semibold text-slate-800">Theorem &amp; Graph Analysis Prompts:</p>
                        <p>• Identify key coordinates, intercepts, stationary points, or angle relationships on the figure.</p>
                        <p>• Exterior angle of a triangle equals the sum of two opposite interior angles.</p>
                        <p>• Corresponding, alternate, and co-interior angles on parallel lines.</p>
                    </div>
                )}
            </div>

            {/* Interactive GeoGebra+ / JSXGraph Diagram Canvas */}
            {diagramSpec && (
                <div className="flex flex-col items-center gap-4 p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs" data-testid="diagram-canvas-container">
                    {(!hideStimulusDiagram || hasSelectableEdges) && (
                        <DiagramRenderer
                            spec={diagramSpec}
                            interactive={true}
                            selectedEdge={selectedElement}
                            onSelectEdge={handleSelectEdge}
                            graded={Boolean(result)}
                            correctEdge={result?.correct_edge || targetElement}
                        />
                    )}

                    {/* MCQ Options if present */}
                    {Array.isArray(mcqOptions) && mcqOptions.length > 0 && (
                        <div className="w-full grid grid-cols-1 sm:grid-cols-2 gap-2.5 pt-2">
                            {mcqOptions.map((opt, idx) => {
                                const isSel = selectedElement === idx || selectedElement === opt;
                                return (
                                    <button
                                        key={idx}
                                        type="button"
                                        data-testid={`btn-diagram-mcq-${idx}`}
                                        onClick={() => !revealedModel && setSelectedElement(question.correct_index !== undefined ? idx : opt)}
                                        className={`p-3 rounded-xl border text-left text-xs font-medium transition cursor-pointer ${
                                            isSel
                                                ? 'border-[#13519C] bg-blue-50/70 text-[#13519C] font-bold'
                                                : 'border-slate-200 bg-white text-slate-700 hover:bg-slate-50'
                                        }`}
                                    >
                                        <MathText text={String(opt)} />
                                    </button>
                                );
                            })}
                        </div>
                    )}

                    {/* Mathematical / Numeric Input for non-edge-click calculation questions */}
                    {!hasSelectableEdges && (!Array.isArray(mcqOptions) || mcqOptions.length === 0) && (
                        <div className="w-full pt-2">
                            <label className="block text-xs font-semibold text-slate-600 mb-1.5">
                                Enter your calculated answer or coordinates:
                            </label>
                            <input
                                type="text"
                                data-testid="diagram-math-answer-input"
                                value={typedAnswer}
                                onChange={(e) => {
                                    if (revealedModel) return;
                                    setTypedAnswer(e.target.value);
                                    setSelectedElement(e.target.value);
                                }}
                                placeholder="e.g. 45° or (2; -4) or 52,36"
                                className="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm font-mono text-slate-800 focus:outline-none focus:border-[#13519C] focus:ring-2 focus:ring-[#13519C]/15"
                            />
                        </div>
                    )}

                    <div className="flex flex-wrap items-center justify-between w-full pt-2 border-t border-slate-100 gap-2">
                        <div className="flex items-center gap-3">
                            <span className="text-xs text-slate-500 font-medium">
                                {activeAnswer !== null && activeAnswer !== ''
                                    ? `Selected: ${activeAnswer}`
                                    : hasSelectableEdges
                                    ? 'Click an edge or angle to select'
                                    : 'Inspect the figure above and enter your answer'}
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
                            onClick={() => onCheck && onCheck(activeAnswer)}
                            disabled={isChecking || activeAnswer === null || activeAnswer === ''}
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
