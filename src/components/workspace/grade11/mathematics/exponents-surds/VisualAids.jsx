import React from 'react';

const ExponentsSurdsVisualAids = () => {
    return (
        <div className="space-y-3">
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Exponent laws</div>
                <div className="text-sm text-gray-700 mt-1">
                    a^m·a^n = a^(m+n), a^m/a^n = a^(m−n), (a^m)^n = a^(mn), a^0 = 1, a^(−n) = 1/a^n.
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Rational exponents ↔ radicals</div>
                <div className="text-sm text-gray-700 mt-1">
                    a^(m/n) = (n√a)^m. For even roots, require a ≥ 0 when working in real numbers.
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Surds & rationalising</div>
                <div className="text-sm text-gray-700 mt-1">
                    Simplify by factoring out perfect squares. Rationalise denominators using a conjugate when needed.
                </div>
            </div>
            <div className="bg-white border border-gray-200 rounded-lg p-4">
                <div className="text-sm font-semibold text-gray-800">Applications of exponentials</div>
                <div className="text-sm text-gray-700 mt-1">
                    Exponential growth/decay often has the form A = A0·b^t (or A = A0·(1+r)^t).
                </div>
            </div>
        </div>
    );
};

export default ExponentsSurdsVisualAids;
