import React, { useState } from 'react';

// Motion Graphs Component
const MotionGraphs = ({
  initialData = {
    graphType: 'position_time',
    data: [
      { time: 0, position: 0, velocity: 0, acceleration: 2 },
      { time: 1, position: 1, velocity: 2, acceleration: 2 },
      { time: 2, position: 4, velocity: 4, acceleration: 2 },
      { time: 3, position: 9, velocity: 6, acceleration: 2 },
      { time: 4, position: 16, velocity: 8, acceleration: 2 }
    ],
    showGrid: true,
    showLabels: true,
    selectedPoint: null
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const addDataPoint = () => {
    const lastPoint = data.data[data.data.length - 1];
    const newPoint = {
      time: lastPoint.time + 1,
      position: lastPoint.position + lastPoint.velocity + 0.5 * lastPoint.acceleration,
      velocity: lastPoint.velocity + lastPoint.acceleration,
      acceleration: lastPoint.acceleration
    };
    const newData = { ...data, data: [...data.data, newPoint] };
    handleDataChange(newData);
  };

  const resetData = () => {
    const resetData = { ...data, data: initialData.data };
    handleDataChange(resetData);
  };

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Motion Graphs</h3>
      
      <div className="mb-4 space-y-2">
        <div className="flex items-center space-x-4">
          <label className="flex items-center">
            <input
              type="radio"
              name="graphType"
              value="position_time"
              checked={data.graphType === 'position_time'}
              onChange={(e) => handleDataChange({ ...data, graphType: e.target.value })}
              className="mr-2"
            />
            Position vs Time
          </label>
          <label className="flex items-center">
            <input
              type="radio"
              name="graphType"
              value="velocity_time"
              checked={data.graphType === 'velocity_time'}
              onChange={(e) => handleDataChange({ ...data, graphType: e.target.value })}
              className="mr-2"
            />
            Velocity vs Time
          </label>
          <label className="flex items-center">
            <input
              type="radio"
              name="graphType"
              value="acceleration_time"
              checked={data.graphType === 'acceleration_time'}
              onChange={(e) => handleDataChange({ ...data, graphType: e.target.value })}
              className="mr-2"
            />
            Acceleration vs Time
          </label>
        </div>
        
        <div className="flex space-x-2">
          <button
            onClick={addDataPoint}
            className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Add Point
          </button>
          <button
            onClick={resetData}
            className="px-3 py-1 bg-gray-500 text-white rounded hover:bg-gray-600"
          >
            Reset
          </button>
        </div>
      </div>

      <div className="mb-4">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showGrid}
            onChange={(e) => handleDataChange({ ...data, showGrid: e.target.checked })}
            className="mr-2"
          />
          Show Grid
        </label>
        <label className="flex items-center ml-4">
          <input
            type="checkbox"
            checked={data.showLabels}
            onChange={(e) => handleDataChange({ ...data, showLabels: e.target.checked })}
            className="mr-2"
          />
          Show Labels
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[300px]">
        <div className="text-center text-gray-600">
          {data.graphType === 'position_time' && 'Position vs Time Graph'}
          {data.graphType === 'velocity_time' && 'Velocity vs Time Graph'}
          {data.graphType === 'acceleration_time' && 'Acceleration vs Time Graph'}
        </div>
        
        <div className="mt-4 space-y-2">
          {data.data.map((point, index) => (
            <div key={index} className="flex space-x-4 text-sm">
              <span>t={point.time}s:</span>
              <span>s={point.position.toFixed(1)}m</span>
              <span>v={point.velocity.toFixed(1)}m/s</span>
              <span>a={point.acceleration.toFixed(1)}m/s²</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Force Diagram Component
const ForceDiagram = ({
  initialData = {
    forces: [
      { name: 'Weight', magnitude: 50, direction: 'down', color: '#ef4444' },
      { name: 'Normal', magnitude: 50, direction: 'up', color: '#3b82f6' },
      { name: 'Friction', magnitude: 10, direction: 'left', color: '#f59e0b' }
    ],
    showComponents: true,
    showResultant: true,
    selectedForce: null
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const addForce = () => {
    const newForce = {
      name: `Force ${data.forces.length + 1}`,
      magnitude: 20,
      direction: 'right',
      color: `#${Math.floor(Math.random()*16777215).toString(16)}`
    };
    const newData = { ...data, forces: [...data.forces, newForce] };
    handleDataChange(newData);
  };

  const removeForce = (index) => {
    const newForces = data.forces.filter((_, i) => i !== index);
    const newData = { ...data, forces: newForces };
    handleDataChange(newData);
  };

  const calculateResultant = () => {
    let fx = 0, fy = 0;
    data.forces.forEach(force => {
      const angle = getDirectionAngle(force.direction);
      fx += force.magnitude * Math.cos(angle);
      fy += force.magnitude * Math.sin(angle);
    });
    return Math.sqrt(fx * fx + fy * fy);
  };

  const getDirectionAngle = (direction) => {
    const angles = { up: -Math.PI/2, down: Math.PI/2, left: Math.PI, right: 0 };
    return angles[direction] || 0;
  };

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Force Diagram</h3>
      
      <div className="mb-4">
        <button
          onClick={addForce}
          className="px-3 py-1 bg-green-500 text-white rounded hover:bg-green-600"
        >
          Add Force
        </button>
      </div>

      <div className="mb-4 space-y-2">
        {data.forces.map((force, index) => (
          <div key={index} className="flex items-center space-x-2 p-2 border rounded">
            <input
              type="text"
              value={force.name}
              onChange={(e) => {
                const newForces = [...data.forces];
                newForces[index].name = e.target.value;
                handleDataChange({ ...data, forces: newForces });
              }}
              className="w-20 px-2 py-1 border rounded"
            />
            <input
              type="number"
              value={force.magnitude}
              onChange={(e) => {
                const newForces = [...data.forces];
                newForces[index].magnitude = parseFloat(e.target.value) || 0;
                handleDataChange({ ...data, forces: newForces });
              }}
              className="w-16 px-2 py-1 border rounded"
            />
            <select
              value={force.direction}
              onChange={(e) => {
                const newForces = [...data.forces];
                newForces[index].direction = e.target.value;
                handleDataChange({ ...data, forces: newForces });
              }}
              className="px-2 py-1 border rounded"
            >
              <option value="up">Up</option>
              <option value="down">Down</option>
              <option value="left">Left</option>
              <option value="right">Right</option>
            </select>
            <input
              type="color"
              value={force.color}
              onChange={(e) => {
                const newForces = [...data.forces];
                newForces[index].color = e.target.value;
                handleDataChange({ ...data, forces: newForces });
              }}
              className="w-8 h-8 border rounded"
            />
            <button
              onClick={() => removeForce(index)}
              className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
            >
              ×
            </button>
          </div>
        ))}
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showComponents}
            onChange={(e) => handleDataChange({ ...data, showComponents: e.target.checked })}
            className="mr-2"
          />
          Show Force Components
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showResultant}
            onChange={(e) => handleDataChange({ ...data, showResultant: e.target.checked })}
            className="mr-2"
          />
          Show Resultant Force
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[200px]">
        <div className="text-center text-gray-600 mb-4">Force Diagram Visualization</div>
        
        {data.showResultant && (
          <div className="text-center p-2 bg-blue-100 rounded">
            <strong>Resultant Force:</strong> {calculateResultant().toFixed(2)} N
          </div>
        )}
        
        <div className="mt-4 space-y-1 text-sm">
          {data.forces.map((force, index) => (
            <div key={index} className="flex items-center space-x-2">
              <div
                className="w-4 h-4 rounded"
                style={{ backgroundColor: force.color }}
              ></div>
              <span>{force.name}: {force.magnitude}N {force.direction}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Pulse Simulator Component
const PulseSimulator = ({
  initialData = {
    pulseType: 'transverse',
    amplitude: 20,
    pulseWidth: 50,
    speed: 2,
    isAnimating: true,
    showGrid: true,
    showMeasurements: true,
    selectedMedium: 'string'
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetPulse = () => {
    handleDataChange({ ...data, amplitude: 20, pulseWidth: 50, speed: 2 });
  };

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Pulse Simulator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Pulse Type</label>
          <select
            value={data.pulseType}
            onChange={(e) => handleDataChange({ ...data, pulseType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="transverse">Transverse</option>
            <option value="longitudinal">Longitudinal</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Medium</label>
          <select
            value={data.selectedMedium}
            onChange={(e) => handleDataChange({ ...data, selectedMedium: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="string">String</option>
            <option value="spring">Spring</option>
            <option value="water">Water</option>
            <option value="air">Air</option>
          </select>
        </div>
      </div>

      <div className="mb-4 grid grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Amplitude</label>
          <input
            type="range"
            min="5"
            max="50"
            value={data.amplitude}
            onChange={(e) => handleDataChange({ ...data, amplitude: parseInt(e.target.value) })}
            className="w-full"
          />
          <span className="text-sm text-gray-600">{data.amplitude} units</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Pulse Width</label>
          <input
            type="range"
            min="20"
            max="100"
            value={data.pulseWidth}
            onChange={(e) => handleDataChange({ ...data, pulseWidth: parseInt(e.target.value) })}
            className="w-full"
          />
          <span className="text-sm text-gray-600">{data.pulseWidth} units</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Speed</label>
          <input
            type="range"
            min="1"
            max="5"
            value={data.speed}
            onChange={(e) => handleDataChange({ ...data, speed: parseInt(e.target.value) })}
            className="w-full"
          />
          <span className="text-sm text-gray-600">{data.speed} units/s</span>
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Animation
        </button>
        <button
          onClick={resetPulse}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showGrid}
            onChange={(e) => handleDataChange({ ...data, showGrid: e.target.checked })}
            className="mr-2"
          />
          Show Grid
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showMeasurements}
            onChange={(e) => handleDataChange({ ...data, showMeasurements: e.target.checked })}
            className="mr-2"
          />
          Show Measurements
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[300px]">
        <div className="text-center text-gray-600 mb-4">
          {data.pulseType === 'transverse' ? 'Transverse' : 'Longitudinal'} Pulse on {data.selectedMedium}
        </div>
        
        <div className="text-center p-2 bg-blue-100 rounded">
          <strong>Pulse Properties:</strong> Amplitude: {data.amplitude}, Width: {data.pulseWidth}, Speed: {data.speed}
        </div>
        
        <div className="mt-4 text-sm text-gray-600">
          {data.pulseType === 'transverse' ? (
            <p>Transverse pulse: particles move perpendicular to wave direction</p>
          ) : (
            <p>Longitudinal pulse: particles move parallel to wave direction</p>
          )}
        </div>
      </div>
    </div>
  );
};

// Sound Wave Analyzer Component
const SoundWaveAnalyzer = ({
  initialData = {
    frequency: 440,
    amplitude: 50,
    waveform: 'sine',
    showHarmonics: true,
    showSpectrum: true,
    selectedNote: 'A4',
    isPlaying: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const togglePlayback = () => {
    handleDataChange({ ...data, isPlaying: !data.isPlaying });
  };

  const changeNote = (note) => {
    const noteFrequencies = {
      'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23,
      'G4': 392.00, 'A4': 440.00, 'B4': 493.88, 'C5': 523.25
    };
    handleDataChange({ ...data, selectedNote: note, frequency: noteFrequencies[note] });
  };

  const calculateWavelength = () => {
    const speedOfSound = 343; // m/s in air
    return (speedOfSound / data.frequency).toFixed(2);
  };

  const calculatePeriod = () => {
    return (1000 / data.frequency).toFixed(2); // in milliseconds
  };

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Sound Wave Analyzer</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Musical Note</label>
          <select
            value={data.selectedNote}
            onChange={(e) => changeNote(e.target.value)}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="C4">C4 (261.63 Hz)</option>
            <option value="D4">D4 (293.66 Hz)</option>
            <option value="E4">E4 (329.63 Hz)</option>
            <option value="F4">F4 (349.23 Hz)</option>
            <option value="G4">G4 (392.00 Hz)</option>
            <option value="A4">A4 (440.00 Hz)</option>
            <option value="B4">B4 (493.88 Hz)</option>
            <option value="C5">C5 (523.25 Hz)</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Waveform</label>
          <select
            value={data.waveform}
            onChange={(e) => handleDataChange({ ...data, waveform: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="sine">Sine Wave</option>
            <option value="square">Square Wave</option>
            <option value="sawtooth">Sawtooth Wave</option>
            <option value="triangle">Triangle Wave</option>
          </select>
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Frequency: {data.frequency} Hz</label>
          <input
            type="range"
            min="20"
            max="20000"
            value={data.frequency}
            onChange={(e) => handleDataChange({ ...data, frequency: parseInt(e.target.value) })}
            className="w-full"
          />
          <span className="text-sm text-gray-600">20 Hz - 20 kHz</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Amplitude: {data.amplitude}%</label>
          <input
            type="range"
            min="10"
            max="100"
            value={data.amplitude}
            onChange={(e) => handleDataChange({ ...data, amplitude: parseInt(e.target.value) })}
            className="w-full"
          />
          <span className="text-sm text-gray-600">10% - 100%</span>
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={togglePlayback}
          className={`px-4 py-2 rounded ${
            data.isPlaying 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isPlaying ? 'Stop' : 'Play'} Sound
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showHarmonics}
            onChange={(e) => handleDataChange({ ...data, showHarmonics: e.target.checked })}
            className="mr-2"
          />
          Show Harmonics
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showSpectrum}
            onChange={(e) => handleDataChange({ ...data, showSpectrum: e.target.checked })}
            className="mr-2"
          />
          Show Frequency Spectrum
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[300px]">
        <div className="text-center text-gray-600 mb-4">
          {data.waveform.charAt(0).toUpperCase() + data.waveform.slice(1)} Wave at {data.frequency} Hz
        </div>
        
        <div className="grid grid-cols-2 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <strong>Wavelength:</strong> {calculateWavelength()} m
          </div>
          <div className="text-center p-2 bg-green-100 rounded">
            <strong>Period:</strong> {calculatePeriod()} ms
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Wave Properties:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Frequency: {data.frequency} Hz (cycles per second)</li>
            <li>Amplitude: {data.amplitude}% (loudness)</li>
            <li>Waveform: {data.waveform} (shape of the wave)</li>
            <li>Speed in air: 343 m/s</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

// Motion Graph Builder Component
const MotionGraphBuilder = ({
  initialData = {
    motionType: 'uniform_acceleration',
    initialVelocity: 10,
    acceleration: -2,
    timeRange: [0, 10],
    showPosition: true,
    showVelocity: true,
    showAcceleration: true,
    units: { time: 's', position: 'm', velocity: 'm/s', acceleration: 'm/s²' }
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const calculatePosition = (t) => {
    if (data.motionType === 'uniform_acceleration') {
      return data.initialVelocity * t + 0.5 * data.acceleration * t * t;
    } else if (data.motionType === 'uniform_motion') {
      return data.initialVelocity * t;
    } else if (data.motionType === 'free_fall') {
      return 0.5 * 9.8 * t * t; // g = 9.8 m/s²
    }
    return 0;
  };

  const calculateVelocity = (t) => {
    if (data.motionType === 'uniform_acceleration') {
      return data.initialVelocity + data.acceleration * t;
    } else if (data.motionType === 'uniform_motion') {
      return data.initialVelocity;
    } else if (data.motionType === 'free_fall') {
      return 9.8 * t;
    }
    return 0;
  };

  const calculateTimeToStop = () => {
    if (data.motionType === 'uniform_acceleration' && data.acceleration !== 0) {
      return -data.initialVelocity / data.acceleration;
    }
    return null;
  };

  const generateDataPoints = () => {
    const points = [];
    const step = (data.timeRange[1] - data.timeRange[0]) / 20;
    
    for (let t = data.timeRange[0]; t <= data.timeRange[1]; t += step) {
      points.push({
        time: t,
        position: calculatePosition(t),
        velocity: calculateVelocity(t),
        acceleration: data.motionType === 'uniform_acceleration' ? data.acceleration : 0
      });
    }
    return points;
  };

  const timeToStop = calculateTimeToStop();
  const dataPoints = generateDataPoints();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Motion Graph Builder</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Motion Type</label>
          <select
            value={data.motionType}
            onChange={(e) => handleDataChange({ ...data, motionType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="uniform_motion">Uniform Motion (Constant Velocity)</option>
            <option value="uniform_acceleration">Uniform Acceleration</option>
            <option value="free_fall">Free Fall</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Initial Velocity</label>
          <input
            type="number"
            value={data.initialVelocity}
            onChange={(e) => handleDataChange({ ...data, initialVelocity: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
          />
          <span className="text-sm text-gray-600">{data.units.velocity}</span>
        </div>
      </div>

      {data.motionType === 'uniform_acceleration' && (
        <div className="mb-4">
          <label className="block text-sm font-medium mb-1">Acceleration</label>
          <input
            type="number"
            value={data.acceleration}
            onChange={(e) => handleDataChange({ ...data, acceleration: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
          />
          <span className="text-sm text-gray-600">{data.units.acceleration}</span>
        </div>
      )}

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Time Range Start</label>
          <input
            type="number"
            value={data.timeRange[0]}
            onChange={(e) => {
              const newRange = [parseFloat(e.target.value) || 0, data.timeRange[1]];
              handleDataChange({ ...data, timeRange: newRange });
            }}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
          />
          <span className="text-sm text-gray-600">{data.units.time}</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Time Range End</label>
          <input
            type="number"
            value={data.timeRange[1]}
            onChange={(e) => {
              const newRange = [data.timeRange[0], parseFloat(e.target.value) || 10];
              handleDataChange({ ...data, timeRange: newRange });
            }}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
          />
          <span className="text-sm text-gray-600">{data.units.time}</span>
        </div>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showPosition}
            onChange={(e) => handleDataChange({ ...data, showPosition: e.target.checked })}
            className="mr-2"
          />
          Show Position Graph
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showVelocity}
            onChange={(e) => handleDataChange({ ...data, showVelocity: e.target.checked })}
            className="mr-2"
          />
          Show Velocity Graph
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showAcceleration}
            onChange={(e) => handleDataChange({ ...data, showAcceleration: e.target.checked })}
            className="mr-2"
          />
          Show Acceleration Graph
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          {data.motionType === 'uniform_motion' && 'Uniform Motion Analysis'}
          {data.motionType === 'uniform_acceleration' && 'Uniformly Accelerated Motion Analysis'}
          {data.motionType === 'free_fall' && 'Free Fall Motion Analysis'}
        </div>
        
        {timeToStop && (
          <div className="text-center p-2 bg-yellow-100 rounded mb-4">
            <strong>Time to Stop:</strong> {timeToStop.toFixed(2)} {data.units.time}
          </div>
        )}
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Initial Velocity</div>
            <div className="text-lg font-bold text-blue-800">
              {data.initialVelocity} {data.units.velocity}
            </div>
          </div>
          
          {data.motionType === 'uniform_acceleration' && (
            <div className="text-center p-2 bg-green-100 rounded">
              <div className="text-sm text-green-600 font-medium">Acceleration</div>
              <div className="text-lg font-bold text-green-800">
                {data.acceleration} {data.units.acceleration}
              </div>
            </div>
          )}
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Time Range</div>
            <div className="text-lg font-bold text-purple-800">
              {data.timeRange[0]} - {data.timeRange[1]} {data.units.time}
            </div>
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Motion Equations:</strong></p>
          {data.motionType === 'uniform_motion' && (
            <ul className="list-disc list-inside ml-4 space-y-1">
              <li>Position: x(t) = x₀ + v₀t</li>
              <li>Velocity: v(t) = v₀ (constant)</li>
              <li>Acceleration: a = 0</li>
            </ul>
          )}
          {data.motionType === 'uniform_acceleration' && (
            <ul className="list-disc list-inside ml-4 space-y-1">
              <li>Position: x(t) = x₀ + v₀t + ½at²</li>
              <li>Velocity: v(t) = v₀ + at</li>
              <li>Acceleration: a = constant</li>
            </ul>
          )}
          {data.motionType === 'free_fall' && (
            <ul className="list-disc list-inside ml-4 space-y-1">
              <li>Position: y(t) = y₀ + v₀t + ½gt²</li>
              <li>Velocity: v(t) = v₀ + gt</li>
              <li>Acceleration: g = 9.8 m/s² (downward)</li>
            </ul>
          )}
        </div>
      </div>
    </div>
  );
};

// Free Fall Simulator Component
const FreeFallSimulator = ({
  initialData = {
    initialHeight: 100,
    initialVelocity: 0,
    gravity: 9.8,
    airResistance: 0,
    isAnimating: false,
    showTrajectory: true,
    showVelocityVectors: true,
    showTimeMarkers: true,
    selectedPlanet: 'earth'
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetSimulation = () => {
    handleDataChange({ ...data, initialHeight: 100, initialVelocity: 0, isAnimating: false });
  };

  const calculateTimeToGround = () => {
    if (data.initialVelocity === 0) {
      return Math.sqrt(2 * data.initialHeight / data.gravity);
    } else {
      // Quadratic equation: h = v₀t + ½gt²
      const a = 0.5 * data.gravity;
      const b = data.initialVelocity;
      const c = -data.initialHeight;
      const discriminant = b * b - 4 * a * c;
      if (discriminant >= 0) {
        const t1 = (-b + Math.sqrt(discriminant)) / (2 * a);
        const t2 = (-b - Math.sqrt(discriminant)) / (2 * a);
        return Math.max(t1, t2); // Return positive time
      }
    }
    return null;
  };

  const calculateFinalVelocity = () => {
    const timeToGround = calculateTimeToGround();
    if (timeToGround) {
      return data.initialVelocity + data.gravity * timeToGround;
    }
    return null;
  };

  const calculateMaxHeight = () => {
    if (data.initialVelocity > 0) {
      return data.initialHeight + (data.initialVelocity * data.initialVelocity) / (2 * data.gravity);
    }
    return data.initialHeight;
  };

  const timeToGround = calculateTimeToGround();
  const finalVelocity = calculateFinalVelocity();
  const maxHeight = calculateMaxHeight();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Free Fall Simulator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Planet/Celestial Body</label>
          <select
            value={data.selectedPlanet}
            onChange={(e) => {
              const planet = e.target.value;
              const gravities = {
                'earth': 9.8,
                'moon': 1.62,
                'mars': 3.71,
                'jupiter': 24.79,
                'sun': 274.0
              };
              handleDataChange({ ...data, selectedPlanet: planet, gravity: gravities[planet] });
            }}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="earth">Earth (9.8 m/s²)</option>
            <option value="moon">Moon (1.62 m/s²)</option>
            <option value="mars">Mars (3.71 m/s²)</option>
            <option value="jupiter">Jupiter (24.79 m/s²)</option>
            <option value="sun">Sun (274.0 m/s²)</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Initial Height</label>
          <input
            type="number"
            value={data.initialHeight}
            onChange={(e) => handleDataChange({ ...data, initialHeight: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
          <span className="text-sm text-gray-600">meters</span>
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Initial Velocity</label>
          <input
            type="number"
            value={data.initialVelocity}
            onChange={(e) => handleDataChange({ ...data, initialVelocity: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
          />
          <span className="text-sm text-gray-600">m/s (positive = upward)</span>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Gravity</label>
          <input
            type="number"
            value={data.gravity}
            onChange={(e) => handleDataChange({ ...data, gravity: parseFloat(e.target.value) || 9.8 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
          <span className="text-sm text-gray-600">m/s²</span>
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Simulation
        </button>
        <button
          onClick={resetSimulation}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showTrajectory}
            onChange={(e) => handleDataChange({ ...data, showTrajectory: e.target.checked })}
            className="mr-2"
          />
          Show Trajectory Path
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showVelocityVectors}
            onChange={(e) => handleDataChange({ ...data, showVelocityVectors: e.target.checked })}
            className="mr-2"
          />
          Show Velocity Vectors
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showTimeMarkers}
            onChange={(e) => handleDataChange({ ...data, showTimeMarkers: e.target.checked })}
            className="mr-2"
          />
          Show Time Markers
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Free Fall Simulation on {data.selectedPlanet.charAt(0).toUpperCase() + data.selectedPlanet.slice(1)}
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Initial Height</div>
            <div className="text-lg font-bold text-blue-800">
              {data.initialHeight} m
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Initial Velocity</div>
            <div className="text-lg font-bold text-green-800">
              {data.initialVelocity} m/s
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Gravity</div>
            <div className="text-lg font-bold text-purple-800">
              {data.gravity} m/s²
            </div>
          </div>
        </div>
        
        {timeToGround && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
            <div className="text-center p-2 bg-yellow-100 rounded">
              <div className="text-sm text-yellow-600 font-medium">Time to Ground</div>
              <div className="text-lg font-bold text-yellow-800">
                {timeToGround.toFixed(2)} s
              </div>
            </div>
            
            <div className="text-center p-2 bg-red-100 rounded">
              <div className="text-sm text-red-600 font-medium">Final Velocity</div>
              <div className="text-lg font-bold text-red-800">
                {finalVelocity?.toFixed(2)} m/s
              </div>
            </div>
            
            <div className="text-center p-2 bg-indigo-100 rounded">
              <div className="text-sm text-indigo-600 font-medium">Max Height</div>
              <div className="text-lg font-bold text-indigo-800">
                {maxHeight.toFixed(2)} m
              </div>
            </div>
          </div>
        )}
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Free Fall Equations:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Position: y(t) = y₀ + v₀t + ½gt²</li>
            <li>Velocity: v(t) = v₀ + gt</li>
            <li>Time to ground: t = √(2h/g) for v₀ = 0</li>
            <li>Final velocity: v = √(2gh) for v₀ = 0</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

// Superposition Visualizer Component
const SuperpositionVisualizer = ({
  initialData = {
    waveType: 'sine',
    wave1: { amplitude: 50, frequency: 2, phase: 0, color: '#3B82F6' },
    wave2: { amplitude: 30, frequency: 3, phase: 0, color: '#EF4444' },
    showIndividualWaves: true,
    showSuperposition: true,
    showInterference: true,
    isAnimating: true,
    timeRange: [0, 10]
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetWaves = () => {
    handleDataChange({
      ...data,
      wave1: { amplitude: 50, frequency: 2, phase: 0, color: '#3B82F6' },
      wave2: { amplitude: 30, frequency: 3, phase: 0, color: '#EF4444' },
      isAnimating: true
    });
  };

  const calculateWave = (wave, x) => {
    if (data.waveType === 'sine') {
      return wave.amplitude * Math.sin(2 * Math.PI * wave.frequency * x + wave.phase);
    } else if (data.waveType === 'cosine') {
      return wave.amplitude * Math.cos(2 * Math.PI * wave.frequency * x + wave.phase);
    } else if (data.waveType === 'square') {
      return wave.amplitude * Math.sign(Math.sin(2 * Math.PI * wave.frequency * x + wave.phase));
    }
    return 0;
  };

  const calculateSuperposition = (x) => {
    const y1 = calculateWave(data.wave1, x);
    const y2 = calculateWave(data.wave2, x);
    return y1 + y2;
  };

  const calculateInterferencePattern = () => {
    const points = [];
    const step = (data.timeRange[1] - data.timeRange[0]) / 100;
    
    for (let x = data.timeRange[0]; x <= data.timeRange[1]; x += step) {
      points.push({
        x: x,
        y1: calculateWave(data.wave1, x),
        y2: calculateWave(data.wave2, x),
        superposition: calculateSuperposition(x)
      });
    }
    
    return points;
  };

  const interferencePoints = calculateInterferencePattern();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Superposition Visualizer</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Wave Type</label>
          <select
            value={data.waveType}
            onChange={(e) => handleDataChange({ ...data, waveType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="sine">Sine Wave</option>
            <option value="cosine">Cosine Wave</option>
            <option value="square">Square Wave</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Time Range</label>
          <input
            type="number"
            value={data.timeRange[1]}
            onChange={(e) => {
              const newRange = [0, parseFloat(e.target.value) || 10];
              handleDataChange({ ...data, timeRange: newRange });
            }}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="1"
          />
          <span className="text-sm text-gray-600">seconds</span>
        </div>
      </div>

      <div className="mb-4 grid grid-cols-1 md:grid-cols-2 gap-4">
        {/* Wave 1 Controls */}
        <div className="border rounded p-3">
          <h4 className="font-medium mb-2">Wave 1</h4>
          <div className="space-y-2">
            <div>
              <label className="block text-sm text-gray-600">Amplitude</label>
              <input
                type="range"
                min="10"
                max="100"
                value={data.wave1.amplitude}
                onChange={(e) => {
                  const newWave1 = { ...data.wave1, amplitude: parseInt(e.target.value) };
                  handleDataChange({ ...data, wave1: newWave1 });
                }}
                className="w-full"
              />
              <span className="text-sm text-gray-600">{data.wave1.amplitude}</span>
            </div>
            <div>
              <label className="block text-sm text-gray-600">Frequency</label>
              <input
                type="range"
                min="0.5"
                max="5"
                step="0.1"
                value={data.wave1.frequency}
                onChange={(e) => {
                  const newWave1 = { ...data.wave1, frequency: parseFloat(e.target.value) };
                  handleDataChange({ ...data, wave1: newWave1 });
                }}
                className="w-full"
              />
              <span className="text-sm text-gray-600">{data.wave1.frequency} Hz</span>
            </div>
            <div>
              <label className="block text-sm text-gray-600">Phase</label>
              <input
                type="range"
                min="0"
                max="6.28"
                step="0.1"
                value={data.wave1.phase}
                onChange={(e) => {
                  const newWave1 = { ...data.wave1, phase: parseFloat(e.target.value) };
                  handleDataChange({ ...data, wave1: newWave1 });
                }}
                className="w-full"
              />
              <span className="text-sm text-gray-600">{(data.wave1.phase * 180 / Math.PI).toFixed(1)}°</span>
            </div>
          </div>
        </div>

        {/* Wave 2 Controls */}
        <div className="border rounded p-3">
          <h4 className="font-medium mb-2">Wave 2</h4>
          <div className="space-y-2">
            <div>
              <label className="block text-sm text-gray-600">Amplitude</label>
              <input
                type="range"
                min="10"
                max="100"
                value={data.wave2.amplitude}
                onChange={(e) => {
                  const newWave2 = { ...data.wave2, amplitude: parseInt(e.target.value) };
                  handleDataChange({ ...data, wave2: newWave2 });
                }}
                className="w-full"
              />
              <span className="text-sm text-gray-600">{data.wave2.amplitude}</span>
            </div>
            <div>
              <label className="block text-sm text-gray-600">Frequency</label>
              <input
                type="range"
                min="0.5"
                max="5"
                step="0.1"
                value={data.wave2.frequency}
                onChange={(e) => {
                  const newWave2 = { ...data.wave2, frequency: parseFloat(e.target.value) };
                  handleDataChange({ ...data, wave2: newWave2 });
                }}
                className="w-full"
              />
              <span className="text-sm text-gray-600">{data.wave2.frequency} Hz</span>
            </div>
            <div>
              <label className="block text-sm text-gray-600">Phase</label>
              <input
                type="range"
                min="0"
                max="6.28"
                step="0.1"
                value={data.wave2.phase}
                onChange={(e) => {
                  const newWave2 = { ...data.wave2, phase: parseFloat(e.target.value) };
                  handleDataChange({ ...data, wave2: newWave2 });
                }}
                className="w-full"
              />
              <span className="text-sm text-gray-600">{(data.wave2.phase * 180 / Math.PI).toFixed(1)}°</span>
            </div>
          </div>
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Animation
        </button>
        <button
          onClick={resetWaves}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showIndividualWaves}
            onChange={(e) => handleDataChange({ ...data, showIndividualWaves: e.target.checked })}
            className="mr-2"
          />
          Show Individual Waves
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showSuperposition}
            onChange={(e) => handleDataChange({ ...data, showSuperposition: e.target.checked })}
            className="mr-2"
          />
          Show Superposition
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showInterference}
            onChange={(e) => handleDataChange({ ...data, showInterference: e.target.checked })}
            className="mr-2"
          />
          Show Interference Pattern
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Wave Superposition and Interference Analysis
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Wave 1</div>
            <div className="text-lg font-bold text-blue-800">
              A={data.wave1.amplitude}, f={data.wave1.frequency}Hz
            </div>
          </div>
          
          <div className="text-center p-2 bg-red-100 rounded">
            <div className="text-sm text-red-600 font-medium">Wave 2</div>
            <div className="text-lg font-bold text-red-800">
              A={data.wave2.amplitude}, f={data.wave2.frequency}Hz
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Superposition</div>
            <div className="text-lg font-bold text-purple-800">
              Max: {Math.max(...interferencePoints.map(p => p.superposition)).toFixed(1)}
            </div>
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Superposition Principle:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>When two waves meet, their displacements add algebraically</li>
            <li>Constructive interference: waves add to create larger amplitude</li>
            <li>Destructive interference: waves cancel each other out</li>
            <li>Beat frequency: |f₁ - f₂| when frequencies are close</li>
          </ul>
        </div>
        
        <div className="mt-4 p-4 bg-gray-900 rounded">
          <div className="text-center text-white mb-2">Wave Visualization</div>
          <div className="h-48 bg-blue-900 rounded relative overflow-hidden">
            {/* Wave visualization would go here */}
            <div className="absolute inset-0 flex items-center justify-center text-blue-300">
              Interactive wave superposition visualization
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Electric Field Visualizer Component
const ElectricFieldVisualizer = ({
  initialData = {
    chargeType: 'point',
    charges: [
      { x: 100, y: 150, magnitude: 1, type: 'positive', color: '#ef4444' },
      { x: 300, y: 150, magnitude: 1, type: 'negative', color: '#3b82f6' }
    ],
    showFieldLines: true,
    showEquipotential: false,
    showVectors: true,
    fieldStrength: 1.0,
    gridSize: 20,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetField = () => {
    handleDataChange({
      ...data,
      charges: [
        { x: 100, y: 150, magnitude: 1, type: 'positive', color: '#ef4444' },
        { x: 300, y: 150, magnitude: 1, type: 'negative', color: '#3b82f6' }
      ],
      isAnimating: false
    });
  };

  const addCharge = () => {
    const newCharge = {
      x: 200,
      y: 100,
      magnitude: 1,
      type: 'positive',
      color: '#ef4444'
    };
    const newData = { ...data, charges: [...data.charges, newCharge] };
    handleDataChange(newData);
  };

  const removeCharge = (index) => {
    const newCharges = data.charges.filter((_, i) => i !== index);
    const newData = { ...data, charges: newCharges };
    handleDataChange(newData);
  };

  const updateCharge = (index, field, value) => {
    const newCharges = [...data.charges];
    newCharges[index][field] = field === 'x' || field === 'y' || field === 'magnitude' ? 
                               parseFloat(value) || 0 : value;
    const newData = { ...data, charges: newCharges };
    handleDataChange(newData);
  };

  const calculateFieldAtPoint = (x, y) => {
    let totalEx = 0;
    let totalEy = 0;
    const k = 8.99e9; // Coulomb's constant

    data.charges.forEach(charge => {
      const dx = x - charge.x;
      const dy = y - charge.y;
      const r = Math.sqrt(dx * dx + dy * dy);
      
      if (r > 0) {
        const force = k * charge.magnitude / (r * r);
        const sign = charge.type === 'positive' ? 1 : -1;
        
        totalEx += sign * force * dx / r;
        totalEy += sign * force * dy / r;
      }
    });

    return { Ex: totalEx, Ey: totalEy };
  };

  const calculatePotentialAtPoint = (x, y) => {
    let totalPotential = 0;
    const k = 8.99e9;

    data.charges.forEach(charge => {
      const dx = x - charge.x;
      const dy = y - charge.y;
      const r = Math.sqrt(dx * dx + dy * dy);
      
      if (r > 0) {
        const sign = charge.type === 'positive' ? 1 : -1;
        totalPotential += sign * k * charge.magnitude / r;
      }
    });

    return totalPotential;
  };

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Electric Field Visualizer</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Charge Type</label>
          <select
            value={data.chargeType}
            onChange={(e) => handleDataChange({ ...data, chargeType: e.target.value })}
            className="w-full px-3 py-2 border rounded"
          >
            <option value="point">Point Charges</option>
            <option value="line">Line Charge</option>
            <option value="plane">Plane Charge</option>
          </select>
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Field Strength</label>
          <input
            type="range"
            min="0.1"
            max="2.0"
            step="0.1"
            value={data.fieldStrength}
            onChange={(e) => handleDataChange({ ...data, fieldStrength: parseFloat(e.target.value) })}
            className="w-full"
          />
          <span className="text-sm text-gray-600">{data.fieldStrength}</span>
        </div>
      </div>

      <div className="mb-4">
        <div className="flex justify-between items-center mb-2">
          <h4 className="font-medium">Charges</h4>
          <button
            onClick={addCharge}
            className="px-3 py-1 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            Add Charge
          </button>
        </div>
        
        <div className="space-y-2">
          {data.charges.map((charge, index) => (
            <div key={index} className="flex items-center space-x-2 p-2 border rounded">
              <select
                value={charge.type}
                onChange={(e) => updateCharge(index, 'type', e.target.value)}
                className="w-20 px-2 py-1 border rounded"
              >
                <option value="positive">+</option>
                <option value="negative">-</option>
              </select>
              <input
                type="number"
                value={charge.magnitude}
                onChange={(e) => updateCharge(index, 'magnitude', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Q"
                step="0.1"
                min="0"
              />
              <span className="text-sm text-gray-600">× 10⁻⁶ C</span>
              <input
                type="number"
                value={charge.x}
                onChange={(e) => updateCharge(index, 'x', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="X"
                min="0"
                max="400"
              />
              <input
                type="number"
                value={charge.y}
                onChange={(e) => updateCharge(index, 'y', e.target.value)}
                className="w-16 px-2 py-1 border rounded"
                placeholder="Y"
                min="0"
                max="300"
              />
              <button
                onClick={() => removeCharge(index)}
                className="px-2 py-1 bg-red-500 text-white rounded hover:bg-red-600"
              >
                ×
              </button>
            </div>
          ))}
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Animation
        </button>
        <button
          onClick={resetField}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showFieldLines}
            onChange={(e) => handleDataChange({ ...data, showFieldLines: e.target.checked })}
            className="mr-2"
          />
          Show Field Lines
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showEquipotential}
            onChange={(e) => handleDataChange({ ...data, showEquipotential: e.target.checked })}
            className="mr-2"
          />
          Show Equipotential Lines
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showVectors}
            onChange={(e) => handleDataChange({ ...data, showVectors: e.target.checked })}
            className="mr-2"
          />
          Show Field Vectors
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Electric Field Visualization
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Number of Charges</div>
            <div className="text-lg font-bold text-blue-800">
              {data.charges.length}
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Net Charge</div>
            <div className="text-lg font-bold text-green-800">
              {data.charges.reduce((sum, charge) => 
                sum + (charge.type === 'positive' ? charge.magnitude : -charge.magnitude), 0
              ).toFixed(2)} × 10⁻⁶ C
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Field Strength</div>
            <div className="text-lg font-bold text-purple-800">
              {data.fieldStrength}
            </div>
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Electric Field Properties:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Field lines point away from positive charges, toward negative charges</li>
            <li>Field strength decreases with distance (1/r² for point charges)</li>
            <li>Equipotential lines are perpendicular to field lines</li>
            <li>Field vectors show direction and relative strength</li>
          </ul>
        </div>
        
        <div className="mt-4 p-4 bg-gray-900 rounded">
          <div className="text-center text-white mb-2">Electric Field Visualization</div>
          <div className="h-48 bg-blue-900 rounded relative overflow-hidden">
            {/* Field visualization would go here */}
            <div className="absolute inset-0 flex items-center justify-center text-blue-300">
              Interactive electric field visualization
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Capacitor Charging Simulator Component
const CapacitorChargingSimulator = ({
  initialData = {
    voltage: 12.0,
    resistance: 1000,
    capacitance: 100,
    timeRange: [0, 5],
    showCharging: true,
    showDischarging: false,
    showCurrent: true,
    showPower: false,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetSimulation = () => {
    handleDataChange({
      ...data,
      voltage: 12.0,
      resistance: 1000,
      capacitance: 100,
      isAnimating: false
    });
  };

  const calculateTimeConstant = () => {
    return data.resistance * data.capacitance / 1000; // Convert to seconds
  };

  const calculateChargingVoltage = (time) => {
    const tau = calculateTimeConstant();
    return data.voltage * (1 - Math.exp(-time / tau));
  };

  const calculateDischargingVoltage = (time) => {
    const tau = calculateTimeConstant();
    return data.voltage * Math.exp(-time / tau);
  };

  const calculateCurrent = (time, isCharging = true) => {
    const tau = calculateTimeConstant();
    const maxCurrent = data.voltage / data.resistance;
    return isCharging ? 
      maxCurrent * Math.exp(-time / tau) : 
      -maxCurrent * Math.exp(-time / tau);
  };

  const calculatePower = (time, isCharging = true) => {
    const current = calculateCurrent(time, isCharging);
    const voltage = isCharging ? calculateChargingVoltage(time) : calculateDischargingVoltage(time);
    return current * voltage;
  };

  const timeConstant = calculateTimeConstant();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Capacitor Charging Simulator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Voltage (V)</label>
          <input
            type="number"
            value={data.voltage}
            onChange={(e) => handleDataChange({ ...data, voltage: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Resistance (Ω)</label>
          <input
            type="number"
            value={data.resistance}
            onChange={(e) => handleDataChange({ ...data, resistance: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="10"
            min="0"
          />
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Capacitance (μF)</label>
          <input
            type="number"
            value={data.capacitance}
            onChange={(e) => handleDataChange({ ...data, capacitance: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Time Range (s)</label>
          <input
            type="number"
            value={data.timeRange[1]}
            onChange={(e) => {
              const newRange = [0, parseFloat(e.target.value) || 5];
              handleDataChange({ ...data, timeRange: newRange });
            }}
            className="w-full px-3 py-2 border rounded"
            step="0.5"
            min="0.5"
          />
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Simulation
        </button>
        <button
          onClick={resetSimulation}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showCharging}
            onChange={(e) => handleDataChange({ ...data, showCharging: e.target.checked })}
            className="mr-2"
          />
          Show Charging Curve
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showDischarging}
            onChange={(e) => handleDataChange({ ...data, showDischarging: e.target.checked })}
            className="mr-2"
          />
          Show Discharging Curve
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showCurrent}
            onChange={(e) => handleDataChange({ ...data, showCurrent: e.target.checked })}
            className="mr-2"
          />
          Show Current
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showPower}
            onChange={(e) => handleDataChange({ ...data, showPower: e.target.checked })}
            className="mr-2"
          />
          Show Power
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          RC Circuit Analysis
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Time Constant</div>
            <div className="text-lg font-bold text-blue-800">
              {timeConstant.toFixed(3)} s
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Max Current</div>
            <div className="text-lg font-bold text-green-800">
              {(data.voltage / data.resistance * 1000).toFixed(2)} mA
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Max Energy</div>
            <div className="text-lg font-bold text-purple-800">
              {(0.5 * data.capacitance * data.voltage * data.voltage / 1000000).toFixed(3)} mJ
            </div>
          </div>
          
          <div className="text-center p-2 bg-yellow-100 rounded">
            <div className="text-sm text-yellow-600 font-medium">Max Power</div>
            <div className="text-lg font-bold text-yellow-800">
              {(data.voltage * data.voltage / data.resistance).toFixed(2)} mW
            </div>
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>RC Circuit Equations:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Time constant: τ = RC</li>
            <li>Charging: V(t) = V₀(1 - e^(-t/τ))</li>
            <li>Discharging: V(t) = V₀e^(-t/τ)</li>
            <li>Current: I(t) = (V₀/R)e^(-t/τ)</li>
            <li>Energy: E = ½CV²</li>
          </ul>
        </div>
        
        <div className="mt-4 p-4 bg-gray-900 rounded">
          <div className="text-center text-white mb-2">RC Circuit Visualization</div>
          <div className="h-48 bg-blue-900 rounded relative overflow-hidden">
            {/* Circuit visualization would go here */}
            <div className="absolute inset-0 flex items-center justify-center text-blue-300">
              Interactive RC circuit simulation
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Electromagnetic Induction Simulator Component
const ElectromagneticInductionSimulator = ({
  initialData = {
    magneticFieldStrength: 0.5,
    coilArea: 0.01,
    numberOfTurns: 100,
    rotationSpeed: 60,
    rotationAxis: 'horizontal',
    showMagneticField: true,
    showInducedEMF: true,
    showFlux: true,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetSimulation = () => {
    handleDataChange({
      ...data,
      magneticFieldStrength: 0.5,
      coilArea: 0.01,
      numberOfTurns: 100,
      rotationSpeed: 60,
      isAnimating: false
    });
  };

  const calculateMagneticFlux = (angle) => {
    // Φ = B × A × cos(θ)
    return data.magneticFieldStrength * data.coilArea * Math.cos(angle * Math.PI / 180);
  };

  const calculateInducedEMF = (angle, angularVelocity) => {
    // ε = -N × dΦ/dt = -N × B × A × ω × sin(θ)
    const omega = angularVelocity * Math.PI / 30; // Convert RPM to rad/s
    return -data.numberOfTurns * data.magneticFieldStrength * data.coilArea * omega * Math.sin(angle * Math.PI / 180);
  };

  const calculateMaxEMF = () => {
    const omega = data.rotationSpeed * Math.PI / 30;
    return data.numberOfTurns * data.magneticFieldStrength * data.coilArea * omega;
  };

  const calculateRMSEMF = () => {
    return calculateMaxEMF() / Math.sqrt(2);
  };

  const maxEMF = calculateMaxEMF();
  const rmsEMF = calculateRMSEMF();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">Electromagnetic Induction Simulator</h3>
      
      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Magnetic Field (T)</label>
          <input
            type="number"
            value={data.magneticFieldStrength}
            onChange={(e) => handleDataChange({ ...data, magneticFieldStrength: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.1"
            min="0"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Coil Area (m²)</label>
          <input
            type="number"
            value={data.coilArea}
            onChange={(e) => handleDataChange({ ...data, coilArea: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.001"
            min="0"
          />
        </div>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Number of Turns</label>
          <input
            type="number"
            value={data.numberOfTurns}
            onChange={(e) => handleDataChange({ ...data, numberOfTurns: parseInt(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="10"
            min="1"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Rotation Speed (RPM)</label>
          <input
            type="number"
            value={data.rotationSpeed}
            onChange={(e) => handleDataChange({ ...data, rotationSpeed: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="10"
            min="0"
          />
        </div>
      </div>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Rotation Axis</label>
        <select
          value={data.rotationAxis}
          onChange={(e) => handleDataChange({ ...data, rotationAxis: e.target.value })}
          className="w-full px-3 py-2 border rounded"
        >
          <option value="horizontal">Horizontal</option>
          <option value="vertical">Vertical</option>
          <option value="diagonal">Diagonal</option>
        </select>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Simulation
        </button>
        <button
          onClick={resetSimulation}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showMagneticField}
            onChange={(e) => handleDataChange({ ...data, showMagneticField: e.target.checked })}
            className="mr-2"
          />
          Show Magnetic Field Lines
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showInducedEMF}
            onChange={(e) => handleDataChange({ ...data, showInducedEMF: e.target.checked })}
            className="mr-2"
          />
          Show Induced EMF
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showFlux}
            onChange={(e) => handleDataChange({ ...data, showFlux: e.target.checked })}
            className="mr-2"
          />
          Show Magnetic Flux
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          Faraday's Law of Electromagnetic Induction
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Max EMF</div>
            <div className="text-lg font-bold text-blue-800">
              {maxEMF.toFixed(3)} V
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">RMS EMF</div>
            <div className="text-lg font-bold text-green-800">
              {rmsEMF.toFixed(3)} V
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Frequency</div>
            <div className="text-lg font-bold text-purple-800">
              {(data.rotationSpeed / 60).toFixed(1)} Hz
            </div>
          </div>
          
          <div className="text-center p-2 bg-yellow-100 rounded">
            <div className="text-sm text-yellow-600 font-medium">Max Flux</div>
            <div className="text-lg font-bold text-yellow-800">
              {(data.magneticFieldStrength * data.coilArea).toFixed(5)} Wb
            </div>
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>Faraday's Law Equations:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Magnetic Flux: Φ = B × A × cos(θ)</li>
            <li>Induced EMF: ε = -N × dΦ/dt</li>
            <li>For rotating coil: ε = -N × B × A × ω × sin(ωt)</li>
            <li>Max EMF: ε_max = N × B × A × ω</li>
            <li>RMS EMF: ε_rms = ε_max / √2</li>
          </ul>
        </div>
        
        <div className="mt-4 p-4 bg-gray-900 rounded">
          <div className="text-center text-white mb-2">Electromagnetic Induction Visualization</div>
          <div className="h-48 bg-blue-900 rounded relative overflow-hidden">
            {/* Induction visualization would go here */}
            <div className="absolute inset-0 flex items-center justify-center text-blue-300">
              Interactive electromagnetic induction simulation
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// AC Circuit Analyzer Component
const ACCircuitAnalyzer = ({
  initialData = {
    circuitType: 'rlc_series',
    voltage: 120,
    frequency: 60,
    resistance: 100,
    inductance: 0.1,
    capacitance: 100,
    showPhasor: true,
    showImpedance: true,
    showPower: true,
    isAnimating: false
  },
  onChange = () => {},
  isSubmitted = false
}) => {
  const [data, setData] = useState(initialData);

  const handleDataChange = (newData) => {
    setData(newData);
    onChange(newData);
  };

  const toggleAnimation = () => {
    handleDataChange({ ...data, isAnimating: !data.isAnimating });
  };

  const resetCircuit = () => {
    handleDataChange({
      ...data,
      voltage: 120,
      frequency: 60,
      resistance: 100,
      inductance: 0.1,
      capacitance: 100,
      isAnimating: false
    });
  };

  const calculateAngularFrequency = () => {
    return 2 * Math.PI * data.frequency;
  };

  const calculateInductiveReactance = () => {
    const omega = calculateAngularFrequency();
    return omega * data.inductance;
  };

  const calculateCapacitiveReactance = () => {
    const omega = calculateAngularFrequency();
    return 1 / (omega * data.capacitance / 1000000); // Convert μF to F
  };

  const calculateImpedance = () => {
    const XL = calculateInductiveReactance();
    const XC = calculateCapacitiveReactance();
    
    if (data.circuitType === 'rlc_series') {
      return Math.sqrt(data.resistance * data.resistance + Math.pow(XL - XC, 2));
    } else if (data.circuitType === 'rlc_parallel') {
      const ZR = data.resistance;
      const ZL = XL;
      const ZC = XC;
      return 1 / Math.sqrt(1/(ZR*ZR) + 1/(ZL*ZL) + 1/(ZC*ZC));
    } else if (data.circuitType === 'rl_series') {
      return Math.sqrt(data.resistance * data.resistance + XL * XL);
    } else if (data.circuitType === 'rc_series') {
      return Math.sqrt(data.resistance * data.resistance + XC * XC);
    }
    return data.resistance;
  };

  const calculateCurrent = () => {
    return data.voltage / calculateImpedance();
  };

  const calculatePhaseAngle = () => {
    const XL = calculateInductiveReactance();
    const XC = calculateCapacitiveReactance();
    
    if (data.circuitType === 'rlc_series') {
      return Math.atan2(XL - XC, data.resistance) * 180 / Math.PI;
    } else if (data.circuitType === 'rl_series') {
      return Math.atan2(XL, data.resistance) * 180 / Math.PI;
    } else if (data.circuitType === 'rc_series') {
      return Math.atan2(-XC, data.resistance) * 180 / Math.PI;
    }
    return 0;
  };

  const calculatePowerFactor = () => {
    return Math.cos(calculatePhaseAngle() * Math.PI / 180);
  };

  const calculateApparentPower = () => {
    return data.voltage * calculateCurrent();
  };

  const calculateRealPower = () => {
    return calculateApparentPower() * calculatePowerFactor();
  };

  const calculateReactivePower = () => {
    return calculateApparentPower() * Math.sin(calculatePhaseAngle() * Math.PI / 180);
  };

  const impedance = calculateImpedance();
  const current = calculateCurrent();
  const phaseAngle = calculatePhaseAngle();
  const powerFactor = calculatePowerFactor();
  const apparentPower = calculateApparentPower();
  const realPower = calculateRealPower();
  const reactivePower = calculateReactivePower();

  return (
    <div className="p-4 border rounded-lg bg-white">
      <h3 className="text-lg font-semibold mb-4">AC Circuit Analyzer</h3>
      
      <div className="mb-4">
        <label className="block text-sm font-medium mb-1">Circuit Type</label>
        <select
          value={data.circuitType}
          onChange={(e) => handleDataChange({ ...data, circuitType: e.target.value })}
          className="w-full px-3 py-2 border rounded"
        >
          <option value="rlc_series">RLC Series</option>
          <option value="rlc_parallel">RLC Parallel</option>
          <option value="rl_series">RL Series</option>
          <option value="rc_series">RC Series</option>
          <option value="resistor_only">Resistor Only</option>
        </select>
      </div>

      <div className="mb-4 grid grid-cols-2 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Voltage (V)</label>
          <input
            type="number"
            value={data.voltage}
            onChange={(e) => handleDataChange({ ...data, voltage: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Frequency (Hz)</label>
          <input
            type="number"
            value={data.frequency}
            onChange={(e) => handleDataChange({ ...data, frequency: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
        </div>
      </div>

      <div className="mb-4 grid grid-cols-3 gap-4">
        <div>
          <label className="block text-sm font-medium mb-1">Resistance (Ω)</label>
          <input
            type="number"
            value={data.resistance}
            onChange={(e) => handleDataChange({ ...data, resistance: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Inductance (H)</label>
          <input
            type="number"
            value={data.inductance}
            onChange={(e) => handleDataChange({ ...data, inductance: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="0.01"
            min="0"
          />
        </div>
        
        <div>
          <label className="block text-sm font-medium mb-1">Capacitance (μF)</label>
          <input
            type="number"
            value={data.capacitance}
            onChange={(e) => handleDataChange({ ...data, capacitance: parseFloat(e.target.value) || 0 })}
            className="w-full px-3 py-2 border rounded"
            step="1"
            min="0"
          />
        </div>
      </div>

      <div className="mb-4 flex space-x-2">
        <button
          onClick={toggleAnimation}
          className={`px-4 py-2 rounded ${
            data.isAnimating 
              ? 'bg-red-500 hover:bg-red-600 text-white' 
              : 'bg-green-500 hover:bg-green-600 text-white'
          }`}
        >
          {data.isAnimating ? 'Stop' : 'Start'} Analysis
        </button>
        <button
          onClick={resetCircuit}
          className="px-4 py-2 bg-gray-500 text-white rounded hover:bg-gray-600"
        >
          Reset
        </button>
      </div>

      <div className="mb-4 space-y-2">
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showPhasor}
            onChange={(e) => handleDataChange({ ...data, showPhasor: e.target.checked })}
            className="mr-2"
          />
          Show Phasor Diagram
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showImpedance}
            onChange={(e) => handleDataChange({ ...data, showImpedance: e.target.checked })}
            className="mr-2"
          />
          Show Impedance Triangle
        </label>
        <label className="flex items-center">
          <input
            type="checkbox"
            checked={data.showPower}
            onChange={(e) => handleDataChange({ ...data, showPower: e.target.checked })}
            className="mr-2"
          />
          Show Power Triangle
        </label>
      </div>

      <div className="border rounded p-4 bg-gray-50 min-h-[400px]">
        <div className="text-center text-gray-600 mb-4">
          AC Circuit Analysis Results
        </div>
        
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-4">
          <div className="text-center p-2 bg-blue-100 rounded">
            <div className="text-sm text-blue-600 font-medium">Impedance</div>
            <div className="text-lg font-bold text-blue-800">
              {impedance.toFixed(1)} Ω
            </div>
          </div>
          
          <div className="text-center p-2 bg-green-100 rounded">
            <div className="text-sm text-green-600 font-medium">Current</div>
            <div className="text-lg font-bold text-green-800">
              {current.toFixed(3)} A
            </div>
          </div>
          
          <div className="text-center p-2 bg-purple-100 rounded">
            <div className="text-sm text-purple-600 font-medium">Phase Angle</div>
            <div className="text-lg font-bold text-purple-800">
              {phaseAngle.toFixed(1)}°
            </div>
          </div>
          
          <div className="text-center p-2 bg-yellow-100 rounded">
            <div className="text-sm text-yellow-600 font-medium">Power Factor</div>
            <div className="text-lg font-bold text-yellow-800">
              {powerFactor.toFixed(3)}
            </div>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
          <div className="text-center p-2 bg-red-100 rounded">
            <div className="text-sm text-red-600 font-medium">Apparent Power</div>
            <div className="text-lg font-bold text-red-800">
              {apparentPower.toFixed(1)} VA
            </div>
          </div>
          
          <div className="text-center p-2 bg-orange-100 rounded">
            <div className="text-sm text-orange-600 font-medium">Real Power</div>
            <div className="text-lg font-bold text-orange-800">
              {realPower.toFixed(1)} W
            </div>
          </div>
          
          <div className="text-center p-2 bg-indigo-100 rounded">
            <div className="text-sm text-indigo-600 font-medium">Reactive Power</div>
            <div className="text-lg font-bold text-indigo-800">
              {reactivePower.toFixed(1)} VAR
            </div>
          </div>
        </div>
        
        <div className="text-sm text-gray-600 space-y-2">
          <p><strong>AC Circuit Equations:</strong></p>
          <ul className="list-disc list-inside ml-4 space-y-1">
            <li>Angular frequency: ω = 2πf</li>
            <li>Inductive reactance: X_L = ωL</li>
            <li>Capacitive reactance: X_C = 1/(ωC)</li>
            <li>Impedance: Z = √(R² + (X_L - X_C)²)</li>
            <li>Phase angle: φ = tan⁻¹((X_L - X_C)/R)</li>
            <li>Power factor: cos(φ)</li>
          </ul>
        </div>
        
        <div className="mt-4 p-4 bg-gray-900 rounded">
          <div className="text-center text-white mb-2">AC Circuit Visualization</div>
          <div className="h-48 bg-blue-900 rounded relative overflow-hidden">
            {/* Circuit visualization would go here */}
            <div className="absolute inset-0 flex items-center justify-center text-blue-300">
              Interactive AC circuit analysis
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default { MotionGraphs, ForceDiagram, PulseSimulator, SoundWaveAnalyzer, MotionGraphBuilder, FreeFallSimulator, SuperpositionVisualizer, ElectricFieldVisualizer, CapacitorChargingSimulator, ElectromagneticInductionSimulator, ACCircuitAnalyzer };
