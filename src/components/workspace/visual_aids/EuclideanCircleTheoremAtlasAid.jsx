import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Layers, CircleDot } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createSphereAtom3D } from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

/**
 * EuclideanCircleTheoremAtlasAid
 * ------------------------------
 * Grade 11–12 Mathematics:
 * 3D-Layered Euclidean Circle Theorem Proof Unfolder.
 *
 * Separates overlapping circle-theorem triangles (e.g., Isosceles ΔOAP and ΔOBP
 * for "Angle at Centre = 2 × Angle at Circumference", or Tangent-Chord Theorem)
 * along the vertical z/y height axis so learners can visually isolate radii OA = OB = OP = r
 * and exterior angle steps without visual clutter.
 */

export default function EuclideanCircleTheoremAtlasAid() {
  const [theorem, setTheorem] = useState('angle_at_centre'); // 'angle_at_centre' | 'tan_chord'
  const [circumAngleDeg, setCircumAngleDeg] = useState(52);
  const [explodeLayers, setExplodeLayers] = useState(true);
  const [selectedId, setSelectedId] = useState('centre_double');

  const x1 = Math.round(circumAngleDeg * 0.55);
  const x2 = circumAngleDeg - x1;
  const centreAngle = 2 * circumAngleDeg;

  const calculationsMap = useMemo(() => {
    if (theorem === 'tan_chord') {
      return {
        tan_chord_proof: {
          id: 'tan_chord_proof',
          symbol: '\\angle\\text{ between tangent \\& chord}',
          label: 'Tan-Chord Theorem (⊥ Radius + Angle in Semi-Circle)',
          color: '#2B5B84',
          badgeText: `∠PTB = ∠PAB = ${circumAngleDeg}°`,
          formula: 'OT \\perp \\text{Tangent } (90^\\circ) \\implies \\angle PTB = 90^\\circ - \\angle OTP = \\angle PAB',
          substitution: `\\angle PTB = ${circumAngleDeg}^\\circ = \\angle\\text{ subtended by chord } PB \\text{ in alternate segment}`,
          result: `\\angle_{\\text{tan-chord}} = \\angle_{\\text{alt segment}} = ${circumAngleDeg}^\\circ`,
          meaning: 'By elevating the radius-tangent 90° right angle above the chord-subtended triangle, you see immediately why the complement equals the angle in the alternate segment.',
        },
      };
    }

    return {
      centre_double: {
        id: 'centre_double',
        symbol: '\\angle AOB = 2 \\angle APB',
        label: 'Angle at Centre = 2 × Angle at Circumference',
        color: '#2B5B84',
        badgeText: `∠AOB = ${centreAngle}°`,
        formula: '\\angle AOB = 2x_1 + 2x_2 = 2(x_1 + x_2) = 2\\,\\angle APB',
        substitution: `\\angle AOB = 2(${x1}^\\circ) + 2(${x2}^\\circ) = 2(${circumAngleDeg}^\\circ)`,
        result: `\\angle AOB = ${centreAngle}^\\circ,\\quad \\angle APB = ${circumAngleDeg}^\\circ`,
        meaning: 'Drawing auxiliary radius PO splits ΔAPB into two isosceles triangles (ΔOAP and ΔOBP) because OA = OP = OB = r (radii).',
      },
      isosceles_radii: {
        id: 'isosceles_radii',
        symbol: 'OA = OP = OB = r',
        label: 'Isosceles Radius Triangles (ΔOAP & ΔOBP) + Exterior Angle',
        color: '#D97706',
        badgeText: `x₁=${x1}°, x₂=${x2}°`,
        formula: 'OA = OP \\text{ (radii)} \\implies \\angle OAP = \\angle OPA = x_1,\\quad \\text{ext } \\angle AOD = 2x_1',
        substitution: `\\text{Ext } \\angle AOD = ${x1}^\\circ + ${x1}^\\circ = ${2 * x1}^\\circ,\\quad \\text{Ext } \\angle BOD = ${2 * x2}^\\circ`,
        result: `\\angle AOB = ${2 * x1}^\\circ + ${2 * x2}^\\circ = ${centreAngle}^\\circ`,
        meaning: 'Exploding the two isosceles triangles vertically in 3D makes the equal radii OA = OP = OB and exterior angle addition crystal clear.',
      },
    };
  }, [centreAngle, circumAngleDeg, theorem, x1, x2]);

  const activeCalculation = calculationsMap[selectedId] || Object.values(calculationsMap)[0];

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    const R = 1.45;
    // Base Circle Ring at y = 0.04
    const ringGeo = new THREE.TorusGeometry(R, 0.025, 12, 64);
    ringGeo.rotateX(Math.PI / 2);
    const ringMesh = new THREE.Mesh(ringGeo, new THREE.MeshBasicMaterial({ color: 0x1E1B18 }));
    ringMesh.position.set(0, 0.04, 0);
    root.add(ringMesh);

    // Points O (0,0), P (top circumference), A (bottom-left), B (bottom-right)
    const ptO = new THREE.Vector3(0, 0.04, 0);
    const ptP = new THREE.Vector3(0, 0.04, -R);
    const ptA = new THREE.Vector3(-R * Math.sin(1.05), 0.04, R * Math.cos(1.05));
    const ptB = new THREE.Vector3(R * Math.sin(1.05), 0.04, R * Math.cos(1.05));

    const makeTriLayer = (p1, p2, p3, yLift, colorHex, interactiveId) => {
      const shape = new THREE.Shape();
      shape.moveTo(p1.x, -p1.z);
      shape.lineTo(p2.x, -p2.z);
      shape.lineTo(p3.x, -p3.z);
      shape.closePath();
      const geo = new THREE.ShapeGeometry(shape);
      geo.rotateX(-Math.PI / 2);
      const mesh = new THREE.Mesh(
        geo,
        createPaperMaterial(colorHex, { opacity: 0.55, transparent: true, side: THREE.DoubleSide })
      );
      addInkEdges(mesh, colorHex, 0.9);
      mesh.position.y = yLift;
      mesh.userData = {
        interactiveId,
        labelPoint: [(p1.x + p2.x + p3.x) / 3, yLift + 0.12, (p1.z + p2.z + p3.z) / 3],
      };
      return mesh;
    };

    const lift1 = explodeLayers ? 0.38 : 0.06;
    const lift2 = explodeLayers ? 0.72 : 0.08;

    if (theorem === 'angle_at_centre') {
      // Base Centre Triangle ΔOAB
      root.add(makeTriLayer(ptO, ptA, ptB, 0.05, 0x2B5B84, 'centre_double'));
      // Left Isosceles ΔOAP lifted to lift1
      root.add(makeTriLayer(ptO, ptA, ptP, lift1, 0xD97706, 'isosceles_radii'));
      // Right Isosceles ΔOBP lifted to lift2
      root.add(makeTriLayer(ptO, ptB, ptP, lift2, 0x2D6A4F, 'isosceles_radii'));
    } else {
      // Tan-Chord Theorem layer + tangent line at B
      root.add(makeTriLayer(ptP, ptA, ptB, 0.06, 0x2B5B84, 'tan_chord_proof'));
      root.add(makeTriLayer(ptO, ptP, ptB, lift1, 0xD97706, 'tan_chord_proof'));
    }

    [ptO, ptP, ptA, ptB].forEach((p) => {
      const s = createSphereAtom3D({ radius: 0.08, color: 0x1E1B18, interactiveId: Object.keys(calculationsMap)[0] });
      s.position.copy(p);
      root.add(s);
    });

    return { interactiveObjects: [root] };
  }, [calculationsMap, explodeLayers, theorem]);

  return (
    <div data-testid="euclidean-circle-theorem-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-amber-100 text-amber-900 uppercase tracking-wider">
              3D Euclidean Proof Deconstruction
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              Circle Geometry Proof Unfolder (Isolating Overlapping Radii & Triangles)
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-thm-centre"
              onClick={() => {
                setTheorem('angle_at_centre');
                setSelectedId('centre_double');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold ${
                theorem === 'angle_at_centre' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              ∠ at Centre = 2× ∠ at Circum
            </button>
            <button
              type="button"
              data-testid="btn-thm-tanchord"
              onClick={() => {
                setTheorem('tan_chord');
                setSelectedId('tan_chord_proof');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold ${
                theorem === 'tan_chord' ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              Tan-Chord Theorem
            </button>
            <button
              type="button"
              data-testid="btn-explode-proof-layers"
              onClick={() => setExplodeLayers((v) => !v)}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold border flex items-center gap-1 ${
                explodeLayers
                  ? 'bg-amber-50 border-amber-300 text-amber-900'
                  : 'bg-white border-slate-200 text-slate-600'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              {explodeLayers ? '3D Layers Exploded' : 'Collapsed 2D View'}
            </button>
          </div>
        </div>

        <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
          <div className="flex justify-between text-xs font-semibold text-slate-700">
            <span>Subtended Circumference Angle (∠APB)</span>
            <span className="font-mono font-bold text-[#2B5B84]">
              {circumAngleDeg}° (Centre ∠AOB = {centreAngle}°)
            </span>
          </div>
          <input
            type="range"
            min="30"
            max="80"
            step="2"
            value={circumAngleDeg}
            onChange={(e) => setCircumAngleDeg(parseInt(e.target.value, 10))}
            className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
          />
        </label>
      </div>

      <AtlasCanvas3D
        testId="euclidean-circle-theorem-canvas"
        height={290}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Orbit in 3D to see how the auxiliary radius OP splits ∠APB into two elevated isosceles radius triangles"
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />
    </div>
  );
}
