import React from 'react';
import { ArrowRight } from 'lucide-react';

const TopicModeCard = ({
    title,
    description,
    onStartScaffold,
    onStartPractice,
    containerClassName = 'mb-6 bg-white border border-slate-200 rounded-2xl p-5 shadow-xs',
    titleClassName = 'font-bold text-slate-900 text-lg',
    descriptionClassName = 'text-xs sm:text-sm text-slate-600 mt-1 leading-relaxed',
}) => {
    const handleStart = onStartPractice || onStartScaffold;

    return (
        <div className={containerClassName}>
            <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div className="flex-1">
                    <h4 className={titleClassName}>{title}</h4>
                    <p className={descriptionClassName}>{description}</p>
                </div>
                <div className="shrink-0">
                    <button
                        type="button"
                        onClick={handleStart}
                        className="px-6 py-2.5 bg-brand-orange text-white rounded-xl font-bold shadow-ribbon hover:bg-brand-orangeDark transition active:scale-95 cursor-pointer flex items-center gap-2 text-sm"
                    >
                        <span>Start Practice</span>
                        <ArrowRight className="h-4 w-4" />
                    </button>
                </div>
            </div>
        </div>
    );
};

export default TopicModeCard;

