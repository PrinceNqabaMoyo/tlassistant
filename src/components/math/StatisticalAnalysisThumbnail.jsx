import React, { useEffect, useRef } from 'react';

const StatisticalAnalysisThumbnail = ({ width = 120, height = 80 }) => {
    const canvasRef = useRef(null);

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;

        const ctx = canvas.getContext('2d');
        if (!canvas) return;

        // Set canvas size
        canvas.width = width;
        canvas.height = height;

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        // Sample data: [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8]
        const data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8];
        
        // Calculate statistics
        const sortedData = [...data].sort((a, b) => a - b);
        const mean = data.reduce((sum, val) => sum + val, 0) / data.length;
        const median = sortedData[Math.floor(sortedData.length / 2)];
        const mode = 5; // Most frequent value
        
        // Draw histogram
        const barWidth = 15;
        const maxHeight = height - 30;
        const startX = 10;
        
        // Count frequencies
        const frequencies = {};
        data.forEach(val => {
            frequencies[val] = (frequencies[val] || 0) + 1;
        });
        
        // Draw bars
        ctx.fillStyle = '#3B82F6';
        Object.entries(frequencies).forEach(([value, freq], index) => {
            const barHeight = (freq / Math.max(...Object.values(frequencies))) * maxHeight;
            const x = startX + index * barWidth;
            const y = height - 25 - barHeight;
            
            ctx.fillRect(x, y, barWidth - 1, barHeight);
            
            // Draw value label
            ctx.fillStyle = '#000000';
            ctx.font = '8px Arial';
            ctx.textAlign = 'center';
            ctx.fillText(value, x + barWidth/2, height - 5);
            ctx.fillStyle = '#3B82F6';
        });
        
        // Draw mean line
        ctx.strokeStyle = '#EF4444';
        ctx.lineWidth = 2;
        const meanX = startX + (mean - 2) * barWidth + barWidth/2;
        ctx.beginPath();
        ctx.moveTo(meanX, 10);
        ctx.lineTo(meanX, height - 25);
        ctx.stroke();
        
        // Draw median line
        ctx.strokeStyle = '#10B981';
        ctx.lineWidth = 2;
        const medianX = startX + (median - 2) * barWidth + barWidth/2;
        ctx.beginPath();
        ctx.moveTo(medianX, 10);
        ctx.lineTo(medianX, height - 25);
        ctx.stroke();
        
        // Draw mode line
        ctx.strokeStyle = '#F59E0B';
        ctx.lineWidth = 2;
        const modeX = startX + (mode - 2) * barWidth + barWidth/2;
        ctx.beginPath();
        ctx.moveTo(modeX, 10);
        ctx.lineTo(modeX, height - 25);
        ctx.stroke();
        
        // Draw legend
        ctx.fillStyle = '#000000';
        ctx.font = '6px Arial';
        ctx.textAlign = 'left';
        
        // Mean
        ctx.fillStyle = '#EF4444';
        ctx.fillText('Mean', 5, 8);
        
        // Median
        ctx.fillStyle = '#10B981';
        ctx.fillText('Median', 5, 16);
        
        // Mode
        ctx.fillStyle = '#F59E0B';
        ctx.fillText('Mode', 5, 24);

    }, [width, height]);

    return (
        <canvas
            ref={canvasRef}
            style={{
                border: '1px solid #e5e7eb',
                borderRadius: '4px',
                width: width,
                height: height
            }}
        />
    );
};

export default StatisticalAnalysisThumbnail;
