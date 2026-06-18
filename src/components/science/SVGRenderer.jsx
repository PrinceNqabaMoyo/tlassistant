import React from 'react';

const SVGRenderer = ({ svgString, title = "Diagram" }) => {
    return (
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200 flex flex-col items-center">
            {title && <h3 className="text-sm font-semibold text-gray-700 mb-2 w-full text-left">{title}</h3>}
            <div 
                className="max-w-full overflow-x-auto flex justify-center p-4"
                dangerouslySetInnerHTML={{ __html: svgString }} 
            />
        </div>
    );
};

export default SVGRenderer;
