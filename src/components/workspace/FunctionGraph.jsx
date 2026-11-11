import React, { useState, useMemo } from 'react';
import SvgRichLabel, { cleanSvgText } from './shared/mathx/SvgRichLabel';

/**
 * Desmos+ / GeoGebra+ Precision Multi-Curve Cartesian, Calculus, Analytical Circle,
 * Argand Plane & Trapezoidal Rule Vector Plotter (Milestone 11).
 *
 * Accepts either:
 *   - `graph={{ type, params, domain, range, ... }}`
 *   - `spec={{ kind: 'function_graph' | 'circle_geometry' | 'argand_diagram' | 'trapezoidal_rule' | 'linear_programming', ... }}`
 */

function evalFamily(family, xVal, p) {
    const a = p.a ?? 1;
    const b = p.b ?? 2;
    const c = p.c ?? 0;
    const d = p.d ?? 0;
    const q = p.q ?? 0;
    const shiftP = p.p ?? 0;
    const m = p.m ?? a;

    switch (family) {
        case 'line':
        case 'linear':
            return m * xVal + (p.c !== undefined ? p.c : q);
        case 'parabola':
        case 'quadratic':
            if (p.b !== undefined && p.c !== undefined && p.family !== 'quadratic') {
                return a * xVal * xVal + b * xVal + c;
            }
            return a * Math.pow(xVal - shiftP, 2) + q;
        case 'cubic':
            return a * Math.pow(xVal, 3) + b * Math.pow(xVal, 2) + c * xVal + d;
        case 'hyperbola': {
            const denom = xVal - shiftP;
            if (Math.abs(denom) < 0.04) return null;
            return a / denom + q;
        }
        case 'exponential':
            return a * Math.pow(b > 0 ? b : 2, xVal - shiftP) + q;
        case 'sin':
            return a * Math.sin(((xVal - shiftP) * Math.PI) / 180) + q;
        case 'cos':
            return a * Math.cos(((xVal - shiftP) * Math.PI) / 180) + q;
        case 'tan': {
            const rad = ((xVal - shiftP) * Math.PI) / 180;
            if (Math.abs(Math.cos(rad)) < 0.06) return null;
            return a * Math.tan(rad) + q;
        }
        case 'trig': {
            const fn = p.fn || 'sin';
            const k = p.k ?? 1;
            const rad = (k * (xVal - shiftP) * Math.PI) / 180;
            if (fn === 'cos') return a * Math.cos(rad) + q;
            if (fn === 'tan') return Math.abs(Math.cos(rad)) < 0.06 ? null : a * Math.tan(rad) + q;
            return a * Math.sin(rad) + q;
        }
        default:
            return null;
    }
}

