import React, { useMemo, useState } from 'react';

const clamp = (v, lo, hi) => Math.max(lo, Math.min(hi, v));

const FunctionGraph = ({ graph, className = '' }) => {
    const [hover, setHover] = useState(null);

    const cfg = graph || {};
    const xRange = Array.isArray(cfg.x_range) ? cfg.x_range : [-10, 10];
    const yRange = Array.isArray(cfg.y_range) ? cfg.y_range : [-10, 10];

    const xMin = Number(xRange[0] ?? -10);
    const xMax = Number(xRange[1] ?? 10);
    const yMin = Number(yRange[0] ?? -10);
    const yMax = Number(yRange[1] ?? 10);

    const m = Number(cfg.m ?? 1);
    const c = Number(cfg.c ?? 0);

    const gridStep = Number(cfg.grid_step ?? 1);
    const points = Array.isArray(cfg.points) ? cfg.points : [];

    const viewBox = useMemo(() => {
        const w = xMax - xMin;
        const h = yMax - yMin;
        return `${xMin} ${-yMax} ${w} ${h}`;
    }, [xMin, xMax, yMin, yMax]);

    const linePath = useMemo(() => {
        const y1 = m * xMin + c;
        const y2 = m * xMax + c;
        return `M ${xMin} ${-y1} L ${xMax} ${-y2}`;
    }, [m, c, xMin, xMax]);

    const gridLines = useMemo(() => {
        const lines = [];
        if (!Number.isFinite(gridStep) || gridStep <= 0) return lines;

        const xStart = Math.ceil(xMin / gridStep) * gridStep;
        for (let x = xStart; x <= xMax; x += gridStep) {
            lines.push({ type: 'v', x });
        }

        const yStart = Math.ceil(yMin / gridStep) * gridStep;
        for (let y = yStart; y <= yMax; y += gridStep) {
            lines.push({ type: 'h', y });
        }

        return lines;
    }, [xMin, xMax, yMin, yMax, gridStep]);

    const toMathCoord = (evt) => {
        const svg = evt.currentTarget;
        const rect = svg.getBoundingClientRect();
        const px = clamp(evt.clientX - rect.left, 0, rect.width);
        const py = clamp(evt.clientY - rect.top, 0, rect.height);

        const x = xMin + (px / rect.width) * (xMax - xMin);
        const y = yMax - (py / rect.height) * (yMax - yMin);
        return { x, y };
    };

    return (
        <div className={`w-full ${className}`}>
            <div className="rounded-xl border border-gray-200 bg-white overflow-hidden">
                <div className="px-4 py-3 border-b border-gray-200 flex items-center justify-between">
                    <div className="text-sm font-semibold text-gray-900">Graph</div>
                    <div className="text-xs text-gray-600 font-mono">y = {m}x {c >= 0 ? '+' : ''}{c}</div>
                </div>

                <div className="p-3">
                    <div className="relative">
                        <svg
                            viewBox={viewBox}
                            preserveAspectRatio="none"
                            className="w-full h-64 bg-gray-50 rounded-lg border border-gray-200"
                            onMouseMove={(e) => setHover(toMathCoord(e))}
                            onMouseLeave={() => setHover(null)}
                        >
                            <g>
                                {gridLines.map((l) => (
                                    l.type === 'v' ? (
                                        <line
                                            key={`v_${l.x}`}
                                            x1={l.x}
                                            y1={-yMin}
                                            x2={l.x}
                                            y2={-yMax}
                                            stroke={l.x === 0 ? '#111827' : '#E5E7EB'}
                                            strokeWidth={l.x === 0 ? 0.15 : 0.08}
                                        />
                                    ) : (
                                        <line
                                            key={`h_${l.y}`}
                                            x1={xMin}
                                            y1={-l.y}
                                            x2={xMax}
                                            y2={-l.y}
                                            stroke={l.y === 0 ? '#111827' : '#E5E7EB'}
                                            strokeWidth={l.y === 0 ? 0.15 : 0.08}
                                        />
                                    )
                                ))}
                            </g>

                            <path d={linePath} stroke="#2563EB" strokeWidth={0.2} fill="none" />

                            {points.map((p, idx) => (
                                <g key={`pt_${idx}_${p.x}_${p.y}`}>
                                    <circle cx={p.x} cy={-p.y} r={0.25} fill="#DC2626" />
                                    {p.label && (
                                        <text x={p.x + 0.4} y={-(p.y) - 0.4} fontSize={0.9} fill="#374151">
                                            {p.label}
                                        </text>
                                    )}
                                </g>
                            ))}
                        </svg>

                        {hover && (
                            <div className="absolute top-2 right-2 bg-white/95 backdrop-blur border border-gray-200 rounded-lg px-2 py-1 text-xs font-mono text-gray-700">
                                x={hover.x.toFixed(2)}, y={hover.y.toFixed(2)}
                            </div>
                        )}
                    </div>

                    <div className="mt-2 text-xs text-gray-600">
                        Hover to read coordinates.
                    </div>
                </div>
            </div>
        </div>
    );
};

export default FunctionGraph;
