import * as THREE from 'three';
import {
  createPaperMaterial,
  addInkEdges,
  tagInteractive3D,
} from './atlasRenderEngine';

/**
 * atlasPartsKit.js
 *
 * Reusable 3D "Paper & Ink" Procedural Geometry Kit for Fundile Sidecar Visual Aids.
 * Provides crisp, low-poly scientific, mathematical, and biological primitives:
 *   - Architectural reference floor grids
 *   - 3D Vector Arrows (shaft + conical head) with raycast hitboxes
 *   - Beveled 3D Blocks / Ramps / Pulleys
 *   - 3D Helical Resistor Coils & Intermolecular Spring Bonds
 *   - 3D CPK Atoms, Orbital Clouds & Crystal Lattice Nodes
 *   - 3D Cutaway Peristalsis Muscular Tube with Bolus Contraction Wave
 */

/**
 * Editorial paper reference floor grid.
 */
export function createFloorGrid3D({
  size = 10,
  divisions = 10,
  y = -1.6,
  colorCenter = 0xcbd5e1,
  colorGrid = 0xe2e8f0,
} = {}) {
  const grid = new THREE.GridHelper(size, divisions, colorCenter, colorGrid);
  grid.position.y = y;
  grid.raycast = () => {};
  return grid;
}

/**
 * 3D Vector Arrow (Cylindrical shaft + Conical tip) with an enlarged invisible
 * hit-cylinder so clicking or hovering narrow vectors is effortless.
 */
export function createVectorArrow3D({
  origin = [0, 0, 0],
  dir = [1, 0, 0],
  direction = null,
  length = 2.0,
  color = 0x2563eb,
  shaftRadius = 0.065,
  headRadius = 0.17,
  headLength = 0.38,
  interactiveId = null,
} = {}) {
  const effectiveDir = direction || dir;
  const group = new THREE.Group();
  const safeLen = Math.max(0.25, length);
  const actualHeadLen = Math.min(headLength, safeLen * 0.45);
  const shaftLen = Math.max(0.05, safeLen - actualHeadLen);

  const mat = createPaperMaterial(color);

  // Shaft cylinder along +Y
  const shaftGeo = new THREE.CylinderGeometry(shaftRadius, shaftRadius, shaftLen, 14);
  shaftGeo.translate(0, shaftLen / 2, 0);
  const shaftMesh = new THREE.Mesh(shaftGeo, mat);
  addInkEdges(shaftMesh, 35, 0x0f172a, 0.55);
  group.add(shaftMesh);

  // Arrowhead cone at tip
  const headGeo = new THREE.ConeGeometry(headRadius, actualHeadLen, 16);
  headGeo.translate(0, shaftLen + actualHeadLen / 2, 0);
  const headMesh = new THREE.Mesh(headGeo, mat);
  addInkEdges(headMesh, 35, 0x0f172a, 0.65);
  group.add(headMesh);

  // Invisible wider hitbox cylinder for easy mouse/touch raycasting
  if (interactiveId) {
    const hitGeo = new THREE.CylinderGeometry(headRadius * 1.45, headRadius * 1.45, safeLen, 8);
    hitGeo.translate(0, safeLen / 2, 0);
    const hitMat = new THREE.MeshBasicMaterial({ visible: false });
    const hitMesh = new THREE.Mesh(hitGeo, hitMat);
    group.add(hitMesh);
  }

  // Orient along dir vector
  const dirVec = new THREE.Vector3(...effectiveDir);
  if (dirVec.lengthSq() > 1e-6) {
    dirVec.normalize();
    const up = new THREE.Vector3(0, 1, 0);
    const quat = new THREE.Quaternion().setFromUnitVectors(up, dirVec);
    group.quaternion.copy(quat);
  }

  group.position.set(...origin);
  if (interactiveId) tagInteractive3D(group, interactiveId);
  group.group = group;
  return group;
}

/**
 * 3D Box / Mass Block / Plate with crisp ink silhouette edges.
 */
export function createBlock3D({
  width = 1.2,
  height = 0.8,
  depth = 1.0,
  color = 0x3b82f6,
  position = [0, 0, 0],
  rotation = [0, 0, 0],
  opacity = 1.0,
  glow = 0.0,
  interactiveId = null,
} = {}) {
  const geo = new THREE.BoxGeometry(width, height, depth);
  const mat = createPaperMaterial(color, { opacity, glow });
  const mesh = new THREE.Mesh(geo, mat);
  mesh.position.set(...position);
  mesh.rotation.set(...rotation);
  addInkEdges(mesh, 20, 0x1e293b, opacity < 1 ? 0.45 : 0.82);
  if (interactiveId) tagInteractive3D(mesh, interactiveId);
  return mesh;
}

/**
 * 3D Wedge / Inclined Plane Ramp.
 */
