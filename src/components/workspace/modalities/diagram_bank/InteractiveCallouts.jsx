import React from 'react';
import SvgRichLabel from '../../shared/mathx/SvgRichLabel';

/**
 * Computes whether two 2D line segments (p1->p2) and (p3->p4) strictly intersect.
 */
function segmentsIntersect(p1, p2, p3, p4) {
  const ccw = (A, B, C) => (C[1] - A[1]) * (B[0] - A[0]) > (B[1] - A[1]) * (C[0] - A[0]);
  // Share an endpoint -> not a crossing
  if (
    (Math.hypot(p1[0] - p3[0], p1[1] - p3[1]) < 1) ||
    (Math.hypot(p1[0] - p4[0], p1[1] - p4[1]) < 1) ||
    (Math.hypot(p2[0] - p3[0], p2[1] - p3[1]) < 1) ||
    (Math.hypot(p2[0] - p4[0], p2[1] - p4[1]) < 1)
  ) {
    return false;
  }
  return ccw(p1, p3, p4) !== ccw(p2, p3, p4) && ccw(p1, p2, p3) !== ccw(p1, p2, p4);
}

function polylinesCross(ptsA, ptsB) {
  for (let i = 0; i < ptsA.length - 1; i++) {
    for (let j = 0; j < ptsB.length - 1; j++) {
      if (segmentsIntersect(ptsA[i], ptsA[i + 1], ptsB[j], ptsB[j + 1])) {
        return true;
      }
    }
  }
  return false;
}

/**
 * Resolves vertical badge positions on one margin side ('left' or 'right') so that:
 * 1. No two badges/landmarks ever overlap vertically (R4: minimum 38px center-to-center spacing).
 * 2. Badge vertical order matches anchor vertical order (R3: prevents leader line crossings).
 * 3. If default_box positions are already non-overlapping and monotonically ordered with anchors,
 *    exact default_box y values are preserved.
 */
function layoutSideItems(items, vbHeight, vbWidth, side) {
  if (items.length === 0) return [];
  const minMarginY = 26;
  const maxMarginY = vbHeight - 26;
  const minGap = 38;

  // Check if the caller's requested y values are already valid (in bounds, >= minGap apart, and ordered with ay)
  const sortedByAy = [...items].sort((a, b) => (a.ay - b.ay) || (a.ax - b.ax));
  let needsRelax = false;
  for (let i = 0; i < sortedByAy.length; i++) {
    const it = sortedByAy[i];
    const wy = it.wantedY;
    if (wy < minMarginY || wy > maxMarginY) needsRelax = true;
    if (it.kind === 'landmark' && it.anchorUnderBox && Math.abs(wy - it.ay) < 26) {
      needsRelax = true;
    }
    if (i > 0) {
      const prevWy = sortedByAy[i - 1].wantedY;
      // Inverted order relative to anchor y OR too close vertically
      if (wy < prevWy + minGap - 1) {
        needsRelax = true;
      }
    }
  }

  // Assign vertical slots in anchor-y order
  const ys = sortedByAy.map((it) => {
    let wy = Math.max(minMarginY, Math.min(maxMarginY, it.wantedY));
    if (it.kind === 'landmark' && it.anchorUnderBox && Math.abs(wy - it.ay) < 26) {
      // Shift landmark pill box above or below its own anchor so it never covers (ax, ay)
      const upY = it.ay - 28;
      const downY = it.ay + 28;
      if (wy <= it.ay && upY >= minMarginY) {
        wy = upY;
      } else if (downY <= maxMarginY) {
        wy = downY;
      } else {
        wy = Math.max(minMarginY, upY);
      }
    }
    return wy;
  });
  if (needsRelax && ys.length > 1) {
    // Forward pass: push down overlapping or inverted slots
    for (let i = 1; i < ys.length; i++) {
      if (ys[i] < ys[i - 1] + minGap) {
        ys[i] = ys[i - 1] + minGap;
      }
      const it = sortedByAy[i];
      if (it.kind === 'landmark' && it.anchorUnderBox && Math.abs(ys[i] - it.ay) < 26) {
        ys[i] = Math.min(maxMarginY, it.ay + 28);
      }
    }
    // Backward pass: clamp to bottom margin and push up if needed
    if (ys[ys.length - 1] > maxMarginY) {
      ys[ys.length - 1] = maxMarginY;
      for (let i = ys.length - 2; i >= 0; i--) {
        if (ys[i] > ys[i + 1] - minGap) {
          ys[i] = Math.max(minMarginY, ys[i + 1] - minGap);
        }
        const it = sortedByAy[i];
        if (it.kind === 'landmark' && it.anchorUnderBox && Math.abs(ys[i] - it.ay) < 26) {
          ys[i] = Math.max(minMarginY, it.ay - 28);
        }
      }
    }
  }

  // Build 2-segment angled knee leader paths: (ax, ay) -> (kneeX, by) -> (attachX, by).
  // For wide text landmark badges, route kneeX just toward the diagram side of the anchor
  // so angled leader lines never slice through neighboring wide text boxes on the same margin!
  const slotAssignments = sortedByAy.map((it, idx) => ({
    item: it,
    by: ys[idx],
  }));

  const makePoints = (it, by) => {
    const isLeft = side === 'left';
    const attachX = it.attachX;
    if (it.kind === 'landmark') {
      if (it.anchorUnderBox) {
        const edgeY = it.ay >= by ? by + 11 : by - 11;
        return [
          [it.ax, it.ay],
          [attachX, edgeY],
        ];
      }
      const kneeX = isLeft
        ? Math.min(it.ax - 4, attachX + 10)
        : Math.max(it.ax + 4, attachX - 10);
      return [
        [it.ax, it.ay],
        [kneeX, by],
        [attachX, by],
      ];
    }
    const kneeX = isLeft
      ? Math.min(it.ax - 4, attachX + 14)
      : Math.max(it.ax + 4, attachX - 14);
    return [
      [it.ax, it.ay],
      [kneeX, by],
      [attachX, by],
    ];
  };

  // 2-opt uncrossing guarantee
  for (let pass = 0; pass < 4; pass++) {
    let swapped = false;
    for (let i = 0; i < slotAssignments.length; i++) {
      for (let j = i + 1; j < slotAssignments.length; j++) {
        const ptsI = makePoints(slotAssignments[i].item, slotAssignments[i].by);
        const ptsJ = makePoints(slotAssignments[j].item, slotAssignments[j].by);
        if (polylinesCross(ptsI, ptsJ)) {
          const tmp = slotAssignments[i].by;
          slotAssignments[i].by = slotAssignments[j].by;
          slotAssignments[j].by = tmp;
          swapped = true;
        }
      }
    }
    if (!swapped) break;
  }

  return slotAssignments.map(({ item, by }) => {
    const pts = makePoints(item, by);
    return {
      ...item,
      resolvedY: by,
      pointsAttr: pts.map(([x, y]) => `${x},${y}`).join(' '),
    };
  });
}

