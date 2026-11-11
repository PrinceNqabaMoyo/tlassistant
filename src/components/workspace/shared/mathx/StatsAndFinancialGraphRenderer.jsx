import React from 'react';
import SvgRichLabel, { cleanSvgText } from './SvgRichLabel';

/**
 * Statistical, Probability & Financial Graph Renderer (Milestone 12)
 * Supports:
 *  - box_and_whisker
 *  - statistics_box_and_ogive / ogive
 *  - scatter_plot_regression
 *  - timeline_finance
 *  - contingency_table / contingency_table_and_tree
 *  - venn_3_sets
 *  - step_tariff
 *  - break_even
 */

function BoxAndWhiskerSvg({ spec }) {
    const bw = spec.box_and_whisker || spec.summary || spec;
    const usedFallback = !spec.box_and_whisker && !spec.summary && (spec.min === undefined || spec.max === undefined);
    const minV = Number(bw.min ?? 18);
    const q1 = Number(bw.q1 ?? 32);
    const med = Number(bw.median ?? bw.q2 ?? 45);
    const q3 = Number(bw.q3 ?? 58);
    const maxV = Number(bw.max ?? 74);
    const outliers = bw.outliers || [];
    const showStatsSummary = bw.show_summary === true;

    const lo = Math.floor((Math.min(minV, ...outliers) - 6) / 5) * 5;
    const hi = Math.ceil((Math.max(maxV, ...outliers) + 6) / 5) * 5;
    const W = 560;
    const H = 210;
    const padL = 45;
    const padR = 45;
    const plotW = W - padL - padR;

    const sx = (v) => padL + ((v - lo) / Math.max(1, hi - lo)) * plotW;
    const yMid = 88;
    const boxH = 48;

    const ticks = [];
    const step = hi - lo > 60 ? 10 : 5;
    for (let t = lo; t <= hi; t += step) ticks.push(t);

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            data-diagram-kind={spec.kind || 'box_and_whisker'}
            data-diagram-fallback={usedFallback ? 'true' : 'false'}
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Five-Number Summary & Box-and-Whisker Plot
                </span>
                {showStatsSummary && (
                    <span className="font-mono text-blue-700 font-semibold">
                        Min={minV} | Q₁={q1} | M={med} | Q₃={q3} | Max={maxV}
                    </span>
                )}
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {/* Calibrated Number Line */}
                <line x1={padL} y1={160} x2={W - padR} y2={160} stroke="#334155" strokeWidth="2" />
                {ticks.map((t) => (
                    <g key={t}>
                        <line x1={sx(t)} y1={154} x2={sx(t)} y2={166} stroke="#334155" strokeWidth="1.6" />
                        <line x1={sx(t)} y1={30} x2={sx(t)} y2={154} stroke="#f1f5f9" strokeWidth="1" />
                        <text x={sx(t)} y={180} textAnchor="middle" fontSize="11" fontWeight="600" fill="#475569">
                            {t}
                        </text>
                    </g>
                ))}

                {/* Whiskers */}
                <line x1={sx(minV)} y1={yMid} x2={sx(q1)} y2={yMid} stroke="#1e293b" strokeWidth="2.4" />
                <line x1={sx(q3)} y1={yMid} x2={sx(maxV)} y2={yMid} stroke="#1e293b" strokeWidth="2.4" />
                {/* Whisker end caps */}
                <line x1={sx(minV)} y1={yMid - 14} x2={sx(minV)} y2={yMid + 14} stroke="#1e293b" strokeWidth="2.4" />
                <line x1={sx(maxV)} y1={yMid - 14} x2={sx(maxV)} y2={yMid + 14} stroke="#1e293b" strokeWidth="2.4" />

                {/* Interquartile Box */}
                <rect
                    x={sx(q1)}
                    y={yMid - boxH / 2}
                    width={Math.max(4, sx(q3) - sx(q1))}
                    height={boxH}
                    fill="#dbeafe"
                    fillOpacity="0.65"
                    stroke="#1d4ed8"
                    strokeWidth="2.4"
                    rx="3"
                />

                {/* Median vertical line */}
                <line
                    x1={sx(med)}
                    y1={yMid - boxH / 2}
                    x2={sx(med)}
                    y2={yMid + boxH / 2}
                    stroke="#dc2626"
                    strokeWidth="3"
                />

                {/* Labels */}
                {[
                    { v: minV, lbl: `Min (${minV})`, col: '#334155', dy: -24 },
                    { v: q1, lbl: `Q_1 (${q1})`, col: '#1d4ed8', dy: -32 },
                    { v: med, lbl: `M (${med})`, col: '#dc2626', dy: 40 },
                    { v: q3, lbl: `Q_3 (${q3})`, col: '#1d4ed8', dy: -32 },
                    { v: maxV, lbl: `Max (${maxV})`, col: '#334155', dy: -24 },
                ].map((item, idx) => (
                    <SvgRichLabel
                        key={idx}
                        x={sx(item.v)}
                        y={yMid + item.dy}
                        textAnchor="middle"
                        fontSize={11}
                        fontWeight="700"
                        fill={item.col}
                        text={item.lbl}
                    />
                ))}

                {/* Outliers */}
                {outliers.map((o, i) => (
                    <g key={`out-${i}`}>
                        <circle cx={sx(o)} cy={yMid} r="5" fill="#dc2626" />
                        <text x={sx(o)} y={yMid - 12} textAnchor="middle" fontSize="10" fontWeight="700" fill="#dc2626">
                            Outlier ({o})
                        </text>
                    </g>
                ))}
            </svg>
        </div>
    );
}

