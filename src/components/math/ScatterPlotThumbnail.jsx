import React, { useEffect, useRef } from 'react';

const ScatterPlotThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for scatter plot (positive correlation)
        const data = [
            { x: 1, y: 2 }, { x: 2, y: 3 }, { x: 3, y: 2.5 }, { x: 4, y: 4 },
            { x: 5, y: 3.5 }, { x: 6, y: 5 }, { x: 7, y: 4.5 }, { x: 8, y: 6 },
            { x: 9, y: 5.5 }, { x: 10, y: 7 }
        ];
        const lineColor = '#EF4444';
        const pointColor = '#3B82F6';

        // Calculate scale factors
        const padding = 20;
        const plotWidth = width - 2 * padding;
        const plotHeight = height - 2 * padding;
        
        const xValues = data.map(point => point.x);
        const yValues = data.map(point => point.y);
        const xMin = Math.min(...xValues);
        const xMax = Math.max(...xValues);
        const yMin = Math.min(...yValues);
        const yMax = Math.max(...yValues);
        
        const xScale = plotWidth / (xMax - xMin);
        const yScale = plotHeight / (yMax - yMin);

        // Helper function to convert data coordinates to canvas coordinates
        const toCanvasX = (x) => padding + (x - xMin) * xScale;
        const toCanvasY = (y) => height - padding - (y - yMin) * yScale;

        // Draw axes
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        
        // X-axis
        ctx.beginPath();
        ctx.moveTo(padding, height - padding);
        ctx.lineTo(width - padding, height - padding);
        ctx.stroke();
        
        // Y-axis
        ctx.beginPath();
        ctx.moveTo(padding, padding);
        ctx.lineTo(padding, height - padding);
        ctx.stroke();

        // Draw grid lines
        ctx.strokeStyle = '#D1D5DB';
        ctx.lineWidth = 0.5;
        
        // Vertical grid lines
        for (let x = xMin; x <= xMax; x++) {
            const canvasX = toCanvasX(x);
            ctx.beginPath();
            ctx.moveTo(canvasX, padding);
            ctx.lineTo(canvasX, height - padding);
            ctx.stroke();
        }
        
        // Horizontal grid lines
        for (let y = yMin; y <= yMax; y++) {
            const canvasY = toCanvasY(y);
            ctx.beginPath();
            ctx.moveTo(padding, canvasY);
            ctx.lineTo(width - padding, canvasY);
            ctx.stroke();
        }

        // Draw trend line (simple linear regression)
        const n = data.length;
        const sumX = data.reduce((sum, point) => sum + point.x, 0);
        const sumY = data.reduce((sum, point) => sum + point.y, 0);
        const sumXY = data.reduce((sum, point) => sum + point.x * point.y, 0);
        const sumXX = data.reduce((sum, point) => sum + point.x * point.x, 0);
        
        const slope = (n * sumXY - sumX * sumY) / (n * sumXX - sumX * sumX);
        const intercept = (sumY - slope * sumX) / n;
        
        // Draw trend line
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(toCanvasX(xMin), toCanvasY(slope * xMin + intercept));
        ctx.lineTo(toCanvasX(xMax), toCanvasY(slope * xMax + intercept));
        ctx.stroke();

        // Draw data points
        ctx.fillStyle = pointColor;
        data.forEach(point => {
            const canvasX = toCanvasX(point.x);
            const canvasY = toCanvasY(point.y);
            
            ctx.beginPath();
            ctx.arc(canvasX, canvasY, 3, 0, 2 * Math.PI);
            ctx.fill();
        });

        // Add axis labels
        ctx.fillStyle = '#374151';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';
        
        // X-axis labels
        for (let x = xMin; x <= xMax; x++) {
            const canvasX = toCanvasX(x);
            ctx.fillText(x.toString(), canvasX, height - padding + 12);
        }
        
        // Y-axis labels
        for (let y = yMin; y <= yMax; y++) {
            const canvasY = toCanvasY(y);
            ctx.fillText(y.toString(), padding - 8, canvasY + 3);
        }

        // Add title
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Scatter Plot', width / 2, 15);

        // Add correlation info
        const correlation = slope > 0 ? 'Positive' : 'Negative';
        ctx.fillStyle = '#6B7280';
        ctx.font = '8px Arial';
        ctx.textAlign = 'left';
        ctx.fillText(`Correlation: ${correlation}`, padding, height - padding + 25);

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

export default ScatterPlotThumbnail;