function ArgandPlaneGraph({ spec }) {
    const a = Number(spec.a ?? 3);
    const b = Number(spec.b ?? 4);
    const maxR = Math.max(Math.abs(a), Math.abs(b), 5) * 1.25 + 1.5;
    const W = 560;
    const H = 380;
    const cx = W / 2;
    const cy = H / 2;
    const scale = Math.min(W - 80, H - 80) / (2 * maxR);

    const sx = (x) => cx + x * scale;
    const sy = (y) => cy - y * scale;
    const zx = sx(a);
    const zy = sy(b);

    const modSq = a * a + b * b;
    const modStr = Number.isInteger(Math.sqrt(modSq)) ? String(Math.sqrt(modSq)) : `√${modSq}`;
    let thetaDeg = Math.round((Math.atan2(b, a) * 180) / Math.PI * 10) / 10;
    if (thetaDeg < 0) thetaDeg = Math.round((thetaDeg + 360) * 10) / 10;

    const vecLen = Math.hypot(zx - cx, zy - cy);
    const arcR = Math.min(36, Math.max(18, vecLen * 0.45));
    const rad = Math.atan2(b, a);
    const endX = cx + arcR * Math.cos(rad);
    const endY = cy - arcR * Math.sin(rad);
    const largeArc = thetaDeg > 180 ? 1 : 0;
    const pillAbove = Math.abs(zy - cy) < 56;
    const pillX = pillAbove ? zx - 50 : (a >= 0 ? zx + 10 : zx - 110);
    const pillY = pillAbove ? (b >= 0 ? zy - 32 : zy + 10) : zy - 14;
    const thetaLabelR = arcR + (pillAbove ? 26 : 20);
    const thetaLabelAngle = pillAbove && a >= 0 && b >= 0 ? rad * 0.28 : rad / 2;

    return (
        <div
            data-testid="geogebra-function-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <div className="flex items-center gap-2">
                    <span className="inline-block w-2 h-2 rounded-full bg-indigo-600" />
                    <span className="font-semibold text-slate-700 uppercase tracking-wider">
                        Complex Argand Plane
                    </span>
                </div>
                <span className="font-mono font-semibold text-indigo-700">
                    {spec.showPolarAnswer ? `z = ${a} ${b >= 0 ? `+ ${b}i` : `- ${Math.abs(b)}i`} | |z| = ${modStr} | θ = ${thetaDeg}°` : `Complex Vector z in Argand Plane`}
                </span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {Array.from({ length: Math.floor(maxR) * 2 + 1 }, (_, i) => i - Math.floor(maxR)).map((g) => (
                    <g key={g}>
                        <line x1={sx(g)} y1={16} x2={sx(g)} y2={H - 16} stroke="#f1f5f9" strokeWidth="1" />
                        <line x1={16} y1={sy(g)} x2={W - 16} y2={sy(g)} stroke="#f1f5f9" strokeWidth="1" />
                    </g>
                ))}
                {/* Axes */}
                <line x1={20} y1={cy} x2={W - 20} y2={cy} stroke="#334155" strokeWidth="2" />
                <line x1={cx} y1={24} x2={cx} y2={H - 20} stroke="#334155" strokeWidth="2" />
                <text x={W - 38} y={cy - 8} fontSize="12" fontWeight="700" fill="#0f172a">Re(z)</text>
                <text x={cx} y={16} textAnchor="middle" fontSize="12" fontWeight="700" fill="#0f172a">Im(z)</text>

                {/* Projections */}
                <line x1={zx} y1={zy} x2={zx} y2={cy} stroke="#64748b" strokeWidth="1.6" strokeDasharray="5,4" />
                <line x1={zx} y1={zy} x2={cx} y2={zy} stroke="#64748b" strokeWidth="1.6" strokeDasharray="5,4" />
                <text x={zx} y={cy + (b >= 0 ? 16 : -8)} textAnchor="middle" fontSize="11" fontWeight="700" fill="#1d4ed8">{a}</text>
                <text
                    x={a >= 0 ? cx - 8 : cx + 8}
                    y={zy + 4}
                    textAnchor={a >= 0 ? 'end' : 'start'}
                    fontSize="11"
                    fontWeight="700"
                    fill="#059669"
                >
                    {b}i
                </text>

                {/* Argument arc */}
                <path
                    d={`M ${cx + arcR} ${cy} A ${arcR} ${arcR} 0 ${largeArc} 0 ${endX} ${endY}`}
                    fill="none"
                    stroke="#d97706"
                    strokeWidth="2.2"
                />
                <text
                    x={cx + thetaLabelR * Math.cos(thetaLabelAngle)}
                    y={cy - thetaLabelR * Math.sin(thetaLabelAngle)}
                    textAnchor={a >= 0 && pillAbove ? 'start' : 'middle'}
                    fontSize="11"
                    fontWeight="700"
                    fill="#b45309"
                >
                    θ = {thetaDeg}°
                </text>

                {/* Vector z */}
                <line x1={cx} y1={cy} x2={zx} y2={zy} stroke="#4f46e5" strokeWidth="3" />
                <circle cx={zx} cy={zy} r="5.5" fill="#dc2626" stroke="#ffffff" strokeWidth="2" />
                <rect x={pillX} y={pillY} width="100" height="22" rx="6" fill="#1e1b4b" />
                <text x={pillX + 50} y={pillY + 15} textAnchor="middle" fontSize="11" fontWeight="700" fill="#ffffff">
                    z({a}; {b}i)
                </text>
            </svg>
        </div>
    );
}

