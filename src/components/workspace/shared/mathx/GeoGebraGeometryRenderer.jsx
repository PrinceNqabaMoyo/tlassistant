import React, { useState } from 'react';
import SvgRichLabel, { cleanSvgText } from './SvgRichLabel';

/**
 * Precision Vector Geometry Renderer (Milestone 10)
 * Renders high-DPI SVG mathematical figures for:
 *  - dot_pattern (Visual geometric dot/matchstick/tile sequences for Fig 1, 2, 3)
 *  - cartesian_point (Cartesian Plane / 4-Quadrant CAST Trig diagram)
 *  - radian_sector (Technical Maths circular sector with arc s=rθ, shaded sector, chord)
 *  - proportionality_triangle (Grade 12 Euclidean ΔABC with parallel line DE || BC & ratio callouts)
 *  - cube_net, rectangular_prism_net, triangular_prism_net, square_pyramid_net, cylinder_net, solid_3d
 */

function renderDotArrangement(arrangement, stepIndex, count) {
    const n = stepIndex + 1;
    const shapes = [];
    if (arrangement === 'matchsticks' || arrangement === 'squares' || arrangement === 'tiles') {
        const isTiles = arrangement === 'tiles';
        const sqSize = Math.min(28, Math.floor(110 / Math.max(1, isTiles ? count : n)));
        const numSquares = isTiles ? count : n;
        const cols = isTiles ? Math.min(5, Math.max(2, Math.ceil(Math.sqrt(numSquares * 1.4)))) : numSquares;
        const rows = isTiles ? Math.ceil(numSquares / cols) : 1;
        const cellGap = isTiles ? 3 : 0;
        const totalW = cols * sqSize + (cols - 1) * cellGap;
        const totalH = rows * sqSize + (rows - 1) * cellGap;
        const startX = 75 - totalW / 2;
        const startY = 55 - totalH / 2;

        for (let i = 0; i < numSquares; i++) {
            const c = i % cols;
            const r = Math.floor(i / cols);
            const x = startX + c * (sqSize + cellGap);
            const y = startY + r * (sqSize + cellGap);
            shapes.push(
                <rect
                    key={`sq-${i}`}
                    x={x}
                    y={y}
                    width={sqSize}
                    height={sqSize}
                    rx={isTiles ? 3 : 0}
                    fill={isTiles ? '#bfdbfe' : '#dbeafe'}
                    fillOpacity={isTiles ? '0.8' : '0.45'}
                    stroke="#1d4ed8"
                    strokeWidth="2.2"
                />
            );
            if (!isTiles) {
                // Corner vertices (matchstick heads)
                [[x, y], [x + sqSize, y], [x, y + sqSize], [x + sqSize, y + sqSize]].forEach(([vx, vy], vi) => {
                    shapes.push(
                        <circle key={`v-${i}-${vi}`} cx={vx} cy={vy} r="3" fill="#dc2626" />
                    );
                });
            }
        }
        return shapes;
    }

    if (arrangement === 'tables') {
        // Rectangular tables pushed together with chairs around perimeter
        const tW = Math.min(30, Math.floor(100 / Math.max(1, n)));
        const tH = 26;
        const startX = 75 - (n * tW) / 2;
        const startY = 55 - tH / 2;
        for (let i = 0; i < n; i++) {
            const x = startX + i * tW;
            shapes.push(
                <rect
                    key={`tbl-${i}`}
                    x={x}
                    y={startY}
                    width={tW}
                    height={tH}
                    fill="#e0e7ff"
                    stroke="#3730a3"
                    strokeWidth="2"
                />
            );
            // Top & bottom chairs
            shapes.push(<circle key={`ct-${i}`} cx={x + tW / 2} cy={startY - 8} r="4.5" fill="#2563eb" />);
            shapes.push(<circle key={`cb-${i}`} cx={x + tW / 2} cy={startY + tH + 8} r="4.5" fill="#2563eb" />);
        }
        // Left & right end chairs
        shapes.push(<circle key="cl" cx={startX - 8} cy={startY + tH / 2} r="4.5" fill="#dc2626" />);
        shapes.push(<circle key="cr" cx={startX + n * tW + 8} cy={startY + tH / 2} r="4.5" fill="#dc2626" />);
        return shapes;
    }

    // Default geometric dot grid / triangular / stadium array representing `count` dots
    const cols = Math.min(6, Math.max(2, Math.ceil(Math.sqrt(count * 1.4))));
    const rows = Math.ceil(count / cols);
    const spacing = Math.min(18, Math.floor(96 / Math.max(cols, rows)));
    const startX = 75 - ((cols - 1) * spacing) / 2;
    const startY = 55 - ((rows - 1) * spacing) / 2;

    for (let idx = 0; idx < count; idx++) {
        const r = Math.floor(idx / cols);
        const c = idx % cols;
        shapes.push(
            <circle
                key={`d-${idx}`}
                cx={startX + c * spacing}
                cy={startY + r * spacing}
                r="5"
                fill={idx < count - (stepIndex > 0 ? 2 : 0) ? '#2563eb' : '#059669'}
                stroke="#ffffff"
                strokeWidth="1.2"
            />
        );
    }
    return shapes;
}

