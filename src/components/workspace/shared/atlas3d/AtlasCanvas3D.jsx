import React, { useEffect, useRef, useState, useCallback, useMemo } from 'react';
import { Compass, RotateCcw, MousePointerClick } from 'lucide-react';
import { createAtlasViewport } from './atlasRenderEngine';

/**
 * AtlasCanvas3D
 *
 * Reusable React wrapper for the Three.js Paper & Ink 3D Visualization Engine.
 * Supports:
 *   - Smooth pointer-drag 3D orbit and wheel zoom
 *   - Camera angle presets (3D Isometric, Top Plan, Front Elevation, Side View)
 *   - Raycasting click & hover detection on 3D vectors/parts (`interactiveId`)
 *   - Synchronized 2D screen-projected floating math/value badges (`floatingLabels` or `badgeItems`)
 *   - Clean WebGL resource disposal on unmount
 */
export default function AtlasCanvas3D({
  buildScene,
  sceneDeps = [],
  initialCamera = { radius: 8.2, theta: 0.65, phi: 1.08, target: [0, 0.5, 0] },
  floatingLabels = [],
  badgeItems = [],
  activeInteractiveId = null,
  selectedId = null,
  onSelectInteractive,
  onSelect,
  heightClass = 'h-[300px] sm:h-[330px]',
  badgeText = 'Paper & Ink 3D Simulation',
  subBadgeText = 'Drag to orbit 3D • Click any vector or part for calculation',
  subtitle = '',
  testId = 'atlas-canvas-3d',
}) {
  const containerRef = useRef(null);
  const viewportRef = useRef(null);
  const animFrameRef = useRef(null);
  const stepCallbackRef = useRef(null);
  const isDraggingRef = useRef(false);
  const dragDistRef = useRef(0);
  const lastPointerRef = useRef({ x: 0, y: 0 });

  const effectiveSelectedId = selectedId ?? activeInteractiveId;
  const effectiveOnSelect = onSelect || onSelectInteractive;
  const effectiveSubBadge = subtitle || subBadgeText;

  // Normalize floating labels from either floatingLabels or badgeItems
  const normalizedLabels = useMemo(() => {
    if (floatingLabels && floatingLabels.length > 0) return floatingLabels;
    if (badgeItems && badgeItems.length > 0) {
      return badgeItems.map((b, idx) => ({
        id: b.id || `badge-${idx}`,
        interactiveId: b.id,
        text: b.badgeText || b.shortLabel || b.label,
        color: b.color || '#13519C',
        position: b.position || [(idx - (badgeItems.length - 1) / 2) * 1.45, 1.55 + (idx % 2) * 0.35, 0],
      }));
    }
    return [];
  }, [floatingLabels, badgeItems]);

  const [cameraAngles, setCameraAngles] = useState({ thetaDeg: 37, phiDeg: 62 });
  const [hoveredId, setHoveredId] = useState(null);
  const [projectedBadges, setProjectedBadges] = useState([]);

  const updateProjectedBadges = useCallback(() => {
    const vp = viewportRef.current;
    if (!vp || normalizedLabels.length === 0) {
      setProjectedBadges([]);
      return;
    }
    const next = normalizedLabels.map((lbl) => {
      const proj = vp.projectToScreen(lbl.position || [0, 0, 0]);
      return {
        ...lbl,
        screenX: proj.x,
        screenY: proj.y,
        visible: proj.visible,
      };
    });
    setProjectedBadges(next);
  }, [normalizedLabels]);

  // Initialize Three.js Paper & Ink Viewport
  useEffect(() => {
    const el = containerRef.current;
    if (!el) return;

    const vp = createAtlasViewport({
      container: el,
      initialCamera,
      onCameraChange: (angles) => {
        setCameraAngles(angles);
      },
    });
    viewportRef.current = vp;

    const resizeObserver =
      typeof ResizeObserver !== 'undefined'
        ? new ResizeObserver(() => {
            vp.resize();
            vp.renderFrame();
          })
        : null;
    if (resizeObserver) resizeObserver.observe(el);

    return () => {
      if (resizeObserver) resizeObserver.disconnect();
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
      vp.dispose();
      viewportRef.current = null;
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // Rebuild or update 3D scene contents when parameters or buildScene change
  useEffect(() => {
    const vp = viewportRef.current;
    if (!vp || typeof buildScene !== 'function') return;

    // Clear previous dynamic objects (keep base lights/grid at indices 0, 1)
    while (vp.scene.children.length > 2) {
      const child = vp.scene.children[vp.scene.children.length - 1];
      vp.scene.remove(child);
    }

    const result = buildScene({
      scene: vp.scene,
      camera: vp.camera,
      renderFrame: vp.renderFrame,
    });

    if (typeof result?.update === 'function') {
      stepCallbackRef.current = (dt, elapsed) => result.update(dt, elapsed);
    } else if (typeof result?.onTick === 'function') {
      stepCallbackRef.current = (_dt, elapsed) => result.onTick(elapsed);
    } else {
      stepCallbackRef.current = null;
    }

    vp.renderFrame();
    updateProjectedBadges();

    if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
    let startTime = performance.now();
    let prevTime = startTime;
    const loop = (now) => {
      const dt = Math.min(0.05, (now - prevTime) * 0.001);
      prevTime = now;
      const elapsedSec = (now - startTime) * 0.001;
      if (stepCallbackRef.current) {
        stepCallbackRef.current(dt, elapsedSec);
      }
      vp.renderFrame();
      animFrameRef.current = requestAnimationFrame(loop);
    };
    animFrameRef.current = requestAnimationFrame(loop);

    return () => {
      if (animFrameRef.current) cancelAnimationFrame(animFrameRef.current);
      if (typeof result?.cleanup === 'function') result.cleanup();
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [buildScene, ...sceneDeps, updateProjectedBadges]);

  // Pointer Orbit & Raycast Selection Handlers
  const handlePointerDown = (e) => {
    isDraggingRef.current = true;
    dragDistRef.current = 0;
    lastPointerRef.current = { x: e.clientX, y: e.clientY };
  };

  const handlePointerMove = (e) => {
    const vp = viewportRef.current;
    if (!vp) return;

    if (isDraggingRef.current) {
      const dx = e.clientX - lastPointerRef.current.x;
      const dy = e.clientY - lastPointerRef.current.y;
      dragDistRef.current += Math.hypot(dx, dy);
      lastPointerRef.current = { x: e.clientX, y: e.clientY };
      vp.orbitByDelta(dx, dy);
      updateProjectedBadges();
    } else {
      const hitId = vp.findInteractiveHit(e.clientX, e.clientY);
      setHoveredId(hitId);
    }
  };

  const handlePointerUp = (e) => {
    const wasDragging = isDraggingRef.current;
    const totalDrag = dragDistRef.current;
    isDraggingRef.current = false;

    if (wasDragging && totalDrag < 6 && viewportRef.current) {
      const hitId = viewportRef.current.findInteractiveHit(e.clientX, e.clientY);
      if (hitId && effectiveOnSelect) {
        effectiveOnSelect(hitId);
      }
    }
  };

  const handlePreset = (preset) => {
    if (!viewportRef.current) return;
    viewportRef.current.setCameraPreset(preset);
    updateProjectedBadges();
  };

  return (
    <div
      data-testid={testId}
      className="relative w-full rounded-2xl overflow-hidden border border-slate-300 bg-[#FBFBF9] shadow-sm select-none"
    >
      {/* Top Floating Editorial Header Bar */}
      <div className="px-3 py-2 bg-white/95 backdrop-blur-xs border-b border-slate-200 flex flex-wrap items-center justify-between gap-2 z-20 relative">
        <div className="flex items-center gap-2">
          <span className="px-2 py-0.5 rounded-md bg-[#13519C] text-white text-[10px] font-bold uppercase tracking-wider">
            {badgeText}
          </span>
          <span className="text-[11px] text-slate-600 hidden sm:inline items-center gap-1">
            {effectiveSubBadge}
          </span>
        </div>

        {/* Camera Angle Presets */}
        <div className="flex items-center gap-1">
          {[
            { id: 'iso', label: '3D Orbit' },
            { id: 'front', label: 'Front' },
            { id: 'top', label: 'Top Plan' },
            { id: 'side', label: 'Side' },
          ].map((view) => (
            <button
              key={view.id}
              type="button"
              data-testid={`btn-camera-${view.id}`}
              onClick={() => handlePreset(view.id)}
              className="px-2 py-0.5 rounded text-[10px] font-semibold bg-slate-100 hover:bg-slate-200 text-slate-700 border border-slate-200/80 transition-colors"
            >
              {view.label}
            </button>
          ))}
          <button
            type="button"
            data-testid="btn-camera-reset"
            onClick={() => handlePreset('iso')}
            className="p-1 rounded bg-slate-100 hover:bg-slate-200 text-slate-600 border border-slate-200/80"
            title="Reset 3D camera"
          >
            <RotateCcw className="w-3 h-3" />
          </button>
        </div>
      </div>

      {/* Main Three.js WebGL Paper & Ink Canvas Area */}
      <div className={`relative w-full ${heightClass}`}>
        <div
          ref={containerRef}
          onPointerDown={handlePointerDown}
          onPointerMove={handlePointerMove}
          onPointerUp={handlePointerUp}
          onPointerLeave={() => {
            isDraggingRef.current = false;
            setHoveredId(null);
          }}
          className={`w-full h-full ${
            hoveredId ? 'cursor-pointer' : 'cursor-grab active:cursor-grabbing'
          }`}
        />

        {/* Floating Screen-Projected Interactive Value & Vector Badges */}
        <div className="absolute inset-0 pointer-events-none overflow-hidden">
          {projectedBadges.map((lbl, idx) => {
            if (!lbl.visible) return null;
            const isSelected = effectiveSelectedId && lbl.interactiveId === effectiveSelectedId;
            const isHovered = hoveredId && lbl.interactiveId === hoveredId;
            return (
              <button
                key={lbl.id || idx}
                type="button"
                data-testid={
                  lbl.interactiveId ? `badge-3d-${lbl.interactiveId}` : `badge-3d-${idx}`
                }
                onClick={(e) => {
                  e.stopPropagation();
                  if (lbl.interactiveId && effectiveOnSelect) {
                    effectiveOnSelect(lbl.interactiveId);
                  }
                }}
                style={{
                  left: `${Math.max(14, Math.min(86, (lbl.screenX / 460) * 100))}%`,
                  top: `${Math.max(12, Math.min(82, (lbl.screenY / 320) * 100))}%`,
                  transform: 'translate(-50%, -50%)',
                  borderColor: lbl.color || '#13519C',
                }}
                className={`pointer-events-auto absolute px-2 py-0.5 rounded-full text-[10px] font-mono font-bold shadow-xs border transition-transform ${
                  isSelected || isHovered
                    ? 'bg-slate-900 text-white scale-110 z-20 ring-2 ring-amber-400'
                    : 'bg-white/95 text-slate-900 hover:scale-105 z-10'
                }`}
              >
                <span
                  className="inline-block w-2 h-2 rounded-full mr-1"
                  style={{ backgroundColor: lbl.color || '#13519C' }}
                />
                {lbl.text}
              </button>
            );
          })}
        </div>

        {/* Bottom-Left Camera Telemetry & Hint Pill */}
        <div className="absolute bottom-2.5 left-2.5 right-2.5 flex items-center justify-between pointer-events-none z-10">
          <div className="px-2.5 py-1 rounded-full bg-slate-900/80 text-white text-[10px] font-mono flex items-center gap-1.5 shadow-xs">
            <Compass className="w-3 h-3 text-sky-400" />
            <span>
              Orbit θ:{cameraAngles.thetaDeg}° φ:{cameraAngles.phiDeg}°
            </span>
          </div>

          <div className="px-2.5 py-1 rounded-full bg-white/90 border border-slate-300 text-slate-700 text-[10px] font-semibold flex items-center gap-1 shadow-xs">
            <MousePointerClick className="w-3 h-3 text-[#13519C]" />
            <span>Click any vector/part for live formula</span>
          </div>
        </div>
      </div>
    </div>
  );
}
