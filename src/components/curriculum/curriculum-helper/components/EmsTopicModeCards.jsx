import React from 'react';
import TopicModeCard from './TopicModeCard';
import {
    isGrade7EMSMoneyNeeds,
    isGrade7EMSBusinesses,
    isGrade7EMSAccountingConcepts,
    isGrade7EMSIncomeExpenses,
    isGrade7EMSBudgets,
    isGrade7EMSEntrepreneurship,
} from '../topicMatchers';

const EmsTopicModeCards = ({ selectedTopic, navigateToWorkspaceWithMode, flags }) => {
    if (!flags.isGrade7EMS && flags.subject !== 'ems' && !(flags.isGrade7 && String(flags.subjectName || '').toLowerCase() === 'ems')) {
        return null;
    }

    const topicName = selectedTopic?.name || '';
    const isEmsTopic = isGrade7EMSMoneyNeeds(topicName) ||
        isGrade7EMSBusinesses(topicName) ||
        isGrade7EMSAccountingConcepts(topicName) ||
        isGrade7EMSIncomeExpenses(topicName) ||
        isGrade7EMSBudgets(topicName) ||
        isGrade7EMSEntrepreneurship(topicName);

    if (!isEmsTopic) return null;

    let scaffoldMode = null;
    let practiceMode = null;

    if (isGrade7EMSMoneyNeeds(topicName)) {
        scaffoldMode = 'grade7_ems_money_needs_scaffold';
        practiceMode = 'grade7_ems_money_needs_practice';
    } else if (isGrade7EMSBusinesses(topicName)) {
        scaffoldMode = 'grade7_ems_businesses_scaffold';
        practiceMode = 'grade7_ems_businesses_practice';
    } else if (isGrade7EMSAccountingConcepts(topicName)) {
        scaffoldMode = 'grade7_ems_accounting_concepts_scaffold';
        practiceMode = 'grade7_ems_accounting_concepts_practice';
    } else if (isGrade7EMSIncomeExpenses(topicName)) {
        scaffoldMode = 'grade7_ems_income_expenses_scaffold';
        practiceMode = 'grade7_ems_income_expenses_practice';
    } else if (isGrade7EMSBudgets(topicName)) {
        scaffoldMode = 'grade7_ems_budgets_scaffold';
        practiceMode = 'grade7_ems_budgets_practice';
    } else if (isGrade7EMSEntrepreneurship(topicName)) {
        scaffoldMode = 'grade7_ems_entrepreneurship_scaffold';
        practiceMode = 'grade7_ems_entrepreneurship_practice';
    }

    const cards = [
        {
            title: "Scaffold Mode",
            description: "Step-by-step guidance. Rich cell-level hints and teaching notes.",
            colorClass: "bg-blue-50 hover:bg-blue-100 border-blue-200",
            textColorClass: "text-blue-800",
            buttonClass: "bg-blue-500 hover:bg-blue-600",
            mode: scaffoldMode,
            label: 'Scaffold'
        },
        {
            title: "Practice Mode",
            description: "Test your skills without hints. Practice for exams.",
            colorClass: "bg-green-50 hover:bg-green-100 border-green-200",
            textColorClass: "text-green-800",
            buttonClass: "bg-green-500 hover:bg-green-600",
            mode: practiceMode,
            label: 'Practice'
        },
        {
            title: "Assessment Mode",
            description: "Full exam-length paper. Timed and graded without hints.",
            colorClass: "bg-purple-50 hover:bg-purple-100 border-purple-200",
            textColorClass: "text-purple-800",
            buttonClass: "bg-purple-500 hover:bg-purple-600",
            mode: 'grade7_ems_assessment',
            label: 'Assessment'
        }
    ];

    return (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
            {cards.map((card, index) => (
                <TopicModeCard
                    key={index}
                    title={card.title}
                    description={card.description}
                    colorClass={card.colorClass}
                    textColorClass={card.textColorClass}
                    buttonClass={card.buttonClass}
                    onStart={() => navigateToWorkspaceWithMode(card.mode, card.label)}
                    disabled={!card.mode}
                />
            ))}
        </div>
    );
};

export default EmsTopicModeCards;
