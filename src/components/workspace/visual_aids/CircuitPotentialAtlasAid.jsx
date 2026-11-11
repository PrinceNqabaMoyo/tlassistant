import React, { useState, useMemo, useCallback } from 'react';
import * as THREE from 'three';
import { Zap, Play, Pause, Activity, Flame, GitBranch } from 'lucide-react';
import AtlasCanvas3D from '../shared/atlas3d/AtlasCanvas3D';
import CalculationPopoverCard from '../shared/atlas3d/CalculationPopoverCard';
import AtlasSyncChartSvg from '../shared/atlas3d/AtlasSyncChartSvg';
import { createPaperMaterial, addInkEdges } from '../shared/atlas3d/atlasRenderEngine';
import { createBlock3D, createSphereAtom3D, createVectorArrow3D } from '../shared/atlas3d/atlasPartsKit';

/**
 * CircuitPotentialAtlasAid
 * ------------------------
 * Grade 8–9 Natural Sciences & Grade 10–12 Physical Sciences:
 * 3D Electric Potential Landscape & Microscopic Electron Drift Explorer.
 *
 * Key Conceptual Breakthroughs:
 * 1. Vertical Elevation y ∝ V(x) (Electric Potential):
 *    Shows EMF lift (+ε), internal resistance drop ("lost volts" Ir), and external drops V1, V2.
 * 2. Microscopic Resistor Lattice Collisions & Electron Deceleration:
 *    Electrons visibly collide with vibrating Cu2+/nichrome lattice ions inside the resistive zone,
 *    decelerating through the resistor and converting electrical potential energy into thermal kinetic
 *    vibration (Joule heating P = I^2 R glow).
 * 3. Series vs. Parallel Current Splitting:
 *    In Parallel mode, branch drift speeds split inversely with resistance (I1/I2 = R2/R1) while sharing
 *    the exact same vertical potential drop ΔV.
 */

