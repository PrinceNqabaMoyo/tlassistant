import React, { useRef, useEffect, useState, useId } from 'react';

/**
 * JSXGraphRenderer — renders interactive geometry diagrams using the JSXGraph
 * library loaded via CDN in index.html.
 *
 * @param {Object} config
 * @param {string} config.shape        - 'triangle' | 'quadrilateral' | 'circle' | 'polygon'
 * @param {Object} config.vertices     - Map of vertex labels to [x, y] coordinates,
 *                                        e.g. { A: [0, 0], B: [4, 0], C: [2, 3] }
 * @param {Object} [config.labels]     - Optional labels for sides and angles.
 * @param {Object} [config.labels.sides]  - e.g. { AB: '5 cm', BC: '7 cm' }
 * @param {Object} [config.labels.angles] - e.g. { A: '60°', B: '80°' }
 * @param {boolean} [config.interactive]  - If true, points are draggable.
 *
 * Usage:
 *   <JSXGraphRenderer config={{
 *     shape: 'triangle',
 *     vertices: { A: [0, 0], B: [4, 0], C: [2, 3] },
 *     labels: {
 *       sides: { AB: '5 cm', BC: '4 cm', CA: '3 cm' },
 *       angles: { A: '60°', B: '80°', C: '40°' },
 *     },
 *     interactive: true,
 *   }} />
 */
