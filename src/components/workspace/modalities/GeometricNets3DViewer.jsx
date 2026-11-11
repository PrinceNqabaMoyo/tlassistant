import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Box, Layers, CheckCircle2 } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

const POLYHEDRA = {
  cube: {
    name: 'Cube (Hexahedron)',
    faces: 6,
    vertices: 8,
    edges: 12,
    formula: 'F(6) + V(8) - E(12) = 2',
    saFormula: 'TSA = 6 s^2',
    volFormula: 'V = s^3',
    defaultDims: { s: 4, l: 4, b: 4, h: 4 },
    description: '6 congruent square faces meeting at 90° right angles.',
  },
  rectangular_prism: {
    name: 'Rectangular Prism',
    faces: 6,
    vertices: 8,
    edges: 12,
    formula: 'F(6) + V(8) - E(12) = 2',
    saFormula: 'TSA = 2(lb + lh + bh)',
    volFormula: 'V = l \\cdot b \\cdot h',
    defaultDims: { s: 4, l: 6, b: 4, h: 3 },
    description: '3 pairs of opposite identical rectangular faces.',
  },
  triangular_prism: {
    name: 'Triangular Prism',
    faces: 5,
    vertices: 6,
    edges: 9,
    formula: 'F(5) + V(6) - E(9) = 2',
    saFormula: 'TSA = 2\\!\\left(\\tfrac{1}{2}bh_{\\triangle}\\right) + P_{\\triangle} \\cdot H',
    volFormula: 'V = \\left(\\tfrac{1}{2} b h_{\\triangle}\\right) \\cdot H',
    defaultDims: { s: 4, l: 5, b: 4, h: 3 },
    description: '2 parallel triangular bases connected by 3 rectangular sides.',
  },
  square_pyramid: {
    name: 'Square-based Pyramid',
    faces: 5,
    vertices: 5,
    edges: 8,
    formula: 'F(5) + V(5) - E(8) = 2',
    saFormula: 'TSA = b^2 + 4\\!\\left(\\tfrac{1}{2} b h_{\\text{slant}}\\right)',
    volFormula: 'V = \\tfrac{1}{3} b^2 h_{\\perp}',
    defaultDims: { s: 4, l: 4, b: 4, h: 4 },
    description: '1 square base with 4 triangular faces meeting at the apex.',
  },
  tetrahedron: {
    name: 'Tetrahedron (Triangular Pyramid)',
    faces: 4,
    vertices: 4,
    edges: 6,
    formula: 'F(4) + V(4) - E(6) = 2',
    saFormula: 'TSA = \\sqrt{3}\\, s^2',
    volFormula: 'V = \\frac{s^3}{6\\sqrt{2}}',
    defaultDims: { s: 4, l: 4, b: 4, h: 4 },
    description: '4 equilateral triangular faces. Platonic solid.',
  },
};

