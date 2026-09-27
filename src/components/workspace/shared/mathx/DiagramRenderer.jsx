import React from 'react';
import JXG from 'jsxgraph';

const { JSXGraph } = JXG;

let _boardSeq = 0;

const COLORS = {
    line: '#475569',
    fill: '#6366f1',
    label: '#0f172a',
    angle: '#6366f1',
    select: '#2563eb',
    correct: '#059669',
    wrong: '#dc2626',
    hint: '#94a3b8',
};

// Outward label offset per edge in the canonical right-triangle layout
// (A bottom-left = θ, B bottom-right = right angle, C apex top-right).
const EDGE_LABEL_OFFSET = {
    AB: [0, -0.45],
    BC: [0.5, 0],
    AC: [-0.55, 0.35],
};

/**
 * Render a right-triangle spec into a JSXGraph board.
 * Returns a cleanup function.
 */
function renderRightTriangle(spec, { id, interactive, selectedEdge, graded, correctEdge, selectRef }) {
    const pts = spec.points || {};
    const xs = Object.values(pts).map((p) => p[0]);
    const ys = Object.values(pts).map((p) => p[1]);
    const pad = 1.3;
    const bbox = [Math.min(...xs) - pad, Math.max(...ys) + pad, Math.max(...xs) + pad, Math.min(...ys) - pad];

    const board = JSXGraph.initBoard(id, {
        boundingbox: bbox,
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: true,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    const P = {};
    Object.entries(pts).forEach(([name, [x, y]]) => {
        P[name] = board.create('point', [x, y], {
            name: spec.vertex_labels?.[name] || '',
            size: 1,
            fixed: true,
            showInfobox: false,
            label: { offset: [6, 6], fontSize: 14, strokeColor: COLORS.label },
            fillColor: COLORS.line,
            strokeColor: COLORS.line,
            visible: !!spec.vertex_labels?.[name],
        });
    });

    board.create('polygon', [P.A, P.B, P.C], {
        fillColor: COLORS.fill,
        fillOpacity: 0.06,
        borders: { visible: false },
        vertices: { visible: false },
        withLines: false,
        fixed: true,
        highlight: false,
    });

    const edgeColor = (edge) => {
        if (graded) {
            if (edge === correctEdge) return COLORS.correct;
            if (edge === selectedEdge && selectedEdge !== correctEdge) return COLORS.wrong;
            return COLORS.line;
        }
        if (edge === selectedEdge) return COLORS.select;
        return COLORS.line;
    };

    (spec.sides || []).forEach((side) => {
        const edge = side.edge;
        const seg = board.create('segment', [P[side.from], P[side.to]], {
            strokeColor: edgeColor(edge),
            strokeWidth: edge === selectedEdge ? 4 : 2.5,
            fixed: true,
            highlight: interactive,
            highlightStrokeColor: interactive ? COLORS.select : edgeColor(edge),
            highlightStrokeWidth: interactive ? 4 : 2.5,
            cursor: interactive ? 'pointer' : 'default',
        });
        if (interactive && !graded) {
            seg.on('down', () => selectRef.current && selectRef.current(edge));
        }
        if (side.label) {
            const a = pts[side.from];
            const b = pts[side.to];
            const off = EDGE_LABEL_OFFSET[edge] || [0, 0];
            board.create('text', [(a[0] + b[0]) / 2 + off[0], (a[1] + b[1]) / 2 + off[1], side.label], {
                fontSize: 15,
                fixed: true,
                anchorX: 'middle',
                anchorY: 'middle',
                strokeColor: COLORS.label,
                highlight: false,
            });
        }
    });

    if (spec.right_angle_at && P[spec.right_angle_at]) {
        const v = spec.right_angle_at;
        const others = ['A', 'B', 'C'].filter((n) => n !== v);
        board.create('angle', [P[others[0]], P[v], P[others[1]]], {
            type: 'square',
            radius: 0.45,
            fillColor: COLORS.hint,
            fillOpacity: 0.5,
            strokeColor: COLORS.hint,
            fixed: true,
            name: '',
            withLabel: false,
            highlight: false,
        });
    }

    (spec.angles || []).forEach((ang) => {
        if (!P[ang.at]) return;
        const v = ang.at;
        const others = ['A', 'B', 'C'].filter((n) => n !== v);
        board.create('angle', [P[others[0]], P[v], P[others[1]]], {
            radius: 0.8,
            fillColor: COLORS.angle,
            fillOpacity: 0.12,
            strokeColor: COLORS.angle,
            fixed: true,
            name: ang.label || '',
            label: { fontSize: 15, strokeColor: COLORS.angle },
            highlight: false,
        });
    });

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * Render a number-line spec into a JSXGraph board.
 * Returns a cleanup function.
 */
function renderNumberLine(spec, { id }) {
    const minVal = spec.min ?? -5;
    const maxVal = spec.max ?? 5;
    const ticks = spec.ticks ?? 1;
    const pad = 1;
    const bbox = [minVal - pad, 1.5, maxVal + pad, -1.5];

    const board = JSXGraph.initBoard(id, {
        boundingbox: bbox,
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: false,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    // Main axis line
    board.create('segment', [[minVal, 0], [maxVal, 0]], {
        strokeColor: COLORS.line,
        strokeWidth: 2,
        fixed: true,
        lastArrow: { type: 1, size: 6 },
        highlight: false,
    });

    // Tick marks
    for (let t = Math.ceil(minVal / ticks) * ticks; t <= maxVal; t += ticks) {
        board.create('segment', [[t, -0.15], [t, 0.15]], {
            strokeColor: COLORS.line,
            strokeWidth: 1.5,
            fixed: true,
            highlight: false,
        });
        if (t !== 0) {
            board.create('text', [t, -0.55, String(t)], {
                fontSize: 12,
                fixed: true,
                anchorX: 'middle',
                anchorY: 'middle',
                strokeColor: COLORS.label,
                highlight: false,
            });
        }
    }

    // Zero label
    board.create('text', [0, -0.55, '0'], {
        fontSize: 12,
        fixed: true,
        anchorX: 'middle',
        anchorY: 'middle',
        strokeColor: COLORS.label,
        highlight: false,
    });

    // Point (open or closed dot)
    const pointAt = spec.point?.at ?? 0;
    const isClosed = spec.point?.closed ?? true;
    if (isClosed) {
        board.create('point', [pointAt, 0], {
            name: '',
            size: 4,
            fillColor: COLORS.line,
            strokeColor: COLORS.line,
            fixed: true,
            highlight: false,
        });
    } else {
        board.create('point', [pointAt, 0], {
            name: '',
            size: 4,
            fillColor: '#ffffff',
            strokeColor: COLORS.line,
            strokeWidth: 2,
            fixed: true,
            highlight: false,
        });
    }

    // Ray
    const rayDir = spec.ray?.direction ?? 'positive';
    if (rayDir === 'positive') {
        board.create('segment', [[pointAt, 0], [maxVal, 0]], {
            strokeColor: COLORS.select,
            strokeWidth: 4,
            fixed: true,
            highlight: false,
        });
    } else if (rayDir === 'negative') {
        board.create('segment', [[minVal, 0], [pointAt, 0]], {
            strokeColor: COLORS.select,
            strokeWidth: 4,
            fixed: true,
            highlight: false,
        });
    }

    // Label
    if (spec.label) {
        board.create('text', [(minVal + maxVal) / 2, 0.9, spec.label], {
            fontSize: 14,
            fixed: true,
            anchorX: 'middle',
            anchorY: 'middle',
            strokeColor: COLORS.label,
            highlight: false,
        });
    }

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * Render a triangle spec into a JSXGraph board.
 */
function renderTriangle(spec, { id }) {
    const pts = spec.points || {};
    const xs = Object.values(pts).map((p) => p[0]);
    const ys = Object.values(pts).map((p) => p[1]);
    const pad = 1.5;
    const bbox = [Math.min(...xs) - pad, Math.max(...ys) + pad, Math.max(...xs) + pad, Math.min(...ys) - pad];

    const board = JSXGraph.initBoard(id, {
        boundingbox: bbox,
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: true,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    const P = {};
    const verts = spec.vertices || ['A', 'B', 'C'];
    verts.forEach((name) => {
        const [x, y] = pts[name] || [0, 0];
        P[name] = board.create('point', [x, y], {
            name: name,
            size: 1,
            fixed: true,
            showInfobox: false,
            label: { offset: [6, 6], fontSize: 14, strokeColor: COLORS.label },
            fillColor: COLORS.line,
            strokeColor: COLORS.line,
        });
    });

    const edges = [];
    const trianglesList = (spec.triangles && spec.triangles.length > 0)
        ? spec.triangles
        : [verts];

    trianglesList.forEach((tVerts) => {
        for (let i = 0; i < tVerts.length; i++) {
            const from = tVerts[i];
            const to = tVerts[(i + 1) % tVerts.length];
            if (!P[from] || !P[to]) continue;
            const seg = board.create('segment', [P[from], P[to]], {
                strokeColor: COLORS.line,
                strokeWidth: 2.5,
                fixed: true,
                highlight: false,
            });
            edges.push({ from, to, seg });
            const label = (spec.side_labels || {})[`${from}${to}`] || (spec.side_labels || {})[`${to}${from}`] || '';
            if (label) {
                const a = pts[from];
                const b = pts[to];
                const dx = b[0] - a[0];
                const dy = b[1] - a[1];
                const len = Math.hypot(dx, dy) || 1;
                const nx = -dy / len;
                const ny = dx / len;
                board.create('text', [
                    (a[0] + b[0]) / 2 + nx * 0.45,
                    (a[1] + b[1]) / 2 + ny * 0.45,
                    label,
                ], {
                    fontSize: 15, fixed: true, anchorX: 'middle', anchorY: 'middle',
                    strokeColor: COLORS.label, highlight: false,
                });
            }
        }
    });

    // Tick marks for equal sides
    (spec.equal_sides || []).forEach((group) => {
        group.forEach((edgeKey) => {
            const edge = edges.find((e) => e.from + e.to === edgeKey || e.to + e.from === edgeKey);
            if (!edge) return;
            const a = pts[edge.from];
            const b = pts[edge.to];
            const mx = (a[0] + b[0]) / 2;
            const my = (a[1] + b[1]) / 2;
            const dx = b[0] - a[0];
            const dy = b[1] - a[1];
            const len = Math.hypot(dx, dy) || 1;
            const ux = -dy / len * 0.2;
            const uy = dx / len * 0.2;
            board.create('segment', [[mx - ux, my - uy], [mx + ux, my + uy]], {
                strokeColor: COLORS.line, strokeWidth: 2, fixed: true, highlight: false,
            });
        });
    });

    // Helper to find connected neighbor vertices along drawn edges
    const getConnectedNeighbors = (v) => {
        const neighbors = [];
        edges.forEach((e) => {
            if (e.from === v && !neighbors.includes(e.to)) neighbors.push(e.to);
            else if (e.to === v && !neighbors.includes(e.from)) neighbors.push(e.from);
        });
        return neighbors;
    };

    // Right angle square (supports single vertex string or array of vertices)
    const rightAngleVerts = Array.isArray(spec.right_angle_at)
        ? spec.right_angle_at
        : (spec.right_angle_at ? [spec.right_angle_at] : []);
    rightAngleVerts.forEach((v) => {
        if (!P[v]) return;
        const adj = getConnectedNeighbors(v);
        if (adj.length >= 2) {
            board.create('angle', [P[adj[0]], P[v], P[adj[1]]], {
                type: 'square', radius: 0.4, fillColor: COLORS.hint, fillOpacity: 0.5,
                strokeColor: COLORS.hint, fixed: true, name: '', withLabel: false, highlight: false,
            });
        }
    });

    // Angle arcs and labels
    const angleVals = spec.angle_values || {};
    const angleLabels = spec.angle_labels || {};
    verts.forEach((v) => {
        if (!P[v]) return;
        const adj = getConnectedNeighbors(v);
        if (adj.length < 2) return;
        const hasLabel = angleLabels[v];
        const hasValue = angleVals[v] !== undefined;
        if (hasLabel || hasValue) {
            const ang = board.create('angle', [P[adj[0]], P[v], P[adj[1]]], {
                radius: 0.7, fillColor: COLORS.angle, fillOpacity: 0.12,
                strokeColor: COLORS.angle, fixed: true,
                name: angleLabels[v] || '',
                label: { fontSize: 14, strokeColor: COLORS.angle },
                highlight: false,
            });
        }
    });

    // Explicit angle arcs if spec.angles is provided
    (spec.angles || []).forEach((ang) => {
        const arms = ang.arms || [];
        if (arms.length >= 3 && P[arms[0]] && P[arms[1]] && P[arms[2]]) {
            board.create('angle', [P[arms[0]], P[arms[1]], P[arms[2]]], {
                radius: ang.radius || 0.7,
                fillColor: COLORS.angle,
                fillOpacity: 0.12,
                strokeColor: COLORS.angle,
                fixed: true,
                name: ang.label || '',
                label: { fontSize: 14, strokeColor: COLORS.angle },
                highlight: false,
            });
        }
    });

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * Render a quadrilateral spec into a JSXGraph board.
 */
function renderQuadrilateral(spec, { id }) {
    const pts = spec.points || {};
    const xs = Object.values(pts).map((p) => p[0]);
    const ys = Object.values(pts).map((p) => p[1]);
    const pad = 1.5;
    const bbox = [Math.min(...xs) - pad, Math.max(...ys) + pad, Math.max(...xs) + pad, Math.min(...ys) - pad];

    const board = JSXGraph.initBoard(id, {
        boundingbox: bbox,
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: true,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    const P = {};
    const verts = spec.vertices || ['A', 'B', 'C', 'D'];
    verts.forEach((name) => {
        const [x, y] = pts[name] || [0, 0];
        P[name] = board.create('point', [x, y], {
            name: name,
            size: 1,
            fixed: true,
            showInfobox: false,
            label: { offset: [6, 6], fontSize: 14, strokeColor: COLORS.label },
            fillColor: COLORS.line,
            strokeColor: COLORS.line,
        });
    });

    // Polygon fill
    if (verts.length >= 3) {
        board.create('polygon', verts.map((v) => P[v]), {
            fillColor: COLORS.fill,
            fillOpacity: 0.06,
            borders: { visible: false },
            vertices: { visible: false },
            withLines: false,
            fixed: true,
            highlight: false,
        });
    }

    // Sides
    const edges = [];
    for (let i = 0; i < verts.length; i++) {
        const from = verts[i];
        const to = verts[(i + 1) % verts.length];
        const seg = board.create('segment', [P[from], P[to]], {
            strokeColor: COLORS.line,
            strokeWidth: 2.5,
            fixed: true,
            highlight: false,
        });
        edges.push({ from, to, seg });
        const label = (spec.side_labels || {})[`${from}${to}`] || '';
        if (label) {
            const a = pts[from];
            const b = pts[to];
            const dx = b[0] - a[0];
            const dy = b[1] - a[1];
            const len = Math.hypot(dx, dy) || 1;
            const nx = -dy / len;
            const ny = dx / len;
            board.create('text', [
                (a[0] + b[0]) / 2 + nx * 0.45,
                (a[1] + b[1]) / 2 + ny * 0.45,
                label,
            ], {
                fontSize: 15, fixed: true, anchorX: 'middle', anchorY: 'middle',
                strokeColor: COLORS.label, highlight: false,
            });
        }
    }

    // Diagonals
    if (spec.diagonals && verts.length === 4) {
        const d1 = board.create('segment', [P[verts[0]], P[verts[2]]], {
            strokeColor: COLORS.hint, strokeWidth: 1.5, dash: 2,
            fixed: true, highlight: false,
        });
        const d2 = board.create('segment', [P[verts[1]], P[verts[3]]], {
            strokeColor: COLORS.hint, strokeWidth: 1.5, dash: 2,
            fixed: true, highlight: false,
        });
    }

    // Tick marks for equal sides
    (spec.equal_sides || []).forEach((group) => {
        group.forEach((edgeKey) => {
            const edge = edges.find((e) => e.from + e.to === edgeKey || e.to + e.from === edgeKey);
            if (!edge) return;
            const a = pts[edge.from];
            const b = pts[edge.to];
            const mx = (a[0] + b[0]) / 2;
            const my = (a[1] + b[1]) / 2;
            const dx = b[0] - a[0];
            const dy = b[1] - a[1];
            const len = Math.hypot(dx, dy) || 1;
            const ux = -dy / len * 0.2;
            const uy = dx / len * 0.2;
            board.create('segment', [[mx - ux, my - uy], [mx + ux, my + uy]], {
                strokeColor: COLORS.line, strokeWidth: 2, fixed: true, highlight: false,
            });
        });
    });

    // Angle arcs and labels
    const angleLabels = spec.angle_labels || {};
    verts.forEach((v) => {
        if (!P[v]) return;
        const adj = verts.filter((n) => n !== v);
        if (adj.length < 2) return;
        const prev = adj[0];
        const next = adj[1];
        if (angleLabels[v]) {
            board.create('angle', [P[prev], P[v], P[next]], {
                radius: 0.7, fillColor: COLORS.angle, fillOpacity: 0.12,
                strokeColor: COLORS.angle, fixed: true,
                name: angleLabels[v],
                label: { fontSize: 14, strokeColor: COLORS.angle },
                highlight: false,
            });
        }
    });

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * Render an angle diagram spec into a JSXGraph board.
 */
function renderAngleDiagram(spec, { id }) {
    const board = JSXGraph.initBoard(id, {
        boundingbox: [-2, 2, 4, -2],
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: true,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    const O = board.create('point', [0, 0], {
        name: spec.vertex || 'O', size: 1, fixed: true, showInfobox: false,
        label: { offset: [6, 6], fontSize: 14, strokeColor: COLORS.label },
        fillColor: COLORS.line, strokeColor: COLORS.line,
    });

    const arms = spec.arms || ['OA', 'OB'];
    const armPts = [];
    if (arms.length >= 2) {
        const p1 = board.create('point', [3, 0], {
            name: arms[0], size: 1, fixed: true, showInfobox: false,
            label: { offset: [6, 6], fontSize: 14, strokeColor: COLORS.label },
            fillColor: COLORS.line, strokeColor: COLORS.line,
        });
        const p2 = board.create('point', [Math.cos((spec.angle_value || 60) * Math.PI / 180) * 3, Math.sin((spec.angle_value || 60) * Math.PI / 180) * 3], {
            name: arms[1], size: 1, fixed: true, showInfobox: false,
            label: { offset: [6, 6], fontSize: 14, strokeColor: COLORS.label },
            fillColor: COLORS.line, strokeColor: COLORS.line,
        });
        armPts.push(p1, p2);
        board.create('segment', [O, p1], { strokeColor: COLORS.line, strokeWidth: 2.5, fixed: true, highlight: false });
        board.create('segment', [O, p2], { strokeColor: COLORS.line, strokeWidth: 2.5, fixed: true, highlight: false });
    }

    if (spec.angle_arc && armPts.length === 2) {
        board.create('angle', [armPts[0], O, armPts[1]], {
            radius: 1.2, fillColor: COLORS.angle, fillOpacity: 0.12,
            strokeColor: COLORS.angle, fixed: true,
            name: spec.angle_label || `${spec.angle_value || 60}°`,
            label: { fontSize: 14, strokeColor: COLORS.angle },
            highlight: false,
        });
    }

    (spec.supplementary_angles || []).forEach((sa) => {
        const sx = Math.cos((sa.value || 120) * Math.PI / 180) * 3;
        const sy = Math.sin((sa.value || 120) * Math.PI / 180) * 3;
        const sp = board.create('point', [sx, sy], {
            name: sa.vertex || '', size: 1, fixed: true, showInfobox: false,
            label: { fontSize: 14, strokeColor: COLORS.label },
            fillColor: COLORS.line, strokeColor: COLORS.line,
        });
        board.create('segment', [O, sp], { strokeColor: COLORS.line, strokeWidth: 2.5, fixed: true, highlight: false });
    });

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * Render a parallel-transversal spec into a JSXGraph board.
 */
function renderParallelTransversal(spec, { id }) {
    const board = JSXGraph.initBoard(id, {
        boundingbox: [-0.5, 3, 6.5, -0.5],
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: false,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    const y1 = 2.5;
    const y2 = 0.5;

    // Two parallel horizontal lines
    const line1 = board.create('segment', [[0, y1], [6, y1]], {
        strokeColor: COLORS.line, strokeWidth: 2.5, fixed: true, highlight: false,
    });
    const line2 = board.create('segment', [[0, y2], [6, y2]], {
        strokeColor: COLORS.line, strokeWidth: 2.5, fixed: true, highlight: false,
    });

    // Transversal
    const trans = board.create('segment', [[1.5, -0.2], [4.5, 3.2]], {
        strokeColor: COLORS.line, strokeWidth: 2.5, fixed: true, highlight: false,
    });

    // Labels
    board.create('text', [0.2, y1 + 0.25, spec.line1_label || 'AB'], {
        fontSize: 14, fixed: true, anchorX: 'left', anchorY: 'middle', strokeColor: COLORS.label, highlight: false,
    });
    board.create('text', [0.2, y2 - 0.25, spec.line2_label || 'CD'], {
        fontSize: 14, fixed: true, anchorX: 'left', anchorY: 'middle', strokeColor: COLORS.label, highlight: false,
    });
    board.create('text', [4.7, 2.9, spec.transversal_label || 'EF'], {
        fontSize: 14, fixed: true, anchorX: 'left', anchorY: 'middle', strokeColor: COLORS.label, highlight: false,
    });

    // Given angle arc
    const given = spec.given_angle || 50;
    const pos = spec.given_position || 'top_left_interior';
    const isTop = pos.startsWith('top');
    const isLeft = pos.includes('left');
    const isExterior = pos.includes('exterior');

    const ly = isTop ? y1 : y2;
    const tx = isLeft ? 2.2 : 3.8;
    const ty = isTop ? (isExterior ? 3.0 : 1.8) : (isExterior ? 0.0 : 1.2);

    const angPt1 = board.create('point', [tx + (isLeft ? -0.8 : 0.8), ly], { visible: false, fixed: true });
    const angPt2 = board.create('point', [tx, ly], { visible: false, fixed: true });
    const angPt3 = board.create('point', [tx + (isLeft ? -0.6 : 0.6), ty], { visible: false, fixed: true });

    board.create('angle', [angPt1, angPt2, angPt3], {
        radius: 0.7, fillColor: COLORS.angle, fillOpacity: 0.12,
        strokeColor: COLORS.angle, fixed: true,
        name: `${given}°`,
        label: { fontSize: 14, strokeColor: COLORS.angle },
        highlight: false,
    });

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * Render circle geometry specs into a JSXGraph board.
 * Supports:
 * - circle_subtended_angle (angle at center = 2 * angle at circumference)
 * - circle_cyclic_quad (cyclic quad opposite angles, exterior angle)
 * - circle_tangent_secant (tangent-chord theorem, radius perpendicular to tangent)
 */
function renderCircleGeometry(spec, { id, interactive, selectedEdge, graded, correctEdge, selectRef }) {
    const pts = spec.points || {};
    const centerKey = spec.center || 'O';
    const centerCoord = pts[centerKey] || [0, 0];
    const radius = spec.radius || 3.0;

    const pad = 1.6;
    const bbox = [
        centerCoord[0] - radius - pad,
        centerCoord[1] + radius + pad,
        centerCoord[0] + radius + pad,
        centerCoord[1] - radius - pad,
    ];

    const board = JSXGraph.initBoard(id, {
        boundingbox: bbox,
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepAspectRatio: true,
        pan: { enabled: false },
        zoom: { enabled: false },
    });

    // 1. Create Points
    const P = {};
    Object.entries(pts).forEach(([name, [x, y]]) => {
        const isCenter = name === centerKey;
        const displayName = spec.vertex_labels?.[name] !== undefined ? spec.vertex_labels[name] : name;
        P[name] = board.create('point', [x, y], {
            name: displayName,
            size: isCenter ? 2 : 2.5,
            fixed: true,
            showInfobox: false,
            label: { offset: [6, 6], fontSize: 13, strokeColor: COLORS.label },
            fillColor: isCenter ? COLORS.hint : COLORS.line,
            strokeColor: COLORS.line,
            visible: displayName !== '',
        });
    });

    // 2. Draw Circle around center
    if (P[centerKey]) {
        board.create('circle', [P[centerKey], radius], {
            strokeColor: COLORS.line,
            strokeWidth: 2,
            fillColor: COLORS.fill,
            fillOpacity: 0.04,
            fixed: true,
            highlight: false,
        });
    }

    // 3. Draw Lines / Chords / Tangents
    const edgeColor = (edge) => {
        if (graded) {
            if (edge === correctEdge) return COLORS.correct;
            if (edge === selectedEdge && selectedEdge !== correctEdge) return COLORS.wrong;
            return COLORS.line;
        }
        if (edge === selectedEdge) return COLORS.select;
        return COLORS.line;
    };

    (spec.lines || []).forEach((pair) => {
        const from = pair[0];
        const to = pair[1];
        if (!P[from] || !P[to]) return;
        const edge = from < to ? from + to : to + from;
        const seg = board.create('segment', [P[from], P[to]], {
            strokeColor: edgeColor(edge),
            strokeWidth: edge === selectedEdge ? 4 : 2,
            fixed: true,
            highlight: interactive,
            highlightStrokeColor: interactive ? COLORS.select : edgeColor(edge),
            highlightStrokeWidth: interactive ? 4 : 2,
            cursor: interactive ? 'pointer' : 'default',
        });
        if (interactive && !graded) {
            seg.on('down', () => selectRef.current && selectRef.current(edge));
        }
    });

    // 4. Draw Angle Arcs with labels
    (spec.angles || []).forEach((ang) => {
        const arms = ang.arms || [];
        if (arms.length >= 3 && P[arms[0]] && P[arms[1]] && P[arms[2]]) {
            board.create('angle', [P[arms[0]], P[arms[1]], P[arms[2]]], {
                radius: ang.radius || 0.7,
                fillColor: COLORS.angle,
                fillOpacity: 0.12,
                strokeColor: COLORS.angle,
                fixed: true,
                name: ang.label || '',
                label: { fontSize: 13, strokeColor: COLORS.angle },
                highlight: false,
            });
        }
    });

    return () => {
        try { JSXGraph.freeBoard(board); } catch { /* already freed */ }
    };
}

/**
 * DiagramRenderer — turns a Diagram Spec (see backend ``_diagram.py``) into a
 * JSXGraph figure. The same spec renders a static figure or, when
 * ``interactive``, an answer surface whose clickable sides emit edge keys back
 * (the bidirectional Diagram Spec the procedure/marking pipeline consumes).
 *
 * Props:
 *   spec          the diagram spec object
 *   interactive   sides become clickable (for ``diagram_select``)
 *   selectedEdge  currently selected edge key ("AB" | "BC" | "AC")
 *   onSelectEdge  (edgeKey) => void
 *   graded        once marked, colour the correct/selected edges
 *   correctEdge   the correct edge key (for grading colours)
 */
const DiagramRenderer = ({
    spec,
    interactive = false,
    selectedEdge = null,
    onSelectEdge,
    graded = false,
    correctEdge = null,
}) => {
    const boxRef = React.useRef(null);
    const boardRef = React.useRef(null);
    const idRef = React.useRef(`jxgbox-${++_boardSeq}`);
    const selectRef = React.useRef(onSelectEdge);
    selectRef.current = onSelectEdge;

    const specKey = React.useMemo(() => JSON.stringify(spec || {}), [spec]);

    React.useEffect(() => {
        if (!spec || !boxRef.current) return undefined;

        if (spec.kind === 'right_triangle') {
            return renderRightTriangle(spec, {
                id: idRef.current, interactive, selectedEdge, graded, correctEdge, selectRef,
            });
        }

        if (spec.kind === 'number_line') {
            return renderNumberLine(spec, { id: idRef.current });
        }

        if (spec.kind === 'triangle') {
            return renderTriangle(spec, { id: idRef.current });
        }

        if (spec.kind === 'quadrilateral') {
            return renderQuadrilateral(spec, { id: idRef.current });
        }

        if (spec.kind === 'angle_diagram') {
            return renderAngleDiagram(spec, { id: idRef.current });
        }

        if (spec.kind === 'parallel_transversal') {
            return renderParallelTransversal(spec, { id: idRef.current });
        }

        if (['circle_subtended_angle', 'circle_cyclic_quad', 'circle_tangent_secant'].includes(spec.kind)) {
            return renderCircleGeometry(spec, {
                id: idRef.current, interactive, selectedEdge, graded, correctEdge, selectRef,
            });
        }

        return undefined;
    }, [specKey, interactive, selectedEdge, graded, correctEdge]); // eslint-disable-line react-hooks/exhaustive-deps

    if (!spec) return null;

    const isRightTriangle = spec.kind === 'right_triangle';
    const isNumberLine = spec.kind === 'number_line';
    const isDotPattern = spec.kind === 'dot_pattern';
    const isCircleGeometry = ['circle_subtended_angle', 'circle_cyclic_quad', 'circle_tangent_secant'].includes(spec.kind);
    const isGeometry = ['triangle', 'quadrilateral', 'angle_diagram', 'parallel_transversal'].includes(spec.kind) || isCircleGeometry;
    if (!isRightTriangle && !isNumberLine && !isDotPattern && !isGeometry) return null;

    if (isDotPattern) {
        return (
            <div className="flex flex-col items-center rounded-xl border border-slate-200 bg-white p-4">
                <p className="text-sm font-medium text-slate-700">
                    Pattern family: <span className="capitalize">{spec.family}</span>
                </p>
                {spec.count_rule ? (
                    <p className="mt-1 text-sm text-slate-600">
                        Count rule: <span className="font-mono">{spec.count_rule}</span>
                    </p>
                ) : null}
                <p className="mt-2 text-xs text-slate-400">Figure {spec.figure_index}</p>
                {spec.caption ? <p className="mt-1 text-xs text-slate-400">{spec.caption}</p> : null}
            </div>
        );
    }

    const boxStyle = isNumberLine
        ? { width: 400, height: 120, position: 'relative', overflow: 'hidden', userSelect: 'none' }
        : { width: 320, height: 250, position: 'relative', overflow: 'hidden', userSelect: 'none' };

    return (
        <div className="flex flex-col items-center">
            <div
                id={idRef.current}
                ref={boxRef}
                className="jxgbox rounded-xl border border-slate-200 bg-white"
                style={boxStyle}
            />
            {spec.caption ? <p className="mt-1 text-xs text-slate-400">{spec.caption}</p> : null}
        </div>
    );
};

export default DiagramRenderer;
