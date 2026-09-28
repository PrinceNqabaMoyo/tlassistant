import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import {
  Compass,
  RotateCw,
  Sparkles,
  Info,
  Play,
  Pause,
  RotateCcw,
  CheckCircle,
  Box,
  Layers
} from 'lucide-react';

/**
 * ComplexPlaneExplorer Component
 * Interactive Cognitive & Pedagogical Explorer for Complex Numbers:
 *
 * Tab 1: "The Origin of i" — Solving y = x² + q = 0 (q ∈ [-4, 4])
 *   - 2D Real Parabola view vs 3D Orthogonal Complex Root Extender.
 *   - When q > 0, roots do not vanish; they extend orthogonally into
 *     the imaginary plane as x = ±i√q.
 *
 * Tab 2: "Geometric Meaning of i" — Argand Plane & Rotations
 *   - Interactive z = a + bi with modulus |z| = r and argument θ.
 *   - Step-by-step 90° rotation animation proving i² = -1 as a half-turn
 *     (two 90° rotations make a 180° flip).
 */
export default function ComplexPlaneExplorer({
  initialData = {},
  onChange = () => {},
  isSubmitted = false,
}) {
  const [activeTab, setActiveTab] = useState(initialData.activeTab || 'origin'); // 'origin' | 'geometry'

  // ── TAB 1 STATE: Origin of i (y = x² + q) ──
  const [qValue, setQValue] = useState(initialData.qValue ?? 1); // default q = 1 (y = x² + 1)
  const [viewMode3D, setViewMode3D] = useState(false); // 2D vs 3D Orthogonal
  const [rotX, setRotX] = useState(25); // 3D pitch angle
  const [rotY, setRotY] = useState(45); // 3D yaw angle
  const isDragging3D = useRef(false);
  const dragStartPos = useRef({ x: 0, y: 0 });

  // ── TAB 2 STATE: Geometric Meaning of i (z = a + bi) ──
  const [realPart, setRealPart] = useState(initialData.realPart ?? 2);
  const [imagPart, setImagPart] = useState(initialData.imagPart ?? 1);
  const [rotationAngle, setRotationAngle] = useState(0); // animated rotation offset (deg)
  const [isRotating, setIsRotating] = useState(false);
  const [autoRotate, setAutoRotate] = useState(false);
  const [multiplierStep, setMultiplierStep] = useState(0); // 0: 1, 1: i, 2: i² (-1), 3: i³ (-i)
  const [showUnitCircle, setShowUnitCircle] = useState(true);
  const [showModulusArc, setShowModulusArc] = useState(true);

  // Notify parent of state changes
  useEffect(() => {
    onChange({
      activeTab,
      qValue,
      realPart,
      imagPart,
      multiplierStep,
    });
  }, [activeTab, qValue, realPart, imagPart, multiplierStep, onChange]);

  // ── TAB 1 CALCULATIONS ──
  const discriminant = useMemo(() => -4 * qValue, [qValue]);
  const hasRealRoots = qValue <= 0;
  const realRootVal = hasRealRoots ? Math.sqrt(-qValue) : null;
  const imagRootVal = qValue > 0 ? Math.sqrt(qValue) : null;

  // ── TAB 2 CALCULATIONS ──
  const currentAngleRad = (rotationAngle * Math.PI) / 180;
  // Apply visual rotation to vector (a, b)
  const animatedA = realPart * Math.cos(currentAngleRad) - imagPart * Math.sin(currentAngleRad);
  const animatedB = realPart * Math.sin(currentAngleRad) + imagPart * Math.cos(currentAngleRad);

  const modulus = useMemo(() => {
    return Math.sqrt(realPart * realPart + imagPart * imagPart);
  }, [realPart, imagPart]);

  const argumentRad = useMemo(() => {
    return Math.atan2(imagPart, realPart);
  }, [realPart, imagPart]);

  const argumentDeg = useMemo(() => {
    const deg = (argumentRad * 180) / Math.PI;
    return deg < 0 ? deg + 360 : deg;
  }, [argumentRad]);

  // ── AUTO ROTATION INTERVAL ──
  useEffect(() => {
    let timer = null;
    if (autoRotate) {
      timer = setInterval(() => {
        setMultiplierStep((prev) => (prev + 1) % 4);
      }, 1600);
    }
    return () => {
      if (timer) clearInterval(timer);
    };
  }, [autoRotate]);

  // Sync rotation angle smoothly with multiplierStep
  useEffect(() => {
    const targetDeg = multiplierStep * 90;
    setIsRotating(true);
    setRotationAngle(targetDeg);
    const timeout = setTimeout(() => setIsRotating(false), 500);
    return () => clearTimeout(timeout);
  }, [multiplierStep]);

  // Rotate by 90° (+i)
  const handleMultiplyByI = useCallback(() => {
    setMultiplierStep((prev) => (prev + 1) % 4);
  }, []);

  // Reset rotation to base z
  const handleResetRotation = useCallback(() => {
    setMultiplierStep(0);
    setRotationAngle(0);
    setAutoRotate(false);
  }, []);

  // ── 3D DRAG HANDLING ──
  const handleMouseDown3D = (e) => {
    isDragging3D.current = true;
    dragStartPos.current = { x: e.clientX, y: e.clientY };
  };

  const handleMouseMove3D = (e) => {
    if (!isDragging3D.current) return;
    const dx = e.clientX - dragStartPos.current.x;
    const dy = e.clientY - dragStartPos.current.y;
    dragStartPos.current = { x: e.clientX, y: e.clientY };
    setRotY((y) => (y + dx * 0.5) % 360);
    setRotX((x) => Math.max(-10, Math.min(80, x - dy * 0.5)));
  };

  const handleMouseUp3D = () => {
    isDragging3D.current = false;
  };

  // 3D Isometric Projector
  const project3D = (x, y, z, cx = 220, cy = 180, scale = 24) => {
    const radX = (rotX * Math.PI) / 180;
    const radY = (rotY * Math.PI) / 180;

    // Yaw rotation around vertical axis (Z or Y)
    const x1 = x * Math.cos(radY) - y * Math.sin(radY);
    const y1 = x * Math.sin(radY) + y * Math.cos(radY);
    const z1 = z;

    // Pitch rotation
    const y2 = y1 * Math.cos(radX) - z1 * Math.sin(radX);
    const z2 = y1 * Math.sin(radX) + z1 * Math.cos(radX);

    return {
      px: cx + x1 * scale,
      py: cy - z2 * scale, // SVG inverted y
      depth: y2,
    };
  };

  return (
    <div className="w-full bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden flex flex-col text-slate-100 font-sans">
      {/* ── TOOL HEADER ── */}
      <div className="px-5 py-4 border-b border-slate-800 bg-slate-950/80 flex flex-wrap items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-br from-[#13519C] to-indigo-600 flex items-center justify-center text-white shadow-md">
            <Compass className="w-5 h-5 text-cyan-300" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-base sm:text-lg font-bold text-white font-afacad tracking-tight">
                Complex Plane &amp; Origin of <span className="text-cyan-400 font-serif italic">i</span>
              </h2>
              <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                Cognitive Visualizer
              </span>
              {isSubmitted && (
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                  Recorded
                </span>
              )}
            </div>
            <p className="text-xs text-slate-400">
              Interactive pedagogy: Orthogonal root extension &amp; 90° rotational meaning of <span className="font-serif italic text-cyan-400">i² = -1</span>
            </p>
          </div>
        </div>

        {/* Tab Switcher */}
        <div className="flex items-center p-1 bg-slate-900 border border-slate-800 rounded-xl">
          <button
            type="button"
            onClick={() => setActiveTab('origin')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer flex items-center gap-1.5 ${
              activeTab === 'origin'
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            <span>1. Origin of i (y = x² + q)</span>
          </button>
          <button
            type="button"
            onClick={() => setActiveTab('geometry')}
            className={`px-3.5 py-1.5 rounded-lg text-xs font-bold transition cursor-pointer flex items-center gap-1.5 ${
              activeTab === 'geometry'
                ? 'bg-[#13519C] text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200'
            }`}
          >
            <RotateCw className="w-3.5 h-3.5" />
            <span>2. Geometric Meaning (Argand)</span>
          </button>
        </div>
      </div>

      {/* ── TAB 1: ORIGIN OF i (y = x² + q) ── */}
      {activeTab === 'origin' && (
        <div className="p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Canvas Panel (7 cols) */}
          <div className="lg:col-span-7 flex flex-col space-y-3">
            {/* View Controls Bar */}
            <div className="flex items-center justify-between bg-slate-950/60 p-2.5 rounded-xl border border-slate-800 text-xs">
              <div className="flex items-center gap-2">
                <span className="text-slate-400 font-medium">Viewport:</span>
                <button
                  type="button"
                  onClick={() => setViewMode3D(false)}
                  className={`px-2.5 py-1 rounded-lg font-bold transition cursor-pointer ${
                    !viewMode3D
                      ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40'
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  2D Real Plane (x, y)
                </button>
                <button
                  type="button"
                  onClick={() => setViewMode3D(true)}
                  className={`px-2.5 py-1 rounded-lg font-bold transition cursor-pointer flex items-center gap-1 ${
                    viewMode3D
                      ? 'bg-purple-500/20 text-purple-300 border border-purple-500/40'
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  <Box className="w-3 h-3 text-purple-400" />
                  <span>3D Orthogonal Extender</span>
                </button>
              </div>

              {viewMode3D && (
                <span className="text-[11px] text-slate-400 font-mono hidden sm:inline">
                  Drag 3D canvas to rotate view
                </span>
              )}
            </div>

            {/* SVG Visualizer Area */}
            <div
              className="relative w-full h-[360px] bg-slate-950 border border-slate-800 rounded-2xl overflow-hidden flex items-center justify-center select-none"
              onMouseDown={viewMode3D ? handleMouseDown3D : undefined}
              onMouseMove={viewMode3D ? handleMouseMove3D : undefined}
              onMouseUp={viewMode3D ? handleMouseUp3D : undefined}
            >
              {!viewMode3D ? (
                // ── 2D REAL VIEW SVG ──
                <svg
                  viewBox="-220 -180 440 360"
                  className="w-full h-full"
                  style={{ overflow: 'visible' }}
                >
                  {/* Grid Lines */}
                  {[-4, -3, -2, -1, 1, 2, 3, 4].map((n) => (
                    <g key={`grid-x-${n}`}>
                      <line
                        x1={n * 40}
                        y1={-160}
                        x2={n * 40}
                        y2={160}
                        stroke="#1e293b"
                        strokeWidth="1"
                      />
                      <text
                        x={n * 40}
                        y={14}
                        fill="#64748b"
                        fontSize="9"
                        textAnchor="middle"
                        fontFamily="monospace"
                      >
                        {n}
                      </text>
                    </g>
                  ))}
                  {[-4, -3, -2, -1, 1, 2, 3, 4].map((n) => (
                    <g key={`grid-y-${n}`}>
                      <line
                        x1={-200}
                        y1={-n * 32}
                        x2={200}
                        y2={-n * 32}
                        stroke="#1e293b"
                        strokeWidth="1"
                      />
                      <text
                        x={-8}
                        y={-n * 32 + 3}
                        fill="#64748b"
                        fontSize="9"
                        textAnchor="end"
                        fontFamily="monospace"
                      >
                        {n}
                      </text>
                    </g>
                  ))}

                  {/* Real X-Axis and Y-Axis */}
                  <line x1="-210" y1="0" x2="210" y2="0" stroke="#475569" strokeWidth="1.5" />
                  <line x1="0" y1="-170" x2="0" y2="170" stroke="#475569" strokeWidth="1.5" />
                  <text x="205" y="-6" fill="#94a3b8" fontSize="10" fontWeight="bold">
                    x (Real)
                  </text>
                  <text x="8" y="-160" fill="#94a3b8" fontSize="10" fontWeight="bold">
                    y = x² + q
                  </text>

                  {/* Parabola: y = x² + q */}
                  <path
                    d={(() => {
                      const pts = [];
                      for (let x = -3.5; x <= 3.5; x += 0.1) {
                        const y = x * x + qValue;
                        const sx = x * 40;
                        const sy = -y * 32;
                        pts.push(`${x === -3.5 ? 'M' : 'L'} ${sx.toFixed(1)} ${sy.toFixed(1)}`);
                      }
                      return pts.join(' ');
                    })()}
                    fill="none"
                    stroke={qValue > 0 ? '#38bdf8' : '#10b981'}
                    strokeWidth="2.5"
                  />

                  {/* Vertex Point */}
                  <circle
                    cx="0"
                    cy={-qValue * 32}
                    r="4.5"
                    fill="#f59e0b"
                    stroke="#ffffff"
                    strokeWidth="1.5"
                  />
                  <text
                    x="12"
                    y={-qValue * 32 + 4}
                    fill="#fbbf24"
                    fontSize="10"
                    fontWeight="bold"
                  >
                    Vertex (0, {qValue})
                  </text>

                  {/* Real Roots when q <= 0 */}
                  {hasRealRoots && realRootVal !== null && (
                    <>
                      <circle
                        cx={-realRootVal * 40}
                        cy="0"
                        r="5"
                        fill="#10b981"
                        stroke="#ffffff"
                        strokeWidth="1.5"
                      />
                      <text
                        x={-realRootVal * 40}
                        y="-10"
                        fill="#34d399"
                        fontSize="10"
                        fontWeight="bold"
                        textAnchor="middle"
                      >
                        x₁ = -{realRootVal.toFixed(1)}
                      </text>

                      <circle
                        cx={realRootVal * 40}
                        cy="0"
                        r="5"
                        fill="#10b981"
                        stroke="#ffffff"
                        strokeWidth="1.5"
                      />
                      <text
                        x={realRootVal * 40}
                        y="-10"
                        fill="#34d399"
                        fontSize="10"
                        fontWeight="bold"
                        textAnchor="middle"
                      >
                        x₂ = +{realRootVal.toFixed(1)}
                      </text>
                    </>
                  )}

                  {/* Complex Roots Ghost Guide when q > 0 */}
                  {qValue > 0 && imagRootVal !== null && (
                    <g>
                      {/* Ghost line indicating roots have lifted off */}
                      <line
                        x1="0"
                        y1={-qValue * 32}
                        x2="0"
                        y2="0"
                        stroke="#c084fc"
                        strokeWidth="1.5"
                        strokeDasharray="4 3"
                      />
                      <rect
                        x="-100"
                        y="-35"
                        width="200"
                        height="24"
                        rx="6"
                        fill="#581c87"
                        fillOpacity="0.8"
                        stroke="#c084fc"
                        strokeWidth="1"
                      />
                      <text
                        x="0"
                        y="-20"
                        fill="#f3e8ff"
                        fontSize="10"
                        fontWeight="bold"
                        textAnchor="middle"
                      >
                        ✨ Roots lifted off into 3D: ± {imagRootVal === 1 ? '' : imagRootVal.toFixed(1)}i
                      </text>
                    </g>
                  )}
                </svg>
              ) : (
                // ── 3D ORTHOGONAL EXTENDER VIEW SVG ──
                <svg viewBox="0 0 440 360" className="w-full h-full cursor-grab active:cursor-grabbing">
                  {/* Real Axis (X) */}
                  {(() => {
                    const pStart = project3D(-4, 0, 0);
                    const pEnd = project3D(4, 0, 0);
                    return (
                      <g>
                        <line
                          x1={pStart.px}
                          y1={pStart.py}
                          x2={pEnd.px}
                          y2={pEnd.py}
                          stroke="#38bdf8"
                          strokeWidth="2"
                        />
                        <text
                          x={pEnd.px + 8}
                          y={pEnd.py + 4}
                          fill="#38bdf8"
                          fontSize="11"
                          fontWeight="bold"
                        >
                          Re(x) [Real]
                        </text>
                      </g>
                    );
                  })()}

                  {/* Imaginary Axis (Y_im) Orthogonal / Depth Axis */}
                  {(() => {
                    const pStart = project3D(0, -3.5, 0);
                    const pEnd = project3D(0, 3.5, 0);
                    return (
                      <g>
                        <line
                          x1={pStart.px}
                          y1={pStart.py}
                          x2={pEnd.px}
                          y2={pEnd.py}
                          stroke="#c084fc"
                          strokeWidth="2"
                          strokeDasharray="4 2"
                        />
                        <text
                          x={pEnd.px + 8}
                          y={pEnd.py + 4}
                          fill="#c084fc"
                          fontSize="11"
                          fontWeight="bold"
                        >
                          Im(x) [Imaginary ⟂]
                        </text>
                      </g>
                    );
                  })()}

                  {/* Height Axis (Output y) */}
                  {(() => {
                    const pStart = project3D(0, 0, -2);
                    const pEnd = project3D(0, 0, 5);
                    return (
                      <g>
                        <line
                          x1={pStart.px}
                          y1={pStart.py}
                          x2={pEnd.px}
                          y2={pEnd.py}
                          stroke="#64748b"
                          strokeWidth="1.5"
                        />
                        <text
                          x={pEnd.px}
                          y={pEnd.py - 8}
                          fill="#cbd5e1"
                          fontSize="10"
                          fontWeight="bold"
                        >
                          Height (y)
                        </text>
                      </g>
                    );
                  })()}

                  {/* Base y = 0 complex plane reference grid */}
                  <polygon
                    points={`${project3D(-3, -3, 0).px},${project3D(-3, -3, 0).py} ${
                      project3D(3, -3, 0).px
                    },${project3D(3, -3, 0).py} ${project3D(3, 3, 0).px},${
                      project3D(3, 3, 0).py
                    } ${project3D(-3, 3, 0).px},${project3D(-3, 3, 0).py}`}
                    fill="#1e293b"
                    fillOpacity="0.4"
                    stroke="#334155"
                    strokeWidth="1"
                  />

                  {/* 1. Real Slice Parabola: x ∈ [-3, 3], Im(x) = 0, y = x² + q */}
                  <path
                    d={(() => {
                      const pts = [];
                      for (let x = -3; x <= 3; x += 0.2) {
                        const z = x * x + qValue;
                        const proj = project3D(x, 0, z);
                        pts.push(`${x === -3 ? 'M' : 'L'} ${proj.px.toFixed(1)} ${proj.py.toFixed(1)}`);
                      }
                      return pts.join(' ');
                    })()}
                    fill="none"
                    stroke="#38bdf8"
                    strokeWidth="2.5"
                  />

                  {/* 2. Orthogonal Complex Root Extender Parabola: Re(x) = 0, y = q - (Im)² */}
                  {qValue > 0 && (
                    <path
                      d={(() => {
                        const pts = [];
                        const maxIm = Math.sqrt(qValue) + 0.8;
                        for (let im = -maxIm; im <= maxIm; im += 0.15) {
                          const z = qValue - im * im;
                          const proj = project3D(0, im, z);
                          pts.push(`${im === -maxIm ? 'M' : 'L'} ${proj.px.toFixed(1)} ${proj.py.toFixed(1)}`);
                        }
                        return pts.join(' ');
                      })()}
                      fill="none"
                      stroke="#c084fc"
                      strokeWidth="2.5"
                      strokeDasharray="5 3"
                    />
                  )}

                  {/* Vertex in 3D */}
                  {(() => {
                    const proj = project3D(0, 0, qValue);
                    return (
                      <g>
                        <circle cx={proj.px} cy={proj.py} r="5" fill="#f59e0b" stroke="#ffffff" strokeWidth="1.5" />
                        <text x={proj.px + 8} y={proj.py - 6} fill="#fbbf24" fontSize="10" fontWeight="bold">
                          Vertex (0, 0, {qValue})
                        </text>
                      </g>
                    );
                  })()}

                  {/* Complex Roots Intersection in 3D (where orthogonal curve cuts y = 0) */}
                  {qValue > 0 && imagRootVal !== null && (
                    <>
                      {/* Positive imaginary root (0, +√q, 0) */}
                      {(() => {
                        const proj = project3D(0, imagRootVal, 0);
                        return (
                          <g>
                            <circle cx={proj.px} cy={proj.py} r="6" fill="#ec4899" stroke="#ffffff" strokeWidth="2" />
                            <text
                              x={proj.px + 10}
                              y={proj.py + 4}
                              fill="#f472b6"
                              fontSize="11"
                              fontWeight="bold"
                            >
                              x = +{imagRootVal === 1 ? '' : imagRootVal.toFixed(1)}i
                            </text>
                          </g>
                        );
                      })()}

                      {/* Negative imaginary root (0, -√q, 0) */}
                      {(() => {
                        const proj = project3D(0, -imagRootVal, 0);
                        return (
                          <g>
                            <circle cx={proj.px} cy={proj.py} r="6" fill="#ec4899" stroke="#ffffff" strokeWidth="2" />
                            <text
                              x={proj.px - 10}
                              y={proj.py + 4}
                              fill="#f472b6"
                              fontSize="11"
                              fontWeight="bold"
                              textAnchor="end"
                            >
                              x = -{imagRootVal === 1 ? '' : imagRootVal.toFixed(1)}i
                            </text>
                          </g>
                        );
                      })()}
                    </>
                  )}
                </svg>
              )}
            </div>

            {/* Parameter Slider: q */}
            <div className="p-4 bg-slate-950/70 rounded-xl border border-slate-800 space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="font-semibold text-slate-300">
                  Vertical Shift Parameter <span className="font-mono text-cyan-400 font-bold">q = {qValue}</span>
                </span>
                <span className="text-[11px] font-mono text-slate-400">
                  Equation: <strong className="text-white">y = x² {qValue >= 0 ? `+ ${qValue}` : `- ${Math.abs(qValue)}`}</strong>
                </span>
              </div>

              <input
                type="range"
                min="-4"
                max="4"
                step="0.5"
                value={qValue}
                onChange={(e) => setQValue(parseFloat(e.target.value))}
                className="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-400"
              />

              {/* Quick Presets */}
              <div className="flex items-center justify-between pt-1">
                <span className="text-[10px] text-slate-500 uppercase tracking-wider font-bold">Presets:</span>
                <div className="flex gap-1.5">
                  {[-4, -1, 0, 1, 4].map((val) => (
                    <button
                      key={`preset-${val}`}
                      type="button"
                      onClick={() => setQValue(val)}
                      className={`px-2 py-0.5 rounded text-[11px] font-mono transition cursor-pointer ${
                        qValue === val
                          ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/40 font-bold'
                          : 'bg-slate-800 text-slate-400 hover:text-white'
                      }`}
                    >
                      q = {val}
                    </button>
                  ))}
                </div>
              </div>
            </div>
          </div>

          {/* Right Pedagogical Explanation Panel (5 cols) */}
          <div className="lg:col-span-5 flex flex-col space-y-4">
            {/* Cognitive Status Card */}
            <div
              className={`p-4 rounded-xl border transition ${
                qValue > 0
                  ? 'bg-purple-950/30 border-purple-500/40'
                  : qValue === 0
                  ? 'bg-amber-950/30 border-amber-500/40'
                  : 'bg-emerald-950/30 border-emerald-500/40'
              }`}
            >
              <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                  Root Nature &amp; Discriminant
                </span>
                <span
                  className={`text-[10px] font-bold px-2 py-0.5 rounded-full ${
                    qValue > 0
                      ? 'bg-purple-500/20 text-purple-300 border border-purple-500/30'
                      : qValue === 0
                      ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                      : 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30'
                  }`}
                >
                  Δ = {discriminant}
                </span>
              </div>

              <div className="text-sm font-bold text-white font-afacad">
                {qValue > 0 ? (
                  <span className="text-purple-300">
                    2 Purely Imaginary Roots: x = ±{imagRootVal === 1 ? '' : imagRootVal?.toFixed(2)}i
                  </span>
                ) : qValue === 0 ? (
                  <span className="text-amber-300">1 Repeated Real Root: x = 0</span>
                ) : (
                  <span className="text-emerald-300">
                    2 Distinct Real Roots: x = ±{realRootVal?.toFixed(2)}
                  </span>
                )}
              </div>

              <p className="text-xs text-slate-300 mt-1 leading-relaxed">
                {qValue > 0
                  ? 'The parabola does not touch the real x-axis because its roots extend 90° into the orthogonal imaginary dimension.'
                  : qValue === 0
                  ? 'The vertex touches the real x-axis at the origin (0, 0), creating a single double root.'
                  : 'The parabola dips below the real line, cutting the real x-axis at two visible intercepts.'}
              </p>
            </div>

            {/* Step-by-Step Algebraic Derivation */}
            <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2.5 text-xs">
              <span className="font-bold text-slate-200 block text-[11px] uppercase tracking-wider">
                Step-by-Step Rigorous Derivation
              </span>

              <div className="space-y-1.5 font-mono text-[12px] bg-slate-900/90 p-3 rounded-lg border border-slate-800">
                <div className="flex justify-between">
                  <span className="text-slate-400">1. Set equation to zero:</span>
                  <span className="text-white">x² + {qValue} = 0</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">2. Subtract {qValue}:</span>
                  <span className="text-cyan-300">x² = {-qValue}</span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">3. Take square root:</span>
                  <span className="text-amber-300">x = ±√({-qValue})</span>
                </div>

                {qValue > 0 && (
                  <>
                    <div className="flex justify-between border-t border-slate-800 pt-1.5">
                      <span className="text-slate-400">4. Factor out √(-1):</span>
                      <span className="text-purple-300">x = ±√(−1) · √({qValue})</span>
                    </div>
                    <div className="flex justify-between font-bold">
                      <span className="text-slate-400">5. Substitute i = √(-1):</span>
                      <span className="text-pink-400">x = ±{imagRootVal === 1 ? '' : imagRootVal?.toFixed(2)}i</span>
                    </div>
                  </>
                )}
              </div>
            </div>

            {/* Cognitive Takeaway Callout */}
            <div className="p-3.5 rounded-xl bg-cyan-950/20 border border-cyan-500/30 text-xs text-cyan-200 flex items-start gap-2.5">
              <Sparkles className="w-4 h-4 text-cyan-400 flex-shrink-0 mt-0.5" />
              <div>
                <strong className="block text-cyan-300 font-bold mb-0.5">
                  The Fundamental Pedagogical Insight
                </strong>
                <span>
                  High school textbooks often say: &quot;A negative square root does not exist.&quot;{' '}
                  <strong className="text-white">It does exist</strong>, but not on the 1D real line.
                  Just as negative numbers were invented when subtraction walked backwards past zero,
                  imaginary numbers were discovered when roots walked 90° perpendicular to the line!
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ── TAB 2: GEOMETRIC MEANING OF i (ARGAND ROTATION) ── */}
      {activeTab === 'geometry' && (
        <div className="p-4 sm:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
          {/* Left Argand Diagram Canvas (7 cols) */}
          <div className="lg:col-span-7 flex flex-col space-y-3">
            {/* Argand View Controls */}
            <div className="flex items-center justify-between bg-slate-950/60 p-2.5 rounded-xl border border-slate-800 text-xs">
              <div className="flex items-center gap-2">
                <button
                  type="button"
                  onClick={() => setShowUnitCircle((c) => !c)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                    showUnitCircle
                      ? 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30'
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  Unit Circle (r = 1)
                </button>
                <button
                  type="button"
                  onClick={() => setShowModulusArc((a) => !a)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition cursor-pointer ${
                    showModulusArc
                      ? 'bg-amber-500/20 text-amber-300 border border-amber-500/30'
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  Modulus Arc (r = {modulus.toFixed(1)})
                </button>
              </div>

              <div className="flex items-center gap-1.5">
                <button
                  type="button"
                  onClick={handleResetRotation}
                  className="p-1 text-slate-400 hover:text-white rounded hover:bg-slate-800"
                  title="Reset to 0°"
                >
                  <RotateCcw className="w-4 h-4" />
                </button>
                <button
                  type="button"
                  onClick={() => setAutoRotate((a) => !a)}
                  className={`px-2.5 py-1 rounded-lg text-xs font-bold transition cursor-pointer flex items-center gap-1 ${
                    autoRotate
                      ? 'bg-pink-600 text-white'
                      : 'bg-slate-800 text-slate-300 hover:bg-slate-700'
                  }`}
                >
                  {autoRotate ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
                  <span>{autoRotate ? 'Pause' : 'Auto-Rotate'}</span>
                </button>
              </div>
            </div>

            {/* Argand Plane SVG */}
            <div className="relative w-full h-[360px] bg-slate-950 border border-slate-800 rounded-2xl overflow-hidden flex items-center justify-center select-none">
              <svg
                viewBox="-220 -180 440 360"
                className="w-full h-full"
                style={{ overflow: 'visible' }}
              >
                {/* Grid Rings */}
                {[1, 2, 3, 4].map((r) => (
                  <circle
                    key={`ring-${r}`}
                    cx="0"
                    cy="0"
                    r={r * 40}
                    fill="none"
                    stroke="#1e293b"
                    strokeWidth="1"
                    strokeDasharray={r === 1 && showUnitCircle ? 'none' : '2 2'}
                  />
                ))}

                {/* Optional Modulus Circle */}
                {showModulusArc && modulus > 0 && (
                  <circle
                    cx="0"
                    cy="0"
                    r={modulus * 40}
                    fill="none"
                    stroke="#f59e0b"
                    strokeWidth="1.2"
                    strokeDasharray="4 3"
                    strokeOpacity="0.6"
                  />
                )}

                {/* Real & Imaginary Axes */}
                <line x1="-210" y1="0" x2="210" y2="0" stroke="#475569" strokeWidth="1.5" />
                <line x1="0" y1="-170" x2="0" y2="170" stroke="#475569" strokeWidth="1.5" />

                {/* Axis Labels */}
                <text x="180" y="-8" fill="#38bdf8" fontSize="10" fontWeight="bold">
                  +Re (Real)
                </text>
                <text x="-210" y="-8" fill="#64748b" fontSize="10">
                  -Re (-1)
                </text>
                <text x="8" y="-155" fill="#c084fc" fontSize="10" fontWeight="bold">
                  +Im (+i)
                </text>
                <text x="8" y="165" fill="#64748b" fontSize="10">
                  -Im (-i)
                </text>

                {/* Tick numbers */}
                {[-4, -3, -2, -1, 1, 2, 3, 4].map((n) => (
                  <g key={`tick-${n}`}>
                    <line x1={n * 40} y1="-3" x2={n * 40} y2="3" stroke="#64748b" />
                    <text x={n * 40} y="13" fill="#64748b" fontSize="8" textAnchor="middle">
                      {n}
                    </text>
                    <line x1="-3" y1={-n * 40} x2="3" y2={-n * 40} stroke="#64748b" />
                    <text x="-8" y={-n * 40 + 3} fill="#64748b" fontSize="8" textAnchor="end">
                      {n}i
                    </text>
                  </g>
                ))}

                {/* Rotation Trail Arc (from base angle to animated angle) */}
                {rotationAngle > 0 && (
                  <path
                    d={(() => {
                      const rPx = Math.min(modulus * 40, 150);
                      const startAng = argumentRad;
                      const endAng = argumentRad + currentAngleRad;
                      const x1 = rPx * Math.cos(startAng);
                      const y1 = -rPx * Math.sin(startAng);
                      const x2 = rPx * Math.cos(endAng);
                      const y2 = -rPx * Math.sin(endAng);
                      const largeArc = currentAngleRad > Math.PI ? 1 : 0;
                      return `M ${x1} ${y1} A ${rPx} ${rPx} 0 ${largeArc} 0 ${x2} ${y2}`;
                    })()}
                    fill="none"
                    stroke="#ec4899"
                    strokeWidth="2.5"
                    strokeDasharray="4 2"
                  />
                )}

                {/* Base vector ghost (original z before rotation) */}
                {rotationAngle > 0 && (
                  <line
                    x1="0"
                    y1="0"
                    x2={realPart * 40}
                    y2={-imagPart * 40}
                    stroke="#475569"
                    strokeWidth="1.5"
                    strokeDasharray="3 3"
                  />
                )}

                {/* Active Rotating Vector z */}
                <line
                  x1="0"
                  y1="0"
                  x2={animatedA * 40}
                  y2={-animatedB * 40}
                  stroke="#38bdf8"
                  strokeWidth="3"
                  className={isRotating ? 'transition-all duration-500 ease-out' : ''}
                />

                {/* Complex point z */}
                <circle
                  cx={animatedA * 40}
                  cy={-animatedB * 40}
                  r="6"
                  fill="#0284c7"
                  stroke="#38bdf8"
                  strokeWidth="2"
                  className={isRotating ? 'transition-all duration-500 ease-out' : ''}
                />

                {/* Point Label */}
                <text
                  x={animatedA * 40 + 10}
                  y={-animatedB * 40 - 10}
                  fill="#ffffff"
                  fontSize="12"
                  fontWeight="bold"
                  className={isRotating ? 'transition-all duration-500 ease-out' : ''}
                >
                  {multiplierStep === 0
                    ? `z = (${realPart >= 0 ? realPart : realPart} + ${imagPart}i)`
                    : multiplierStep === 1
                    ? `z · i = (${animatedA.toFixed(1)} + ${animatedB.toFixed(1)}i)`
                    : multiplierStep === 2
                    ? `z · i² = -z = (${animatedA.toFixed(1)} + ${animatedB.toFixed(1)}i)`
                    : `z · i³ = -zi = (${animatedA.toFixed(1)} + ${animatedB.toFixed(1)}i)`}
                </text>
              </svg>
            </div>

            {/* Interactive Coordinate Sliders for z = a + bi */}
            <div className="grid grid-cols-2 gap-3 p-3.5 bg-slate-950/70 rounded-xl border border-slate-800 text-xs">
              <div className="space-y-1.5">
                <div className="flex justify-between">
                  <span className="text-slate-400">Real Part (a):</span>
                  <span className="font-mono text-cyan-400 font-bold">{realPart}</span>
                </div>
                <input
                  type="range"
                  min="-4"
                  max="4"
                  step="0.5"
                  value={realPart}
                  onChange={(e) => {
                    setRealPart(parseFloat(e.target.value));
                    setMultiplierStep(0);
                    setRotationAngle(0);
                  }}
                  className="w-full h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-cyan-400"
                />
              </div>

              <div className="space-y-1.5">
                <div className="flex justify-between">
                  <span className="text-slate-400">Imaginary Part (b):</span>
                  <span className="font-mono text-purple-400 font-bold">{imagPart}i</span>
                </div>
                <input
                  type="range"
                  min="-4"
                  max="4"
                  step="0.5"
                  value={imagPart}
                  onChange={(e) => {
                    setImagPart(parseFloat(e.target.value));
                    setMultiplierStep(0);
                    setRotationAngle(0);
                  }}
                  className="w-full h-1.5 bg-slate-800 rounded appearance-none cursor-pointer accent-purple-400"
                />
              </div>
            </div>
          </div>

          {/* Right Pedagogical Explanation & Multiplier Controls (5 cols) */}
          <div className="lg:col-span-5 flex flex-col space-y-4">
            {/* 1-Tap Multiply Action Banner */}
            <div className="p-4 rounded-xl bg-gradient-to-br from-[#13519C]/30 to-purple-950/40 border border-cyan-500/40 space-y-3">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-bold text-white font-afacad">
                  The Rotational Power of <span className="text-cyan-300 font-serif italic">i</span>
                </h3>
                <span className="text-[10px] font-mono px-2 py-0.5 rounded bg-cyan-500/20 text-cyan-300 font-bold">
                  +90° / turn
                </span>
              </div>

              <button
                type="button"
                onClick={handleMultiplyByI}
                className="w-full py-3 rounded-xl bg-[#13519C] hover:bg-[#0f3e77] text-white text-xs font-bold transition flex items-center justify-center gap-2 shadow-lg cursor-pointer"
              >
                <RotateCw className="w-4 h-4 text-cyan-300" />
                <span>Multiply by i (Rotate +90° Counterclockwise)</span>
              </button>

              {/* 4-Cycle State Stepper */}
              <div className="grid grid-cols-4 gap-1 pt-1">
                {[
                  { step: 0, label: '· 1', deg: '0°' },
                  { step: 1, label: '· i', deg: '90°' },
                  { step: 2, label: '· i² (-1)', deg: '180°' },
                  { step: 3, label: '· i³ (-i)', deg: '270°' },
                ].map((item) => (
                  <button
                    key={`step-${item.step}`}
                    type="button"
                    onClick={() => setMultiplierStep(item.step)}
                    className={`p-2 rounded-lg text-center transition cursor-pointer ${
                      multiplierStep === item.step
                        ? 'bg-cyan-500/30 border border-cyan-400 text-white font-bold'
                        : 'bg-slate-900/80 border border-slate-800 text-slate-400 hover:text-slate-200'
                    }`}
                  >
                    <div className="text-[11px] font-mono">{item.label}</div>
                    <div className="text-[9px] text-slate-400">{item.deg}</div>
                  </button>
                ))}
              </div>
            </div>

            {/* Modulus & Argument Breakdown */}
            <div className="p-4 rounded-xl bg-slate-950/70 border border-slate-800 space-y-2.5 text-xs">
              <span className="font-bold text-slate-200 block text-[11px] uppercase tracking-wider">
                Polar &amp; Exponential Representation
              </span>

              <div className="space-y-1.5 font-mono text-[11px] bg-slate-900/90 p-3 rounded-lg border border-slate-800">
                <div className="flex justify-between">
                  <span className="text-slate-400">Modulus (Length r = |z|):</span>
                  <span className="text-amber-400 font-bold">
                    √({realPart}² + {imagPart}²) = {modulus.toFixed(2)}
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">Argument (Angle θ):</span>
                  <span className="text-pink-400 font-bold">
                    {argumentDeg.toFixed(1)}° ({(argumentRad / Math.PI).toFixed(2)}π rad)
                  </span>
                </div>
                <div className="flex justify-between border-t border-slate-800 pt-1.5">
                  <span className="text-slate-400">Polar Form:</span>
                  <span className="text-cyan-300">
                    {modulus.toFixed(1)}(cos {argumentDeg.toFixed(0)}° + i sin {argumentDeg.toFixed(0)}°)
                  </span>
                </div>
                <div className="flex justify-between">
                  <span className="text-slate-400">Euler&apos;s Form:</span>
                  <span className="text-purple-300">
                    {modulus.toFixed(1)} · e^(i·{argumentDeg.toFixed(0)}°)
                  </span>
                </div>
              </div>
            </div>

            {/* Why i² = -1 Pedagogical Takeaway */}
            <div className="p-3.5 rounded-xl bg-purple-950/20 border border-purple-500/30 text-xs text-purple-200 flex items-start gap-2.5">
              <Info className="w-4 h-4 text-purple-400 flex-shrink-0 mt-0.5" />
              <div>
                <strong className="block text-purple-300 font-bold mb-0.5">
                  Why i × i = -1 (Geometric Proof)
                </strong>
                <span>
                  Multiplying any real number by -1 produces a 180° rotation on the number line.
                  Because multiplying by <strong className="text-cyan-300">i</strong> rotates by 90°,
                  multiplying twice (<strong className="text-white">i × i</strong>) rotates 90° + 90° = 180°,
                  landing directly on <strong className="text-pink-300">-1</strong>!
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* ── TOOL FOOTER ── */}
      <div className="px-5 py-3 border-t border-slate-800 bg-slate-950 flex flex-wrap items-center justify-between gap-2 text-xs text-slate-400">
        <div className="flex items-center gap-1.5">
          <CheckCircle className="w-3.5 h-3.5 text-emerald-400" />
          <span>CAPS FET Mathematics Grade 11-12 &amp; Technical Mathematics Enrichment</span>
        </div>
        <div className="font-mono text-[11px] text-slate-400">Fundile Cognitive Explorers</div>
      </div>
    </div>
  );
}
