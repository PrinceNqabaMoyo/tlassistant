import React from 'react';

/**
 * ComplexPlaneExplorerThumbnail
 * Miniature preview icon/card for Complex Plane Explorer:
 * Displays Argand plane crosshair, rotational vector +i, and orthogonal indicator.
 */
export default function ComplexPlaneExplorerThumbnail({ width = 80, height = 60 }) {
  return (
    <div
      className="w-full h-full bg-gradient-to-br from-indigo-900/60 to-purple-900/60 rounded-lg flex flex-col items-center justify-center p-1.5 border border-indigo-500/40 relative overflow-hidden"
      style={{ width: `${width}px`, height: `${height}px` }}
    >
      {/* Mini Argand Axes */}
      <svg viewBox="-30 -20 60 40" className="w-full h-full">
        {/* Real and Imaginary Axes */}
        <line x1="-26" y1="0" x2="26" y2="0" stroke="#38bdf8" strokeWidth="1" />
        <line x1="0" y1="-18" x2="0" y2="18" stroke="#c084fc" strokeWidth="1" strokeDasharray="2 1" />

        {/* Mini unit circle */}
        <circle cx="0" cy="0" r="12" fill="none" stroke="#6366f1" strokeWidth="0.75" strokeOpacity="0.6" />

        {/* 90-degree Rotation Arc */}
        <path
          d="M 10 0 A 10 10 0 0 0 0 -10"
          fill="none"
          stroke="#ec4899"
          strokeWidth="1.2"
          strokeDasharray="2 1"
        />

        {/* Root vector to +i */}
        <line x1="0" y1="0" x2="0" y2="-12" stroke="#f472b6" strokeWidth="1.5" />
        <circle cx="0" cy="-12" r="2" fill="#ec4899" />

        {/* Complex notation */}
        <text x="3" y="-13" fill="#f472b6" fontSize="5" fontWeight="bold">
          +i
        </text>
        <text x="14" y="5" fill="#38bdf8" fontSize="4.5">
          Re
        </text>
      </svg>
      <div className="absolute bottom-0.5 inset-x-0 text-[8px] font-bold text-center text-cyan-200 uppercase tracking-tighter truncate px-1">
        Complex i
      </div>
    </div>
  );
}
