import React from 'react';

const TopicModeCard = ({
    title,
    description,
    onStartScaffold,
    onStartPractice,
    containerClassName = 'mb-6 bg-indigo-50 border border-indigo-200 rounded-lg p-4',
    titleClassName = 'font-semibold text-indigo-900',
    descriptionClassName = 'text-sm text-indigo-800',
    scaffoldButtonClassName = 'px-4 py-2 bg-indigo-600 text-white rounded-lg font-semibold hover:bg-indigo-700',
    practiceButtonClassName = 'px-4 py-2 bg-white text-indigo-700 border border-indigo-300 rounded-lg font-semibold hover:bg-indigo-50',
}) => (
    <div className={containerClassName}>
        <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-3">
            <div>
                <h4 className={titleClassName}>{title}</h4>
                <p className={descriptionClassName}>{description}</p>
            </div>
            <div className="flex flex-col sm:flex-row gap-2">
                <button
                    onClick={onStartScaffold}
                    className={scaffoldButtonClassName}
                >
                    Start Scaffold
                </button>
                <button
                    onClick={onStartPractice}
                    className={practiceButtonClassName}
                >
                    Start Practice
                </button>
            </div>
        </div>
    </div>
);

export default TopicModeCard;
