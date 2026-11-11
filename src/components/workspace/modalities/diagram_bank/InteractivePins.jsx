import React from 'react';

/**
 * Reusable interactive pin layer for biological, chemical, and physical vector diagrams.
 * Renders circular SVG badges with letter labels (A, B, C, D...) at relative (x%, y%) coordinates.
 */
export default function InteractivePins({ labels = [], activePin, onSelectPin, width = 400, height = 240 }) {
  if (!labels || labels.length === 0) return null;

  return (
    <g className="interactive-pins-layer">
      {labels.map((pin) => {
        const px = (pin.x / 100) * width;
        const py = (pin.y / 100) * height;
        const isSelected = activePin === pin.id;

        return (
          <g
            key={pin.id}
            data-testid={`bio-pin-${pin.id}`}
            className="cursor-pointer transition-transform hover:scale-110"
            onClick={() => onSelectPin && onSelectPin(pin.id)}
          >
            {/* Invisible large hit area */}
            <circle cx={px} cy={py} r="20" fill="transparent" pointerEvents="all" />
            
            {/* Pulsing ring when selected */}
            {isSelected && (
              <circle
                cx={px}
                cy={py}
                r="16"
                fill="none"
                stroke="#3b82f6"
                strokeWidth="2"
                strokeDasharray="3 2"
                className="animate-spin"
                style={{ transformOrigin: `${px}px ${py}px` }}
              />
            )}

            {/* Badge Background */}
            <circle
              cx={px}
              cy={py}
              r="12"
              fill={isSelected ? '#13519C' : '#ffffff'}
              stroke={isSelected ? '#13519C' : '#e11d48'}
              strokeWidth="2.5"
              className="drop-shadow-xs"
            />

            {/* Badge Letter */}
            <text
              x={px}
              y={py + 4}
              fontSize="11"
              fill={isSelected ? '#ffffff' : '#e11d48'}
              fontWeight="bold"
              textAnchor="middle"
              fontFamily="monospace"
              pointerEvents="none"
            >
              {pin.id}
            </text>
          </g>
        );
      })}
    </g>
  );
}
