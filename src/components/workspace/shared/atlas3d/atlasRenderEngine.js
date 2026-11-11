import * as THREE from 'three';

/**
 * atlasRenderEngine.js
 *
 * Native Three.js "Paper & Ink" 3D Rendering Engine for Fundile Sidecar Visual Aids.
 * Adapts the matte paper-shading and crisp architectural silhouette aesthetic from
 * Atlas of Physics into a modular, zero-leak React lifecycle engine with raycasting
 * and automatic headless-browser fallback.
 */

const PAPER_BG_HEX = 0xfbfbf9;
const INK_HEX = 0x1e293b;

// Facing-ratio Paper & Ink Shader (inspired by Atlas of Physics SHADE_V / SHADE_F)
const PAPER_VERTEX_SHADER = `
  varying vec3 vNormalView;
  varying vec3 vViewPos;
  void main() {
    vNormalView = normalize(normalMatrix * normal);
    vec4 mvPos = modelViewMatrix * vec4(position, 1.0);
    vViewPos = -mvPos.xyz;
    gl_Position = projectionMatrix * mvPos;
  }
`;

const PAPER_FRAGMENT_SHADER = `
  uniform vec3 uBaseColor;
  uniform vec3 uWarmTint;
  uniform vec3 uCoolShadow;
  uniform float uOpacity;
  uniform float uGlow;
  varying vec3 vNormalView;
  varying vec3 vViewPos;

  void main() {
    vec3 n = normalize(vNormalView);
    vec3 lightDir = normalize(vec3(0.45, 0.75, 0.65));
    float ndl = dot(n, lightDir) * 0.5 + 0.5;
    float facing = abs(dot(n, normalize(vViewPos)));

    // Matte editorial paper shading with subtle rim ink darkening
    vec3 shaded = mix(uBaseColor * uCoolShadow, uBaseColor * uWarmTint, smoothstep(0.15, 0.88, ndl));
    shaded = mix(shaded * 0.82, shaded, smoothstep(0.08, 0.35, facing));
    shaded += uBaseColor * uGlow * 0.45;

    gl_FragColor = vec4(shaded, uOpacity);
  }
`;

/**
 * Creates a matte editorial paper-shaded material with optional glow & transparency.
 */
export function createPaperMaterial(colorHex = 0x3b82f6, options = {}) {
  const baseColor = new THREE.Color(colorHex);
  const opacity = options.opacity ?? 1.0;
  const transparent = opacity < 0.999 || Boolean(options.transparent);

  if (options.wireframe || options.basic) {
    return new THREE.MeshBasicMaterial({
      color: baseColor,
      wireframe: Boolean(options.wireframe),
      transparent,
      opacity,
      side: options.side ?? (options.doubleSided ? THREE.DoubleSide : THREE.FrontSide),
    });
  }

  return new THREE.ShaderMaterial({
    uniforms: {
      uBaseColor: { value: baseColor },
      uWarmTint: { value: new THREE.Color(1.06, 1.04, 1.0) },
      uCoolShadow: { value: new THREE.Color(0.68, 0.71, 0.78) },
      uOpacity: { value: opacity },
      uGlow: { value: options.glow ?? 0.0 },
    },
    vertexShader: PAPER_VERTEX_SHADER,
    fragmentShader: PAPER_FRAGMENT_SHADER,
    transparent,
    depthWrite: !transparent || Boolean(options.depthWrite),
    side: options.side ?? (options.doubleSided ? THREE.DoubleSide : THREE.FrontSide),
  });
}

/**
 * Attaches crisp architectural ink silhouette/crease edges to a 3D mesh.
 * Supports both addInkEdges(mesh, thresholdDeg, inkColor, opacity)
 * and shorthand addInkEdges(mesh, inkColorHex, opacity).
 */
export function addInkEdges(mesh, arg2 = 22, arg3 = INK_HEX, arg4 = 0.72) {
  if (!mesh || !mesh.geometry) return null;
  const isColorSecond = typeof arg2 === 'number' && arg2 > 360;
  const thresholdDeg = isColorSecond ? 22 : arg2;
  const inkColor = isColorSecond ? arg2 : arg3;
  const opacity = isColorSecond ? (typeof arg3 === 'number' && arg3 <= 1 ? arg3 : 0.75) : arg4;

  const edgesGeo = new THREE.EdgesGeometry(mesh.geometry, thresholdDeg);
  const edgesMat = new THREE.LineBasicMaterial({
    color: inkColor,
    transparent: opacity < 1.0,
    opacity,
  });
  const lines = new THREE.LineSegments(edgesGeo, edgesMat);
  lines.raycast = () => {}; // Never intercept raycasts meant for the parent mesh
  mesh.add(lines);
  return lines;
}

/**
 * Tag a 3D Object3D (and all its descendant meshes) with an interactive ID for raycasting.
 */
export function tagInteractive3D(object3D, interactiveId) {
  if (!object3D || !interactiveId) return object3D;
  object3D.userData.interactiveId = interactiveId;
  object3D.traverse((child) => {
    child.userData.interactiveId = interactiveId;
  });
  return object3D;
}

/**
 * Initializes the Three.js Paper & Ink viewport inside a container element.
 */
