const constellationPointCache = new WeakMap();
const svgContourPointCache = new Map();

const clamp = (value, min, max) => Math.min(Math.max(value, min), max);

const mix = (start, end, progress) => start + ((end - start) * progress);

const easeOutCubic = (value) => 1 - Math.pow(1 - clamp(value, 0, 1), 3);

const easeInOutCubic = (value) => {
  const clamped = clamp(value, 0, 1);
  return clamped < 0.5
    ? 4 * clamped * clamped * clamped
    : 1 - Math.pow(-2 * clamped + 2, 3) / 2;
};

const hashValue = (seed) => {
  const raw = Math.sin(seed * 12.9898) * 43758.5453123;
  return raw - Math.floor(raw);
};

const colorWithAlpha = (color, alpha) => {
  if (typeof color === 'string' && color.startsWith('#')) {
    let normalized = color.slice(1);

    if (normalized.length === 3) {
      normalized = normalized.split('').map((char) => char + char).join('');
    }

    if (normalized.length === 6) {
      const red = parseInt(normalized.slice(0, 2), 16);
      const green = parseInt(normalized.slice(2, 4), 16);
      const blue = parseInt(normalized.slice(4, 6), 16);
      return `rgba(${red}, ${green}, ${blue}, ${alpha})`;
    }
  }

  return `rgba(255, 145, 0, ${alpha})`;
};

const getSvgContourTargets = ({ svgString, density, logoX, logoY, logoW, logoH }) => {
  if (!svgString || typeof DOMParser === 'undefined') {
    return [];
  }

  const cacheKey = `${density}:${svgString}`;

  if (!svgContourPointCache.has(cacheKey)) {
    try {
      const parser = new DOMParser();
      const svgDocument = parser.parseFromString(svgString, 'image/svg+xml');
      const svgElement = svgDocument.querySelector('svg');

      if (!svgElement) {
        return [];
      }

      const viewBox = (svgElement.getAttribute('viewBox') || '0 0 1024 800')
        .split(/\s+/)
        .map(Number);
      const viewBoxWidth = viewBox[2] || 1024;
      const viewBoxHeight = viewBox[3] || 800;
      const densityMultiplier = Math.max(density, 1) / 100;
      const sampleSpacing = Math.max(10, 18 / densityMultiplier);
      const contourTargets = [];

      svgDocument.querySelectorAll('path').forEach((path, pathIndex) => {
        if (typeof path.getTotalLength !== 'function') {
          return;
        }

        const totalLength = path.getTotalLength();

        if (!Number.isFinite(totalLength) || totalLength <= 0) {
          return;
        }

        const segmentCount = Math.max(12, Math.ceil(totalLength / sampleSpacing));

        for (let step = 0; step <= segmentCount; step += 1) {
          const length = (step / segmentCount) * totalLength;
          const point = path.getPointAtLength(length);
          const previousPoint = path.getPointAtLength(Math.max(0, length - 1));
          const nextPoint = path.getPointAtLength(Math.min(totalLength, length + 1));

          contourTargets.push({
            normalizedX: point.x / viewBoxWidth,
            normalizedY: point.y / viewBoxHeight,
            tangentX: nextPoint.x - previousPoint.x,
            tangentY: nextPoint.y - previousPoint.y,
            kind: 'contour',
            clusterSeed: pathIndex,
          });
        }
      });

      svgContourPointCache.set(cacheKey, contourTargets);
    } catch {
      svgContourPointCache.set(cacheKey, []);
    }
  }

  return svgContourPointCache.get(cacheKey).map((point) => ({
    ...point,
    x: logoX + (point.normalizedX * logoW),
    y: logoY + (point.normalizedY * logoH),
  }));
};

