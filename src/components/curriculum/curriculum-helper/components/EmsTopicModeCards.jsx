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

    return (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4 mb-8">
            <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs flex flex-col justify-between">
                <div>
                    <h4 className="font-bold text-slate-900 text-lg">EMS Practice &amp; Mastery</h4>
                    <p className="text-xs sm:text-sm text-slate-600 mt-1 leading-relaxed">
                        Interactive problem solving with dynamic, unfoldable double-entry guidance and transaction rules.
                    </p>
                </div>
                <div className="mt-4 flex justify-end">
                    <button
                        type="button"
                        onClick={() => navigateToWorkspaceWithMode(practiceMode || scaffoldMode, 'Practice & Mastery')}
                        className="px-6 py-2.5 bg-brand-orange text-white rounded-xl font-bold shadow-ribbon hover:bg-brand-orangeDark transition active:scale-95 cursor-pointer text-sm"
                    >
                        Start Practice →
                    </button>
                </div>
            </div>

            <div className="bg-white border border-slate-200 rounded-2xl p-5 shadow-xs flex flex-col justify-between">
                <div>
                    <h4 className="font-bold text-slate-900 text-lg">Timed Assessment</h4>
                    <p className="text-xs sm:text-sm text-slate-600 mt-1 leading-relaxed">
                        Official exam conditions with timed countdown, no hints, and post-exam diagnostic autopsy.
                    </p>
                </div>
                <div className="mt-4 flex justify-end">
                    <button
                        type="button"
                        onClick={() => navigateToWorkspaceWithMode('grade7_ems_assessment', 'Timed Assessment')}
                        className="px-6 py-2.5 bg-brand-blue text-white rounded-xl font-bold shadow-xs hover:bg-brand-cobalt transition active:scale-95 cursor-pointer text-sm"
                    >
                        Start Assessment ⏱️
                    </button>
                </div>
            </div>
        </div>
    );
};

export default EmsTopicModeCards;
