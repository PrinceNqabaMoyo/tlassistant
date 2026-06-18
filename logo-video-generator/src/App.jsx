import React, { useState, useEffect, useRef } from 'react';
import { 
  Play, 
  Pause, 
  RotateCcw, 
  Video, 
  Settings, 
  Download, 
  Sparkles, 
  Sliders, 
  Type, 
  Layers,
  Palette
} from 'lucide-react';
import { renderFrame, startVideoRender, createParticleSystem, updateParticles, getVideoExportSupport, FINAL_HOLD_DURATION } from './canvasExporter';

const getSvgString = (color, hideAccents) => `
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 800">
  <g>
    <g>
      ${!hideAccents ? `
      <g transform="translate(150, 101.77) scale(0.75)">
        <path transform="translate(-166.4869, -27.606)" fill="${color}" opacity="1.000000" stroke="none" d="M281.100800,82.430374 C296.863281,82.430435 312.139648,82.430435 327.589142,82.430435 C327.589142,101.156349 327.589142,119.218277 327.589142,137.604797 C309.226532,137.604797 291.146423,137.604797 272.610504,137.604797 C272.610504,119.531845 272.610504,101.481499 272.610504,82.430305 C275.160431,82.430305 277.887573,82.430305 281.100800,82.430374 z"/>
        <path fill="${color}" opacity="1.000000" stroke="none" d="M281.100800,82.430374 C296.863281,82.430435 312.139648,82.430435 327.589142,82.430435 C327.589142,101.156349 327.589142,119.218277 327.589142,137.604797 C309.226532,137.604797 291.146423,137.604797 272.610504,137.604797 C272.610504,119.531845 272.610504,101.481499 272.610504,82.430305 C275.160431,82.430305 277.887573,82.430305 281.100800,82.430374 z"/>
        <path fill="${color}" opacity="1.000000" stroke="none" d="M234.051895,135.066223 C224.745880,148.067596 215.644699,160.771545 206.224594,173.920700 C191.142197,163.057236 176.346191,152.400055 161.102249,141.420258 C171.897430,126.295197 182.400925,111.578819 193.222076,96.417397 C208.472687,107.127121 223.382523,117.597542 238.759613,128.396088 C237.075623,130.779358 235.666183,132.774078 234.051895,135.066223 z"/>
        <path fill="${color}" opacity="1.000000" stroke="none" d="M287.318604,233.165192 C273.012787,244.051132 258.971313,254.686829 244.461060,265.677582 C233.276215,250.872467 222.308655,236.354980 211.026871,221.421555 C225.902328,210.163956 240.315781,199.255997 254.990143,188.150589 C256.061981,189.313354 257.003143,190.179214 257.763031,191.182358 C267.103516,203.512344 276.449860,215.838257 285.690308,228.242981 C286.661530,229.546768 286.967987,231.345734 287.318604,233.165192 z"/>
      </g>
      ` : ''}
      <path fill="${color}" opacity="1.000000" stroke="none" d=" M346.618164,323.599243 C390.887054,300.100555 434.830627,276.778168 478.816315,253.535477 C490.312988,247.460464 502.069885,242.258408 515.593506,242.888382 C526.837036,243.412109 536.962891,247.456100 546.631958,252.590546 C605.086304,283.631073 663.469849,314.805176 721.830627,346.021515 C741.277954,356.423615 760.671387,366.933228 779.924744,377.688446 C788.846985,382.672546 793.581482,390.354065 793.151917,401.025787 C792.944519,406.178833 790.979065,410.274750 786.950012,412.873901 C776.925781,419.340515 766.795715,425.687531 756.382141,431.498291 C715.830627,454.125977 675.130371,476.487030 634.528320,499.024323 C603.924683,516.011719 573.575562,533.471863 542.694214,549.935608 C534.276367,554.423462 524.518555,557.463745 515.060120,558.648132 C504.622375,559.955017 494.436676,555.726318 485.240387,550.665100 C439.169922,525.310059 393.255981,499.670929 347.238922,474.218567 C315.021484,456.398865 282.718964,438.733063 250.479980,420.952118 C247.576355,419.350677 244.919174,417.307678 242.047882,415.641510 C228.019974,407.501282 231.543488,389.717133 240.164764,382.425934 C245.302017,378.081238 251.256653,374.559265 257.211456,371.349426 C286.843445,355.376984 316.597473,339.630981 346.618164,323.599243 M509.620361,444.230133 C512.299622,444.117645 515.457214,444.896881 517.584778,443.755798 C540.802307,431.303711 563.873291,418.577637 586.946411,405.857727 C591.374939,403.416290 591.300964,401.418671 586.821289,398.972992 C563.992676,386.509277 541.118408,374.128845 518.327942,361.595978 C514.570251,359.529572 511.388153,359.634857 507.630035,361.713196 C485.298676,374.062622 462.845703,386.191986 440.495819,398.508331 C438.778381,399.454742 437.540466,401.126362 436.079681,402.538502 C437.656189,403.882191 439.057922,405.543751 440.835754,406.511321 C463.496643,418.986617 486.211426,431.348831 509.620361,444.085133 z"/>
      <path fill="${color}" opacity="1.000000" stroke="none" d=" M530.902283,583.963318 C579.000061,555.740784 626.738159,527.630981 675.098083,499.154999 C675.098083,501.254150 675.080383,502.833069 675.100769,504.411560 C675.431519,530.050720 676.440857,555.704041 675.899902,581.324646 C675.419739,604.060913 666.363403,623.657898 648.652710,638.331360 C640.255859,645.288208 630.888550,651.135437 621.655457,657.004822 C611.017029,663.767578 600.027039,669.975891 589.215393,676.467773 C573.771118,685.741272 558.458008,695.238708 542.890686,704.299988 C525.288452,714.545654 506.851746,716.305420 488.165741,707.565125 C473.860107,700.873718 459.910980,693.423096 445.759888,686.397583 C421.355072,674.281494 396.832611,662.399475 372.516479,650.108765 C349.411194,638.429932 333.341370,620.744141 327.668762,594.873291 C326.400208,589.087646 325.419006,583.097412 325.412933,577.200256 C325.381042,546.214417 325.703827,515.228271 325.917938,484.242279 C325.919891,483.960632 326.119965,483.680389 326.393372,482.966705 C337.198914,489.207153 347.928986,495.411743 358.666290,501.603729 C406.111877,528.964600 453.515015,556.399719 501.075989,583.558533 C505.773682,586.241089 511.401672,588.452820 516.671387,588.624268 C521.240967,588.773010 525.914856,585.716187 530.902283,583.963318 z"/>
      <path fill="${color}" opacity="1.000000" stroke="none" d="M727.104553,542.000000 C727.104492,554.662109 727.255981,566.827271 727.010742,578.984436 C726.939697,582.507202 727.955078,584.633972 730.756042,586.836365 C745.057800,598.081787 747.519531,617.167419 735.435364,629.111267 C730.770569,633.721924 731.136902,637.142212 732.927734,642.274536 C738.051880,656.959961 742.820801,671.769775 747.685852,686.545044 C751.600159,698.432983 748.005920,705.663330 735.837463,709.084167 C723.171570,712.644958 710.215027,711.725037 697.413269,709.852844 C692.003113,709.061584 687.834473,705.635925 684.933289,700.724121 C682.407043,696.447144 682.672607,692.277222 684.186523,687.836975 C689.837402,671.263672 695.343201,654.640625 701.083069,638.098511 C702.138062,635.057983 701.908508,633.276367 699.294861,630.955688 C686.045898,619.191650 687.093201,598.850830 701.525269,587.564697 C704.625305,585.140381 705.654602,582.683167 705.627808,578.857422 C705.446960,553.035034 705.451660,527.210693 705.563782,501.387695 C705.577026,498.349792 706.090027,495.091919 707.283569,492.330231 C709.385864,487.465454 715.054260,484.735840 719.237549,485.864258 C724.024475,487.155518 727.051208,491.551239 727.070496,497.516357 C727.117920,512.177490 727.097900,526.838745 727.104553,542.000000 z"/>
    </g>
  </g>
</svg>
`;

