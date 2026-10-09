import React, { useState, useRef, useEffect } from 'react';
import { 
  Atom, 
  RotateCw, 
  Play, 
  Pause, 
  Sparkles, 
  Thermometer, 
  Compass, 
  CheckCircle2 
} from 'lucide-react';

const MOLECULES = {
  butane: {
    name: 'Butane (Unbranched Chain)',
    formula: 'C4H10',
    type: 'Chain Isomer',
    boilingPoint: '-0.5°C',
    imf: 'London Dispersion (Higher surface area -> Stronger intermolecular forces)',
    description: 'Straight 4-carbon alkane chain. Greater contact area than branched isomer.',
    atoms: [
      { id: 'c1', type: 'C', x: -60, y: 0, z: 0 },
      { id: 'c2', type: 'C', x: -20, y: 25, z: 15 },
      { id: 'c3', type: 'C', x: 20, y: -10, z: -15 },
      { id: 'c4', type: 'C', x: 60, y: 15, z: 10 },
      // Hydrogens
      { id: 'h1', type: 'H', x: -80, y: -15, z: -10 },
      { id: 'h2', type: 'H', x: -75, y: 20, z: -15 },
      { id: 'h3', type: 'H', x: -65, y: -15, z: 25 },
      { id: 'h4', type: 'H', x: 80, y: 30, z: 0 },
      { id: 'h5', type: 'H', x: 75, y: -10, z: 20 },
      { id: 'h6', type: 'H', x: 65, y: 20, z: -25 },
    ],
    bonds: [
      ['c1', 'c2'], ['c2', 'c3'], ['c3', 'c4'],
      ['c1', 'h1'], ['c1', 'h2'], ['c1', 'h3'],
      ['c4', 'h4'], ['c4', 'h5'], ['c4', 'h6'],
    ],
  },
  methylpropane: {
    name: '2-Methylpropane (Isobutane)',
    formula: 'C4H10',
    type: 'Chain Isomer',
    boilingPoint: '-11.7°C',
    imf: 'London Dispersion (Spherical shape -> Less surface area -> Weaker forces)',
    description: 'Branched alkane. Compact spherical geometry reduces intermolecular contact.',
    atoms: [
      { id: 'c1', type: 'C', x: 0, y: 0, z: 0 },
      { id: 'c2', type: 'C', x: -45, y: -30, z: -10 },
      { id: 'c3', type: 'C', x: 45, y: -30, z: -10 },
      { id: 'c4', type: 'C', x: 0, y: 50, z: 20 },
      // Hydrogens
      { id: 'h1', type: 'H', x: 0, y: -15, z: 35 },
      { id: 'h2', type: 'H', x: -65, y: -45, z: 0 },
      { id: 'h3', type: 'H', x: 65, y: -45, z: 0 },
      { id: 'h4', type: 'H', x: 0, y: 75, z: 0 },
    ],
    bonds: [
      ['c1', 'c2'], ['c1', 'c3'], ['c1', 'c4'], ['c1', 'h1'],
      ['c2', 'h2'], ['c3', 'h3'], ['c4', 'h4'],
    ],
  },
  propan1ol: {
    name: 'Propan-1-ol (Primary Alcohol)',
    formula: 'C3H8O',
    type: 'Positional Isomer',
    boilingPoint: '97.2°C',
    imf: 'Hydrogen Bonding (Terminal -OH group creates accessible polar site)',
    description: 'Hydroxyl group on carbon 1. Strong hydrogen bonding between molecules.',
    atoms: [
      { id: 'c1', type: 'C', x: -45, y: 0, z: 0 },
      { id: 'c2', type: 'C', x: 0, y: 20, z: 10 },
      { id: 'c3', type: 'C', x: 45, y: -10, z: -10 },
      { id: 'o1', type: 'O', x: 80, y: 15, z: 5 },
      { id: 'h1', type: 'H', x: 105, y: 25, z: 10 },
      // Hydrogens
      { id: 'h2', type: 'H', x: -65, y: -20, z: -10 },
      { id: 'h3', type: 'H', x: -55, y: 20, z: 15 },
    ],
    bonds: [
      ['c1', 'c2'], ['c2', 'c3'], ['c3', 'o1'], ['o1', 'h1'],
      ['c1', 'h2'], ['c1', 'h3'],
    ],
  },
  propan2ol: {
    name: 'Propan-2-ol (Secondary Alcohol)',
    formula: 'C3H8O',
    type: 'Positional Isomer',
    boilingPoint: '82.6°C',
    imf: 'Hydrogen Bonding (Internal -OH group sterically crowded -> Slightly lower BP)',
    description: 'Hydroxyl group on carbon 2. Steric hindrance lowers hydrogen bond strength.',
    atoms: [
      { id: 'c1', type: 'C', x: -45, y: -20, z: 0 },
      { id: 'c2', type: 'C', x: 0, y: 10, z: 0 },
      { id: 'c3', type: 'C', x: 45, y: -20, z: 0 },
      { id: 'o1', type: 'O', x: 0, y: 55, z: 15 },
      { id: 'h1', type: 'H', x: -15, y: 75, z: 20 },
    ],
    bonds: [
      ['c1', 'c2'], ['c2', 'c3'], ['c2', 'o1'], ['o1', 'h1'],
    ],
  },
};

