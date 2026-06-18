import React, { useEffect, useRef } from 'react';

const GeometricConstructionThumbnail = ({ width = 120, height = 80 }) => {
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

        // Draw grid
        ctx.strokeStyle = '#e5e7eb';
        ctx.lineWidth = 1;
        
        // Vertical grid lines
        for (let x = 0; x <= width; x += 20) {
            ctx.beginPath();
            ctx.moveTo(x, 0);
            ctx.lineTo(x, height);
            ctx.stroke();
        }
        
        // Horizontal grid lines
        for (let y = 0; y <= height; y += 20) {
            ctx.beginPath();
            ctx.moveTo(0, y);
            ctx.lineTo(width, y);
            ctx.stroke();
        }

        // Draw a simple triangle construction
        const centerX = width / 2;
        const centerY = height / 2;
        
        // Draw triangle
        ctx.strokeStyle = '#3B82F6';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(centerX - 25, centerY + 15);
        ctx.lineTo(centerX + 25, centerY + 15);
        ctx.lineTo(centerX, centerY - 20);
        ctx.closePath();
        ctx.stroke();
        
        // Draw construction circles (compass marks)
        ctx.strokeStyle = '#10B981';
        ctx.lineWidth = 1;
        
        // Circle 1 (from left vertex)
        ctx.beginPath();
        ctx.arc(centerX - 25, centerY + 15, 20, 0, 2 * Math.PI);
        ctx.stroke();
        
        // Circle 2 (from right vertex)
        ctx.beginPath();
        ctx.arc(centerX + 25, centerY + 15, 20, 0, 2 * Math.PI);
        ctx.stroke();
        
        // Draw protractor-like angle measurement
        ctx.strokeStyle = '#F59E0B';
        ctx.lineWidth = 1;
        ctx.beginPath();
        ctx.arc(centerX, centerY + 15, 15, 0, Math.PI);
        ctx.stroke();
        
        // Draw angle markers
        ctx.beginPath();
        ctx.moveTo(centerX - 15, centerY + 15);
        ctx.lineTo(centerX - 12, centerY + 12);
        ctx.moveTo(centerX - 15, centerY + 15);
        ctx.lineTo(centerX - 12, centerY + 18);
        ctx.stroke();
        
        ctx.beginPath();
        ctx.moveTo(centerX + 15, centerY + 15);
        ctx.lineTo(centerX + 12, centerY + 12);
        ctx.moveTo(centerX + 15, centerY + 15);
        ctx.lineTo(centerX + 12, centerY + 18);
        ctx.stroke();

        // Draw tools icons
        ctx.fillStyle = '#6B7280';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';
        
        // Compass icon
        ctx.fillText('⊙', centerX - 35, centerY - 25);
        
        // Ruler icon
        ctx.fillText('📏', centerX + 35, centerY - 25);
        
        // Protractor icon
        ctx.fillText('∠', centerX, centerY + 35);

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

export default GeometricConstructionThumbnail;
