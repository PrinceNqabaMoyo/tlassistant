import React, { useState } from 'react';
import MathText from '../shared/mathx/MathText';
import MathAnswerArea from '../shared/mathx/MathAnswerArea';
import { Zap, Info } from 'lucide-react';

export default function CircuitModalityRenderer({
    question,
    topic,
    onCheck,
    result,
    isChecking,
    showDynamicScaffold,
    onToggleScaffold,
    hideStimulusDiagram = false,
    stimulusOnly = false,
}) {
    if (!question) return null;

    const [selectedComponent, setSelectedComponent] = useState(null);
    const spec = question.circuit_spec || question.diagram_spec || {};
    const circuitType = spec.type || (question.prompt?.toLowerCase().includes('parallel') ? 'parallel' : 'series');
    const components = spec.components || [];

    // Extract component values or fall back to question data
    const battery = components.find(c => c.type === 'battery') || { label: 'Battery', voltage: spec.voltage || 12 };
    const switchComp = components.find(c => c.type === 'switch') || { state: 'closed' };
    const ammeter = components.find(c => c.type === 'ammeter') || { label: 'A' };
    const resistors = components.filter(c => c.type === 'resistor');
    const voltmeters = components.filter(c => c.type === 'voltmeter');

    // Default 2 resistors if none explicitly specified in spec
    const activeResistors = resistors.length > 0 ? resistors : [
        { id: 'R1', label: 'R₁', resistance: 4 },
        { id: 'R2', label: 'R₂', resistance: 6 }
    ];

    return (
        <div className="space-y-6">
            {/* Circuit Schematic Card */}
            {!hideStimulusDiagram && (
            <div 
                data-testid="circuit-schematic-canvas" 
                className="p-4 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-3 font-sans"
            >
                <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                    <div className="flex items-center gap-2">
                        <span className="w-6 h-6 rounded-lg bg-amber-500 text-white flex items-center justify-center text-xs font-bold shadow-2xs">
                            <Zap className="w-3.5 h-3.5" />
                        </span>
                        <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                            Electric Circuit Schematic ({circuitType.toUpperCase()})
                        </span>
                    </div>
                    <span className="text-[11px] font-mono text-slate-500 font-semibold bg-slate-100 px-2 py-0.5 rounded">
                        Interactive SVG Diagram
                    </span>
                </div>

                {/* SVG Circuit Canvas */}
                <div className="flex justify-center items-center bg-slate-50/70 p-3 rounded-xl border border-slate-200/80 overflow-x-auto">
                    <svg viewBox="0 0 500 240" className="w-full max-w-[500px] h-auto select-none" style={{ minWidth: '320px' }}>
                        {/* Outer loop wires */}
                        <path
                            d="M 60 120 L 60 40 L 440 40 L 440 200 L 60 200 L 60 120"
                            fill="none"
                            stroke="#334155"
                            strokeWidth="2.5"
                            strokeLinecap="round"
                            strokeLinejoin="round"
                        />

                        {/* Top Rail: Battery (Left) and Switch (Right) */}
                        {/* Battery */}
                        <g 
                            data-testid="circuit-component-battery"
                            className="cursor-pointer transition-transform hover:scale-105"
                            onClick={() => setSelectedComponent(battery)}
                        >
                            <rect x="130" y="25" width="60" height="30" fill="white" stroke="none" />
                            {/* Positive plate (longer, thinner) */}
                            <line x1="150" y1="28" x2="150" y2="52" stroke="#13519C" strokeWidth="3" />
                            {/* Negative plate (shorter, thicker) */}
                            <line x1="160" y1="34" x2="160" y2="46" stroke="#13519C" strokeWidth="5" />
                            <text x="142" y="24" fontSize="11" fill="#13519C" fontWeight="bold" textAnchor="middle">+</text>
                            <text x="168" y="24" fontSize="11" fill="#13519C" fontWeight="bold" textAnchor="middle">−</text>
                            <text x="155" y="65" fontSize="11" fill="#1e293b" fontWeight="600" textAnchor="middle" fontFamily="monospace">
                                {battery.label || `${battery.voltage || 12} V`}
                            </text>
                        </g>

                        {/* Switch */}
                        <g 
                            data-testid="circuit-component-switch"
                            className="cursor-pointer"
                            onClick={() => setSelectedComponent({ type: 'switch', state: switchComp.state || 'closed' })}
                        >
                            <rect x="290" y="30" width="40" height="20" fill="white" stroke="none" />
                            <circle cx="295" cy="40" r="3" fill="#334155" />
                            <circle cx="325" cy="40" r="3" fill="#334155" />
                            {switchComp.state === 'open' ? (
                                <line x1="295" y1="40" x2="320" y2="28" stroke="#E11D48" strokeWidth="2.5" />
                            ) : (
                                <line x1="295" y1="40" x2="325" y2="40" stroke="#10B981" strokeWidth="2.5" />
                            )}
                            <text x="310" y="22" fontSize="10" fill="#475569" fontWeight="bold" textAnchor="middle" fontFamily="monospace">
                                Switch ({switchComp.state === 'open' ? 'Open' : 'Closed'})
                            </text>
                        </g>

                        {/* Right Rail: Ammeter */}
                        <g 
                            data-testid="circuit-component-ammeter"
                            className="cursor-pointer"
                            onClick={() => setSelectedComponent({ type: 'ammeter', reading: ammeter.reading })}
                        >
                            <circle cx="440" cy="120" r="16" fill="white" stroke="#13519C" strokeWidth="2.5" />
                            <text x="440" y="125" fontSize="13" fill="#13519C" fontWeight="bold" textAnchor="middle" fontFamily="monospace">A</text>
                            <text x="465" y="124" fontSize="10" fill="#64748b" fontWeight="bold">Ammeter</text>
                        </g>

                        {/* Bottom Rail: Resistors */}
                        {circuitType === 'series' ? (
                            /* Series: R1 and R2 along the bottom rail */
                            <g>
                                {/* Resistor 1 */}
                                <g 
                                    data-testid="circuit-component-resistor-1"
                                    className="cursor-pointer"
                                    onClick={() => setSelectedComponent(activeResistors[0])}
                                >
                                    <rect x="130" y="188" width="60" height="24" fill="white" stroke="#475569" strokeWidth="2" rx="3" />
                                    <text x="160" y="204" fontSize="11" fill="#0f172a" fontWeight="bold" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[0]?.label || 'R₁'}
                                    </text>
                                    <text x="160" y="226" fontSize="10" fill="#2563eb" fontWeight="600" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[0]?.resistance ? `${activeResistors[0].resistance} Ω` : ''}
                                    </text>
                                </g>

                                {/* Resistor 2 */}
                                <g 
                                    data-testid="circuit-component-resistor-2"
                                    className="cursor-pointer"
                                    onClick={() => setSelectedComponent(activeResistors[1])}
                                >
                                    <rect x="270" y="188" width="60" height="24" fill="white" stroke="#475569" strokeWidth="2" rx="3" />
                                    <text x="300" y="204" fontSize="11" fill="#0f172a" fontWeight="bold" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[1]?.label || 'R₂'}
                                    </text>
                                    <text x="300" y="226" fontSize="10" fill="#2563eb" fontWeight="600" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[1]?.resistance ? `${activeResistors[1].resistance} Ω` : ''}
                                    </text>
                                </g>
                            </g>
                        ) : (
                            /* Parallel: Two parallel branches between x=160 and x=320 */
                            <g>
                                {/* Branch splits */}
                                <line x1="160" y1="200" x2="160" y2="160" stroke="#334155" strokeWidth="2.5" />
                                <line x1="160" y1="160" x2="320" y2="160" stroke="#334155" strokeWidth="2.5" />
                                <line x1="320" y1="160" x2="320" y2="200" stroke="#334155" strokeWidth="2.5" />

                                {/* Upper Parallel Branch: Resistor 1 */}
                                <g 
                                    data-testid="circuit-component-resistor-1"
                                    className="cursor-pointer"
                                    onClick={() => setSelectedComponent(activeResistors[0])}
                                >
                                    <rect x="210" y="148" width="60" height="24" fill="white" stroke="#475569" strokeWidth="2" rx="3" />
                                    <text x="240" y="164" fontSize="11" fill="#0f172a" fontWeight="bold" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[0]?.label || 'R₁'}
                                    </text>
                                    <text x="240" y="142" fontSize="10" fill="#2563eb" fontWeight="600" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[0]?.resistance ? `${activeResistors[0].resistance} Ω` : ''}
                                    </text>
                                </g>

                                {/* Lower Parallel Branch: Resistor 2 */}
                                <g 
                                    data-testid="circuit-component-resistor-2"
                                    className="cursor-pointer"
                                    onClick={() => setSelectedComponent(activeResistors[1])}
                                >
                                    <rect x="210" y="188" width="60" height="24" fill="white" stroke="#475569" strokeWidth="2" rx="3" />
                                    <text x="240" y="204" fontSize="11" fill="#0f172a" fontWeight="bold" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[1]?.label || 'R₂'}
                                    </text>
                                    <text x="240" y="226" fontSize="10" fill="#2563eb" fontWeight="600" textAnchor="middle" fontFamily="monospace">
                                        {activeResistors[1]?.resistance ? `${activeResistors[1].resistance} Ω` : ''}
                                    </text>
                                </g>
                            </g>
                        )}

                        {/* Optional Voltmeter bridged across R1 */}
                        <g 
                            data-testid="circuit-component-voltmeter"
                            className="cursor-pointer"
                            onClick={() => setSelectedComponent(voltmeters[0] || { type: 'voltmeter', label: 'V₁' })}
                        >
                            <line x1="110" y1="200" x2="110" y2="230" stroke="#94a3b8" strokeDasharray="3 3" strokeWidth="1.5" />
                            <line x1="110" y1="230" x2="210" y2="230" stroke="#94a3b8" strokeDasharray="3 3" strokeWidth="1.5" />
                            <line x1="210" y1="230" x2="210" y2="200" stroke="#94a3b8" strokeDasharray="3 3" strokeWidth="1.5" />
                            <circle cx="160" cy="230" r="12" fill="white" stroke="#059669" strokeWidth="2" />
                            <text x="160" y="234" fontSize="11" fill="#059669" fontWeight="bold" textAnchor="middle" fontFamily="monospace">V</text>
                        </g>
                    </svg>
                </div>

                {/* Selected Component Inspector Pill */}
                {selectedComponent && (
                    <div className="flex items-center gap-2 p-2 bg-blue-50 border border-blue-200 rounded-lg text-xs text-blue-900 animate-in fade-in">
                        <Info className="w-3.5 h-3.5 text-blue-600 shrink-0" />
                        <span>
                            <strong>Selected:</strong> {selectedComponent.label || selectedComponent.type}
                            {selectedComponent.resistance && ` • Resistance: ${selectedComponent.resistance} Ω`}
                            {selectedComponent.voltage && ` • Voltage: ${selectedComponent.voltage} V`}
                            {selectedComponent.state && ` • State: ${selectedComponent.state}`}
                        </span>
                    </div>
                )}
            </div>
            )}

            {/* Response Area (MCQ / Keypad / Short Answer) */}
            {!stimulusOnly && (
            <MathAnswerArea
                question={question}
                topic={topic}
                onCheck={onCheck}
                result={result}
                busy={isChecking}
            />
            )}
        </div>
    );
}
