import React from 'react';
import TopicModeCard from './TopicModeCard';
import {
    isGrade10IndigenousBookkeepingTopic,
    isGrade10EthicsTopic,
    isGrade10GAAPTopic,
    isGrade10InternalControlsTopic,
    isGrade10SoleTraderTopic,
    isGrade10SalariesWagesTopic,
    isGrade10FinalAccountsTopic,
    isGrade10VATTopic,
} from '../topicMatchers';

const amberCard = 'mb-6 bg-amber-50 border border-amber-200 rounded-lg p-4';
const amberTitle = 'font-semibold text-amber-900';
const amberDescription = 'text-sm text-amber-800';
const amberScaffold = 'px-4 py-2 bg-amber-600 text-white rounded-lg font-semibold hover:bg-amber-700';
const amberPractice = 'px-4 py-2 bg-white text-amber-700 border border-amber-300 rounded-lg font-semibold hover:bg-amber-50';
const violetCard = 'mb-6 bg-violet-50 border border-violet-200 rounded-lg p-4';
const violetTitle = 'font-semibold text-violet-900';
const violetDescription = 'text-sm text-violet-800';
const violetScaffold = 'px-4 py-2 bg-violet-600 text-white rounded-lg font-semibold hover:bg-violet-700';
const violetPractice = 'px-4 py-2 bg-white text-violet-700 border border-violet-300 rounded-lg font-semibold hover:bg-violet-50';
const tealCard = 'mb-6 bg-teal-50 border border-teal-200 rounded-lg p-4';
const tealTitle = 'font-semibold text-teal-900';
const tealDescription = 'text-sm text-teal-800';
const tealScaffold = 'px-4 py-2 bg-teal-600 text-white rounded-lg font-semibold hover:bg-teal-700';
const tealPractice = 'px-4 py-2 bg-white text-teal-700 border border-teal-300 rounded-lg font-semibold hover:bg-teal-50';

