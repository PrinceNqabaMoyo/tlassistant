import React from 'react';
import Grade9EmsScaffold from '../grade9/ems/Grade9EmsScaffold';

const h = React.createElement;

// Wrapper to pass route props
const Grade9EmsRoute = ({ workspaceMode, ctx }) => {
    return h(Grade9EmsScaffold, { workspaceMode, ctx });
};

export const grade9EmsRegistry = {
    'grade9_ems_crj': {
        topic: 'crj',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_crj', ctx })
    },
    'grade9_ems_cpj': {
        topic: 'cpj',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_cpj', ctx })
    },
    'grade9_ems_general_ledger': {
        topic: 'general_ledger',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_general_ledger', ctx })
    },
    'grade9_ems_economic_systems': {
        topic: 'economic_systems',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_economic_systems', ctx })
    },
    'grade9_ems_debtors_journal': {
        topic: 'debtors_journal',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_debtors_journal', ctx })
    },
    'grade9_ems_price_theory': {
        topic: 'price_theory',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_price_theory', ctx })
    },
    'grade9_ems_creditors_journal': {
        topic: 'creditors_journal',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_creditors_journal', ctx })
    },
    'grade9_ems_debtors_ledger': {
        topic: 'debtors_ledger',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_debtors_ledger', ctx })
    },
    'grade9_ems_business_functions': {
        topic: 'business_functions',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_business_functions', ctx })
    },
    'grade9_ems_assessment': {
        topic: 'assessment',
        render: (ctx) => h(Grade9EmsRoute, { workspaceMode: 'grade9_ems_assessment', ctx })
    }
};
