import React, { useEffect, useRef } from 'react';

const NumberLineThumbnail = ({ width = 120, height = 80 }) => {
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

        // Draw number line
        const centerY = height / 2;
        const startX = 10;
        const endX = width - 10;
        const lineLength = endX - startX;

        // Draw main line
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(startX, centerY);
        ctx.lineTo(endX, centerY);
        ctx.stroke();

        // Draw tick marks and numbers
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        ctx.fillStyle = '#000000';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';

        // Draw ticks from -5 to 5
        for (let i = -5; i <= 5; i++) {
            const x = startX + (i + 5) * (lineLength / 10);
            
            // Draw tick mark
            ctx.beginPath();
            ctx.moveTo(x, centerY - 5);
            ctx.lineTo(x, centerY + 5);
            ctx.stroke();
            
            // Draw number
            ctx.fillText(i.toString(), x, centerY + 20);
        }

        // Draw arrowheads
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        
        // Left arrow
        ctx.beginPath();
        ctx.moveTo(startX, centerY);
        ctx.lineTo(startX + 8, centerY - 4);
        ctx.moveTo(startX, centerY);
        ctx.lineTo(startX + 8, centerY + 4);
        ctx.stroke();
        
        // Right arrow
        ctx.beginPath();
        ctx.moveTo(endX, centerY);
        ctx.lineTo(endX - 8, centerY - 4);
        ctx.moveTo(endX, centerY);
        ctx.lineTo(endX - 8, centerY + 4);
        ctx.stroke();

        // Highlight zero
        const zeroX = startX + 5 * (lineLength / 10);
        ctx.strokeStyle = '#3B82F6';
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(zeroX, centerY - 8);
        ctx.lineTo(zeroX, centerY + 8);
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

export default NumberLineThumbnail;
