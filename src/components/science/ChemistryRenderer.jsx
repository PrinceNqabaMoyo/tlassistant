import React, { useEffect, useRef } from 'react';

const ChemistryRenderer = ({ smilesData }) => {
    const canvasRef = useRef(null);

    useEffect(() => {
        if (window.initRDKitModule) {
            window.initRDKitModule().then((RDKit) => {
                if (canvasRef.current && smilesData) {
                    const mol = RDKit.get_mol(smilesData);
                    if (mol) {
                        mol.draw_to_canvas_with_highlights(canvasRef.current, "{}");
                        mol.delete();
                    }
                }
            }).catch(e => console.error("RDKit init failed", e));
        }
    }, [smilesData]);

    return (
        <div className="bg-white p-4 rounded-lg shadow-sm border border-gray-200">
            <h3 className="text-sm font-semibold text-gray-700 mb-2">Molecular Structure</h3>
            <canvas ref={canvasRef} width={400} height={300} className="w-full max-w-full" />
        </div>
    );
};

export default ChemistryRenderer;
