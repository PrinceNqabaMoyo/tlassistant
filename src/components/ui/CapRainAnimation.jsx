import React from 'react';
import GraduationCapSplash from './GraduationCapSplash';

const capSquares = [
  { left: '30.5%', top: '15.5%', size: '5.4%', rotate: '-4deg', delay: 0 },
  { left: '36.8%', top: '15.5%', size: '5.4%', rotate: '4deg', delay: 320 },
  { left: '26.7%', top: '26.2%', size: '6.2%', rotate: '-35deg', delay: 700 },
  { left: '33.8%', top: '37.8%', size: '6.2%', rotate: '37deg', delay: 1080 },
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
      `}</style>
      <div className="relative h-full w-full">
        <GraduationCapSplash className="h-full w-full" hideAccentSquares />
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
              className="block h-full w-full bg-[#FF9100]"
              style={{
                animation: `fundile-square-drop 620ms cubic-bezier(0.22, 1, 0.36, 1) forwards`,
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
