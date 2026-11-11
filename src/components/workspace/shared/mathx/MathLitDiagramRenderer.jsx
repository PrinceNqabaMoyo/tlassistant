import React from 'react';

/**
 * MathLitDiagramRenderer — Dedicated Examination-Standard Vector Renderer for
 * Mathematical Literacy (Grades 10–12).
 *
 * Implements Rule 0d-14 & Diagram Doctrine:
 * - 100% Static, 2D Parameter-Locked Examination Figures.
 * - Archival Paper Folio aesthetic (#FAF8F3 background, stone borders #EAE5DC, charcoal #1E2022).
 * - Exact seeded dimensions matching question prompt parameters.
 */

export function MathLitDiagramRenderer({ spec }) {
    if (!spec) return null;

    const kind = (spec.kind || spec.diagram_type || spec.type || '').toLowerCase();
    const title = spec.title || spec.caption || 'Examination Diagram Stimulus';

    // 1. INLINE SVG DIRECT RENDERER
    if (kind === 'inline_svg' || spec.svg || spec.svg_data) {
        const svgString = spec.svg || spec.svg_data || '';
        return (
            <div data-testid="mathlit-inline-svg" className="flex flex-col items-center w-full my-2">
                {title && (
                    <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                        {title}
                    </div>
                )}
                <div
                    className="p-3 bg-white rounded-xl border border-slate-200 shadow-2xs overflow-auto max-w-full"
                    dangerouslySetInnerHTML={{ __html: svgString }}
                />
            </div>
        );
    }

    // 2. ARCHITECTURAL FLOOR PLAN
    if (kind === 'floor_plan') {
        const rawRooms = spec.rooms || ['Bedroom 1', 'Bedroom 2', 'Kitchen', 'Lounge', 'Bathroom'];
        const rooms = rawRooms.map((r, i) => {
            if (typeof r === 'object' && r !== null) {
                const name = r.name || r.label || `Room ${i + 1}`;
                const lStr = r.length_m ? `${String(r.length_m).replace('.', ',')} m` : '';
                const wStr = r.width_m ? `${String(r.width_m).replace('.', ',')} m` : '';
                const dims = lStr && wStr ? `${lStr} × ${wStr}` : (r.dimensions || '');
                return { name, dims, length_m: r.length_m, width_m: r.width_m };
            }
            return { name: String(r), dims: '', length_m: null, width_m: null };
        });
        const scale = spec.scale || '1 : 100';
        const totalLength = spec.length_m ? `${String(spec.length_m).replace('.', ',')} m` : (spec.total_length || '10,8 m');
        const totalWidth = spec.width_m ? `${String(spec.width_m).replace('.', ',')} m` : (spec.total_width || '7,0 m');

        return (
            <div data-testid="mathlit-diagram-floor-plan" className="flex flex-col items-center w-full my-2">
                <div className="w-full flex items-center justify-between px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-t-xl text-xs font-semibold text-slate-700">
                    <span>{title}</span>
                    <span className="font-mono text-slate-500">Scale {scale}</span>
                </div>
                <div className="w-full p-4 bg-white border-x border-b border-slate-200 rounded-b-xl flex justify-center">
                    <svg viewBox="0 0 540 320" className="w-full max-w-[540px] h-auto font-sans">
                        {/* Outer Perimeter Walls (Double Line for Architectural Standard) */}
                        <rect x="30" y="30" width="480" height="260" fill="#FAF8F3" stroke="#1E2022" strokeWidth="4" />
                        <rect x="34" y="34" width="472" height="252" fill="none" stroke="#64748B" strokeWidth="1" />

                        {/* Room Dividing Walls */}
                        <line x1="260" y1="30" x2="260" y2="290" stroke="#1E2022" strokeWidth="3" />
                        <line x1="30" y1="160" x2="260" y2="160" stroke="#1E2022" strokeWidth="3" />
                        <line x1="260" y1="180" x2="510" y2="180" stroke="#1E2022" strokeWidth="3" />
                        <line x1="390" y1="180" x2="390" y2="290" stroke="#1E2022" strokeWidth="3" />

                        {/* Room Labels & Dimension Callouts */}
                        <text x="145" y="100" textAnchor="middle" fontSize="13" fontWeight="bold" fill="#0F172A">
                            {rooms[0]?.name || 'Bedroom 1'}
                        </text>
                        <text x="145" y="118" textAnchor="middle" fontSize="10" fill="#64748B">
                            {rooms[0]?.dims || '3,8 m × 3,2 m'}
                        </text>

                        <text x="145" y="230" textAnchor="middle" fontSize="13" fontWeight="bold" fill="#0F172A">
                            {rooms[1]?.name || 'Bedroom 2'}
                        </text>
                        <text x="145" y="248" textAnchor="middle" fontSize="10" fill="#64748B">
                            {rooms[1]?.dims || '3,5 m × 3,2 m'}
                        </text>

                        <text x="385" y="105" textAnchor="middle" fontSize="13" fontWeight="bold" fill="#0F172A">
                            {rooms[3]?.name || 'Lounge / Living'}
                        </text>
                        <text x="385" y="123" textAnchor="middle" fontSize="10" fill="#64748B">
                            {rooms[3]?.dims || '5,2 m × 3,8 m'}
                        </text>

                        <text x="325" y="240" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#0F172A">
                            {rooms[2]?.name || 'Kitchen'}
                        </text>

                        <text x="450" y="240" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#0F172A">
                            {rooms[4]?.name || 'Bathroom'}
                        </text>

                        {/* Door Swing Arcs */}
                        {/* Front Exterior Door */}
                        <path d="M 360 290 A 24 24 0 0 1 384 266" fill="none" stroke="#2563EB" strokeWidth="1.5" strokeDasharray="2,2" />
                        <line x1="360" y1="290" x2="384" y2="266" stroke="#2563EB" strokeWidth="2" />
                        <text x="372" y="306" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#2563EB">Front Door</text>

                        {/* Bedroom 1 Door */}
                        <path d="M 260 110 A 20 20 0 0 1 240 90" fill="none" stroke="#2563EB" strokeWidth="1.5" strokeDasharray="2,2" />
                        <line x1="260" y1="110" x2="240" y2="90" stroke="#2563EB" strokeWidth="2" />

                        {/* Windows (Parallel Line Symbols within Wall Openings) */}
                        <rect x="80" y="27" width="50" height="6" fill="#38BDF8" stroke="#0284C7" strokeWidth="1" />
                        <rect x="80" y="287" width="50" height="6" fill="#38BDF8" stroke="#0284C7" strokeWidth="1" />
                        <rect x="420" y="27" width="60" height="6" fill="#38BDF8" stroke="#0284C7" strokeWidth="1" />
                        <rect x="507" y="90" width="6" height="50" fill="#38BDF8" stroke="#0284C7" strokeWidth="1" />

                        {/* North Arrow Compass Indicator */}
                        <g transform="translate(480, 70)">
                            <circle cx="0" cy="0" r="16" fill="#FFFFFF" stroke="#CBD5E1" strokeWidth="1" />
                            <polygon points="0,-12 4,4 0,0 -4,4" fill="#DC2626" />
                            <text x="0" y="-14" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#DC2626">N</text>
                        </g>

                        {/* Dimension Leader Lines */}
                        <line x1="30" y1="15" x2="510" y2="15" stroke="#94A3B8" strokeWidth="1" markerStart="url(#arrow)" markerEnd="url(#arrow)" />
                        <text x="270" y="11" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#475569">Total Length: {totalLength}</text>
                        <line x1="15" y1="30" x2="15" y2="290" stroke="#94A3B8" strokeWidth="1" />
                        <text x="11" y="165" textAnchor="middle" fontSize="10" fontWeight="bold" fill="#475569" transform="rotate(-90 11 165)">Width: {totalWidth}</text>
                    </svg>
                </div>
            </div>
        );
    }

    // 3. GRAPHIC BAR SCALE
    if (kind === 'bar_scale' || kind === 'graphic_scale') {
        const firstSeg = Array.isArray(spec.segments) && typeof spec.segments[0] === 'object' ? spec.segments[0] : null;
        const segLenCm = Number(spec.segment_length_cm || spec.length_cm || spec.bar_len_cm || firstSeg?.length_cm || 2);
        const isMetres = spec.segment_value_m !== undefined || firstSeg?.unit === 'm';
        const unitLabel = isMetres ? 'm' : 'km';
        const totalSegs = Number(spec.total_segments || (typeof spec.segments === 'number' ? spec.segments : 4));
        const segVal = Number(
            spec.segment_value_km ??
            spec.segment_value_m ??
            spec.represents_km ??
            firstSeg?.real_val ??
            (spec.total_km ? Number(spec.total_km) / Math.max(1, totalSegs) : null) ??
            spec.bar_km ??
            10
        );
        const totalVal = Number(spec.total_km ?? (segVal * totalSegs));
        const ratioDisplay = spec.scale || spec.ratio_str || spec.ratio || `1 cm represents ${(segVal / Math.max(0.1, segLenCm)).toLocaleString('en-ZA')} ${unitLabel}`;
        const measuredCm = spec.measured_cm || spec.measured_line_cm || spec.measured_map_distance_cm || firstSeg?.label;

        return (
            <div data-testid="mathlit-diagram-bar-scale" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title}
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center">
                    <svg viewBox="0 0 460 105" className="w-full max-w-[460px] h-auto font-sans">
                        {/* Bar Scale Alternating Blocks */}
                        {Array.from({ length: totalSegs }).map((_, i) => {
                            const x = 50 + i * 80;
                            const isEven = i % 2 === 0;
                            return (
                                <g key={i}>
                                    <rect
                                        x={x}
                                        y={30}
                                        width={80}
                                        height={14}
                                        fill={isEven ? '#1E2022' : '#FFFFFF'}
                                        stroke="#1E2022"
                                        strokeWidth="1.5"
                                    />
                                    <line x1={x} y1={25} x2={x} y2={44} stroke="#1E2022" strokeWidth="1.5" />
                                    <text x={x} y={20} textAnchor="middle" fontSize="11" fontWeight="bold" fill="#1E2022">
                                        {Number((i * segVal).toFixed(2))}
                                    </text>
                                </g>
                            );
                        })}
                        <line x1={50 + totalSegs * 80} y1={25} x2={50 + totalSegs * 80} y2={44} stroke="#1E2022" strokeWidth="1.5" />
                        <text x={50 + totalSegs * 80} y={20} textAnchor="middle" fontSize="11" fontWeight="bold" fill="#1E2022">
                            {Number(totalVal.toFixed(2))} {unitLabel}
                        </text>

                        <line x1={50} y1={65} x2={50 + 80} y2={65} stroke="#2563EB" strokeWidth="2" />
                        <text x={150} y={84} textAnchor="middle" fontSize="11" fontWeight="bold" fill="#2563EB">
                            {segLenCm} cm on ruler = {segVal} {unitLabel} {measuredCm ? `| Measured: ${measuredCm}${typeof measuredCm === 'number' ? ' cm' : ''}` : ''}
                        </text>
                    </svg>
                    <span className="text-[11px] font-mono text-slate-600 mt-1">
                        Scale: {ratioDisplay} {spec.enlargement_percent ? `(Enlarged ${spec.enlargement_percent}%)` : ''}
                    </span>
                </div>
            </div>
        );
    }

    // 4. COMPASS ROSE & BEARINGS
    if (kind === 'compass_rose' || kind === 'bearing_map' || kind === 'elevation_compass') {
        const dirToDeg = {
            north: 0, n: 0,
            'north-east': 45, ne: 45,
            east: 90, e: 90,
            'south-east': 135, se: 135,
            south: 180, s: 180,
            'south-west': 225, sw: 225,
            west: 270, w: 270,
            'north-west': 315, nw: 315,
        };
        const dirStr = String(spec.target_dir || spec.wall_direction || '').toLowerCase().trim();
        const resolvedDeg = spec.bearing_deg ?? spec.angle ?? (dirToDeg[dirStr] !== undefined ? dirToDeg[dirStr] : 45);
        const bearingAngle = Number(resolvedDeg);
        const towns = Array.isArray(spec.towns) && spec.towns.length >= 2 ? `${spec.towns[0]} → ${spec.towns[1]}` : null;
        const gpsPt = Array.isArray(spec.points) && spec.points[0] ? `${spec.points[0].name || 'Point'} (${spec.points[0].lat}°S, ${spec.points[0].long}°E)` : null;
        const destination = spec.destination || towns || gpsPt || spec.north_facing_wall || spec.target_dir || 'Target';

        return (
            <div data-testid="mathlit-diagram-compass" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title}
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center">
                    <svg viewBox="0 0 340 340" className="w-full max-w-[340px] h-auto font-sans">
                        <circle cx="170" cy="170" r="130" fill="#FAF8F3" stroke="#CBD5E1" strokeWidth="2" />
                        <circle cx="170" cy="170" r="100" fill="#FFFFFF" stroke="#94A3B8" strokeWidth="1" strokeDasharray="3,3" />

                        <polygon points="170,40 178,160 170,170 162,160" fill="#DC2626" />
                        <polygon points="170,300 178,180 170,170 162,180" fill="#1E2022" />
                        <polygon points="300,170 180,178 170,170 180,162" fill="#1E2022" />
                        <polygon points="40,170 160,178 170,170 160,162" fill="#1E2022" />

                        <text x="170" y="32" textAnchor="middle" fontSize="14" fontWeight="bold" fill="#DC2626">N (000° / 360°)</text>
                        <text x="315" y="175" textAnchor="start" fontSize="12" fontWeight="bold" fill="#1E2022">E (090°)</text>
                        <text x="170" y="325" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#1E2022">S (180°)</text>
                        <text x="25" y="175" textAnchor="end" fontSize="12" fontWeight="bold" fill="#1E2022">W (270°)</text>

                        <g transform={`rotate(${bearingAngle} 170 170)`}>
                            <line x1="170" y1="170" x2="170" y2="55" stroke="#2563EB" strokeWidth="3" strokeDasharray="4,2" />
                            <circle cx="170" cy="55" r="5" fill="#2563EB" />
                        </g>
                        <circle cx="170" cy="170" r="4" fill="#0F172A" />
                        <text x="170" y="198" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#2563EB">
                            {destination}: {String(bearingAngle).padStart(3, '0')}° {spec.target_dir ? `(${spec.target_dir})` : ''}
                        </text>
                    </svg>
                </div>
            </div>
        );
    }

    // 5a. ALPHANUMERIC STREET & TOPOGRAPHIC GRID MAP
    if (kind === 'grid_map') {
        const cols = Array.isArray(spec.columns) && spec.columns.length > 0 ? spec.columns : ['A', 'B', 'C', 'D', 'E'];
        const rows = Array.isArray(spec.rows) && spec.rows.length > 0 ? spec.rows : ['1', '2', '3', '4'];
        const landmarks = Array.isArray(spec.landmarks) ? spec.landmarks : [];
        if (spec.facility && spec.coordinate) {
            landmarks.push({ name: spec.facility, cell: spec.coordinate });
        }
        if (Array.isArray(spec.cells)) {
            spec.cells.forEach((c) => {
                const cCol = cols[(c.col || 1) - 1] || 'A';
                const cRow = rows[(c.row || 1) - 1] || '1';
                landmarks.push({ name: c.label || 'Point', cell: `${cCol}${cRow}` });
            });
        }

        const cellW = 76;
        const cellH = 44;
        const padL = 50;
        const padT = 36;
        const W = padL + cols.length * cellW + 30;
        const H = padT + rows.length * cellH + 35;

        return (
            <div data-testid="mathlit-diagram-grid-map" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title}
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs w-full flex justify-center overflow-x-auto">
                    <svg viewBox={`0 0 ${W} ${H}`} className="w-full max-w-[520px] h-auto font-sans">
                        {cols.map((colLbl, cIdx) => (
                            <text key={cIdx} x={padL + cIdx * cellW + cellW / 2} y={24} textAnchor="middle" fontSize="12" fontWeight="bold" fill="#1E2022">
                                {colLbl}
                            </text>
                        ))}
                        {rows.map((rowLbl, rIdx) => (
                            <g key={rIdx}>
                                <text x={28} y={padT + rIdx * cellH + cellH / 2 + 4} textAnchor="middle" fontSize="12" fontWeight="bold" fill="#1E2022">
                                    {rowLbl}
                                </text>
                                {cols.map((colLbl, cIdx) => {
                                    const coord = `${colLbl}${rowLbl}`;
                                    const lm = landmarks.find((l) => String(l.cell || l.coord || '').toUpperCase() === coord.toUpperCase()) || (rIdx === 0 && cIdx === 0 && landmarks[0] && !landmarks[0].cell ? landmarks[0] : null);
                                    const x = padL + cIdx * cellW;
                                    const y = padT + rIdx * cellH;
                                    return (
                                        <g key={cIdx}>
                                            <rect
                                                x={x}
                                                y={y}
                                                width={cellW}
                                                height={cellH}
                                                fill={lm ? '#EFF6FF' : '#FAF8F3'}
                                                stroke="#94A3B8"
                                                strokeWidth="1.5"
                                            />
                                            <text x={x + 6} y={y + 13} fontSize="9" fill="#64748B">{coord}</text>
                                            {lm && (
                                                <text x={x + cellW / 2} y={y + 28} textAnchor="middle" fontSize="9.5" fontWeight="bold" fill="#1D4ED8">
                                                    {String(lm.name || lm.label || coord).slice(0, 12)}
                                                </text>
                                            )}
                                        </g>
                                    );
                                })}
                            </g>
                        ))}
                    </svg>
                </div>
            </div>
        );
    }

    // 5b. ARCHITECTURAL ELEVATION VIEW & TOPOGRAPHIC PROFILE
    if (kind === 'elevation_view') {
        const sideLabel = spec.side || spec.view_name || 'Front Elevation';
        const elevLabel = spec.elevation || spec.label || sideLabel;
        const widthM = spec.width_m ?? spec.front_width_m ?? (spec.door_w_mm ? spec.door_w_mm / 1000 : 6.0);
        const heightM = spec.height_m ?? spec.total_height_m ?? spec.real_height_m ?? spec.wall_height_m ?? (spec.door_h_mm ? spec.door_h_mm / 1000 : 3.2);
        const roofHeightM = spec.roof_height_m ?? (typeof spec.roof === 'object' ? spec.roof?.rise_m : 1.2);
        const hasPitchedRoof = Boolean(spec.roof || spec.roof_type);
        const scaleStr = spec.scale_ratio || (Array.isArray(spec.layers) && spec.layers[0]?.scale) || '1 : 100';
        const featuresList = Array.isArray(spec.features) ? spec.features.join(' • ') : '';
        const extraDim = spec.overhang_mm
            ? `Overhang: ${spec.overhang_mm} mm`
            : spec.real_sill_mm
                ? `Sill Height: ${spec.real_sill_mm} mm`
                : spec.step_mm
                    ? `FFL Step: ${spec.step_mm} mm`
                    : spec.trench_cm
                        ? `Trench: ${spec.trench_cm} cm`
                        : typeof spec.dimensions === 'string'
                            ? spec.dimensions
                            : '';

        return (
            <div data-testid="mathlit-diagram-elevation" className="flex flex-col items-center w-full my-2">
                <div className="w-full flex items-center justify-between px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-t-xl text-xs font-semibold text-slate-700">
                    <span>{title} ({sideLabel})</span>
                    <span className="font-mono text-slate-500">Scale {scaleStr}</span>
                </div>
                <div className="w-full p-4 bg-white border-x border-b border-slate-200 rounded-b-xl flex flex-col items-center">
                    <svg viewBox="0 0 480 240" className="w-full max-w-[480px] h-auto font-sans">
                        {/* Ground / Natural Ground Level Line */}
                        <line x1="40" y1="195" x2="440" y2="195" stroke="#334155" strokeWidth="3" />
                        <text x="435" y="212" textAnchor="end" fontSize="10" fontWeight="bold" fill="#475569">NGL / Ground Level</text>

                        {/* Pitched Roof Gable */}
                        {hasPitchedRoof && (
                            <polygon points="95,95 240,35 385,95" fill="#E2E8F0" stroke="#1E2022" strokeWidth="2.5" />
                        )}

                        {/* Building Elevation Wall Facade */}
                        <rect x="110" y="95" width="260" height="100" fill="#FAF8F3" stroke="#1E2022" strokeWidth="2.5" />

                        {/* Door & Window Openings */}
                        <rect x="150" y="125" width="42" height="70" fill="#FFFFFF" stroke="#2563EB" strokeWidth="2" />
                        <rect x="235" y="120" width="55" height="40" fill="#E0F2FE" stroke="#0284C7" strokeWidth="1.8" />
                        <line x1="262.5" y1="120" x2="262.5" y2="160" stroke="#0284C7" strokeWidth="1.2" />

                        {/* Elevation Dimension Callouts */}
                        <line x1="405" y1={hasPitchedRoof ? 35 : 95} x2="405" y2="195" stroke="#2563EB" strokeWidth="1.8" />
                        <text x="415" y="135" fontSize="11" fontWeight="bold" fill="#1D4ED8">
                            Height: {heightM} m {roofHeightM && hasPitchedRoof ? `(Roof: ${roofHeightM} m)` : ''}
                        </text>

                        <text x="240" y="218" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0F172A">
                            Width: {widthM} m | {String(elevLabel)} {extraDim ? `| ${extraDim}` : ''}
                        </text>
                    </svg>
                    {featuresList && (
                        <div className="mt-1 text-xs font-medium text-slate-600 bg-slate-50 px-3 py-1 rounded border border-slate-200">
                            Features: {featuresList}
                        </div>
                    )}
                </div>
            </div>
        );
    }

    // 5c. STRIP MAP / HIGHWAY ROUTE
    if (kind === 'strip_map') {
        const stops = spec.stops || [
            { name: 'Johannesburg', km: 0 },
            { name: 'Kroonstad', km: 210 },
            { name: 'Bloemfontein', km: 398 },
            { name: 'Colesberg', km: 625 },
        ];
        return (
            <div data-testid="mathlit-diagram-strip-map" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title}
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs w-full overflow-x-auto">
                    <svg viewBox="0 0 520 120" className="w-full min-w-[500px] h-auto font-sans">
                        {/* Highway Ribbon */}
                        <line x1="40" y1="50" x2="480" y2="50" stroke="#334155" strokeWidth="8" strokeLinecap="round" />
                        <line x1="40" y1="50" x2="480" y2="50" stroke="#FBBF24" strokeWidth="1" strokeDasharray="6,6" />

                        {/* Town Stop Nodes */}
                        {stops.map((st, i) => {
                            const x = 50 + (i / Math.max(1, stops.length - 1)) * 420;
                            return (
                                <g key={i}>
                                    <circle cx={x} cy="50" r="8" fill="#FFFFFF" stroke="#0F172A" strokeWidth="3" />
                                    <circle cx={x} cy="50" r="3" fill="#2563EB" />
                                    <text x={x} y="32" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0F172A">
                                        {st.name}
                                    </text>
                                    <text x={x} y="78" textAnchor="middle" fontSize="10" fontStyle="italic" fill="#64748B">
                                        {st.km} km
                                    </text>
                                </g>
                            );
                        })}
                    </svg>
                </div>
            </div>
        );
    }

    // 6. CINEMA / AUDITORIUM SEATING PLAN
    if (kind === 'seating_plan') {
        const rows = Array.isArray(spec.rows) && spec.rows.length > 0 ? spec.rows : ['A', 'B', 'C', 'D', 'E'];
        const seatsPerRow = Number(spec.seats_per_row || 8);
        const displayCols = Math.min(10, Math.max(4, seatsPerRow));
        const targetSeat = spec.target_seat || spec.highlighted_seat || '';

        return (
            <div data-testid="mathlit-diagram-seating-plan" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title} {targetSeat ? `— Target: ${targetSeat}` : ''} ({seatsPerRow} seats/row)
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center">
                    <svg viewBox="0 0 480 230" className="w-full max-w-[480px] h-auto font-sans">
                        <rect x="80" y="15" width="320" height="12" rx="4" fill="#E2E8F0" stroke="#94A3B8" strokeWidth="1" />
                        <text x="240" y="24" textAnchor="middle" fontSize="9" fontWeight="bold" fill="#475569">
                            STAGE / PROJECTION SCREEN ({seatsPerRow} SEATS PER ROW)
                        </text>

                        {rows.slice(0, 6).map((rLabel, rIdx) => {
                            const y = 52 + rIdx * 28;
                            return (
                                <g key={rLabel}>
                                    <text x="35" y={y + 14} textAnchor="middle" fontSize="11" fontWeight="bold" fill="#64748B">
                                        Row {rLabel}
                                    </text>
                                    {Array.from({ length: displayCols }).map((_, cIdx) => {
                                        const seatNum = cIdx === displayCols - 1 && seatsPerRow > displayCols ? seatsPerRow : cIdx + 1;
                                        const isHighlighted = targetSeat && targetSeat.includes(`Row ${rLabel}`) && targetSeat.includes(String(seatNum));
                                        const x = 68 + cIdx * 36 + (cIdx >= Math.floor(displayCols / 2) ? 18 : 0);
                                        return (
                                            <g key={cIdx}>
                                                <rect
                                                    x={x}
                                                    y={y}
                                                    width="26"
                                                    height="20"
                                                    rx="3"
                                                    fill={isHighlighted ? '#DBEAFE' : '#F8FAFC'}
                                                    stroke={isHighlighted ? '#2563EB' : '#64748B'}
                                                    strokeWidth={isHighlighted ? '2' : '1.5'}
                                                />
                                                <text x={x + 13} y={y + 14} textAnchor="middle" fontSize="9" fontWeight="bold" fill={isHighlighted ? '#1D4ED8' : '#334155'}>
                                                    {seatNum}
                                                </text>
                                            </g>
                                        );
                                    })}
                                </g>
                            );
                        })}
                    </svg>
                </div>
            </div>
        );
    }

    // 7. PACKAGING & CARTON PACKING LAYOUT
    if (kind === 'packaging_packing' || kind === 'packaging_cartons') {
        const layout = spec.layout || 'standard';
        const cartonL = spec.carton_l || (spec.container?.length) || 60;
        const cartonW = spec.carton_w || (spec.container?.width) || 40;
        const cartonH = spec.carton_h || (spec.container?.height) || 30;
        const boxL = spec.box_l || (spec.box?.length) || 15;
        const boxW = spec.box_w || (spec.box?.width) || 10;
        const boxH = spec.box_h || (spec.box?.height) || 10;

        const countL = Math.max(1, Math.floor(cartonL / boxL));
        const countW = Math.max(1, Math.floor(cartonW / boxW));
        const countH = Math.max(1, Math.floor(cartonH / boxH));
        const total = countL * countW * countH;

        return (
            <div data-testid="mathlit-diagram-packaging" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title} {layout !== 'standard' ? `(${layout} layout)` : ''}
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center">
                    <svg viewBox="0 0 460 220" className="w-full max-w-[460px] h-auto font-sans">
                        {/* Outer Shipping Carton 3D Isometric View */}
                        <polygon points="80,140 220,180 380,130 240,90" fill="#E2E8F0" stroke="#475569" strokeWidth="2" />
                        <polygon points="80,140 80,60 240,20 240,90" fill="#CBD5E1" stroke="#475569" strokeWidth="2" />
                        <polygon points="240,90 240,20 380,60 380,130" fill="#94A3B8" stroke="#475569" strokeWidth="2" />

                        {/* Packed Inner Boxes Grid Representation */}
                        <line x1="150" y1="160" x2="310" y2="110" stroke="#2563EB" strokeWidth="1.5" strokeDasharray="3,2" />
                        <line x1="160" y1="75" x2="160" y2="145" stroke="#2563EB" strokeWidth="1.5" strokeDasharray="3,2" />

                        {/* Dimensions Annotation */}
                        <text x="140" y="185" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0F172A">
                            Length: {cartonL} cm ({countL} boxes)
                        </text>
                        <text x="320" y="165" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0F172A">
                            Width: {cartonW} cm ({countW} boxes)
                        </text>
                        <text x="60" y="100" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#0F172A">
                            Height: {cartonH} cm ({countH} layers)
                        </text>
                    </svg>
                    <div className="mt-2 text-xs font-mono font-bold text-emerald-800 bg-emerald-50 px-3 py-1 rounded-lg border border-emerald-200">
                        Packing Capacity: {countL} × {countW} × {countH} = {total} individual boxes fit inside carton
                    </div>
                </div>
            </div>
        );
    }

    // 8. 2D / 3D MENSURATION PARAMETERIZED SHAPES (RECTANGLES, CYLINDERS, TRIANGLES)
    if (kind === 'mensuration_2d' || kind === 'mensuration_3d' || kind === '2d_polygon') {
        const shape = (spec.shape || 'rectangle').toLowerCase();
        const nestedDims = typeof spec.dimensions === 'object' && spec.dimensions !== null ? spec.dimensions : {};
        const dimL = spec.length ?? spec.dim_l ?? nestedDims.length ?? nestedDims.base ?? 12;
        const dimW = spec.width ?? spec.dim_w ?? nestedDims.width ?? nestedDims.depth ?? spec.height ?? 8;
        const dimR = spec.radius ?? spec.dim_r ?? nestedDims.radius ?? (nestedDims.diameter ? nestedDims.diameter / 2 : 5);
        const dimH = spec.height ?? spec.dim_h ?? nestedDims.height ?? nestedDims.depth ?? 10;
        const areaM2 = spec.area_m2 ?? nestedDims.area_m2;
        const volCm3 = spec.volume_cm3 ?? nestedDims.volume_cm3;
        const scaleInfo = spec.scale ? `Scale ${spec.scale}` : '';
        const ratioInfo = spec.area_ratio ? `Area Ratio ${spec.area_ratio}` : (spec.volume_ratio ? `Volume Ratio ${spec.volume_ratio}` : '');
        const customLblW = spec.labels?.width;
        const customLblReal = spec.labels?.real;
        const unit = spec.unit || 'm';

        const topCallout = customLblW
            ? `${customLblW} (${customLblReal || ''})`
            : areaM2
                ? `Surface Area = ${areaM2} m²`
                : volCm3
                    ? `Volume = ${volCm3} cm³`
                    : (scaleInfo || ratioInfo) && !spec.length && !nestedDims.length
                        ? `${scaleInfo} ${ratioInfo}`.trim()
                        : `Length = ${dimL} ${unit}`;

        const sideCallout = nestedDims.coats
            ? `Coats = ${nestedDims.coats}`
            : ratioInfo && (spec.length || nestedDims.length)
                ? ratioInfo
                : `Width = ${dimW} ${unit}`;

        return (
            <div data-testid="mathlit-diagram-mensuration" className="flex flex-col items-center w-full my-2">
                <div className="w-full text-center text-xs font-bold text-slate-700 uppercase tracking-wider mb-2">
                    {title} {scaleInfo ? `(${scaleInfo})` : ''}
                </div>
                <div className="p-4 bg-white rounded-xl border border-slate-200 shadow-2xs flex flex-col items-center">
                    <svg viewBox="0 0 380 200" className="w-full max-w-[380px] h-auto font-sans">
                        {shape === 'circle' ? (
                            <g>
                                <circle cx="190" cy="100" r="70" fill="#FAF8F3" stroke="#1E2022" strokeWidth="2.5" />
                                <line x1="190" y1="100" x2="260" y2="100" stroke="#2563EB" strokeWidth="2" />
                                <circle cx="190" cy="100" r="3" fill="#2563EB" />
                                <text x="225" y="90" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#2563EB">
                                    r = {dimR} {unit}
                                </text>
                            </g>
                        ) : shape.includes('cylinder') || shape.includes('tank') ? (
                            <g>
                                <ellipse cx="190" cy="50" rx="70" ry="22" fill="#FAF8F3" stroke="#1E2022" strokeWidth="2" />
                                <line x1="120" y1="50" x2="120" y2="145" stroke="#1E2022" strokeWidth="2" />
                                <line x1="260" y1="50" x2="260" y2="145" stroke="#1E2022" strokeWidth="2" />
                                <ellipse cx="190" cy="145" rx="70" ry="22" fill="#FAF8F3" stroke="#1E2022" strokeWidth="2" />
                                <line x1="190" y1="50" x2="260" y2="50" stroke="#2563EB" strokeWidth="2" />
                                <text x="225" y="42" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#2563EB">
                                    {scaleInfo || `r = ${dimR} ${unit}`}
                                </text>
                                <line x1="275" y1="50" x2="275" y2="145" stroke="#94A3B8" strokeWidth="1.5" />
                                <text x="322" y="102" textAnchor="middle" fontSize="11" fontWeight="bold" fill="#475569">
                                    {ratioInfo || `h = ${dimH} ${unit}`}
                                </text>
                            </g>
                        ) : (
                            <g>
                                <rect x="90" y="45" width="200" height="110" fill="#FAF8F3" stroke="#1E2022" strokeWidth="2.5" />
                                <text x="190" y="32" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#1E2022">
                                    {topCallout}
                                </text>
                                <text x="65" y="105" textAnchor="middle" fontSize="12" fontWeight="bold" fill="#1E2022" transform="rotate(-90 65 105)">
                                    {sideCallout}
                                </text>
                            </g>
                        )}
                    </svg>
                </div>
            </div>
        );
    }

    // 9. FIRST-QUADRANT CARTESIAN SYSTEM (BREAK-EVEN, TARIFFS, COST CURVES, UIF)
    if (kind === 'cartesian_system') {
        const lines = Array.isArray(spec.lines) ? spec.lines : [];
        const pois = Array.isArray(spec.points_of_interest) ? spec.points_of_interest : [];
        const xRange = spec.x_range || [0, 100];
        const yRange = spec.y_range || [0, 100];
        const xMin = Number(xRange[0] ?? 0);
        const xMax = Number(xRange[1] ?? 100);
        const yMin = Number(yRange[0] ?? 0);
        const yMax = Number(yRange[1] ?? 100);
        const xLabel = spec.x_label || spec.x_axis_label || 'Units / Quantity';
        const yLabel = spec.y_label || spec.y_axis_label || 'Amount (R)';

        const W = 560;
        const H = 320;
        const padL = 65;
        const padR = 40;
        const padT = 30;
        const padB = 45;
        const plotW = W - padL - padR;
        const plotH = H - padT - padB;

        const sx = (x) => padL + ((x - xMin) / Math.max(1e-5, xMax - xMin)) * plotW;
        const sy = (y) => padT + plotH - ((y - yMin) / Math.max(1e-5, yMax - yMin)) * plotH;

        const palette = ['#2563EB', '#DC2626', '#16A34A', '#9333EA', '#D97706'];

        return (
            <div data-testid="mathlit-diagram-cartesian" className="flex flex-col items-center w-full my-2">
                <div className="w-full flex items-center justify-between px-3 py-1.5 bg-slate-50 border border-slate-200 rounded-t-xl text-xs font-semibold text-slate-700">
                    <span>{title}</span>
                    <span className="font-mono text-slate-500">{xLabel} vs {yLabel}</span>
                </div>
                <div className="w-full p-4 bg-white border-x border-b border-slate-200 rounded-b-xl flex justify-center overflow-x-auto">
                    <svg viewBox={`0 0 ${W} ${H}`} className="w-full max-w-[560px] h-auto font-sans">
                        {/* Axes */}
                        <line x1={padL} y1={padT + plotH} x2={W - padR + 15} y2={padT + plotH} stroke="#1E2022" strokeWidth="2" />
                        <line x1={padL} y1={padT - 10} x2={padL} y2={padT + plotH} stroke="#1E2022" strokeWidth="2" />
                        {/* Axis Labels */}
                        <text x={W - padR} y={padT + plotH + 32} textAnchor="end" fontSize="11" fontWeight="bold" fill="#334155">
                            {xLabel}
                        </text>
                        <text x={padL - 10} y={padT - 5} textAnchor="start" fontSize="11" fontWeight="bold" fill="#334155">
                            {yLabel}
                        </text>

                        {/* Axis Range Ticks */}
                        <text x={padL} y={padT + plotH + 16} textAnchor="middle" fontSize="10" fill="#64748B">{xMin}</text>
                        <text x={padL + plotW} y={padT + plotH + 16} textAnchor="middle" fontSize="10" fill="#64748B">{xMax.toLocaleString('en-ZA')}</text>
                        <text x={padL - 8} y={padT + plotH} textAnchor="end" fontSize="10" fill="#64748B">{yMin}</text>
                        <text x={padL - 8} y={padT + 4} textAnchor="end" fontSize="10" fill="#64748B">{yMax.toLocaleString('en-ZA')}</text>

                        {/* Plotted Series Lines */}
                        {lines.map((ln, idx) => {
                            const pts = Array.isArray(ln.points) ? ln.points : [];
                            if (pts.length < 2) return null;
                            const pathStr = pts.map((p, i) => `${i === 0 ? 'M' : 'L'} ${sx(p[0])} ${sy(p[1])}`).join(' ');
                            const col = ln.color || palette[idx % palette.length];
                            const lastPt = pts[pts.length - 1];
                            return (
                                <g key={idx}>
                                    <path d={pathStr} fill="none" stroke={col} strokeWidth="2.5" strokeDasharray={ln.dashed ? '4,3' : 'none'} />
                                    {ln.label && lastPt && (
                                        <text x={sx(lastPt[0]) + 4} y={sy(lastPt[1]) - 4} fontSize="11" fontWeight="bold" fill={col}>
                                            {ln.label}
                                        </text>
                                    )}
                                </g>
                            );
                        })}

                        {/* Points of Interest */}
                        {pois.map((poi, idx) => {
                            const px = sx(poi.x);
                            const py = sy(poi.y);
                            return (
                                <g key={idx}>
                                    <line x1={px} y1={py} x2={px} y2={padT + plotH} stroke="#94A3B8" strokeWidth="1" strokeDasharray="3,3" />
                                    <line x1={padL} y1={py} x2={px} y2={py} stroke="#94A3B8" strokeWidth="1" strokeDasharray="3,3" />
                                    <circle cx={px} cy={py} r="5" fill="#DC2626" stroke="#FFFFFF" strokeWidth="1.5" />
                                    {poi.label && (
                                        <text x={px + 8} y={py - 6} fontSize="11" fontWeight="bold" fill="#0F172A">
                                            {poi.label} ({poi.x}; {poi.y})
                                        </text>
                                    )}
                                </g>
                            );
                        })}
                    </svg>
                </div>
            </div>
        );
    }

    // Default fallback: return null
    return null;
}

export default MathLitDiagramRenderer;
