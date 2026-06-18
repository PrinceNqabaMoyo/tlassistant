import React from 'react';

const Trigonometry1VisualAids = () => {
    return (
        <div className="space-y-3">
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">SOHCAHTOA</div>
                <div className="text-sm text-gray-700 mt-1">
                    sin θ = opp/hyp, cos θ = adj/hyp, tan θ = opp/adj
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Special angles</div>
                <div className="text-sm text-gray-700 mt-1">
                    30°, 45°, 60° have exact values (use √2 and √3).
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Calculator</div>
                <div className="text-sm text-gray-700 mt-1">
                    Make sure you are in degrees mode. Use inverse keys for angles (sin⁻¹, cos⁻¹, tan⁻¹).
                </div>
            </div>
        </div>
    );
};

export default Trigonometry1VisualAids;
