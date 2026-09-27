import React, { useEffect, useRef, useState } from 'react';
import GraduationCapSplash from './GraduationCapSplash';
import { renderFrame, FINAL_HOLD_DURATION } from '../../../logo-video-generator/src/canvasExporter';

const splashOptions = {
  duration: 2.8, // Punchy 2.8s total animation
  formationMode: 'constellation',
  constellationVariant: 'classic',
  pixelIntensity: 24,
  glowIntensity: 0,
  accentColor: '#ff9100',
  titleText: 'fundile',
  taglineText: 'A Curriculum-aligned Teaching & Learning Assistant',
  titleFontScale: 160,
  taglineFontScale: 130,
  constellationDensity: 100,
  constellationSpread: 120,
  constellationLineStrength: 10,
  showConstellationRadialGlow: false,
  hideAccentSquares: false,
  bgStyle: 'original-blue',
  particleCount: 0,
  particleSpeed: 1,
};

const SplashScreen = ({ onComplete }) => {
  const [isVisible, setIsVisible] = useState(true);
  const canvasRef = useRef(null);
  const svgHostRef = useRef(null);
  
  // Guard against React StrictMode / re-render double execution
  const hasStartedRef = useRef(false);
  const isFinishedRef = useRef(false);
  const onCompleteRef = useRef(onComplete);
  onCompleteRef.current = onComplete;

  const finishSplash = () => {
    if (isFinishedRef.current) return;
    isFinishedRef.current = true;
    setIsVisible(false);
    window.setTimeout(() => {
      if (typeof onCompleteRef.current === 'function') {
        onCompleteRef.current();
      }
    }, 400);
  };

  useEffect(() => {
    if (hasStartedRef.current) {
      return undefined;
    }
    hasStartedRef.current = true;

    const canvas = canvasRef.current;
    const svgElement = svgHostRef.current?.querySelector('svg');

    if (!canvas || !svgElement) {
      finishSplash();
      return undefined;
    }

    const ctx = canvas.getContext('2d');
    const svgMarkup = svgElement.outerHTML;
    const svgBlob = new Blob([svgMarkup], { type: 'image/svg+xml;charset=utf-8' });
    const svgUrl = URL.createObjectURL(svgBlob);
    const svgImage = new Image();
    const totalDuration = splashOptions.duration + FINAL_HOLD_DURATION;
    let animationFrameId;
    let startTimestamp = null;
    let completeTimeout;
    let fontWaitTimeout;

    const syncCanvasSize = () => {
      const dpr = window.devicePixelRatio || 1;
      const width = Math.max(1, Math.floor(window.innerWidth * dpr));
      const height = Math.max(1, Math.floor(window.innerHeight * dpr));

      if (canvas.width !== width || canvas.height !== height) {
        canvas.width = width;
        canvas.height = height;
      }

      return { width, height };
    };

    const draw = (timestamp) => {
      if (isFinishedRef.current) return;

      if (startTimestamp === null) {
        startTimestamp = timestamp;
      }

      const elapsedSeconds = Math.min((timestamp - startTimestamp) / 1000, totalDuration);
      const renderTime = Math.min(elapsedSeconds, splashOptions.duration);
      const { width, height } = syncCanvasSize();

      renderFrame(ctx, width, height, renderTime, splashOptions.duration, splashOptions, svgImage, [], '');

      if (elapsedSeconds < totalDuration) {
        animationFrameId = window.requestAnimationFrame(draw);
      } else {
        finishSplash();
      }
    };

    // Safety fallback timeout so splash screen NEVER hangs as a blank screen on mobile devices
    const safetyFallbackTimeout = window.setTimeout(finishSplash, 3000);

    const startAnimation = async () => {
      // Ensure custom fonts are loaded before starting
      if (document.fonts && document.fonts.ready) {
        const timeoutPromise = new Promise(resolve => {
          fontWaitTimeout = window.setTimeout(resolve, 800);
        });
        await Promise.race([document.fonts.ready, timeoutPromise]);
      }

      svgImage.onload = () => {
        if (!isFinishedRef.current) {
          animationFrameId = window.requestAnimationFrame(draw);
        }
      };

      svgImage.onerror = () => {
        console.warn('Splash SVG failed to load, completing splash fallback');
        finishSplash();
      };

      svgImage.src = svgUrl;
    };

    startAnimation();

    return () => {
      window.cancelAnimationFrame(animationFrameId);
      window.clearTimeout(completeTimeout);
      window.clearTimeout(fontWaitTimeout);
      window.clearTimeout(safetyFallbackTimeout);
      URL.revokeObjectURL(svgUrl);
    };
  }, []); // Run ONCE on mount

  return (
    <div 
      onClick={finishSplash}
      onTouchStart={finishSplash}
      className={`fixed inset-0 z-[9999] bg-[#13519C] transition-opacity duration-400 select-none cursor-pointer ${isVisible ? 'opacity-100' : 'opacity-0 pointer-events-none'}`}
    >
      <canvas ref={canvasRef} className="h-full w-full" />
      <div ref={svgHostRef} className="hidden" aria-hidden="true">
        <GraduationCapSplash className="h-32 w-32" />
      </div>
    </div>
  );
};

export default SplashScreen;
