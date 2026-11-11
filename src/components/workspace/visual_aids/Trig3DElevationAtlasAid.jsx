import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Compass, Layers } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createBlock3D, createSphereAtom3D } from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

/**
 * Trig3DElevationAtlasAid
 * -----------------------
 * Grade 11–12 Mathematics & Technical Mathematics:
 * 3D Height, Bearing & Inclination Explorer (Tower PQ + Horizontal Ground Triangle PQR).
 *
 * Includes an "Unfold Vertical Triangles Flat" slider so learners can see how the
 * vertical right-angled elevation triangle ΔPQR_top hinges at 90° to the horizontal
 * ground triangle ΔPAB.
 */

export default function Trig3DElevationAtlasAid() {
  const [towerHeight, setTowerHeight] = useState(25.0); // h (m)
  const [alphaDeg, setAlphaDeg] = useState(38); // Angle of elevation from A to top Q
  const [groundAngleDeg, setGroundAngleDeg] = useState(65); // ∠PAB or ∠APB on ground
  const [distAB, setDistAB] = useState(40.0); // baseline AB on ground (m)
  const [unfoldPlanes, setUnfoldPlanes] = useState(false);
  const [selectedId, setSelectedId] = useState('vertical_elevation');

  const trigMath = useMemo(() => {
    const alphaRad = (alphaDeg * Math.PI) / 180;
    const paDist = towerHeight / Math.tan(alphaRad);
    const qaSlant = towerHeight / Math.sin(alphaRad);

    // Cosine rule in ground triangle ΔPAB to find PB given PA, AB, and included angle ∠PAB = groundAngleDeg
    const gammaRad = (groundAngleDeg * Math.PI) / 180;
    const pbSq = paDist * paDist + distAB * distAB - 2 * paDist * distAB * Math.cos(gammaRad);
    const pbDist = Math.sqrt(Math.max(1, pbSq));

    // Area of horizontal ground triangle ΔPAB
    const areaPAB = 0.5 * paDist * distAB * Math.sin(gammaRad);
    // Angle of elevation β from B to top of tower Q
    const betaDeg = (Math.atan(towerHeight / pbDist) * 180) / Math.PI;

    return {
      paDist,
      qaSlant,
      pbDist,
      areaPAB,
      betaDeg,
    };
  }, [towerHeight, alphaDeg, groundAngleDeg, distAB]);

  const calculationsMap = useMemo(() => {
    const { paDist, pbDist, areaPAB, betaDeg } = trigMath;
    return {
      vertical_elevation: {
        id: 'vertical_elevation',
        symbol: '\\triangle QPA (90^\\circ)',
        label: 'Vertical Right-Angled Elevation Triangle (PA Link Edge)',
        color: '#2B5B84',
        badgeText: `PA = ${paDist.toFixed(1)} m`,
        formula: '\\tan\\alpha = \\frac{h}{PA} \\implies PA = \\frac{h}{\\tan\\alpha}',
        substitution: `PA = \\frac{${towerHeight.toFixed(1)}}{\\tan(${alphaDeg}^\\circ)} = \\frac{${towerHeight.toFixed(1)}}{${Math.tan((alphaDeg * Math.PI) / 180).toFixed(3)}}`,
        result: `PA = ${paDist.toFixed(2)}\\text{ m (shared edge between vertical & horizontal planes)}`,
        meaning: 'Side PA is the bridge between the vertical right-angled triangle ΔQPA and the horizontal ground triangle ΔPAB.',
      },
      ground_cosine: {
        id: 'ground_cosine',
        symbol: '\\triangle PAB (\\text{Cosine Rule})',
        label: 'Horizontal Ground Bearing Triangle (Cosine & Sine Rules)',
        color: '#D97706',
        badgeText: `PB = ${pbDist.toFixed(1)} m`,
        formula: 'PB^2 = PA^2 + AB^2 - 2(PA)(AB)\\cos(\\angle PAB)',
        substitution: `PB^2 = (${paDist.toFixed(1)})^2 + (${distAB.toFixed(1)})^2 - 2(${paDist.toFixed(1)})(${distAB.toFixed(1)})\\cos(${groundAngleDeg}^\\circ)`,
        result: `PB = ${pbDist.toFixed(2)}\\text{ m} \\implies \\beta = \\arctan\\!\\left(\\frac{h}{PB}\\right) = ${betaDeg.toFixed(1)}^\\circ`,
        meaning: 'In 3D trigonometry, you NEVER apply SOHCAHTOA inside the oblique horizontal ground triangle ΔPAB—use the Sine or Cosine Rule there!',
      },
      ground_area: {
        id: 'ground_area',
        symbol: '\\text{Area}(\\triangle PAB)',
        label: 'Area Rule in Horizontal Ground Plane',
        color: '#2D6A4F',
        badgeText: `Area = ${areaPAB.toFixed(0)} m²`,
        formula: '\\text{Area}(\\triangle PAB) = \\tfrac{1}{2}(PA)(AB)\\sin(\\angle PAB)',
        substitution: `\\text{Area} = \\tfrac{1}{2}(${paDist.toFixed(1)})(${distAB.toFixed(1)})\\sin(${groundAngleDeg}^\\circ)`,
        result: `\\text{Area}(\\triangle PAB) = ${areaPAB.toFixed(1)}\\text{ m}^2`,
        meaning: 'The Area Rule uses two sides and the included angle in the horizontal plane.',
      },
    };
  }, [trigMath, towerHeight, alphaDeg, distAB, groundAngleDeg]);

  const activeCalculation = calculationsMap[selectedId] || calculationsMap.vertical_elevation;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    // Coordinates in 3D space:
    // P (base of tower) at (-1.2, 0, -0.8)
    // Q (top of tower) at (-1.2, h3d, -0.8)
    // A (observer 1) at (1.3, 0, -0.4)
    // B (observer 2) at (0.3, 0, 1.35)
    const h3d = Math.min(2.2, Math.max(0.9, towerHeight * 0.055));
    const pPt = new THREE.Vector3(-1.25, 0.02, -0.75);
    const aPt = new THREE.Vector3(1.35, 0.02, -0.35);
    const bPt = new THREE.Vector3(0.15, 0.02, 1.35);

    // Ground triangle ΔPAB
    const groundShape = new THREE.Shape();
    groundShape.moveTo(pPt.x, -pPt.z);
    groundShape.lineTo(aPt.x, -aPt.z);
    groundShape.lineTo(bPt.x, -bPt.z);
    groundShape.closePath();
    const groundGeo = new THREE.ShapeGeometry(groundShape);
    groundGeo.rotateX(-Math.PI / 2);
    const groundMesh = new THREE.Mesh(
      groundGeo,
      createPaperMaterial(0xD97706, { opacity: 0.38, transparent: true, side: THREE.DoubleSide })
    );
    addInkEdges(groundMesh, 0xD97706, 0.85);
    groundMesh.position.y = 0.02;
    groundMesh.userData = { interactiveId: 'ground_cosine', labelPoint: [0.1, 0.15, 0.25] };
    root.add(groundMesh);

    // Vertical Elevation Triangle ΔQPA hinged along edge PA
    const paVec = new THREE.Vector3().subVectors(aPt, pPt);
    const paLen = paVec.length();
    const paAngle = Math.atan2(paVec.z, paVec.x);

    const vertPivot = new THREE.Group();
    vertPivot.position.copy(pPt);
    vertPivot.rotation.y = -paAngle;
    if (unfoldPlanes) {
      vertPivot.rotation.x = -Math.PI / 2;
    }

    const vShape = new THREE.Shape();
    vShape.moveTo(0, 0);
    vShape.lineTo(paLen, 0);
    vShape.lineTo(0, h3d);
    vShape.closePath();
    const vGeo = new THREE.ShapeGeometry(vShape);
    const vMesh = new THREE.Mesh(
      vGeo,
      createPaperMaterial(0x2B5B84, { opacity: 0.45, transparent: true, side: THREE.DoubleSide })
    );
    addInkEdges(vMesh, 0x2B5B84, 0.9);
    vMesh.userData = { interactiveId: 'vertical_elevation', labelPoint: [paLen * 0.35, h3d * 0.45, 0] };
    vertPivot.add(vMesh);

    // Tower pillar along PQ
    const towerPillar = createBlock3D({
      width: 0.14,
      height: h3d,
      depth: 0.14,
      color: 0x1E1B18,
      interactiveId: 'vertical_elevation',
    });
    towerPillar.position.set(0, h3d / 2, 0);
    vertPivot.add(towerPillar);

    root.add(vertPivot);

    // Vertex markers P, A, B
    [
      { p: pPt, c: 0x1E1B18, id: 'vertical_elevation' },
      { p: aPt, c: 0x2B5B84, id: 'vertical_elevation' },
      { p: bPt, c: 0x2D6A4F, id: 'ground_area' },
    ].forEach((v) => {
      const m = createSphereAtom3D({ radius: 0.09, color: v.c, interactiveId: v.id });
      m.position.copy(v.p);
      root.add(m);
    });

    return { interactiveObjects: [root] };
  }, [towerHeight, unfoldPlanes]);

  return (
    <div data-testid="trig-3d-elevation-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-indigo-100 text-indigo-900 uppercase tracking-wider">
              Grade 12 3D Trigonometry
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              3D Vertical Elevation (<span className="font-mono">ΔQPA</span>) & Horizontal Ground Plane (<span className="font-mono">ΔPAB</span>)
            </h4>
          </div>

          <button
            type="button"
            data-testid="btn-unfold-3d-trig"
            onClick={() => setUnfoldPlanes((v) => !v)}
            className={`px-3 py-1 rounded-lg text-xs font-semibold border transition-all flex items-center gap-1.5 ${
              unfoldPlanes
                ? 'bg-indigo-600 border-indigo-600 text-white'
                : 'bg-slate-100 border-slate-200 text-slate-700 hover:bg-slate-200'
            }`}
          >
            <Layers className="w-3.5 h-3.5" />
            {unfoldPlanes ? 'Planes Unfolded Flat (2D Net)' : 'Unfold Vertical Triangle Flat'}
          </button>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5">
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Tower Height (h)</span>
              <span className="font-mono font-bold text-[#2B5B84]">{towerHeight.toFixed(0)} m</span>
            </div>
            <input
              type="range"
              min="10"
              max="45"
              step="1"
              value={towerHeight}
              onChange={(e) => setTowerHeight(parseFloat(e.target.value))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Elevation (α)</span>
              <span className="font-mono font-bold text-[#2B5B84]">{alphaDeg}°</span>
            </div>
            <input
              type="range"
              min="20"
              max="65"
              step="1"
              value={alphaDeg}
              onChange={(e) => setAlphaDeg(parseInt(e.target.value, 10))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Ground ∠PAB</span>
              <span className="font-mono font-bold text-amber-700">{groundAngleDeg}°</span>
            </div>
            <input
              type="range"
              min="30"
              max="120"
              step="5"
              value={groundAngleDeg}
              onChange={(e) => setGroundAngleDeg(parseInt(e.target.value, 10))}
              className="w-full accent-amber-600 cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Baseline AB</span>
              <span className="font-mono font-bold text-emerald-700">{distAB.toFixed(0)} m</span>
            </div>
            <input
              type="range"
              min="20"
              max="70"
              step="2"
              value={distAB}
              onChange={(e) => setDistAB(parseFloat(e.target.value))}
              className="w-full accent-emerald-600 cursor-pointer h-1.5"
            />
          </label>
        </div>
      </div>

      <AtlasCanvas3D
        testId="trig-3d-elevation-canvas"
        height={300}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Click the blue vertical elevation plane (ΔQPA) or amber horizontal ground triangle (ΔPAB) to trace the shared edge PA"
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />
    </div>
  );
}
