import React, { useEffect, useRef } from 'react';

const LinearFunctionGraphThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for y=2x+3 (same as main component)
        const m = 2;
        const c = 3;
        const x_range = [-10, 10];
        const y_range = [-20, 20];
        const lineColor = '#3B82F6';
        const showGrid = true;
        const showPoints = true;
        const showSlope = false; // Disable for thumbnail
        const showYIntercept = true;
        const showXIntercept = true;

        // Calculate scale factors
        const xScale = width / (x_range[1] - x_range[0]);
        const yScale = height / (y_range[1] - y_range[0]);

        // Helper function to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - x_range[0]) * xScale;
        const toCanvasY = (y) => height - (y - y_range[0]) * yScale;

        // Draw grid (same as main component)
        if (showGrid) {
            ctx.strokeStyle = '#D1D5DB'; // Subtle grey grid lines
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

        // Draw the linear function (same as main component)
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 3;
        ctx.beginPath();

        // Calculate two points on the line
        const x1 = x_range[0];
        const y1 = m * x1 + c;
        const x2 = x_range[1];
        const y2 = m * x2 + c;

        const canvasX1 = toCanvasX(x1);
        const canvasY1 = toCanvasY(y1);
        const canvasX2 = toCanvasX(x2);
        const canvasY2 = toCanvasY(y2);

        ctx.moveTo(canvasX1, canvasY1);
        ctx.lineTo(canvasX2, canvasY2);
        ctx.stroke();

        // Draw points if enabled (same as main component)
        if (showPoints) {
            ctx.fillStyle = lineColor;
            ctx.beginPath();
            ctx.arc(canvasX1, canvasY1, 4, 0, 2 * Math.PI);
            ctx.fill();
            ctx.beginPath();
            ctx.arc(canvasX2, canvasY2, 4, 0, 2 * Math.PI);
            ctx.fill();
        }

        // Draw y-intercept if enabled (same as main component)
        if (showYIntercept) {
            const yInterceptX = 0;
            const yInterceptY = c;
            const yInterceptCanvasX = toCanvasX(yInterceptX);
            const yInterceptCanvasY = toCanvasY(yInterceptY);

            if (yInterceptCanvasY >= 0 && yInterceptCanvasY <= height) {
                ctx.fillStyle = '#10B981';
                ctx.beginPath();
                ctx.arc(yInterceptCanvasX, yInterceptCanvasY, 6, 0, 2 * Math.PI);
                ctx.fill();
            }
        }

        // Draw x-intercept if enabled (same as main component)
        if (showXIntercept && m !== 0) {
            const xInterceptX = -c / m;
            const xInterceptY = 0;
            const xInterceptCanvasX = toCanvasX(xInterceptX);
            const xInterceptCanvasY = toCanvasY(xInterceptY);

            if (xInterceptCanvasX >= 0 && xInterceptCanvasX <= width) {
                ctx.fillStyle = '#F59E0B';
                ctx.beginPath();
                ctx.arc(xInterceptCanvasX, xInterceptCanvasY, 6, 0, 2 * Math.PI);
                ctx.fill();
            }
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

export default LinearFunctionGraphThumbnail;
