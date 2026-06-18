import React, { useEffect, useRef, useState } from 'react';
import GraduationCapSplash from './GraduationCapSplash';
import { renderFrame, FINAL_HOLD_DURATION } from '../../../logo-video-generator/src/canvasExporter';

const splashOptions = {
  duration: 6.0,
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

  useEffect(() => {
    const canvas = canvasRef.current;
    const svgElement = svgHostRef.current?.querySelector('svg');

    if (!canvas || !svgElement) {
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

    const finishSplash = () => {
      setIsVisible(false);
      completeTimeout = window.setTimeout(() => {
        onComplete();
      }, 500);
    };

    const draw = (timestamp) => {
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

    let fontWaitTimeout;
    
    const startAnimation = async () => {
      // Ensure custom fonts (like Afacad) are fully loaded before rendering the canvas
      if (document.fonts && document.fonts.ready) {
        // Fallback timeout in case font loading hangs
        const timeoutPromise = new Promise(resolve => {
          fontWaitTimeout = window.setTimeout(resolve, 1000);
        });
        await Promise.race([document.fonts.ready, timeoutPromise]);
      }

      svgImage.onload = () => {
        animationFrameId = window.requestAnimationFrame(draw);
      };

      svgImage.src = svgUrl;
    };

    startAnimation();

    return () => {
      window.cancelAnimationFrame(animationFrameId);
      window.clearTimeout(completeTimeout);
      window.clearTimeout(fontWaitTimeout);
      URL.revokeObjectURL(svgUrl);
    };
  }, [onComplete]);

  return (
    <div className={`fixed inset-0 z-[9999] bg-[#13519C] transition-opacity duration-500 ${isVisible ? 'opacity-100' : 'opacity-0'}`}>
      <canvas ref={canvasRef} className="h-full w-full" />
      <div ref={svgHostRef} className="hidden" aria-hidden="true">
        <GraduationCapSplash className="h-32 w-32" />
      </div>
    </div>
  );
};

export default SplashScreen;
