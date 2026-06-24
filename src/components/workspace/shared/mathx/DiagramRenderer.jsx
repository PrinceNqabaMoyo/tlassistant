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
        if (!spec || spec.kind !== 'right_triangle' || !boxRef.current) return undefined;
        const pts = spec.points || {};
        const xs = Object.values(pts).map((p) => p[0]);
        const ys = Object.values(pts).map((p) => p[1]);
        const pad = 1.3;
        const bbox = [Math.min(...xs) - pad, Math.max(...ys) + pad, Math.max(...xs) + pad, Math.min(...ys) - pad];

        const board = JSXGraph.initBoard(idRef.current, {
            boundingbox: bbox,
            axis: false,
            grid: false,
            showNavigation: false,
            showCopyright: false,
            keepAspectRatio: true,
            pan: { enabled: false },
            zoom: { enabled: false },
        });
        boardRef.current = board;

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

        // Triangle fill (non-interactive backdrop).
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
            // Side label at the midpoint, offset outward.
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

        // Right-angle marker.
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

        // Marked angles (e.g. θ at A).
        (spec.angles || []).forEach((ang) => {
            if (!P[ang.at]) return;
            const v = ang.at;
            // Order the two rays so the arc opens into the triangle.
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
            boardRef.current = null;
        };
    }, [specKey, interactive, selectedEdge, graded, correctEdge]); // eslint-disable-line react-hooks/exhaustive-deps

    if (!spec || spec.kind !== 'right_triangle') return null;

    return (
        <div className="flex flex-col items-center">
            <div
                id={idRef.current}
                ref={boxRef}
                className="jxgbox rounded-xl border border-slate-200 bg-white"
                style={{ width: 320, height: 250, position: 'relative', overflow: 'hidden', userSelect: 'none' }}
            />
            {spec.caption ? <p className="mt-1 text-xs text-slate-400">{spec.caption}</p> : null}
        </div>
    );
};

export default DiagramRenderer;
