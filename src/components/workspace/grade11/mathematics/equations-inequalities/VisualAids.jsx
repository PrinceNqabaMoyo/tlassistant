import React from 'react';

const EquationsInequalitiesVisualAids = () => {
    return (
        <div className="space-y-3">
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Quadratics</div>
                <div className="text-sm text-gray-700 mt-1">
                    Use completing the square or the quadratic formula. Use a sign chart for quadratic inequalities.
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Quadratic formula</div>
                <div className="text-sm text-gray-700 mt-1">
                    x = (−b ± √(b^2 − 4ac)) / (2a)
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Simultaneous equations</div>
                <div className="text-sm text-gray-700 mt-1">
                    Use elimination or substitution. Always check the solution in both equations.
                </div>
            </div>
        </div>
    );
};

export default EquationsInequalitiesVisualAids;