const getRasterTargets = ({ svgImage, width, height, logoX, logoY, logoW, logoH, density }) => {
  let imageCache = constellationPointCache.get(svgImage);

  if (!imageCache) {
    imageCache = new Map();
    constellationPointCache.set(svgImage, imageCache);
  }

  const densityMultiplier = Math.max(density, 1) / 100;
  const sampleStep = Math.max(6, Math.round(12 / densityMultiplier));
  const cacheKey = [
    width,
    height,
    Math.round(logoX),
    Math.round(logoY),
    Math.round(logoW),
    Math.round(logoH),
    sampleStep,
  ].join(':');

  if (imageCache.has(cacheKey)) {
    return imageCache.get(cacheKey);
  }

  const offscreenCanvas = document.createElement('canvas');
  offscreenCanvas.width = width;
  offscreenCanvas.height = height;
  const offscreenContext = offscreenCanvas.getContext('2d');

  if (!offscreenContext) {
    return [{ x: logoX + (logoW / 2), y: logoY + (logoH / 2) }];
  }

  offscreenContext.clearRect(0, 0, width, height);
  offscreenContext.drawImage(svgImage, logoX, logoY, logoW, logoH);

  const imageData = offscreenContext.getImageData(0, 0, width, height).data;
  const targets = [];
  const startX = Math.max(0, Math.floor(logoX));
  const endX = Math.min(width, Math.ceil(logoX + logoW));
  const startY = Math.max(0, Math.floor(logoY));
  const endY = Math.min(height, Math.ceil(logoY + logoH));

  for (let y = startY; y < endY; y += sampleStep) {
    for (let x = startX; x < endX; x += sampleStep) {
      const alphaIndex = ((y * width) + x) * 4 + 3;

      if (imageData[alphaIndex] > 32) {
        targets.push({ x, y });
      }
    }
  }

  if (targets.length === 0) {
    targets.push({ x: logoX + (logoW / 2), y: logoY + (logoH / 2) });
  }

  imageCache.set(cacheKey, targets);
  return targets;
};

const getConstellationTargets = ({ svgImage, svgString, width, height, logoX, logoY, logoW, logoH, density }) => {
  const contourTargets = getSvgContourTargets({
    svgString,
    density,
    logoX,
    logoY,
    logoW,
    logoH,
  });
  const fillTargets = getRasterTargets({
    svgImage,
    width,
    height,
    logoX,
    logoY,
    logoW,
    logoH,
    density: Math.max(60, density * 0.82),
  }).map((point, index) => ({
    ...point,
    normalizedX: clamp((point.x - logoX) / Math.max(logoW, 1), 0, 1),
    normalizedY: clamp((point.y - logoY) / Math.max(logoH, 1), 0, 1),
    tangentX: 0,
    tangentY: 0,
    kind: 'fill',
    clusterSeed: index % 7,
  }));

  if (contourTargets.length > 0) {
    const fillStride = contourTargets.length > 400 ? 3 : 2;
    return [
      ...contourTargets,
      ...fillTargets.filter((_, index) => index % fillStride === 0),
    ];
  }

  if (fillTargets.length > 0) {
    return fillTargets;
  }

  return [{
    x: logoX + (logoW / 2),
    y: logoY + (logoH / 2),
    normalizedX: 0.5,
    normalizedY: 0.5,
    tangentX: 0,
    tangentY: 0,
    kind: 'fill',
    clusterSeed: 0,
  }];
};

