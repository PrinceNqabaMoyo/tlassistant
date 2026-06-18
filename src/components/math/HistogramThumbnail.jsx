import React, { useEffect, useRef } from 'react';

const HistogramThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for histogram
        const data = [2, 3, 3, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 7, 7, 8];
        const lineColor = '#8B5CF6';
        const barColor = '#DDD6FE';

        // Calculate histogram bins
        const min = Math.min(...data);
        const max = Math.max(...data);
        const binCount = 6;
        const binWidth = (max - min) / binCount;
        
        const bins = new Array(binCount).fill(0);
        data.forEach(value => {
            const binIndex = Math.min(Math.floor((value - min) / binWidth), binCount - 1);
            bins[binIndex]++;
        });

        // Calculate scale factors
        const padding = 20;
        const plotWidth = width - 2 * padding;
        const plotHeight = height - 2 * padding;
        
        const maxFrequency = Math.max(...bins);
        const xScale = plotWidth / binCount;
        const yScale = plotHeight / maxFrequency;

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

        // Draw histogram bars
        bins.forEach((frequency, index) => {
            if (frequency > 0) {
                const barHeight = frequency * yScale;
                const barX = padding + index * xScale;
                const barY = height - padding - barHeight;
                const barWidth = xScale * 0.8;

                // Fill bar
                ctx.fillStyle = barColor;
                ctx.fillRect(barX + xScale * 0.1, barY, barWidth, barHeight);

                // Bar border
                ctx.strokeStyle = lineColor;
                ctx.lineWidth = 1;
                ctx.strokeRect(barX + xScale * 0.1, barY, barWidth, barHeight);

                // Add frequency label
                ctx.fillStyle = '#374151';
                ctx.font = '8px Arial';
                ctx.textAlign = 'center';
                ctx.fillText(frequency.toString(), barX + xScale / 2, barY - 5);
            }
        });

        // Add bin labels
        ctx.fillStyle = '#374151';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';
        
        for (let i = 0; i <= binCount; i++) {
            const value = min + i * binWidth;
            const x = padding + i * xScale;
            ctx.fillText(value.toFixed(1), x, height - padding + 12);
        }

        // Add title
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Histogram', width / 2, 15);

        // Add statistics
        const mean = data.reduce((sum, val) => sum + val, 0) / data.length;
        const sortedData = [...data].sort((a, b) => a - b);
        const median = sortedData[Math.floor(sortedData.length / 2)];
        
        ctx.fillStyle = '#6B7280';
        ctx.font = '8px Arial';
        ctx.textAlign = 'left';
        ctx.fillText(`Mean: ${mean.toFixed(1)}`, padding, height - padding + 25);
        ctx.fillText(`Median: ${median}`, padding + 60, height - padding + 25);

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

export default HistogramThumbnail;
