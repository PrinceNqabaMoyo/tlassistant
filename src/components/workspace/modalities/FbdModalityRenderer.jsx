import React, { useState } from 'react';
import MathText from '../shared/mathx/MathText';
import MathAnswerArea from '../shared/mathx/MathAnswerArea';
import { Compass, Info } from 'lucide-react';

export default function FbdModalityRenderer({
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

    const [activeForce, setActiveForce] = useState(null);
    const spec = question.fbd_spec || {};
    const mass = spec.mass_kg || 10;
    const inclineDeg = Number(spec.angle_deg || 0);
    const inclineRad = (inclineDeg * Math.PI) / 180;

    const rawForces = spec.forces && Array.isArray(spec.forces) && spec.forces.length > 0
        ? spec.forces
        : [
            { name: 'F_N', label: 'Normal Force (FN)', magnitude: Math.round(mass * 9.8 * Math.cos(inclineRad)), dir: 'up' },
            { name: 'F_g', label: 'Weight (Fg)', magnitude: Math.round(mass * 9.8), dir: 'down' },
            { name: 'f_k', label: 'Friction (fk)', magnitude: 15, dir: 'left' },
            { name: 'F_app', label: 'Applied Force (F)', magnitude: 50, dir: 'right' },
        ];

    const cx = 180;
    const cy = 130;

    // Determine scale for arrow lengths
    const maxMag = Math.max(...rawForces.map(f => Number(f.magnitude) || 50), 50);

    // Compute dynamic geometry for each force
    const computedForces = rawForces.map((f) => {
        let angleRad = 0;
        const dir = String(f.dir || '').toLowerCase();

        if (typeof f.angle_deg === 'number') {
            angleRad = (f.angle_deg * Math.PI) / 180;
        } else if (dir === 'up') {
            // Normal force is perpendicular to the surface
            angleRad = Math.PI / 2 + inclineRad;
        } else if (dir === 'down') {
            // Gravity always acts vertically down towards earth center
            angleRad = -Math.PI / 2;
        } else if (dir === 'left') {
            // Friction / parallel opposes motion along surface
            angleRad = Math.PI + inclineRad;
        } else if (dir === 'right') {
            // Applied / parallel along surface
            angleRad = inclineRad;
        }

        const mag = Number(f.magnitude) || 40;
        const arrowLength = Math.min(95, Math.max(50, 45 + (mag / maxMag) * 45));

        const x2 = cx + arrowLength * Math.cos(angleRad);
        const y2 = cy - arrowLength * Math.sin(angleRad); // SVG y is inverted

        // Label position slightly beyond arrow tip
        const labelOffset = 18;
        const labelX = cx + (arrowLength + labelOffset) * Math.cos(angleRad);
        const labelY = cy - (arrowLength + labelOffset) * Math.sin(angleRad) + 4;

        // Semantic color
        let strokeColor = '#059669'; // Emerald default for applied/resultant
        const nameLower = String(f.name || '').toLowerCase();
        const labelLower = String(f.label || '').toLowerCase();

        if (nameLower.includes('f_n') || labelLower.includes('normal')) {
            strokeColor = '#2563eb'; // Blue
        } else if (nameLower.includes('f_g') || nameLower.includes('weight') || labelLower.includes('weight') || labelLower.includes('gravity')) {
            strokeColor = '#e11d48'; // Red
        } else if (nameLower.includes('f_k') || labelLower.includes('friction')) {
            strokeColor = '#d97706'; // Amber
        } else if (nameLower.includes('f_y')) {
            strokeColor = '#7c3aed'; // Purple
        } else if (nameLower.includes('f_x')) {
            strokeColor = '#0284c7'; // Sky
        }

        // Semantic test IDs for E2E tests
        let semanticTestId = `fbd-force-${nameLower.replace(/[^a-z0-9]/g, '-')}`;
        if (nameLower.includes('f_n') || labelLower.includes('normal')) semanticTestId = 'fbd-force-normal';
        else if (nameLower.includes('f_g') || labelLower.includes('weight') || labelLower.includes('gravity')) semanticTestId = 'fbd-force-gravity';
        else if (nameLower.includes('f_k') || labelLower.includes('friction')) semanticTestId = 'fbd-force-friction';
        else if (nameLower.includes('f_app') || nameLower.includes('f_pull') || labelLower.includes('tensile') || labelLower.includes('applied')) semanticTestId = 'fbd-force-applied';

        return {
            ...f,
            x2,
            y2,
            labelX,
            labelY,
            strokeColor,
            semanticTestId,
            angleRad
        };
    });

    return (
        <div className="space-y-6">
            {/* FBD Schematic Card */}
            {!hideStimulusDiagram && (
            <div 
                data-testid="fbd-canvas" 
                className="p-4 sm:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-4 font-sans"
            >
                <div className="flex items-center justify-between border-b border-slate-100 pb-2">
                    <div className="flex items-center gap-2">
                        <span className="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs font-bold shadow-2xs">
                            <Compass className="w-3.5 h-3.5" />
                        </span>
                        <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
                            Free Body Diagram (FBD) • {mass} kg Mass {inclineDeg > 0 ? `• ${inclineDeg}° Incline` : '• Horizontal Plane'}
                        </span>
                    </div>
                    <span className="text-[11px] font-mono text-indigo-700 font-semibold bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded">
                        {computedForces.length} Forces Plotted
                    </span>
                </div>

                {/* SVG Vector Canvas */}
                <div className="flex justify-center items-center bg-slate-50/70 p-4 rounded-xl border border-slate-200/80 overflow-x-auto">
                    <svg viewBox="0 0 360 260" className="w-full max-w-[400px] h-auto select-none" style={{ minWidth: '280px' }}>
                        <defs>
                            <marker id="fbd-arrow" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill="#334155" />
                            </marker>
                            {computedForces.map((f, i) => (
                                <marker 
                                    key={i} 
                                    id={`marker-${f.semanticTestId}`} 
                                    viewBox="0 0 10 10" 
                                    refX="5" 
                                    refY="5" 
                                    markerWidth="6" 
                                    markerHeight="6" 
                                    orient="auto-start-reverse"
                                >
                                    <path d="M 0 1.5 L 10 5 L 0 8.5 z" fill={f.strokeColor} />
                                </marker>
                            ))}
                        </defs>

                        {/* Ground / Surface rendering */}
                        {inclineDeg === 0 ? (
                            /* Flat horizontal surface */
                            <g>
                                <line x1="30" y1="160" x2="330" y2="160" stroke="#94a3b8" strokeWidth="2.5" strokeDasharray="5 3" />
                                <text x="325" y="155" fontSize="10" fill="#64748b" textAnchor="end" fontFamily="sans-serif">Horizontal Surface</text>
                            </g>
                        ) : (
                            /* Tilted Incline Surface */
                            <g>
                                <line 
                                    x1={cx - 140 * Math.cos(inclineRad)} 
                                    y1={cy + 30 + 140 * Math.sin(inclineRad)} 
                                    x2={cx + 140 * Math.cos(inclineRad)} 
                                    y2={cy + 30 - 140 * Math.sin(inclineRad)} 
                                    stroke="#94a3b8" 
                                    strokeWidth="3" 
                                />
                                <line 
                                    x1={cx - 140 * Math.cos(inclineRad)} 
                                    y1={cy + 30 + 140 * Math.sin(inclineRad)} 
                                    x2={cx + 140 * Math.cos(inclineRad)} 
                                    y2={cy + 30 + 140 * Math.sin(inclineRad)} 
                                    stroke="#cbd5e1" 
                                    strokeWidth="1.5" 
                                    strokeDasharray="4 2" 
                                />
                                <text 
                                    x={cx - 100} 
                                    y={cy + 25 + 140 * Math.sin(inclineRad)} 
                                    fontSize="11" 
                                    fill="#475569" 
                                    fontWeight="bold" 
                                    fontFamily="sans-serif"
                                >
                                    θ = {inclineDeg}°
                                </text>
                            </g>
                        )}

                        {/* Central Mass Block (tilted by incline angle) */}
                        <g transform={`rotate(${-inclineDeg}, ${cx}, ${cy})`}>
                            <rect 
                                x={cx - 30} 
                                y={cy - 30} 
                                width="60" 
                                height="60" 
                                fill="#f8fafc" 
                                stroke="#334155" 
                                strokeWidth="2.5" 
                                rx="4" 
                            />
                            <text 
                                x={cx} 
                                y={cy + 5} 
                                fontSize="12" 
                                fill="#1e293b" 
                                fontWeight="bold" 
                                textAnchor="middle" 
                                fontFamily="monospace"
                            >
                                {mass} kg
                            </text>
                        </g>

                        {/* Center of Mass origin pin */}
                        <circle cx={cx} cy={cy} r="4.5" fill="#0f172a" stroke="#ffffff" strokeWidth="1.5" />

                        {/* Dynamically Plotted Force Vectors from question.fbd_spec */}
                        {computedForces.map((f, idx) => {
                            const isSelected = activeForce === f.name;
                            return (
                                <g 
                                    key={idx}
                                    data-testid={f.semanticTestId}
                                    data-force-name={f.name}
                                    className="cursor-pointer transition-transform"
                                    onClick={() => setActiveForce(f.name)}
                                >
                                    {/* Hit target line with pointer-events enabled */}
                                    <line 
                                        x1={cx} 
                                        y1={cy} 
                                        x2={f.x2} 
                                        y2={f.y2} 
                                        stroke="#ffffff"
                                        strokeOpacity="0.01" 
                                        strokeWidth="24" 
                                        strokeLinecap="round" 
                                        style={{ pointerEvents: 'stroke' }}
                                    />
                                    {/* The authentic vector arrow line */}
                                    <line 
                                        x1={cx} 
                                        y1={cy} 
                                        x2={f.x2} 
                                        y2={f.y2} 
                                        stroke={f.strokeColor} 
                                        strokeWidth={isSelected ? '3.5' : '2.5'} 
                                        markerEnd={`url(#marker-${f.semanticTestId})`} 
                                    />
                                    {/* Force symbol text */}
                                    <text 
                                        data-testid={`fbd-label-${f.semanticTestId}`}
                                        x={f.labelX} 
                                        y={f.labelY} 
                                        fontSize="11" 
                                        fill={f.strokeColor} 
                                        fontWeight="bold" 
                                        textAnchor="middle" 
                                        fontFamily="monospace"
                                        style={{ pointerEvents: 'all' }}
                                    >
                                        {f.name}
                                    </text>
                                </g>
                            );
                        })}
                    </svg>
                </div>

                {/* Dynamic Force Vector Legend (strictly matching question.fbd_spec) */}
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 text-xs">
                    {computedForces.map((f, idx) => (
                        <div 
                            key={idx} 
                            data-testid={`fbd-legend-${f.semanticTestId}`}
                            onClick={() => setActiveForce(f.name)}
                            className={`p-2 rounded-lg border font-mono text-center cursor-pointer transition-all ${
                                activeForce === f.name 
                                    ? 'bg-indigo-50 border-indigo-400 shadow-xs' 
                                    : 'bg-slate-50 border-slate-200/80 hover:bg-slate-100/70'
                            }`}
                        >
                            <span className="font-bold text-slate-800 block" style={{ color: f.strokeColor }}>
                                {f.label || f.name}
                            </span>
                            <span className="text-[11px] text-slate-500 block">
                                {f.magnitude ? `${f.magnitude} N` : f.dir}
                            </span>
                        </div>
                    ))}
                </div>
            </div>
            )}

            {/* Answer Area */}
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
