import React, { useEffect, useRef } from 'react';

const AlgebraicExpressionBuilderThumbnail = ({ width = 120, height = 80 }) => {
    const canvasRef = useRef(null);

    console.log('🔍 AlgebraicExpressionBuilderThumbnail render called with:', { width, height });

    useEffect(() => {
        console.log('🔍 AlgebraicExpressionBuilderThumbnail useEffect triggered');
        
        const canvas = canvasRef.current;
        if (!canvas) {
            console.error('❌ Canvas ref is null!');
            return;
        }

        console.log('🔍 Canvas element found:', canvas);

        const ctx = canvas.getContext('2d');
        if (!ctx) {
            console.error('❌ Could not get 2D context!');
            return;
        }

        console.log('🔍 2D context obtained successfully');

        // Set canvas size
        canvas.width = width;
        canvas.height = height;
        console.log('🔍 Canvas size set to:', { width: canvas.width, height: canvas.height });

        // Clear canvas
        ctx.clearRect(0, 0, width, height);

        // Set background
        ctx.fillStyle = '#ffffff';
        ctx.fillRect(0, 0, width, height);

        // Add border
        ctx.strokeStyle = '#E5E7EB';
        ctx.lineWidth = 1;
        ctx.strokeRect(0, 0, width, height);

        // Set text properties
        ctx.font = 'bold 12px Arial';
        ctx.textAlign = 'center';
        ctx.fillStyle = '#1F2937';

        // Draw title
        ctx.fillText('Algebraic', width / 2, 18);
        ctx.fillText('Expressions', width / 2, 32);

        // Draw mathematical symbols and expressions
        ctx.font = '14px Arial';
        
        // Draw x² symbol
        ctx.fillStyle = '#3B82F6';
        ctx.fillText('x²', width / 4, 50);
        
        // Draw + symbol
        ctx.fillStyle = '#6B7280';
        ctx.fillText('+', width / 2, 50);
        
        // Draw √ symbol
        ctx.fillStyle = '#10B981';
        ctx.fillText('√', 3 * width / 4, 50);
        
        // Draw π symbol
        ctx.fillStyle = '#8B5CF6';
        ctx.fillText('π', width / 4, 65);
        
        // Draw × symbol
        ctx.fillStyle = '#F59E0B';
        ctx.fillText('×', width / 2, 65);
        
        // Draw ÷ symbol
        ctx.fillStyle = '#EF4444';
        ctx.fillText('÷', 3 * width / 4, 65);

        // Draw operation examples
        ctx.font = '10px Arial';
        ctx.fillStyle = '#6B7280';
        ctx.textAlign = 'left';
        
        // Example 1: Simplify
        ctx.fillText('2x + 3x → 5x', 5, height - 15);
        
        // Example 2: Factor
        ctx.fillText('x² - 4 → (x+2)(x-2)', 5, height - 5);

        // Draw decorative elements
        ctx.strokeStyle = '#E5E7EB';
        ctx.lineWidth = 1;
        
        // Draw horizontal separator line
        ctx.beginPath();
        ctx.moveTo(5, height - 20);
        ctx.lineTo(width - 5, height - 20);
        ctx.stroke();

        // Draw small mathematical operation icons
        ctx.fillStyle = '#3B82F6';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';
        
        // Draw operation labels
        ctx.fillText('Simplify', width / 4, height - 25);
        ctx.fillText('Factor', width / 2, height - 25);
        ctx.fillText('Solve', 3 * width / 4, height - 25);

        console.log('🔍 Canvas rendering completed successfully');

    }, [width, height]);

    console.log('🔍 Returning canvas element');
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

export default AlgebraicExpressionBuilderThumbnail;
