import React from 'react';
import { Briefcase, FileText } from 'lucide-react';
import SelectionCard from './SelectionCard';
import { topicColors, getTopicIcon, abbreviateSubjectName, formatGrade } from '../repositories';
import { canBypassComingSoon } from '../../../../app/constants/access';

const TopicListSection = ({
    selectedSubject,
    selectedGrade,
    onGoToClasswork,
    hasSyllabus,
    orderedTopicNames,
    currentUser,
    onTopicSelect,
    onLockedTopicSelect,
    getTopicCardTitle,
    getTopicTerm,
}) => (
    <>
        <div className="flex items-center justify-between mb-8">
            <h2 className="text-3xl font-bold text-gray-900">
                {abbreviateSubjectName(selectedSubject.name)} - {formatGrade(selectedGrade)} Topics
            </h2>
            {onGoToClasswork && (
                <button
                    onClick={onGoToClasswork}
                    className="flex items-center gap-2 px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 hover:border-gray-400 transition-colors duration-200 shadow-sm"
                >
                    <Briefcase size={16} />
                    <span>Class Assignments</span>
                </button>
            )}
        </div>
        {hasSyllabus && (
            <div className="bg-green-50 p-3 rounded-lg border border-green-200 text-green-800 text-sm mb-4 flex items-center">
                <FileText className="h-4 w-4 mr-2" />
                Syllabus available for this subject and grade.
            </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {orderedTopicNames.length > 0 ? orderedTopicNames.map((topicName, index) => {
                const cardColor = topicColors[index % topicColors.length];
                const cardIcon = getTopicIcon(topicName, selectedSubject.name);
                const termLabel = getTopicTerm(topicName);
                const isGradeLocked = (() => {
                    if (!currentUser) return false;
                    if (currentUser.isOwner) return false;
                    if (currentUser.subscriptionExpired) return true;
                    const grades = currentUser.subscribedGrades || [];
                    if (grades.length === 0) return true;
                    return !grades.includes(Number(selectedGrade));
                })();

                const normalizedTopic = String(topicName || '').trim().toLowerCase();
                const isAccounting = String(selectedSubject?.name || '').toLowerCase().trim() === 'accounting';
                let isComingSoon = false;

                if (isAccounting && String(selectedGrade).trim() === '10') {
                    isComingSoon = [
                        'budget',
                        'cost account',
                        'difference between',
                        'managing resource'
                    ].some(avail => normalizedTopic.includes(avail));
                } else if (isAccounting && String(selectedGrade).trim() === '11') {
                    const grade11Available = [
                        'ethic',
                        'internal control',
                        'bank recon',
                        'fixed tangible',
                        'partnership',
                        'analysis and interp',
                        'non profit',
                        'non-profit'
                    ];
                    isComingSoon = !grade11Available.some(avail => normalizedTopic.includes(avail));
                } else if (isAccounting && String(selectedGrade).trim() === '12') {
                    isComingSoon = true;
                } else if (!isAccounting) {
                    isComingSoon = true;
                }

                // Bypass all temporary blocks for owners/superadmins
                if (canBypassComingSoon(currentUser)) {
                    isComingSoon = false;
                }

                return (
                    <SelectionCard
                        key={topicName}
                        title={getTopicCardTitle(topicName)}
                        description={selectedSubject.topicsByGrade[selectedGrade]?.overview?.[topicName] || 'Click to explore this topic.'}
                        icon={cardIcon}
                        onSelect={() => onTopicSelect(topicName)}
                        onLockedSelect={onLockedTopicSelect}
                        color={cardColor}
                        badge={termLabel}
                        locked={isGradeLocked}
                        comingSoon={isComingSoon}
                    />
                );
            }) : (
                <p className="text-gray-600 col-span-full text-center">No topics available for this selection.</p>
            )}
        </div>
    </>
);

export default TopicListSection;