const AccountingTopicModeCards = ({ selectedTopic, navigateToWorkspaceWithMode, flags }) => {
    const topicName = selectedTopic?.name;
    if (!topicName) return null;

    const cards = [
        {
            condition: flags.isGrade10Accounting && isGrade10IndigenousBookkeepingTopic(topicName),
            title: '1 Informal / Indigenous bookkeeping',
            description: 'Term 1. Differences between informal and formal bookkeeping; plan an informal business; compare systems using tables.',
            scaffoldMode: 'grade10_accounting_indigenous_scaffold',
            scaffoldLabel: 'Informal / Indigenous bookkeeping • Scaffold',
            practiceMode: 'grade10_accounting_indigenous_practice',
            practiceLabel: 'Informal / Indigenous bookkeeping • Practice',
        },
        {
            condition: flags.isGrade10Accounting && isGrade10EthicsTopic(topicName),
            title: '2 Ethics',
            description: 'Term 1. Code of ethics, principles (integrity, accountability, transparency, objectivity, etc.), and ethical leadership. Includes a matching-columns activity.',
            scaffoldMode: 'grade10_accounting_ethics_scaffold',
            scaffoldLabel: 'Ethics • Scaffold',
            practiceMode: 'grade10_accounting_ethics_practice',
            practiceLabel: 'Ethics • Practice',
        },
        {
            condition: flags.isGrade10Accounting && isGrade10GAAPTopic(topicName),
            title: '3 GAAP',
            description: 'Term 1. What GAAP is, why it matters, and the key principles (historical cost, prudence, materiality, business entity, going concern, matching). Includes matching-columns practice.',
            scaffoldMode: 'grade10_accounting_gaap_scaffold',
            scaffoldLabel: 'GAAP • Scaffold',
            practiceMode: 'grade10_accounting_gaap_practice',
            practiceLabel: 'GAAP • Practice',
        },
        {
            condition: flags.isGrade10Accounting && isGrade10InternalControlsTopic(topicName),
            title: '4 Internal Controls',
            description: 'Term 1. Define internal controls, understand the control process, and apply controls to stock, debtors, creditors, fixed assets, consumables, and cash (CRJ/CPJ/PCJ). Includes a delivery-service scenario.',
            scaffoldMode: 'grade10_accounting_internal_control_scaffold',
            scaffoldLabel: 'Internal Controls • Scaffold',
            practiceMode: 'grade10_accounting_internal_control_practice',
            practiceLabel: 'Internal Controls • Practice',
        },
        {
            condition: flags.isGrade10Accounting && isGrade10SoleTraderTopic(topicName),
            title: '5 Financial accounting and bookkeeping of a sole trader',
            description: 'Term 2. Core accounting concepts and the accounting equation, bookkeeping cycle, and subsidiary journals (CRJ/CPJ/DJ/DAJ/CJ/CAJ/PCJ/GJ). Includes interactive journal practice.',
            scaffoldMode: 'grade10_accounting_sole_trader_scaffold',
            scaffoldLabel: 'Financial accounting and bookkeeping of a sole trader • Scaffold',
            practiceMode: 'grade10_accounting_sole_trader_practice',
            practiceLabel: 'Financial accounting and bookkeeping of a sole trader • Practice',
        },
        {
            condition: flags.isGrade10Accounting && isGrade10VATTopic(topicName),
            title: '6 Value Added Tax (VAT)',
            description: 'Term 2. VAT at 15%, inclusive/exclusive calculations, classification of supplies (standard-rated, zero-rated, exempt). Tax evasion vs avoidance, ethical scenarios.',
            scaffoldMode: 'grade10_accounting_vat_scaffold',
            scaffoldLabel: 'Value Added Tax (VAT) • Scaffold',
            practiceMode: 'grade10_accounting_vat_practice',
            practiceLabel: 'Value Added Tax (VAT) • Practice',
            containerClassName: violetCard,
            titleClassName: violetTitle,
            descriptionClassName: violetDescription,
            scaffoldButtonClassName: violetScaffold,
            practiceButtonClassName: violetPractice,
        },
        {
            condition: flags.isGrade10Accounting && isGrade10SalariesWagesTopic(topicName),
            title: '7 Salaries & Wages Journal',
            description: 'Term 2. Salary scales, gross wage calculations (ordinary + overtime), PAYE, UIF, pension & medical aid deductions. Employer contributions (SDL, UIF). Complete salary and wage journals, post to General Ledger.',
            scaffoldMode: 'grade10_accounting_salaries_wages_scaffold',
            scaffoldLabel: 'Salaries & Wages Journal • Scaffold',
            practiceMode: 'grade10_accounting_salaries_wages_practice',
            practiceLabel: 'Salaries & Wages Journal • Practice',
            containerClassName: tealCard,
            titleClassName: tealTitle,
            descriptionClassName: tealDescription,
            scaffoldButtonClassName: tealScaffold,
            practiceButtonClassName: tealPractice,
        },
        {
            condition: flags.isGrade10Accounting && isGrade10FinalAccountsTopic(topicName),
            title: '8 Final Accounts & Year-end',
            description: 'Term 2. Closing transfers, depreciation (straight-line & diminishing balance), bad debts, year-end adjustments (accruals, prepayments, consumables), Trading & Profit and Loss accounts, Post-closing Trial Balance.',
            scaffoldMode: 'grade10_accounting_final_accounts_scaffold',
            scaffoldLabel: 'Final Accounts & Year-end • Scaffold',
            practiceMode: 'grade10_accounting_final_accounts_practice',
            practiceLabel: 'Final Accounts & Year-end • Practice',
            containerClassName: amberCard,
            titleClassName: amberTitle,
            descriptionClassName: amberDescription,
            scaffoldButtonClassName: amberScaffold,
            practiceButtonClassName: amberPractice,
        },
        {
            condition: flags.isGrade11Accounting,
            title: 'Grade 11 Accounting',
            description: 'Choose a mode to begin. Scaffold generates one question at a time with marking and hints; Practice generates a mixed set across Concepts, Fixed assets, Partnerships (ledger & balance sheet), Reconciliation, and Income Statement.',
            scaffoldMode: 'grade11_accounting_scaffold',
            scaffoldLabel: 'Grade 11 Accounting • Scaffold',
            practiceMode: 'grade11_accounting_practice',
            practiceLabel: 'Grade 11 Accounting • Practice',
            practiceButtonClassName: 'px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700',
        },
        {
            condition: flags.isGrade12Accounting,
            title: 'Grade 12 Accounting',
            description: 'Choose a mode to begin. Scaffold generates one question at a time with marking and hints; Practice generates a mixed set across Concepts, Audits/Governance/Shareholding, Company General Ledger, Financial Statements & Notes, Cash Flow, and Analysis & Interpretation.',
            scaffoldMode: 'grade12_accounting_scaffold',
            scaffoldLabel: 'Grade 12 Accounting • Scaffold',
            practiceMode: 'grade12_accounting_practice',
            practiceLabel: 'Grade 12 Accounting • Practice',
            practiceButtonClassName: 'px-4 py-2 bg-green-600 text-white rounded-lg font-semibold hover:bg-green-700',
        },
    ];

    const card = cards.find((entry) => entry.condition);
    if (!card) return null;

    return (
        <TopicModeCard
            title={card.title}
            description={card.description}
            onStartScaffold={() => navigateToWorkspaceWithMode(card.scaffoldMode, card.scaffoldLabel)}
            onStartPractice={() => navigateToWorkspaceWithMode(card.practiceMode, card.practiceLabel)}
            containerClassName={card.containerClassName}
            titleClassName={card.titleClassName}
            descriptionClassName={card.descriptionClassName}
            scaffoldButtonClassName={card.scaffoldButtonClassName}
            practiceButtonClassName={card.practiceButtonClassName}
        />
    );
};

export default AccountingTopicModeCards;