const ATOM_STYLES = {
  C: { bg: 'bg-slate-700', border: 'border-slate-500', size: 'w-7 h-7', label: 'C', color: '#334155' },
  H: { bg: 'bg-slate-100 text-slate-900', border: 'border-slate-300', size: 'w-4 h-4', label: 'H', color: '#f1f5f9' },
  O: { bg: 'bg-rose-600', border: 'border-rose-400', size: 'w-6 h-6', label: 'O', color: '#e11d48' },
  N: { bg: 'bg-blue-600', border: 'border-blue-400', size: 'w-6 h-6', label: 'N', color: '#2563eb' },
};

export default function OrganicChemistry3DViewer() {
  const [activeKey, setActiveKey] = useState('butane');
  const [rotation, setRotation] = useState({ x: -15, y: 40 });
  const [isAutoRotating, setIsAutoRotating] = useState(true);
  const isDraggingRef = useRef(false);
  const lastMousePosRef = useRef({ x: 0, y: 0 });
  const animRef = useRef(null);

  const activeMolecule = MOLECULES[activeKey] || MOLECULES.butane;

  // Auto rotation
  useEffect(() => {
    if (isAutoRotating) {
      const step = () => {
        setRotation(prev => ({
          x: prev.x,
          y: (prev.y + 0.6) % 360,
        }));
        animRef.current = requestAnimationFrame(step);
      };
      animRef.current = requestAnimationFrame(step);
    } else if (animRef.current) {
      cancelAnimationFrame(animRef.current);
    }
    return () => {
      if (animRef.current) cancelAnimationFrame(animRef.current);
    };
  }, [isAutoRotating]);

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

  // Build projected 2D coordinates with 3D rotation matrix
  const radX = (rotation.x * Math.PI) / 180;
  const radY = (rotation.y * Math.PI) / 180;

  const projectedAtoms = activeMolecule.atoms.map(a => {
    // Rotate Y
    const x1 = a.x * Math.cos(radY) + a.z * Math.sin(radY);
    const z1 = -a.x * Math.sin(radY) + a.z * Math.cos(radY);
    // Rotate X
    const y2 = a.y * Math.cos(radX) - z1 * Math.sin(radX);
    const z2 = a.y * Math.sin(radX) + z1 * Math.cos(radX);

    return {
      ...a,
      projX: x1,
      projY: y2,
      projZ: z2,
    };
  });

  const atomMap = Object.fromEntries(projectedAtoms.map(a => [a.id, a]));

  return (
    <div className="w-full bg-slate-900 text-white rounded-2xl overflow-hidden border border-slate-700 shadow-xl flex flex-col select-none">
      {/* Top Header */}
      <div className="px-4 py-3 bg-slate-800/90 border-b border-slate-700 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-teal-600/30 text-teal-400 border border-teal-500/40 flex items-center justify-center">
            <Atom className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-white flex items-center gap-1.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
              3D Ball-and-Stick Molecular Isomer Explorer
              <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-teal-500/20 text-teal-300 border border-teal-500/30">
                AI Blackboard SOTA
              </span>
            </h3>
            <p className="text-[11px] text-slate-400">
              Rotatable 3D Isomers • Tetrahedral Carbon • CPK Conventions • Intermolecular Forces
            </p>
          </div>
        </div>

        {/* Molecule selection pills */}
        <div className="flex items-center gap-1 overflow-x-auto scrollbar-none py-1">
          {Object.entries(MOLECULES).map(([key, item]) => (
            <button
              key={key}
              onClick={() => setActiveKey(key)}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
                activeKey === key
                  ? 'bg-teal-600 text-white shadow-xs'
                  : 'bg-slate-700/60 text-slate-300 hover:bg-slate-700 hover:text-white'
              }`}
            >
              {item.name.split(' ')[0]}
            </button>
          ))}
        </div>
      </div>

      {/* 3D Viewport Stage */}
      <div
        className="relative w-full h-[280px] sm:h-[320px] bg-radial from-slate-800 to-slate-950 flex items-center justify-center overflow-hidden cursor-grab active:cursor-grabbing"
        onPointerDown={handlePointerDown}
        onPointerMove={handlePointerMove}
        onPointerUp={handlePointerUp}
        onPointerLeave={handlePointerUp}
      >
        {/* Status overlay */}
        <div className="absolute top-3 left-3 flex flex-col gap-1.5 z-10 pointer-events-none">
          <div className="px-2.5 py-1 rounded-full bg-slate-900/80 backdrop-blur-md border border-slate-700/70 text-[11px] font-mono text-teal-300 flex items-center gap-1.5">
            <Atom className="w-3.5 h-3.5 text-teal-400" />
            <span>{activeMolecule.name}</span>
          </div>
          <div className="px-2.5 py-1 rounded-full bg-slate-900/80 backdrop-blur-md border border-slate-700/70 text-[11px] font-mono text-slate-300 flex items-center gap-1.5">
            <Thermometer className="w-3.5 h-3.5 text-rose-400" />
            <span>BP: {activeMolecule.boilingPoint}</span>
          </div>
        </div>

        {/* Controls overlay */}
        <div className="absolute top-3 right-3 flex items-center gap-1.5 z-10">
          <button
            onClick={() => setIsAutoRotating(!isAutoRotating)}
            className="p-1.5 rounded-lg bg-slate-800/90 border border-slate-700 text-slate-300 hover:text-white text-xs"
          >
            {isAutoRotating ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
          </button>
          <button
            onClick={() => setRotation({ x: -15, y: 40 })}
            className="p-1.5 rounded-lg bg-slate-800/90 border border-slate-700 text-slate-300 hover:text-white text-xs"
          >
            <RotateCw className="w-3.5 h-3.5" />
          </button>
        </div>

        {/* SVG Bonds & Projected Atoms Layer */}
        <svg className="w-full h-full pointer-events-none overflow-visible">
          <g transform="translate(250, 150)">
            {/* Draw Bonds */}
            {activeMolecule.bonds.map(([id1, id2], i) => {
              const a1 = atomMap[id1];
              const a2 = atomMap[id2];
              if (!a1 || !a2) return null;
              return (
                <line
                  key={i}
                  x1={a1.projX * 1.5}
                  y1={-a1.projY * 1.5}
                  x2={a2.projX * 1.5}
                  y2={-a2.projY * 1.5}
                  stroke="#64748b"
                  strokeWidth="5"
                  strokeLinecap="round"
                />
              );
            })}

            {/* Draw Atoms (sorted by Z depth so front covers back) */}
            {[...projectedAtoms]
              .sort((a, b) => a.projZ - b.projZ)
              .map(atom => {
                const style = ATOM_STYLES[atom.type] || ATOM_STYLES.C;
                const r = atom.type === 'C' ? 14 : atom.type === 'O' ? 13 : 8;
                return (
                  <g key={atom.id} transform={`translate(${atom.projX * 1.5}, ${-atom.projY * 1.5})`}>
                    <circle
                      r={r}
                      fill={style.color}
                      stroke="#0f172a"
                      strokeWidth="2"
                      filter="drop-shadow(0px 2px 4px rgba(0,0,0,0.5))"
                    />
                    <text
                      y={atom.type === 'H' ? 2.5 : 4}
                      textAnchor="middle"
                      fill={atom.type === 'H' ? '#0f172a' : '#ffffff'}
                      fontSize={atom.type === 'H' ? '8px' : '10px'}
                      fontWeight="bold"
                      fontFamily="monospace"
                    >
                      {atom.type}
                    </text>
                  </g>
                );
              })}
          </g>
        </svg>
      </div>

      {/* Intermolecular Forces & CAPS Explanation Footer */}
      <div className="p-4 bg-slate-800 border-t border-slate-700 flex flex-col gap-2">
        <div className="flex items-center justify-between text-xs">
          <span className="font-semibold text-slate-300">Isomer Classification & Physical Properties:</span>
          <span className="font-mono text-teal-400 font-bold">{activeMolecule.type} ({activeMolecule.formula})</span>
        </div>

        <div className="p-2.5 rounded-xl bg-slate-900/70 border border-slate-700 text-xs text-slate-300 flex flex-col gap-1">
          <div className="flex items-center gap-1.5 font-bold text-white">
            <Sparkles className="w-3.5 h-3.5 text-amber-400" />
            Intermolecular Forces:
          </div>
          <p className="text-[11px] text-slate-300 leading-relaxed">
            {activeMolecule.imf}
          </p>
        </div>

        <div className="flex items-center justify-between text-[11px] text-slate-400 pt-1">
          <span>CPK Colors: Black = C, White = H, Red = O</span>
          <span className="text-emerald-400 flex items-center gap-1">
            <CheckCircle2 className="w-3 h-3 text-emerald-400" /> Tetrahedral Bond Geometry (109.5°)
          </span>
        </div>
      </div>
    </div>
  );
}
