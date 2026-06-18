import React, { useState, useEffect, useCallback } from 'react';
import { RotateCcw, Maximize2, Settings, Zap } from 'lucide-react';

const InteractiveParameterControls = ({ 
  shapeType, 
  initialDimensions, 
  onParameterChange, 
  onReset,
  onMaximize,
  isGenerating = false 
}) => {
  const [dimensions, setDimensions] = useState(initialDimensions || {});
  const [isRealTime, setIsRealTime] = useState(true);
  const [animationSpeed, setAnimationSpeed] = useState(1);

  // Update dimensions when initialDimensions change
  useEffect(() => {
    setDimensions(initialDimensions || {});
  }, [initialDimensions]);

  // Real-time parameter update with debouncing
  const handleParameterChange = useCallback((param, value) => {
    const newDimensions = { ...dimensions, [param]: parseFloat(value) };
    setDimensions(newDimensions);
    
    if (isRealTime) {
      // Debounce real-time updates
      const timeoutId = setTimeout(() => {
        onParameterChange(newDimensions);
      }, 100);
      
      return () => clearTimeout(timeoutId);
    }
  }, [dimensions, isRealTime, onParameterChange]);

  // Manual update trigger
  const handleManualUpdate = useCallback(() => {
    onParameterChange(dimensions);
  }, [dimensions, onParameterChange]);

  // Reset to initial values
  const handleReset = useCallback(() => {
    setDimensions(initialDimensions || {});
    onReset();
  }, [initialDimensions, onReset]);

  // Generate parameter controls based on shape type
  const renderParameterControls = () => {
    switch (shapeType) {
      case 'cube':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Side Length: {dimensions.side_length?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="10"
                step="0.1"
                value={dimensions.side_length || 3}
                onChange={(e) => handleParameterChange('side_length', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
              <div className="flex justify-between text-xs text-gray-500 mt-1">
                <span>0.5 cm</span>
                <span>10 cm</span>
              </div>
            </div>
          </div>
        );

      case 'rectangular_prism':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Length: {dimensions.length?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="15"
                step="0.1"
                value={dimensions.length || 4}
                onChange={(e) => handleParameterChange('length', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
            
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Breadth: {dimensions.breadth?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="12"
                step="0.1"
                value={dimensions.breadth || 3}
                onChange={(e) => handleParameterChange('breadth', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
            
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Height: {dimensions.height?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="10"
                step="0.1"
                value={dimensions.height || 2}
                onChange={(e) => handleParameterChange('height', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
          </div>
        );

      case 'cylinder':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Radius: {dimensions.radius?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="8"
                step="0.1"
                value={dimensions.radius || 2}
                onChange={(e) => handleParameterChange('radius', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
            
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Height: {dimensions.height?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="15"
                step="0.1"
                value={dimensions.height || 5}
                onChange={(e) => handleParameterChange('height', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
          </div>
        );

      case 'sphere':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Radius: {dimensions.radius?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="0.5"
                max="6"
                step="0.1"
                value={dimensions.radius || 3}
                onChange={(e) => handleParameterChange('radius', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
          </div>
        );

      case 'triangle':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Base: {dimensions.base?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="1"
                max="20"
                step="0.1"
                value={dimensions.base || 8}
                onChange={(e) => handleParameterChange('base', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
            
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Height: {dimensions.height?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="1"
                max="15"
                step="0.1"
                value={dimensions.height || 6}
                onChange={(e) => handleParameterChange('height', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
          </div>
        );

      case 'rectangle':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Length: {dimensions.length?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="1"
                max="25"
                step="0.1"
                value={dimensions.length || 10}
                onChange={(e) => handleParameterChange('length', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
            
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Width: {dimensions.width?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="1"
                max="20"
                step="0.1"
                value={dimensions.width || 6}
                onChange={(e) => handleParameterChange('width', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
          </div>
        );

      case 'circle':
        return (
          <div className="space-y-4">
            <div className="parameter-control">
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Radius: {dimensions.radius?.toFixed(1)} cm
              </label>
              <input
                type="range"
                min="1"
                max="12"
                step="0.1"
                value={dimensions.radius || 5}
                onChange={(e) => handleParameterChange('radius', e.target.value)}
                className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
                disabled={isGenerating}
              />
            </div>
          </div>
        );

      default:
        return (
          <div className="text-center text-gray-500 py-4">
            <Settings className="w-8 h-8 mx-auto mb-2" />
            <p>No interactive controls available for this shape type.</p>
          </div>
        );
    }
  };

  return (
    <div className="bg-white rounded-lg border p-6">
      <div className="flex items-center justify-between mb-4">
        <h3 className="text-lg font-semibold text-gray-800 flex items-center">
          <Settings className="w-5 h-5 mr-2" />
          Interactive Controls
        </h3>
        
        <div className="flex items-center space-x-2">
          <label className="flex items-center text-sm text-gray-600">
            <input
              type="checkbox"
              checked={isRealTime}
              onChange={(e) => setIsRealTime(e.target.checked)}
              className="mr-2"
            />
            Real-time
          </label>
        </div>
      </div>

      {/* Parameter Controls */}
      <div className="mb-6">
        {renderParameterControls()}
      </div>

      {/* Control Buttons */}
      <div className="flex flex-wrap gap-2">
        {!isRealTime && (
          <button
            onClick={handleManualUpdate}
            disabled={isGenerating}
            className="flex items-center px-4 py-2 bg-blue-600 text-white rounded-md hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <Zap className="w-4 h-4 mr-2" />
            Update Shape
          </button>
        )}
        
        <button
          onClick={handleReset}
          disabled={isGenerating}
          className="flex items-center px-4 py-2 bg-gray-600 text-white rounded-md hover:bg-gray-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <RotateCcw className="w-4 h-4 mr-2" />
          Reset
        </button>
        
        <button
          onClick={onMaximize}
          disabled={isGenerating}
          className="flex items-center px-4 py-2 bg-green-600 text-white rounded-md hover:bg-green-700 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          <Maximize2 className="w-4 h-4 mr-2" />
          Maximize View
        </button>
      </div>

      {/* Animation Speed Control */}
      <div className="mt-4 pt-4 border-t">
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Animation Speed: {animationSpeed}x
        </label>
        <input
          type="range"
          min="0.5"
          max="3"
          step="0.5"
          value={animationSpeed}
          onChange={(e) => setAnimationSpeed(parseFloat(e.target.value))}
          className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer slider"
        />
        <div className="flex justify-between text-xs text-gray-500 mt-1">
          <span>0.5x</span>
          <span>3x</span>
        </div>
      </div>

      <style jsx>{`
        .slider::-webkit-slider-thumb {
          appearance: none;
          height: 20px;
          width: 20px;
          border-radius: 50%;
          background: #3b82f6;
          cursor: pointer;
          border: 2px solid #ffffff;
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
        
        .slider::-moz-range-thumb {
          height: 20px;
          width: 20px;
          border-radius: 50%;
          background: #3b82f6;
          cursor: pointer;
          border: 2px solid #ffffff;
          box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }
      `}</style>
    </div>
  );
};

export default InteractiveParameterControls;