function OgiveAndBoxSvg({ spec }) {
    const ogive = spec.ogive_curve || spec;
    const pts = ogive.points || [
        [20, 0],
        [30, 4],
        [40, 12],
        [50, 30],
        [60, 44],
        [70, 50],
    ];
    const xs = pts.map((p) => p[0]);
    const ys = pts.map((p) => p[1]);
    const minX = Math.min(...xs);
    const maxX = Math.max(...xs);
    const maxY = Math.max(...ys, 50);

    const W = 560;
    const H = 360;
    const padL = 55;
    const padR = 35;
    const padT = 28;
    const padB = 45;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const sx = (x) => padL + ((x - minX) / Math.max(1, maxX - minX)) * plotW;
    const sy = (y) => padT + plotH - (y / maxY) * plotH;

    const medCf = maxY * 0.5;
    const medX = ogive.median_lookup?.estimated_mark ?? (minX + maxX) / 2;

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Cumulative Frequency Curve (Ogive) & Quartile Drop-Lines
                </span>
                <span className="font-mono text-blue-700 font-semibold">
                    N = {maxY} | Median CF (N/2 = {medCf})
                </span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {/* Grid */}
                {xs.map((x) => (
                    <g key={`gx-${x}`}>
                        <line x1={sx(x)} y1={padT} x2={sx(x)} y2={padT + plotH} stroke="#f1f5f9" strokeWidth="1" />
                        <text x={sx(x)} y={padT + plotH + 18} textAnchor="middle" fontSize="11" fontWeight="600" fill="#475569">
                            {x}
                        </text>
                    </g>
                ))}
                {[0, 0.25, 0.5, 0.75, 1].map((f, i) => {
                    const yVal = Math.round(maxY * f);
                    return (
                        <g key={`gy-${i}`}>
                            <line x1={padL} y1={sy(yVal)} x2={padL + plotW} y2={sy(yVal)} stroke="#f1f5f9" strokeWidth="1" />
                            <text x={padL - 8} y={sy(yVal) + 4} textAnchor="end" fontSize="11" fontWeight="600" fill="#475569">
                                {yVal}
                            </text>
                        </g>
                    );
                })}

                {/* Axes */}
                <line x1={padL} y1={padT + plotH} x2={padL + plotW} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                <line x1={padL} y1={padT} x2={padL} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                <text x={padL + plotW / 2} y={H - 8} textAnchor="middle" fontSize="11.5" fontWeight="700" fill="#334155">
                    Upper Class Boundary (Marks)
                </text>

                {/* Median Drop-Line */}
                <line
                    x1={padL}
                    y1={sy(medCf)}
                    x2={sx(medX)}
                    y2={sy(medCf)}
                    stroke="#dc2626"
                    strokeWidth="1.8"
                    strokeDasharray="5,4"
                />
                <line
                    x1={sx(medX)}
                    y1={sy(medCf)}
                    x2={sx(medX)}
                    y2={padT + plotH}
                    stroke="#dc2626"
                    strokeWidth="1.8"
                    strokeDasharray="5,4"
                />
                <SvgRichLabel
                    x={sx(medX) + 6}
                    y={padT + plotH - 10}
                    fontSize={11}
                    fontWeight="700"
                    fill="#dc2626"
                    text={`Q_2 ≈ ${Number(medX).toFixed(1).replace('.', ',')}`}
                />

                {/* Smooth S-Curve Polyline */}
                <polyline
                    fill="none"
                    stroke="#2563eb"
                    strokeWidth="3"
                    points={pts.map(([px, py]) => `${sx(px)},${sy(py)}`).join(' ')}
                />
                {pts.map(([px, py], i) => (
                    <g key={i}>
                        <circle cx={sx(px)} cy={sy(py)} r="4.5" fill="#1d4ed8" stroke="#ffffff" strokeWidth="1.5" />
                        <text x={sx(px) - 6} y={sy(py) - 8} textAnchor="end" fontSize="10" fontWeight="700" fill="#1e293b">
                            ({px}; {py})
                        </text>
                    </g>
                ))}
            </svg>
            {spec.box_and_whisker && <BoxAndWhiskerSvg spec={spec.box_and_whisker} />}
        </div>
    );
}

function ScatterRegressionSvg({ spec }) {
    const rawPts = spec.points || [];
    const pts = rawPts.map((p) =>
        Array.isArray(p)
            ? { x: Number(p[0] ?? 0), y: Number(p[1] ?? 0) }
            : { x: Number(p?.x ?? 0), y: Number(p?.y ?? 0) }
    );
    const centroid = spec.centroid;
    const outlier = spec.outlier;

    const allX = pts.length > 0 ? pts.map((p) => p.x) : [0, 10];
    const allY = pts.length > 0 ? pts.map((p) => p.y) : [0, 10];
    const minX = Math.min(...allX, 0);
    const maxX = Math.max(...allX, 10) * 1.1;
    const minY = Math.min(...allY, 0);
    const maxY = Math.max(...allY, 10) * 1.15;

    let reg = spec.regression_line;
    if (!reg && pts.length >= 2) {
        const n = pts.length;
        const meanX = allX.reduce((a, b) => a + b, 0) / n;
        const meanY = allY.reduce((a, b) => a + b, 0) / n;
        const num = pts.reduce((acc, p) => acc + (p.x - meanX) * (p.y - meanY), 0);
        const den = pts.reduce((acc, p) => acc + (p.x - meanX) ** 2, 0);
        const b = den > 1e-6 ? num / den : 1;
        const a = meanY - b * meanX;
        reg = { a, b };
    } else if (!reg) {
        reg = { a: 0, b: 1 };
    }

    const W = 560;
    const H = 350;
    const padL = 55;
    const padR = 35;
    const padT = 28;
    const padB = 45;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const sx = (x) => padL + ((x - minX) / Math.max(1, maxX - minX)) * plotW;
    const sy = (y) => padT + plotH - ((y - minY) / Math.max(1, maxY - minY)) * plotH;

    const x1 = Math.min(...allX);
    const x2 = Math.max(...allX);
    const y1 = reg.a + reg.b * x1;
    const y2 = reg.a + reg.b * x2;

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Bivariate Scatter Plot & Least Squares Regression Line
                </span>
                {spec.show_equation === true && (
                    <span className="font-mono text-blue-700 font-semibold">
                        ŷ = {Number(reg.a).toFixed(2)} + {Number(reg.b).toFixed(2)}x
                    </span>
                )}
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                <line x1={padL} y1={padT + plotH} x2={padL + plotW} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                <line x1={padL} y1={padT} x2={padL} y2={padT + plotH} stroke="#334155" strokeWidth="2" />

                {/* Regression line */}
                <line
                    x1={sx(x1)}
                    y1={sy(y1)}
                    x2={sx(x2)}
                    y2={sy(y2)}
                    stroke="#2563eb"
                    strokeWidth="2.6"
                />

                {/* Data points */}
                {pts.map((p, i) => {
                    const isOutlier = outlier && Math.abs(p.x - outlier.x) < 0.01 && Math.abs(p.y - outlier.y) < 0.01;
                    return (
                        <g key={i}>
                            <circle
                                cx={sx(p.x)}
                                cy={sy(p.y)}
                                r={isOutlier ? '5.5' : '4.5'}
                                fill={isOutlier ? '#dc2626' : '#1e293b'}
                                stroke="#ffffff"
                                strokeWidth="1.5"
                            />
                            {isOutlier && (
                                <text
                                    x={sx(p.x) > W - 120 ? sx(p.x) - 10 : sx(p.x) + 10}
                                    y={sy(p.y) - 6}
                                    textAnchor={sx(p.x) > W - 120 ? 'end' : 'start'}
                                    fontSize="10.5"
                                    fontWeight="700"
                                    fill="#dc2626"
                                    style={{ paintOrder: 'stroke', stroke: '#ffffff', strokeWidth: '3px', strokeLinejoin: 'round' }}
                                >
                                    Outlier ({p.x}; {p.y})
                                </text>
                            )}
                        </g>
                    );
                })}

                {/* Centroid (x̄; ȳ) */}
                {centroid && (
                    <g>
                        <circle
                            cx={sx(centroid.x)}
                            cy={sy(centroid.y)}
                            r="6"
                            fill="#059669"
                            stroke="#ffffff"
                            strokeWidth="2"
                        />
                        <SvgRichLabel
                            x={sx(centroid.x) + 8}
                            y={sy(centroid.y) + 14}
                            fontSize={11}
                            fontWeight="700"
                            fill="#059669"
                            text={cleanSvgText(`Mean ${centroid.label || ''}`)}
                        />
                    </g>
                )}

                <SvgRichLabel
                    x={padL + plotW / 2}
                    y={H - 10}
                    textAnchor="middle"
                    fontSize={11.5}
                    fontWeight="700"
                    fill="#334155"
                    text={cleanSvgText(spec.x_label || 'Independent Variable (x)')}
                />
            </svg>
        </div>
    );
}

