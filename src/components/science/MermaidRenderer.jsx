import React, { useEffect, useRef, useState } from 'react';

const MermaidRenderer = ({ chart }) => {
    const containerRef = useRef(null);
    const [svgContent, setSvgContent] = useState('');

    useEffect(() => {
        if (window.mermaid) {
            window.mermaid.initialize({ startOnLoad: false, theme: 'default' });
            
            const renderChart = async () => {
                try {
                    const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`;
                    const { svg } = await window.mermaid.render(id, chart);
                    setSvgContent(svg);
                } catch (error) {
                    console.error("Mermaid rendering failed:", error);
                    setSvgContent(`<div class="text-red-500">Failed to render timeline/diagram</div>`);
                }
            };
            
            renderChart();
        }
    }, [chart]);

    return (
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200 overflow-x-auto">
            <h3 className="text-sm font-semibold text-gray-700 mb-2">Process / Timeline</h3>
            <div 
                ref={containerRef}
                dangerouslySetInnerHTML={{ __html: svgContent }} 
                className="flex justify-center"
            />
        </div>
    );
};

export default MermaidRenderer;