export function createInclinedRamp3D({
  baseLength = 5.0,
  run = null,
  height: explicitHeight = null,
  angleDeg = 30,
  depth = 2.2,
  color = 0xe2e8f0,
  interactiveId = null,
} = {}) {
  const actualRun = run ?? baseLength;
  const rad = (angleDeg * Math.PI) / 180;
  const height = explicitHeight ?? actualRun * Math.tan(rad);

  const shape = new THREE.Shape();
  shape.moveTo(0, 0);
  shape.lineTo(actualRun, 0);
  shape.lineTo(0, height);
  shape.closePath();

  const extrudeGeo = new THREE.ExtrudeGeometry(shape, {
    depth,
    bevelEnabled: false,
  });
  if (run === null) {
    extrudeGeo.translate(-actualRun / 2, 0, -depth / 2);
  }

  const mat = createPaperMaterial(color);
  const mesh = new THREE.Mesh(extrudeGeo, mat);
  addInkEdges(mesh, 15, 0x1e293b, 0.85);
  if (interactiveId) tagInteractive3D(mesh, interactiveId);
  return mesh;
}

/**
 * 3D CPK Atom / Ion / Particle Sphere.
 */
export function createSphereAtom3D({
  radius = 0.35,
  color = 0xef4444,
  position = [0, 0, 0],
  opacity = 1.0,
  glow = 0.0,
  segments = 20,
  interactiveId = null,
} = {}) {
  const geo = new THREE.SphereGeometry(radius, segments, segments);
  const mat = createPaperMaterial(color, { opacity, glow });
  const mesh = new THREE.Mesh(geo, mat);
  mesh.position.set(...position);
  if (interactiveId) tagInteractive3D(mesh, interactiveId);
  return mesh;
}

/**
 * 3D Covalent / Ionic Bond Cylinder between two 3D points (supports order 1, 2, 3).
 */
export function createBondCylinder3D({
  start = [0, 0, 0],
  end = [1, 0, 0],
  radius = 0.065,
  color = 0x64748b,
  order = 1,
  opacity = 1.0,
  interactiveId = null,
} = {}) {
  const group = new THREE.Group();
  const vStart = new THREE.Vector3(...start);
  const vEnd = new THREE.Vector3(...end);
  const diff = new THREE.Vector3().subVectors(vEnd, vStart);
  const len = Math.max(0.05, diff.length());
  const mid = new THREE.Vector3().addVectors(vStart, vEnd).multiplyScalar(0.5);

  const mat = createPaperMaterial(color, { opacity });
  const offsets =
    order === 3
      ? [-radius * 2.2, 0, radius * 2.2]
      : order === 2
      ? [-radius * 1.4, radius * 1.4]
      : [0];

  offsets.forEach((off) => {
    const cylGeo = new THREE.CylinderGeometry(radius * 0.85, radius * 0.85, len, 12);
    const cyl = new THREE.Mesh(cylGeo, mat);
    cyl.position.x = off;
    addInkEdges(cyl, 40, 0x1e293b, 0.4);
    group.add(cyl);
  });

  group.position.copy(mid);
  if (diff.lengthSq() > 1e-6) {
    const up = new THREE.Vector3(0, 1, 0);
    group.quaternion.setFromUnitVectors(up, diff.clone().normalize());
  }
  if (interactiveId) tagInteractive3D(group, interactiveId);
  group.group = group;
  return group;
}

/**
 * 3D Helical Spring / Resistor Coil between two 3D points.
 */
export function createHelixCoil3D({
  start = null,
  end = null,
  height = null,
  radius = 0.24,
  turns = 6,
  tubeRadius = 0.045,
  color = 0xd97706,
  glow = 0.0,
  interactiveId = null,
} = {}) {
  const effStart = start || (height ? [0, 0, 0] : [-1, 0, 0]);
  const effEnd = end || (height ? [0, height, 0] : [1, 0, 0]);
  const vStart = new THREE.Vector3(...effStart);
  const vEnd = new THREE.Vector3(...effEnd);
  const axis = new THREE.Vector3().subVectors(vEnd, vStart);
  const len = Math.max(0.2, axis.length());
  const dir = axis.clone().normalize();

  // Build orthogonal basis (u, v) perpendicular to dir
  const arbitrary = Math.abs(dir.y) < 0.9 ? new THREE.Vector3(0, 1, 0) : new THREE.Vector3(1, 0, 0);
  const u = new THREE.Vector3().crossVectors(dir, arbitrary).normalize();
  const v = new THREE.Vector3().crossVectors(dir, u).normalize();

  const points = [];
  const steps = Math.max(36, turns * 12);
  for (let i = 0; i <= steps; i++) {
    const t = i / steps;
    const angle = t * turns * Math.PI * 2;
    const envelope = Math.sin(Math.min(1, t * 8) * (Math.PI / 2)) * Math.sin(Math.min(1, (1 - t) * 8) * (Math.PI / 2));
    const r = radius * envelope;
    const pt = vStart
      .clone()
      .addScaledVector(dir, t * len)
      .addScaledVector(u, r * Math.cos(angle))
      .addScaledVector(v, r * Math.sin(angle));
    points.push(pt);
  }

  const curve = new THREE.CatmullRomCurve3(points);
  const tubeGeo = new THREE.TubeGeometry(curve, steps, tubeRadius, 8, false);
  const mat = createPaperMaterial(color, { glow });
  const mesh = new THREE.Mesh(tubeGeo, mat);

  // Invisible bounding cylinder for easy click/hover raycasting
  if (interactiveId) {
    const group = new THREE.Group();
    group.add(mesh);
    const hitGeo = new THREE.CylinderGeometry(radius * 1.4, radius * 1.4, len, 8);
    const hitMesh = new THREE.Mesh(hitGeo, new THREE.MeshBasicMaterial({ visible: false }));
    hitMesh.position.copy(vStart.clone().add(vEnd).multiplyScalar(0.5));
    hitMesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), dir);
    group.add(hitMesh);
    tagInteractive3D(group, interactiveId);
    return group;
  }

  return mesh;
}

