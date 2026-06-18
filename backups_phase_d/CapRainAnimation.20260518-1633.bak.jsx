import React from 'react';
import GraduationCapSplash from './GraduationCapSplash';

const capSquares = [
  { left: '30%', top: '15%', size: '12%', rotate: '-4deg', delay: 0 },
  { left: '37%', top: '15%', size: '12%', rotate: '4deg', delay: 320 },
  { left: '26.5%', top: '26%', size: '13%', rotate: '-35deg', delay: 700 },
  { left: '33.5%', top: '37.5%', size: '13%', rotate: '37deg', delay: 1080 },
];

const CapRainAnimation = ({ className = '' }) => {
  return (
    <div className={`relative ${className}`}>
      <style>{`
        @keyframes fundile-square-drop {
          0% {
            opacity: 0;
            transform: translate3d(0, -110px, 0) scale(0.78);
          }
          68% {
            opacity: 1;
            transform: translate3d(0, 9px, 0) scale(1.05);
          }
          100% {
            opacity: 1;
            transform: translate3d(0, 0, 0) scale(1);
          }
        }

        @keyframes fundile-cap-glow {
          0%, 55% {
            filter: drop-shadow(0 0 0 rgba(255, 209, 102, 0));
          }
          100% {
            filter: drop-shadow(0 0 18px rgba(255, 209, 102, 0.28));
          }
        }
      `}</style>
      <div className="absolute inset-0 rounded-full bg-[radial-gradient(circle_at_center,_rgba(255,181,3,0.2),_transparent_60%)] blur-2xl" />
      <div className="relative h-full w-full">
        <div className="h-full w-full" style={{ animation: 'fundile-cap-glow 1700ms ease-out forwards' }}>
          <GraduationCapSplash className="h-full w-full" hideAccentSquares />
        </div>
        {capSquares.map((square, index) => (
          <div
            key={`${square.left}-${square.top}-${index}`}
            className="absolute"
            style={{
              left: square.left,
              top: square.top,
              height: square.size,
              width: square.size,
              transform: `rotate(${square.rotate})`,
            }}
          >
            <span
              className="block h-full w-full bg-[#FF9100] shadow-[0_0_16px_rgba(255,181,3,0.35)]"
              style={{
                animation: `fundile-square-drop 560ms cubic-bezier(0.22, 1, 0.36, 1) forwards`,
                animationDelay: `${square.delay}ms`,
                opacity: 0,
              }}
            />
          </div>
        ))}
      </div>
    </div>
  );
};

export default CapRainAnimation;