function TimelineFinanceSvg({ spec }) {
    const totalYears = Number(spec.total_years || 6);
    const events = spec.events || [];
    const W = 560;
    const H = 205;
    const padX = 55;
    const lineY = 108;
    const sx = (yr) => padX + (yr / Math.max(1, totalYears)) * (W - padX * 2);

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Multi-Stage Compound Interest Timeline (T₀ → T{totalYears})
                </span>
                <span className="font-mono text-blue-700 font-semibold">Term: {totalYears} Years</span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                <line x1={padX} y1={lineY} x2={W - padX} y2={lineY} stroke="#1e293b" strokeWidth="3" />
                {Array.from({ length: totalYears + 1 }, (_, yr) => (
                    <g key={yr}>
                        <line x1={sx(yr)} y1={lineY - 8} x2={sx(yr)} y2={lineY + 8} stroke="#1e293b" strokeWidth="2" />
                        <SvgRichLabel
                            x={sx(yr)}
                            y={lineY + 24}
                            textAnchor="middle"
                            fontSize={11.5}
                            fontWeight="700"
                            fill="#334155"
                            text={`T_${yr}`}
                        />
                    </g>
                ))}
                {(() => {
                    const placedTop = [];
                    const placedBot = [];
                    return events.map((ev, idx) => {
                        const yr = ev.year ?? 0;
                        const x = sx(yr);
                        const isTop = idx % 2 === 0;
                        const boxW = 158;
                        let boxX = Math.max(8, Math.min(W - boxW - 8, x - boxW / 2));
                        const placed = isTop ? placedTop : placedBot;
                        for (const prevX of placed) {
                            if (boxX < prevX + boxW + 6 && boxX + boxW + 6 > prevX) {
                                boxX = Math.min(W - boxW - 8, prevX + boxW + 6);
                            }
                        }
                        placed.push(boxX);
                        const boxCenterX = boxX + boxW / 2;
                        const boxY = isTop ? 14 : 142;
                        const rawLbl = cleanSvgText(ev.label || '');
                        const prefixedLbl = /^T[₀-₉0-9_]/.test(rawLbl) ? rawLbl : `T_${yr}: ${rawLbl}`;
                        return (
                            <g key={idx}>
                                {/* Leader line connecting callout box to exact T_yr tick */}
                                <line
                                    x1={x}
                                    y1={isTop ? lineY - 6 : lineY + 6}
                                    x2={boxCenterX}
                                    y2={isTop ? boxY + 44 : boxY}
                                    stroke="#2563eb"
                                    strokeWidth="1.5"
                                    strokeDasharray="3,2"
                                />
                                <circle cx={x} cy={lineY} r="5.5" fill="#2563eb" stroke="#ffffff" strokeWidth="2" />
                                <rect
                                    x={boxX}
                                    y={boxY}
                                    width={boxW}
                                    height="44"
                                    rx="6"
                                    fill="#eff6ff"
                                    stroke="#93c5fd"
                                />
                                <SvgRichLabel
                                    x={boxCenterX}
                                    y={boxY + 18}
                                    textAnchor="middle"
                                    fontSize={10}
                                    fontWeight="700"
                                    fill="#1e3a8a"
                                    text={prefixedLbl}
                                />
                                {ev.rate && (
                                    <SvgRichLabel
                                        x={boxCenterX}
                                        y={boxY + 35}
                                        textAnchor="middle"
                                        fontSize={9.5}
                                        fontWeight="600"
                                        fill="#047857"
                                        text={cleanSvgText(ev.rate)}
                                    />
                                )}
                            </g>
                        );
                    });
                })()}
            </svg>
        </div>
    );
}