/**
 * 3D Cutaway Peristalsis Muscular Tube (Oesophagus / Small Intestine)
 * Dynamically pinches circular smooth muscles immediately behind `bolusT` (0..1)
 * and relaxes circular muscles ahead of `bolusT` to show active peristaltic wave mechanics.
 */
export function createPeristalsisTube3D({
  length = 6.4,
  baseRadius = 0.68,
  bolusT = 0.45,
  contractionStrength = 0.52,
  interactiveId = 'peristalsis_wave',
} = {}) {
  const group = new THREE.Group();
  const segments = 48;
  const halfLen = length / 2;

  const radiusAt = (t) => {
    // Behind bolus (t < bolusT): circular muscles contract tightly (pinch)
    const pinchDist = t - (bolusT - 0.13);
    const pinch = contractionStrength * Math.exp(-(pinchDist * pinchDist) / 0.0065);
    // At bolus (t == bolusT): lumen distends around the food bolus
    const distendDist = t - bolusT;
    const bulge = 0.28 * Math.exp(-(distendDist * distendDist) / 0.0055);
    return Math.max(0.2, baseRadius - pinch + bulge);
  };

  // Build upper & lower cutaway muscular wall profiles
  const outerMat = createPaperMaterial(0xf43f5e, { doubleSided: true });
  const innerMucosaMat = createPaperMaterial(0xfda4af, { doubleSided: true });

  for (let i = 0; i < segments; i++) {
    const t0 = i / segments;
    const t1 = (i + 1) / segments;
    const x0 = -halfLen + t0 * length;
    const x1 = -halfLen + t1 * length;
    const r0 = radiusAt(t0);
    const r1 = radiusAt(t1);
    const segLen = x1 - x0;

    // Half-cylinder cutaway shell (angle Pi/3 to 5*Pi/3) so interior lumen & bolus are visible
    const cylGeo = new THREE.CylinderGeometry(r1, r0, segLen, 16, 1, true, Math.PI * 0.25, Math.PI * 1.5);
    cylGeo.rotateZ(-Math.PI / 2);
    const segMesh = new THREE.Mesh(cylGeo, i % 2 === 0 ? outerMat : innerMucosaMat);
    segMesh.position.x = (x0 + x1) / 2;
    group.add(segMesh);
  }

  // Highlighted Circular Muscle Contraction Rings behind the bolus
  const ringMat = createPaperMaterial(0xbe123c, { glow: 0.25 });
  for (let offset of [-0.16, -0.12, -0.08]) {
    const rt = Math.max(0.04, Math.min(0.96, bolusT + offset));
    const rx = -halfLen + rt * length;
    const rr = radiusAt(rt) + 0.04;
    const torusGeo = new THREE.TorusGeometry(rr, 0.045, 10, 24);
    torusGeo.rotateY(Math.PI / 2);
    const ringMesh = new THREE.Mesh(torusGeo, ringMat);
    ringMesh.position.x = rx;
    tagInteractive3D(ringMesh, 'circular_muscle_contracted');
    group.add(ringMesh);
  }

  // Food Bolus inside lumen at bolusT
  const bolusX = -halfLen + bolusT * length;
  const bolusGeo = new THREE.SphereGeometry(0.46, 20, 16);
  bolusGeo.scale(1.35, 0.92, 0.92);
  const bolusMat = createPaperMaterial(0xd97706, { glow: 0.15 });
  const bolusMesh = new THREE.Mesh(bolusGeo, bolusMat);
  bolusMesh.position.set(bolusX, 0, 0);
  addInkEdges(bolusMesh, 30, 0x78350f, 0.5);
  tagInteractive3D(bolusMesh, 'food_bolus');
  group.add(bolusMesh);

  // Direction arrow ahead of bolus
  const arrow = createVectorArrow3D({
    origin: [bolusX + 0.65, 0, 0],
    dir: [1, 0, 0],
    length: 0.95,
    color: 0x059669,
    interactiveId: 'relaxation_wave',
  });
  group.add(arrow);

  if (interactiveId) tagInteractive3D(group, interactiveId);
  group.group = group;
  return group;
}
