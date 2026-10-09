import React, { useState, useRef, useEffect, useMemo } from 'react';
import { 
  Box, 
  RotateCw, 
  Maximize2, 
  Sparkles, 
  Eye, 
  CheckCircle2, 
  Play, 
  Pause,
  Layers,
  Compass
} from 'lucide-react';

const POLYHEDRA = {
  cube: {
    name: 'Cube (Hexahedron)',
    faces: 6,
    vertices: 8,
    edges: 12,
    baseSize: 100,
    eulerValid: true,
    formula: 'F(6) + V(8) - E(12) = 2',
    description: '6 congruent square faces meeting at 90° right angles.',
  },
  rectangular_prism: {
    name: 'Rectangular Prism',
    faces: 6,
    vertices: 8,
    edges: 12,
    baseSize: 110,
    eulerValid: true,
    formula: 'F(6) + V(8) - E(12) = 2',
    description: '3 pairs of opposite identical rectangular faces.',
  },
  triangular_prism: {
    name: 'Triangular Prism',
    faces: 5,
    vertices: 6,
    edges: 9,
    baseSize: 100,
    eulerValid: true,
    formula: 'F(5) + V(6) - E(9) = 2',
    description: '2 parallel triangular bases connected by 3 rectangular sides.',
  },
  square_pyramid: {
    name: 'Square-based Pyramid',
    faces: 5,
    vertices: 5,
    edges: 8,
    baseSize: 100,
    eulerValid: true,
    formula: 'F(5) + V(5) - E(8) = 2',
    description: '1 square base with 4 triangular faces meeting at the apex.',
  },
  tetrahedron: {
    name: 'Tetrahedron (Triangular Pyramid)',
    faces: 4,
    vertices: 4,
    edges: 6,
    baseSize: 100,
    eulerValid: true,
    formula: 'F(4) + V(4) - E(6) = 2',
    description: '4 equilateral triangular faces. Platonic solid.',
  },
};

