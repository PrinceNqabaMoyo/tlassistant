/**
 * Fundile Logo Intro Canvas Renderer & Video Exporter
 * 
 * Handles rendering the animation frames onto a canvas (both for preview
 * and 1080p high-resolution export) and recording the output as a 60fps WebM/MP4.
 */

import { drawConstellationFormation } from './constellationRenderer';

export const FINAL_HOLD_DURATION = 3;

const WEBM_MIME_TYPES = [
  'video/webm;codecs=vp9',
  'video/webm;codecs=vp8',
  'video/webm;codecs=vp9,opus',
  'video/webm;codecs=vp8,opus',
  'video/webm',
];

const MP4_MIME_TYPES = [
  'video/mp4;codecs=avc1.42E01E',
  'video/mp4;codecs=avc1',
  'video/mp4',
];

const getSupportedMimeType = (types) => {
  if (typeof MediaRecorder === 'undefined' || typeof MediaRecorder.isTypeSupported !== 'function') {
    return '';
  }

  for (const type of types) {
    if (MediaRecorder.isTypeSupported(type)) {
      return type;
    }
  }

  return '';
};

export const getVideoExportSupport = () => ({
  webm: Boolean(getSupportedMimeType(WEBM_MIME_TYPES)),
  mp4: Boolean(getSupportedMimeType(MP4_MIME_TYPES)),
});

const resolveExportMimeType = (formatPreference = 'auto') => {
  if (formatPreference === 'mp4') {
    return getSupportedMimeType(MP4_MIME_TYPES);
  }

  if (formatPreference === 'webm') {
    return getSupportedMimeType(WEBM_MIME_TYPES);
  }

  return getSupportedMimeType([...WEBM_MIME_TYPES, ...MP4_MIME_TYPES]);
};

// Initialize a list of particles
export const createParticleSystem = (count, width, height) => {
  const particles = [];
  for (let i = 0; i < count; i++) {
    particles.push({
      x: Math.random() * width,
      y: height + Math.random() * 100,
      size: Math.random() * 3 + 1,
      speedY: Math.random() * 1.5 + 0.5,
      amplitude: Math.random() * 2 + 0.5,
      frequency: Math.random() * 0.02 + 0.005,
      alpha: Math.random() * 0.5 + 0.2,
      phase: Math.random() * Math.PI * 2,
      life: Math.random() * 0.5 + 0.5, // % of screen height
    });
  }
  return particles;
};

// Update particles
export const updateParticles = (particles, width, height, particleSpeed = 1) => {
  particles.forEach(p => {
    p.y -= p.speedY * particleSpeed;
    p.phase += p.frequency;
    p.x += Math.sin(p.phase) * p.amplitude * 0.5;

    // Reset particle if it goes off screen or dies
    if (p.y < height * (1 - p.life) || p.y < -10) {
      p.y = height + Math.random() * 50;
      p.x = Math.random() * width;
      p.alpha = Math.random() * 0.5 + 0.2;
    }
  });
};

/**
 * Render a single frame of the animation
 */
