import React, { useEffect, useRef } from 'react';

const CubicFunctionThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for y=x³-2x (cubic function)
        const a = 1;
        const b = 0;
        const c = -2;
        const d = 0;
        const x_range = [-3, 3];
        const y_range = [-8, 8];
        const lineColor = '#8B5CF6';
        const showGrid = true;
        const showPoints = true;

        // Calculate scale factors
        const xScale = width / (x_range[1] - x_range[0]);
        const yScale = height / (y_range[1] - y_range[0]);

        // Helper function to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - x_range[0]) * xScale;
        const toCanvasY = (y) => height - (y - y_range[0]) * yScale;

        // Calculate cubic function value
        const calculateY = (x) => a * Math.pow(x, 3) + b * Math.pow(x, 2) + c * x + d;

        // Draw grid
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB';
            ctx.lineWidth = 1;

            // Vertical grid lines
            for (let x = x_range[0]; x <= x_range[1]; x++) {
                if (x === 0) continue; // Skip y-axis
                const canvasX = toCanvasX(x);
                ctx.beginPath();
                ctx.moveTo(canvasX, 0);
                ctx.lineTo(canvasX, height);
                ctx.stroke();
            }

            // Horizontal grid lines
            for (let y = y_range[0]; y <= y_range[1]; y++) {
                if (y === 0) continue; // Skip x-axis
                const canvasY = toCanvasY(y);
                ctx.beginPath();
                ctx.moveTo(0, canvasY);
                ctx.lineTo(width, canvasY);
                ctx.stroke();
            }
        }

        // Draw axes
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;

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

        // Draw the cubic function
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 2;
        ctx.beginPath();

        // Generate points for the curve
        const step = (x_range[1] - x_range[0]) / 100;
        let firstPoint = true;

        for (let x = x_range[0]; x <= x_range[1]; x += step) {
            const y = calculateY(x);
            const canvasX = toCanvasX(x);
            const canvasY = toCanvasY(y);

            if (firstPoint) {
                ctx.moveTo(canvasX, canvasY);
                firstPoint = false;
            } else {
                ctx.lineTo(canvasX, canvasY);
            }
        }
        ctx.stroke();

        // Draw key points
        if (showPoints) {
            ctx.fillStyle = lineColor;
            
            // Origin point
            const originX = toCanvasX(0);
            const originY = toCanvasY(0);
            if (originX >= 0 && originX <= width && originY >= 0 && originY <= height) {
                ctx.beginPath();
                ctx.arc(originX, originY, 3, 0, 2 * Math.PI);
                ctx.fill();
            }

            // Critical points (where derivative = 0)
            const criticalX1 = Math.sqrt(-c / (3 * a));
            const criticalX2 = -Math.sqrt(-c / (3 * a));
            
            if (criticalX1 >= x_range[0] && criticalX1 <= x_range[1]) {
                const criticalY1 = calculateY(criticalX1);
                const canvasX1 = toCanvasX(criticalX1);
                const canvasY1 = toCanvasY(criticalY1);
                if (canvasX1 >= 0 && canvasX1 <= width && canvasY1 >= 0 && canvasY1 <= height) {
                    ctx.beginPath();
                    ctx.arc(canvasX1, canvasY1, 3, 0, 2 * Math.PI);
                    ctx.fill();
                }
            }

            if (criticalX2 >= x_range[0] && criticalX2 <= x_range[1]) {
                const criticalY2 = calculateY(criticalX2);
                const canvasX2 = toCanvasX(criticalX2);
                const canvasY2 = toCanvasY(criticalY2);
                if (canvasX2 >= 0 && canvasX2 <= width && canvasY2 >= 0 && canvasY2 <= height) {
                    ctx.beginPath();
                    ctx.arc(canvasX2, canvasY2, 3, 0, 2 * Math.PI);
                    ctx.fill();
                }
            }
        }

        // Add function label
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('f(x) = x³ - 2x', width / 2, height - 5);

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

export default CubicFunctionThumbnail;
