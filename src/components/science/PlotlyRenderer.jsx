import React, { useEffect, useRef } from 'react';

const PlotlyRenderer = ({ data, layout, config }) => {
    const chartRef = useRef(null);

    useEffect(() => {
        if (chartRef.current && window.Plotly) {
            window.Plotly.newPlot(chartRef.current, data, layout, config);
        }
        
        return () => {
            if (chartRef.current && window.Plotly) {
                window.Plotly.purge(chartRef.current);
            }
        };
    }, [data, layout, config]);

    return (
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <h3 className="text-sm font-semibold text-gray-700 mb-2">Graph View</h3>
            <div ref={chartRef} className="w-full h-[400px]" />
        </div>
    );
};

export default PlotlyRenderer;