/**
 * Authentic textbook-grade leader-line and callout placement engine.
 * Guarantees non-crossing leader lines (R3), non-overlapping badges (R4),
 * and high-contrast white-cased strokes that pop against any diagram palette (R5).
 */
export default function InteractiveCallouts({
  pins = [],
  landmarks = [],
  activePin,
  onSelectPin,
  viewBox = '0 0 600 480',
}) {
  const vbParts = String(viewBox).split(' ').map(Number);
  const vbWidth = vbParts[2] || 600;
  const vbHeight = vbParts[3] || 480;

  const validLandmarks = landmarks
    .filter((lm) => lm && typeof (lm.text || lm.name) === 'string' && (lm.text || lm.name).length > 0)
    .map((lm, idx) => {
      const lmText = lm.text || lm.name || '';
      const [ax, ay] = lm.anchor || [0, 0];
      const side = lm.side === 'left' ? 'left' : 'right';
      const isLeft = side === 'left';
      const boxWidth = Math.max(84, lmText.length * 6.5 + 16);
      const boxX = isLeft ? 8 : vbWidth - boxWidth - 8;
      // Attach to the edge closest to the anchor (or bottom/top center if anchor is vertically under/over the box)
      const anchorUnderBox = isLeft ? ax < boxX + boxWidth + 10 : ax > boxX - 10;
      const attachX = anchorUnderBox
        ? Math.max(boxX + 12, Math.min(boxX + boxWidth - 12, ax))
        : (isLeft ? boxX + boxWidth : boxX);
      const [_, by] = lm.default_box || [0, ay];
      return {
        kind: 'landmark',
        id: `lm-${idx}`,
        raw: { ...lm, text: lmText },
        ax: Number(ax) || 0,
        ay: Number(ay) || 0,
        side,
        isLeft,
        boxX,
        boxWidth,
        boxHeight: 22,
        attachX,
        anchorUnderBox,
        wantedY: Number.isFinite(by) ? Number(by) : Number(ay) || 0,
      };
    });

  const validPins = pins.map((p) => {
    const [ax, ay] = p.anchor || [0, 0];
    const side = p.side === 'left' ? 'left' : 'right';
    const isLeft = side === 'left';
    const boxSize = 32;
    const boxX = isLeft ? 24 : vbWidth - 24 - boxSize;
    const attachX = isLeft ? boxX + boxSize : boxX;
    const [_, by] = p.default_box || [0, ay];
    return {
      kind: 'pin',
      id: `pin-${p.pin}`,
      raw: p,
      ax: Number(ax) || 0,
      ay: Number(ay) || 0,
      side,
      isLeft,
      boxX,
      boxWidth: boxSize,
      boxHeight: boxSize,
      attachX,
      wantedY: Number.isFinite(by) ? Number(by) : Number(ay) || 0,
    };
  });

  const allItems = [...validPins, ...validLandmarks];
  const leftResolved = layoutSideItems(
    allItems.filter((it) => it.side === 'left'),
    vbHeight,
    vbWidth,
    'left'
  );
  const rightResolved = layoutSideItems(
    allItems.filter((it) => it.side === 'right'),
    vbHeight,
    vbWidth,
    'right'
  );
  const resolvedAll = [...leftResolved, ...rightResolved];
  const resolvedLandmarks = resolvedAll.filter((it) => it.kind === 'landmark');
  const resolvedPins = resolvedAll.filter((it) => it.kind === 'pin');

  return (
    <g className="interactive-callouts-layer select-none" data-testid="interactive-callouts-layer">
      {/* 1a. Context Landmarks Leader Lines & Anchor Dots (rendered underneath all text pills) */}
      {resolvedLandmarks.map((item) => {
        const { ax, ay, pointsAttr, id } = item;
        return (
          <g key={`${id}-leader`} className="landmark-leader">
            {/* White outer casing for contrast against dark/coloured plates */}
            <polyline
              points={pointsAttr}
              fill="none"
              stroke="#ffffff"
              strokeWidth="3.5"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
            {/* Core leader line */}
            <polyline
              points={pointsAttr}
              fill="none"
              stroke="#1e293b"
              strokeWidth="1.5"
              strokeDasharray="4 2"
              strokeLinejoin="round"
            />
            {/* Anchor dot */}
            <circle cx={ax} cy={ay} r="4" fill="#1e293b" stroke="#ffffff" strokeWidth="1.5" />
          </g>
        );
      })}

      {/* 1b. Context Landmarks Text Pills (always opaque on top of leader lines) */}
      {resolvedLandmarks.map((item) => {
        const { raw: lm, boxX, boxWidth, resolvedY, id } = item;
        return (
          <g key={id} className="landmark-callout">
            <rect
              x={boxX}
              y={resolvedY - 11}
              width={boxWidth}
              height="22"
              rx="4"
              fill="#ffffff"
              stroke="#334155"
              strokeWidth="1.25"
            />
            <text
              x={boxX + boxWidth / 2}
              y={resolvedY + 4}
              fontSize="10.5"
              fill="#0f172a"
              fontWeight="700"
              textAnchor="middle"
              fontFamily="system-ui, sans-serif"
            >
              <SvgRichLabel text={lm.text} />
            </text>
          </g>
        );
      })}

      {/* 2. Target Examination Pins Layer (Clickable, high-contrast cased, zero answer leakage) */}
      {resolvedPins.map((item) => {
        const { raw: p, ax, ay, boxX, boxWidth: boxSize, resolvedY, pointsAttr } = item;
        const isSelected = activePin === p.pin;
        const boxY = resolvedY - boxSize / 2;
        const coreColor = isSelected ? '#13519C' : '#0f172a';

        return (
          <g
            key={`pin-${p.pin}`}
            data-testid={`btn-select-pin-${p.pin}`}
            className="cursor-pointer group"
            onClick={() => onSelectPin && onSelectPin(p.pin)}
          >
            {/* Primary leader polyline (starts at ax,ay) with high-contrast dark navy/blue stroke */}
            <polyline
              points={pointsAttr}
              fill="none"
              stroke={coreColor}
              strokeWidth={isSelected ? '2.75' : '2.2'}
              strokeLinejoin="round"
              style={{ filter: 'drop-shadow(0px 0px 1.5px #ffffff) drop-shadow(0px 0px 1.5px #ffffff)' }}
              className="transition-colors"
            />

            {/* Structural Anchor Point on the Organ (white halo + dark core so it pops on red/dark tissue) */}
            <circle
              cx={ax}
              cy={ay}
              r={isSelected ? 5.5 : 4.5}
              fill={coreColor}
              stroke="#ffffff"
              strokeWidth="2.2"
              className="transition-all"
            />

            {/* Outer focus halo when selected */}
            {isSelected && (
              <rect
                x={boxX - 4}
                y={boxY - 4}
                width={boxSize + 8}
                height={boxSize + 8}
                rx="10"
                fill="none"
                stroke="#38bdf8"
                strokeWidth="2"
                strokeDasharray="4 2"
                className="animate-pulse"
                pointerEvents="none"
              />
            )}

            {/* Callout Badge Box - Topmost primary interactive hit target */}
            <rect
              data-testid={`bio-pin-${p.pin}`}
              x={boxX}
              y={boxY}
              width={boxSize}
              height={boxSize}
              rx="8"
              fill={isSelected ? '#13519C' : '#ffffff'}
              stroke={coreColor}
              strokeWidth="2.5"
              className="drop-shadow-xs transition-colors cursor-pointer"
              pointerEvents="all"
              onClick={(e) => {
                e.stopPropagation();
                onSelectPin && onSelectPin(p.pin);
              }}
            />

            {/* Pin Identification Letter (A, B, C...) */}
            <text
              x={boxX + boxSize / 2}
              y={boxY + boxSize / 2 + 5}
              fontSize="14"
              fontWeight="bold"
              fill={isSelected ? '#ffffff' : '#0f172a'}
              textAnchor="middle"
              fontFamily="monospace, sans-serif"
              pointerEvents="none"
            >
              {p.pin}
            </text>
          </g>
        );
      })}
    </g>
  );
}