function DotPatternSvg({ spec }) {
    const counts = spec.step_counts || [4, 7, 10];
    const arrangement = spec.arrangement || 'dots';
    const d = counts.length >= 2 ? counts[1] - counts[0] : 0;
    const showDiff = spec.show_difference === true;

    return (
        <div
            data-testid="geogebra-geometry-svg"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <div className="flex items-center gap-2">
                    <span className="inline-block w-2 h-2 rounded-full bg-blue-600" />
                    <span className="font-semibold text-slate-700 uppercase tracking-wider">
                        Visual Geometric Sequence ({arrangement})
                    </span>
                </div>
                {showDiff && d !== 0 && (
                    <span className="px-2 py-0.5 rounded bg-blue-50 text-blue-700 font-mono font-medium">
                        Constant difference d = {d > 0 ? `+${d}` : d}
                    </span>
                )}
            </div>
            <svg viewBox="0 0 560 175" className="w-full h-auto block bg-white">
                {counts.slice(0, 3).map((cnt, i) => {
                    const offsetX = 18 + i * 182;
                    return (
                        <g key={i} transform={`translate(${offsetX}, 12)`}>
                            <rect
                                x="0"
                                y="0"
                                width="150"
                                height="148"
                                rx="10"
                                fill="#f8fafc"
                                stroke="#cbd5e1"
                                strokeWidth="1.5"
                            />
                            <SvgRichLabel
                                x={75}
                                y={20}
                                textAnchor="middle"
                                fontSize={11}
                                fontWeight="700"
                                fill="#475569"
                                text={`FIGURE ${i + 1} (T_${i + 1})`}
                            />
                            <g transform="translate(0, 12)">
                                {renderDotArrangement(arrangement, i, cnt)}
                            </g>
                            <rect
                                x="35"
                                y="118"
                                width="80"
                                height="22"
                                rx="6"
                                fill="#eff6ff"
                                stroke="#bfdbfe"
                            />
                            <SvgRichLabel
                                x={75}
                                y={133}
                                textAnchor="middle"
                                fontSize={12}
                                fontWeight="700"
                                fill="#1d4ed8"
                                text={`T_${i + 1} = ${cnt}`}
                            />
                            {i < 2 && (
                                <g transform="translate(154, 70)">
                                    <line x1="0" y1="0" x2="20" y2="0" stroke="#94a3b8" strokeWidth="2" />
                                    <polygon points="20,-4 26,0 20,4" fill="#94a3b8" />
                                </g>
                            )}
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function CartesianPointSvg({ spec }) {
    const [px, py] = spec.point || [-3, 4];
    const showCast = spec.show_cast === true;
    const showCoords = spec.show_coords === true;
    const label = cleanSvgText(spec.label || (showCoords ? `P(${px}; ${py})` : 'P'));
    const showAngle = spec.show_angle !== false && showCast;
    const showProjection = spec.show_projection !== false;

    const maxCoord = Math.max(Math.abs(px), Math.abs(py), 5) + 1.5;
    const maxTick = Math.floor(maxCoord) - 1;
    const W = 520;
    const H = 380;
    const cx = W / 2;
    const cy = H / 2;
    const scale = Math.min(W, H) / (2 * maxCoord);

    const sx = (x) => cx + x * scale;
    const sy = (y) => cy - y * scale;

    const pX = sx(px);
    const pY = sy(py);
    const thetaRad = Math.atan2(py, px);
    let thetaDeg = Math.round((thetaRad * 180) / Math.PI);
    if (thetaDeg < 0) thetaDeg += 360;

    // Angle arc from positive x-axis to OP
    const arcR = 38;
    const endX = cx + arcR * Math.cos(thetaRad);
    const endY = cy - arcR * Math.sin(thetaRad);
    const largeArc = thetaDeg > 180 ? 1 : 0;
    const arcPath = `M ${cx + arcR} ${cy} A ${arcR} ${arcR} 0 ${largeArc} 0 ${endX} ${endY}`;

    const rSquared = px * px + py * py;
    const rClean = Number.isInteger(Math.sqrt(rSquared)) ? String(Math.sqrt(rSquared)) : `√${rSquared}`;

    return (
        <div
            data-testid="geogebra-geometry-svg"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {showCast ? 'Cartesian Trig Plane (CAST Diagram)' : 'Cartesian Coordinate Plane'}
                </span>
                {showCast && (
                    <span className="font-mono text-slate-600">
                        r = {rClean} | θ ≈ {thetaDeg}°
                    </span>
                )}
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {/* Calibrated grid & axis tick numbers */}
                {Array.from({ length: Math.floor(maxCoord) * 2 + 1 }, (_, i) => i - Math.floor(maxCoord)).map((g) => (
                    <g key={g}>
                        <line x1={sx(g)} y1={16} x2={sx(g)} y2={H - 16} stroke="#e2e8f0" strokeWidth="1" />
                        <line x1={16} y1={sy(g)} x2={W - 16} y2={sy(g)} stroke="#e2e8f0" strokeWidth="1" />
                        {g !== 0 && Math.abs(g) <= maxTick && (
                            <>
                                <line x1={sx(g)} y1={cy - 4} x2={sx(g)} y2={cy + 4} stroke="#334155" strokeWidth="1.5" />
                                <text x={sx(g)} y={cy + 16} textAnchor="middle" fontSize="10" fontWeight="600" fill="#475569">
                                    {g}
                                </text>
                                <line x1={cx - 4} y1={sy(g)} x2={cx + 4} y2={sy(g)} stroke="#334155" strokeWidth="1.5" />
                                <text x={cx - 8} y={sy(g) + 3.5} textAnchor="end" fontSize="10" fontWeight="600" fill="#475569">
                                    {g}
                                </text>
                            </>
                        )}
                    </g>
                ))}

                {/* CAST Quadrant watermarks (only for FET Trigonometry) */}
                {showCast && (
                    <>
                        <text x={W - 65} y={42} fontSize="12" fontWeight="700" fill="#cbd5e1">QI (All +)</text>
                        <text x={28} y={42} fontSize="12" fontWeight="700" fill="#cbd5e1">QII (sin +)</text>
                        <text x={28} y={H - 26} fontSize="12" fontWeight="700" fill="#cbd5e1">QIII (tan +)</text>
                        <text x={W - 65} y={H - 26} fontSize="12" fontWeight="700" fill="#cbd5e1">QIV (cos +)</text>
                    </>
                )}

                {/* Axes */}
                <line x1={20} y1={cy} x2={W - 20} y2={cy} stroke="#334155" strokeWidth="2" />
                <line x1={cx} y1={20} x2={cx} y2={H - 20} stroke="#334155" strokeWidth="2" />
                <text x={W - 14} y={cy + 4} fontSize="13" fontWeight="700" fill="#0f172a">x</text>
                <text x={cx + 8} y={20} fontSize="13" fontWeight="700" fill="#0f172a">y</text>
                <text x={cx - 12} y={cy + 15} fontSize="11" fontWeight="600" fill="#475569">O</text>

                {/* Projection drop-lines & right-angle marker */}
                {showProjection && (
                    <g>
                        <line
                            x1={pX}
                            y1={pY}
                            x2={pX}
                            y2={cy}
                            stroke="#64748b"
                            strokeWidth="1.6"
                            strokeDasharray="4,4"
                        />
                        <line
                            x1={pX}
                            y1={pY}
                            x2={cx}
                            y2={pY}
                            stroke="#64748b"
                            strokeWidth="1.6"
                            strokeDasharray="4,4"
                        />
                        {showCast && (
                            <>
                                <line
                                    x1={cx}
                                    y1={cy}
                                    x2={pX}
                                    y2={cy}
                                    stroke="#2563eb"
                                    strokeWidth="2.5"
                                />
                                {/* Right angle box on x-axis */}
                                <rect
                                    x={px >= 0 ? pX - 10 : pX}
                                    y={py >= 0 ? cy - 10 : cy}
                                    width="10"
                                    height="10"
                                    fill="none"
                                    stroke="#64748b"
                                    strokeWidth="1.4"
                                />
                            </>
                        )}
                        {showCoords && (
                            <>
                                <text
                                    x={(cx + pX) / 2}
                                    y={cy + (py >= 0 ? 18 : -8)}
                                    textAnchor="middle"
                                    fontSize="12"
                                    fontWeight="700"
                                    fill="#1d4ed8"
                                >
                                    x = {px}
                                </text>
                                <text
                                    x={pX + (px >= 0 ? 26 : -26)}
                                    y={(cy + pY) / 2}
                                    textAnchor="middle"
                                    fontSize="12"
                                    fontWeight="700"
                                    fill="#059669"
                                >
                                    y = {py}
                                </text>
                            </>
                        )}
                    </g>
                )}

                {/* Angle arc θ */}
                {showAngle && (
                    <g>
                        <path d={arcPath} fill="none" stroke="#d97706" strokeWidth="2.2" />
                        <text
                            x={cx + (arcR + 16) * Math.cos(thetaRad / 2)}
                            y={cy - (arcR + 16) * Math.sin(thetaRad / 2)}
                            textAnchor="middle"
                            fontSize="13"
                            fontWeight="700"
                            fill="#b45309"
                        >
                            θ
                        </text>
                    </g>
                )}

                {/* Terminal ray OP (only when CAST / trig mode is active) */}
                {showCast && (
                    <>
                        <line x1={cx} y1={cy} x2={pX} y2={pY} stroke="#0f172a" strokeWidth="2.8" />
                        <text
                            x={(cx + pX) / 2 + (py >= 0 ? -14 : 14)}
                            y={(cy + pY) / 2 - 8}
                            textAnchor="middle"
                            fontSize="12"
                            fontWeight="700"
                            fill="#0f172a"
                        >
                            r = {rClean}
                        </text>
                    </>
                )}

                {/* Point P */}
                <circle cx={pX} cy={pY} r="5.5" fill="#dc2626" stroke="#ffffff" strokeWidth="2" />
                <rect
                    x={pX + (px >= 0 ? 10 : -(Math.max(36, label.length * 8 + 18) + 10))}
                    y={pY - 14}
                    width={Math.max(36, label.length * 8 + 18)}
                    height="24"
                    rx="6"
                    fill="#0f172a"
                />
                <SvgRichLabel
                    x={pX + (px >= 0 ? 10 + Math.max(36, label.length * 8 + 18) / 2 : -(10 + Math.max(36, label.length * 8 + 18) / 2))}
                    y={pY + 2}
                    textAnchor="middle"
                    fontSize={12}
                    fontWeight="700"
                    fill="#ffffff"
                    text={label}
                />
            </svg>
        </div>
    );
}

function RadianSectorSvg({ spec }) {
    const rVal = cleanSvgText(String(spec.radius_label || spec.radius || 8));
    const deg = spec.deg_angle || 60;
    const radStr = cleanSvgText(spec.rad_label || `${(deg * Math.PI / 180).toFixed(2).replace('.', ',')} rad`);
    const arcStr = cleanSvgText(spec.arc_label || `s = rθ`);
    const unit = cleanSvgText(spec.unit || 'cm');

    const cx = 240;
    const cy = 195;
    const R = 130;
    const rad = (deg * Math.PI) / 180;
    const bx = cx + R * Math.cos(rad);
    const by = cy - R * Math.sin(rad);
    const largeArc = deg > 180 ? 1 : 0;

    const sectorPath = `M ${cx} ${cy} L ${cx + R} ${cy} A ${R} ${R} 0 ${largeArc} 0 ${bx} ${by} Z`;
    const arcMidX = cx + (R + 26) * Math.cos(rad / 2);
    const arcMidY = cy - (R + 26) * Math.sin(rad / 2);

    return (
        <div
            data-testid="geogebra-geometry-svg"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Circular Sector & Arc Length (s = rθ)
                </span>
                <span className="font-mono text-blue-700 font-semibold">
                    r = {rVal} {unit} | θ = {deg}° ({radStr})
                </span>
            </div>
            <svg viewBox="0 0 540 360" className="w-full h-auto block bg-white">
                {/* Full reference circle */}
                <circle
                    cx={cx}
                    cy={cy}
                    r={R}
                    fill="#f8fafc"
                    stroke="#cbd5e1"
                    strokeWidth="1.8"
                    strokeDasharray="6,4"
                />
                {/* Shaded sector OAB */}
                <path
                    d={sectorPath}
                    fill="#3b82f6"
                    fillOpacity="0.16"
                    stroke="#1d4ed8"
                    strokeWidth="2.8"
                />
                {/* Chord AB (dashed) */}
                <line
                    x1={cx + R}
                    y1={cy}
                    x2={bx}
                    y2={by}
                    stroke="#64748b"
                    strokeWidth="1.6"
                    strokeDasharray="4,4"
                />
                {/* Central angle arc */}
                <path
                    d={`M ${cx + 42} ${cy} A 42 42 0 ${largeArc} 0 ${cx + 42 * Math.cos(rad)} ${cy - 42 * Math.sin(rad)}`}
                    fill="#fef3c7"
                    fillOpacity="0.6"
                    stroke="#d97706"
                    strokeWidth="2.2"
                />
                <SvgRichLabel
                    x={cx + 66 * Math.cos(rad / 2)}
                    y={cy - 66 * Math.sin(rad / 2) + 4}
                    textAnchor="middle"
                    fontSize={12}
                    fontWeight="700"
                    fill="#b45309"
                    text={`${deg}° (${radStr})`}
                />

                {/* Radius label on OA */}
                <SvgRichLabel
                    x={cx + R / 2}
                    y={cy + 20}
                    textAnchor="middle"
                    fontSize={13}
                    fontWeight="700"
                    fill="#0f172a"
                    text={`r = ${rVal} ${unit}`}
                />

                {/* Arc length callout */}
                <SvgRichLabel
                    x={arcMidX}
                    y={arcMidY}
                    textAnchor="middle"
                    fontSize={13}
                    fontWeight="700"
                    fill="#1d4ed8"
                    text={arcStr}
                />

                {/* Points O, A, B */}
                <circle cx={cx} cy={cy} r="4.5" fill="#0f172a" />
                <text x={cx - 16} y={cy + 16} fontSize="13" fontWeight="700" fill="#0f172a">O</text>

                <circle cx={cx + R} cy={cy} r="4.5" fill="#1d4ed8" />
                <text x={cx + R + 14} y={cy + 5} fontSize="13" fontWeight="700" fill="#1d4ed8">A</text>

                <circle cx={bx} cy={by} r="4.5" fill="#1d4ed8" />
                <text
                    x={bx + 14 * Math.cos(rad)}
                    y={by - 14 * Math.sin(rad)}
                    fontSize="13"
                    fontWeight="700"
                    fill="#1d4ed8"
                >
                    B
                </text>
            </svg>
        </div>
    );
}

function SolidAndNetSvg({ spec }) {
    const kind = spec.kind || 'cube_net';
    const defaultView = spec.view || spec.viewMode || (kind === 'solid_3d' ? '3d' : kind.endsWith('_net') ? 'net' : 'both');
    const [viewMode, setViewMode] = useState(defaultView);
    const activeView = spec.allowViewSwitch === true ? viewMode : defaultView;
    const hideSolidName = Boolean(spec.hide_solid_name || spec.diagram_role === 'identify' || spec.role === 'identify');

    const radius = spec.radius || 5;
    const height = spec.height || 12;
    const base = spec.base || 8;
    const length = spec.length || 15;
    const side = spec.side || spec.edge || 6;

    const shapeStr = `${kind} ${spec.shape || ''}`.toLowerCase();
    const isCylinder = shapeStr.includes('cylinder');
    const isTriPrism = shapeStr.includes('triangular_prism') || shapeStr.includes('triangular prism');
    const isPyramid = shapeStr.includes('pyramid');
    const isRectPrism = shapeStr.includes('rectangular_prism') || shapeStr.includes('rectangular prism') || shapeStr.includes('cuboid');

    const title = hideSolidName
        ? (activeView === '3d' ? '3D Polyhedron — Isometric Projection' : '2D Unfolded Geometric Surface Net')
        : activeView === '3d'
        ? isCylinder
            ? `Right Cylinder (r = ${radius} cm, h = ${height} cm)`
            : isTriPrism
            ? 'Right Triangular Prism — 3D Isometric Solid'
            : isPyramid
            ? 'Square-Based Pyramid — 3D Isometric Solid'
            : isRectPrism
            ? 'Rectangular Prism (Cuboid) — 3D Isometric Solid'
            : 'Cube (Hexahedron) — 3D Isometric Solid'
        : isCylinder
        ? `Right Cylinder (r = ${radius} cm, h = ${height} cm)`
        : isTriPrism
        ? `Right Triangular Prism (b = ${base} cm, h = ${height} cm, L = ${length} cm)`
        : isPyramid
        ? 'Square-Based Pyramid & 2D Fold Net'
        : isRectPrism
        ? 'Rectangular Prism (Cuboid) & 2D Fold Net'
        : 'Cube (Hexahedron) & 2D Fold Net';

    return (
        <div
            data-testid="geogebra-geometry-svg"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {title}
                </span>
                {spec.allowViewSwitch === true && (
                    <div className="flex items-center gap-1">
                        {['both', '3d', 'net'].map((m) => (
                            <button
                                key={m}
                                type="button"
                                onClick={() => setViewMode(m)}
                                className={`px-2 py-0.5 rounded font-medium transition-colors ${
                                    activeView === m
                                        ? 'bg-blue-600 text-white'
                                        : 'bg-white text-slate-600 border border-slate-200 hover:bg-slate-100'
                                }`}
                            >
                                {m === 'both' ? '3D + Net' : m === '3d' ? '3D Wireframe' : '2D Net'}
                            </button>
                        ))}
                    </div>
                )}
            </div>

            <svg viewBox="0 0 560 280" className="w-full h-auto block bg-white">
                {/* Left Panel: Isometric 3D Solid Wireframe */}
                {(activeView === 'both' || activeView === '3d') && (
                    <g transform={activeView === '3d' ? 'translate(155, 10)' : 'translate(15, 10)'}>
                        <rect x="0" y="0" width="250" height="255" rx="10" fill="#f8fafc" stroke="#e2e8f0" />
                        <text x="125" y="22" textAnchor="middle" fontSize="11" fontWeight="700" fill="#475569">
                            3D ISOMETRIC WIREFRAME
                        </text>

                        {isCylinder ? (
                            <g transform="translate(65, 48)">
                                {/* Back dashed bottom arc */}
                                <ellipse cx="60" cy="150" rx="52" ry="18" fill="#dbeafe" fillOpacity="0.3" stroke="#64748b" strokeWidth="1.6" strokeDasharray="5,4" />
                                {/* Side walls */}
                                <rect x="8" y="30" width="104" height="120" fill="#dbeafe" fillOpacity="0.35" />
                                <line x1="8" y1="30" x2="8" y2="150" stroke="#1e293b" strokeWidth="2.4" />
                                <line x1="112" y1="30" x2="112" y2="150" stroke="#1e293b" strokeWidth="2.4" />
                                {/* Bottom front solid arc */}
                                <path d="M 8 150 A 52 18 0 0 0 112 150" fill="none" stroke="#1e293b" strokeWidth="2.4" />
                                {/* Top circular face */}
                                <ellipse cx="60" cy="30" rx="52" ry="18" fill="#bfdbfe" fillOpacity="0.6" stroke="#1e293b" strokeWidth="2.4" />
                                {/* Radius line & label */}
                                <line x1="60" y1="30" x2="112" y2="30" stroke="#dc2626" strokeWidth="2" />
                                <circle cx="60" cy="30" r="3" fill="#dc2626" />
                                <text x="86" y="24" textAnchor="middle" fontSize="11" fontWeight="700" fill="#dc2626">
                                    r = {radius} cm
                                </text>
                                {/* Height dimension arrow */}
                                <line x1="128" y1="30" x2="128" y2="150" stroke="#1d4ed8" strokeWidth="1.8" />
                                <text x="158" y="95" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1d4ed8">
                                    h = {height} cm
                                </text>
                            </g>
                        ) : isTriPrism ? (
                            <g transform="translate(45, 52)">
                                {/* Back triangle (dashed) */}
                                <polygon points="55,15 55,105 135,105" fill="#dbeafe" fillOpacity="0.2" stroke="#64748b" strokeWidth="1.6" strokeDasharray="4,4" />
                                {/* Connecting edges */}
                                <line x1="15" y1="55" x2="55" y2="15" stroke="#1e293b" strokeWidth="2.2" />
                                <line x1="15" y1="145" x2="55" y2="105" stroke="#64748b" strokeWidth="1.6" strokeDasharray="4,4" />
                                <line x1="95" y1="145" x2="135" y2="105" stroke="#1e293b" strokeWidth="2.2" />
                                {/* Front right-angled triangle */}
                                <polygon points="15,55 15,145 95,145" fill="#bfdbfe" fillOpacity="0.5" stroke="#1e293b" strokeWidth="2.4" />
                                <rect x="15" y="135" width="10" height="10" fill="none" stroke="#dc2626" strokeWidth="1.5" />
                                <text x="55" y="162" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1e293b">b = {base} cm</text>
                                <text x="-8" y="105" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1e293b">h = {height}</text>
                                <text x="132" y="135" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1d4ed8">L = {length} cm</text>
                            </g>
                        ) : isPyramid ? (
                            <g transform="translate(50, 45)">
                                {/* Square base in perspective */}
                                <polygon points="20,145 95,145 130,110 55,110" fill="#dbeafe" fillOpacity="0.4" stroke="#1e293b" strokeWidth="2" />
                                {/* Apex at (75, 25) */}
                                <line x1="75" y1="25" x2="55" y2="110" stroke="#64748b" strokeWidth="1.5" strokeDasharray="4,4" />
                                <line x1="75" y1="25" x2="20" y2="145" stroke="#1e293b" strokeWidth="2.4" />
                                <line x1="75" y1="25" x2="95" y2="145" stroke="#1e293b" strokeWidth="2.4" />
                                <line x1="75" y1="25" x2="130" y2="110" stroke="#1e293b" strokeWidth="2.4" />
                                {/* Perpendicular altitude */}
                                <line x1="75" y1="25" x2="75" y2="127" stroke="#dc2626" strokeWidth="1.8" strokeDasharray="3,3" />
                                <circle cx="75" cy="25" r="3.5" fill="#dc2626" />
                            </g>
                        ) : (
                            <g transform="translate(55, 50)">
                                {/* Isometric Cube / Rectangular Prism */}
                                <rect x="40" y="15" width="85" height="85" fill="#dbeafe" fillOpacity="0.2" stroke="#64748b" strokeWidth="1.6" strokeDasharray="4,4" />
                                <line x1="10" y1="45" x2="40" y2="15" stroke="#1e293b" strokeWidth="2.2" />
                                <line x1="95" y1="45" x2="125" y2="15" stroke="#1e293b" strokeWidth="2.2" />
                                <line x1="10" y1="130" x2="40" y2="100" stroke="#64748b" strokeWidth="1.6" strokeDasharray="4,4" />
                                <line x1="95" y1="130" x2="125" y2="100" stroke="#1e293b" strokeWidth="2.2" />
                                <rect x="10" y="45" width="85" height="85" fill="#bfdbfe" fillOpacity="0.45" stroke="#1e293b" strokeWidth="2.4" />
                                <text x="52" y="148" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1e293b">
                                    s = {side} cm
                                </text>
                            </g>
                        )}
                    </g>
                )}

                {/* Right Panel: 2D Unfolded Geometric Net */}
                {(activeView === 'both' || activeView === 'net') && (
                    <g transform={activeView === 'net' ? 'translate(150, 10)' : 'translate(285, 10)'}>
                        <rect x="0" y="0" width="260" height="255" rx="10" fill="#f8fafc" stroke="#e2e8f0" />
                        <text x="130" y="22" textAnchor="middle" fontSize="11" fontWeight="700" fill="#475569">
                            2D UNFOLDED SURFACE NET
                        </text>

                        {Array.isArray(spec.boxes) && spec.boxes.length > 0 ? (
                            <g transform="translate(42, 42)">
                                {(spec.boxes || []).map((b, i) => (
                                    <g key={`b-${i}`}>
                                        <rect
                                            x={b.x * 42}
                                            y={b.y * 42}
                                            width={b.w * 42}
                                            height={b.h * 42}
                                            fill="#dbeafe"
                                            fillOpacity="0.55"
                                            stroke="#1d4ed8"
                                            strokeWidth="2"
                                        />
                                        {b.label && (
                                            <SvgRichLabel
                                                x={(b.x + b.w / 2) * 42}
                                                y={(b.y + b.h / 2) * 42 + 4}
                                                textAnchor="middle"
                                                fontSize={9.5}
                                                fontWeight="700"
                                                fill="#1e3a8a"
                                                text={cleanSvgText(b.label)}
                                            />
                                        )}
                                    </g>
                                ))}
                                {(spec.triangles || []).map((t, i) => {
                                    const pts = t.points || [];
                                    const cx = pts.length ? pts.reduce((acc, p) => acc + p[0], 0) / pts.length : 0;
                                    const cy = pts.length ? pts.reduce((acc, p) => acc + p[1], 0) / pts.length : 0;
                                    return (
                                        <g key={`t-${i}`}>
                                            <polygon
                                                points={pts.map(([px, py]) => `${px * 42},${py * 42}`).join(' ')}
                                                fill="#bfdbfe"
                                                fillOpacity="0.65"
                                                stroke="#1d4ed8"
                                                strokeWidth="2"
                                            />
                                            {t.label && (
                                                <SvgRichLabel
                                                    x={cx * 42}
                                                    y={cy * 42 + 3}
                                                    textAnchor="middle"
                                                    fontSize={9}
                                                    fontWeight="700"
                                                    fill="#1e3a8a"
                                                    text={cleanSvgText(t.label)}
                                                />
                                            )}
                                        </g>
                                    );
                                })}
                                {(spec.circles || []).map((c, i) => (
                                    <g key={`c-${i}`}>
                                        <circle
                                            cx={c.cx * 42}
                                            cy={c.cy * 42}
                                            r={c.r * 42}
                                            fill="#bfdbfe"
                                            fillOpacity="0.65"
                                            stroke="#1d4ed8"
                                            strokeWidth="2"
                                        />
                                        {c.label && (
                                            <SvgRichLabel
                                                x={c.cx * 42}
                                                y={c.cy * 42 + 3}
                                                textAnchor="middle"
                                                fontSize={9}
                                                fontWeight="700"
                                                fill="#dc2626"
                                                text={cleanSvgText(c.label)}
                                            />
                                        )}
                                    </g>
                                ))}
                            </g>
                        ) : isCylinder ? (
                            <g transform="translate(45, 38)">
                                <circle cx="85" cy="24" r="22" fill="#bfdbfe" stroke="#1d4ed8" strokeWidth="2" />
                                <line x1="85" y1="24" x2="107" y2="24" stroke="#dc2626" strokeWidth="1.8" />
                                <text x="85" y="18" textAnchor="middle" fontSize="9.5" fontWeight="700" fill="#dc2626">
                                    r = {radius} cm
                                </text>
                                <rect x="15" y="48" width="140" height="85" fill="#dbeafe" stroke="#1d4ed8" strokeWidth="2" />
                                <text x="85" y="94" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1e3a8a">
                                    h = {height} cm
                                </text>
                                <circle cx="85" cy="157" r="22" fill="#bfdbfe" stroke="#1d4ed8" strokeWidth="2" />
                                <text x="85" y="161" textAnchor="middle" fontSize="9.5" fontWeight="700" fill="#1e3a8a">
                                    r = {radius} cm
                                </text>
                            </g>
                        ) : isTriPrism ? (
                            <g transform="translate(45, 38)">
                                {/* Triangular prism unfolded net */}
                                <polygon points="55,35 115,35 85,5" fill="#bfdbfe" stroke="#1d4ed8" strokeWidth="2" />
                                <text x="85" y="30" textAnchor="middle" fontSize="9" fontWeight="700" fill="#1e3a8a">
                                    b = {base} cm
                                </text>
                                <rect x="10" y="35" width="45" height="95" fill="#dbeafe" stroke="#1d4ed8" strokeWidth="2" />
                                <rect x="55" y="35" width="60" height="95" fill="#dbeafe" stroke="#1d4ed8" strokeWidth="2" />
                                <rect x="115" y="35" width="45" height="95" fill="#dbeafe" stroke="#1d4ed8" strokeWidth="2" />
                                <polygon points="55,130 115,130 85,160" fill="#bfdbfe" stroke="#1d4ed8" strokeWidth="2" />
                                <text x="85" y="85" textAnchor="middle" fontSize="10" fontWeight="700" fill="#1e3a8a">
                                    L = {length} cm
                                </text>
                            </g>
                        ) : (
                            <g transform="translate(55, 42)">
                                {/* Standard Cross Net of a Cube (6 congruent squares) */}
                                {[
                                    [1, 0],
                                    [0, 1],
                                    [1, 1],
                                    [2, 1],
                                    [1, 2],
                                    [1, 3],
                                ].map(([gx, gy], idx) => (
                                    <rect
                                        key={idx}
                                        x={gx * 42}
                                        y={gy * 42}
                                        width="42"
                                        height="42"
                                        fill="#dbeafe"
                                        fillOpacity="0.65"
                                        stroke="#1d4ed8"
                                        strokeWidth="2"
                                    />
                                ))}
                                <text x="63" y="67" textAnchor="middle" fontSize="9.5" fontWeight="700" fill="#1e3a8a">
                                    {side} cm
                                </text>
                            </g>
                        )}
                    </g>
                )}
            </svg>
        </div>
    );
}

export default function GeoGebraGeometryRenderer({ spec }) {
    if (!spec) return null;
    switch (spec.kind) {
        case 'dot_pattern':
            return <DotPatternSvg spec={spec} />;
        case 'cartesian_point':
            return <CartesianPointSvg spec={spec} />;
        case 'radian_sector':
            return <RadianSectorSvg spec={spec} />;
        case 'cube_net':
        case 'rectangular_prism_net':
        case 'triangular_prism_net':
        case 'square_pyramid_net':
        case 'cylinder_net':
        case 'solid_3d':
            return <SolidAndNetSvg spec={spec} />;
        default:
            return null;
    }
}
