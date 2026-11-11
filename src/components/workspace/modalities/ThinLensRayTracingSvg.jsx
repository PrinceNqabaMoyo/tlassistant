import React from 'react';

/**
 * Authentic Thin Lens Ray Tracing Diagram Component.
 * Aligned with South African Physical Sciences Grade 11 Paper 1/2 (Geometrical Optics Term 2).
 * Constructs geometric principal rays for converging (biconvex) and diverging (biconcave) thin lenses:
 * 1. Ray 1 (Red): Incident parallel to principal axis -> refracts through principal focus F2.
 * 2. Ray 2 (Blue): Incident through optical centre O -> passes undeviated.
 * 3. Ray 3 (Emerald): Incident through principal focus F1 -> refracts parallel to principal axis.
 */
export default function ThinLensRayTracingSvg({
  lens_type = 'converging',
  focal_length_cm = 10,
  object_distance_cm = 25,
  object_height_cm = 4,
  image_distance_cm = 16.7,
  image_height_cm = -2.7,
  magnification = -0.67,
  image_nature = 'Real, inverted, and diminished',
  activeRay,
  onSelectRay,
}) {
  const isDiverging = String(lens_type).toLowerCase().includes('diverg');

  // SVG Geometry constants (500x300 viewBox)
  const cx = 250;
  const cy = 150;

  // Scale factor: 1 cm -> 5.5 SVG pixels (bounded for canvas fit)
  const pxPerCm = 5.5;
  const f_px = Math.max(35, Math.min(100, Math.abs(Number(focal_length_cm) || 10) * pxPerCm));
  const do_px = Math.max(45, Math.min(190, Math.abs(Number(object_distance_cm) || 25) * pxPerCm));
  const ho_px = Math.max(25, Math.min(65, Math.abs(Number(object_height_cm) || 4) * 8));

  // Compute image geometry
  const di_val = Number(image_distance_cm) || 16.7;
  const isReal = di_val > 0;
  const di_px = Math.max(30, Math.min(190, Math.abs(di_val) * pxPerCm));
  const hi_px = Math.max(15, Math.min(75, Math.abs(Number(image_height_cm) || 2.7) * 8));

  // Coordinates
  const obj_x = cx - do_px;
  const obj_top_y = cy - ho_px;

  // Image coordinates: real images form to the right (cx + di_px) inverted below axis (cy + hi_px)
  // Virtual images form on the left (cx - di_px) upright above axis (cy - hi_px)
  const img_x = isReal ? cx + di_px : cx - di_px;
  const img_tip_y = isReal ? cy + hi_px : cy - hi_px;

  // Focal points coordinates
  const f1_x = cx - f_px;
  const f2_x = cx + f_px;
  const two_f1_x = cx - 2 * f_px;
  const two_f2_x = cx + 2 * f_px;

  return (
    <svg
      viewBox="0 0 500 300"
      data-testid="thin-lens-canvas"
      className="w-full max-w-[500px] h-auto select-none"
      style={{ minWidth: '320px' }}
    >
      <defs>
        {/* Ray 1 Arrowhead (Red) */}
        <marker id="ray1-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#dc2626" />
        </marker>

        {/* Ray 2 Arrowhead (Blue) */}
        <marker id="ray2-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
        </marker>

        {/* Ray 3 Arrowhead (Emerald) */}
        <marker id="ray3-arrow" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
        </marker>

        {/* Object Arrow Head (Amber) */}
        <marker id="obj-head" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
        </marker>

        {/* Image Arrow Head (Indigo) */}
        <marker id="img-head" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
          <path d="M 0 1 L 10 5 L 0 9 z" fill="#4f46e5" />
        </marker>

        {/* Lens subtle glass fill */}
        <linearGradient id="lensGlass" x1="0%" y1="0%" x2="100%" y2="0%">
          <stop offset="0%" stopColor="#bae6fd" stopOpacity="0.4" />
          <stop offset="50%" stopColor="#ffffff" stopOpacity="0.7" />
          <stop offset="100%" stopColor="#bae6fd" stopOpacity="0.4" />
        </linearGradient>
      </defs>

      {/* ── BACKGROUND GRID ── */}
      <rect x="10" y="10" width="480" height="280" rx="8" fill="#f8fafc" stroke="#e2e8f0" strokeWidth="1" />

      {/* ── PRINCIPAL AXIS (Horizontal Line) ── */}
      <line x1="20" y1={cy} x2="480" y2={cy} stroke="#64748b" strokeWidth="1.6" />
      <text x="475" y={cy - 6} fontSize="9" fill="#64748b" fontWeight="bold" textAnchor="end" fontFamily="sans-serif">
        Principal Axis
      </text>

      {/* ── FOCAL POINTS & 2F MARKS ── */}
      {/* Primary Focus F1 (Left) */}
      <circle cx={f1_x} cy={cy} r="3" fill="#0284c7" />
      <text x={f1_x} y={cy + 14} fontSize="9" fill="#0369a1" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
        F₁
      </text>
      {/* 2F1 (Left) */}
      {two_f1_x > 25 && (
        <>
          <circle cx={two_f1_x} cy={cy} r="2.5" fill="#64748b" />
          <text x={two_f1_x} y={cy + 14} fontSize="8" fill="#64748b" textAnchor="middle" fontFamily="sans-serif">
            2F₁
          </text>
        </>
      )}

      {/* Secondary Focus F2 (Right) */}
      <circle cx={f2_x} cy={cy} r="3" fill="#0284c7" />
      <text x={f2_x} y={cy + 14} fontSize="9" fill="#0369a1" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
        F₂
      </text>
      {/* 2F2 (Right) */}
      {two_f2_x < 475 && (
        <>
          <circle cx={two_f2_x} cy={cy} r="2.5" fill="#64748b" />
          <text x={two_f2_x} y={cy + 14} fontSize="8" fill="#64748b" textAnchor="middle" fontFamily="sans-serif">
            2F₂
          </text>
        </>
      )}

      {/* Optical Centre O */}
      <circle cx={cx} cy={cy} r="3" fill="#0f172a" />
      <text x={cx + 6} y={cy + 13} fontSize="9" fill="#0f172a" fontWeight="bold" fontFamily="sans-serif">
        O
      </text>

      {/* ── THIN LENS APERTURE LINE ── */}
      <line x1={cx} y1="25" x2={cx} y2="275" stroke="#0284c7" strokeWidth="2.5" />
      {/* Converging Double Arrow Ends (pointing outwards) */}
      {!isDiverging ? (
        <>
          {/* Top double arrow */}
          <polygon points={`${cx},20 ${cx - 6},32 ${cx + 6},32`} fill="#0284c7" />
          {/* Bottom double arrow */}
          <polygon points={`${cx},280 ${cx - 6},268 ${cx + 6},268`} fill="#0284c7" />
          {/* Curved convex glass silhouette */}
          <path d={`M ${cx},25 Q ${cx + 12},${cy} ${cx},275 Q ${cx - 12},${cy} ${cx},25`} fill="url(#lensGlass)" stroke="#38bdf8" strokeWidth="0.8" opacity="0.6" />
        </>
      ) : (
        <>
          {/* Diverging inverted arrow ends */}
          <polygon points={`${cx},32 ${cx - 6},20 ${cx + 6},20`} fill="#0284c7" />
          <polygon points={`${cx},268 ${cx - 6},280 ${cx + 6},280`} fill="#0284c7" />
          <path d={`M ${cx},25 Q ${cx - 10},${cy} ${cx},275 L ${cx},275 Q ${cx + 10},${cy} ${cx},25 Z`} fill="url(#lensGlass)" stroke="#38bdf8" strokeWidth="0.8" opacity="0.6" />
        </>
      )}
      <text x={cx} y="18" fontSize="8.5" fill="#0369a1" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
        {isDiverging ? 'DIVERGING (CONCAVE)' : 'CONVERGING (CONVEX)'} LENS
      </text>

      {/* ── OBJECT ARROW ── */}
      <g id="lens-object" data-testid="lens-object">
        <line x1={obj_x} y1={cy} x2={obj_x} y2={obj_top_y} stroke="#d97706" strokeWidth="3" markerEnd="url(#obj-head)" />
        <text x={obj_x} y={obj_top_y - 8} fontSize="9" fill="#b45309" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
          Object
        </text>
        <text x={obj_x} y={cy - 4} fontSize="7" fill="#d97706" textAnchor="middle" fontFamily="sans-serif">
          do = {object_distance_cm} cm
        </text>
      </g>

      {/* ── PRINCIPAL RAYS ── */}
      <g id="principal-rays">
        {/* ── RAY 1 (RED): Parallel to axis -> refracts through F2 ── */}
        <g id="ray-1" opacity={activeRay && activeRay !== 'ray1' ? 0.25 : 1} className="transition-opacity">
          {/* Incident ray: from top of object parallel to lens */}
          <line
            x1={obj_x}
            y1={obj_top_y}
            x2={cx}
            y2={obj_top_y}
            stroke="#dc2626"
            strokeWidth="1.8"
            markerMid="url(#ray1-arrow)"
          />
          {/* Direction arrow on incident ray */}
          <line x1={obj_x} y1={obj_top_y} x2={(obj_x + cx) / 2 + 5} y2={obj_top_y} stroke="#dc2626" strokeWidth="1.8" markerEnd="url(#ray1-arrow)" />

          {/* Refracted ray: through F2 to image tip */}
          {!isDiverging ? (
            <line
              x1={cx}
              y1={obj_top_y}
              x2={img_x + 30}
              y2={obj_top_y + ((img_tip_y - obj_top_y) / (img_x - cx)) * (img_x + 30 - cx)}
              stroke="#dc2626"
              strokeWidth="1.8"
            />
          ) : (
            <>
              {/* Diverging ray travels up away from F1 */}
              <line x1={cx} y1={obj_top_y} x2={cx + 80} y2={obj_top_y - 30} stroke="#dc2626" strokeWidth="1.8" />
              {/* Virtual extension backwards to F1 */}
              <line x1={f1_x} y1={cy} x2={cx} y2={obj_top_y} stroke="#dc2626" strokeWidth="1.2" strokeDasharray="3 2" />
            </>
          )}
        </g>

        {/* ── RAY 2 (BLUE): Through Optical Center O without deviation ── */}
        <g id="ray-2" opacity={activeRay && activeRay !== 'ray2' ? 0.25 : 1} className="transition-opacity">
          <line
            x1={obj_x}
            y1={obj_top_y}
            x2={isReal ? img_x + 25 : cx + 60}
            y2={isReal ? img_tip_y + ((img_tip_y - cy) / (img_x - cx)) * 25 : cy + ((cy - obj_top_y) / (cx - obj_x)) * 60}
            stroke="#2563eb"
            strokeWidth="1.8"
          />
          {/* Mid arrow */}
          <line x1={obj_x} y1={obj_top_y} x2={(obj_x + cx) / 2 + 5} y2={(obj_top_y + cy) / 2} stroke="#2563eb" strokeWidth="1.8" markerEnd="url(#ray2-arrow)" />
        </g>

        {/* ── RAY 3 (EMERALD): Through F1 -> refracts parallel to axis ── */}
        {!isDiverging && (
          <g id="ray-3" opacity={activeRay && activeRay !== 'ray3' ? 0.25 : 1} className="transition-opacity">
            {/* Slope from top of object through F1 */}
            {(() => {
              const slope = (cy - obj_top_y) / (f1_x - obj_x);
              const lens_hit_y = obj_top_y + slope * (cx - obj_x);
              return (
                <>
                  {/* Incident segment through F1 to lens */}
                  <line x1={obj_x} y1={obj_top_y} x2={cx} y2={lens_hit_y} stroke="#059669" strokeWidth="1.6" />
                  <line x1={obj_x} y1={obj_top_y} x2={(obj_x + cx) / 2} y2={(obj_top_y + lens_hit_y) / 2} stroke="#059669" strokeWidth="1.6" markerEnd="url(#ray3-arrow)" />
                  {/* Refracted segment parallel to principal axis */}
                  <line x1={cx} y1={lens_hit_y} x2={img_x + 30} y2={lens_hit_y} stroke="#059669" strokeWidth="1.6" />
                </>
              );
            })()}
          </g>
        )}
      </g>

      {/* ── IMAGE ARROW ── */}
      <g id="lens-image" data-testid="lens-image">
        {isReal ? (
          <>
            {/* Real inverted image arrow pointing down */}
            <line x1={img_x} y1={cy} x2={img_x} y2={img_tip_y} stroke="#4f46e5" strokeWidth="3" markerEnd="url(#img-head)" />
            <text x={img_x} y={img_tip_y + 12} fontSize="9" fill="#4338ca" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
              Image
            </text>
            <text x={img_x} y={cy - 4} fontSize="7" fill="#6366f1" textAnchor="middle" fontFamily="sans-serif">
              di = {image_distance_cm} cm
            </text>
          </>
        ) : (
          <>
            {/* Virtual upright image arrow (dashed) */}
            <line x1={img_x} y1={cy} x2={img_x} y2={img_tip_y} stroke="#4f46e5" strokeWidth="2.5" strokeDasharray="3 2" markerEnd="url(#img-head)" />
            <text x={img_x} y={img_tip_y - 8} fontSize="9" fill="#4338ca" fontWeight="bold" textAnchor="middle" fontFamily="sans-serif">
              Virtual Image
            </text>
          </>
        )}
      </g>

      {/* ── DESCRIPTIVE OPTICS SPEC LEGEND ── */}
      <g id="optics-spec-legend">
        {/* Object & Focal Length Box */}
        <rect x="25" y="248" width="160" height="34" rx="4" fill="#ffffff" stroke="#cbd5e1" strokeWidth="1" />
        <text x="32" y="260" fontSize="7.5" fill="#475569" fontWeight="bold" fontFamily="sans-serif">
          f = {focal_length_cm} cm | do = {object_distance_cm} cm
        </text>
        <text x="32" y="274" fontSize="7.5" fill="#b45309" fontWeight="bold" fontFamily="sans-serif">
          Object Height ho = {object_height_cm} cm
        </text>

        {/* Image Nature Box */}
        <rect x="295" y="248" width="180" height="34" rx="4" fill="#eef2ff" stroke="#c7d2fe" strokeWidth="1" />
        <text x="302" y="260" fontSize="7.5" fill="#3730a3" fontWeight="bold" fontFamily="sans-serif">
          di = {image_distance_cm} cm | m = {magnification}
        </text>
        <text x="302" y="274" fontSize="7" fill="#4f46e5" fontWeight="bold" fontFamily="sans-serif">
          Nature: {image_nature}
        </text>
      </g>
    </svg>
  );
}