export default function App() {
  // --- Options State ---
  const [options, setOptions] = useState({
    duration: 5.0,
    formationMode: 'pixelate',
    constellationVariant: 'medium',
    pixelIntensity: 24,
    glowIntensity: 20,
    accentColor: '#ff9100',
    titleText: 'fundile', // Lowercase default
    taglineText: 'A Curriculum-aligned Teaching & Learning Assistant',
    titleFontScale: 100,
    taglineFontScale: 100,
    constellationDensity: 100,
    constellationSpread: 120,
    constellationLineStrength: 55,
    showConstellationRadialGlow: false,
    hideAccentSquares: false,
    bgStyle: 'original-blue', // Brand original blue background by default
    exportFormat: 'auto',
    particleCount: 50,
    particleSpeed: 1.0,
  });

  // --- Playback State ---
  const [isPlaying, setIsPlaying] = useState(true);
  const [currentTime, setCurrentTime] = useState(0.0);
  const [activeTab, setActiveTab] = useState('animation'); // animation, brand, particles, output

  // --- Rendering State ---
  const [isExporting, setIsExporting] = useState(false);
  const [exportProgress, setExportProgress] = useState(0);
  const [exportedVideoUrl, setExportedVideoUrl] = useState(null);
  const [exportedType, setExportedType] = useState('webm');
  const [exportError, setExportError] = useState('');

  // --- Refs ---
  const canvasRef = useRef(null);
  const animationFrameRef = useRef(null);
  const lastTimeRef = useRef(null);
  const svgImageRef = useRef(null);
  const particlesRef = useRef([]);

  // Generate real-time particle system on canvas dimension change
  useEffect(() => {
    particlesRef.current = createParticleSystem(options.particleCount, 960, 540);
  }, [options.particleCount]);

  // Load SVG Image whenever styles change
  useEffect(() => {
    const svgString = getSvgString(options.accentColor, options.hideAccentSquares);
    const svgBlob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(svgBlob);
    
    const img = new Image();
    img.onload = () => {
      svgImageRef.current = img;
      // Trigger a render frame if paused to reflect changes instantly
      if (!isPlaying) {
        drawPreviewFrame();
      }
    };
    img.src = url;

    return () => {
      URL.revokeObjectURL(url);
    };
  }, [options.accentColor, options.hideAccentSquares]);

  // Function to draw a single preview frame (960x540)
  const drawPreviewFrame = () => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const renderTime = Math.min(currentTime, options.duration);
    
    renderFrame(
      ctx, 
      canvas.width, 
      canvas.height, 
      renderTime, 
      options.duration, 
      options, 
      svgImageRef.current, 
      particlesRef.current,
      getSvgString(options.accentColor, options.hideAccentSquares)
    );
  };

  const exportSupport = getVideoExportSupport();
  const mp4Unsupported = options.exportFormat === 'mp4' && !exportSupport.mp4;
  const totalPlaybackDuration = options.duration + FINAL_HOLD_DURATION;

  // Playback Loop
  useEffect(() => {
    if (!isPlaying || isExporting) {
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }
      lastTimeRef.current = null;
      return;
    }

    const playLoop = (timestamp) => {
      if (!lastTimeRef.current) {
        lastTimeRef.current = timestamp;
      }
      
      const delta = (timestamp - lastTimeRef.current) / 1000;
      lastTimeRef.current = timestamp;

      setCurrentTime(prevTime => {
        const nextTime = prevTime + delta;
        if (nextTime >= totalPlaybackDuration) {
          // Loop around
          return 0.0;
        }
        return nextTime;
      });

      // Update particle positions
      if (currentTime < options.duration) {
        updateParticles(particlesRef.current, 960, 540, options.particleSpeed);
      }

      // Render Frame
      drawPreviewFrame();
      
      animationFrameRef.current = requestAnimationFrame(playLoop);
    };

    animationFrameRef.current = requestAnimationFrame(playLoop);

    return () => {
      if (animationFrameRef.current) {
        cancelAnimationFrame(animationFrameRef.current);
      }
    };
  }, [isPlaying, currentTime, options, isExporting, totalPlaybackDuration]);

  // Redraw when scrubbing manually (paused)
  useEffect(() => {
    if (!isPlaying) {
      drawPreviewFrame();
    }
  }, [currentTime, options]);

  const togglePlayback = () => setIsPlaying(!isPlaying);
  
  const resetPlayback = () => {
    setIsPlaying(false);
    setCurrentTime(0.0);
  };

  // Trigger high-res export
  const handleExport = async () => {
    if (mp4Unsupported) {
      setExportError('MP4 export is not supported in this browser. Please switch to Auto or WebM.');
      setActiveTab('output');
      return;
    }

    setIsPlaying(false);
    setIsExporting(true);
    setExportProgress(0);
    setExportedVideoUrl(null);
    setExportError('');

    const svgString = getSvgString(options.accentColor, options.hideAccentSquares);
    
    try {
      await startVideoRender(
        options, 
        svgString, 
        (progress) => setExportProgress(progress),
        (videoUrl, ext) => {
          setExportedVideoUrl(videoUrl);
          setExportedType(ext);
          setIsExporting(false);
          setActiveTab('output');
        }
      );
    } catch (err) {
      console.error(err);
      setExportError(err.message || 'Error rendering video.');
      setActiveTab('output');
      setIsExporting(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col">
      {/* Header */}
      <header className="glass-panel border-b px-6 py-4 flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <div className="bg-gradient-to-tr from-amber-500 to-orange-600 p-2.5 rounded-xl shadow-lg orange-box-glow">
            <Sparkles className="h-6 w-6 text-white" />
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight bg-gradient-to-r from-white via-slate-100 to-amber-400 bg-clip-text text-transparentOutfit">
              Fundile Logo Intro Video Generator
            </h1>
            <p className="text-xs text-slate-400 font-medium font-sans">
              Create and export a highly aesthetic 1080p intro for your app's demo video
            </p>
          </div>
        </div>
        <div className="flex items-center space-x-2 text-xs font-semibold px-3 py-1.5 rounded-full bg-slate-800/40 border border-slate-700/50 text-slate-300">
          <span className="h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></span>
          <span>Self-contained sub-project</span>
        </div>
      </header>

      {/* Main Workspace */}
      <div className="flex-1 grid grid-cols-1 lg:grid-cols-12 gap-6 p-6 overflow-hidden">
        {/* Preview Panel (Left) */}
        <div className="lg:col-span-7 flex flex-col space-y-4">
          <div className="flex-1 glass-panel rounded-2xl p-4 flex flex-col justify-between overflow-hidden relative group">
            {/* Visualizer Canvas container */}
            <div className="flex-1 flex items-center justify-center bg-black/40 rounded-xl overflow-hidden relative border border-slate-900 shadow-inner">
              <canvas
                ref={canvasRef}
                width={960}
                height={540}
                className="w-full h-auto max-h-[460px] aspect-video object-contain"
              />
              {isExporting && (
                <div className="absolute inset-0 bg-black/85 backdrop-blur-md flex flex-col items-center justify-center z-20 transition-all">
                  <div className="w-16 h-16 rounded-full border-4 border-amber-500/20 border-t-amber-500 animate-spin mb-4"></div>
                  <h3 className="text-lg font-bold text-white mb-2 orange-glow">Rendering High-Resolution 1080p Video</h3>
                  <div className="w-64 bg-slate-800 h-2 rounded-full overflow-hidden border border-slate-700/50 shadow-md">
                    <div 
                      className="bg-gradient-to-r from-amber-400 to-orange-500 h-full rounded-full transition-all duration-300 shadow-inner"
                      style={{ width: `${exportProgress}%` }}
                    />
                  </div>
                  <span className="text-sm font-bold text-amber-400 mt-2 font-mono">{exportProgress}% Completed</span>
                  <p className="text-xs text-slate-400 mt-3 italic">
                    Sequentially rendering exact frames... Please do not close this tab.
                  </p>
                </div>
              )}
            </div>

            {/* Timelines and Scrubber */}
            <div className="mt-4 space-y-3">
              <div className="flex items-center space-x-3 bg-slate-900/50 px-4 py-2.5 rounded-xl border border-slate-800/40">
                <button
                  onClick={togglePlayback}
                  disabled={isExporting}
                  className="p-2 rounded-lg bg-amber-500 hover:bg-amber-600 text-slate-950 font-bold transition-all shadow-md active:scale-95 disabled:opacity-50"
                  title={isPlaying ? "Pause" : "Play"}
                >
                  {isPlaying ? <Pause className="h-4 w-4" fill="currentColor" /> : <Play className="h-4 w-4" fill="currentColor" />}
                </button>
                <button
                  onClick={resetPlayback}
                  disabled={isExporting}
                  className="p-2 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700/50 transition-all shadow active:scale-95 disabled:opacity-50"
                  title="Rewind / Reset"
                >
                  <RotateCcw className="h-4 w-4" />
                </button>
                
                {/* Time Indicator */}
                <div className="text-xs font-bold font-mono text-slate-300 w-24">
                  {currentTime.toFixed(2)}s / {totalPlaybackDuration.toFixed(1)}s
                </div>

                {/* Timeline slider */}
                <input
                  type="range"
                  min={0}
                  max={totalPlaybackDuration}
                  step={0.01}
                  value={currentTime}
                  disabled={isExporting}
                  onChange={(e) => {
                    setIsPlaying(false);
                    setCurrentTime(parseFloat(e.target.value));
                  }}
                  className="flex-1 accent-amber-500 bg-slate-800 h-1.5 rounded-lg appearance-none cursor-pointer"
                />
              </div>
            </div>
          </div>
        </div>

        {/* Controls Panel (Right) */}
        <div className="lg:col-span-5 flex flex-col h-full">
          <div className="flex-1 glass-panel rounded-2xl overflow-hidden flex flex-col border border-slate-800/80 shadow-2xl">
            {/* Tabs */}
            <div className="flex border-b border-slate-800/80 bg-slate-900/40 text-sm">
              <button
                onClick={() => setActiveTab('animation')}
                className={`flex-1 py-3 px-4 flex items-center justify-center space-x-2 font-semibold border-b-2 transition-all ${
                  activeTab === 'animation' 
                    ? 'border-amber-500 text-amber-400 bg-amber-500/5' 
                    : 'border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/20'
                }`}
              >
                <Sliders className="h-4 w-4" />
                <span>Animation</span>
              </button>
              <button
                onClick={() => setActiveTab('brand')}
                className={`flex-1 py-3 px-4 flex items-center justify-center space-x-2 font-semibold border-b-2 transition-all ${
                  activeTab === 'brand' 
                    ? 'border-amber-500 text-amber-400 bg-amber-500/5' 
                    : 'border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/20'
                }`}
              >
                <Type className="h-4 w-4" />
                <span>Branding</span>
              </button>
              <button
                onClick={() => setActiveTab('particles')}
                className={`flex-1 py-3 px-4 flex items-center justify-center space-x-2 font-semibold border-b-2 transition-all ${
                  activeTab === 'particles' 
                    ? 'border-amber-500 text-amber-400 bg-amber-500/5' 
                    : 'border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/20'
                }`}
              >
                <Sparkles className="h-4 w-4" />
                <span>FX</span>
              </button>
              <button
                onClick={() => setActiveTab('output')}
                className={`flex-1 py-3 px-4 flex items-center justify-center space-x-2 font-semibold border-b-2 transition-all ${
                  activeTab === 'output' 
                    ? 'border-amber-500 text-amber-400 bg-amber-500/5' 
                    : 'border-transparent text-slate-400 hover:text-slate-200 hover:bg-slate-800/20'
                }`}
              >
                <Video className="h-4 w-4" />
                <span>Export</span>
              </button>
            </div>

            {/* Tab Contents */}
            <div className="flex-1 p-6 overflow-y-auto space-y-6">
              
              {/* Tab: Animation Parameters */}
              {activeTab === 'animation' && (
                <div className="space-y-5">
                  <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                    <Layers className="h-4 w-4 text-amber-400" />
                    <span>Intro Video Config</span>
                  </h3>
                  
                  {/* Slider: Duration */}
                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">Animation Duration</span>
                      <span className="text-amber-400 font-mono font-bold">{options.duration.toFixed(1)} seconds + {FINAL_HOLD_DURATION.toFixed(0)}s hold</span>
                    </div>
                    <input
                      type="range"
                      min={3.0}
                      max={8.0}
                      step={0.5}
                      value={options.duration}
                      onChange={(e) => setOptions({ ...options, duration: parseFloat(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                    <p className="text-[10px] text-slate-500 font-medium">
                      The final composed frame now stays fixed for {FINAL_HOLD_DURATION.toFixed(0)} extra seconds to make editing and transitions easier.
                    </p>
                  </div>

                  <div className="space-y-2">
                    <span className="text-xs font-semibold text-slate-400">Logo Formation Style</span>
                    <div className="grid grid-cols-2 gap-2">
                      {[
                        { id: 'pixelate', label: 'Pixel Gather' },
                        { id: 'constellation', label: 'Constellation Gather' }
                      ].map((mode) => (
                        <button
                          key={mode.id}
                          onClick={() => setOptions({ ...options, formationMode: mode.id })}
                          className={`py-2 px-3 rounded-lg text-xs font-bold border transition-all ${
                            options.formationMode === mode.id
                              ? 'border-amber-500/50 bg-amber-500/10 text-amber-400'
                              : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:text-slate-200'
                          }`}
                        >
                          {mode.label}
                        </button>
                      ))}
                    </div>
                  </div>

                  {options.formationMode === 'constellation' && (
                    <div className="space-y-5 rounded-xl border border-slate-800/50 bg-slate-900/25 p-4">
                      <div className="space-y-2">
                        <span className="text-xs font-semibold text-slate-400">Constellation Variant</span>
                        <div className="grid grid-cols-2 gap-2">
                          {[
                            { id: 'medium', label: 'Classic' },
                            { id: 'premium', label: 'Premium' }
                          ].map((variant) => (
                            <button
                              key={variant.id}
                              onClick={() => setOptions({ ...options, constellationVariant: variant.id })}
                              className={`py-2 px-3 rounded-lg text-xs font-bold border transition-all ${
                                options.constellationVariant === variant.id
                                  ? 'border-amber-500/50 bg-amber-500/10 text-amber-400'
                                  : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:text-slate-200'
                              }`}
                            >
                              {variant.label}
                            </button>
                          ))}
                        </div>
                      </div>

                      <div className="space-y-2">
                        <div className="flex justify-between text-xs font-semibold">
                          <span className="text-slate-400">Constellation Density</span>
                          <span className="text-amber-400 font-mono font-bold">{options.constellationDensity}%</span>
                        </div>
                        <input
                          type="range"
                          min={70}
                          max={180}
                          step={5}
                          value={options.constellationDensity}
                          onChange={(e) => setOptions({ ...options, constellationDensity: parseInt(e.target.value) })}
                          className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                        />
                      </div>

                      <div className="space-y-2">
                        <div className="flex justify-between text-xs font-semibold">
                          <span className="text-slate-400">Gather Spread</span>
                          <span className="text-amber-400 font-mono font-bold">{options.constellationSpread}%</span>
                        </div>
                        <input
                          type="range"
                          min={80}
                          max={180}
                          step={5}
                          value={options.constellationSpread}
                          onChange={(e) => setOptions({ ...options, constellationSpread: parseInt(e.target.value) })}
                          className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                        />
                      </div>

                      <div className="space-y-2">
                        <div className="flex justify-between text-xs font-semibold">
                          <span className="text-slate-400">Link Strength</span>
                          <span className="text-amber-400 font-mono font-bold">{options.constellationLineStrength}%</span>
                        </div>
                        <input
                          type="range"
                          min={0}
                          max={100}
                          step={5}
                          value={options.constellationLineStrength}
                          onChange={(e) => setOptions({ ...options, constellationLineStrength: parseInt(e.target.value) })}
                          className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                        />
                      </div>

                      <label className="flex items-center space-x-3 bg-slate-900/30 p-3.5 rounded-xl border border-slate-800/40 cursor-pointer select-none">
                        <input
                          type="checkbox"
                          checked={options.showConstellationRadialGlow}
                          onChange={(e) => setOptions({ ...options, showConstellationRadialGlow: e.target.checked })}
                          className="w-4 h-4 text-amber-500 accent-amber-500 border-slate-700 bg-slate-800 rounded cursor-pointer"
                        />
                        <div>
                          <span className="text-xs font-bold text-slate-200 block">Show Background Radial Glow</span>
                          <span className="text-[10px] text-slate-500">Adds the soft circular highlight behind the logo during constellation mode.</span>
                        </div>
                      </label>
                    </div>
                  )}

                  {/* Slider: Pixel Block Size */}
                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">Initial Pixel Block Size</span>
                      <span className="text-amber-400 font-mono font-bold">{options.pixelIntensity}px</span>
                    </div>
                    <input
                      type="range"
                      min={8}
                      max={48}
                      step={2}
                      value={options.pixelIntensity}
                      onChange={(e) => setOptions({ ...options, pixelIntensity: parseInt(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                    <p className="text-[10px] text-slate-500 font-medium">
                      Controls the degree of blocky mosaic pixelation at the start of the intro.
                    </p>
                  </div>

                  {/* Color Picker: Accent */}
                  <div className="space-y-3 bg-slate-900/30 p-4 rounded-xl border border-slate-800/40">
                    <span className="text-xs font-semibold text-slate-400 block">Theme Palette & Accents</span>
                    <div className="flex items-center space-x-4">
                      <input
                        type="color"
                        value={options.accentColor}
                        onChange={(e) => setOptions({ ...options, accentColor: e.target.value })}
                        className="w-12 h-10 rounded border border-slate-700 bg-slate-800 cursor-pointer p-0.5"
                      />
                      <div>
                        <span className="text-xs font-bold text-slate-200 block">Logo Accent Color</span>
                        <span className="text-[10px] text-slate-400 uppercase font-mono">{options.accentColor}</span>
                      </div>
                    </div>
                  </div>

                  {/* Background Selector */}
                  <div className="space-y-2">
                    <span className="text-xs font-semibold text-slate-400">Background Styling</span>
                    <div className="grid grid-cols-2 gap-2">
                      {[
                        { id: 'original-blue', label: 'Original Blue (#13519C)' },
                        { id: 'dark-radial', label: 'Indigo Radial' },
                        { id: 'dark-linear', label: 'Slate Linear' },
                        { id: 'plain-black', label: 'Solid Black' }
                      ].map(bg => (
                        <button
                          key={bg.id}
                          onClick={() => setOptions({ ...options, bgStyle: bg.id })}
                          className={`py-2 px-1 rounded-lg text-xs font-bold border transition-all ${
                            options.bgStyle === bg.id
                              ? 'border-amber-500/50 bg-amber-500/10 text-amber-400'
                              : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:text-slate-200'
                          }`}
                        >
                          {bg.label}
                        </button>
                      ))}
                    </div>
                  </div>

                  {/* Accent Squares Toggle */}
                  <label className="flex items-center space-x-3 bg-slate-900/30 p-3.5 rounded-xl border border-slate-800/40 cursor-pointer select-none">
                    <input
                      type="checkbox"
                      checked={options.hideAccentSquares}
                      onChange={(e) => setOptions({ ...options, hideAccentSquares: e.target.checked })}
                      className="w-4 h-4 text-amber-500 accent-amber-500 border-slate-700 bg-slate-800 rounded cursor-pointer"
                    />
                    <div>
                      <span className="text-xs font-bold text-slate-200 block">Hide SVG Accent Squares</span>
                      <span className="text-[10px] text-slate-500">Removes the outer decorative square geometries from the graduation cap.</span>
                    </div>
                  </label>
                </div>
              )}

              {/* Tab: Branding */}
              {activeTab === 'brand' && (
                <div className="space-y-5">
                  <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                    <Type className="h-4 w-4 text-amber-400" />
                    <span>Text & Branding Overlay</span>
                  </h3>

                  {/* Input: Title */}
                  <div className="space-y-2">
                    <label className="text-xs font-semibold text-slate-400 block">App Title</label>
                    <input
                      type="text"
                      value={options.titleText}
                      onChange={(e) => setOptions({ ...options, titleText: e.target.value })}
                      placeholder="Title"
                      className="w-full glass-input px-4 py-2.5 rounded-xl text-slate-200 font-bold tracking-wide"
                    />
                  </div>

                  {/* Input: Tagline */}
                  <div className="space-y-2">
                    <label className="text-xs font-semibold text-slate-400 block">Slogan / Suffix Slogans</label>
                    <textarea
                      value={options.taglineText}
                      rows={2}
                      onChange={(e) => setOptions({ ...options, taglineText: e.target.value })}
                      placeholder="Tagline"
                      className="w-full glass-input px-4 py-2.5 rounded-xl text-slate-300 text-sm"
                    />
                  </div>

                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">App Title Size</span>
                      <span className="text-amber-400 font-mono font-bold">{options.titleFontScale}%</span>
                    </div>
                    <input
                      type="range"
                      min={60}
                      max={160}
                      step={5}
                      value={options.titleFontScale}
                      onChange={(e) => setOptions({ ...options, titleFontScale: parseInt(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                  </div>

                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">Slogan Size</span>
                      <span className="text-amber-400 font-mono font-bold">{options.taglineFontScale}%</span>
                    </div>
                    <input
                      type="range"
                      min={60}
                      max={180}
                      step={5}
                      value={options.taglineFontScale}
                      onChange={(e) => setOptions({ ...options, taglineFontScale: parseInt(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                  </div>

                  {/* Typography Glow Slider */}
                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">Title Neon Glow Blur</span>
                      <span className="text-amber-400 font-mono font-bold">{options.glowIntensity}px</span>
                    </div>
                    <input
                      type="range"
                      min={0}
                      max={40}
                      value={options.glowIntensity}
                      onChange={(e) => setOptions({ ...options, glowIntensity: parseInt(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                  </div>
                </div>
              )}

              {/* Tab: Particles / FX */}
              {activeTab === 'particles' && (
                <div className="space-y-5">
                  <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                    <Palette className="h-4 w-4 text-amber-400" />
                    <span>Special Effects System</span>
                  </h3>

                  {/* Slider: Count */}
                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">Sparkle Particle Count</span>
                      <span className="text-amber-400 font-mono font-bold">{options.particleCount} dusts</span>
                    </div>
                    <input
                      type="range"
                      min={0}
                      max={150}
                      step={5}
                      value={options.particleCount}
                      onChange={(e) => setOptions({ ...options, particleCount: parseInt(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                    <p className="text-[10px] text-slate-500 font-medium">
                      Simulates beautiful ambient floating gold embers rising up behind the logo.
                    </p>
                  </div>

                  {/* Slider: Speed */}
                  <div className="space-y-2">
                    <div className="flex justify-between text-xs font-semibold">
                      <span className="text-slate-400">Particle Floating Speed</span>
                      <span className="text-amber-400 font-mono font-bold">{options.particleSpeed.toFixed(1)}x</span>
                    </div>
                    <input
                      type="range"
                      min={0.2}
                      max={3.0}
                      step={0.1}
                      value={options.particleSpeed}
                      onChange={(e) => setOptions({ ...options, particleSpeed: parseFloat(e.target.value) })}
                      className="w-full accent-amber-500 h-1 bg-slate-800 rounded appearance-none cursor-pointer"
                    />
                  </div>
                </div>
              )}

              {/* Tab: Output & Exports */}
              {activeTab === 'output' && (
                <div className="space-y-5">
                  <h3 className="text-sm font-bold text-slate-300 uppercase tracking-wider flex items-center space-x-2">
                    <Video className="h-4 w-4 text-amber-400" />
                    <span>Render Video Exports</span>
                  </h3>

                  <div className="space-y-3 rounded-xl border border-slate-800/70 bg-slate-900/30 p-4">
                    <span className="text-xs font-semibold text-slate-400 block">Export Format</span>
                    <div className="grid grid-cols-3 gap-2">
                      {[
                        { id: 'auto', label: 'Auto' },
                        { id: 'webm', label: 'WebM' },
                        { id: 'mp4', label: 'MP4' }
                      ].map((format) => (
                        <button
                          key={format.id}
                          onClick={() => {
                            setOptions({ ...options, exportFormat: format.id });
                            setExportError('');
                          }}
                          className={`py-2 px-3 rounded-lg text-xs font-bold border transition-all ${
                            options.exportFormat === format.id
                              ? 'border-amber-500/50 bg-amber-500/10 text-amber-400'
                              : 'border-slate-800 bg-slate-900/30 text-slate-400 hover:text-slate-200'
                          }`}
                        >
                          {format.label}
                        </button>
                      ))}
                    </div>
                    <div className="text-[11px] text-slate-500 space-y-1">
                      <div>Detected support: WebM {exportSupport.webm ? 'available' : 'unavailable'} | MP4 {exportSupport.mp4 ? 'available' : 'unavailable'}</div>
                      {options.exportFormat === 'auto' && (
                        <div>Auto will use the best supported format available in this browser.</div>
                      )}
                    </div>
                    {mp4Unsupported && (
                      <div className="rounded-lg border border-amber-500/25 bg-amber-500/10 px-3 py-2 text-xs text-amber-300">
                        MP4 export is not supported in this browser. Switch to Auto or WebM for this device.
                      </div>
                    )}
                    {exportError && (
                      <div className="rounded-lg border border-rose-500/25 bg-rose-500/10 px-3 py-2 text-xs text-rose-300">
                        {exportError}
                      </div>
                    )}
                  </div>
                  
                  <div className="p-4 rounded-xl bg-slate-900/40 border border-slate-800/80 space-y-4">
                    <div className="flex items-start space-x-3 text-xs text-slate-400">
                      <span className="bg-amber-500/10 text-amber-400 p-1.5 rounded-lg border border-amber-500/20 font-bold font-mono">1080p</span>
                      <p className="leading-relaxed">
                        Outputs a crystal clear, high-resolution Full HD (<span className="text-slate-200 font-semibold">1920x1080</span>) video recorded programmatically at a perfect <span className="text-slate-200 font-semibold">60fps</span> with custom settings.
                      </p>
                    </div>
                    
                    {!exportedVideoUrl ? (
                      <button
                        onClick={handleExport}
                        disabled={isExporting || mp4Unsupported}
                        className="w-full py-3 px-4 bg-gradient-to-r from-amber-500 to-orange-600 hover:from-amber-600 hover:to-orange-700 text-slate-950 font-extrabold rounded-xl transition-all shadow-lg active:scale-98 flex items-center justify-center space-x-2 glow-btn cursor-pointer disabled:opacity-50"
                      >
                        <Video className="h-5 w-5 text-slate-950 fill-current" />
                        <span>Generate & Export 1080p Intro</span>
                      </button>
                    ) : (
                      <div className="space-y-3">
                        <div className="p-3 bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-xs rounded-xl font-bold flex items-center space-x-2">
                          <span className="h-2.5 w-2.5 rounded-full bg-emerald-400 animate-ping"></span>
                          <span>Video intro successfully generated!</span>
                        </div>
                        
                        {/* Download button */}
                        <a
                          href={exportedVideoUrl}
                          download={`fundile-logo-intro.${exportedType}`}
                          className="w-full py-3 px-4 bg-gradient-to-r from-emerald-500 to-teal-600 hover:from-emerald-600 hover:to-teal-700 text-white font-extrabold rounded-xl transition-all shadow-lg active:scale-98 flex items-center justify-center space-x-2 cursor-pointer"
                        >
                          <Download className="h-5 w-5" />
                          <span>Download Intro Video (.{exportedType})</span>
                        </a>

                        <button
                          onClick={() => setExportedVideoUrl(null)}
                          className="w-full py-2.5 px-4 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-300 rounded-xl border border-slate-700/50 transition-all"
                        >
                          Render Another Combination
                        </button>
                      </div>
                    )}
                  </div>

                  <div className="bg-slate-900/20 p-4 rounded-xl border border-slate-800/60 text-xs space-y-2 text-slate-400">
                    <span className="font-bold text-slate-300 block">🎬 Usage Guide:</span>
                    <ol className="list-decimal pl-4 space-y-1.5">
                      <li>Use standard video editing tools (DaVinci Resolve, CapCut, Premiere, AE) to prepend this video file to your app's demo video.</li>
                      <li>For transparency, you can set the background option to **"Solid Black"** and use **Add / Screen blend mode** inside your video editor.</li>
                      <li>Auto picks the best export format this browser can record. Choose MP4 only when the support indicator shows it is available.</li>
                    </ol>
                  </div>
                </div>
              )}
            </div>
            
            {/* Control Panel Footer */}
            <div className="p-4 border-t border-slate-800 bg-slate-900/60 flex justify-between items-center text-xs">
              <span className="text-slate-500 font-semibold font-mono">FRAME CAPTURE SYSTEM v1.0</span>
              {!isExporting && !exportedVideoUrl && (
                <button
                  onClick={handleExport}
                  disabled={mp4Unsupported}
                  className="px-4 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700/60 font-bold rounded-lg transition-all flex items-center space-x-1.5 cursor-pointer"
                >
                  <Video className="h-3.5 w-3.5 text-amber-500" />
                  <span>Quick Export</span>
                </button>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