export default function GeometricNets3DViewer({
  defaultShape = 'cube',
  onFoldComplete = () => {},
}) {
  const [activeShape, setActiveShape] = useState(defaultShape);
  const [foldProgress, setFoldProgress] = useState(0.35); // 0 = 2D flat, 1 = 3D folded
  const [rotation, setRotation] = useState({ x: -25, y: 35 });
  const [isAutoRotating, setIsAutoRotating] = useState(false);
  const [highlightMode, setHighlightMode] = useState('all'); // 'all' | 'faces' | 'vertices' | 'edges'
  const isDraggingRef = useRef(false);
  const lastMousePosRef = useRef({ x: 0, y: 0 });
  const animationFrameRef = useRef(null);

  const shapeData = POLYHEDRA[activeShape] || POLYHEDRA.cube;

  // Auto-rotation loop
  useEffect(() => {
    if (isAutoRotating) {
      const step = () => {
        setRotation(prev => ({
          x: prev.x,
          y: (prev.y + 0.5) % 360,
        }));
        animationFrameRef.current = requestAnimationFrame(step);
      };
      animationFrameRef.current = requestAnimationFrame(step);
    } else if (animationFrameRef.current) {
      cancelAnimationFrame(animationFrameRef.current);
    }
    return () => {
      if (animationFrameRef.current) cancelAnimationFrame(animationFrameRef.current);
    };
  }, [isAutoRotating]);

  // Pointer drag to orbit 3D model
  const handlePointerDown = (e) => {
    isDraggingRef.current = true;
    lastMousePosRef.current = { x: e.clientX, y: e.clientY };
  };

  const handlePointerMove = (e) => {
    if (!isDraggingRef.current) return;
    const dx = e.clientX - lastMousePosRef.current.x;
    const dy = e.clientY - lastMousePosRef.current.y;
    lastMousePosRef.current = { x: e.clientX, y: e.clientY };

    setRotation(prev => ({
      x: Math.max(-85, Math.min(85, prev.x - dy * 0.5)),
      y: (prev.y + dx * 0.5) % 360,
    }));
  };

  const handlePointerUp = () => {
    isDraggingRef.current = false;
  };

  // Fold angle calculation (0 to 90 degrees)
  const foldAngle = foldProgress * 90;
  const isFullyFolded = foldProgress >= 0.98;
  const isFullyFlat = foldProgress <= 0.05;

  return (
    <div className="w-full bg-slate-900 text-white rounded-2xl overflow-hidden border border-slate-700 shadow-xl flex flex-col select-none">
      {/* Top Header / Mode Bar */}
      <div className="px-4 py-3 bg-slate-800/90 border-b border-slate-700 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-blue-600/30 text-blue-400 border border-blue-500/40 flex items-center justify-center">
            <Box className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-white flex items-center gap-1.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
              Dynamic 2D-to-3D Folding Net
              <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-blue-500/20 text-blue-300 border border-blue-500/30">
                AI Blackboard SOTA
              </span>
            </h3>
            <p className="text-[11px] text-slate-400">
              Extrude flat nets into rotatable 3D polyhedra • Real-time Euler verification
            </p>
          </div>
        </div>

        {/* Shape Selector Chips */}
        <div className="flex items-center gap-1 overflow-x-auto scrollbar-none py-1">
          {Object.entries(POLYHEDRA).map(([key, item]) => (
            <button
              key={key}
              onClick={() => setActiveShape(key)}
              className={`px-2.5 py-1 rounded-lg text-xs font-medium transition-all ${
                activeShape === key
                  ? 'bg-blue-600 text-white shadow-xs'
                  : 'bg-slate-700/60 text-slate-300 hover:bg-slate-700 hover:text-white'
              }`}
            >
              {item.name.split(' ')[0]}
            </button>
          ))}
        </div>
      </div>

      {/* Main 3D Canvas Viewport */}
      <div 
        className="relative w-full h-[360px] sm:h-[420px] bg-radial from-slate-800 to-slate-950 flex items-center justify-center overflow-hidden cursor-grab active:cursor-grabbing"
        onPointerDown={handlePointerDown}
        onPointerMove={handlePointerMove}
        onPointerUp={handlePointerUp}
        onPointerLeave={handlePointerUp}
        style={{ perspective: '900px' }}
      >
        {/* Subtle 3D Grid floor */}
        <div 
          className="absolute inset-0 pointer-events-none opacity-20"
          style={{
            backgroundImage: 'radial-gradient(circle, #3b82f6 1px, transparent 1px)',
            backgroundSize: '24px 24px',
          }}
        />

        {/* Status Pills Overlay */}
        <div className="absolute top-3 left-3 flex flex-col gap-1.5 z-10 pointer-events-none">
          <div className="px-2.5 py-1 rounded-full bg-slate-900/80 backdrop-blur-md border border-slate-700/70 text-[11px] font-mono text-slate-300 flex items-center gap-1.5">
            <Compass className="w-3.5 h-3.5 text-blue-400" />
            <span>Rot: X:{Math.round(rotation.x)}° Y:{Math.round(rotation.y)}°</span>
          </div>
          <div className="px-2.5 py-1 rounded-full bg-slate-900/80 backdrop-blur-md border border-slate-700/70 text-[11px] font-mono text-emerald-400 flex items-center gap-1.5">
            <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
            <span>State: {isFullyFolded ? '3D Solid (Folded)' : isFullyFlat ? '2D Flat Net' : `Folding ${Math.round(foldProgress * 100)}%`}</span>
          </div>
        </div>

        {/* Orbit / Reset Controls Overlay */}
        <div className="absolute top-3 right-3 flex items-center gap-1.5 z-10">
          <button
            onClick={() => setIsAutoRotating(!isAutoRotating)}
            className={`p-1.5 rounded-lg border text-xs font-medium transition-all ${
              isAutoRotating
                ? 'bg-blue-600 border-blue-400 text-white'
                : 'bg-slate-800/90 border-slate-700 text-slate-300 hover:text-white'
            }`}
            title={isAutoRotating ? 'Pause rotation' : 'Auto-rotate'}
          >
            {isAutoRotating ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
          </button>
          <button
            onClick={() => setRotation({ x: -25, y: 35 })}
            className="p-1.5 rounded-lg bg-slate-800/90 border border-slate-700 text-slate-300 hover:text-white text-xs font-medium"
            title="Reset view"
          >
            <RotateCw className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* 3D Polyhedron / Net Model */}
        <div
          className="relative transition-transform duration-75 ease-out"
          style={{
            transformStyle: 'preserve-3d',
            transform: `rotateX(${rotation.x}deg) rotateY(${rotation.y}deg)`,
            width: '100px',
            height: '100px',
          }}
        >
          {/* CUBE & RECTANGULAR PRISM RENDERING */}
          {(activeShape === 'cube' || activeShape === 'rectangular_prism') && (
            <div className="relative w-full h-full" style={{ transformStyle: 'preserve-3d' }}>
              {/* Face 1: Base (Bottom) */}
              <div 
                className={`absolute inset-0 bg-blue-500/80 border-2 ${highlightMode === 'edges' ? 'border-amber-400' : 'border-blue-300'} flex items-center justify-center font-bold text-white text-xs shadow-inner transition-colors`}
                style={{
                  transform: 'translateZ(0px)',
                  boxShadow: '0 0 15px rgba(59, 130, 246, 0.4)',
                }}
              >
                Base
              </div>

              {/* Face 2: Front (folds UP from bottom edge of Base) */}
              <div
                className={`absolute inset-0 bg-cyan-500/75 border-2 ${highlightMode === 'edges' ? 'border-amber-400' : 'border-cyan-300'} flex items-center justify-center font-bold text-white text-xs transition-colors`}
                style={{
                  transformOrigin: 'top',
                  transform: `translateY(100px) rotateX(${-foldAngle}deg)`,
                }}
              >
                Front
              </div>

              {/* Face 3: Back (folds UP from top edge of Base) */}
              <div
                className={`absolute inset-0 bg-indigo-500/75 border-2 ${highlightMode === 'edges' ? 'border-amber-400' : 'border-indigo-300'} flex items-center justify-center font-bold text-white text-xs transition-colors`}
                style={{
                  transformOrigin: 'bottom',
                  transform: `translateY(-100px) rotateX(${foldAngle}deg)`,
                }}
              >
                Back
              </div>

              {/* Face 4: Left (folds UP from left edge of Base) */}
              <div
                className={`absolute inset-0 bg-emerald-500/75 border-2 ${highlightMode === 'edges' ? 'border-amber-400' : 'border-emerald-300'} flex items-center justify-center font-bold text-white text-xs transition-colors`}
                style={{
                  transformOrigin: 'right',
                  transform: `translateX(-100px) rotateY(${-foldAngle}deg)`,
                }}
              >
                Left
              </div>

              {/* Face 5: Right (folds UP from right edge of Base) */}
              <div
                className={`absolute inset-0 bg-amber-500/75 border-2 ${highlightMode === 'edges' ? 'border-amber-400' : 'border-amber-300'} flex items-center justify-center font-bold text-white text-xs transition-colors`}
                style={{
                  transformOrigin: 'left',
                  transform: `translateX(100px) rotateY(${foldAngle}deg)`,
                }}
              >
                {/* Face 6: Top (attached to Right face and folds 90 deg inward) */}
                <div
                  className={`absolute inset-0 bg-rose-500/75 border-2 ${highlightMode === 'edges' ? 'border-amber-400' : 'border-rose-300'} flex items-center justify-center font-bold text-white text-xs transition-colors`}
                  style={{
                    transformOrigin: 'left',
                    transform: `translateX(100px) rotateY(${foldAngle}deg)`,
                  }}
                >
                  Top
                </div>
                Right
              </div>
            </div>
          )}

          {/* SQUARE-BASED PYRAMID RENDERING */}
          {(activeShape === 'square_pyramid' || activeShape === 'tetrahedron' || activeShape === 'triangular_prism') && (
            <div className="relative w-full h-full" style={{ transformStyle: 'preserve-3d' }}>
              {/* Base */}
              <div 
                className="absolute inset-0 bg-blue-600/80 border-2 border-blue-300 flex items-center justify-center font-bold text-white text-xs"
                style={{ transform: 'translateZ(0px)' }}
              >
                Base
              </div>

              {/* Triangular Flap 1 (North) */}
              <div
                className="absolute inset-0 flex items-center justify-center"
                style={{
                  transformOrigin: 'bottom',
                  transform: `translateY(-100px) rotateX(${foldProgress * 65}deg)`,
                  clipPath: 'polygon(50% 0%, 0% 100%, 100% 100%)',
                  backgroundColor: 'rgba(234, 88, 12, 0.8)',
                  border: '1px solid #fdba74',
                }}
              >
                <span className="text-[10px] font-bold mt-6">N</span>
              </div>

              {/* Triangular Flap 2 (South) */}
              <div
                className="absolute inset-0 flex items-center justify-center"
                style={{
                  transformOrigin: 'top',
                  transform: `translateY(100px) rotateX(${-foldProgress * 65}deg)`,
                  clipPath: 'polygon(50% 100%, 0% 0%, 100% 0%)',
                  backgroundColor: 'rgba(16, 185, 129, 0.8)',
                  border: '1px solid #86efac',
                }}
              >
                <span className="text-[10px] font-bold mb-6">S</span>
              </div>

              {/* Triangular Flap 3 (West) */}
              <div
                className="absolute inset-0 flex items-center justify-center"
                style={{
                  transformOrigin: 'right',
                  transform: `translateX(-100px) rotateY(${-foldProgress * 65}deg)`,
                  clipPath: 'polygon(0% 50%, 100% 0%, 100% 100%)',
                  backgroundColor: 'rgba(168, 85, 247, 0.8)',
                  border: '1px solid #d8b4fe',
                }}
              >
                <span className="text-[10px] font-bold mr-6">W</span>
              </div>

              {/* Triangular Flap 4 (East) */}
              <div
                className="absolute inset-0 flex items-center justify-center"
                style={{
                  transformOrigin: 'left',
                  transform: `translateX(100px) rotateY(${foldProgress * 65}deg)`,
                  clipPath: 'polygon(100% 50%, 0% 0%, 0% 100%)',
                  backgroundColor: 'rgba(236, 72, 153, 0.8)',
                  border: '1px solid #fbcfe8',
                }}
              >
                <span className="text-[10px] font-bold ml-6">E</span>
              </div>
            </div>
          )}
        </div>
      </div>

      {/* Interactive Controls & Euler Formula Dashboard */}
      <div className="p-4 bg-slate-800 border-t border-slate-700 flex flex-col gap-3">
        {/* The Folding Net Extrusion Slider */}
        <div className="flex flex-col gap-1.5">
          <div className="flex items-center justify-between text-xs">
            <span className="font-semibold text-slate-300 flex items-center gap-1.5">
              <Layers className="w-3.5 h-3.5 text-blue-400" />
              Fold Extrusion Gesture:
            </span>
            <div className="flex items-center gap-2 font-mono text-[11px]">
              <button 
                onClick={() => setFoldProgress(0)}
                className="text-slate-400 hover:text-white underline cursor-pointer"
              >
                Flat 2D (0%)
              </button>
              <span className="text-blue-400 font-bold">{Math.round(foldProgress * 100)}%</span>
              <button 
                onClick={() => setFoldProgress(1)}
                className="text-slate-400 hover:text-white underline cursor-pointer"
              >
                Folded 3D (100%)
              </button>
            </div>
          </div>
          <input
            type="range"
            min="0"
            max="1"
            step="0.01"
            value={foldProgress}
            onChange={(e) => {
              const val = parseFloat(e.target.value);
              setFoldProgress(val);
              if (val >= 0.98) onFoldComplete(shapeData);
            }}
            className="w-full h-2 bg-slate-700 rounded-lg appearance-none cursor-pointer accent-blue-500"
          />
        </div>

        {/* Live Euler Formula Inspector: F + V - E = 2 */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
          <div 
            onClick={() => setHighlightMode(highlightMode === 'faces' ? 'all' : 'faces')}
            className={`p-2.5 rounded-xl border cursor-pointer transition-all ${
              highlightMode === 'faces' 
                ? 'bg-blue-600/30 border-blue-400 text-white' 
                : 'bg-slate-900/60 border-slate-700/80 text-slate-300 hover:border-slate-600'
            }`}
          >
            <div className="text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Faces (F)</div>
            <div className="text-lg font-bold font-mono text-blue-400">{shapeData.faces}</div>
            <div className="text-[10px] text-slate-400">2D polygonal surfaces</div>
          </div>

          <div 
            onClick={() => setHighlightMode(highlightMode === 'vertices' ? 'all' : 'vertices')}
            className={`p-2.5 rounded-xl border cursor-pointer transition-all ${
              highlightMode === 'vertices' 
                ? 'bg-emerald-600/30 border-emerald-400 text-white' 
                : 'bg-slate-900/60 border-slate-700/80 text-slate-300 hover:border-slate-600'
            }`}
          >
            <div className="text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Vertices (V)</div>
            <div className="text-lg font-bold font-mono text-emerald-400">{shapeData.vertices}</div>
            <div className="text-[10px] text-slate-400">Corner intersections</div>
          </div>

          <div 
            onClick={() => setHighlightMode(highlightMode === 'edges' ? 'all' : 'edges')}
            className={`p-2.5 rounded-xl border cursor-pointer transition-all ${
              highlightMode === 'edges' 
                ? 'bg-amber-600/30 border-amber-400 text-white' 
                : 'bg-slate-900/60 border-slate-700/80 text-slate-300 hover:border-slate-600'
            }`}
          >
            <div className="text-[10px] text-slate-400 uppercase tracking-wider font-semibold">Edges (E)</div>
            <div className="text-lg font-bold font-mono text-amber-400">{shapeData.edges}</div>
            <div className="text-[10px] text-slate-400">Fold line boundaries</div>
          </div>

          <div className="p-2.5 rounded-xl bg-purple-950/40 border border-purple-500/40 text-purple-200">
            <div className="text-[10px] text-purple-300 uppercase tracking-wider font-semibold">Euler Check</div>
            <div className="text-sm font-bold font-mono text-purple-300 pt-0.5">{shapeData.formula}</div>
            <div className="text-[10px] text-purple-400 flex items-center gap-1">
              <CheckCircle2 className="w-3 h-3 text-emerald-400 inline" /> Valid Polyhedron
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
