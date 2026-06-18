import React, { useEffect, useRef } from 'react';

const TreeDiagramThumbnail = ({ width = 120, height = 80 }) => {
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

        // Default values for tree diagram
        const startX = width / 2;
        const startY = 20;
        const levelHeight = 25;
        const nodeRadius = 8;
        const lineColor = '#3B82F6';
        const nodeColor = '#DBEAFE';

        // Draw tree structure
        ctx.strokeStyle = lineColor;
        ctx.lineWidth = 2;
        ctx.fillStyle = nodeColor;

        // Root node
        ctx.beginPath();
        ctx.arc(startX, startY, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        // First level nodes
        const leftNode1 = { x: startX - 30, y: startY + levelHeight };
        const rightNode1 = { x: startX + 30, y: startY + levelHeight };

        // Draw connections to first level
        ctx.beginPath();
        ctx.moveTo(startX, startY + nodeRadius);
        ctx.lineTo(leftNode1.x, leftNode1.y - nodeRadius);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(startX, startY + nodeRadius);
        ctx.lineTo(rightNode1.x, rightNode1.y - nodeRadius);
        ctx.stroke();

        // Draw first level nodes
        ctx.beginPath();
        ctx.arc(leftNode1.x, leftNode1.y, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(rightNode1.x, rightNode1.y, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        // Second level nodes
        const leftNode2a = { x: leftNode1.x - 20, y: leftNode1.y + levelHeight };
        const leftNode2b = { x: leftNode1.x + 20, y: leftNode1.y + levelHeight };
        const rightNode2a = { x: rightNode1.x - 20, y: rightNode1.y + levelHeight };
        const rightNode2b = { x: rightNode1.x + 20, y: rightNode1.y + levelHeight };

        // Draw connections to second level
        ctx.beginPath();
        ctx.moveTo(leftNode1.x, leftNode1.y + nodeRadius);
        ctx.lineTo(leftNode2a.x, leftNode2a.y - nodeRadius);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(leftNode1.x, leftNode1.y + nodeRadius);
        ctx.lineTo(leftNode2b.x, leftNode2b.y - nodeRadius);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(rightNode1.x, rightNode1.y + nodeRadius);
        ctx.lineTo(rightNode2a.x, rightNode2a.y - nodeRadius);
        ctx.stroke();

        ctx.beginPath();
        ctx.moveTo(rightNode1.x, rightNode1.y + nodeRadius);
        ctx.lineTo(rightNode2b.x, rightNode2b.y - nodeRadius);
        ctx.stroke();

        // Draw second level nodes
        ctx.beginPath();
        ctx.arc(leftNode2a.x, leftNode2a.y, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(leftNode2b.x, leftNode2b.y, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(rightNode2a.x, rightNode2a.y, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        ctx.beginPath();
        ctx.arc(rightNode2b.x, rightNode2b.y, nodeRadius, 0, 2 * Math.PI);
        ctx.fill();
        ctx.stroke();

        // Add probability labels
        ctx.fillStyle = '#374151';
        ctx.font = '8px Arial';
        ctx.textAlign = 'center';

        // First level probabilities
        ctx.fillText('0.5', (startX + leftNode1.x) / 2, (startY + leftNode1.y) / 2);
        ctx.fillText('0.5', (startX + rightNode1.x) / 2, (startY + rightNode1.y) / 2);

        // Second level probabilities
        ctx.fillText('0.5', (leftNode1.x + leftNode2a.x) / 2, (leftNode1.y + leftNode2a.y) / 2);
        ctx.fillText('0.5', (leftNode1.x + leftNode2b.x) / 2, (leftNode1.y + leftNode2b.y) / 2);
        ctx.fillText('0.5', (rightNode1.x + rightNode2a.x) / 2, (rightNode1.y + rightNode2a.y) / 2);
        ctx.fillText('0.5', (rightNode1.x + rightNode2b.x) / 2, (rightNode1.y + rightNode2b.y) / 2);

        // Add outcome labels
        ctx.fillText('A', leftNode2a.x, leftNode2a.y + 15);
        ctx.fillText('B', leftNode2b.x, leftNode2b.y + 15);
        ctx.fillText('C', rightNode2a.x, rightNode2a.y + 15);
        ctx.fillText('D', rightNode2b.x, rightNode2b.y + 15);

        // Add title
        ctx.fillStyle = '#374151';
        ctx.font = '10px Arial';
        ctx.textAlign = 'center';
        ctx.fillText('Tree Diagram', width / 2, 15);

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

export default TreeDiagramThumbnail;
