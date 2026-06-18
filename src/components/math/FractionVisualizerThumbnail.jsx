import React, { useEffect, useRef } from 'react';

const FractionVisualizerThumbnail = ({ width = 120, height = 80 }) => {
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

        // Draw fraction 3/4 as example
        const numerator = 3;
        const denominator = 4;
        
        // Draw circle
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) / 3;
        
        // Draw circle outline
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, 2 * Math.PI);
        ctx.stroke();
        
        // Draw fraction lines
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 1;
        
        // Vertical line
        ctx.beginPath();
        ctx.moveTo(centerX, centerY - radius);
        ctx.lineTo(centerX, centerY + radius);
        ctx.stroke();
        
        // Horizontal line
        ctx.beginPath();
        ctx.moveTo(centerX - radius, centerY);
        ctx.lineTo(centerX + radius, centerY);
        ctx.stroke();
        
        // Fill 3/4 of the circle (top-left, top-right, bottom-left)
        ctx.fillStyle = '#3B82F6';
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, -Math.PI, -Math.PI/2); // Top-left quadrant
        ctx.lineTo(centerX, centerY);
        ctx.closePath();
        ctx.fill();
        
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, -Math.PI/2, 0); // Top-right quadrant
        ctx.lineTo(centerX, centerY);
        ctx.closePath();
        ctx.fill();
        
        ctx.beginPath();
        ctx.arc(centerX, centerY, radius, 0, Math.PI/2); // Bottom-right quadrant
        ctx.lineTo(centerX, centerY);
        ctx.closePath();
        ctx.fill();
        
        // Draw fraction text
        ctx.fillStyle = '#000000';
        ctx.font = 'bold 14px Arial';
        ctx.textAlign = 'center';
        
        // Numerator (top)
        ctx.fillText(numerator.toString(), centerX, centerY - 25);
        
        // Denominator (bottom)
        ctx.fillText(denominator.toString(), centerX, centerY + 25);
        
        // Fraction bar
        ctx.strokeStyle = '#000000';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX - 15, centerY);
        ctx.lineTo(centerX + 15, centerY);
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

export default FractionVisualizerThumbnail;