function TrapezoidalRuleGraph({ spec }) {
    const h = Number(spec.h ?? 4);
    const ordinates = spec.ordinates || [2, 5, 8, 6, 3];
    const unit = spec.unit || 'm';
    const nIntervals = ordinates.length - 1;
    const maxY = Math.max(...ordinates, 5) * 1.25;

    const W = 560;
    const H = 340;
    const padL = 56;
    const padR = 36;
    const padT = 32;
    const padB = 48;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const sx = (idx) => padL + (idx / Math.max(1, nIntervals)) * plotW;
    const sy = (y) => padT + plotH - (y / maxY) * plotH;

    return (
        <div
            data-testid="geogebra-function-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Trapezoidal Rule Numerical Integration
                </span>
                <span className="font-mono font-semibold text-blue-700">
                    {nIntervals} equal strips | h = {h} {unit} | {ordinates.length} ordinates
                </span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {/* Axes */}
                <line x1={padL} y1={padT + plotH} x2={W - padR + 12} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                <line x1={padL} y1={padT - 10} x2={padL} y2={padT + plotH} stroke="#334155" strokeWidth="2" />

                {/* Trapezoidal strips */}
                {ordinates.slice(0, -1).map((yCurr, i) => {
                    const yNext = ordinates[i + 1];
                    const x1 = sx(i);
                    const x2 = sx(i + 1);
                    const py1 = sy(yCurr);
                    const py2 = sy(yNext);
                    const base = padT + plotH;
                    return (
                        <g key={i}>
                            <polygon
                                points={`${x1},${base} ${x1},${py1} ${x2},${py2} ${x2},${base}`}
                                fill={i % 2 === 0 ? '#dbeafe' : '#bfdbfe'}
                                fillOpacity="0.55"
                                stroke="#2563eb"
                                strokeWidth="1.8"
                            />
                            <text
                                x={(x1 + x2) / 2}
                                y={base + 18}
                                textAnchor="middle"
                                fontSize="11"
                                fontWeight="700"
                                fill="#475569"
                            >
                                h = {h}{unit}
                            </text>
                        </g>
                    );
                })}

                {/* Ordinate verticals & labels */}
                {ordinates.map((yVal, i) => {
                    const x = sx(i);
                    const py = sy(yVal);
                    return (
                        <g key={`ord-${i}`}>
                            <line
                                x1={x}
                                y1={padT + plotH}
                                x2={x}
                                y2={py}
                                stroke="#1d4ed8"
                                strokeWidth="2.2"
                                strokeDasharray={i === 0 || i === ordinates.length - 1 ? undefined : '4,3'}
                            />
                            <circle cx={x} cy={py} r="4.5" fill="#dc2626" stroke="#ffffff" strokeWidth="1.5" />
                            <text
                                x={x}
                                y={py - 14}
                                textAnchor="middle"
                                fontSize="11"
                                fontWeight="700"
                                fill="#0f172a"
                                style={{ paintOrder: 'stroke', stroke: '#ffffff', strokeWidth: '3.5px', strokeLinejoin: 'round' }}
                            >
                                <SvgRichLabel text={`y_{${i + 1}} = ${yVal}`} />
                            </text>
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function AnalyticalCircleGraph({ spec }) {
    const [cxVal, cyVal] = spec.center || [2, -1];
    const rVal = Number(spec.radius || 5);
    const pts = spec.points || {};
    const labels = spec.vertex_labels || {};

    const allXs = [cxVal - rVal, cxVal + rVal, 0, ...Object.values(pts).map((p) => p[0])];
    const allYs = [cyVal - rVal, cyVal + rVal, 0, ...Object.values(pts).map((p) => p[1])];
    const minX = Math.min(...allXs) - 2.5;
    const maxX = Math.max(...allXs) + 2.5;
    const minY = Math.min(...allYs) - 2.5;
    const maxY = Math.max(...allYs) + 2.5;

    const span = Math.max(maxX - minX, maxY - minY, 10);
    const midX = (minX + maxX) / 2;
    const midY = (minY + maxY) / 2;

    const W = 560;
    const H = 420;
    const scale = Math.min(W - 60, H - 60) / span;
    const sx = (x) => W / 2 + (x - midX) * scale;
    const sy = (y) => H / 2 - (y - midY) * scale;

    return (
        <div
            data-testid="geogebra-function-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Analytical Circle & Perpendicular Tangent
                </span>
                <span className="font-mono font-semibold text-blue-700">
                    Centre M({cxVal}; {cyVal}) | r = {Number.isInteger(rVal) ? rVal : rVal.toFixed(2)}
                </span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {/* Coordinate Axes */}
                <line x1={20} y1={sy(0)} x2={W - 20} y2={sy(0)} stroke="#64748b" strokeWidth="1.8" />
                <line x1={sx(0)} y1={20} x2={sx(0)} y2={H - 20} stroke="#64748b" strokeWidth="1.8" />
                <text x={W - 18} y={sy(0) - 6} fontSize="12" fontWeight="700" fill="#334155">x</text>
                <text x={sx(0) + 8} y={24} fontSize="12" fontWeight="700" fill="#334155">y</text>

                {/* Circle */}
                <circle
                    cx={sx(cxVal)}
                    cy={sy(cyVal)}
                    r={rVal * scale}
                    fill="#dbeafe"
                    fillOpacity="0.18"
                    stroke="#1d4ed8"
                    strokeWidth="2.6"
                />

                {/* Radius chords */}
                {(spec.chords || []).map(([p1, p2], idx) => {
                    const a = pts[p1];
                    const b = pts[p2];
                    if (!a || !b) return null;
                    return (
                        <line
                            key={`ch-${idx}`}
                            x1={sx(a[0])}
                            y1={sy(a[1])}
                            x2={sx(b[0])}
                            y2={sy(b[1])}
                            stroke="#059669"
                            strokeWidth="2.2"
                            strokeDasharray="5,4"
                        />
                    );
                })}

                {/* Tangent lines */}
                {(spec.tangents || []).map(([p1, p2], idx) => {
                    const a = pts[p1];
                    const b = pts[p2];
                    if (!a || !b) return null;
                    const dx = b[0] - a[0];
                    const dy = b[1] - a[1];
                    return (
                        <line
                            key={`tan-${idx}`}
                            x1={sx(a[0] - dx * 0.35)}
                            y1={sy(a[1] - dy * 0.35)}
                            x2={sx(b[0] + dx * 0.35)}
                            y2={sy(b[1] + dy * 0.35)}
                            stroke="#dc2626"
                            strokeWidth="2.4"
                        />
                    );
                })}

                {/* Labeled Points */}
                {Object.entries(pts).map(([k, [px, py]]) => (
                    <g key={k}>
                        <circle
                            cx={sx(px)}
                            cy={sy(py)}
                            r="4.5"
                            fill={k === 'M' ? '#1d4ed8' : '#dc2626'}
                            stroke="#ffffff"
                            strokeWidth="1.5"
                        />
                        <text
                            x={sx(px) + (k === 'M' ? 12 : 8)}
                            y={sy(py) + (k === 'M' ? 14 : -10)}
                            fontSize="12"
                            fontWeight="700"
                            fill="#0f172a"
                            style={{ paintOrder: 'stroke', stroke: '#ffffff', strokeWidth: '3.5px', strokeLinejoin: 'round' }}
                        >
                            <SvgRichLabel text={labels[k] || k} />
                        </text>
                    </g>
                ))}
            </svg>
        </div>
    );
}

function StandardCartesianGraph({ resolved, onTransformChange }) {
    const interactiveTarget = resolved?.interactive?.target;
    const [sliderA, setSliderA] = useState(resolved?.a ?? 1);
    const [sliderQ, setSliderQ] = useState(resolved?.q ?? 0);
    const [hoverCoord, setHoverCoord] = useState(null);

    const family = resolved.family || resolved.type || 'linear';
    const isTrig = ['sin', 'cos', 'tan', 'trig'].includes(family);
    const domain = resolved.domain || (isTrig ? [0, 360] : [-6, 6]);
    const [xMin, xMax] = domain;

    const hasSliders = Boolean(resolved?.interactive?.sliders?.length);
    const activeParams = useMemo(() => {
        if (resolved.params) {
            return { ...resolved.params, family };
        }
        return {
            ...resolved,
            a: hasSliders ? sliderA : (resolved.a ?? 1),
            q: hasSliders ? sliderQ : (resolved.q ?? 0),
            b: resolved.b ?? 2,
            c: resolved.c,
            d: resolved.d,
            p: resolved.p ?? 0,
            family,
        };
    }, [resolved, family, hasSliders, sliderA, sliderQ]);

    // Auto-compute clean y-range
    const [yMin, yMax] = useMemo(() => {
        if (resolved.range) return resolved.range;
        if (isTrig) {
            const amp = Math.abs(activeParams.a || 1) + Math.abs(activeParams.q || 0) + 1.5;
            return [-Math.max(4, amp), Math.max(4, amp)];
        }
        return [-8, 8];
    }, [resolved.range, isTrig, activeParams.a, activeParams.q]);

    const W = 580;
    const H = 390;
    const pad = 38;
    const plotW = W - pad * 2;
    const plotH = H - pad * 2;

    const toSvgX = (x) => pad + ((x - xMin) / (xMax - xMin)) * plotW;
    const toSvgY = (y) => H - pad - ((y - yMin) / (yMax - yMin)) * plotH;

    const buildSegments = (paramsObj) => {
        const segs = [];
        let curr = [];
        const steps = 320;
        const dx = (xMax - xMin) / steps;
        for (let i = 0; i <= steps; i++) {
            const xVal = xMin + i * dx;
            const yVal = evalFamily(family, xVal, paramsObj);
            if (yVal !== null && !Number.isNaN(yVal) && yVal >= yMin - 3 && yVal <= yMax + 3) {
                curr.push(`${toSvgX(xVal).toFixed(1)},${toSvgY(yVal).toFixed(1)}`);
            } else if (curr.length > 0) {
                segs.push(curr);
                curr = [];
            }
        }
        if (curr.length > 0) segs.push(curr);
        return segs;
    };

    const primarySegments = buildSegments(activeParams);
    const targetSegments = interactiveTarget
        ? buildSegments({ ...activeParams, ...interactiveTarget })
        : [];

    // Asymptotes
    const horizAsymptote =
        resolved?.features?.asymptotes?.horizontal ??
        (['hyperbola', 'exponential'].includes(family) ? activeParams.q : null);
    const vertAsymptote =
        resolved?.features?.asymptotes?.vertical ??
        (family === 'hyperbola' ? (activeParams.p ?? 0) : null);

    // Highlighted points (intercepts, turning points, stationary points, inflection point).
    // Turning/stationary and inflection coordinates are NOT printed unless showStationaryCoords
    // is explicitly true, preventing the graph from giving away calculus answers (R9 / MATH12_CUBIC_CALCULUS).
    const showStationaryCoords = Boolean(resolved?.showStationaryCoords);
    const featurePoints = [];
    if (Array.isArray(resolved?.features?.x_intercepts) && resolved?.showInterceptCoords !== false) {
        resolved.features.x_intercepts.forEach(([px, py]) => {
            featurePoints.push({ x: px, y: py, label: `(${px}; ${py})`, color: '#1d4ed8', dx: 8, dy: -8, anchor: 'start' });
        });
    }
    if (Array.isArray(resolved?.features?.y_intercept)) {
        const [px, py] = resolved.features.y_intercept;
        const overlapsInflection =
            Array.isArray(resolved?.features?.inflection_point) &&
            Math.abs(resolved.features.inflection_point[0] - px) < 0.01 &&
            Math.abs(resolved.features.inflection_point[1] - py) < 0.01;
        featurePoints.push({
            x: px,
            y: py,
            label: `(0; ${py})`,
            color: '#059669',
            dx: overlapsInflection ? 10 : 8,
            dy: overlapsInflection ? 16 : -8,
            anchor: 'start',
        });
    }
    if (Array.isArray(resolved?.features?.stationary_points)) {
        resolved.features.stationary_points.forEach(([px, py], idx) => {
            const sym = String.fromCharCode(65 + idx);
            featurePoints.push({
                x: px,
                y: py,
                label: showStationaryCoords ? `${sym}(${px}; ${py})` : sym,
                color: '#dc2626',
                dx: 8,
                dy: -10,
                anchor: 'start',
            });
        });
    }
    if (Array.isArray(resolved?.features?.inflection_point)) {
        const [px, py] = resolved.features.inflection_point;
        featurePoints.push({
            x: px,
            y: py,
            label: showStationaryCoords ? `I(${px}; ${py})` : 'I',
            color: '#7c3aed',
            dx: 12,
            dy: -10,
            anchor: 'start',
        });
    }

    const xTicks = isTrig
        ? [0, 90, 180, 270, 360].filter((t) => t >= xMin && t <= xMax)
        : Array.from({ length: Math.floor(xMax) - Math.ceil(xMin) + 1 }, (_, i) => Math.ceil(xMin) + i).filter(
              (t) => t !== 0 && t % 2 === 0
          );

    const yTicks = Array.from({ length: Math.floor(yMax) - Math.ceil(yMin) + 1 }, (_, i) => Math.ceil(yMin) + i).filter(
        (t) => t !== 0 && t % 2 === 0
    );

    const handleSliderChange = (nextA, nextQ) => {
        setSliderA(nextA);
        setSliderQ(nextQ);
        if (onTransformChange) {
            onTransformChange({ a: nextA, q: nextQ });
        }
    };

    return (
        <div
            data-testid="geogebra-function-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <div className="flex items-center gap-2">
                    <span className="inline-block w-2 h-2 rounded-full bg-blue-600" />
                    <span className="font-semibold text-slate-700 uppercase tracking-wider">
                        Cartesian Function Graph ({family})
                    </span>
                </div>
                <span className="font-mono text-slate-600">
                    {hoverCoord ? `Cursor: (${hoverCoord.x}; ${hoverCoord.y})` : cleanSvgText(resolved.caption || '1:1 Coordinate Plane')}
                </span>
            </div>

            <svg
                viewBox={`0 0 ${W} ${H}`}
                className="w-full h-auto block bg-white cursor-crosshair"
                onMouseMove={(e) => {
                    const rect = e.currentTarget.getBoundingClientRect();
                    const relX = ((e.clientX - rect.left) / rect.width) * W;
                    const relY = ((e.clientY - rect.top) / rect.height) * H;
                    const mathX = xMin + ((relX - pad) / plotW) * (xMax - xMin);
                    const mathY = yMin + ((H - pad - relY) / plotH) * (yMax - yMin);
                    if (mathX >= xMin && mathX <= xMax && mathY >= yMin && mathY <= yMax) {
                        setHoverCoord({ x: mathX.toFixed(1), y: mathY.toFixed(1) });
                    }
                }}
                onMouseLeave={() => setHoverCoord(null)}
            >
                {/* Grid lines */}
                {xTicks.map((x) => (
                    <g key={`gx-${x}`}>
                        <line x1={toSvgX(x)} y1={pad} x2={toSvgX(x)} y2={H - pad} stroke="#f1f5f9" strokeWidth="1" />
                        <text
                            x={toSvgX(x)}
                            y={Math.min(H - 12, Math.max(pad + 14, toSvgY(0) + 15))}
                            textAnchor="middle"
                            fontSize="10.5"
                            fontWeight="600"
                            fill="#64748b"
                        >
                            {isTrig ? `${x}°` : x}
                        </text>
                    </g>
                ))}
                {yTicks.map((y) => (
                    <g key={`gy-${y}`}>
                        <line x1={pad} y1={toSvgY(y)} x2={W - pad} y2={toSvgY(y)} stroke="#f1f5f9" strokeWidth="1" />
                        <text
                            x={Math.max(18, Math.min(W - pad - 10, toSvgX(0) - 8))}
                            y={toSvgY(y) + 4}
                            textAnchor="end"
                            fontSize="10.5"
                            fontWeight="600"
                            fill="#64748b"
                        >
                            {y}
                        </text>
                    </g>
                ))}

                {/* Axes */}
                {yMin <= 0 && yMax >= 0 && (
                    <line x1={pad} y1={toSvgY(0)} x2={W - pad} y2={toSvgY(0)} stroke="#334155" strokeWidth="2" />
                )}
                {xMin <= 0 && xMax >= 0 && (
                    <line x1={toSvgX(0)} y1={pad} x2={toSvgX(0)} y2={H - pad} stroke="#334155" strokeWidth="2" />
                )}
                <text x={W - pad + 8} y={toSvgY(0) + 4} fontSize="12" fontWeight="700" fill="#0f172a">
                    {isTrig ? 'θ' : 'x'}
                </text>
                <text x={toSvgX(0) + 6} y={pad - 8} fontSize="12" fontWeight="700" fill="#0f172a">
                    y
                </text>

                {/* Horizontal & Vertical Asymptotes */}
                {horizAsymptote !== null && horizAsymptote >= yMin && horizAsymptote <= yMax && (
                    <g>
                        <line
                            x1={pad}
                            y1={toSvgY(horizAsymptote)}
                            x2={W - pad}
                            y2={toSvgY(horizAsymptote)}
                            stroke="#dc2626"
                            strokeWidth="1.8"
                            strokeDasharray="6,4"
                        />
                        <text
                            x={W - pad - 8}
                            y={toSvgY(horizAsymptote) - 6}
                            textAnchor="end"
                            fontSize="11"
                            fontWeight="700"
                            fill="#dc2626"
                        >
                            y = {horizAsymptote}
                        </text>
                    </g>
                )}
                {vertAsymptote !== null && vertAsymptote >= xMin && vertAsymptote <= xMax && (
                    <g>
                        <line
                            x1={toSvgX(vertAsymptote)}
                            y1={pad}
                            x2={toSvgX(vertAsymptote)}
                            y2={H - pad}
                            stroke="#dc2626"
                            strokeWidth="1.8"
                            strokeDasharray="6,4"
                        />
                        <text
                            x={toSvgX(vertAsymptote) + 6}
                            y={pad + 14}
                            fontSize="11"
                            fontWeight="700"
                            fill="#dc2626"
                        >
                            x = {vertAsymptote}
                        </text>
                    </g>
                )}

                {/* Dashed Target Curve (for interactive parameter manipulation) */}
                {targetSegments.map((seg, i) => (
                    <polyline
                        key={`tgt-${i}`}
                        fill="none"
                        stroke="#94a3b8"
                        strokeWidth="2.4"
                        strokeDasharray="6,4"
                        points={seg.join(' ')}
                    />
                ))}

                {/* Primary Function Curve */}
                {primarySegments.map((seg, i) => (
                    <polyline
                        key={`pri-${i}`}
                        fill="none"
                        stroke="#2563eb"
                        strokeWidth="2.8"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        points={seg.join(' ')}
                    />
                ))}

                {/* Feature Landmarks (Intercepts, Stationary Points, Inflection) */}
                {featurePoints.map((pt, idx) => (
                    <g key={`fp-${idx}`}>
                        <circle
                            cx={toSvgX(pt.x)}
                            cy={toSvgY(pt.y)}
                            r="5"
                            fill={pt.color}
                            stroke="#ffffff"
                            strokeWidth="1.8"
                        />
                        <text
                            x={toSvgX(pt.x) + (pt.dx ?? 8)}
                            y={toSvgY(pt.y) + (pt.dy ?? -8)}
                            textAnchor={pt.anchor || 'start'}
                            fontSize="11.5"
                            fontWeight="700"
                            fill={pt.color}
                            style={{ paintOrder: 'stroke', stroke: '#ffffff', strokeWidth: '3.5px', strokeLinejoin: 'round' }}
                        >
                            <SvgRichLabel text={pt.label} />
                        </text>
                    </g>
                ))}
            </svg>

            {/* Interactive Parameter Sliders (when spec.interactive is enabled) */}
            {hasSliders && (
                <div className="px-4 py-2.5 bg-slate-50 border-t border-slate-200 flex flex-wrap items-center gap-6 text-xs">
                    <label className="flex items-center gap-2 font-semibold text-slate-700">
                        <span>Parameter a = {sliderA}</span>
                        <input
                            type="range"
                            min="-4"
                            max="4"
                            step="1"
                            value={sliderA}
                            onChange={(e) => handleSliderChange(Number(e.target.value), sliderQ)}
                            className="accent-blue-600"
                        />
                    </label>
                    <label className="flex items-center gap-2 font-semibold text-slate-700">
                        <span>Vertical shift q = {sliderQ}</span>
                        <input
                            type="range"
                            min="-5"
                            max="5"
                            step="1"
                            value={sliderQ}
                            onChange={(e) => handleSliderChange(sliderA, Number(e.target.value))}
                            className="accent-blue-600"
                        />
                    </label>
                </div>
            )}
        </div>
    );
}

export default function FunctionGraph({ graph, spec, onTransformChange }) {
    const resolved = spec || graph;
    if (!resolved) return null;

    if (resolved.kind === 'argand_diagram') {
        return <ArgandPlaneGraph spec={resolved} />;
    }
    if (resolved.kind === 'trapezoidal_rule') {
        return <TrapezoidalRuleGraph spec={resolved} />;
    }
    if (resolved.kind === 'circle_geometry') {
        return <AnalyticalCircleGraph spec={resolved} />;
    }

    return <StandardCartesianGraph resolved={resolved} onTransformChange={onTransformChange} />;
}
