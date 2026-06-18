import React, { useEffect, useRef } from 'react';

const CoordinatePlaneThumbnail = ({ width = 120, height = 80 }) => {
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

        // Grid settings
        const x_range = [-5, 5];
        const y_range = [-4, 4];

        // Calculate scale factors
        const xScale = width / (x_range[1] - x_range[0]);
        const yScale = height / (y_range[1] - y_range[0]);

        // Helper function to convert math coordinates to canvas coordinates
        const toCanvasX = (x) => (x - x_range[0]) * xScale;
        const toCanvasY = (y) => height - (y - y_range[0]) * yScale;

        // Draw grid (subtle)
        ctx.strokeStyle = '#E5E7EB';
        ctx.lineWidth = 0.5;

        // Vertical grid lines
        for (let x = x_range[0]; x <= x_range[1]; x++) {
            if (x === 0) continue;
            const canvasX = toCanvasX(x);
            ctx.beginPath();
            ctx.moveTo(canvasX, 0);
            ctx.lineTo(canvasX, height);
            ctx.stroke();
        }

        // Horizontal grid lines
        for (let y = y_range[0]; y <= y_range[1]; y++) {
            if (y === 0) continue;
            const canvasY = toCanvasY(y);
            ctx.beginPath();
            ctx.moveTo(0, canvasY);
            ctx.lineTo(width, canvasY);
            ctx.stroke();
        }

        // Draw axes
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1.5;

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

        // Draw some example points
        const points = [
            { x: 2, y: 3, color: '#3B82F6' },
            { x: -1, y: 2, color: '#EF4444' },
            { x: 0, y: -2, color: '#10B981' },
            { x: -3, y: -1, color: '#F59E0B' }
        ];

        points.forEach(point => {
            const canvasX = toCanvasX(point.x);
            const canvasY = toCanvasY(point.y);
            
            if (canvasX >= 0 && canvasX <= width && canvasY >= 0 && canvasY <= height) {
                ctx.fillStyle = point.color;
                ctx.beginPath();
                ctx.arc(canvasX, canvasY, 2, 0, 2 * Math.PI);
                ctx.fill();
            }
        });

        // Draw axis labels
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 8px Arial';
        ctx.textAlign = 'center';
        
        // X-axis label
        ctx.fillText('X', width / 2, height - 5);
        
        // Y-axis label
        ctx.save();
        ctx.translate(8, height / 2);
        ctx.rotate(-Math.PI / 2);
        ctx.fillText('Y', 0, 0);
        ctx.restore();

    }, [width, height]);

    return (
        <div
            style={{
                width: width,
                height: height,
                backgroundColor: '#F59E0B',
                border: '3px solid #D97706',
                borderRadius: '4px',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: 'white',
                fontSize: '10px',
                fontWeight: 'bold'
            }}
        >
            Grid
        </div>
    );
};

export default CoordinatePlaneThumbnail;
