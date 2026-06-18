import React from 'react';
import FeatureGatePanel from '../ui/FeatureGatePanel';
import { CLASS_ASSIGNMENTS_BLOCKED_MESSAGE } from '../../app/constants/access';

const ClassworkView = () => {
    return (
        <div className="p-4 sm:p-6 lg:p-8">
            <h1 className="text-3xl font-bold text-gray-800 mb-2">My Class Work</h1>
            <p className="text-gray-600 mb-8">Assignment workflows are not part of the current South Africa launch scope.</p>
            <FeatureGatePanel
                title="Class assignments"
                description={CLASS_ASSIGNMENTS_BLOCKED_MESSAGE}
                badge="Unavailable"
            />
        </div>
    );
};

export default ClassworkView;
