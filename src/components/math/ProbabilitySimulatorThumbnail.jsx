import React, { useEffect, useRef } from 'react';

const ProbabilitySimulatorThumbnail = ({ width = 120, height = 80 }) => {
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

        // Draw coin flip simulation
        const centerX = width / 2;
        const centerY = height / 2;
        
        // Draw coin
        ctx.strokeStyle = '#F59E0B';
        ctx.lineWidth = 2;
        ctx.fillStyle = '#FCD34D';
        ctx.beginPath();
        ctx.arc(centerX, centerY, 20, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();
        
        // Draw coin face (heads)
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 12px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('H', centerX, centerY + 4);
        
        // Draw results bar chart
        const barWidth = 25;
        const barHeight = 30;
        const startX = 10;
        const startY = height - 35;
        
        // Heads bar
        ctx.fillStyle = '#10B981';
        ctx.fillRect(startX, startY - 20, barWidth, 20);
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        ctx.strokeRect(startX, startY - 20, barWidth, 20);
        
        // Tails bar
        ctx.fillStyle = '#EF4444';
        ctx.fillRect(startX + barWidth + 5, startY - 15, barWidth, 15);
        ctx.strokeRect(startX + barWidth + 5, startY - 15, barWidth, 15);
        
        // Labels
        ctx.fillStyle = '#000000';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('H', startX + barWidth/2, startY + 10);
        ctx.fillText('T', startX + barWidth + 5 + barWidth/2, startY + 10);
        
        // Draw probability text
        ctx.fillStyle = '#6B7280';
        ctx.font = '6px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('P(H) = 0.5', startX + barWidth/2, startY - 25);
        ctx.fillText('P(T) = 0.5', startX + barWidth + 5 + barWidth/2, startY - 25);
        
        // Draw simulation dots
        ctx.fillStyle = '#3B82F6';
        for (let i = 0; i < 8; i++) {
            const x = startX + 60 + (i % 4) * 8;
            const y = startY - 35 + Math.floor(i / 4) * 8;
            ctx.beginPath();
            ctx.arc(x, y, 2, 0, 2 * Math.PI);
            ctx.fill();
        }
        
        // Draw arrow showing simulation
        ctx.strokeStyle = '#6B7280';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.moveTo(centerX + 30, centerY);
        ctx.lineTo(centerX + 45, centerY);
        ctx.stroke();
        
        // Arrowhead
        ctx.beginPath();
        ctx.moveTo(centerX + 45, centerY);
        ctx.lineTo(centerX + 42, centerY - 3);
        ctx.moveTo(centerX + 45, centerY);
        ctx.lineTo(centerX + 42, centerY + 3);
        ctx.stroke();

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

export default ProbabilitySimulatorThumbnail;