const drawMediumConstellationFormation = ({
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
  svgImage,
  logoOpacity,
  logoX,
  logoY,
  logoW,
  logoH,
}) => {
  const targets = getRasterTargets({
    svgImage,
    width,
    height,
    logoX,
    logoY,
    logoW,
    logoH,
    density: constellationDensity,
  });

  const gatherStart = duration * 0.08;
  const gatherEnd = duration * 0.62;
  const revealStart = duration * 0.46;
  const revealEnd = duration * 0.78;
  const gatherProgress = clamp((time - gatherStart) / Math.max(gatherEnd - gatherStart, 0.001), 0, 1);
  const easedGather = easeInOutCubic(gatherProgress);
  const revealProgress = clamp((time - revealStart) / Math.max(revealEnd - revealStart, 0.001), 0, 1);
  const easedReveal = easeOutCubic(revealProgress);
  const starFadeStart = duration * 0.58;
  const starFadeEnd = duration * 0.8;
  const starFadeProgress = clamp((time - starFadeStart) / Math.max(starFadeEnd - starFadeStart, 0.001), 0, 1);
  const starVisibility = 1 - easeOutCubic(starFadeProgress);
  const lineStrength = constellationLineStrength / 100;
  const spreadMultiplier = constellationSpread / 100;
  const centerX = width / 2;
  const centerY = (height / 2) - 30;
  const baseRadius = Math.max(logoW, logoH) * (0.9 + (spreadMultiplier * 0.55));
  const driftRadius = baseRadius * Math.pow(1 - easedGather, 1.15);
  const lineReveal = easeOutCubic(clamp((gatherProgress - 0.18) / 0.55, 0, 1));
  const points = new Array(targets.length);

  ctx.save();

  for (let index = 0; index < targets.length; index += 1) {
    const target = targets[index];
    const angle = (index * 2.399963229728653) + (hashValue(index + 19) * Math.PI * 2);
    const radial = baseRadius * (0.62 + (hashValue(index + 37) * 0.68));
    const skewX = (hashValue(index + 71) - 0.5) * width * 0.18 * spreadMultiplier;
    const skewY = (hashValue(index + 97) - 0.5) * height * 0.16 * spreadMultiplier;
    const startX = centerX + (Math.cos(angle) * radial) + skewX;
    const startY = centerY + (Math.sin(angle) * radial * 0.72) + skewY;
    const orbitX = Math.cos(angle + (time * 1.6)) * driftRadius * (0.08 + (hashValue(index + 11) * 0.14));
    const orbitY = Math.sin((angle * 1.2) + (time * 1.45)) * driftRadius * (0.06 + (hashValue(index + 23) * 0.12));
    const x = mix(startX, target.x, easedGather) + orbitX;
    const y = mix(startY, target.y, easedGather) + orbitY;
    const radius = ((1.1 + (hashValue(index + 53) * 1.5)) * (0.9 + (easedGather * 0.22))) * (0.75 + (starVisibility * 0.25));
    const alpha = clamp((0.22 + (easedGather * 0.65) + (revealProgress * 0.12)) * (0.82 + (hashValue(index + 89) * 0.28)) * logoOpacity * starVisibility, 0, 1);

    points[index] = { x, y, radius, alpha };
  }

  if (lineStrength > 0 && starVisibility > 0.01) {
    const maxLineDistance = 18 + (lineStrength * 44);

    ctx.lineWidth = 1;
    for (let index = 0; index < points.length; index += 1) {
      const point = points[index];
      const candidateIndexes = [index + 1, index + 3, index + 7];

      for (let candidatePointer = 0; candidatePointer < candidateIndexes.length; candidatePointer += 1) {
        const candidate = points[candidateIndexes[candidatePointer]];

        if (!candidate) {
          continue;
        }

        const deltaX = candidate.x - point.x;
        const deltaY = candidate.y - point.y;
        const distance = Math.hypot(deltaX, deltaY);

        if (distance > maxLineDistance) {
          continue;
        }

        const alpha = ((1 - (distance / maxLineDistance)) * 0.34 * lineStrength * lineReveal * logoOpacity * starVisibility) * (1 - (easedReveal * 0.25));

        if (alpha <= 0.01) {
          continue;
        }

        ctx.strokeStyle = colorWithAlpha(accentColor, alpha);
        ctx.beginPath();
        ctx.moveTo(point.x, point.y);
        ctx.lineTo(candidate.x, candidate.y);
        ctx.stroke();
      }
    }
  }

  ctx.shadowColor = colorWithAlpha(accentColor, 0.8);
  ctx.shadowBlur = glowIntensity * (0.4 + (easedGather * 0.35)) * starVisibility;

  for (let index = 0; index < points.length; index += 1) {
    const point = points[index];

    if (point.alpha <= 0.01 || point.radius <= 0.01) {
      continue;
    }

    ctx.fillStyle = colorWithAlpha('#ffffff', point.alpha * (0.95 - (easedReveal * 0.2)));
    ctx.beginPath();
    ctx.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = colorWithAlpha(accentColor, point.alpha * 0.4);
    ctx.beginPath();
    ctx.arc(point.x, point.y, Math.max(0.65, point.radius * 0.45), 0, Math.PI * 2);
    ctx.fill();
  }

  if (easedReveal > 0) {
    ctx.globalAlpha = easedReveal * 0.92 * logoOpacity;
    ctx.shadowColor = accentColor;
    ctx.shadowBlur = glowIntensity * (0.75 + (easedReveal * 0.45));
    ctx.drawImage(svgImage, logoX, logoY, logoW, logoH);
  }

  if (bgStyle === 'original-blue' && showConstellationRadialGlow) {
    ctx.globalCompositeOperation = 'screen';
    ctx.globalAlpha = 0.12 * (1 - (easedReveal * 0.35)) * logoOpacity;
    ctx.fillStyle = colorWithAlpha('#ffffff', 0.3);
    ctx.beginPath();
    ctx.arc(centerX, centerY + 18, baseRadius * 0.65, 0, Math.PI * 2);
    ctx.fill();
  }

  ctx.restore();
};

