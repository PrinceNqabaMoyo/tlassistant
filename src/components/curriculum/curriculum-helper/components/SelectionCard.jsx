import React from 'react';

const SelectionCard = ({
    title,
    description,
    icon: Icon,
    onSelect,
    color = 'bg-indigo-100',
    badge,
    locked,
    comingSoon,
    onLockedSelect,
}) => (
    <div
        onClick={locked ? onLockedSelect : comingSoon ? undefined : onSelect}
        className={`bg-white rounded-xl shadow-lg transform transition-all duration-300 overflow-hidden group relative ${
            locked || comingSoon ? 'cursor-not-allowed opacity-75' : 'cursor-pointer hover:shadow-2xl hover:-translate-y-2'
        }`}
    >
        <div className={`h-24 ${color} flex items-center justify-center relative`}>
            <Icon className="h-12 w-12 text-white/90 transition-transform duration-300 group-hover:scale-110" />
            {badge && (
                <span className={`absolute top-2 right-2 text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded-full shadow-sm ${
                    badge === 'Term 2'
                        ? 'bg-emerald-500 text-white'
                        : 'bg-blue-500 text-white'
                }`}>
                    {badge}
                </span>
            )}
            {locked && (
                <div className="absolute inset-0 bg-gray-900/40 flex items-center justify-center">
                    <span className="text-white text-sm font-bold flex items-center gap-1.5">
                        🔒 Upgrade
                    </span>
                </div>
            )}
        </div>
        <div className="p-6">
            <div className="mb-2 flex items-start justify-between gap-2">
                <h3 className="text-xl font-bold text-gray-800">{title}</h3>
                {comingSoon && (
                    <span className="shrink-0 rounded-full bg-amber-100 px-2 py-1 text-[10px] font-semibold uppercase tracking-[0.2em] text-amber-700">
                        Coming soon
                    </span>
                )}
            </div>
            <p className="text-gray-600 text-sm">{description}</p>
        </div>
    </div>
);

export default SelectionCard;
