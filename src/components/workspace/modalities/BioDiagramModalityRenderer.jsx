import React, { useState } from 'react';
import MathText from '../shared/mathx/MathText';
import MathAnswerArea from '../shared/mathx/MathAnswerArea';
import { Microscope, Zap, Atom, Globe, Compass, FileText, CheckCircle, AlertCircle } from 'lucide-react';
import { getBankedDiagramComponent } from './diagram_bank';

function getDiagramMetadata(diagramType) {
    const dt = String(diagramType || '').toLowerCase();
    if (/circuit|electric|wave|doppler|pulley|incline|generator|motor|hydraulic|geyser|heater|resistor/i.test(dt)) {
        return {
            title: 'Physics & Electrical Schematic',
            Icon: Zap,
            colorClass: 'bg-amber-600',
            bgClass: 'bg-amber-50/20 border-amber-100',
        };
    }
    if (/galvanic|titration|distillation|electrolytic|reaction|gas_evolution|bonding|bohr|atom|particle|matter/i.test(dt)) {
        return {
            title: 'Chemistry & Laboratory Apparatus',
            Icon: Atom,
            colorClass: 'bg-indigo-600',
            bgClass: 'bg-indigo-50/20 border-indigo-100',
        };
    }
    if (/solar|space|planet|earth|lithosphere|telescope|astronom/i.test(dt)) {
        return {
            title: 'Earth & Space Science Diagram',
            Icon: Globe,
            colorClass: 'bg-blue-600',
            bgClass: 'bg-blue-50/20 border-blue-100',
        };
    }
    if (/cell|heart|eye|ear|nephron|reproductive|digestive|villus|mitosis|meiosis|endocrine|leaf|alveolus|lung|organ|microorganism/i.test(dt)) {
        return {
            title: 'Life Sciences Anatomical Diagram',
            Icon: Microscope,
            colorClass: 'bg-teal-600',
            bgClass: 'bg-emerald-50/30 border-emerald-100',
        };
    }
    if (/floor|plan|architectural|geometric/i.test(dt)) {
        return {
            title: 'Technical & Geometric Schematic',
            Icon: Compass,
            colorClass: 'bg-slate-700',
            bgClass: 'bg-slate-50 border-slate-200',
        };
    }
    return {
        title: 'Scientific Reference Diagram',
        Icon: FileText,
        colorClass: 'bg-indigo-700',
        bgClass: 'bg-slate-50 border-slate-200',
    };
}

