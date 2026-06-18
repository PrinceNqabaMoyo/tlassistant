# Math Component Thumbnails

This directory contains thumbnail components for mathematical visual aids that appear in the sidebar of the freeform workspace.

## How Thumbnails Work

Thumbnails are small canvas-based previews of mathematical components that show the default state of each component. They help users quickly identify what each visual aid does before selecting it.

## Current Thumbnails

- **LinearFunctionGraphThumbnail**: Shows y=2x+3 with intercepts
- **QuadraticGraphThumbnail**: Shows y=x²-4 with roots and vertex
- **CoordinatePlaneThumbnail**: Shows a coordinate grid with example points

## Adding a New Thumbnail

To add a thumbnail for a new math component:

1. **Create the thumbnail component** in `src/components/math/`:
   ```jsx
   // ExampleComponentThumbnail.jsx
   import React, { useEffect, useRef } from 'react';
   
   const ExampleComponentThumbnail = ({ width = 120, height = 80 }) => {
       const canvasRef = useRef(null);
       
       useEffect(() => {
           const canvas = canvasRef.current;
           if (!canvas) return;
           
           const ctx = canvas.getContext('2d');
           if (!ctx) return;
           
           // Set canvas size
           canvas.width = width;
           canvas.height = height;
           
           // Clear canvas
           ctx.clearRect(0, 0, width, height);
           
           // Set background
           ctx.fillStyle = '#ffffff';
           ctx.fillRect(0, 0, width, height);
           
           // Draw your component's default visualization here
           // Use the same drawing logic as the main component
           // but with smaller dimensions and simplified features
           
       }, [width, height]);
       
       return (
           <canvas
               ref={canvasRef}
               width={width}
               height={height}
               className="border border-gray-200 rounded"
               style={{ imageRendering: 'pixelated' }}
           />
       );
   };
   
   export default ExampleComponentThumbnail;
   ```

2. **Add it to the registry** in `ThumbnailRegistry.jsx`:
   ```jsx
   import ExampleComponentThumbnail from './ExampleComponentThumbnail';
   
   const thumbnailRegistry = {
       'linear_function': LinearFunctionGraphThumbnail,
       'quadratic_function': QuadraticGraphThumbnail,
       'coordinate_plane': CoordinatePlaneThumbnail,
       'example_component': ExampleComponentThumbnail, // Add your component here
   };
   ```

3. **The thumbnail will automatically appear** in the MathComponentsRepository when the component ID matches.

## Thumbnail Guidelines

- **Size**: Default 80x60 pixels, but can be customized
- **Style**: Use subtle colors and thin lines for grid/axes
- **Content**: Show the default state of the component
- **Performance**: Keep drawing operations simple and efficient
- **Consistency**: Use similar styling across all thumbnails

## Best Practices

1. **Use the same default values** as the main component
2. **Simplify complex features** - don't show every option
3. **Make it recognizable** - users should understand what the component does
4. **Keep it lightweight** - thumbnails should load quickly
5. **Test at different sizes** - ensure it looks good at various dimensions

## Example: Adding a Circle Thumbnail

```jsx
// CircleThumbnail.jsx
const CircleThumbnail = ({ width = 120, height = 80 }) => {
    // ... setup code ...
    
    // Draw a simple circle with radius 2 at origin
    const centerX = width / 2;
    const centerY = height / 2;
    const radius = Math.min(width, height) / 4;
    
    ctx.strokeStyle = '#3B82F6';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
    ctx.stroke();
    
    // ... rest of component
};
```

Then add `'circle': CircleThumbnail` to the registry.
