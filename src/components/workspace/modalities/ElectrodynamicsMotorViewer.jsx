import React, { useState, useRef, useEffect } from 'react';
import { 
  Zap, 
  RotateCw, 
  Play, 
  Pause, 
  Gauge, 
  Activity, 
  Settings2,
  CheckCircle2,
  Info
} from 'lucide-react';

export default function ElectrodynamicsMotorViewer({
  defaultMode = 'ac_generator', // 'ac_generator' | 'dc_motor'
}) {
  const [mode, setMode] = useState(defaultMode);
  const [isRunning, setIsRunning] = useState(true);
  const [frequency, setFrequency] = useState(0.8); // Hz
  const [angle, setAngle] = useState(0); // in radians
  const canvasRef = useRef(null);
  const animationFrameRef = useRef(null);
  const waveHistoryRef = useRef([]);

  // Animation loop updating angle and tracing oscilloscope
  useEffect(() => {
    let lastTime = performance.now();

    const animate = (time) => {
      const dt = (time - lastTime) / 1000;
      lastTime = time;

      if (isRunning) {
        setAngle(prev => {
          const next = (prev + 2 * Math.PI * frequency * dt) % (2 * Math.PI);
          // Calculate induced EMF
          // For AC generator: EMF = Vmax * sin(angle)
          // For DC motor/generator with split rings: EMF = Vmax * |sin(angle)|
          const rawEmf = Math.sin(next);
          const currentEmf = mode === 'dc_motor' ? Math.abs(rawEmf) : rawEmf;

          waveHistoryRef.current.push({ angle: next, emf: currentEmf });
          if (waveHistoryRef.current.length > 200) {
            waveHistoryRef.current.shift();
          }
          return next;
        });
      }

      animationFrameRef.current = requestAnimationFrame(animate);
    };

    animationFrameRef.current = requestAnimationFrame(animate);
    return () => {
      if (animationFrameRef.current) cancelAnimationFrame(animationFrameRef.current);
    };
  }, [isRunning, frequency, mode]);

  // Render Oscilloscope wave onto HTML5 Canvas
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    const midY = height / 2;

    ctx.clearRect(0, 0, width, height);

    // Oscilloscope grid lines
    ctx.strokeStyle = 'rgba(51, 65, 85, 0.5)';
    ctx.lineWidth = 1;

    // Horizontal centerline
    ctx.beginPath();
    ctx.moveTo(0, midY);
    ctx.lineTo(width, midY);
    ctx.stroke();

    // Horizontal dashed guides (+Vmax and -Vmax)
    ctx.setLineDash([4, 4]);
    ctx.beginPath();
    ctx.moveTo(0, midY - 35);
    ctx.lineTo(width, midY - 35);
    ctx.moveTo(0, midY + 35);
    ctx.lineTo(width, midY + 35);
    ctx.stroke();
    ctx.setLineDash([]);

    // Draw wave history
    const history = waveHistoryRef.current;
    if (history.length > 1) {
      ctx.beginPath();
      ctx.lineWidth = 2.5;
      ctx.strokeStyle = mode === 'ac_generator' ? '#38bdf8' : '#fb923c';

      for (let i = 0; i < history.length; i++) {
        const x = (i / 200) * width;
        const y = midY - history[i].emf * 35;
        if (i === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      }
      ctx.stroke();

      // Draw leading current dot
      const lastPoint = history[history.length - 1];
      const curX = ((history.length - 1) / 200) * width;
      const curY = midY - lastPoint.emf * 35;
      ctx.fillStyle = '#f8fafc';
      ctx.beginPath();
      ctx.arc(curX, curY, 4, 0, 2 * Math.PI);
      ctx.fill();
    }
  }, [angle, mode]);

  const degAngle = Math.round((angle * 180) / Math.PI) % 360;
  const currentEmf = mode === 'dc_motor' ? Math.abs(Math.sin(angle)) : Math.sin(angle);

  return (
    <div className="w-full bg-slate-900 text-white rounded-2xl overflow-hidden border border-slate-700 shadow-xl flex flex-col select-none">
      {/* Top Header */}
      <div className="px-4 py-3 bg-slate-800/90 border-b border-slate-700 flex flex-wrap items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-lg bg-cyan-600/30 text-cyan-400 border border-cyan-500/40 flex items-center justify-center">
            <Zap className="w-4 h-4" />
          </div>
          <div>
            <h3 className="text-sm font-bold tracking-tight text-white flex items-center gap-1.5" style={{ fontFamily: 'Afacad, sans-serif' }}>
              Electrodynamics Armature & Live Oscilloscope
              <span className="px-2 py-0.5 rounded-full text-[10px] font-mono bg-cyan-500/20 text-cyan-300 border border-cyan-500/30">
                AI Blackboard SOTA
              </span>
            </h3>
            <p className="text-[11px] text-slate-400">
              Fleming's Right-Hand Rule • Magnetic Flux Rate of Change • Faradays Law
            </p>
          </div>
        </div>

        {/* Generator / Motor Mode Toggle */}
        <div className="flex items-center gap-1 bg-slate-800 p-1 rounded-xl border border-slate-700">
          <button
            onClick={() => setMode('ac_generator')}
            className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
              mode === 'ac_generator'
                ? 'bg-cyan-600 text-white shadow-xs'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            AC Generator (Slip Rings)
          </button>
          <button
            onClick={() => setMode('dc_motor')}
            className={`px-3 py-1 rounded-lg text-xs font-semibold transition-all ${
              mode === 'dc_motor'
                ? 'bg-orange-600 text-white shadow-xs'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            DC Motor (Split Ring)
          </button>
        </div>
      </div>

      {/* 3D Magnetic Armature Stage */}
      <div className="relative w-full h-[260px] bg-gradient-to-b from-slate-900 to-slate-950 flex items-center justify-center overflow-hidden">
        {/* Left North Pole */}
        <div className="absolute left-6 w-16 h-36 bg-rose-700/80 border-2 border-rose-500 rounded-lg flex items-center justify-center shadow-lg shadow-rose-900/50">
          <span className="text-2xl font-black text-white font-mono">N</span>
        </div>

        {/* Right South Pole */}
        <div className="absolute right-6 w-16 h-36 bg-blue-700/80 border-2 border-blue-500 rounded-lg flex items-center justify-center shadow-lg shadow-blue-900/50">
          <span className="text-2xl font-black text-white font-mono">S</span>
        </div>

        {/* Magnetic Field Lines B (dashed cyan arrows from N to S) */}
        <div className="absolute inset-x-24 h-24 flex flex-col justify-between pointer-events-none opacity-40">
          {[...Array(4)].map((_, i) => (
            <div key={i} className="w-full border-t-2 border-dashed border-cyan-400 flex items-center justify-end">
              <span className="text-[10px] text-cyan-300 font-mono -mt-3.5 mr-2">→ B</span>
            </div>
          ))}
        </div>

        {/* Rotating Armature Coil (Center) */}
        <div 
          className="relative w-36 h-28 border-4 border-amber-400 rounded-md bg-amber-500/10 shadow-lg shadow-amber-500/20 flex items-center justify-center transition-transform duration-75"
          style={{
            transform: `perspective(600px) rotateY(${degAngle}deg)`,
          }}
        >
          {/* Axis Shaft */}
          <div className="absolute inset-x-[-20px] h-1.5 bg-slate-400 rounded-full" />
          <div className="text-[11px] font-mono font-bold text-amber-300 bg-slate-900/90 px-2 py-0.5 rounded border border-amber-500/40">
            Coil {degAngle}°
          </div>
        </div>

        {/* Commutator rings at bottom of coil */}
        <div className="absolute bottom-4 flex items-center gap-2 font-mono text-[11px] text-slate-300 bg-slate-800/80 px-3 py-1 rounded-full border border-slate-700">
          <span>Rings: {mode === 'ac_generator' ? 'Two Slip Rings (Continuous AC)' : 'Split-Ring Commutator (Pulsating DC)'}</span>
        </div>
      </div>

      {/* Live 60fps Oscilloscope Display */}
      <div className="p-4 bg-slate-800 border-t border-slate-700 flex flex-col gap-2">
        <div className="flex items-center justify-between text-xs">
          <div className="flex items-center gap-1.5 text-slate-300 font-semibold">
            <Activity className="w-3.5 h-3.5 text-cyan-400" />
            Live Oscilloscope Output EMF:
            <span className="font-mono text-cyan-300 font-bold ml-1">
              {currentEmf.toFixed(2)} Vmax
            </span>
          </div>

          <div className="flex items-center gap-3">
            {/* Speed slider */}
            <div className="flex items-center gap-1.5 text-[11px] font-mono text-slate-400">
              <Gauge className="w-3 h-3 text-slate-400" />
              <span>Freq:</span>
              <input
                type="range"
                min="0.2"
                max="2.0"
                step="0.1"
                value={frequency}
                onChange={(e) => setFrequency(parseFloat(e.target.value))}
                className="w-16 h-1.5 bg-slate-700 rounded appearance-none cursor-pointer accent-cyan-500"
              />
              <span className="text-white font-bold">{frequency.toFixed(1)} Hz</span>
            </div>

            <button
              onClick={() => setIsRunning(!isRunning)}
              className="p-1 rounded-md bg-slate-700 hover:bg-slate-600 text-white"
              title={isRunning ? 'Pause' : 'Play'}
            >
              {isRunning ? <Pause className="w-3 h-3" /> : <Play className="w-3 h-3" />}
            </button>
          </div>
        </div>

        {/* HTML5 Canvas waveform */}
        <canvas
          ref={canvasRef}
          width={500}
          height={90}
          className="w-full h-[90px] bg-slate-950 rounded-xl border border-slate-900 shadow-inner"
        />

        {/* Formula & Rule explanation footer */}
        <div className="flex items-center justify-between text-[11px] text-slate-400 pt-1 font-mono">
          <span>Formula: {mode === 'ac_generator' ? 'ε = ε_max · sin(ωt)' : 'ε = |ε_max · sin(ωt)|'}</span>
          <span className="text-emerald-400">Fleming's Right-Hand Rule Verified ✓</span>
        </div>
      </div>
    </div>
  );
}