export function createAtlasViewport({
  container,
  initialCamera = { radius: 11.5, theta: 0.68, phi: 1.08, target: [0, 0.4, 0] },
  onSelectInteractive,
  onHoverInteractive,
  onCameraChange,
}) {
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(PAPER_BG_HEX);

  const width = Math.max(280, container?.clientWidth || 460);
  const height = Math.max(220, container?.clientHeight || 320);

  const camera = new THREE.PerspectiveCamera(36, width / height, 0.1, 200);

  // Spherical orbit state
  const orbit = {
    radius: initialCamera.radius ?? 11.5,
    theta: initialCamera.theta ?? 0.68, // horizontal azimuth (rad)
    phi: initialCamera.phi ?? 1.08, // vertical polar angle from +Y (rad)
    target: new THREE.Vector3(...(initialCamera.target || [0, 0.4, 0])),
  };

  const syncCamera = () => {
    const safePhi = Math.max(0.15, Math.min(Math.PI - 0.15, orbit.phi));
    orbit.phi = safePhi;
    const sinPhi = Math.sin(safePhi);
    camera.position.set(
      orbit.target.x + orbit.radius * sinPhi * Math.sin(orbit.theta),
      orbit.target.y + orbit.radius * Math.cos(safePhi),
      orbit.target.z + orbit.radius * sinPhi * Math.cos(orbit.theta)
    );
    camera.lookAt(orbit.target);
    camera.updateMatrixWorld();
    onCameraChange?.({
      thetaDeg: Math.round((orbit.theta * 180) / Math.PI),
      phiDeg: Math.round((orbit.phi * 180) / Math.PI),
      radius: Number(orbit.radius.toFixed(1)),
    });
  };
  syncCamera();

  // Ambient + Directional lights for standard materials if used alongside shader materials
  const ambientLight = new THREE.AmbientLight(0xffffff, 0.78);
  const dirLight = new THREE.DirectionalLight(0xfffbeb, 0.85);
  dirLight.position.set(8, 14, 10);
  scene.add(ambientLight, dirLight);

  let renderer = null;
  let webglAvailable = true;

  try {
    renderer = new THREE.WebGLRenderer({
      antialias: true,
      alpha: false,
      powerPreference: 'high-performance',
    });
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    renderer.setSize(width, height);
    if (container) {
      container.innerHTML = '';
      renderer.domElement.style.width = '100%';
      renderer.domElement.style.height = '100%';
      renderer.domElement.style.display = 'block';
      container.appendChild(renderer.domElement);
    }
  } catch {
    webglAvailable = false;
  }

  // Raycasting for click/hover calculation popovers
  const raycaster = new THREE.Raycaster();
  const pointerNDC = new THREE.Vector2();

  const findInteractiveHit = (clientX, clientY) => {
    if (!container) return null;
    const rect = container.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return null;
    pointerNDC.x = ((clientX - rect.left) / rect.width) * 2 - 1;
    pointerNDC.y = -((clientY - rect.top) / rect.height) * 2 + 1;
    raycaster.setFromCamera(pointerNDC, camera);

    const hits = raycaster.intersectObjects(scene.children, true);
    for (const hit of hits) {
      let curr = hit.object;
      while (curr) {
        if (curr.userData && curr.userData.interactiveId) {
          return curr.userData.interactiveId;
        }
        curr = curr.parent;
      }
    }
    return null;
  };

  // Project 3D world point [x, y, z] to 2D container pixel coordinates
  const projectToScreen = (pos3D) => {
    if (!container) return { x: 0, y: 0, visible: false };
    const w = container.clientWidth || width;
    const h = container.clientHeight || height;
    const vec = Array.isArray(pos3D)
      ? new THREE.Vector3(pos3D[0], pos3D[1], pos3D[2])
      : pos3D.clone();
    vec.project(camera);
    const visible = vec.z >= -1 && vec.z <= 1;
    return {
      x: (vec.x * 0.5 + 0.5) * w,
      y: (-vec.y * 0.5 + 0.5) * h,
      visible,
    };
  };

  const setCameraPreset = (preset) => {
    if (preset === 'top') {
      orbit.theta = 0;
      orbit.phi = 0.18;
    } else if (preset === 'front') {
      orbit.theta = 0;
      orbit.phi = Math.PI / 2 - 0.05;
    } else if (preset === 'side') {
      orbit.theta = Math.PI / 2;
      orbit.phi = Math.PI / 2 - 0.05;
    } else {
      orbit.theta = initialCamera.theta ?? 0.68;
      orbit.phi = initialCamera.phi ?? 1.08;
      orbit.radius = initialCamera.radius ?? 11.5;
    }
    syncCamera();
  };

  const orbitByDelta = (dx, dy) => {
    orbit.theta -= dx * 0.0085;
    orbit.phi = Math.max(0.18, Math.min(Math.PI - 0.18, orbit.phi - dy * 0.0085));
    syncCamera();
  };

  const zoomByDelta = (delta) => {
    orbit.radius = Math.max(4.5, Math.min(26, orbit.radius + delta * 0.01));
    syncCamera();
  };

  const resize = () => {
    if (!container || !renderer) return;
    const w = Math.max(260, container.clientWidth || 460);
    const h = Math.max(220, container.clientHeight || 320);
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
    renderer.setSize(w, h);
  };

  const renderFrame = () => {
    if (renderer && webglAvailable) {
      renderer.render(scene, camera);
    }
  };

  const dispose = () => {
    scene.traverse((obj) => {
      if (obj.geometry) obj.geometry.dispose();
      if (obj.material) {
        if (Array.isArray(obj.material)) {
          obj.material.forEach((m) => m.dispose());
        } else {
          obj.material.dispose();
        }
      }
    });
    if (renderer) {
      renderer.dispose();
      if (renderer.domElement && renderer.domElement.parentNode) {
        renderer.domElement.parentNode.removeChild(renderer.domElement);
      }
    }
  };

  return {
    scene,
    camera,
    orbit,
    webglAvailable,
    syncCamera,
    setCameraPreset,
    orbitByDelta,
    zoomByDelta,
    findInteractiveHit,
    projectToScreen,
    resize,
    renderFrame,
    dispose,
  };
}
