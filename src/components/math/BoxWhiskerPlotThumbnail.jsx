import React, { useEffect, useRef } from 'react';

const BoxWhiskerPlotThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for box whisker plot
        const data = [2, 4, 5, 6, 7, 8, 9, 10, 12, 15];
        const lineColor = '#3B82F6';
        const boxColor = '#DBEAFE';
        const medianColor = '#1E40AF';

        // Calculate statistics
        const sortedData = [...data].sort((a, b) => a - b);
        const min = sortedData[0];
        const max = sortedData[sortedData.length - 1];
        const q1 = sortedData[Math.floor(sortedData.length * 0.25)];
        const median = sortedData[Math.floor(sortedData.length * 0.5)];
        const q3 = sortedData[Math.floor(sortedData.length * 0.75)];

        // Calculate scale factors
        const dataRange = max - min;
        const padding = 20;
        const plotWidth = width - 2 * padding;
        const plotHeight = height - 2 * padding;
        
        const xScale = plotWidth / dataRange;
        const yScale = plotHeight / 4; // 4 units for the box plot structure

        // Helper function to convert data values to canvas coordinates
        const toCanvasX = (value) => padding + (value - min) * xScale;
        const toCanvasY = (y) => padding + y * yScale;

        // Draw the box whisker plot
        const centerY = height / 2;
        const boxHeight = 20;

        // Draw whiskers
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 2;

        // Lower whisker
        ctx.beginPath();
        ctx.moveTo(toCanvasX(min), centerY);
        ctx.lineTo(toCanvasX(min), centerY - boxHeight/2);
        ctx.moveTo(toCanvasX(min), centerY);
        ctx.lineTo(toCanvasX(min), centerY + boxHeight/2);
        ctx.stroke();

        // Upper whisker
        ctx.beginPath();
        ctx.moveTo(toCanvasX(max), centerY);
        ctx.lineTo(toCanvasX(max), centerY - boxHeight/2);
        ctx.moveTo(toCanvasX(max), centerY);
        ctx.lineTo(toCanvasX(max), centerY + boxHeight/2);
        ctx.stroke();

        // Draw box
        const boxLeft = toCanvasX(q1);
        const boxRight = toCanvasX(q3);
        const boxTop = centerY - boxHeight/2;
        const boxBottom = centerY + boxHeight/2;

        // Fill box
        ctx.fillStyle = boxColor;
        ctx.fillRect(boxLeft, boxTop, boxRight - boxLeft, boxHeight);

        // Box border
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 2;
        ctx.strokeRect(boxLeft, boxTop, boxRight - boxLeft, boxHeight);

        // Draw median line
        const medianX = toCanvasX(median);
        ctx.strokeStyle = medianColor;
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(medianX, boxTop);
        ctx.lineTo(medianX, boxBottom);
        ctx.stroke();

        // Draw data points (outliers)
        ctx.fillStyle = lineColor;
        data.forEach(value => {
            if (value < q1 - 1.5 * (q3 - q1) || value > q3 + 1.5 * (q3 - q1)) {
                const x = toCanvasX(value);
                const y = centerY + (Math.random() - 0.5) * boxHeight * 0.8;
                ctx.beginPath();
                ctx.arc(x, y, 2, 0, 2 * Math.PI);
                ctx.fill();
            }
        });

        // Draw axis
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(padding, centerY + boxHeight/2 + 10);
        ctx.lineTo(width - padding, centerY + boxHeight/2 + 10);
        ctx.stroke();

        // Add scale markers
        ctx.fillStyle = '#374151';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';
        
        // Min marker
        ctx.fillText(min.toString(), toCanvasX(min), centerY + boxHeight/2 + 25);
        
        // Q1 marker
        ctx.fillText(q1.toString(), toCanvasX(q1), centerY + boxHeight/2 + 25);
        
        // Median marker
        ctx.fillText(median.toString(), toCanvasX(median), centerY + boxHeight/2 + 25);
        
        // Q3 marker
        ctx.fillText(q3.toString(), toCanvasX(q3), centerY + boxHeight/2 + 25);
        
        // Max marker
        ctx.fillText(max.toString(), toCanvasX(max), centerY + boxHeight/2 + 25);

        // Add title
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Box Plot', width / 2, 15);

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

export default BoxWhiskerPlotThumbnail;