export const renderFrame = (ctx, width, height, time, duration, options, svgImage, particles, svgString = '') => {
  const {
    formationMode = 'pixelate',
    constellationVariant = 'medium',
    pixelIntensity = 24,       // Max pixel block size
    glowIntensity = 20,        // Shadow blur
    accentColor = '#ff9100',    // SVG and glow color
    titleText = 'FUNDILE',
    taglineText = 'Your AI Teaching & Learning Assistant',
    titleFontScale = 100,
    taglineFontScale = 100,
    constellationDensity = 100,
    constellationSpread = 120,
    constellationLineStrength = 55,
    showConstellationRadialGlow = false,
    hideAccentSquares = false,
    bgStyle = 'dark-radial',    // dark-radial, dark-linear, plain-black
  } = options;

  // 1. Draw Background
  ctx.save();
  ctx.shadowColor = 'transparent';
  ctx.shadowBlur = 0;
  
  if (bgStyle === 'plain-black') {
    ctx.fillStyle = '#000000';
    ctx.fillRect(0, 0, width, height);
  } else if (bgStyle === 'original-blue') {
    // Beautiful cinematic original blue gradient using brand color #13519C
    const grad = ctx.createRadialGradient(
      width / 2, height / 2, 50,
      width / 2, height / 2, Math.max(width, height) * 0.7
    );
    grad.addColorStop(0, '#1c6fcb'); // bright center glow
    grad.addColorStop(0.6, '#13519C'); // main brand blue
    grad.addColorStop(1, '#0a3468'); // dark edge contrast
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, width, height);
  } else if (bgStyle === 'dark-linear') {
    const grad = ctx.createLinearGradient(0, 0, 0, height);
    grad.addColorStop(0, '#070a13');
    grad.addColorStop(1, '#111827');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, width, height);
  } else {
    // Elegant Dark Radial Gradient with soft center glow
    const grad = ctx.createRadialGradient(
      width / 2, height / 2, 50,
      width / 2, height / 2, Math.max(width, height) * 0.7
    );
    
    // Ambient back-glow intensity based on time
    let glowAlpha = 0.05;
    if (time > 1.0 && time <= 3.0) {
      glowAlpha = 0.05 + ((time - 1.0) / 2.0) * 0.12; // ramp up
    } else if (time > 3.0) {
      glowAlpha = 0.17;
    }
    
    grad.addColorStop(0, `rgba(255, 145, 0, ${glowAlpha})`); // soft orange center glow
    grad.addColorStop(0.4, '#080c16');
    grad.addColorStop(1, '#020408');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, width, height);
  }
  ctx.restore();

  // 2. Draw Floating Gold Dust Particles
  if (particles && particles.length > 0) {
    ctx.save();
    // Particles fade in gradually in Phase 2
    let particleAlphaMultiplier = 0;
    if (time > 1.0 && time <= 2.5) {
      particleAlphaMultiplier = (time - 1.0) / 1.5;
    } else if (time > 2.5) {
      particleAlphaMultiplier = 1.0;
    }

    particles.forEach(p => {
      const alpha = p.alpha * particleAlphaMultiplier;
      if (alpha > 0) {
        ctx.fillStyle = `rgba(255, 183, 77, ${alpha})`;
        ctx.shadowColor = 'rgba(255, 145, 0, 0.4)';
        ctx.shadowBlur = 4;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
        ctx.fill();
      }
    });
    ctx.restore();
  }

  // 3. Draw Logo with Pixelation Effect
  if (svgImage && svgImage.complete) {
    ctx.save();

    // Logo size and positioning
    // Logo is 1024x800. We want it centered.
    // Scales: starts smaller and expands slightly (cinematic zoom)
    const startScale = 0.38;
    const endScale = 0.42;
    let currentScale = startScale;
    
    if (time <= 3.5) {
      // smooth zoom-in over animation
      currentScale = startScale + (time / 3.5) * (endScale - startScale);
    } else {
      currentScale = endScale;
    }

    const svgOriginalWidth = 1024;
    const svgOriginalHeight = 800;
    const logoW = svgOriginalWidth * currentScale;
    const logoH = svgOriginalHeight * currentScale;
    
    // Logo position: centered horizontally, shifted up slightly to make room for text
    const logoX = (width - logoW) / 2;
    const isPortrait = height > width;
    const logoY = (height - logoH) / 2 - (isPortrait ? 100 : 60);

    // Logo opacity fade-in
    let logoOpacity = 0;
    if (time <= 1.2) {
      logoOpacity = time / 1.2;
    } else {
      logoOpacity = 1.0;
    }

    // Determine current pixel size (solidification curve)
    // 0.0s - 1.0s: locked at maximum pixel blockiness
    // 1.0s - 3.2s: smoothly drops down to 1.0px (solid logo)
    // 3.2s - 5.0s: locked at 1.0px (completely solid vector)
    let currentPixelSize = pixelIntensity;
    if (time > 1.0 && time <= 3.2) {
      const progress = (time - 1.0) / 2.2; // 0 to 1
      // Use cubic easing out for rapid solidification near the end
      const ease = 1 - Math.pow(1 - progress, 3);
      currentPixelSize = pixelIntensity - (ease * (pixelIntensity - 1));
    } else if (time > 3.2) {
      currentPixelSize = 1;
    }

    if (formationMode === 'constellation') {
      drawConstellationFormation({
        ctx,
        width,
        height,
        time,
        duration,
        accentColor,
        bgStyle,
        glowIntensity,
        constellationDensity,
        constellationSpread,
        constellationLineStrength,
        showConstellationRadialGlow,
        constellationVariant,
        svgImage,
        svgString,
        logoOpacity,
        logoX,
        logoY,
        logoW,
        logoH,
      });
    } else {
      ctx.globalAlpha = logoOpacity;

      if (currentPixelSize > 1.5) {
        // Draw pixelated using offscreen scale down / scale up method
        const offscreenCanvas = document.createElement('canvas');
        const offCtx = offscreenCanvas.getContext('2d');
        
        const pixelSize = Math.round(currentPixelSize);
        offscreenCanvas.width = Math.max(10, Math.round(width / pixelSize));
        offscreenCanvas.height = Math.max(10, Math.round(height / pixelSize));

        // Draw SVG at scaled down position on offscreen
        offCtx.save();
        offCtx.scale(1 / pixelSize, 1 / pixelSize);
        
        // Draw ambient orange drop shadow for logo inside offscreen
        offCtx.shadowColor = accentColor;
        offCtx.shadowBlur = glowIntensity * 0.5;
        
        offCtx.drawImage(svgImage, logoX, logoY, logoW, logoH);
        offCtx.restore();

        // Render pixelated blocks back onto main canvas
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(offscreenCanvas, 0, 0, width, height);
      } else {
        // Solid rendering: Apply elegant glow/drop shadow directly
        ctx.shadowColor = accentColor;
        // Glow pulse
        const glowPulse = Math.sin(time * 2) * 5 + glowIntensity;
        ctx.shadowBlur = glowPulse;
        ctx.drawImage(svgImage, logoX, logoY, logoW, logoH);
      }
    }
    ctx.restore();
  }

  // 4. Draw Typography (FUNDILE & TAGLINE)
  // Phase 3: t >= 2.5s
  if (time >= 2.2) {
    ctx.save();

    // Calculate text fade in
    let textOpacity = 0;
    let textOffsetY = 20; // slide up effect
    
    if (time > 2.2 && time <= 3.5) {
      const progress = (time - 2.2) / 1.3;
      textOpacity = progress;
      textOffsetY = 20 * (1 - progress);
    } else if (time > 3.5) {
      textOpacity = 1.0;
      textOffsetY = 0;
    }

    ctx.globalAlpha = textOpacity;

    // Draw Main Title: "fundile" (Afacad font, solid white)
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    
    // Responsive/scaled font size, constrained by width for mobile portrait screens
    const scaleBase = Math.min(width * 1.2, height);
    const titleSize = Math.round((scaleBase * 0.08) * (titleFontScale / 100)); // 86px at 1080p base
    ctx.font = `700 ${titleSize}px Afacad, sans-serif`;
    
    const titleX = width / 2;
    // Position title relative to logo bottom to prevent overlap completely
    const isPortrait = height > width;
    const titleY = (height / 2 - (isPortrait ? 100 : 60)) + ((800 * (isPortrait ? 0.38 : 0.42)) / 2) + (isPortrait ? 60 : 80) + textOffsetY;
    
    ctx.fillStyle = '#ffffff'; // Pristine solid white title
    
    // Custom adaptive glow shadow for text
    ctx.shadowColor = bgStyle === 'original-blue' ? 'rgba(255, 255, 255, 0.3)' : 'rgba(255, 145, 0, 0.4)';
    ctx.shadowBlur = glowIntensity;
    
    ctx.fillText(titleText, titleX, titleY, width * 0.9);

    // Draw Tagline
    // Delays slightly after title
    let taglineOpacity = 0;
    if (time > 2.8 && time <= 4.0) {
      taglineOpacity = (time - 2.8) / 1.2;
    } else if (time > 4.0) {
      taglineOpacity = 1.0;
    }

    if (taglineOpacity > 0) {
      ctx.globalAlpha = taglineOpacity;
      ctx.shadowBlur = 0; // remove heavy glow for small text readability
      
      const taglineSize = Math.round((scaleBase * 0.026) * (taglineFontScale / 100)); // 28px at 1080p base
      ctx.font = `400 ${taglineSize}px 'Plus Jakarta Sans', system-ui, sans-serif`;
      
      // Sleek silver/slate color
      ctx.fillStyle = '#94a3b8';
      ctx.letterSpacing = '2px'; // works in modern canvas contexts
      
      const taglineY = titleY + titleSize * 0.7 + 10;
      ctx.fillText(taglineText, titleX, taglineY, width * 0.9);
    }

    ctx.restore();
  }
};

