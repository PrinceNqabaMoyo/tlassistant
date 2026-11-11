import React from 'react';
import { Activity } from 'lucide-react';

/**
 * AtlasSyncChartSvg
 *
 * High-DPI synchronized 2D SVG graph companion for 3D Paper & Ink Sidecar tools.
 * Plots live mathematical/physical curves (e.g., V(x) potential profile,
 * Heating curve T(Q), Boyle's Law P(V), Projectile y(t)/v(t), Enzyme rate vs pH,
 * Cubic optimization V(x)) with a live operating-point marker and plateau/landmark bands.
 */
export default function AtlasSyncChartSvg({
  title = 'Synchronized Mathematical & Physical Profile',
  subtitle = '',
  xLabel = 'x',
  yLabel = 'y',
  xDomain = [0, 10],
  yDomain = [0, 100],
  series = [],
  currentPoint = null,
  activePoint = null,
  landmarks = [],
  zones = [],
  height = 175,
  testId = 'atlas-sync-chart-svg',
}) {
  const opPoint = currentPoint || activePoint;
  const width = 480;
  const pad = { top: 22, right: 24, bottom: 32, left: 48 };
  const plotW = width - pad.left - pad.right;
  const plotH = height - pad.top - pad.bottom;

  const [xMin, xMax] = xDomain;
  const [yMin, yMax] = yDomain;
  const xSpan = Math.max(1e-6, xMax - xMin);
  const ySpan = Math.max(1e-6, yMax - yMin);

  const toX = (val) => pad.left + ((val - xMin) / xSpan) * plotW;
  const toY = (val) => pad.top + plotH - ((val - yMin) / ySpan) * plotH;

  // Generate 4 horizontal grid lines
  const yTicks = [0, 0.25, 0.5, 0.75, 1].map((t) => yMin + t * ySpan);
  const xTicks = [0, 0.25, 0.5, 0.75, 1].map((t) => xMin + t * xSpan);

  return (
    <div className="bg-white rounded-xl border border-slate-200 p-3 shadow-xs space-y-2">
      <div className="flex items-center justify-between gap-2">
        <div className="flex items-center gap-1.5">
          <Activity className="w-3.5 h-3.5 text-[#13519C]" />
          <span className="text-[11px] font-bold uppercase tracking-wider text-slate-700">
            {title}
          </span>
        </div>
        {subtitle && (
          <span className="text-[11px] font-mono font-semibold text-[#13519C] bg-indigo-50 px-2 py-0.5 rounded border border-indigo-200">
            {subtitle}
          </span>
        )}
      </div>

      <svg
        data-testid={testId}
        viewBox={`0 0 ${width} ${height}`}
        className="w-full h-auto select-none bg-[#FBFBF9] rounded-lg border border-slate-200/80"
      >
        {/* Shaded Phase / Operating Zones */}
        {zones.map((z, idx) => {
          const x1 = Math.max(pad.left, toX(z.xStart));
          const x2 = Math.min(pad.left + plotW, toX(z.xEnd));
          if (x2 <= x1) return null;
          return (
            <g key={idx}>
              <rect
                x={x1}
                y={pad.top}
                width={x2 - x1}
                height={plotH}
                fill={z.color || '#E0E7FF'}
                opacity={z.opacity ?? 0.35}
              />
              {z.label && (
                <text
                  x={(x1 + x2) / 2}
                  y={pad.top + 11}
                  textAnchor="middle"
                  fontSize="8.5"
                  fontWeight="700"
                  fill={z.textColor || '#3730A3'}
                  fontFamily="system-ui, sans-serif"
                >
                  {z.label}
                </text>
              )}
            </g>
          );
        })}

        {/* Grid Lines */}
        {yTicks.map((yv, idx) => {
          const py = toY(yv);
          return (
            <g key={`y-${idx}`}>
              <line
                x1={pad.left}
                y1={py}
                x2={pad.left + plotW}
                y2={py}
                stroke={Math.abs(yv) < 1e-4 ? '#94A3B8' : '#E2E8F0'}
                strokeWidth={Math.abs(yv) < 1e-4 ? '1.2' : '1'}
                strokeDasharray={Math.abs(yv) < 1e-4 ? undefined : '3 3'}
              />
              <text
                x={pad.left - 6}
                y={py + 3}
                textAnchor="end"
                fontSize="8.5"
                fill="#64748B"
                fontFamily="monospace"
              >
                {Number.isInteger(yv) ? yv : yv.toFixed(1)}
              </text>
            </g>
          );
        })}

        {xTicks.map((xv, idx) => {
          const px = toX(xv);
          return (
            <g key={`x-${idx}`}>
              <line
                x1={px}
                y1={pad.top}
                x2={px}
                y2={pad.top + plotH}
                stroke="#F1F5F9"
                strokeWidth="1"
              />
              <text
                x={px}
                y={pad.top + plotH + 12}
                textAnchor="middle"
                fontSize="8.5"
                fill="#64748B"
                fontFamily="monospace"
              >
                {Number.isInteger(xv) ? xv : xv.toFixed(1)}
              </text>
            </g>
          );
        })}

        {/* Axes Border */}
        <line
          x1={pad.left}
          y1={pad.top}
          x2={pad.left}
          y2={pad.top + plotH}
          stroke="#475569"
          strokeWidth="1.5"
        />
        <line
          x1={pad.left}
          y1={pad.top + plotH}
          x2={pad.left + plotW}
          y2={pad.top + plotH}
          stroke="#475569"
          strokeWidth="1.5"
        />

        {/* Axis Titles */}
        <text
          x={pad.left + plotW / 2}
          y={height - 4}
          textAnchor="middle"
          fontSize="9.5"
          fontWeight="700"
          fill="#334155"
        >
          {xLabel}
        </text>
        <text
          x={13}
          y={pad.top + plotH / 2}
          textAnchor="middle"
          fontSize="9.5"
          fontWeight="700"
          fill="#334155"
          transform={`rotate(-90, 13, ${pad.top + plotH / 2})`}
        >
          {yLabel}
        </text>

        {/* Series Curves */}
        {series.map((s, sIdx) => {
          const pts = s.points || [];
          if (pts.length === 0) return null;
          const d = pts
            .map((pt, i) => {
              const cx = Math.max(pad.left, Math.min(pad.left + plotW, toX(pt.x)));
              const cy = Math.max(pad.top, Math.min(pad.top + plotH, toY(pt.y)));
              return `${i === 0 ? 'M' : 'L'} ${cx.toFixed(1)} ${cy.toFixed(1)}`;
            })
            .join(' ');
          return (
            <path
              key={s.id || sIdx}
              d={d}
              fill="none"
              stroke={s.color || '#13519C'}
              strokeWidth={s.strokeWidth || 2.5}
              strokeDasharray={s.dashed ? '5 3' : undefined}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          );
        })}

        {/* Static Landmarks */}
        {landmarks.map((lm, idx) => {
          const lx = toX(lm.x);
          const ly = toY(lm.y);
          return (
            <g key={`lm-${idx}`}>
              <circle
                cx={lx}
                cy={ly}
                r="3.5"
                fill={lm.color || '#64748B'}
                stroke="#FFFFFF"
                strokeWidth="1.2"
              />
              {lm.label && (
                <text
                  x={lx + (lm.dx ?? 6)}
                  y={ly + (lm.dy ?? -6)}
                  fontSize="8.5"
                  fontWeight="700"
                  fill={lm.color || '#334155'}
                  fontFamily="monospace"
                >
                  {lm.label}
                </text>
              )}
            </g>
          );
        })}

        {/* Live Synchronized Operating Point */}
        {opPoint && (
          <g data-testid="sync-chart-operating-point">
            <line
              x1={toX(opPoint.x)}
              y1={pad.top}
              x2={toX(opPoint.x)}
              y2={pad.top + plotH}
              stroke={opPoint.color || '#E11D48'}
              strokeWidth="1.2"
              strokeDasharray="3 2"
            />
            <line
              x1={pad.left}
              y1={toY(opPoint.y)}
              x2={toX(opPoint.x)}
              y2={toY(opPoint.y)}
              stroke={opPoint.color || '#E11D48'}
              strokeWidth="1.2"
              strokeDasharray="3 2"
            />
            <circle
              cx={toX(opPoint.x)}
              cy={toY(opPoint.y)}
              r="5.5"
              fill={opPoint.color || '#E11D48'}
              stroke="#FFFFFF"
              strokeWidth="2"
            />
            {opPoint.label && (
              <g
                transform={`translate(${Math.min(
                  pad.left + plotW - 95,
                  Math.max(pad.left + 6, toX(opPoint.x) + 8)
                )}, ${Math.max(pad.top + 14, toY(opPoint.y) - 8)})`}
              >
                <rect
                  x="-3"
                  y="-10"
                  width={Math.max(58, opPoint.label.length * 5.4 + 8)}
                  height="14"
                  rx="3"
                  fill="#0F172A"
                  opacity="0.9"
                />
                <text
                  x="1"
                  y="0"
                  fontSize="8.5"
                  fontWeight="700"
                  fill="#F8FAFC"
                  fontFamily="monospace"
                >
                  {opPoint.label}
                </text>
              </g>
            )}
          </g>
        )}
      </svg>
    </div>
  );
}
