import React, { useState } from 'react';
import MathText from '../shared/mathx/MathText';
import MathAnswerArea from '../shared/mathx/MathAnswerArea';
import { Compass, Eye, Info, Sparkles, CheckCircle } from 'lucide-react';
import ThinLensRayTracingSvg from './ThinLensRayTracingSvg';

/**
 * Procedurally Generated Geometrical Optics Ray Diagram Renderer.
 * Aligned with South African Physical Sciences Grade 11 Term 2 Standards.
 * Dynamically handles two major optical paradigms:
 * 1. Interface Refraction & Snell's Law / Total Internal Reflection
 * 2. Thin Lens Ray Tracing (Converging Convex / Diverging Concave)
 */
export default function OpticsRayModalityRenderer({
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

  const [activeChip, setActiveChip] = useState(null);

  const spec = question.optics_spec || {
    medium_1: { name: 'Air', refractive_index: 1.0 },
    medium_2: { name: 'Crown Glass', refractive_index: 1.52 },
    angle_incidence_deg: 30,
    angle_refraction_deg: 19.2,
    critical_angle_deg: 41.1,
    is_tir: false,
    normal_line: true,
    boundary_label: 'Air / Glass Interface',
  };

  const isThinLens = spec.type === 'thin_lens' || Boolean(spec.lens_type);

  // Interface Refraction parameters
  const theta1 = Number(spec.angle_incidence_deg || 30);
  const theta2 = Number(spec.angle_refraction_deg || 19.2);
  const thetac = Number(spec.critical_angle_deg || 41.1);

  // SVG Geometry Constants for interface refraction
  const cx = 250;
  const cy = 150;
  const rayLength = 115;

  const rad1 = (theta1 * Math.PI) / 180;
  const rad2 = (theta2 * Math.PI) / 180;

  const x1 = cx - rayLength * Math.sin(rad1);
  const y1 = cy - rayLength * Math.cos(rad1);
  const x2 = cx + rayLength * Math.sin(rad2);
  const y2 = cy + rayLength * Math.cos(rad2);

  const arcRadius = 45;
  const arc1_x = cx - arcRadius * Math.sin(rad1);
  const arc1_y = cy - arcRadius * Math.cos(rad1);
  const arc2_x = cx + arcRadius * Math.sin(rad2);
  const arc2_y = cy + arcRadius * Math.cos(rad2);

  return (
    <div className="space-y-6">
      {/* Canvas Card */}
      {!hideStimulusDiagram && (
      <div
        data-testid="optics-ray-canvas"
        className="p-4 sm:p-5 bg-white rounded-2xl border border-slate-200 shadow-2xs space-y-4 font-sans"
      >
        {/* Header Ribbon */}
        <div className="flex items-center justify-between border-b border-slate-100 pb-2">
          <div className="flex items-center gap-2">
            <span className="w-6 h-6 rounded-lg bg-indigo-600 text-white flex items-center justify-center text-xs font-bold shadow-2xs">
              <Compass className="w-3.5 h-3.5" />
            </span>
            <span className="text-xs font-bold text-slate-800 uppercase tracking-wide">
              {isThinLens
                ? `Geometrical Optics • Thin Lens Ray Tracing (${spec.lens_type || 'Converging'})`
                : "Geometrical Optics • Refraction Ray Diagram (Snell's Law)"}
            </span>
          </div>
          {isThinLens ? (
            <span className="text-[11px] font-mono text-indigo-700 font-semibold bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded">
              f = {spec.focal_length_cm} cm | do = {spec.object_distance_cm} cm → di = {spec.image_distance_cm} cm
            </span>
          ) : (
            <span className="text-[11px] font-mono text-indigo-700 font-semibold bg-indigo-50 border border-indigo-200 px-2 py-0.5 rounded">
              θ₁ = {theta1}° → θ₂ = {theta2}°
            </span>
          )}
        </div>

        {/* Dynamic Ray Diagram Canvas */}
        <div className="flex justify-center items-center bg-slate-50/50 p-3 sm:p-5 rounded-xl border border-slate-100 overflow-x-auto">
          {isThinLens ? (
            <ThinLensRayTracingSvg
              lens_type={spec.lens_type}
              focal_length_cm={spec.focal_length_cm}
              object_distance_cm={spec.object_distance_cm}
              object_height_cm={spec.object_height_cm}
              image_distance_cm={spec.image_distance_cm}
              image_height_cm={spec.image_height_cm}
              magnification={spec.magnification}
              image_nature={spec.image_nature}
              activeRay={activeChip}
              onSelectRay={(r) => setActiveChip(r)}
            />
          ) : (
            <svg viewBox="0 0 500 300" className="w-full max-w-[500px] h-auto select-none" style={{ minWidth: '320px' }}>
              <defs>
                <marker
                  id="arrow-incident"
                  viewBox="0 0 10 10"
                  refX="6"
                  refY="5"
                  markerWidth="6"
                  markerHeight="6"
                  orient="auto-start-reverse"
                >
                  <path d="M 0 1 L 10 5 L 0 9 z" fill="#e11d48" />
                </marker>

                <marker
                  id="arrow-refracted"
                  viewBox="0 0 10 10"
                  refX="6"
                  refY="5"
                  markerWidth="6"
                  markerHeight="6"
                  orient="auto-start-reverse"
                >
                  <path d="M 0 1 L 10 5 L 0 9 z" fill="#2563eb" />
                </marker>

                <linearGradient id="medium2Grad" x1="0%" y1="0%" x2="0%" y2="100%">
                  <stop offset="0%" stopColor="#e0f2fe" stopOpacity="0.7" />
                  <stop offset="100%" stopColor="#bae6fd" stopOpacity="0.9" />
                </linearGradient>
              </defs>

              {/* Upper Medium 1 (Optically Less Dense: Air) */}
              <rect x="10" y="10" width="480" height="140" fill="#f8fafc" stroke="#e2e8f0" strokeWidth="1" rx="8" />
              <text x="30" y="40" fontSize="12" fill="#475569" fontWeight="bold" fontFamily="sans-serif">
                Medium 1: {spec.medium_1?.name || 'Air'} (n₁ = {spec.medium_1?.refractive_index?.toFixed(2) || '1.00'})
              </text>
              <text x="30" y="56" fontSize="10" fill="#94a3b8" fontFamily="sans-serif">
                Optically Less Dense (v₁ = c = 3.00 × 10⁸ m/s)
              </text>

              {/* Lower Medium 2 (Optically Denser Material) */}
              <rect x="10" y="150" width="480" height="140" fill="url(#medium2Grad)" stroke="#7dd3fc" strokeWidth="1" rx="8" />
              <text x="30" y="180" fontSize="12" fill="#0369a1" fontWeight="bold" fontFamily="sans-serif">
                Medium 2: {spec.medium_2?.name || 'Denser Medium'} (n₂ = {spec.medium_2?.refractive_index?.toFixed(2) || '1.50'})
              </text>
              <text x="30" y="196" fontSize="10" fill="#0284c7" fontFamily="sans-serif">
                Optically Denser Material (Bends TOWARDS the Normal)
              </text>

              {/* Boundary Interface Line */}
              <line x1="10" y1="150" x2="490" y2="150" stroke="#0284c7" strokeWidth="2.5" />
              <text x="475" y="142" fontSize="9" fill="#0369a1" fontWeight="bold" textAnchor="end" fontFamily="sans-serif">
                Boundary Surface
              </text>

              {/* Normal Line (Perpendicular to boundary at cx, cy) */}
              <line
                data-testid="optics-normal-line"
                x1={cx}
                y1="25"
                x2={cx}
                y2="275"
                stroke="#64748b"
                strokeWidth="1.5"
                strokeDasharray="5 4"
              />
              <text x={cx + 8} y="38" fontSize="10" fill="#475569" fontWeight="bold" fontFamily="sans-serif">
                Normal (N)
              </text>

              {/* Right Angle Indicator at origin */}
              <path
                d={`M ${cx - 12} 150 L ${cx - 12} 138 L ${cx} 138`}
                fill="none"
                stroke="#94a3b8"
                strokeWidth="1"
              />

              {/* Angle of Incidence Arc (θ₁) */}
              <path
                d={`M ${cx} ${cy - arcRadius} A ${arcRadius} ${arcRadius} 0 0 0 ${arc1_x} ${arc1_y}`}
                fill="none"
                stroke="#e11d48"
                strokeWidth="2"
              />
              <text
                data-testid="optics-label-theta1"
                x={cx - 24}
                y={cy - 20}
                fontSize="11"
                fill="#be123c"
                fontWeight="bold"
                fontFamily="sans-serif"
              >
                θ₁ = {theta1}°
              </text>

              {/* Incident Ray (Crimson Red with arrow) */}
              <line
                data-testid="optics-ray-incident"
                x1={x1}
                y1={y1}
                x2={cx}
                y2={cy}
                stroke="#e11d48"
                strokeWidth="3"
                markerEnd="url(#arrow-incident)"
              />
              <text x={x1 - 10} y={y1 - 6} fontSize="11" fill="#be123c" fontWeight="bold" fontFamily="sans-serif">
                Incident Ray
              </text>

              {/* Angle of Refraction Arc (θ₂) */}
              <path
                d={`M ${cx} ${cy + arcRadius} A ${arcRadius} ${arcRadius} 0 0 0 ${arc2_x} ${arc2_y}`}
                fill="none"
                stroke="#2563eb"
                strokeWidth="2"
              />
              <text
                data-testid="optics-label-theta2"
                x={cx + 12}
                y={cy + 30}
                fontSize="11"
                fill="#1d4ed8"
                fontWeight="bold"
                fontFamily="sans-serif"
              >
                θ₂ = {theta2}°
              </text>

              {/* Refracted Ray (Blue with arrow) */}
              <line
                data-testid="optics-ray-refracted"
                x1={cx}
                y1={cy}
                x2={x2}
                y2={y2}
                stroke="#2563eb"
                strokeWidth="3"
                markerEnd="url(#arrow-refracted)"
              />
              <text x={x2 + 8} y={y2 + 10} fontSize="11" fill="#1d4ed8" fontWeight="bold" fontFamily="sans-serif">
                Refracted Ray
              </text>

              {/* Point of Incidence Marker */}
              <circle cx={cx} cy={cy} r="4" fill="#0f172a" stroke="#ffffff" strokeWidth="1.5" />
            </svg>
          )}
        </div>

        {/* Interactive Feature Inspection Chips */}
        <div className="flex flex-wrap items-center justify-between gap-2 text-xs">
          <span className="text-slate-500 font-medium">Click components to inspect physics parameters:</span>
          {isThinLens ? (
            <div className="flex flex-wrap gap-1.5">
              <button
                type="button"
                data-testid="optics-chip-ray1"
                onClick={() => setActiveChip(activeChip === 'ray1' ? null : 'ray1')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                  activeChip === 'ray1' ? 'bg-rose-600 text-white shadow-2xs' : 'bg-rose-50 text-rose-700 hover:bg-rose-100'
                }`}
              >
                Ray 1 (Parallel → Focus)
              </button>
              <button
                type="button"
                data-testid="optics-chip-ray2"
                onClick={() => setActiveChip(activeChip === 'ray2' ? null : 'ray2')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                  activeChip === 'ray2' ? 'bg-blue-600 text-white shadow-2xs' : 'bg-blue-50 text-blue-700 hover:bg-blue-100'
                }`}
              >
                Ray 2 (Through Centre O)
              </button>
              <button
                type="button"
                data-testid="optics-chip-ray3"
                onClick={() => setActiveChip(activeChip === 'ray3' ? null : 'ray3')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                  activeChip === 'ray3' ? 'bg-emerald-600 text-white shadow-2xs' : 'bg-emerald-50 text-emerald-700 hover:bg-emerald-100'
                }`}
              >
                Ray 3 (Focus → Parallel)
              </button>
            </div>
          ) : (
            <div className="flex flex-wrap gap-1.5">
              <button
                type="button"
                data-testid="optics-chip-incident"
                onClick={() => setActiveChip('incident')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                  activeChip === 'incident' ? 'bg-rose-600 text-white shadow-2xs' : 'bg-rose-50 text-rose-700 hover:bg-rose-100'
                }`}
              >
                Incident Ray ({theta1}°)
              </button>
              <button
                type="button"
                data-testid="optics-chip-refracted"
                onClick={() => setActiveChip('refracted')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                  activeChip === 'refracted' ? 'bg-blue-600 text-white shadow-2xs' : 'bg-blue-50 text-blue-700 hover:bg-blue-100'
                }`}
              >
                Refracted Ray ({theta2}°)
              </button>
              <button
                type="button"
                data-testid="optics-chip-critical"
                onClick={() => setActiveChip('critical')}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold transition-all ${
                  activeChip === 'critical' ? 'bg-amber-600 text-white shadow-2xs' : 'bg-amber-50 text-amber-700 hover:bg-amber-100'
                }`}
              >
                Critical Angle (θc = {thetac}°)
              </button>
            </div>
          )}
        </div>

        {/* Inspection Details Callout */}
        {activeChip && (
          <div
            data-testid="optics-inspection-detail"
            className="p-3 bg-indigo-50 border border-indigo-200 rounded-xl flex items-center justify-between text-xs text-indigo-950 animate-in fade-in"
          >
            <div className="flex items-center gap-2">
              <CheckCircle className="w-4 h-4 text-indigo-600 shrink-0" />
              {activeChip === 'ray1' && (
                <span>
                  <strong>Principal Ray 1:</strong> Incident parallel to the principal axis. After passing through the {spec.lens_type || 'converging'} lens, it refracts directly through the real principal focus (F₂).
                </span>
              )}
              {activeChip === 'ray2' && (
                <span>
                  <strong>Principal Ray 2:</strong> Passes directly through the optical centre (O) of the thin lens without undergoing any refraction or deviation.
                </span>
              )}
              {activeChip === 'ray3' && (
                <span>
                  <strong>Principal Ray 3:</strong> Passes through the front focus (F₁). Upon striking the lens, it refracts parallel to the principal axis.
                </span>
              )}
              {activeChip === 'incident' && (
                <span>
                  <strong>Angle of Incidence (θ₁ = {theta1}°):</strong> Measured strictly between the incident ray and the normal line perpendicular to the surface.
                </span>
              )}
              {activeChip === 'refracted' && (
                <span>
                  <strong>Snell's Law Verification:</strong> n₁·sin({theta1}°) = n₂·sin({theta2}°). Because light enters an optically denser medium ({spec.medium_2?.name}), wave speed slows down and the ray bends <em>towards</em> the normal (θ₂ &lt; θ₁).
                </span>
              )}
              {activeChip === 'critical' && (
                <span>
                  <strong>Total Internal Reflection Threshold:</strong> When light attempts to pass from {spec.medium_2?.name} back into air, any angle of incidence greater than θc = {thetac}° will result in 100% total internal reflection with zero transmitted light.
                </span>
              )}
            </div>
            <button
              type="button"
              onClick={() => setActiveChip(null)}
              className="text-[11px] font-mono text-indigo-700 hover:text-indigo-900 underline ml-2"
            >
              Close
            </button>
          </div>
        )}
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
