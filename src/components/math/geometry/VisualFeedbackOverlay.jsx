import React, { useState, useEffect, useRef } from 'react';
import { Eye, EyeOff, Info, CheckCircle, AlertCircle, Lightbulb } from 'lucide-react';

const VisualFeedbackOverlay = ({ 
  diagramData, 
  shapeType, 
  dimensions, 
  calculations, 
  showMeasurements = true,
  showFormulas = true,
  showHints = false,
  onToggleHint,
  hintText = ""
}) => {
  const [overlayVisible, setOverlayVisible] = useState(true);
  const [activeOverlay, setActiveOverlay] = useState('measurements');
  const [animationKey, setAnimationKey] = useState(0);

  // Force re-render when diagram data changes
  useEffect(() => {
    setAnimationKey(prev => prev + 1);
  }, [diagramData, dimensions]);

  // Generate measurement overlays based on shape type
  const generateMeasurementOverlays = () => {
    if (!dimensions) return [];

    const overlays = [];

    switch (shapeType) {
      case 'cube':
        overlays.push({
          id: 'side-length',
          type: 'dimension',
          label: `${dimensions.side_length?.toFixed(1)} cm`,
          position: { x: 50, y: 20 },
          color: '#ef4444',
          description: 'Side Length'
        });
        break;

      case 'rectangular_prism':
        overlays.push(
          {
            id: 'length',
            type: 'dimension',
            label: `${dimensions.length?.toFixed(1)} cm`,
            position: { x: 30, y: 15 },
            color: '#ef4444',
            description: 'Length'
          },
          {
            id: 'breadth',
            type: 'dimension',
            label: `${dimensions.breadth?.toFixed(1)} cm`,
            position: { x: 70, y: 15 },
            color: '#3b82f6',
            description: 'Breadth'
          },
          {
            id: 'height',
            type: 'dimension',
            label: `${dimensions.height?.toFixed(1)} cm`,
            position: { x: 50, y: 85 },
            color: '#10b981',
            description: 'Height'
          }
        );
        break;

      case 'cylinder':
        overlays.push(
          {
            id: 'radius',
            type: 'dimension',
            label: `r = ${dimensions.radius?.toFixed(1)} cm`,
            position: { x: 50, y: 20 },
            color: '#ef4444',
            description: 'Radius'
          },
          {
            id: 'height',
            type: 'dimension',
            label: `h = ${dimensions.height?.toFixed(1)} cm`,
            position: { x: 50, y: 80 },
            color: '#3b82f6',
            description: 'Height'
          }
        );
        break;

      case 'sphere':
        overlays.push({
          id: 'radius',
          type: 'dimension',
          label: `r = ${dimensions.radius?.toFixed(1)} cm`,
          position: { x: 50, y: 50 },
          color: '#ef4444',
          description: 'Radius'
        });
        break;

      case 'triangle':
        overlays.push(
          {
            id: 'base',
            type: 'dimension',
            label: `${dimensions.base?.toFixed(1)} cm`,
            position: { x: 50, y: 90 },
            color: '#ef4444',
            description: 'Base'
          },
          {
            id: 'height',
            type: 'dimension',
            label: `${dimensions.height?.toFixed(1)} cm`,
            position: { x: 20, y: 50 },
            color: '#3b82f6',
            description: 'Height'
          }
        );
        break;

      case 'rectangle':
        overlays.push(
          {
            id: 'length',
            type: 'dimension',
            label: `${dimensions.length?.toFixed(1)} cm`,
            position: { x: 50, y: 10 },
            color: '#ef4444',
            description: 'Length'
          },
          {
            id: 'width',
            type: 'dimension',
            label: `${dimensions.width?.toFixed(1)} cm`,
            position: { x: 10, y: 50 },
            color: '#3b82f6',
            description: 'Width'
          }
        );
        break;

      case 'circle':
        overlays.push({
          id: 'radius',
          type: 'dimension',
          label: `r = ${dimensions.radius?.toFixed(1)} cm`,
          position: { x: 50, y: 50 },
          color: '#ef4444',
          description: 'Radius'
        });
        break;
    }

    return overlays;
  };

  // Generate formula overlays
  const generateFormulaOverlays = () => {
    if (!calculations) return [];

    const formulas = [];

    switch (shapeType) {
      case 'cube':
        formulas.push({
          id: 'volume-formula',
          type: 'formula',
          label: 'V = s³',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Volume Formula'
        });
        formulas.push({
          id: 'surface-area-formula',
          type: 'formula',
          label: 'SA = 6s²',
          position: { x: 10, y: 25 },
          color: '#f59e0b',
          description: 'Surface Area Formula'
        });
        break;

      case 'rectangular_prism':
        formulas.push({
          id: 'volume-formula',
          type: 'formula',
          label: 'V = l × b × h',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Volume Formula'
        });
        formulas.push({
          id: 'surface-area-formula',
          type: 'formula',
          label: 'SA = 2(lb + lh + bh)',
          position: { x: 10, y: 25 },
          color: '#f59e0b',
          description: 'Surface Area Formula'
        });
        break;

      case 'cylinder':
        formulas.push({
          id: 'volume-formula',
          type: 'formula',
          label: 'V = πr²h',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Volume Formula'
        });
        formulas.push({
          id: 'surface-area-formula',
          type: 'formula',
          label: 'SA = 2πr(r + h)',
          position: { x: 10, y: 25 },
          color: '#f59e0b',
          description: 'Surface Area Formula'
        });
        break;

      case 'sphere':
        formulas.push({
          id: 'volume-formula',
          type: 'formula',
          label: 'V = (4/3)πr³',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Volume Formula'
        });
        formulas.push({
          id: 'surface-area-formula',
          type: 'formula',
          label: 'SA = 4πr²',
          position: { x: 10, y: 25 },
          color: '#f59e0b',
          description: 'Surface Area Formula'
        });
        break;

      case 'triangle':
        formulas.push({
          id: 'area-formula',
          type: 'formula',
          label: 'A = ½ × b × h',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Area Formula'
        });
        break;

      case 'rectangle':
        formulas.push({
          id: 'area-formula',
          type: 'formula',
          label: 'A = l × w',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Area Formula'
        });
        formulas.push({
          id: 'perimeter-formula',
          type: 'formula',
          label: 'P = 2(l + w)',
          position: { x: 10, y: 25 },
          color: '#f59e0b',
          description: 'Perimeter Formula'
        });
        break;

      case 'circle':
        formulas.push({
          id: 'area-formula',
          type: 'formula',
          label: 'A = πr²',
          position: { x: 10, y: 10 },
          color: '#8b5cf6',
          description: 'Area Formula'
        });
        formulas.push({
          id: 'circumference-formula',
          type: 'formula',
          label: 'C = 2πr',
          position: { x: 10, y: 25 },
          color: '#f59e0b',
          description: 'Circumference Formula'
        });
        break;
    }

    return formulas;
  };

  // Generate calculation result overlays
  const generateCalculationOverlays = () => {
    if (!calculations) return [];

    const results = [];
    let yOffset = 10;

    Object.entries(calculations).forEach(([key, value]) => {
      if (typeof value === 'number' && !isNaN(value)) {
        results.push({
          id: key,
          type: 'calculation',
          label: `${key.replace('_', ' ').toUpperCase()}: ${value.toFixed(2)}`,
          position: { x: 70, y: yOffset },
          color: '#059669',
          description: 'Calculation Result'
        });
        yOffset += 15;
      }
    });

    return results;
  };

  const measurementOverlays = generateMeasurementOverlays();
  const formulaOverlays = generateFormulaOverlays();
  const calculationOverlays = generateCalculationOverlays();

  const allOverlays = [
    ...(showMeasurements ? measurementOverlays : []),
    ...(showFormulas ? formulaOverlays : []),
    ...calculationOverlays
  ];

  return (
    <div className="relative">
      {/* Overlay Controls */}
      <div className="flex items-center justify-between mb-4 p-3 bg-gray-50 rounded-lg">
        <div className="flex items-center space-x-4">
          <button
            onClick={() => setOverlayVisible(!overlayVisible)}
            className={`flex items-center px-3 py-2 rounded-md text-sm font-medium ${
              overlayVisible 
                ? 'bg-blue-100 text-blue-700' 
                : 'bg-gray-100 text-gray-600'
            }`}
          >
            {overlayVisible ? <Eye className="w-4 h-4 mr-2" /> : <EyeOff className="w-4 h-4 mr-2" />}
            {overlayVisible ? 'Hide Overlays' : 'Show Overlays'}
          </button>

          <div className="flex space-x-2">
            <button
              onClick={() => setActiveOverlay('measurements')}
              className={`px-3 py-1 rounded text-sm ${
                activeOverlay === 'measurements' 
                  ? 'bg-red-100 text-red-700' 
                  : 'bg-gray-100 text-gray-600'
              }`}
            >
              Measurements
            </button>
            <button
              onClick={() => setActiveOverlay('formulas')}
              className={`px-3 py-1 rounded text-sm ${
                activeOverlay === 'formulas' 
                  ? 'bg-purple-100 text-purple-700' 
                  : 'bg-gray-100 text-gray-600'
              }`}
            >
              Formulas
            </button>
            <button
              onClick={() => setActiveOverlay('calculations')}
              className={`px-3 py-1 rounded text-sm ${
                activeOverlay === 'calculations' 
                  ? 'bg-green-100 text-green-700' 
                  : 'bg-gray-100 text-gray-600'
              }`}
            >
              Results
            </button>
          </div>
        </div>

        {/* Hint Toggle */}
        {hintText && (
          <button
            onClick={onToggleHint}
            className={`flex items-center px-3 py-2 rounded-md text-sm font-medium ${
              showHints 
                ? 'bg-yellow-100 text-yellow-700' 
                : 'bg-gray-100 text-gray-600'
            }`}
          >
            <Lightbulb className="w-4 h-4 mr-2" />
            {showHints ? 'Hide Hint' : 'Show Hint'}
          </button>
        )}
      </div>

      {/* Hint Display */}
      {showHints && hintText && (
        <div className="mb-4 p-4 bg-yellow-50 border border-yellow-200 rounded-lg">
          <div className="flex items-start">
            <Lightbulb className="w-5 h-5 text-yellow-600 mt-0.5 mr-3 flex-shrink-0" />
            <div>
              <h4 className="font-medium text-yellow-800 mb-1">Hint</h4>
              <p className="text-yellow-700 text-sm">{hintText}</p>
            </div>
          </div>
        </div>
      )}

      {/* Overlay Container */}
      {overlayVisible && (
        <div 
          className="absolute inset-0 pointer-events-none z-10"
          key={animationKey}
        >
          {allOverlays
            .filter(overlay => {
              if (activeOverlay === 'measurements') return overlay.type === 'dimension';
              if (activeOverlay === 'formulas') return overlay.type === 'formula';
              if (activeOverlay === 'calculations') return overlay.type === 'calculation';
              return true;
            })
            .map((overlay) => (
              <div
                key={overlay.id}
                className="absolute transform -translate-x-1/2 -translate-y-1/2 pointer-events-auto"
                style={{
                  left: `${overlay.position.x}%`,
                  top: `${overlay.position.y}%`,
                }}
              >
                <div
                  className={`px-3 py-1 rounded-full text-sm font-medium shadow-lg border-2 border-white animate-pulse ${
                    overlay.type === 'dimension' ? 'bg-red-100 text-red-800' :
                    overlay.type === 'formula' ? 'bg-purple-100 text-purple-800' :
                    'bg-green-100 text-green-800'
                  }`}
                  style={{ borderColor: overlay.color }}
                >
                  {overlay.label}
                </div>
                
                {/* Tooltip */}
                <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-2 py-1 bg-gray-800 text-white text-xs rounded opacity-0 hover:opacity-100 transition-opacity duration-200 pointer-events-auto">
                  {overlay.description}
                </div>
              </div>
            ))}
        </div>
      )}

      {/* Animation Styles */}
      <style jsx>{`
        @keyframes pulse {
          0%, 100% { opacity: 1; }
          50% { opacity: 0.7; }
        }
        
        .animate-pulse {
          animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
      `}</style>
    </div>
  );
};

export default VisualFeedbackOverlay;