export default function CircuitPotentialAtlasAid() {
  const [topology, setTopology] = useState('series'); // 'series' | 'parallel'
  const [emf, setEmf] = useState(12.0); // V
  const [internalR, setInternalR] = useState(1.0); // Ω
  const [r1, setR1] = useState(4.0); // Ω
  const [r2, setR2] = useState(6.0); // Ω
  const [elevatePotential, setElevatePotential] = useState(true);
  const [isPlaying, setIsPlaying] = useState(true);
  const [selectedId, setSelectedId] = useState('resistor_r1');

  // Deterministic circuit physics calculations
  const circuitMath = useMemo(() => {
    const rExt = topology === 'series'
      ? r1 + r2
      : (r1 * r2) / Math.max(0.01, r1 + r2);
    const rTotal = rExt + internalR;
    const iTotal = emf / Math.max(0.01, rTotal);
    const vLost = iTotal * internalR;
    const vExt = Math.max(0, emf - vLost);

    const v1 = topology === 'series' ? iTotal * r1 : vExt;
    const v2 = topology === 'series' ? iTotal * r2 : vExt;
    const i1 = topology === 'series' ? iTotal : vExt / Math.max(0.01, r1);
    const i2 = topology === 'series' ? iTotal : vExt / Math.max(0.01, r2);

    const p1 = i1 * i1 * r1;
    const p2 = i2 * i2 * r2;
    const pLost = iTotal * iTotal * internalR;
    const pTotal = emf * iTotal;

    return {
      rExt,
      rTotal,
      iTotal,
      vLost,
      vExt,
      v1,
      v2,
      i1,
      i2,
      p1,
      p2,
      pLost,
      pTotal,
    };
  }, [topology, emf, internalR, r1, r2]);

  // Interactive calculation popovers for every component in the 3D scene
  const calculationsMap = useMemo(() => {
    const { rExt, rTotal, iTotal, vLost, vExt, v1, v2, i1, i2, p1, p2, pLost } = circuitMath;
    return {
      battery_emf: {
        id: 'battery_emf',
        symbol: '\\mathcal{E}, r',
        label: 'Battery EMF & Internal Resistance ("Lost Volts")',
        color: '#2B5B84',
        badgeText: `V_ext = ${vExt.toFixed(2)} V`,
        formula: '\\mathcal{E} = I(R_{\\text{ext}} + r) = V_{\\text{ext}} + V_{\\text{lost}}',
        substitution: `${emf.toFixed(1)} = (${iTotal.toFixed(2)})(${rExt.toFixed(2)} + ${internalR.toFixed(1)}) \\implies V_{\\text{lost}} = ${vLost.toFixed(2)}\\text{ V}`,
        result: `V_{\\text{ext}} = ${vExt.toFixed(2)}\\text{ V},\\quad I_{\\text{total}} = ${iTotal.toFixed(2)}\\text{ A}`,
        meaning: `Chemical energy inside the cell lifts charge by +${emf.toFixed(1)} V, but collisions inside the cell's internal resistance r = ${internalR.toFixed(1)} Ω cause an immediate drop of Ir = ${vLost.toFixed(2)} V ("lost volts", P_lost = ${pLost.toFixed(2)} W) before current leaves the terminals.`,
      },
      resistor_r1: {
        id: 'resistor_r1',
        symbol: 'R_1',
        label: `Resistor R₁ (${r1.toFixed(1)} Ω) — Lattice Collision & Joule Heating`,
        color: '#D97706',
        badgeText: `V₁=${v1.toFixed(1)}V | P₁=${p1.toFixed(1)}W`,
        formula: 'V_1 = I_1 R_1 \\quad \\text{and} \\quad P_1 = I_1^2 R_1',
        substitution: `V_1 = (${i1.toFixed(2)})(${r1.toFixed(1)}) = ${v1.toFixed(2)}\\text{ V},\\quad P_1 = (${i1.toFixed(2)})^2(${r1.toFixed(1)})`,
        result: `V_1 = ${v1.toFixed(2)}\\text{ V},\\quad P_1 = ${p1.toFixed(2)}\\text{ W}`,
        meaning: `Inside R₁, drifting electrons collide repeatedly with positive metal lattice ions, slowing down inside the resistive channel and transferring kinetic energy into lattice vibrations (thermal glow P₁ = ${p1.toFixed(2)} W).`,
      },
      resistor_r2: {
        id: 'resistor_r2',
        symbol: 'R_2',
        label: `Resistor R₂ (${r2.toFixed(1)} Ω) — Potential Drop & Drift Speed`,
        color: '#B8432E',
        badgeText: `V₂=${v2.toFixed(1)}V | P₂=${p2.toFixed(1)}W`,
        formula: topology === 'series'
          ? 'V_2 = I_{\\text{total}} R_2 \\quad (\\text{Series: } I_1 = I_2)'
          : 'I_2 = \\frac{V_{\\text{ext}}}{R_2} \\quad (\\text{Parallel: } V_1 = V_2 = V_{\\text{ext}})',
        substitution: topology === 'series'
          ? `V_2 = (${i2.toFixed(2)})(${r2.toFixed(1)}) = ${v2.toFixed(2)}\\text{ V}`
          : `I_2 = \\frac{${vExt.toFixed(2)}}{${r2.toFixed(1)}} = ${i2.toFixed(2)}\\text{ A}`,
        result: `I_2 = ${i2.toFixed(2)}\\text{ A},\\quad P_2 = ${p2.toFixed(2)}\\text{ W}`,
        meaning: topology === 'series'
          ? `In series, the exact same current (${iTotal.toFixed(2)} A) passes through both resistors, so the higher resistance takes the steeper potential drop.`
          : `In parallel, both branches span the same potential cliff (${vExt.toFixed(2)} V), so electron drift speed splits inversely with resistance: I₁ : I₂ = ${i1.toFixed(2)} A : ${i2.toFixed(2)} A.`,
      },
      ground_return: {
        id: 'ground_return',
        symbol: 'V = 0\\text{ V}',
        label: 'Zero-Potential Reference Return Wire',
        color: '#2D6A4F',
        badgeText: '0.0 V Return',
        formula: '\\sum \\Delta V_{\\text{loop}} = \\mathcal{E} - Ir - V_{\\text{ext}} = 0\\text{ V}',
        substitution: `${emf.toFixed(2)} - ${vLost.toFixed(2)} - ${vExt.toFixed(2)} = 0.00\\text{ V}`,
        result: '\\Delta V_{\\text{net}} = 0\\text{ V} \\text{ (Conservation of Energy)}',
        meaning: 'Along an ideal low-resistance return conductor, electric field E ≈ 0 so electrons glide at steady drift velocity with zero potential drop back to the negative terminal.',
      },
    };
  }, [circuitMath, emf, internalR, r1, r2, topology]);

  const activeCalculation = calculationsMap[selectedId] || calculationsMap.resistor_r1;

  // Build 3D scene
  const buildScene = useCallback(({ scene }) => {
    const root = new THREE.Group();
    scene.add(root);

    const { vExt, v1, iTotal, i1, i2, p1, p2 } = circuitMath;
    const hScale = elevatePotential ? 0.14 : 0.0;
    const yEmf = emf * hScale;
    const yExt = vExt * hScale;
    const yMid = topology === 'series' ? (vExt - v1) * hScale : 0;

    // 1. Base translucent reference loop shadow at y = 0
    const shadowMat = new THREE.LineBasicMaterial({ color: 0x94A3B8, transparent: true, opacity: 0.45 });
    const shadowPts = [
      new THREE.Vector3(-2.1, 0.01, -1.1),
      new THREE.Vector3(2.1, 0.01, -1.1),
      new THREE.Vector3(2.1, 0.01, 1.1),
      new THREE.Vector3(-2.1, 0.01, 1.1),
      new THREE.Vector3(-2.1, 0.01, -1.1),
    ];
    root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints(shadowPts), shadowMat));

    // 2. Battery EMF Pillar (Left edge x = -2.1, z from 0.8 to -0.8)
    const batteryGroup = new THREE.Group();
    batteryGroup.userData = { interactiveId: 'battery_emf', labelPoint: [0, Math.max(0.5, yExt * 0.55), 0] };
    batteryGroup.position.set(-2.1, 0, 0);

    const emfHeight = Math.max(0.28, yEmf);
    const emfPillar = createBlock3D({
      width: 0.36,
      height: emfHeight,
      depth: 0.9,
      color: 0x2B5B84,
      interactiveId: 'battery_emf',
    });
    emfPillar.position.set(0, emfHeight / 2, 0);
    batteryGroup.add(emfPillar);

    // Internal resistance drop cap (amber/red top slice showing Ir drop from yEmf to yExt)
    if (elevatePotential && yEmf > yExt + 0.02) {
      const irDropH = Math.max(0.08, yEmf - yExt);
      const irCap = createBlock3D({
        width: 0.4,
        height: irDropH,
        depth: 0.5,
        color: 0xB8432E,
        interactiveId: 'battery_emf',
      });
      irCap.position.set(0, yExt + irDropH / 2, -0.35);
      batteryGroup.add(irCap);
    }

    // Upward EMF arrow inside battery
    const emfArrow = createVectorArrow3D({
      origin: [0, 0.05, 0.65],
      direction: [0, 1, 0],
      length: Math.max(0.55, yExt),
      color: 0x2B5B84,
      interactiveId: 'battery_emf',
    });
    batteryGroup.add(emfArrow);
    root.add(batteryGroup);

    // Helper to build a 3D Resistor Ramp with internal lattice ions that vibrate & glow with P = I^2 R
    const buildResistorChannel = ({ start, end, resistance, power, interactiveId, baseColor }) => {
      const group = new THREE.Group();
      group.userData = {
        interactiveId,
        labelPoint: [
          (start.x + end.x) * 0.5,
          (start.y + end.y) * 0.5 + 0.35,
          (start.z + end.z) * 0.5,
        ],
      };

      const delta = new THREE.Vector3().subVectors(end, start);
      const len = delta.length();
      const mid = new THREE.Vector3().addVectors(start, end).multiplyScalar(0.5);

      // Thermal glow intensity proportional to power P = I^2 R
      const heatRatio = Math.min(1, power / 25);
      const rColor = new THREE.Color(baseColor).lerp(new THREE.Color(0xEF4444), heatRatio * 0.55);

      const channelGeo = new THREE.BoxGeometry(len, 0.16, 0.34);
      const channelMesh = new THREE.Mesh(
        channelGeo,
        createPaperMaterial(rColor.getHex(), { opacity: 0.88, transparent: true })
      );
      addInkEdges(channelMesh, 0x1E1B18, 0.75);
      channelMesh.position.copy(mid);
      channelMesh.lookAt(end);
      channelMesh.rotateY(Math.PI / 2);
      channelMesh.userData = { interactiveId };
      group.add(channelMesh);

      // Add lattice ions inside the resistor channel (higher R -> denser lattice obstacles)
      const ionCount = Math.min(9, Math.max(4, Math.round(resistance)));
      const latticeIons = [];
      for (let k = 0; k < ionCount; k++) {
        const frac = (k + 0.8) / (ionCount + 0.6);
        const basePos = new THREE.Vector3().lerpVectors(start, end, frac);
        const zOffset = (k % 2 === 0 ? 1 : -1) * 0.07;
        basePos.z += zOffset;
        basePos.y += 0.08;
        const ion = createSphereAtom3D({
          radius: 0.065,
          color: heatRatio > 0.35 ? 0xF97316 : 0xD97706,
          interactiveId,
          withEdges: false,
        });
        ion.position.copy(basePos);
        group.add(ion);
        latticeIons.push({ mesh: ion, basePos: basePos.clone(), phase: k * 1.3, heatRatio });
      }

      return { group, latticeIons };
    };

    const allLatticeIons = [];
    const electronPaths = [];

    if (topology === 'series') {
      // High-potential rail from battery top (-2.1, yExt, -1.1) to R1 start (-1.3, yExt, -1.1)
      const pBattTop = new THREE.Vector3(-2.1, yExt, -1.1);
      const pR1Start = new THREE.Vector3(-1.3, yExt, -1.1);
      const pR1End = new THREE.Vector3(0.4, yMid, -1.1);
      const pR2Start = new THREE.Vector3(0.7, yMid, -1.1);
      const pR2End = new THREE.Vector3(2.1, 0.05, -0.2);
      const pCornerBR = new THREE.Vector3(2.1, 0.05, 1.1);
      const pCornerBL = new THREE.Vector3(-2.1, 0.05, 1.1);
      const pBattBot = new THREE.Vector3(-2.1, 0.05, 0.45);

      const r1Obj = buildResistorChannel({
        start: pR1Start,
        end: pR1End,
        resistance: r1,
        power: p1,
        interactiveId: 'resistor_r1',
        baseColor: 0xD97706,
      });
      root.add(r1Obj.group);
      allLatticeIons.push(...r1Obj.latticeIons);

      const r2Obj = buildResistorChannel({
        start: pR2Start,
        end: pR2End,
        resistance: r2,
        power: p2,
        interactiveId: 'resistor_r2',
        baseColor: 0xB8432E,
      });
      root.add(r2Obj.group);
      allLatticeIons.push(...r2Obj.latticeIons);

      // Conductive wires
      const wireMat = new THREE.LineBasicMaterial({ color: 0x1E1B18, linewidth: 2 });
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(-2.1, yExt, -0.45),
        pBattTop,
        pR1Start,
      ]), wireMat));
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([pR1End, pR2Start]), wireMat));

      const returnGroup = new THREE.Group();
      returnGroup.userData = { interactiveId: 'ground_return', labelPoint: [0, 0.2, 1.1] };
      const retTube = new THREE.Mesh(
        new THREE.BoxGeometry(4.2, 0.08, 0.12),
        createPaperMaterial(0x2D6A4F)
      );
      retTube.position.set(0, 0.05, 1.1);
      retTube.userData = { interactiveId: 'ground_return' };
      returnGroup.add(retTube);
      root.add(returnGroup);

      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([pR2End, pCornerBR, pCornerBL, pBattBot]), wireMat));

      // Build segmented electron path with explicit speed multipliers:
      // Fast in low-resistance wire, visibly slowed inside R1 and R2!
      electronPaths.push({
        baseSpeed: Math.max(0.25, Math.min(1.4, iTotal * 0.45)),
        segments: [
          { a: pBattTop, b: pR1Start, speedMult: 1.5, inResistor: false },
          { a: pR1Start, b: pR1End, speedMult: Math.max(0.28, 1.1 / (1 + r1 * 0.28)), inResistor: true },
          { a: pR1End, b: pR2Start, speedMult: 1.4, inResistor: false },
          { a: pR2Start, b: pR2End, speedMult: Math.max(0.25, 1.1 / (1 + r2 * 0.28)), inResistor: true },
          { a: pR2End, b: pCornerBR, speedMult: 1.5, inResistor: false },
          { a: pCornerBR, b: pCornerBL, speedMult: 1.6, inResistor: false },
          { a: pCornerBL, b: pBattBot, speedMult: 1.5, inResistor: false },
        ],
      });
    } else {
      // Parallel topology: two parallel branches bridging yExt down to 0.05 V
      const pTopSplit = new THREE.Vector3(-1.1, yExt, 0);
      const pR1Start = new THREE.Vector3(-0.9, yExt, -0.95);
      const pR1End = new THREE.Vector3(1.2, 0.05, -0.95);
      const pR2Start = new THREE.Vector3(-0.9, yExt, 0.65);
      const pR2End = new THREE.Vector3(1.2, 0.05, 0.65);
      const pJoinBot = new THREE.Vector3(1.7, 0.05, 0);
      const pCornerBR = new THREE.Vector3(1.7, 0.05, 1.25);
      const pCornerBL = new THREE.Vector3(-2.1, 0.05, 1.25);

      const r1Obj = buildResistorChannel({
        start: pR1Start,
        end: pR1End,
        resistance: r1,
        power: p1,
        interactiveId: 'resistor_r1',
        baseColor: 0xD97706,
      });
      root.add(r1Obj.group);
      allLatticeIons.push(...r1Obj.latticeIons);

      const r2Obj = buildResistorChannel({
        start: pR2Start,
        end: pR2End,
        resistance: r2,
        power: p2,
        interactiveId: 'resistor_r2',
        baseColor: 0xB8432E,
      });
      root.add(r2Obj.group);
      allLatticeIons.push(...r2Obj.latticeIons);

      const wireMat = new THREE.LineBasicMaterial({ color: 0x1E1B18, linewidth: 2 });
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(-2.1, yExt, 0),
        pTopSplit,
        pR1Start,
      ]), wireMat));
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([pTopSplit, pR2Start]), wireMat));
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([pR1End, pJoinBot]), wireMat));
      root.add(new THREE.Line(new THREE.BufferGeometry().setFromPoints([pR2End, pJoinBot, pCornerBR, pCornerBL, new THREE.Vector3(-2.1, 0.05, 0.45)]), wireMat));

      const returnGroup = new THREE.Group();
      returnGroup.userData = { interactiveId: 'ground_return', labelPoint: [0, 0.2, 1.25] };
      const retTube = new THREE.Mesh(
        new THREE.BoxGeometry(3.8, 0.08, 0.12),
        createPaperMaterial(0x2D6A4F)
      );
      retTube.position.set(-0.2, 0.05, 1.25);
      retTube.userData = { interactiveId: 'ground_return' };
      returnGroup.add(retTube);
      root.add(returnGroup);

      electronPaths.push({
        baseSpeed: Math.max(0.25, Math.min(1.5, i1 * 0.45)),
        segments: [
          { a: pTopSplit, b: pR1Start, speedMult: 1.4, inResistor: false },
          { a: pR1Start, b: pR1End, speedMult: Math.max(0.28, 1.1 / (1 + r1 * 0.25)), inResistor: true },
          { a: pR1End, b: pJoinBot, speedMult: 1.4, inResistor: false },
          { a: pJoinBot, b: pCornerBR, speedMult: 1.5, inResistor: false },
          { a: pCornerBR, b: pCornerBL, speedMult: 1.5, inResistor: false },
        ],
      });
      electronPaths.push({
        baseSpeed: Math.max(0.25, Math.min(1.5, i2 * 0.45)),
        segments: [
          { a: pTopSplit, b: pR2Start, speedMult: 1.4, inResistor: false },
          { a: pR2Start, b: pR2End, speedMult: Math.max(0.28, 1.1 / (1 + r2 * 0.25)), inResistor: true },
          { a: pR2End, b: pJoinBot, speedMult: 1.4, inResistor: false },
          { a: pJoinBot, b: pCornerBR, speedMult: 1.5, inResistor: false },
          { a: pCornerBR, b: pCornerBL, speedMult: 1.5, inResistor: false },
        ],
      });
    }

    // Create animated electron spheres along each path
    const electronRunners = [];
    electronPaths.forEach((pathObj) => {
      const count = 10;
      for (let i = 0; i < count; i++) {
        const mesh = createSphereAtom3D({
          radius: 0.072,
          color: 0x0EA5E9,
          withEdges: true,
        });
        root.add(mesh);
        electronRunners.push({
          mesh,
          pathObj,
          segIdx: i % pathObj.segments.length,
          t: (i * 0.37) % 1,
        });
      }
    });

    return {
      interactiveObjects: [root],
      update: (dt, elapsed) => {
        if (!isPlaying) return;

        // 1. Vibrate lattice ions inside resistors (higher P = I^2 R -> stronger thermal amplitude)
        allLatticeIons.forEach((ion) => {
          const amp = 0.012 + ion.heatRatio * 0.032;
          ion.mesh.position.x = ion.basePos.x + Math.sin(elapsed * 18 + ion.phase) * amp;
          ion.mesh.position.z = ion.basePos.z + Math.cos(elapsed * 16 + ion.phase) * amp;
        });

        // 2. Advance electrons along segments (slowing down + jittering when colliding inside resistors)
        electronRunners.forEach((runner, idx) => {
          const seg = runner.pathObj.segments[runner.segIdx];
          const segLen = Math.max(0.2, seg.a.distanceTo(seg.b));
          const step = (dt * runner.pathObj.baseSpeed * seg.speedMult) / segLen;
          runner.t += step;
          if (runner.t >= 1) {
            runner.t = 0;
            runner.segIdx = (runner.segIdx + 1) % runner.pathObj.segments.length;
          }
          const activeSeg = runner.pathObj.segments[runner.segIdx];
          runner.mesh.position.lerpVectors(activeSeg.a, activeSeg.b, runner.t);
          runner.mesh.position.y += 0.1;
          if (activeSeg.inResistor) {
            // Microscopic scattering deflection as electrons collide with lattice ions
            runner.mesh.position.z += Math.sin(elapsed * 22 + idx * 1.9) * 0.045;
          }
        });
      },
    };
  }, [circuitMath, elevatePotential, emf, isPlaying, r1, r2, topology]);

  // Synchronized 2D Loop Potential Chart V(x)
  const potentialSeries = useMemo(() => {
    const { vExt, v1 } = circuitMath;
    const midV = topology === 'series' ? Math.max(0, vExt - v1) : vExt;
    return [
      {
        id: 'loop_v',
        label: 'Electric Potential V(x)',
        color: '#2B5B84',
        fillArea: true,
        points: [
          { x: 0, y: 0 },
          { x: 12, y: emf },
          { x: 24, y: vExt },
          { x: 35, y: vExt },
          { x: 58, y: topology === 'series' ? midV : 0 },
          { x: 66, y: topology === 'series' ? midV : 0 },
          { x: 88, y: 0 },
          { x: 100, y: 0 },
        ],
      },
    ];
  }, [circuitMath, emf, topology]);

  const activeChartX = selectedId === 'battery_emf' ? 18 : selectedId === 'resistor_r1' ? 46 : selectedId === 'resistor_r2' ? 76 : 94;
  const activeChartY = selectedId === 'battery_emf'
    ? circuitMath.vExt
    : selectedId === 'resistor_r1'
    ? circuitMath.v1 * 0.5
    : selectedId === 'resistor_r2'
    ? circuitMath.v2 * 0.3
    : 0;

  return (
    <div data-testid="circuit-potential-atlas-aid" className="space-y-4 text-slate-800">
      {/* Top Topology & Controls Bar */}
      <div className="bg-white rounded-xl border border-slate-200 p-3.5 shadow-xs space-y-3">
        <div className="flex flex-wrap items-center justify-between gap-2">
          <div>
            <span className="px-2 py-0.5 text-[10px] font-bold rounded-full bg-amber-100 text-amber-900 uppercase tracking-wider">
              3D Potential Landscape & Resistor Collisions
            </span>
            <h4 className="text-sm font-bold text-slate-900 mt-1">
              Electric Circuits: Voltage Elevation (<span className="font-mono">y ∝ V</span>) & Electron Drift
            </h4>
          </div>

          <div className="flex items-center gap-1.5">
            <button
              type="button"
              data-testid="btn-circuit-series"
              onClick={() => setTopology('series')}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
                topology === 'series'
                  ? 'bg-[#2B5B84] text-white shadow-xs'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              Series Loop
            </button>
            <button
              type="button"
              data-testid="btn-circuit-parallel"
              onClick={() => setTopology('parallel')}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all flex items-center gap-1 ${
                topology === 'parallel'
                  ? 'bg-[#2B5B84] text-white shadow-xs'
                  : 'bg-slate-100 text-slate-600 hover:bg-slate-200'
              }`}
            >
              <GitBranch className="w-3 h-3" />
              Parallel Split
            </button>
            <button
              type="button"
              data-testid="btn-circuit-elevate"
              onClick={() => setElevatePotential((v) => !v)}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold border transition-all ${
                elevatePotential
                  ? 'bg-amber-50 border-amber-300 text-amber-900'
                  : 'bg-white border-slate-200 text-slate-600'
              }`}
            >
              {elevatePotential ? '3D Height y ∝ V: ON' : 'Flat 2D Schematic'}
            </button>
            <button
              type="button"
              onClick={() => setIsPlaying((p) => !p)}
              className="p-1.5 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700"
              title={isPlaying ? 'Pause electron drift' : 'Play electron drift'}
            >
              {isPlaying ? <Pause className="w-3.5 h-3.5" /> : <Play className="w-3.5 h-3.5" />}
            </button>
          </div>
        </div>

        {/* Parameter Sliders */}
        <div className="grid grid-cols-2 sm:grid-cols-4 gap-2.5 pt-1">
          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>EMF (ε)</span>
              <span className="font-mono font-bold text-[#2B5B84]">{emf.toFixed(1)} V</span>
            </div>
            <input
              type="range"
              min="6"
              max="24"
              step="1"
              value={emf}
              onChange={(e) => setEmf(parseFloat(e.target.value))}
              className="w-full accent-[#2B5B84] cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Internal r</span>
              <span className="font-mono font-bold text-rose-700">{internalR.toFixed(1)} Ω</span>
            </div>
            <input
              type="range"
              min="0"
              max="4"
              step="0.5"
              value={internalR}
              onChange={(e) => setInternalR(parseFloat(e.target.value))}
              className="w-full accent-rose-600 cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Resistor R₁</span>
              <span className="font-mono font-bold text-amber-700">{r1.toFixed(1)} Ω</span>
            </div>
            <input
              type="range"
              min="1"
              max="12"
              step="0.5"
              value={r1}
              onChange={(e) => setR1(parseFloat(e.target.value))}
              className="w-full accent-amber-600 cursor-pointer h-1.5"
            />
          </label>

          <label className="bg-slate-50 p-2 rounded-lg border border-slate-200/80 flex flex-col gap-1">
            <div className="flex justify-between text-[11px] font-semibold text-slate-600">
              <span>Resistor R₂</span>
              <span className="font-mono font-bold text-orange-700">{r2.toFixed(1)} Ω</span>
            </div>
            <input
              type="range"
              min="1"
              max="12"
              step="0.5"
              value={r2}
              onChange={(e) => setR2(parseFloat(e.target.value))}
              className="w-full accent-orange-600 cursor-pointer h-1.5"
            />
          </label>
        </div>
      </div>

      {/* 3D Paper & Ink Viewport */}
      <AtlasCanvas3D
        testId="circuit-potential-3d-canvas"
        height={320}
        buildScene={buildScene}
        selectedId={selectedId}
        onSelect={(id) => {
          if (id) setSelectedId(id);
        }}
        badgeItems={Object.values(calculationsMap)}
        subtitle="Click R₁, R₂, or the Battery to inspect Ohm's Law, 'lost volts' (Ir), and lattice collision heating (P = I²R)"
      />

      {/* Interactive Calculation Popover */}
      <CalculationPopoverCard
        calculation={activeCalculation}
        allCalculations={Object.values(calculationsMap)}
        onSelectCalculation={setSelectedId}
      />

      {/* Synchronized Loop Potential Graph V(x) */}
      <AtlasSyncChartSvg
        title="Synchronized Loop Potential Profile V(x) Around Circuit"
        xLabel="Position Along Circuit Loop (%)"
        yLabel="Potential V (Volts)"
        xDomain={[0, 100]}
        yDomain={[0, Math.max(15, emf + 2)]}
        series={potentialSeries}
        activePoint={{
          x: activeChartX,
          y: activeChartY,
          label: `${activeCalculation.badgeText}`,
          color: activeCalculation.color,
        }}
        zones={[
          { xStart: 12, xEnd: 24, label: 'Ir Lost', color: 'rgba(184, 67, 46, 0.14)' },
          { xStart: 35, xEnd: 58, label: 'R₁ Drop', color: 'rgba(217, 119, 6, 0.14)' },
          { xStart: 66, xEnd: 88, label: 'R₂ Drop', color: 'rgba(184, 67, 46, 0.10)' },
        ]}
      />
    </div>
  );
}