export default function BioDiagramModalityRenderer({
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

    const [activePin, setActivePin] = useState(null);
    const spec = question.diagram_spec || question.diagram || question.diagram_meta || {};
    const diagramType = String(spec.image_type || spec.master || spec.type || spec.id || 'plant_cell').toLowerCase();
    
    // Support modern anti-leak contract (pins + landmarks) and legacy format (labels)
    // Rule 0d-14 & NS #14: Only render pins when the question explicitly defines pins/labels!
    // Gen 5 & Phase 2: If diagram_role === 'context', pins are hidden to prevent phantom letters!
    const isContextOnly = spec.diagram_role === 'context' || spec.role === 'context' || question?.diagram_role === 'context';
    const rawPins = Array.isArray(spec.pins) ? spec.pins : [];
    const pins = isContextOnly ? [] : rawPins;
    const landmarks = Array.isArray(spec.landmarks) ? spec.landmarks : [];
    const state = spec.state || 'static';
    const viewBox = spec.viewBox || '0 0 600 480';
    const gradeMask = spec.grade_mask || 'g9';

    const rawLabels = spec.labels && Array.isArray(spec.labels) && spec.labels.length > 0
        ? spec.labels
        : (rawPins.length > 0
            ? rawPins.map((p) => ({ id: p.pin, name: p.name || `Pin ${p.pin}` }))
            : []);
    const labels = isContextOnly ? [] : rawLabels;

    const activePinList = pins.length > 0 ? pins.map((p) => ({ id: p.pin })) : labels;
    const BankedComponent = getBankedDiagramComponent(diagramType);
    const meta = getDiagramMetadata(diagramType);
    const HeaderIcon = meta.Icon;

    return (
        <div className="space-y-6">
            {/* Bio Schematic Card (only rendered here if not already mounted in Question Card) */}
            {!hideStimulusDiagram && (
            <div 
                data-testid="bio-diagram-canvas" 
                className="p-4 sm:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-4 font-sans"
            >
                <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                    <div className="flex items-center gap-2">
                        <span className={`w-6 h-6 rounded-lg ${meta.colorClass} text-white flex items-center justify-center text-xs font-bold shadow-2xs`}>
                            <HeaderIcon className="w-3.5 h-3.5" />
                        </span>
                        <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                            {meta.title} • {diagramType.replace(/_/g, ' ').toUpperCase()}
                        </span>
                    </div>
                    <div className="flex items-center gap-2">
                        {state && state !== 'static' && (
                            <span className="text-[11px] font-mono text-indigo-700 font-semibold bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded uppercase">
                                Phase: {state.replace(/_/g, ' ')}
                            </span>
                        )}
                        {isContextOnly ? (
                            <span className="text-[11px] font-mono text-slate-700 font-semibold bg-slate-100 border border-slate-200 px-2 py-0.5 rounded">
                                Reference Schematic
                            </span>
                        ) : (
                            <span className="text-[11px] font-mono text-teal-700 font-semibold bg-teal-50 border border-teal-200 px-2 py-0.5 rounded">
                                Vector Diagram ({activePinList.length} Pins)
                            </span>
                        )}
                    </div>
                </div>

                {/* SVG Canvas Container */}
                <div className={`flex justify-center items-center ${meta.bgClass} p-4 rounded-xl border overflow-x-auto`}>
                    {BankedComponent ? (
                        <BankedComponent
                            pins={pins}
                            landmarks={landmarks}
                            labels={labels}
                            activePin={activePin}
                            onSelectPin={(pinId) => setActivePin(pinId)}
                            state={state}
                            viewBox={viewBox}
                            gradeMask={gradeMask}
                            anodeMetal={spec.anode_metal}
                            cathodeMetal={spec.cathode_metal}
                            voltmeterReading={spec.voltmeter_reading}
                            {...spec}
                        />
                    ) : (
                        /* Honest unrendered diagram type notice */
                        <div className="p-8 text-center space-y-3">
                            <div className="w-12 h-12 rounded-full bg-amber-50 text-amber-600 flex items-center justify-center mx-auto border border-amber-200">
                                <AlertCircle className="w-6 h-6" />
                            </div>
                            <div>
                                <h4 className="text-sm font-bold text-slate-800">
                                    Diagram Asset Under Bank Calibration: {diagramType.toUpperCase()}
                                </h4>
                                <p className="text-xs text-slate-500 max-w-sm mx-auto mt-1">
                                    This visual archetype is scheduled for vector bank authoring. Refer to the pin descriptors below.
                                </p>
                            </div>
                        </div>
                    )}
                </div>

                {/* Structure Pointer Pill (only shown when question defines pins) */}
                {activePinList.length > 0 && (
                    <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
                        <span className="text-slate-500 font-medium">Click any pin label (A, B, C...) to inspect:</span>
                        <div className="flex gap-1.5">
                            {activePinList.map((pin) => (
                                <button
                                    key={pin.id}
                                    type="button"
                                    data-testid={`btn-select-pin-${pin.id}`}
                                    onClick={() => setActivePin(pin.id)}
                                    className={`px-2.5 py-1 rounded-lg font-mono text-xs font-bold transition-all ${
                                        activePin === pin.id
                                            ? 'bg-[#13519C] text-white shadow-2xs'
                                            : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
                                    }`}
                                >
                                    Pin {pin.id}
                                </button>
                            ))}
                        </div>
                    </div>
                )}

                {/* Pin Details Callout (Strict Anti-Leak: never leak answer name before submission!) */}
                {activePin && (
                    <div data-testid="bio-pin-detail" className="p-3 bg-teal-50 border border-teal-200 rounded-xl flex items-center justify-between text-xs text-teal-900 animate-in fade-in">
                        <div className="flex items-center gap-2">
                            <CheckCircle className="w-4 h-4 text-teal-600 shrink-0" />
                            <span>
                                {result && labels.find((l) => l.id === activePin)?.name ? (
                                    <>
                                        <strong>Pin {activePin}:</strong> {labels.find((l) => l.id === activePin).name}
                                    </>
                                ) : (
                                    <>
                                        <strong>Pin {activePin}:</strong> Active target pin selected for response
                                    </>
                                )}
                            </span>
                        </div>
                        <span className="text-[11px] font-mono text-teal-700">
                            {result ? 'Verified' : 'Selected'}
                        </span>
                    </div>
                )}
            </div>
            )}

            {/* Answer Area */}
            <MathAnswerArea
                question={question}
                topic={topic}
                onCheck={onCheck}
                result={result}
                busy={isChecking}
                hideStimulusDiagram={true}
            />
        </div>
    );
}