/**
 * Capture canvas frames and compile into a high-res .webm/mp4 video download
 */
export const startVideoRender = async (options, svgString, onProgress, onComplete) => {
  const width = 1920;
  const height = 1080;
  const fps = 60;
  const duration = options.duration || 5.0; // seconds
  const totalDuration = duration + FINAL_HOLD_DURATION;
  const totalFrames = totalDuration * fps;
  const formatPreference = options.exportFormat || 'auto';
  
  // 1. Create offline canvas
  const canvas = document.createElement('canvas');
  canvas.width = width;
  canvas.height = height;
  const ctx = canvas.getContext('2d');
  
  // 2. Prepare SVG Image object
  const svgBlob = new Blob([svgString], { type: 'image/svg+xml;charset=utf-8' });
  const url = URL.createObjectURL(svgBlob);
  const svgImage = new Image();
  
  await new Promise((resolve, reject) => {
    svgImage.onload = resolve;
    svgImage.onerror = reject;
    svgImage.src = url;
  });

  // 3. Initialize Particles
  const particles = createParticleSystem(options.particleCount || 40, width, height);

  // 4. Capture Canvas Stream
  // Capture stream at the target frame rate
  const stream = canvas.captureStream(fps);
  
  let selectedType = resolveExportMimeType(formatPreference);
  
  if (!selectedType) {
    if (formatPreference === 'mp4') {
      throw new Error('MP4 export is not supported in this browser. Please switch to Auto or WebM.');
    }

    if (formatPreference === 'webm') {
      throw new Error('WebM export is not supported in this browser. Please switch to Auto or MP4.');
    }

    throw new Error('No supported MediaRecorder video formats found in your browser.');
  }

  const chunks = [];
  const recorder = new MediaRecorder(stream, {
    mimeType: selectedType,
    videoBitsPerSecond: 12 * 1024 * 1024 // 12 Mbps for stellar 1080p quality
  });

  recorder.ondataavailable = (e) => {
    if (e.data && e.data.size > 0) {
      chunks.push(e.data);
    }
  };

  recorder.onstop = () => {
    const blob = new Blob(chunks, { type: selectedType.split(';')[0] });
    const videoUrl = URL.createObjectURL(blob);
    URL.revokeObjectURL(url); // clean up
    onComplete(videoUrl, selectedType.includes('mp4') ? 'mp4' : 'webm');
  };

  // Start recording
  recorder.start();

  // Render each frame sequentially with perfect timing
  let frameIndex = 0;
  
  const recordInterval = 1000 / fps;
  
  return new Promise((resolve) => {
    const runFrameRender = () => {
      if (frameIndex < totalFrames) {
        const time = frameIndex * (1 / fps);
        const renderTime = Math.min(time, duration);
        
        // Update particles
        if (time < duration) {
          updateParticles(particles, width, height, options.particleSpeed || 1);
        }
        
        // Render
        renderFrame(ctx, width, height, renderTime, duration, options, svgImage, particles, svgString);
        
        // Report progress
        const percent = Math.round((frameIndex / totalFrames) * 100);
        onProgress(percent);
        
        frameIndex++;
        // Use setTimeout to ensure MediaRecorder's encoder keeps up with drawing
        setTimeout(runFrameRender, recordInterval);
      } else {
        // Stop recording
        setTimeout(() => {
          recorder.stop();
          resolve();
        }, 300);
      }
    };

    // Kick off rendering sequence
    runFrameRender();
  });
};
