import React, { useEffect, useRef } from 'react';

const VennDiagramThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for Venn diagram
        const centerX = width / 2;
        const centerY = height / 2;
        const radius = Math.min(width, height) / 4;
        const overlap = radius * 0.3;

        // Colors
        const setAColor = '#DBEAFE';
        const setBColor = '#FEF3C7';
        const intersectionColor = '#E0E7FF';
        const borderColor = '#3B82F6';

        // Draw Set A (left circle)
        ctx.fillStyle = setAColor;
        ctx.beginPath();
        ctx.arc(centerX - overlap, centerY, radius, 0, 2 * Math.PI);
        ctx.fill();

        // Draw Set B (right circle)
        ctx.fillStyle = setBColor;
        ctx.beginPath();
        ctx.arc(centerX + overlap, centerY, radius, 0, 2 * Math.PI);
        ctx.fill();

        // Draw intersection with special color
        ctx.fillStyle = intersectionColor;
        ctx.globalCompositeOperation = 'multiply';
        ctx.beginPath();
        ctx.arc(centerX - overlap, centerY, radius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.beginPath();
        ctx.arc(centerX + overlap, centerY, radius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.globalCompositeOperation = 'source-over';

        // Draw borders
        ctx.strokeStyle = borderColor;
        ctx.lineWidth = 2;
        
        // Set A border
        ctx.beginPath();
        ctx.arc(centerX - overlap, centerY, radius, 0, 2 * Math.PI);
        ctx.stroke();
        
        // Set B border
        ctx.beginPath();
        ctx.arc(centerX + overlap, centerY, radius, 0, 2 * Math.PI);
        ctx.stroke();

        // Add set labels
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        
        // Set A label
        ctx.fillText('A', centerX - overlap - radius/2, centerY - radius/2);
        
        // Set B label
        ctx.fillText('B', centerX + overlap + radius/2, centerY - radius/2);

        // Add sample elements
        ctx.font = '8px Arial';
        
        // Elements in A only
        ctx.fillText('1', centerX - overlap - radius/3, centerY - 5);
        ctx.fillText('2', centerX - overlap - radius/3, centerY + 5);
        
        // Elements in B only
        ctx.fillText('4', centerX + overlap + radius/3, centerY - 5);
        ctx.fillText('5', centerX + overlap + radius/3, centerY + 5);
        
        // Elements in intersection
        ctx.fillText('3', centerX, centerY);

        // Add title
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Venn Diagram', width / 2, 15);

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

export default VennDiagramThumbnail;
