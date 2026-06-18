import React from 'react';

/**
 * Shared MCQ radio-button option for consistent circular bullets.
 *
 * Props:
 *   selected  – boolean, is this option currently chosen
 *   onClick   – callback when the option is clicked
 *   label     – string, the option text
 *   disabled  – boolean (optional)
 */
const MCQOption = ({ selected, onClick, label, disabled }) => (
    <button
        type="button"
        onClick={onClick}
        disabled={disabled}
        className={`w-full flex items-center gap-3 text-left px-4 py-3 rounded-xl border transition-all duration-150
            ${selected
                ? 'bg-slate-50 border-slate-300 text-slate-900 shadow-sm'
                : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
            }
            ${disabled ? 'opacity-50 cursor-not-allowed' : 'cursor-pointer'}`}
    >
        {/* Radio indicator — always a perfect circle */}
        <span
            className={`inline-flex h-4 w-4 flex-shrink-0 rounded-full border items-center justify-center
                ${selected ? 'border-slate-600' : 'border-slate-300'}`}
            style={{ aspectRatio: '1' }}
        >
            {selected && <span className="h-2 w-2 rounded-full bg-slate-900" />}
        </span>
        <span className="text-sm font-medium">{label}</span>
    </button>
);

export default MCQOption;