export const drawConstellationFormation = ({
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
}) => {
  if (constellationVariant !== 'premium') {
    drawMediumConstellationFormation({
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
      svgImage,
      logoOpacity,
      logoX,
      logoY,
      logoW,
      logoH,
    });
    return;
  }

  const targets = getConstellationTargets({
    svgImage,
    svgString,
    width,
    height,
    logoX,
    logoY,
    logoW,
    logoH,
    density: constellationDensity,
  });

  const gatherStart = duration * 0.08;
  const gatherEnd = duration * 0.62;
  const revealStart = duration * 0.46;
  const revealEnd = duration * 0.78;
  const gatherProgress = clamp((time - gatherStart) / Math.max(gatherEnd - gatherStart, 0.001), 0, 1);
  const easedGather = easeInOutCubic(gatherProgress);
  const revealProgress = clamp((time - revealStart) / Math.max(revealEnd - revealStart, 0.001), 0, 1);
  const easedReveal = easeOutCubic(revealProgress);
  const starFadeStart = duration * 0.58;
  const starFadeEnd = duration * 0.8;
  const starFadeProgress = clamp((time - starFadeStart) / Math.max(starFadeEnd - starFadeStart, 0.001), 0, 1);
  const starVisibility = 1 - easeOutCubic(starFadeProgress);
  const lineStrength = constellationLineStrength / 100;
  const spreadMultiplier = constellationSpread / 100;
  const centerX = width / 2;
  const centerY = (height / 2) - 30;
  const baseRadius = Math.max(logoW, logoH) * (0.9 + (spreadMultiplier * 0.55));
  const driftRadius = baseRadius * Math.pow(1 - easedGather, 1.15);
  const lineReveal = easeOutCubic(clamp((gatherProgress - 0.18) / 0.55, 0, 1));
  const points = new Array(targets.length);
  const launchZones = [
    { x: width * 0.18, y: height * 0.26 },
    { x: width * 0.82, y: height * 0.24 },
    { x: width * 0.52, y: height * 0.84 },
    { x: width * 0.14, y: height * 0.7 },
  ];
  const globalParallaxX = Math.sin(time * 0.55) * 6 * (1 - (easedReveal * 0.85));
  const globalParallaxY = Math.cos(time * 0.48) * 4 * (1 - (easedReveal * 0.85));

  ctx.save();

  for (let index = 0; index < targets.length; index += 1) {
    const target = targets[index];
    const depth = 0.72 + (hashValue(index + 7) * 0.9);
    const groupIndex = Math.floor((((target.normalizedX * 1.8) + (target.normalizedY * 1.2) + (hashValue(index + target.clusterSeed + 29) * 0.6)) % 1) * launchZones.length);
    const launchZone = launchZones[groupIndex];
    const angle = (index * 2.399963229728653) + (hashValue(index + 19) * Math.PI * 2);
    const radial = baseRadius * (0.28 + (depth * 0.38) + (hashValue(index + 37) * 0.22));
    const skewX = (hashValue(index + 71) - 0.5) * width * 0.1 * spreadMultiplier;
    const skewY = (hashValue(index + 97) - 0.5) * height * 0.1 * spreadMultiplier;
    const startX = launchZone.x + (Math.cos(angle) * radial * 0.42) + skewX;
    const startY = launchZone.y + (Math.sin(angle * 1.08) * radial * 0.32) + skewY;
    const delay = clamp(
      (target.kind === 'contour' ? 0.02 : 0.11)
      + (Math.abs(target.normalizedX - 0.5) * 0.18)
      + ((1 - target.normalizedY) * 0.1)
      + (groupIndex * 0.045)
      + (hashValue(index + 131) * 0.08),
      0,
      0.78,
    );
    const phaseSpan = 0.28 + (depth * 0.16);
    const pointProgress = easeInOutCubic(clamp((gatherProgress - delay) / phaseSpan, 0, 1));
    const settleProgress = easeOutCubic(clamp((pointProgress - 0.72) / 0.28, 0, 1));
    const normalXRaw = target.kind === 'contour' ? target.tangentY : (target.x - centerX);
    const normalYRaw = target.kind === 'contour' ? -target.tangentX : (target.y - centerY);
    const normalLength = Math.hypot(normalXRaw, normalYRaw) || 1;
    const normalX = normalXRaw / normalLength;
    const normalY = normalYRaw / normalLength;
    const overshootDistance = (target.kind === 'contour' ? 12 : 7) * (0.65 + (depth * 0.35)) * (1 - settleProgress);
    const orbitStrength = (1 - pointProgress) * (0.2 + (depth * 0.08));
    const orbitX = Math.cos(angle + (time * (1.1 + (depth * 0.25)))) * driftRadius * orbitStrength;
    const orbitY = Math.sin((angle * 1.18) + (time * (1.02 + (depth * 0.22)))) * driftRadius * orbitStrength * 0.82;
    const parallaxX = globalParallaxX * (depth - 0.7);
    const parallaxY = globalParallaxY * (depth - 0.7);
    const arrivalX = mix(startX, target.x + (normalX * overshootDistance), pointProgress) + orbitX + parallaxX;
    const arrivalY = mix(startY, target.y + (normalY * overshootDistance), pointProgress) + orbitY + parallaxY;
    const x = mix(arrivalX, target.x, settleProgress);
    const y = mix(arrivalY, target.y, settleProgress);
    const radiusBase = target.kind === 'contour' ? 1.15 : 0.9;
    const radius = ((radiusBase + (hashValue(index + 53) * 1.25)) * (0.72 + (depth * 0.36)) * (0.75 + (starVisibility * 0.25))) * (0.82 + (pointProgress * 0.2));
    const alphaBase = target.kind === 'contour' ? 0.26 : 0.18;
    const alpha = clamp((alphaBase + (pointProgress * 0.58) + (revealProgress * 0.08)) * (0.82 + (hashValue(index + 89) * 0.25)) * logoOpacity * starVisibility, 0, 1);

    points[index] = { x, y, radius, alpha, depth, groupIndex };
  }

  if (lineStrength > 0 && starVisibility > 0.01) {
    const maxLineDistance = 18 + (lineStrength * 44);

    ctx.lineWidth = 1;
    for (let index = 0; index < points.length; index += 1) {
      const point = points[index];
      const candidateIndexes = [index + 1, index + 3, index + 7];

      for (let candidatePointer = 0; candidatePointer < candidateIndexes.length; candidatePointer += 1) {
        const candidate = points[candidateIndexes[candidatePointer]];

        if (!candidate) {
          continue;
        }

        const deltaX = candidate.x - point.x;
        const deltaY = candidate.y - point.y;
        const distance = Math.hypot(deltaX, deltaY);

        if (distance > maxLineDistance) {
          continue;
        }

        const sharedGroupBoost = candidate.groupIndex === point.groupIndex ? 1 : 0.55;
        const alpha = ((1 - (distance / maxLineDistance)) * 0.34 * lineStrength * lineReveal * logoOpacity * starVisibility * sharedGroupBoost) * (1 - (easedReveal * 0.25));

        if (alpha <= 0.01) {
          continue;
        }

        ctx.strokeStyle = colorWithAlpha(accentColor, alpha);
        ctx.beginPath();
        ctx.moveTo(point.x, point.y);
        ctx.lineTo(candidate.x, candidate.y);
        ctx.stroke();
      }
    }
  }

  ctx.shadowColor = colorWithAlpha(accentColor, 0.8);
  ctx.shadowBlur = glowIntensity * (0.4 + (easedGather * 0.35)) * starVisibility;

  for (let index = 0; index < points.length; index += 1) {
    const point = points[index];

    if (point.alpha <= 0.01 || point.radius <= 0.01) {
      continue;
    }

    ctx.fillStyle = colorWithAlpha('#ffffff', point.alpha * (0.95 - (easedReveal * 0.2)));
    ctx.beginPath();
    ctx.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
    ctx.fill();

    ctx.fillStyle = colorWithAlpha(accentColor, point.alpha * 0.4);
    ctx.beginPath();
    ctx.arc(point.x, point.y, Math.max(0.65, point.radius * 0.45), 0, Math.PI * 2);
    ctx.fill();
  }

  if (easedReveal > 0) {
    ctx.globalAlpha = easedReveal * 0.92 * logoOpacity;
    ctx.shadowColor = accentColor;
    ctx.shadowBlur = glowIntensity * (0.75 + (easedReveal * 0.45));
    ctx.drawImage(svgImage, logoX, logoY, logoW, logoH);
  }

  if (bgStyle === 'original-blue' && showConstellationRadialGlow) {
    ctx.globalCompositeOperation = 'screen';
    ctx.globalAlpha = 0.12 * (1 - (easedReveal * 0.35)) * logoOpacity;
    ctx.fillStyle = colorWithAlpha('#ffffff', 0.3);
    ctx.beginPath();
    ctx.arc(centerX, centerY + 18, baseRadius * 0.65, 0, Math.PI * 2);
    ctx.fill();
  }

  ctx.restore();
};
