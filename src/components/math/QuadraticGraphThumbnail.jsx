import React, { useEffect, useRef } from 'react';

const QuadraticGraphThumbnail = ({ width = 120, height = 80 }) => {
    console.log('QuadraticGraphThumbnail rendering with:', { width, height });
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

        // Default values for y=x² (same as main component)
        const a = 1;
        const b = 0;
        const c = 0;
        const xMin = -5;
        const xMax = 5;
        const yMin = -5;
        const yMax = 5;
        const lineColor = '#3B82F6';
        const showGrid = true;
        const showPoints = true;
        const showVertex = true;
        const showRoots = true;

        // Calculate scale factors
        const xScale = width / (xMax - xMin);
        const yScale = height / (yMax - yMin);

        // Helper function to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - xMin) * xScale;
        const toCanvasY = (y) => height - (y - yMin) * yScale;

        // Draw grid (same as main component)
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB'; // Subtle grey grid lines
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = Math.ceil(xMin); x <= Math.floor(xMax); x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = Math.ceil(yMin); y <= Math.floor(yMax); y++) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes (same as main component)
        ctx.strokeStyle = '#000000'; // Black bold axes
        ctx.lineWidth = 3;

        // X-axis
        const xAxisY = toCanvasY(0);
        if (xAxisY >= 0 && xAxisY <= height) {
            ctx.beginPath();
            ctx.moveTo(0, xAxisY);
            ctx.lineTo(width, xAxisY);
            ctx.stroke();
        }

        // Y-axis
        const yAxisX = toCanvasX(0);
        if (yAxisX >= 0 && yAxisX <= width) {
            ctx.beginPath();
            ctx.moveTo(yAxisX, 0);
            ctx.lineTo(yAxisX, height);
            ctx.stroke();
        }

        // Draw function (same as main component)
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 3;
        ctx.beginPath();

        let firstPoint = true;
        const step = (xMax - xMin) / 200;
        for (let x = xMin; x <= xMax; x += step) {
            const y = a * x * x + b * x + c;
            if (isFinite(y) && y >= yMin && y <= yMax) {
                const canvasX = toCanvasX(x);
                const canvasY = toCanvasY(y);
                
                if (firstPoint) {
                    ctx.moveTo(canvasX, canvasY);
                    firstPoint = false;
                } else {
                    ctx.lineTo(canvasX, canvasY);
                }
            }
        }
        ctx.stroke();

        // Draw points if enabled (same as main component)
        if (showPoints) {
            ctx.fillStyle = lineColor;
            const step = (xMax - xMin) / 50;
            for (let x = xMin; x <= xMax; x += step) {
                const y = a * x * x + b * x + c;
                if (isFinite(y) && y >= yMin && y <= yMax) {
                    const canvasX = toCanvasX(x);
                    const canvasY = toCanvasY(y);
                    
                    ctx.beginPath();
                    ctx.arc(canvasX, canvasY, 3, 0, 2 * Math.PI);
                    ctx.fill();
                }
            }
        }

        // Draw vertex (same as main component)
        if (showVertex) {
            const vertexX = -b / (2 * a);
            const vertexY = a * vertexX * vertexX + b * vertexX + c;
            
            if (vertexX >= xMin && vertexX <= xMax && vertexY >= yMin && vertexY <= yMax) {
                const canvasX = toCanvasX(vertexX);
                const canvasY = toCanvasY(vertexY);
                
                ctx.fillStyle = '#ef4444';
                ctx.beginPath();
                ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
                ctx.fill();
            }
        }

        // Draw roots (same as main component)
        if (showRoots) {
            const discriminant = b * b - 4 * a * c;
            if (discriminant >= 0) {
                const sqrtDisc = Math.sqrt(discriminant);
                const root1 = (-b + sqrtDisc) / (2 * a);
                const root2 = (-b - sqrtDisc) / (2 * a);
                
                ctx.fillStyle = '#10b981';
                
                if (root1 >= xMin && root1 <= xMax) {
                    const canvasX = toCanvasX(root1);
                    const canvasY = toCanvasY(0);
                    ctx.beginPath();
                    ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
                    ctx.fill();
                }
                
                if (root2 >= xMin && root2 <= xMax) {
                    const canvasX = toCanvasX(root2);
                    const canvasY = toCanvasY(0);
                    ctx.beginPath();
                    ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
                    ctx.fill();
                }
            }
        }

        // Draw y-intercept (same as main component)
        const yIntercept = c;
        if (0 >= xMin && 0 <= xMax && yIntercept >= yMin && yIntercept <= yMax) {
            const canvasX = toCanvasX(0);
            const canvasY = toCanvasY(yIntercept);
            
            ctx.fillStyle = '#3b82f6';
            ctx.beginPath();
            ctx.arc(canvasX, canvasY, 6, 0, 2 * Math.PI);
            ctx.fill();
        }
    }, [width, height]);

    return (
        <canvas
            ref={canvasRef}
            style={{
                width: width,
                height: height,
                border: '1px solid #E5E7EB',
                borderRadius: '4px'
            }}
        />
    );
};

export default QuadraticGraphThumbnail;
