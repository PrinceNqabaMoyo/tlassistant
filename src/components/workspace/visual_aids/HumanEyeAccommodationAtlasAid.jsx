import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Eye, Sun } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import { createSphereAtom3D } from '../shared/atlas3d/atlasPartsKit';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';

/**
 * HumanEyeAccommodationAtlasAid
 * -----------------------------
 * Grade 12 Life Sciences (Responding to the Environment — The Human Eye):
 * 1. Visual Accommodation (Object Distance 6.0 m -> 0.20 m):
 *    Shows Ciliary Muscle ring contracting, Suspensory Ligaments slackening,
 *    and the elastic Crystalline Lens bulging more convex (shorter focal length f)
 *    to keep light rays focused sharply on the yellow spot (fovea) of the retina.
 * 2. Pupillary Mechanism (Dim vs. Bright Light):
 *    Shows antagonistic Radial & Circular Iris muscles regulating pupil aperture.
 */

export default function HumanEyeAccommodationAtlasAid() {
  const [objectDistM, setObjectDistM] = useState(0.35); // 0.20 m (Near) to 6.0 m (Distant)
  const [lightIntensity, setLightIntensity] = useState(50); // 0 (Dim) to 100 (Bright)
  const [selectedId, setSelectedId] = useState('lens_convexity');

  // Near factor: 1.0 when objectDistM = 0.20 m, 0.0 when objectDistM >= 6.0 m
  const nearFactor = Math.max(0, Math.min(1, (6.0 - objectDistM) / 5.8));
  // Lens focal length in mm (approx 22.0 mm for distant vision, 15.5 mm for 20 cm near vision)
  const focalLengthMm = 22.0 - nearFactor * 6.5;
  const dioptres = 1000 / focalLengthMm;
  const pupilDiameterMm = 7.5 - (lightIntensity / 100) * 5.3;

  const calculationsMap = useMemo(() => {
    const isNear = objectDistM < 1.5;
    return {
      lens_convexity: {
        id: 'lens_convexity',
        symbol: '\\frac{1}{f} = \\frac{1}{d_o} + \\frac{1}{d_i}',
        label: isNear
          ? `Near Vision Accommodation (d_o = ${objectDistM.toFixed(2)} m < 6 m)`
          : `Distant Vision Relaxed State (d_o = ${objectDistM.toFixed(2)} m)`,
        color: '#2B5B84',
        badgeText: `f = ${focalLengthMm.toFixed(1)} mm (${dioptres.toFixed(0)} D)`,
        formula: '\\text{Ciliary Muscle} \\to \\text{Suspensory Ligaments} \\to \\text{Lens Convexity } (1/f)',
        substitution: isNear
          ? '\\text{Ciliary muscles CONTRACT} \\implies \\text{Suspensory ligaments SLACKEN} \\implies \\text{Lens bulges MORE CONVEX}'
          : '\\text{Ciliary muscles RELAX} \\implies \\text{Suspensory ligaments TAUT} \\implies \\text{Lens pulled THIN / LESS CONVEX}',
        result: `f = ${focalLengthMm.toFixed(1)}\\text{ mm (Refractive Power } P = ${dioptres.toFixed(1)}\\text{ D)}`,
        meaning: isNear
          ? 'Diverging rays from a nearby object (< 6 m) require stronger refraction. Contracting the sphincter-like ciliary ring moves it inward toward the lens, releasing tension on the suspensory ligaments so the elastic lens rounds up.'
          : 'Parallel rays from a distant object (> 6 m) require less refraction. Relaxed ciliary muscles pull the suspensory ligaments taut, flattening the lens.',
      },
      pupillary_reflex: {
        id: 'pupillary_reflex',
        symbol: `d_{\\text{pupil}} = ${pupilDiameterMm.toFixed(1)}\\text{ mm}`,
        label: lightIntensity > 55 ? 'Bright Light (Pupil Constriction)' : 'Dim Light (Pupil Dilation)',
        color: '#D97706',
        badgeText: `Pupil = ${pupilDiameterMm.toFixed(1)} mm`,
        formula: lightIntensity > 55
          ? '\\text{Circular Iris Muscles CONTRACT} + \\text{Radial Muscles RELAX} \\implies \\text{Pupil Constricts}'
          : '\\text{Radial Iris Muscles CONTRACT} + \\text{Circular Muscles RELAX} \\implies \\text{Pupil Dilates}',
        substitution: `\\text{Light Intensity} = ${lightIntensity}\\% \\implies d_{\\text{pupil}} = ${pupilDiameterMm.toFixed(1)}\\text{ mm}`,
        result: lightIntensity > 55 ? '\\text{Protects photoreceptors from bright glare}' : '\\text{Admits maximum light in dim conditions}',
        meaning: 'The iris contains antagonistic circular and radial smooth muscle fibres that reflexively control the amount of light entering the eye.',
      },
    };
  }, [dioptres, focalLengthMm, lightIntensity, objectDistM, pupilDiameterMm]);

  const activeCalculation = calculationsMap[selectedId] || calculationsMap.lens_convexity;

  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    // 1. Cutaway Sclera/Retina Hemisphere at right (x = +1.35)
    const eyeSphereGeo = new THREE.SphereGeometry(1.15, 28, 20, -Math.PI * 0.45, Math.PI * 0.9);
    const eyeSphere = new THREE.Mesh(
      eyeSphereGeo,
      createPaperMaterial(0xF8FAFC, { opacity: 0.35, transparent: true, side: THREE.DoubleSide })
    );
    addInkEdges(eyeSphere, 0x64748B, 0.45);
    eyeSphere.position.set(0.65, 1.0, 0);
    root.add(eyeSphere);

    // 2. Ciliary Body Ring at x = 0.05 (contracts inward when nearFactor increases)
    const ciliaryRadius = 0.88 - nearFactor * 0.14;
    const ciliaryGeo = new THREE.TorusGeometry(ciliaryRadius, 0.08, 14, 36);
    ciliaryGeo.rotateY(Math.PI / 2);
    const ciliaryMesh = new THREE.Mesh(ciliaryGeo, createPaperMaterial(0xB8432E));
    addInkEdges(ciliaryMesh, 0x1E1B18, 0.7);
    ciliaryMesh.position.set(0.05, 1.0, 0);
    ciliaryMesh.userData = { interactiveId: 'lens_convexity', labelPoint: [0.05, 1.85, 0] };
    root.add(ciliaryMesh);

    // 3. Elastic Biconvex Crystalline Lens (thickens along x when nearFactor increases)
    const lensThicknessScale = 0.28 + nearFactor * 0.34;
    const lensRadius = 0.56 - nearFactor * 0.05;
    const lensGeo = new THREE.SphereGeometry(lensRadius, 24, 20);
    lensGeo.scale(lensThicknessScale, 1, 1);
    const lensMesh = new THREE.Mesh(
      lensGeo,
      createPaperMaterial(0x38BDF8, { opacity: 0.78, transparent: true })
    );
    addInkEdges(lensMesh, 0x2B5B84, 0.8);
    lensMesh.position.set(0.05, 1.0, 0);
    lensMesh.userData = { interactiveId: 'lens_convexity' };
    root.add(lensMesh);

    // 4. Iris & Pupil Ring slightly in front of lens (x = -0.32)
    const pupilRadius = 0.14 + ((100 - lightIntensity) / 100) * 0.28;
    const irisGeo = new THREE.RingGeometry(pupilRadius, 0.58, 32);
    irisGeo.rotateY(Math.PI / 2);
    const irisMesh = new THREE.Mesh(
      irisGeo,
      createPaperMaterial(0xD97706, { side: THREE.DoubleSide })
    );
    addInkEdges(irisMesh, 0x1E1B18, 0.7);
    irisMesh.position.set(-0.32, 1.0, 0);
    irisMesh.userData = { interactiveId: 'pupillary_reflex', labelPoint: [-0.32, 1.65, 0] };
    root.add(irisMesh);

    // 5. Light Rays from Object -> Lens -> Retina Fovea (x = +1.78, y = 1.0)
    const objX = -2.2 + nearFactor * 1.15;
    const objSphere = createSphereAtom3D({
      radius: 0.14,
      color: 0x2D6A4F,
      interactiveId: 'lens_convexity',
    });
    objSphere.position.set(objX, 1.0, 0);
    root.add(objSphere);

    const rayMat = new THREE.LineBasicMaterial({ color: 0xD97706, linewidth: 2 });
    [-0.32, 0.32].forEach((yOff) => {
      const pts = [
        new THREE.Vector3(objX, 1.0, 0),
        new THREE.Vector3(0.05, 1.0 + yOff, 0),
        new THREE.Vector3(1.78, 1.0, 0),
      ];
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(pts), rayMat));
    });

    // Fovea / Yellow Spot marker on retina
    const fovea = createSphereAtom3D({ radius: 0.09, color: 0xB8432E, interactiveId: 'lens_convexity' });
    fovea.position.set(1.78, 1.0, 0);
    root.add(fovea);

    return { interactiveObjects: [root] };
  }, [lightIntensity, nearFactor]);

  return (
    <div data-testid="human-eye-accommodation-atlas-aid" className="space-y-4 text-slate-800">
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-sky-100 text-sky-900 uppercase tracking-wider">
              Grade 12 Life Sciences • The Human Eye
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              3D Visual Accommodation (Lens Curvature) & Pupillary Reflex Explorer
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-eye-near"
              onClick={() => {
                setObjectDistM(0.25);
                setSelectedId('lens_convexity');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold ${
                objectDistM < 1.5 ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              Near Vision (&lt; 6 m)
            </button>
            <button
              type="button"
              data-testid="btn-eye-distant"
              onClick={() => {
                setObjectDistM(6.0);
                setSelectedId('lens_convexity');
              }}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold ${
                objectDistM >= 1.5 ? 'bg-[#2B5B84] text-white' : 'bg-slate-100 text-slate-600'
              }`}
            >
              Distant Vision (&ge; 6 m)
            </button>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-2.5">
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span className="flex items-center gap-1">
                <Eye className="w-3.5 h-3.5 text-[#2B5B84]" />
                Object Distance (d_o)
              </span>
              <span className="font-mono font-bold text-[#2B5B84]">
                {objectDistM.toFixed(2)} m ({objectDistM < 1.5 ? 'Lens Bulges Convex' : 'Lens Flat/Thin'})
              </span>
            </div>
            <input
              type="range"
              min="0.20"
              max="6.00"
              step="0.10"
              value={objectDistM}
              onChange={(e) => {
                setObjectDistM(parseFloat(e.target.value));
                setSelectedId('lens_convexity');
              }}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-xs font-semibold text-slate-700">
              <span className="flex items-center gap-1">
                <Sun className="w-3.5 h-3.5 text-amber-600" />
                Ambient Light Intensity
              </span>
              <span className="font-mono font-bold text-amber-700">
                {lightIntensity}% (Pupil {pupilDiameterMm.toFixed(1)} mm)
              </span>
            </div>
            <input
              type="range"
              min="5"
              max="100"
              step="5"
              value={lightIntensity}
              onChange={(e) => {
                setLightIntensity(parseInt(e.target.value, 10));
                setSelectedId('pupillary_reflex');
              }}
              className="w-full accent-amber-600 cursor-pointer h-1.5"
            />
          </label>
        </div>
      </div>

      <AtlasCanvas3D
        testId="human-eye-accommodation-3d-canvas"
        height={290}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Drag Object Distance from 6.0 m to 0.20 m to watch the Ciliary Ring contract inward & the Crystalline Lens thicken"
      />

      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />
    </div>
  );
}
