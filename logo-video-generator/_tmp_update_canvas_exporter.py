from pathlib import Path

root = Path(r"C:\Users\princ\fundile-tlassistant-vite\logo-video-generator")
canvas_exporter_path = root / "src" / "canvasExporter.js"
accidental_file_path = root / "1.5)"

text = canvas_exporter_path.read_text(encoding="utf-8")

import_line = "import { drawConstellationFormation } from './constellationRenderer';\n\n"
comment_marker = " */\n\n"
comment_index = text.find(comment_marker)
if comment_index == -1:
    raise RuntimeError("Comment marker not found in canvasExporter.js")
if import_line not in text:
    text = text[:comment_index + len(comment_marker)] + import_line + text[comment_index + len(comment_marker):]

old_destructure = """    pixelIntensity = 24,       // Max pixel block size
    glowIntensity = 20,        // Shadow blur
    accentColor = '#ff9100',    // SVG and glow color
    titleText = 'FUNDILE',
    taglineText = 'Your AI Teaching & Learning Assistant',
    titleFontScale = 100,
    taglineFontScale = 100,
    hideAccentSquares = false,
    bgStyle = 'dark-radial',    // dark-radial, dark-linear, plain-black"""
new_destructure = """    formationMode = 'pixelate',
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
    hideAccentSquares = false,
    bgStyle = 'dark-radial',    // dark-radial, dark-linear, plain-black"""
if old_destructure not in text:
    raise RuntimeError("Destructure block not found in canvasExporter.js")
text = text.replace(old_destructure, new_destructure, 1)

start_marker = "    ctx.globalAlpha = logoOpacity;\n"
start_index = text.find(start_marker)
if start_index == -1:
    raise RuntimeError("Logo render start block not found in canvasExporter.js")
end_marker = "    ctx.restore();\n"
end_index = text.find(end_marker, start_index)
if end_index == -1:
    raise RuntimeError("Logo render end block not found in canvasExporter.js")

replacement_block = """    if (formationMode === 'constellation') {
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
        svgImage,
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
"""

text = text[:start_index] + replacement_block + text[end_index:]
canvas_exporter_path.write_text(text, encoding="utf-8")

if accidental_file_path.exists():
    accidental_file_path.unlink()