export default function GeometricNets3DViewer({
  defaultShape = 'cube',
  activeQuestion = null,
  grade = null,
  onFoldComplete = () => {},
}) {
  const inferredShape = useMemo(() => {
    const qTxt = `${activeQuestion?.question_text || ''} ${activeQuestion?.prompt || ''} ${activeQuestion?.archetype || ''}`.toLowerCase();
    if (qTxt.includes('triangular prism')) return 'triangular_prism';
    if (qTxt.includes('rectangular prism') || qTxt.includes('cuboid')) return 'rectangular_prism';
    if (qTxt.includes('square pyramid') || qTxt.includes('square-based pyramid') || qTxt.includes('pyramid')) return 'square_pyramid';
    if (qTxt.includes('tetrahedron') || qTxt.includes('triangular pyramid')) return 'tetrahedron';
    if (qTxt.includes('cube') || qTxt.includes('hexahedron')) return 'cube';
    return defaultShape;
  }, [activeQuestion, defaultShape]);

  const [activeShape, setActiveShape] = useState(inferredShape);
  React.useEffect(() => {
    setActiveShape(inferredShape);
  }, [inferredShape]);
  const isGrade7 = Number(grade) === 7 || Number(activeQuestion?.grade) === 7;
  const [foldProgress, setFoldProgress] = useState(0.55); // 0 = 2D flat net, 1 = 3D folded solid
  const [scaleDim, setScaleDim] = useState(4.0); // side length in cm
  const [selectedCalcId, setSelectedCalcId] = useState('surface_area');

  const shapeData = POLYHEDRA[activeShape] || POLYHEDRA.cube;

  const mensurationMath = useMemo(() => {
    const s = scaleDim;
    const l = s * 1.4;
    const b = s;
    const h = s * 0.85;

    let tsa = 6 * s * s;
    let vol = s * s * s;
    let saSub = `6(${s.toFixed(1)})^2`;
    let volSub = `(${s.toFixed(1)})^3`;

    if (activeShape === 'rectangular_prism') {
      tsa = 2 * (l * b + l * h + b * h);
      vol = l * b * h;
      saSub = `2((${l.toFixed(1)})(${b.toFixed(1)}) + (${l.toFixed(1)})(${h.toFixed(1)}) + (${b.toFixed(1)})(${h.toFixed(1)}))`;
      volSub = `(${l.toFixed(1)})(${b.toFixed(1)})(${h.toFixed(1)})`;
    } else if (activeShape === 'triangular_prism') {
      const triH = (Math.sqrt(3) / 2) * b;
      const baseArea = 0.5 * b * triH;
      tsa = 2 * baseArea + 3 * b * l;
      vol = baseArea * l;
      saSub = `2(${baseArea.toFixed(1)}) + 3(${b.toFixed(1)})(${l.toFixed(1)})`;
      volSub = `(${baseArea.toFixed(1)})(${l.toFixed(1)})`;
    } else if (activeShape === 'square_pyramid') {
      const slant = Math.sqrt((b / 2) * (b / 2) + h * h);
      tsa = b * b + 2 * b * slant;
      vol = (1 / 3) * b * b * h;
      saSub = `(${b.toFixed(1)})^2 + 4(\\tfrac{1}{2})(${b.toFixed(1)})(${slant.toFixed(2)})`;
      volSub = `\\tfrac{1}{3}(${b.toFixed(1)})^2(${h.toFixed(1)})`;
    } else if (activeShape === 'tetrahedron') {
      tsa = Math.sqrt(3) * s * s;
      vol = (s * s * s) / (6 * Math.sqrt(2));
      saSub = `\\sqrt{3}(${s.toFixed(1)})^2`;
      volSub = `\\frac{(${s.toFixed(1)})^3}{6\\sqrt{2}}`;
    }

    return { s, l, b, h, tsa, vol, saSub, volSub };
  }, [activeShape, scaleDim]);

  const calculationsMap = useMemo(() => {
    const { tsa, vol, saSub, volSub } = mensurationMath;
    return {
      surface_area: {
        id: 'surface_area',
        symbol: 'TSA',
        label: `${shapeData.name} — Total Surface Area (Sum of 2D Net Faces)`,
        color: '#2B5B84',
        badgeText: `TSA = ${tsa.toFixed(1)} cm²`,
        formula: shapeData.saFormula,
        substitution: `TSA = ${saSub}`,
        result: `TSA = ${tsa.toFixed(2)}\\text{ cm}^2 \\text{ (${shapeData.faces} faces)}`,
        meaning: `Unfolding the 3D solid flat (0%) proves that Total Surface Area is simply the sum of the areas of all ${shapeData.faces} individual 2D faces in the net.`,
      },
      volume_calc: {
        id: 'volume_calc',
        symbol: 'V',
        label: `${shapeData.name} — Enclosed 3D Volume`,
        color: '#D97706',
        badgeText: `V = ${vol.toFixed(1)} cm³`,
        formula: shapeData.volFormula,
        substitution: `V = ${volSub}`,
        result: `V = ${vol.toFixed(2)}\\text{ cm}^3`,
        meaning: `Folding the net to 100% encloses 3D space. Notice Euler's Polyhedron Theorem holds throughout: ${shapeData.formula}.`,
      },
    };
  }, [mensurationMath, shapeData]);

  const activeCalculation = calculationsMap[selectedCalcId] || calculationsMap.surface_area;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    const w = activeShape === 'rectangular_prism' ? 1.35 : 1.05;
    const d = 1.05;
    const h = activeShape === 'rectangular_prism' ? 0.85 : 1.05;
    const foldRad = foldProgress * (Math.PI / 2);

    const makeFacePlate = (fw, fd, colorHex, interactiveId = 'surface_area') => {
      const geo = new THREE.BoxGeometry(fw, 0.04, fd);
      const mesh = new THREE.Mesh(geo, createPaperMaterial(colorHex, { opacity: 0.92, transparent: true }));
      addInkEdges(mesh, 0x1E1B18, 0.85);
      mesh.userData = { interactiveId };
      return mesh;
    };

    if (activeShape === 'cube' || activeShape === 'rectangular_prism') {
      // Softened pastel textbook palette (#93C5FD, #BFDBFE, #C7D2FE, #A7F3D0, #FDE68A, #FECACA)
      const base = makeFacePlate(w, d, 0x60A5FA, 'surface_area');
      base.position.set(0, 0.02, 0);
      root.add(base);

      // Front hinge (+z edge)
      const frontPivot = new THREE.Group();
      frontPivot.position.set(0, 0.02, d / 2);
      frontPivot.rotation.x = -foldRad;
      const frontFace = makeFacePlate(w, h, 0x93C5FD, 'surface_area');
      frontFace.position.set(0, 0, h / 2);
      frontPivot.add(frontFace);
      root.add(frontPivot);

      // Back hinge (-z edge)
      const backPivot = new THREE.Group();
      backPivot.position.set(0, 0.02, -d / 2);
      backPivot.rotation.x = foldRad;
      const backFace = makeFacePlate(w, h, 0xA5B4FC, 'surface_area');
      backFace.position.set(0, 0, -h / 2);
      backPivot.add(backFace);
      root.add(backPivot);

      // Left hinge (-x edge)
      const leftPivot = new THREE.Group();
      leftPivot.position.set(-w / 2, 0.02, 0);
      leftPivot.rotation.z = -foldRad;
      const leftFace = makeFacePlate(h, d, 0x6EE7B7, 'volume_calc');
      leftFace.position.set(-h / 2, 0, 0);
      leftPivot.add(leftFace);
      root.add(leftPivot);

      // Right hinge (+x edge) + Top lid hinged to Right face
      const rightPivot = new THREE.Group();
      rightPivot.position.set(w / 2, 0.02, 0);
      rightPivot.rotation.z = foldRad;
      const rightFace = makeFacePlate(h, d, 0xFCD34D, 'volume_calc');
      rightFace.position.set(h / 2, 0, 0);
      rightPivot.add(rightFace);

      const topPivot = new THREE.Group();
      topPivot.position.set(h, 0, 0);
      topPivot.rotation.z = foldRad;
      const topFace = makeFacePlate(w, d, 0xFCA5A5, 'volume_calc');
      topFace.position.set(w / 2, 0, 0);
      topPivot.add(topFace);
      rightPivot.add(topPivot);

      root.add(rightPivot);
    } else {
      // Pyramid / Prism hinged triangular flaps (softened palette)
      const base = makeFacePlate(1.2, 1.2, 0x60A5FA, 'surface_area');
      base.position.set(0, 0.02, 0);
      root.add(base);

      const makeTriFlap = (colorHex) => {
        const shape = new THREE.Shape();
        shape.moveTo(-0.6, 0);
        shape.lineTo(0.6, 0);
        shape.lineTo(0, 1.05);
        shape.closePath();
        const geo = new THREE.ShapeGeometry(shape);
        geo.rotateX(Math.PI / 2);
        const mesh = new THREE.Mesh(
          geo,
          createPaperMaterial(colorHex, { side: THREE.DoubleSide, opacity: 0.9, transparent: true })
        );
        addInkEdges(mesh, 0x1E1B18, 0.85);
        mesh.userData = { interactiveId: 'volume_calc' };
        return mesh;
      };

      const maxTilt = activeShape === 'triangular_prism' ? Math.PI / 2 : 1.05;
      const tilt = foldProgress * maxTilt;

      const dirs = [
        { pos: [0, 0.03, 0.6], rotY: 0, color: 0xFCD34D },
        { pos: [0, 0.03, -0.6], rotY: Math.PI, color: 0x6EE7B7 },
        { pos: [0.6, 0.03, 0], rotY: Math.PI / 2, color: 0xFCA5A5 },
        { pos: [-0.6, 0.03, 0], rotY: -Math.PI / 2, color: 0xC4B5FD },
      ];
      dirs.slice(0, activeShape === 'tetrahedron' ? 3 : 4).forEach((cfg) => {
        const pivot = new THREE.Group();
        pivot.position.set(...cfg.pos);
        pivot.rotation.y = cfg.rotY;
        pivot.rotation.x = -tilt;
        pivot.add(makeTriFlap(cfg.color));
        root.add(pivot);
      });
    }

    return { interactiveObjects: [root] };
  }, [activeShape, foldProgress]);

  return (
    <div data-testid="geometric-nets-canvas" className="w-full bg-white text-slate-800 rounded-2xl overflow-hidden border border-slate-200 shadow-sm flex flex-col select-none space-y-3 p-3.5">
      {/* Header & Shape Selector */}
      <div className="flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-blue-50 text-blue-700 border border-blue-200 flex items-center justify-center">
            <Box className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-slate-900 flex items-center gap-1.5">
              3D Hinged Polyhedron Net & Surface Area Unfolder
            </h3>
            <p className="text-[11px] text-slate-500">
              Fold 2D nets into 3D solids • Inspect Surface Area (TSA), Volume (V) & Euler&apos;s Formula
            </p>
          </div>
        </div>

        <div className="flex items-center gap-1 overflow-x-auto scrollbar-none py-1">
          {Object.entries(POLYHEDRA).map(([key, item]) => (
            <button
              key={key}
              data-testid={`btn-net-shape-${key}`}
              onClick={() => setActiveShape(key)}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
                activeShape === key
                  ? 'bg-[#2B5B84] text-white shadow-xs'
                  : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
              }`}
            >
              {item.name.split(' ')[0]}
            </button>
          ))}
        </div>
      </div>

      {/* Fold Slider & Scale Dimension Control */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
        <div className="bg-slate-50 p-2.5 rounded-lg border border-slate-200/80 flex flex-col gap-1">
          <div className="flex items-center justify-between text-xs">
            <span className="font-semibold text-slate-700 flex items-center gap-1">
              <Layers className="w-3.5 h-3.5 text-[#2B5B84]" />
              Hinge Fold Angle:
            </span>
            <div className="flex items-center gap-2 font-mono text-[11px]">
              <button
                type="button"
                data-testid="btn-fold-flat"
                onClick={() => setFoldProgress(0)}
                className="text-slate-500 hover:text-slate-900 underline cursor-pointer"
              >
                Flat 2D (0%)
              </button>
              <span className="text-[#2B5B84] font-bold">{Math.round(foldProgress * 100)}%</span>
              <button
                type="button"
                data-testid="btn-fold-folded"
                onClick={() => {
                  setFoldProgress(1);
                  onFoldComplete(shapeData);
                }}
                className="text-slate-500 hover:text-slate-900 underline cursor-pointer"
              >
                Folded 3D (100%)
              </button>
            </div>
          </div>
          <input
            type="range"
            data-testid="slider-net-fold"
            min="0"
            max="1"
            step="0.01"
            value={foldProgress}
            onChange={(e) => {
              const val = parseFloat(e.target.value);
              setFoldProgress(val);
              if (val >= 0.98) onFoldComplete(shapeData);
            }}
            className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
          />
        </div>

        <label className="bg-slate-50 p-2.5 rounded-lg border border-slate-200/80 flex flex-col gap-1">
          <div className="flex justify-between text-xs font-semibold text-slate-700">
            <span>Base Edge Dimension (s)</span>
            <span className="font-mono font-bold text-amber-700">{scaleDim.toFixed(1)} cm</span>
          </div>
          <input
            type="range"
            min="2"
            max="10"
            step="0.5"
            value={scaleDim}
            onChange={(e) => setScaleDim(parseFloat(e.target.value))}
            className="w-full accent-amber-600 cursor-pointer h-1.5"
          />
        </label>
      </div>

      {/* True Three.js 3D Viewport */}
      <AtlasCanvas3D
        testId="geometric-nets-3d-stage"
        height={290}
        buildScene={buildScene}
        selectedId={selectedCalcId}
        onSelect={(id) => {
          if (id) setSelectedCalcId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Drag the Hinge Fold slider between 0% (Flat 2D Net) and 100% (Closed 3D Solid) • Click faces for TSA & Volume formulas"
      />

      {/* Calculation Popover */}
      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedCalcId}
      />

      {/* Live Faces, Vertices & Edges Inspector (Euler Check hidden for Grade 7 per syllabus) */}
      <div className={`grid grid-cols-3 ${isGrade7 ? '' : 'sm:grid-cols-4'} gap-2 pt-1`}>
        <div className="p-2.5 rounded-xl border bg-slate-50 border-slate-200">
          <div className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Faces (F)</div>
          <div className="text-base font-bold font-mono text-[#2B5B84]">{shapeData.faces}</div>
        </div>
        <div className="p-2.5 rounded-xl border bg-slate-50 border-slate-200">
          <div className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Vertices (V)</div>
          <div className="text-base font-bold font-mono text-emerald-700">{shapeData.vertices}</div>
        </div>
        <div className="p-2.5 rounded-xl border bg-slate-50 border-slate-200">
          <div className="text-[10px] text-slate-500 uppercase tracking-wider font-semibold">Edges (E)</div>
          <div className="text-base font-bold font-mono text-amber-700">{shapeData.edges}</div>
        </div>
        {!isGrade7 && (
          <div className="p-2.5 rounded-xl bg-indigo-50 border border-indigo-200">
            <div className="text-[10px] text-indigo-700 uppercase tracking-wider font-semibold">Euler Check</div>
            <div className="text-xs font-bold font-mono text-indigo-900 pt-0.5">{shapeData.formula}</div>
            <div className="text-[10px] text-emerald-700 flex items-center gap-1">
              <CheckCircle2 className="w-3 h-3 text-emerald-600 inline" /> Valid Solid
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