function JSXGraphRenderer({ config }) {
  const reactId = useId();
  // Build a DOM-safe id — useId() returns something like ":r1:" which isn't
  // valid as an HTML id attribute, so we sanitise it.
  const boardId = useRef(`jsxgraph-${reactId.replace(/[^a-zA-Z0-9]/g, '')}-${Math.random().toString(36).slice(2, 8)}`);
  const boardRef = useRef(null);
  const [jxgReady, setJxgReady] = useState(typeof window !== 'undefined' && !!window.JXG);
  const [error, setError] = useState(null);

  // --- Wait for the JXG global to appear ---
  useEffect(() => {
    if (window.JXG) {
      setJxgReady(true);
      return;
    }

    const interval = setInterval(() => {
      if (window.JXG) {
        setJxgReady(true);
        clearInterval(interval);
      }
    }, 100);

    const timeout = setTimeout(() => {
      clearInterval(interval);
      if (!window.JXG) {
        setError('JSXGraph library failed to load. Please check your internet connection.');
      }
    }, 10000);

    return () => {
      clearInterval(interval);
      clearTimeout(timeout);
    };
  }, []);

  // --- Initialise the board and draw the shape ---
  useEffect(() => {
    if (!jxgReady || !config || !config.vertices) return;

    // Clean up any previous board instance
    if (boardRef.current) {
      try {
        window.JXG.JSXGraph.freeBoard(boardRef.current);
      } catch (_) {
        /* ignore */
      }
      boardRef.current = null;
    }

    try {
      const { vertices, labels = {}, interactive = false, shape } = config;
      const vertexNames = Object.keys(vertices);
      const coords = vertexNames.map((name) => vertices[name]);

      // Compute a bounding box with some padding
      const xs = coords.map((c) => c[0]);
      const ys = coords.map((c) => c[1]);
      const pad = 2;
      const boundingBox = [
        Math.min(...xs) - pad,
        Math.max(...ys) + pad,
        Math.max(...xs) + pad,
        Math.min(...ys) - pad,
      ];

      const board = window.JXG.JSXGraph.initBoard(boardId.current, {
        boundingbox: boundingBox,
        axis: false,
        grid: false,
        showNavigation: false,
        showCopyright: false,
        keepaspectratio: true,
      });
      boardRef.current = board;

      // --- Create points ---
      const pointObjects = {};
      vertexNames.forEach((name, idx) => {
        pointObjects[name] = board.create('point', coords[idx], {
          name,
          size: 3,
          fixed: !interactive,
          label: {
            fontSize: 14,
            fontWeight: 'bold',
            offset: [8, 8],
          },
        });
      });

      // --- Handle circle shape separately ---
      if (shape === 'circle' && vertexNames.length >= 2) {
        // First vertex is the centre, second defines the radius
        const centre = pointObjects[vertexNames[0]];
        const radiusPoint = pointObjects[vertexNames[1]];
        board.create('circle', [centre, radiusPoint], {
          strokeColor: '#2563eb',
          strokeWidth: 2,
          fillColor: 'rgba(37, 99, 235, 0.06)',
        });

        // Label the radius if provided
        if (labels.sides) {
          const radiusKey = `${vertexNames[0]}${vertexNames[1]}`;
          const altRadiusKey = `${vertexNames[1]}${vertexNames[0]}`;
          const radiusLabel = labels.sides[radiusKey] || labels.sides[altRadiusKey];
          if (radiusLabel) {
            const seg = board.create('segment', [centre, radiusPoint], {
              strokeColor: '#2563eb',
              strokeWidth: 1,
              dash: 2,
            });
            board.create('text', [
              () => (centre.X() + radiusPoint.X()) / 2,
              () => (centre.Y() + radiusPoint.Y()) / 2 + 0.3,
              radiusLabel,
            ], {
              fontSize: 12,
              anchorX: 'middle',
              anchorY: 'bottom',
            });
          }
        }
      } else {
        // --- Draw edges (line segments) for polygon-like shapes ---
        const n = vertexNames.length;
        for (let i = 0; i < n; i++) {
          const from = vertexNames[i];
          const to = vertexNames[(i + 1) % n];

          board.create('segment', [pointObjects[from], pointObjects[to]], {
            strokeColor: '#2563eb',
            strokeWidth: 2,
          });

          // Side label at the midpoint
          if (labels.sides) {
            const sideKey = `${from}${to}`;
            const altSideKey = `${to}${from}`;
            const sideLabel = labels.sides[sideKey] || labels.sides[altSideKey];
            if (sideLabel) {
              board.create('text', [
                () => (pointObjects[from].X() + pointObjects[to].X()) / 2,
                () => (pointObjects[from].Y() + pointObjects[to].Y()) / 2 - 0.3,
                sideLabel,
              ], {
                fontSize: 12,
                anchorX: 'middle',
                anchorY: 'top',
                cssStyle: 'color: #4b5563;',
              });
            }
          }
        }

        // --- Draw angle arcs with labels ---
        if (labels.angles) {
          for (let i = 0; i < n; i++) {
            const vertexName = vertexNames[i];
            const angleLabel = labels.angles[vertexName];
            if (!angleLabel) continue;

            // For vertex i, the angle is formed by edges to (i-1) and (i+1)
            const prev = vertexNames[(i - 1 + n) % n];
            const next = vertexNames[(i + 1) % n];

            board.create('angle', [
              pointObjects[prev],
              pointObjects[vertexName],
              pointObjects[next],
            ], {
              radius: 0.6,
              name: angleLabel,
              label: { fontSize: 11, color: '#dc2626' },
              strokeColor: '#dc2626',
              fillColor: 'rgba(220, 38, 38, 0.08)',
              strokeWidth: 1,
            });
          }
        }

        // --- Optional filled polygon background ---
        if (n >= 3) {
          board.create('polygon', vertexNames.map((name) => pointObjects[name]), {
            fillColor: 'rgba(37, 99, 235, 0.04)',
            borders: { strokeWidth: 0 },
            withLines: false,
          });
        }
      }
    } catch (err) {
      setError(`Failed to render geometry: ${err.message}`);
    }

    // Cleanup on unmount
    return () => {
      if (boardRef.current) {
        try {
          window.JXG.JSXGraph.freeBoard(boardRef.current);
        } catch (_) {
          /* ignore */
        }
        boardRef.current = null;
      }
    };
  }, [jxgReady, config]);

  // --- Error state ---
  if (error) {
    return (
      <div
        style={{
          padding: '12px 16px',
          color: '#b91c1c',
          backgroundColor: '#fef2f2',
          border: '1px solid #fecaca',
          borderRadius: '6px',
          fontFamily: 'monospace',
          fontSize: '14px',
        }}
      >
        {error}
      </div>
    );
  }

  // --- Loading state ---
  if (!jxgReady) {
    return (
      <div
        style={{
          padding: '12px 16px',
          color: '#6b7280',
          fontStyle: 'italic',
          fontSize: '14px',
        }}
      >
        Loading geometry renderer…
      </div>
    );
  }

  // --- Board container ---
  return (
    <div
      id={boardId.current}
      style={{
        width: '400px',
        height: '400px',
        border: '1px solid #e5e7eb',
        borderRadius: '6px',
        backgroundColor: '#ffffff',
      }}
    />
  );
}

export default JSXGraphRenderer;