function ProbabilityTreeAndVennSvg({ spec }) {
    if (spec.kind === 'venn_3_sets') {
        const sets = (spec.sets || ['Set A', 'Set B', 'Set C']).map(cleanSvgText);
        const lbl = spec.labels || {};
        return (
            <div
                data-testid="geogebra-stats-finance-graph"
                className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
            >
                <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                    <span className="font-semibold text-slate-700 uppercase tracking-wider">
                        3-Event Venn Diagram (Sample Space S)
                    </span>
                </div>
                <svg viewBox="0 0 540 340" className="w-full h-auto block bg-white">
                    <rect x="20" y="16" width="500" height="308" rx="10" fill="#f8fafc" stroke="#334155" strokeWidth="2" />
                    <text x="36" y="38" fontSize="13" fontWeight="700" fill="#0f172a">S</text>

                    {/* Three overlapping circles */}
                    <circle cx="215" cy="135" r="88" fill="#3b82f6" fillOpacity="0.14" stroke="#1d4ed8" strokeWidth="2.2" />
                    <circle cx="325" cy="135" r="88" fill="#10b981" fillOpacity="0.14" stroke="#047857" strokeWidth="2.2" />
                    <circle cx="270" cy="215" r="88" fill="#f59e0b" fillOpacity="0.14" stroke="#b45309" strokeWidth="2.2" />

                    {/* Set Titles */}
                    <text x="135" y="46" textAnchor="middle" fontSize="12" fontWeight="700" fill="#1d4ed8">{sets[0]}</text>
                    <text x="405" y="46" textAnchor="middle" fontSize="12" fontWeight="700" fill="#047857">{sets[1]}</text>
                    <text x="270" y="318" textAnchor="middle" fontSize="12" fontWeight="700" fill="#b45309">{sets[2]}</text>

                    {/* Region Counts */}
                    <text x="175" y="120" textAnchor="middle" fontSize="12" fontWeight="700" fill="#0f172a">{cleanSvgText(lbl.only_R)}</text>
                    <text x="365" y="120" textAnchor="middle" fontSize="11" fontWeight="700" fill="#0f172a">{cleanSvgText(lbl.only_S)}</text>
                    <text x="270" y="265" textAnchor="middle" fontSize="11" fontWeight="700" fill="#0f172a">{cleanSvgText(lbl.only_C)}</text>
                    <text x="270" y="105" textAnchor="middle" fontSize="12" fontWeight="700" fill="#1e293b">{cleanSvgText(lbl.R_and_S_only)}</text>
                    <text x="215" y="188" textAnchor="middle" fontSize="12" fontWeight="700" fill="#1e293b">{cleanSvgText(lbl.R_and_C_only)}</text>
                    <text x="325" y="188" textAnchor="middle" fontSize="12" fontWeight="700" fill="#dc2626">{cleanSvgText(lbl.S_and_C_only)}</text>
                    <text x="270" y="158" textAnchor="middle" fontSize="13" fontWeight="800" fill="#7c3aed">{cleanSvgText(lbl.all_three)}</text>
                    <text x="475" y="295" textAnchor="end" fontSize="12" fontWeight="700" fill="#475569">Outside = {cleanSvgText(lbl.outside)}</text>
                </svg>
            </div>
        );
    }

    if (spec.kind === 'contingency_table' && Array.isArray(spec.matrix) && Array.isArray(spec.rows) && Array.isArray(spec.columns)) {
        const rows = spec.rows;
        const cols = spec.columns;
        const mat = spec.matrix;
        return (
            <div
                data-testid="geogebra-stats-finance-graph"
                className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
            >
                <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                    <span className="font-semibold text-slate-700 uppercase tracking-wider">
                        {spec.title || 'Two-Way Contingency Table'}
                    </span>
                </div>
                <svg viewBox="0 0 540 200" className="w-full h-auto block bg-white">
                    <rect x="30" y="20" width="480" height="150" rx="8" fill="#f8fafc" stroke="#334155" strokeWidth="2" />
                    <line x1="170" y1="20" x2="170" y2="170" stroke="#334155" strokeWidth="1.5" />
                    <line x1="340" y1="20" x2="340" y2="170" stroke="#334155" strokeWidth="1.5" />
                    <line x1="30" y1="65" x2="510" y2="65" stroke="#334155" strokeWidth="1.5" />
                    <line x1="30" y1="118" x2="510" y2="118" stroke="#334155" strokeWidth="1.5" />
                    <text x="100" y="48" textAnchor="middle" fontSize="11.5" fontWeight="700" fill="#475569">Category</text>
                    {cols.slice(0, 2).map((c, ci) => (
                        <text key={ci} x={255 + ci * 170} y="48" textAnchor="middle" fontSize="11.5" fontWeight="700" fill="#1e3a8a">
                            {cleanSvgText(String(c))}
                        </text>
                    ))}
                    {rows.slice(0, 2).map((r, ri) => (
                        <g key={ri}>
                            <text x="100" y={96 + ri * 52} textAnchor="middle" fontSize="11.5" fontWeight="700" fill="#0f172a">
                                {cleanSvgText(String(r))}
                            </text>
                            {(mat[ri] || []).slice(0, 2).map((val, ci) => (
                                <text key={ci} x={255 + ci * 170} y={96 + ri * 52} textAnchor="middle" fontSize="13" fontWeight="800" fill="#2563eb">
                                    {val}
                                </text>
                            ))}
                        </g>
                    ))}
                </svg>
            </div>
        );
    }

    const tree = spec.tree;
    let s1 = tree?.branches_stage1;
    let s2 = tree?.branches_stage2;

    if (!s1 && Array.isArray(spec.branches) && spec.branches.length > 0) {
        const rawB = spec.branches;
        const outcomes = Array.isArray(spec.outcomes) ? spec.outcomes : [];
        if (typeof rawB[0] === 'object' && rawB[0] !== null) {
            s1 = rawB.map((b, idx) => ({
                choice: b.label || b.choice || b.name || `Branch ${idx + 1}`,
                prob: b.prob || b.probability || '',
            }));
            s2 = [];
            rawB.forEach((b, idx) => {
                const parentName = b.label || b.choice || b.name || `Branch ${idx + 1}`;
                const subs = Array.isArray(b.sub) ? b.sub : [];
                subs.forEach((subItem, sIdx) => {
                    const outIdx = idx * subs.length + sIdx;
                    const subChoice = typeof subItem === 'object' ? (subItem.label || subItem.choice || '') : String(subItem);
                    const subProb = typeof subItem === 'object' ? (subItem.prob || '') : '';
                    s2.push({
                        parent: parentName,
                        choice: subChoice,
                        prob: subProb,
                        outcomeLabel: outcomes[outIdx] || `${parentName}-${subChoice}`,
                    });
                });
            });
        } else {
            s1 = rawB.map((bStr) => {
                const str = String(bStr);
                const m = str.match(/^(.+?)\s*\((.+?)\)$/);
                return m ? { choice: m[1].trim(), prob: m[2].trim() } : { choice: str, prob: '' };
            });
            s2 = [];
            s1.forEach((b1, idx) => {
                s1.forEach((b2, sIdx) => {
                    const outIdx = idx * s1.length + sIdx;
                    s2.push({
                        parent: b1.choice,
                        choice: b2.choice,
                        prob: b2.prob,
                        outcomeLabel: outcomes[outIdx] || `${b1.choice[0] || ''}${b2.choice[0] || ''}`,
                    });
                });
            });
        }
    }

    if (!s1) {
        s1 = [
            { choice: 'Outcome A', prob: 'p' },
            { choice: 'Outcome B', prob: '1-p' },
        ];
    }
    if (!s2) s2 = [];

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {spec.title || 'Two-Stage Probability Tree Diagram'}
                </span>
            </div>
            <svg viewBox="0 0 540 260" className="w-full h-auto block bg-white">
                <circle cx="50" cy="130" r="5" fill="#0f172a" />
                {s1.map((b1, i) => {
                    const y1 = i === 0 ? 70 : 190;
                    const children = s2.filter((c) => c.parent === b1.choice);
                    return (
                        <g key={i}>
                            <line x1="50" y1="130" x2="210" y2={y1} stroke="#1d4ed8" strokeWidth="2.2" />
                            <SvgRichLabel
                                x={125}
                                y={(130 + y1) / 2 - 6}
                                textAnchor="middle"
                                fontSize={11}
                                fontWeight="700"
                                fill="#1d4ed8"
                                text={cleanSvgText(b1.prob)}
                            />
                            <rect x="210" y={y1 - 14} width="84" height="28" rx="6" fill="#eff6ff" stroke="#93c5fd" />
                            <SvgRichLabel
                                x={252}
                                y={y1 + 4}
                                textAnchor="middle"
                                fontSize={11}
                                fontWeight="700"
                                fill="#1e3a8a"
                                text={cleanSvgText(b1.choice)}
                            />

                            {children.map((ch, j) => {
                                const y2 = y1 + (j === 0 ? -32 : 32);
                                const outText = ch.outcomeLabel || `${ch.choice} (${b1.choice[0] || ''}${ch.choice[0] || ''})`;
                                return (
                                    <g key={j}>
                                        <line x1="294" y1={y1} x2="415" y2={y2} stroke="#059669" strokeWidth="2" />
                                        <SvgRichLabel
                                            x={354}
                                            y={(y1 + y2) / 2 - 5}
                                            textAnchor="middle"
                                            fontSize={10.5}
                                            fontWeight="700"
                                            fill="#047857"
                                            text={cleanSvgText(ch.prob)}
                                        />
                                        <SvgRichLabel
                                            x={422}
                                            y={y2 + 4}
                                            fontSize={11}
                                            fontWeight="700"
                                            fill="#0f172a"
                                            text={cleanSvgText(outText)}
                                        />
                                    </g>
                                );
                            })}
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function StepTariffAndBreakEvenSvg({ spec }) {
    if (spec.kind === 'break_even') {
        const fixedCost = Number(spec.fixed_cost || 1200);
        const varCost = Number(spec.variable_cost || 20);
        const price = Number(spec.selling_price || 50);
        const qBE = Math.round(fixedCost / Math.max(1, price - varCost));
        const rBE = qBE * price;
        const maxQ = Math.ceil((qBE * 1.8) / 10) * 10;
        const maxR = maxQ * price * 1.1;

        const W = 560;
        const H = 330;
        const padL = 62;
        const padR = 36;
        const padT = 28;
        const padB = 45;
        const plotW = W - padL - padR;
        const plotH = H - padT - padB;

        const sx = (q) => padL + (q / maxQ) * plotW;
        const sy = (r) => padT + plotH - (r / maxR) * plotH;

        return (
            <div
                data-testid="geogebra-stats-finance-graph"
                className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
            >
                <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                    <span className="font-semibold text-slate-700 uppercase tracking-wider">
                        Income, Cost & Break-Even Analysis
                    </span>
                    {spec.show_bep_coords === true && (
                        <span className="font-mono text-emerald-700 font-semibold">
                            Break-Even Point: ({qBE} units; R{rBE})
                        </span>
                    )}
                </div>
                <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                    <line x1={padL} y1={padT + plotH} x2={padL + plotW} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                    <line x1={padL} y1={padT} x2={padL} y2={padT + plotH} stroke="#334155" strokeWidth="2" />

                    {/* Cost line C(q) = fixed + var*q */}
                    <line
                        x1={sx(0)}
                        y1={sy(fixedCost)}
                        x2={sx(maxQ)}
                        y2={sy(fixedCost + varCost * maxQ)}
                        stroke="#dc2626"
                        strokeWidth="2.6"
                    />
                    {/* Income line I(q) = price*q */}
                    <line
                        x1={sx(0)}
                        y1={sy(0)}
                        x2={sx(maxQ)}
                        y2={sy(price * maxQ)}
                        stroke="#059669"
                        strokeWidth="2.6"
                    />

                    {/* Break-even point */}
                    <circle cx={sx(qBE)} cy={sy(rBE)} r="5.5" fill="#1d4ed8" stroke="#ffffff" strokeWidth="2" />
                    <text x={sx(qBE) + 10} y={sy(rBE) + 4} fontSize="11.5" fontWeight="700" fill="#1d4ed8">
                        {spec.show_bep_coords === false ? 'BEP' : `BEP (${qBE}; R${rBE})`}
                    </text>
                </svg>
            </div>
        );
    }

    // Stepped block tariff graph
    let blocks = spec.blocks;
    let usedFallback = false;
    if (!blocks && Array.isArray(spec.steps) && spec.steps.length > 0) {
        blocks = spec.steps.map((st, i) => ({
            range: st.range || st.label || (st.max ? `${st.min ?? 0}–${st.max} kL` : `>${st.min ?? 0} kL`),
            rate: Number(st.rate ?? st.cost_per_unit ?? st.cost ?? (10 + i * 10))
        }));
    }
    if (!blocks || blocks.length === 0) {
        usedFallback = true;
        blocks = [
            { range: '0–6 kL', rate: 12.5 },
            { range: '>6–15 kL', rate: 24.5 },
            { range: '>15–30 kL', rate: 36.0 },
            { range: '>30 kL', rate: 52.0 },
        ];
    }
    const maxRate = Math.max(...blocks.map((b) => b.rate), 60) * 1.15;

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            data-diagram-kind={spec.kind || 'step_tariff'}
            data-diagram-fallback={usedFallback ? 'true' : 'false'}
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    Municipal Stepped Block Tariff Profile
                </span>
            </div>
            <svg viewBox="0 0 560 260" className="w-full h-auto block bg-white">
                <line x1="60" y1="215" x2="520" y2="215" stroke="#334155" strokeWidth="2" />
                <line x1="60" y1="25" x2="60" y2="215" stroke="#334155" strokeWidth="2" />
                {blocks.map((b, i) => {
                    const x = 80 + i * 108;
                    const barH = (b.rate / maxRate) * 170;
                    const y = 215 - barH;
                    return (
                        <g key={i}>
                            <rect
                                x={x}
                                y={y}
                                width="88"
                                height={barH}
                                fill="#dbeafe"
                                stroke="#1d4ed8"
                                strokeWidth="2"
                                rx="4"
                            />
                            <text x={x + 44} y={y - 8} textAnchor="middle" fontSize="11" fontWeight="700" fill="#1e3a8a">
                                R{b.rate.toFixed(2).replace('.', ',')}/kL
                            </text>
                            <text x={x + 44} y="234" textAnchor="middle" fontSize="10.5" fontWeight="600" fill="#334155">
                                {cleanSvgText(b.range)}
                            </text>
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}


function ProbabilitySpinnerSvg({ spec }) {
    const numSectors = Number(spec.sectors || 8);
    const labels = spec.labels || Array.from({ length: numSectors }, (_, i) => String(i + 1));
    const title = spec.title || `${numSectors}-Sector Probability Spinner (Outcomes 1–${numSectors})`;
    const cx = 280;
    const cy = 160;
    const R = 115;
    const colors = [
        '#dbeafe', '#fef3c7', '#dcfce7', '#fce7f3',
        '#e0e7ff', '#fed7aa', '#ccfbf1', '#f3e8ff'
    ];
    const angleStep = (2 * Math.PI) / numSectors;

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {title}
                </span>
                <span className="font-mono text-blue-700 font-semibold">
                    Equally Likely Outcomes (P = 1/{numSectors})
                </span>
            </div>
            <svg viewBox="0 0 560 320" className="w-full h-auto block bg-white">
                <circle cx={cx} cy={cy} r={R + 6} fill="#f8fafc" stroke="#64748b" strokeWidth="4" />
                {Array.from({ length: numSectors }).map((_, i) => {
                    const startAngle = i * angleStep - Math.PI / 2;
                    const endAngle = (i + 1) * angleStep - Math.PI / 2;
                    const x1 = cx + R * Math.cos(startAngle);
                    const y1 = cy + R * Math.sin(startAngle);
                    const x2 = cx + R * Math.cos(endAngle);
                    const y2 = cy + R * Math.sin(endAngle);
                    const midAngle = (startAngle + endAngle) / 2;
                    const labelR = R * 0.65;
                    const lx = cx + labelR * Math.cos(midAngle);
                    const ly = cy + labelR * Math.sin(midAngle);

                    const pathData = `M ${cx} ${cy} L ${x1} ${y1} A ${R} ${R} 0 0 1 ${x2} ${y2} Z`;
                    return (
                        <g key={i}>
                            <path
                                d={pathData}
                                fill={colors[i % colors.length]}
                                stroke="#475569"
                                strokeWidth="2"
                            />
                            <text
                                x={lx}
                                y={ly + 5}
                                textAnchor="middle"
                                fontSize="16"
                                fontWeight="800"
                                fill="#1e293b"
                            >
                                {labels[i] ?? String(i + 1)}
                            </text>
                        </g>
                    );
                })}

                <circle cx={cx} cy={cy} r="14" fill="#334155" stroke="#ffffff" strokeWidth="2" />
                <polygon
                    points={`${cx},${cy - 8} ${cx + 70},${cy - 50} ${cx + 12},${cy + 2}`}
                    fill="#dc2626"
                    stroke="#991b1b"
                    strokeWidth="1.5"
                />
                <circle cx={cx} cy={cy} r="5" fill="#f8fafc" />
                <text x={cx} y={cy + R + 26} textAnchor="middle" fontSize="11" fontWeight="700" fill="#64748b">
                    Spin Direction ↻ (Fair Wheel)
                </text>
            </svg>
        </div>
    );
}

function FunctionFlowSvg({ spec }) {
    const inputVal = spec.input || 'x';
    const rule1 = spec.rule_step1 || '× 4';
    const rule2 = spec.rule_step2 || '+ 5';
    const outputVal = spec.output || 'y';
    const title = spec.title || 'Linear Function Machine: Flow Diagram';

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {title}
                </span>
                <span className="font-mono text-indigo-700 font-semibold">
                    Input ➔ Processing Rules ➔ Output
                </span>
            </div>
            <svg viewBox="0 0 560 160" className="w-full h-auto block bg-white">
                <defs>
                    <marker id="flow-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                        <path d="M 0 1 L 10 5 L 0 9 z" fill="#4f46e5" />
                    </marker>
                </defs>

                <rect x="25" y="45" width="95" height="60" rx="8" fill="#eff6ff" stroke="#3b82f6" strokeWidth="2" />
                <text x="72" y="68" textAnchor="middle" fontSize="11" fontWeight="700" fill="#1e40af">INPUT</text>
                <text x="72" y="92" textAnchor="middle" fontSize="15" fontWeight="800" fill="#1d4ed8">{inputVal}</text>

                <line x1="120" y1="75" x2="160" y2="75" stroke="#4f46e5" strokeWidth="2.5" markerEnd="url(#flow-arrow)" />

                <rect x="165" y="40" width="105" height="70" rx="10" fill="#f5f3ff" stroke="#7c3aed" strokeWidth="2" />
                <text x="217" y="63" textAnchor="middle" fontSize="10.5" fontWeight="600" fill="#6d28d9">RULE STEP 1</text>
                <text x="217" y="93" textAnchor="middle" fontSize="17" fontWeight="900" fill="#5b21b6">{rule1}</text>

                <line x1="270" y1="75" x2="305" y2="75" stroke="#4f46e5" strokeWidth="2.5" markerEnd="url(#flow-arrow)" />

                <rect x="310" y="40" width="105" height="70" rx="10" fill="#fdf4ff" stroke="#c026d3" strokeWidth="2" />
                <text x="362" y="63" textAnchor="middle" fontSize="10.5" fontWeight="600" fill="#a21caf">RULE STEP 2</text>
                <text x="362" y="93" textAnchor="middle" fontSize="17" fontWeight="900" fill="#86198f">{rule2}</text>

                <line x1="415" y1="75" x2="450" y2="75" stroke="#4f46e5" strokeWidth="2.5" markerEnd="url(#flow-arrow)" />

                <rect x="455" y="45" width="85" height="60" rx="8" fill="#ecfdf5" stroke="#059669" strokeWidth="2" />
                <text x="497" y="68" textAnchor="middle" fontSize="11" fontWeight="700" fill="#065f46">OUTPUT</text>
                <text x="497" y="92" textAnchor="middle" fontSize="15" fontWeight="800" fill="#047857">{outputVal}</text>
            </svg>
        </div>
    );
}

function BarChartSvg({ spec }) {
    let categories = spec.categories;
    let values = spec.values;
    let series2 = spec.values2;
    let usedFallback = false;

    if (Array.isArray(spec.bars) && spec.bars.length > 0) {
        categories = spec.bars.map((b) => b.label || b.category || b.name || String(b));
        values = spec.bars.map((b) => Number(b.value ?? b.count ?? b.y ?? 0));
    } else if (Array.isArray(spec.series) && spec.series.length > 0) {
        const s1 = spec.series[0];
        const s2 = spec.series[1];
        if (s1 && Array.isArray(s1.data)) {
            categories = s1.data.map((d) => d.label || d.category || d.x || String(d));
            values = s1.data.map((d) => Number(d.value ?? d.y ?? 0));
        }
        if (s2 && Array.isArray(s2.data)) {
            series2 = s2.data.map((d) => Number(d.value ?? d.y ?? 0));
        }
    }

    if (!Array.isArray(categories) || categories.length === 0) {
        usedFallback = true;
        categories = ['Cat A', 'Cat B', 'Cat C', 'Cat D'];
        values = [28, 42, 35, 50];
    } else {
        values = (values || []).map(Number);
        if (series2) series2 = series2.map(Number);
    }
    const title = spec.title || (spec.kind === 'histogram' ? 'Grouped Frequency Histogram' : 'Discrete Frequency Bar Graph');
    const yLabel = spec.y_label || 'Frequency';
    const isHistogram = spec.kind === 'histogram';

    const maxVal = Math.max(10, ...values, ...(series2 || []));
    const yMax = Math.ceil((maxVal * 1.15) / 5) * 5;
    const W = 560;
    const H = 260;
    const padL = 55;
    const padR = 30;
    const padT = 30;
    const padB = 45;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const sy = (v) => padT + plotH - (v / yMax) * plotH;
    const slotW = plotW / categories.length;
    const barW = isHistogram ? slotW - 2 : (series2 ? Math.min(28, slotW * 0.36) : Math.min(48, slotW * 0.58));

    const yTicks = [0, Math.round(yMax * 0.25), Math.round(yMax * 0.5), Math.round(yMax * 0.75), yMax];

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            data-diagram-kind={spec.kind || 'bar_graph'}
            data-diagram-fallback={usedFallback ? 'true' : 'false'}
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">{title}</span>
                <span className="font-mono text-blue-700 font-semibold">{yLabel}</span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {yTicks.map((t, idx) => (
                    <g key={idx}>
                        <line x1={padL} y1={sy(t)} x2={W - padR} y2={sy(t)} stroke="#f1f5f9" strokeWidth="1" />
                        <text x={padL - 8} y={sy(t) + 4} textAnchor="end" fontSize="10.5" fontWeight="600" fill="#64748b">
                            {t}
                        </text>
                    </g>
                ))}
                <line x1={padL} y1={padT} x2={padL} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                <line x1={padL} y1={padT + plotH} x2={W - padR} y2={padT + plotH} stroke="#334155" strokeWidth="2" />

                {categories.map((cat, idx) => {
                    const v1 = values[idx] ?? 0;
                    const cx = padL + idx * slotW + slotW / 2;
                    const x1 = series2 ? cx - barW - 2 : cx - barW / 2;
                    const h1 = Math.max(2, (v1 / yMax) * plotH);
                    return (
                        <g key={idx}>
                            <rect
                                x={x1}
                                y={sy(v1)}
                                width={barW}
                                height={h1}
                                fill="#3b82f6"
                                fillOpacity="0.82"
                                stroke="#1d4ed8"
                                strokeWidth="1.5"
                                rx={isHistogram ? 0 : 3}
                            />
                            <text x={x1 + barW / 2} y={sy(v1) - 5} textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#1e3a8a">
                                {v1}
                            </text>
                            {series2 && (
                                <>
                                    <rect
                                        x={cx + 2}
                                        y={sy(series2[idx] ?? 0)}
                                        width={barW}
                                        height={Math.max(2, ((series2[idx] ?? 0) / yMax) * plotH)}
                                        fill="#10b981"
                                        fillOpacity="0.82"
                                        stroke="#047857"
                                        strokeWidth="1.5"
                                        rx="3"
                                    />
                                    <text x={cx + 2 + barW / 2} y={sy(series2[idx] ?? 0) - 5} textAnchor="middle" fontSize="10.5" fontWeight="700" fill="#065f46">
                                        {series2[idx] ?? 0}
                                    </text>
                                </>
                            )}
                            <text x={cx} y={padT + plotH + 18} textAnchor="middle" fontSize="11" fontWeight="600" fill="#334155">
                                {cat}
                            </text>
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function PieChartSvg({ spec }) {
    let rawSectors = spec.sectors;
    let usedFallback = false;
    if (!rawSectors && Array.isArray(spec.slices) && spec.slices.length > 0) {
        rawSectors = spec.slices.map((s) => ({
            label: s.label || s.name || s.category || 'Sector',
            value: Number(s.value ?? s.pct ?? s.percentage ?? 10)
        }));
    }
    if (!Array.isArray(rawSectors) || rawSectors.length === 0) {
        usedFallback = true;
        rawSectors = [
            { label: 'Sector A', value: 40 },
            { label: 'Sector B', value: 30 },
            { label: 'Sector C', value: 20 },
            { label: 'Sector D', value: 10 },
        ];
    }
    const total = Math.max(1, rawSectors.reduce((acc, s) => acc + Number(s.value || 1), 0));
    const palette = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ec4899', '#06b6d4'];
    const cx = 175;
    const cy = 125;
    const R = 86;
    let startAngle = -Math.PI / 2;

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            data-diagram-kind={spec.kind || 'pie_chart'}
            data-diagram-fallback={usedFallback ? 'true' : 'false'}
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">
                    {spec.title || 'Proportional Pie Chart (360° Circle)'}
                </span>
                <span className="font-mono text-indigo-700 font-semibold">Total = {total}</span>
            </div>
            <svg viewBox="0 0 560 250" className="w-full h-auto block bg-white">
                {rawSectors.map((sec, idx) => {
                    const val = Number(sec.value || 1);
                    const sweep = (val / total) * 2 * Math.PI;
                    const endAngle = startAngle + sweep;
                    const x1 = cx + R * Math.cos(startAngle);
                    const y1 = cy + R * Math.sin(startAngle);
                    const x2 = cx + R * Math.cos(endAngle);
                    const y2 = cy + R * Math.sin(endAngle);
                    const largeArc = sweep > Math.PI ? 1 : 0;
                    const pathData = `M ${cx} ${cy} L ${x1} ${y1} A ${R} ${R} 0 ${largeArc} 1 ${x2} ${y2} Z`;
                    startAngle = endAngle;
                    const col = palette[idx % palette.length];
                    const pct = Math.round((val / total) * 100);
                    return (
                        <g key={idx}>
                            <path d={pathData} fill={col} fillOpacity="0.85" stroke="#ffffff" strokeWidth="2" />
                            <rect x={320} y={42 + idx * 34} width={14} height={14} rx="3" fill={col} />
                            <text x={342} y={53 + idx * 34} fontSize="12" fontWeight="700" fill="#1e293b">
                                {sec.label}: {val} ({pct}%)
                            </text>
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

function LineGraphSvg({ spec }) {
    const title = spec.title || 'Trend & Time-Series Line Graph';
    const xLabel = spec.x_label || 'Category / Period';
    const yLabel = spec.y_label || 'Value';
    const palette = ['#2563eb', '#dc2626', '#059669', '#7c3aed'];

    let categories = Array.isArray(spec.categories) ? spec.categories.map(String) : [];
    const seriesList = [];

    if (Array.isArray(spec.series) && spec.series.length > 0) {
        spec.series.forEach((s, idx) => {
            if (Array.isArray(s.values)) {
                seriesList.push({
                    name: s.name || `Series ${idx + 1}`,
                    values: s.values.map(Number),
                });
            } else if (Array.isArray(s.points)) {
                if (categories.length === 0) {
                    categories = s.points.map((pt) => String(Array.isArray(pt) ? pt[0] : pt.x));
                }
                seriesList.push({
                    name: s.name || `Series ${idx + 1}`,
                    values: s.points.map((pt) => Number(Array.isArray(pt) ? pt[1] : pt.y)),
                });
            }
        });
    }

    if (seriesList.length === 0 && Array.isArray(spec.values) && spec.values.length > 0) {
        seriesList.push({
            name: yLabel,
            values: spec.values.map(Number),
        });
    }

    if (categories.length === 0 && seriesList.length > 0) {
        categories = seriesList[0].values.map((_, i) => `T${i + 1}`);
    }

    const allVals = seriesList.flatMap((s) => s.values).filter((v) => !Number.isNaN(v));
    const maxVal = Math.max(10, ...allVals);
    const minVal = Math.min(0, ...allVals);
    const yMax = Math.ceil((maxVal * 1.15) / 5) * 5;
    const yMin = Math.floor(minVal / 5) * 5;

    const W = 560;
    const H = 270;
    const padL = 58;
    const padR = 35;
    const padT = 30;
    const padB = 48;
    const plotW = W - padL - padR;
    const plotH = H - padT - padB;

    const nCats = Math.max(1, categories.length);
    const sx = (idx) => (nCats === 1 ? padL + plotW / 2 : padL + (idx / (nCats - 1)) * plotW);
    const sy = (v) => padT + plotH - ((v - yMin) / Math.max(1e-5, yMax - yMin)) * plotH;
    const yTicks = [yMin, Math.round(yMin + (yMax - yMin) * 0.25), Math.round(yMin + (yMax - yMin) * 0.5), Math.round(yMin + (yMax - yMin) * 0.75), yMax];

    return (
        <div
            data-testid="geogebra-stats-finance-graph"
            data-diagram-kind={spec.kind || 'line_graph'}
            className="w-full rounded-xl border border-slate-200 bg-white shadow-sm overflow-hidden my-2"
        >
            <div className="flex items-center justify-between px-3.5 py-2 bg-slate-50 border-b border-slate-200 text-xs">
                <span className="font-semibold text-slate-700 uppercase tracking-wider">{title}</span>
                <span className="font-mono text-blue-700 font-semibold">{xLabel} vs {yLabel}</span>
            </div>
            <svg viewBox={`0 0 ${W} ${H}`} className="w-full h-auto block bg-white">
                {yTicks.map((t, idx) => (
                    <g key={idx}>
                        <line x1={padL} y1={sy(t)} x2={W - padR} y2={sy(t)} stroke="#f1f5f9" strokeWidth="1" />
                        <text x={padL - 8} y={sy(t) + 4} textAnchor="end" fontSize="10.5" fontWeight="600" fill="#64748b">
                            {t}
                        </text>
                    </g>
                ))}
                <line x1={padL} y1={padT} x2={padL} y2={padT + plotH} stroke="#334155" strokeWidth="2" />
                <line x1={padL} y1={padT + plotH} x2={W - padR} y2={padT + plotH} stroke="#334155" strokeWidth="2" />

                {categories.map((cat, idx) => (
                    <text key={idx} x={sx(idx)} y={padT + plotH + 18} textAnchor="middle" fontSize="10.5" fontWeight="600" fill="#334155">
                        {cat}
                    </text>
                ))}

                {seriesList.map((ser, sIdx) => {
                    const col = palette[sIdx % palette.length];
                    const pts = ser.values.map((v, i) => [sx(i), sy(v), v]);
                    const polyStr = pts.map(([px, py]) => `${px},${py}`).join(' ');
                    return (
                        <g key={sIdx}>
                            {pts.length >= 2 && (
                                <polyline fill="none" stroke={col} strokeWidth="2.6" points={polyStr} />
                            )}
                            {pts.map(([px, py, val], pIdx) => (
                                <g key={pIdx}>
                                    <circle cx={px} cy={py} r="4.5" fill={col} stroke="#ffffff" strokeWidth="1.5" />
                                    <text x={px} y={py - 8} textAnchor="middle" fontSize="10" fontWeight="700" fill={col}>
                                        {val}
                                    </text>
                                </g>
                            ))}
                        </g>
                    );
                })}
            </svg>
        </div>
    );
}

export default function StatsAndFinancialGraphRenderer({ spec }) {
    if (!spec) return null;
    switch (spec.kind) {
        case 'box_and_whisker':
            return <BoxAndWhiskerSvg spec={spec} />;
        case 'statistics_box_and_ogive':
        case 'ogive':
        case 'cumulative_frequency':
            return <OgiveAndBoxSvg spec={spec} />;
        case 'scatter_plot_regression':
        case 'scatter_plot':
            return <ScatterRegressionSvg spec={spec} />;
        case 'timeline_finance':
            return <TimelineFinanceSvg spec={spec} />;
        case 'venn_3_sets':
        case 'venn_diagram':
        case 'contingency_table_and_tree':
        case 'contingency_table':
        case 'tree_diagram':
            return <ProbabilityTreeAndVennSvg spec={spec} />;
        case 'step_tariff':
        case 'break_even':
            return <StepTariffAndBreakEvenSvg spec={spec} />;
        case 'probability_spinner':
            return <ProbabilitySpinnerSvg spec={spec} />;
        case 'function_flow':
        case 'flow_diagram':
            return <FunctionFlowSvg spec={spec} />;
        case 'bar_graph':
        case 'double_bar_graph':
        case 'histogram':
        case 'frequency_polygon':
            return <BarChartSvg spec={spec} />;
        case 'line_graph':
        case 'broken_line_graph':
            return <LineGraphSvg spec={spec} />;
        case 'pie_chart':
            return <PieChartSvg spec={spec} />;
        default:
            return null;
    }
}
