import React from 'react';

const EquationsInequalitiesVisualAids = () => {
    return (
        <div className="space-y-3">
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Balancing</div>
                <div className="text-sm text-gray-700 mt-1">
                    Whatever you do to one side of an equation, do to the other side.
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Inequalities</div>
                <div className="text-sm text-gray-700 mt-1">
                    If you multiply or divide by a negative number, reverse the inequality sign.
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Quadratics</div>
                <div className="text-sm text-gray-700 mt-1">
                    If (A)(B) = 0 then A = 0 or B = 0. Factorise then solve each factor.
                </div>
            </div>
        </div>
    );
};

export default EquationsInequalitiesVisualAids;
