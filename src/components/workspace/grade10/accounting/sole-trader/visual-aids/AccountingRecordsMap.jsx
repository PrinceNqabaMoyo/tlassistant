import React, { useEffect, useMemo, useState } from 'react';

const RECORDS = [
    {
        id: 'source_documents',
        label: 'Source documents',
        summary: 'Original proof that a transaction happened.',
        purpose: 'Provide the first evidence of a transaction before it is classified into the books.',
        usedWhen: 'A transaction first occurs and the learner must decide what happened and which record should be updated next.',
        comesFrom: 'Customers, suppliers, the bank, the owner, or an internal correction event.',
        flowsTo: 'The relevant subsidiary journal or the General Journal.',
        howToRead: [
            'Start with the document name and date.',
            'Identify whether the transaction is cash, credit, return, allowance, petty cash, or adjustment.',
            'Use the details and amount to decide the next book of entry.',
        ],
        deductions: [
            'Which journal should record the transaction.',
            'Which amount should be posted or analysed.',
            'Whether the event affects cash, debtors, creditors, stock, or expenses.',
        ],
        commonMistakes: [
            'Choosing a journal from memory without checking whether the transaction is cash or credit.',
            'Ignoring document clues such as invoice, receipt, credit note, or journal voucher.',
        ],
        hotspots: [
            {
                id: 'document-name',
                label: 'Document type',
                title: 'Document type',
                text: 'The name of the source document is the biggest clue for what kind of transaction happened and which journal may be used next.',
            },
            {
                id: 'document-amount',
                label: 'Amount',
                title: 'Amount',
                text: 'The amount becomes the value recorded in the journal and later posted into accounts.',
            },
            {
                id: 'document-reference',
                label: 'Reference',
                title: 'Reference',
                text: 'A document number helps match the evidence to the journal entry and later to postings or checks.',
            },
        ],
    },
    {
        id: 'journals',
        label: 'Subsidiary journals',
        summary: 'The books of first entry where transactions are classified.',
        purpose: 'Record transactions in the correct journal before they are posted into ledger accounts.',
        usedWhen: 'After the source document is read and the learner knows the transaction type.',
        comesFrom: 'Source documents such as invoices, receipts, debit notes, credit notes, and journal vouchers.',
        flowsTo: 'General Ledger, Debtors Ledger, Creditors Ledger, and control accounts through posting.',
        howToRead: [
            'Check the journal heading first so you know the kind of transaction being recorded.',
            'Read the details column to identify the account or person affected.',
            'Use folio and analysis columns to understand where totals or entries move next.',
        ],
        deductions: [
            'Which ledger account must be posted next.',
            'Which source document supports the entry.',
            'Whether an entry affects a control account, personal account, or expense/income account.',
        ],
        commonMistakes: [
            'Mixing up cash journals with credit journals.',
            'Treating the folio as an amount or ignoring what the analysis column means.',
        ],
        hotspots: [
            {
                id: 'journal-details',
                label: 'Details',
                title: 'Details column',
                text: 'The details column tells you which account, debtor, creditor, or item is being recorded. It often helps you identify the contra account later.',
            },
            {
                id: 'journal-folio',
                label: 'Fol.',
                title: 'Folio',
                text: 'The folio shows the account or book reference used for posting or cross-reference.',
            },
            {
                id: 'journal-analysis',
                label: 'Analysis',
                title: 'Analysis / amount',
                text: 'The amount column is the value that moves into accounts. In some journals, the analysis column also reveals the category affected.',
            },
        ],
    },
    {
        id: 'ledgers',
        label: 'Ledger accounts',
        summary: 'Where transactions are classified account by account.',
        purpose: 'Collect entries belonging to the same account so the running balance of that account can be known.',
        usedWhen: 'After journal entries are posted into the correct General Ledger, Debtors Ledger, or Creditors Ledger accounts.',
        comesFrom: 'Subsidiary journals, the General Journal, and opening balances.',
        flowsTo: 'Trial Balance, control accounts, list totals, and adjustment work.',
        howToRead: [
            'Identify the account name first.',
            'Check whether an amount is on the debit or credit side.',
            'Compare entries and totals to see the balance carried down and brought down.',
        ],
        deductions: [
            'Whether the account has a debit or credit balance.',
            'Which journal supplied the posting.',
            'Which balance should appear later in the Trial Balance or control comparison.',
        ],
        commonMistakes: [
            'Reading left and right sides without checking whether the account is an asset, liability, expense, income, or equity item.',
            'Confusing the personal ledger with the control account total.',
        ],
        hotspots: [
            {
                id: 'ledger-detail',
                label: 'Details',
                title: 'Details / contra account',
                text: 'The detail usually shows the other account or journal total involved in the double entry.',
            },
            {
                id: 'ledger-folio',
                label: 'Fol.',
                title: 'Ledger folio',
                text: 'The folio helps track where the entry came from or where it was posted.',
            },
            {
                id: 'ledger-balance',
                label: 'Balance',
                title: 'Balance c/d and b/d',
                text: 'The balance carried down closes the period; the balance brought down opens the next one and is the figure that often appears in later summaries.',
            },
        ],
    },
    {
        id: 'control_accounts',
        label: 'Control accounts',
        summary: 'Summary accounts for all debtors or all creditors together.',
        purpose: 'Show the total amount owed by debtors or owed to creditors in one account for checking and reporting.',
        usedWhen: 'When total debtors or total creditors must be summarised, analysed, or checked against the list.',
        comesFrom: 'Opening list totals, relevant journals, General Journal entries, petty cash items, and period-end balancing.',
        flowsTo: 'Verification against the Debtors/Creditors list and later to the Trial Balance.',
        howToRead: [
            'Identify whether it is Debtors control or Creditors control.',
            'Track the opening balance, the monthly movements, and the closing balance.',
            'Match specific entries to journals, source documents, and reasons.',
        ],
        deductions: [
            'Opening amount owed.',
            'Contra account for a named amount.',
            'Source document or reason for a posting.',
            'Closing balance and how it should be verified against the list.',
        ],
        commonMistakes: [
            'Treating the control account like a single personal account instead of a total summary.',
            'Forgetting that the closing control balance must agree with the relevant list total.',
        ],
        hotspots: [
            {
                id: 'control-opening',
                label: 'Opening balance',
                title: 'Opening balance',
                text: 'The opening balance usually comes from the previous period or from the net total of the debtors or creditors list.',
            },
            {
                id: 'control-journal-entry',
                label: 'Journal entry',
                title: 'Journal-linked entry',
                text: 'A named entry such as DAJ, CRJ, CJ, CAJ, GJ, or PCJ helps the learner deduce the source document, contra account, and reason.',
            },
            {
                id: 'control-closing',
                label: 'Closing balance',
                title: 'Closing balance',
                text: 'The closing balance is the figure that must be compared to the final list total to confirm that the control account agrees with subsidiary records.',
            },
        ],
    },
    {
        id: 'lists',
        label: 'Debtors / creditors lists',
        summary: 'Lists of individual balances in subsidiary records.',
        purpose: 'Show the balances of each debtor or creditor separately so the total can be checked against the control account.',
        usedWhen: 'At the beginning or end of a period when the total of personal accounts must be summarised or verified.',
        comesFrom: 'Debtors Ledger and Creditors Ledger personal accounts.',
        flowsTo: 'Control-account verification and in some questions to Trial Balance support.',
        howToRead: [
            'Add or compare the individual balances carefully.',
            'Check whether the list is an opening list or a closing list.',
            'Use the total to verify the control account.',
        ],
        deductions: [
            'Net amount owed by or to the group.',
            'Whether the control account agrees with subsidiary records.',
            'Whether an opening balance or closing balance can be derived.',
        ],
        commonMistakes: [
            'Using the list without checking the date.',
            'Comparing the wrong list total to the wrong control-account balance.',
        ],
        hotspots: [
            {
                id: 'list-individual',
                label: 'Individual balances',
                title: 'Individual balances',
                text: 'These balances come from separate personal accounts and explain what makes up the control total.',
            },
            {
                id: 'list-total',
                label: 'List total',
                title: 'List total',
                text: 'The total is the comparison point for the control account. In many questions it helps derive the opening or closing amount owed.',
            },
        ],
    },
    {
        id: 'trial_balance',
        label: 'Trial Balance',
        summary: 'A summary of ledger balances used to test equality and prepare reporting.',
        purpose: 'Bring together balances from accounts so total debits can be compared to total credits.',
        usedWhen: 'After posting and balancing accounts, before final reporting or after month-update work.',
        comesFrom: 'General Ledger balances and control balances, and sometimes list-supported control totals.',
        flowsTo: 'Adjustments, notes, and financial statements.',
        howToRead: [
            'Identify the account name, folio, and whether the balance belongs in debit or credit.',
            'Check section placement where applicable.',
            'Use totals to confirm the statement is balanced.',
        ],
        deductions: [
            'Whether an account is in the correct debit or credit column.',
            'Which balances must still be transferred after transactions or corrections.',
            'Whether totals agree and whether a control balance is correctly placed.',
        ],
        commonMistakes: [
            'Moving balances from ledgers without checking whether they are debit or credit balances.',
            'Treating Trial Balance like a ledger instead of a summary statement.',
        ],
        hotspots: [
            {
                id: 'tb-account',
                label: 'Account',
                title: 'Account column',
                text: 'This names the account whose final balance is being transferred from the ledger to the Trial Balance.',
            },
            {
                id: 'tb-folio',
                label: 'Fol.',
                title: 'Folio column',
                text: 'The folio can test posting/reference knowledge, but it is not the main learning focus in every Trial Balance question.',
            },
            {
                id: 'tb-totals',
                label: 'Totals',
                title: 'Totals row',
                text: 'If the Trial Balance is correct, total debits and credits should agree after all balances are placed correctly.',
            },
        ],
    },
    {
        id: 'notes_adjustments',
        label: 'Notes and adjustments',
        summary: 'Extra calculations and corrections used before final reporting.',
        purpose: 'Explain adjustments, calculations, and note disclosures that refine the reporting figures.',
        usedWhen: 'After the initial Trial Balance when adjustments such as accrued expenses, prepaid expenses, depreciation, or stock notes are needed.',
        comesFrom: 'Trial Balance, additional information, inventory counts, and period-end decisions.',
        flowsTo: 'Adjusted Trial Balance and financial statements.',
        howToRead: [
            'Read the note heading and the additional information together.',
            'Identify which amount is original, which is adjustment, and which becomes the final figure.',
            'Connect the note result back to the relevant account or statement section.',
        ],
        deductions: [
            'What must be added, subtracted, or reclassified.',
            'Which account balance changes before final statements.',
            'How a note explains a final statement figure.',
        ],
        commonMistakes: [
            'Changing the final statement figure without showing how the adjustment was derived.',
            'Treating every extra note as a completely separate topic instead of part of the reporting flow.',
        ],
        hotspots: [
            {
                id: 'note-base',
                label: 'Opening figure',
                title: 'Starting figure',
                text: 'Most notes begin with a balance or value already known from earlier records before adjustments are applied.',
            },
            {
                id: 'note-adjustment',
                label: 'Adjustment',
                title: 'Adjustment line',
                text: 'This line explains what changed and why the original balance is no longer enough on its own.',
            },
        ],
    },
    {
        id: 'financial_statements',
        label: 'Financial statements',
        summary: 'The final reported view of performance and position.',
        purpose: 'Present the final results of the accounting cycle in a structured reporting format.',
        usedWhen: 'After balances and adjustments are finalised for the period.',
        comesFrom: 'Adjusted Trial Balance, notes, and final calculated balances.',
        flowsTo: 'Decision-making and performance/position analysis.',
        howToRead: [
            'Read the statement title and period first.',
            'Check which section each figure belongs to.',
            'Understand that these figures are the end of a chain built from earlier records.',
        ],
        deductions: [
            'Where a final figure originated in the cycle.',
            'Which section an amount belongs to.',
            'How adjustments changed the reported result or position.',
        ],
        commonMistakes: [
            'Treating final statements as isolated facts instead of the end result of postings, balances, and adjustments.',
            'Ignoring the connection between statement items and the supporting notes or Trial Balance figures.',
        ],
        hotspots: [
            {
                id: 'fs-section',
                label: 'Section heading',
                title: 'Section heading',
                text: 'A section heading tells the learner what category of information belongs underneath and helps prevent misplacement of figures.',
            },
            {
                id: 'fs-final-figure',
                label: 'Final figure',
                title: 'Final figure',
                text: 'A final figure should always be explainable by tracing it backwards through notes, Trial Balance, ledgers, journals, and source documents.',
            },
        ],
    },
];

const FLOW = [
    { from: 'source_documents', to: 'journals', label: 'record first entry' },
    { from: 'journals', to: 'ledgers', label: 'post entries' },
    { from: 'ledgers', to: 'control_accounts', label: 'summarise totals' },
    { from: 'ledgers', to: 'lists', label: 'build individual balances' },
    { from: 'control_accounts', to: 'lists', label: 'verify totals' },
    { from: 'control_accounts', to: 'trial_balance', label: 'transfer balance' },
    { from: 'ledgers', to: 'trial_balance', label: 'extract balances' },
    { from: 'trial_balance', to: 'notes_adjustments', label: 'adjust and explain' },
    { from: 'notes_adjustments', to: 'financial_statements', label: 'report final figures' },
];

const SUBSKILL_FOCUS = {
    concepts: { primary: 'source_documents', highlighted: ['source_documents', 'journals', 'ledgers'] },
    equation: { primary: 'source_documents', highlighted: ['source_documents', 'journals', 'ledgers'] },
    crj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers'] },
    cpj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers'] },
    dj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers', 'control_accounts', 'lists'] },
    daj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers', 'control_accounts', 'lists'] },
    cj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers', 'control_accounts', 'lists'] },
    caj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers', 'control_accounts', 'lists'] },
    pcj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers', 'control_accounts'] },
    gj: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers', 'control_accounts', 'trial_balance'] },
    general_ledger: { primary: 'ledgers', highlighted: ['journals', 'ledgers', 'trial_balance'] },
    debtors_ledger: { primary: 'ledgers', highlighted: ['journals', 'ledgers', 'control_accounts', 'lists'] },
    creditors_ledger: { primary: 'ledgers', highlighted: ['journals', 'ledgers', 'control_accounts', 'lists'] },
    trading_stock_account: { primary: 'ledgers', highlighted: ['source_documents', 'journals', 'ledgers', 'trial_balance'] },
    control_accounts: { primary: 'control_accounts', highlighted: ['journals', 'ledgers', 'control_accounts', 'lists', 'trial_balance'] },
    control_accounts_reconciliation: { primary: 'lists', highlighted: ['ledgers', 'control_accounts', 'lists'] },
    reconciliation_analysis: { primary: 'lists', highlighted: ['ledgers', 'control_accounts', 'lists'] },
    trial_balance: { primary: 'trial_balance', highlighted: ['ledgers', 'control_accounts', 'lists', 'trial_balance', 'notes_adjustments'] },
    full_accounting_cycle_bookkeeping: { primary: 'financial_statements', highlighted: RECORDS.map((record) => record.id) },
    journals: { primary: 'journals', highlighted: ['source_documents', 'journals', 'ledgers'] },
    mixed: { primary: 'source_documents', highlighted: RECORDS.map((record) => record.id) },
};

const RECORDS_BY_ID = Object.fromEntries(RECORDS.map((record) => [record.id, record]));

const tableStyle = { width: '100%', borderCollapse: 'collapse', tableLayout: 'fixed' };
const headerCellStyle = { border: '1px solid #000', background: '#e5e7eb', fontWeight: 600, textAlign: 'center', padding: '6px', fontSize: '0.75rem' };
const bodyCellStyle = { border: '1px solid #000', padding: '6px', fontSize: '0.75rem', verticalAlign: 'middle' };
const amountCellStyle = { ...bodyCellStyle, fontFamily: 'ui-monospace, monospace', textAlign: 'right', paddingRight: '6px' };
const spineCellStyle = { borderLeft: '3px solid #000', borderRight: '3px solid #000', background: '#fff', width: '10px', minWidth: '10px', padding: 0 };

const formatLabel = (value) => String(value || '').replace(/_/g, ' ').replace(/\b\w/g, (char) => char.toUpperCase());

const getFocusPreset = (subskill) => {
    const key = String(subskill || 'mixed').trim().toLowerCase();
    return SUBSKILL_FOCUS[key] || SUBSKILL_FOCUS.mixed;
};

const JournalReplica = () => (
    <div className="overflow-x-auto">
        <table style={tableStyle}>
            <thead>
                <tr>
                    <th style={headerCellStyle}>Date</th>
                    <th style={headerCellStyle}>Details</th>
                    <th style={headerCellStyle}>Fol.</th>
                    <th style={headerCellStyle}>Analysis</th>
                    <th style={headerCellStyle}>Bank</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style={bodyCellStyle}>24 Apr</td>
                    <td style={bodyCellStyle}>A. Dlamini</td>
                    <td style={bodyCellStyle}>DL</td>
                    <td style={amountCellStyle}>1 280</td>
                    <td style={amountCellStyle}>1 280</td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>24 Apr</td>
                    <td style={bodyCellStyle}>Discount allowed</td>
                    <td style={bodyCellStyle}>G7</td>
                    <td style={amountCellStyle}>120</td>
                    <td style={amountCellStyle}>0</td>
                </tr>
            </tbody>
        </table>
    </div>
);

const LedgerReplica = () => (
    <div className="overflow-x-auto">
        <table style={tableStyle}>
            <thead>
                <tr>
                    <th style={headerCellStyle} colSpan={4}>Dr. Debtors Control</th>
                    <th style={spineCellStyle} />
                    <th style={headerCellStyle} colSpan={4}>Cr.</th>
                </tr>
                <tr>
                    <th style={headerCellStyle}>Date</th>
                    <th style={headerCellStyle}>Details</th>
                    <th style={headerCellStyle}>Fol.</th>
                    <th style={headerCellStyle}>Amount</th>
                    <th style={spineCellStyle} />
                    <th style={headerCellStyle}>Date</th>
                    <th style={headerCellStyle}>Details</th>
                    <th style={headerCellStyle}>Fol.</th>
                    <th style={headerCellStyle}>Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style={bodyCellStyle}>1 Apr</td>
                    <td style={bodyCellStyle}>Balance b/d</td>
                    <td style={bodyCellStyle}>B7</td>
                    <td style={amountCellStyle}>13 680</td>
                    <td style={spineCellStyle} />
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Bank</td>
                    <td style={bodyCellStyle}>CRJ</td>
                    <td style={amountCellStyle}>12 000</td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Sales</td>
                    <td style={bodyCellStyle}>DJ</td>
                    <td style={amountCellStyle}>18 200</td>
                    <td style={spineCellStyle} />
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Balance c/d</td>
                    <td style={bodyCellStyle}>B7</td>
                    <td style={amountCellStyle}>10 080</td>
                </tr>
            </tbody>
        </table>
    </div>
);

const ControlAccountReplica = () => (
    <div className="overflow-x-auto">
        <table style={tableStyle}>
            <thead>
                <tr>
                    <th style={headerCellStyle} colSpan={4}>Dr. Debtors Control</th>
                    <th style={spineCellStyle} />
                    <th style={headerCellStyle} colSpan={4}>Cr.</th>
                </tr>
                <tr>
                    <th style={headerCellStyle}>Date</th>
                    <th style={headerCellStyle}>Details</th>
                    <th style={headerCellStyle}>Fol.</th>
                    <th style={headerCellStyle}>Amount</th>
                    <th style={spineCellStyle} />
                    <th style={headerCellStyle}>Date</th>
                    <th style={headerCellStyle}>Details</th>
                    <th style={headerCellStyle}>Fol.</th>
                    <th style={headerCellStyle}>Amount</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style={bodyCellStyle}>1 Apr</td>
                    <td style={bodyCellStyle}>Balance b/d</td>
                    <td style={bodyCellStyle}>B7</td>
                    <td style={amountCellStyle}>13 680</td>
                    <td style={spineCellStyle} />
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Debtors allowances</td>
                    <td style={bodyCellStyle}>DAJ</td>
                    <td style={amountCellStyle}>3 100</td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Sales</td>
                    <td style={bodyCellStyle}>DJ</td>
                    <td style={amountCellStyle}>18 200</td>
                    <td style={spineCellStyle} />
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Bank</td>
                    <td style={bodyCellStyle}>CRJ</td>
                    <td style={amountCellStyle}>12 000</td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Journal debits</td>
                    <td style={bodyCellStyle}>GJ</td>
                    <td style={amountCellStyle}>840</td>
                    <td style={spineCellStyle} />
                    <td style={bodyCellStyle}>30 Apr</td>
                    <td style={bodyCellStyle}>Balance c/d</td>
                    <td style={bodyCellStyle}>B7</td>
                    <td style={amountCellStyle}>10 080</td>
                </tr>
            </tbody>
        </table>
    </div>
);

const ListReplica = () => (
    <div className="overflow-x-auto">
        <table style={tableStyle}>
            <thead>
                <tr>
                    <th style={headerCellStyle}>Debtor</th>
                    <th style={headerCellStyle}>Balance</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style={bodyCellStyle}>A. Dlamini</td>
                    <td style={amountCellStyle}>4 300</td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>M. Ndlovu</td>
                    <td style={amountCellStyle}>3 780</td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>S. Khumalo</td>
                    <td style={amountCellStyle}>2 000</td>
                </tr>
                <tr>
                    <td style={{ ...bodyCellStyle, borderTop: '2px solid #000', fontWeight: 600, textDecoration: 'underline' }}>Total</td>
                    <td style={{ ...amountCellStyle, borderTop: '2px solid #000', fontWeight: 600, textDecoration: 'underline' }}>10 080</td>
                </tr>
            </tbody>
        </table>
    </div>
);

const TrialBalanceReplica = () => (
    <div className="overflow-x-auto">
        <table style={tableStyle}>
            <thead>
                <tr>
                    <th style={headerCellStyle}>Account</th>
                    <th style={headerCellStyle}>Fol.</th>
                    <th style={headerCellStyle}>Debit</th>
                    <th style={headerCellStyle}>Credit</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td style={bodyCellStyle}>Bank</td>
                    <td style={bodyCellStyle}>B1</td>
                    <td style={amountCellStyle}>24 580</td>
                    <td style={amountCellStyle}></td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>Debtors Control</td>
                    <td style={bodyCellStyle}>B7</td>
                    <td style={amountCellStyle}>10 080</td>
                    <td style={amountCellStyle}></td>
                </tr>
                <tr>
                    <td style={bodyCellStyle}>Creditors Control</td>
                    <td style={bodyCellStyle}>B8</td>
                    <td style={amountCellStyle}></td>
                    <td style={amountCellStyle}>12 270</td>
                </tr>
            </tbody>
        </table>
    </div>
);

const NotesReplica = () => (
    <div className="space-y-2">
        <div className="rounded-lg border border-gray-200 bg-gray-50 p-3">
            <div className="text-sm font-semibold text-gray-900">Adjustment note</div>
            <div className="mt-1 text-xs text-gray-700">Opening figure: Trading stock on hand</div>
            <div className="text-xs text-gray-700">Adjustment: Add closing stock from stock count</div>
            <div className="text-xs text-gray-700">Final use: Statement / note disclosure</div>
        </div>
        <div className="rounded-lg border border-gray-200 bg-white p-3 text-xs text-gray-700">
            Notes explain how a final reporting figure was built from an earlier balance plus additional information.
        </div>
    </div>
);

const SourceDocumentReplica = () => (
    <div className="grid gap-3 md:grid-cols-2">
        <div className="rounded-xl border border-gray-200 bg-white p-3">
            <div className="text-xs font-semibold uppercase tracking-wide text-gray-500">Invoice</div>
            <div className="mt-2 text-sm font-semibold text-gray-900">Duplicate invoice</div>
            <div className="mt-1 text-xs text-gray-700">Customer: A. Dlamini</div>
            <div className="text-xs text-gray-700">Goods sold on credit</div>
            <div className="text-xs font-semibold text-gray-900 mt-2">R1 280</div>
        </div>
        <div className="rounded-xl border border-gray-200 bg-white p-3">
            <div className="text-xs font-semibold uppercase tracking-wide text-gray-500">Credit note</div>
            <div className="mt-2 text-sm font-semibold text-gray-900">Debtors allowance</div>
            <div className="mt-1 text-xs text-gray-700">Goods returned / overcharge corrected</div>
            <div className="text-xs font-semibold text-gray-900 mt-2">R320</div>
        </div>
    </div>
);

const FinancialStatementReplica = () => (
    <div className="space-y-2">
        <div className="rounded-lg border border-gray-200 bg-white p-3">
            <div className="text-sm font-semibold text-gray-900">Statement of financial position</div>
            <div className="mt-2 grid grid-cols-2 gap-2 text-xs text-gray-700">
                <div>Assets</div>
                <div className="text-right font-mono">R86 200</div>
                <div>Owner’s equity</div>
                <div className="text-right font-mono">R53 700</div>
                <div>Liabilities</div>
                <div className="text-right font-mono">R32 500</div>
            </div>
        </div>
        <div className="rounded-lg border border-gray-200 bg-gray-50 p-3 text-xs text-gray-700">
            Every final figure should be traceable backwards to notes, Trial Balance balances, ledger postings, journals, and source documents.
        </div>
    </div>
);

const renderReplica = (recordId) => {
    switch (recordId) {
    case 'source_documents':
        return <SourceDocumentReplica />;
    case 'journals':
        return <JournalReplica />;
    case 'ledgers':
        return <LedgerReplica />;
    case 'control_accounts':
        return <ControlAccountReplica />;
    case 'lists':
        return <ListReplica />;
    case 'trial_balance':
        return <TrialBalanceReplica />;
    case 'notes_adjustments':
        return <NotesReplica />;
    case 'financial_statements':
        return <FinancialStatementReplica />;
    default:
        return null;
    }
};

const AccountingRecordsMap = ({ currentSubskill }) => {
    const focusPreset = useMemo(() => getFocusPreset(currentSubskill), [currentSubskill]);
    const [selectedRecordId, setSelectedRecordId] = useState(focusPreset.primary);
    const selectedRecord = RECORDS_BY_ID[selectedRecordId] || RECORDS[0];
    const [selectedHotspotId, setSelectedHotspotId] = useState(selectedRecord?.hotspots?.[0]?.id || null);

    useEffect(() => {
        setSelectedRecordId(focusPreset.primary);
    }, [focusPreset.primary]);

    useEffect(() => {
        const hotspotIds = Array.isArray(selectedRecord?.hotspots) ? selectedRecord.hotspots.map((hotspot) => hotspot.id) : [];
        if (!hotspotIds.includes(selectedHotspotId)) {
            setSelectedHotspotId(hotspotIds[0] || null);
        }
    }, [selectedRecord, selectedHotspotId]);

    const selectedHotspot = (selectedRecord?.hotspots || []).find((hotspot) => hotspot.id === selectedHotspotId) || selectedRecord?.hotspots?.[0] || null;
    const highlightedSet = new Set(focusPreset.highlighted || []);
    const currentSubskillLabel = formatLabel(currentSubskill || 'mixed');

    return (
        <div className="space-y-4">
            <div className="rounded-xl border border-indigo-100 bg-indigo-50/70 p-4">
                <div className="flex flex-wrap items-start justify-between gap-3">
                    <div>
                        <div className="text-sm font-semibold text-indigo-900">Interactive accounting-records map</div>
                        <div className="mt-1 text-sm text-indigo-800">
                            Follow how information moves from evidence to recording, posting, checking, adjustment, and final reporting.
                        </div>
                    </div>
                    <div className="inline-flex items-center rounded-full border border-indigo-200 bg-white px-3 py-1 text-xs font-semibold text-indigo-700">
                        Current subskill focus: {currentSubskillLabel}
                    </div>
                </div>
            </div>

            <div className="rounded-xl border border-gray-200 bg-white p-4">
                <div className="text-sm font-semibold text-gray-900">Flow map</div>
                <div className="mt-3 flex flex-wrap items-center gap-2">
                    {RECORDS.map((record, index) => {
                        const isSelected = record.id === selectedRecordId;
                        const isFocused = highlightedSet.has(record.id);
                        return (
                            <React.Fragment key={record.id}>
                                <button
                                    type="button"
                                    onClick={() => setSelectedRecordId(record.id)}
                                    className={`rounded-xl border px-3 py-2 text-left transition-colors ${isSelected ? 'border-indigo-500 bg-indigo-600 text-white shadow-sm' : isFocused ? 'border-indigo-200 bg-indigo-50 text-indigo-900' : 'border-gray-200 bg-gray-50 text-gray-700 hover:bg-white'}`}
                                >
                                    <div className="text-sm font-semibold">{record.label}</div>
                                    <div className={`mt-1 text-xs ${isSelected ? 'text-indigo-100' : isFocused ? 'text-indigo-700' : 'text-gray-500'}`}>{record.summary}</div>
                                </button>
                                {index < RECORDS.length - 1 && (
                                    <div className="text-xs font-semibold text-gray-400">→</div>
                                )}
                            </React.Fragment>
                        );
                    })}
                </div>
                <div className="mt-4 flex flex-wrap gap-2">
                    {FLOW.map((link) => {
                        const linkActive = selectedRecordId === link.from || selectedRecordId === link.to || (highlightedSet.has(link.from) && highlightedSet.has(link.to));
                        return (
                            <div
                                key={`${link.from}-${link.to}`}
                                className={`rounded-full border px-3 py-1 text-xs ${linkActive ? 'border-indigo-200 bg-indigo-50 text-indigo-800' : 'border-gray-200 bg-white text-gray-500'}`}
                            >
                                {RECORDS_BY_ID[link.from]?.label} → {RECORDS_BY_ID[link.to]?.label} · {link.label}
                            </div>
                        );
                    })}
                </div>
            </div>

            <div className="grid gap-4 xl:grid-cols-[1.15fr_1.15fr_0.95fr]">
                <div className="rounded-xl border border-gray-200 bg-white p-4">
                    <div className="flex items-center justify-between gap-3">
                        <div>
                            <div className="text-sm font-semibold text-gray-900">Selected record</div>
                            <div className="text-lg font-bold text-gray-900">{selectedRecord.label}</div>
                        </div>
                        <div className="rounded-full border border-gray-200 bg-gray-50 px-3 py-1 text-xs font-semibold text-gray-600">
                            {selectedRecord.summary}
                        </div>
                    </div>
                    <div className="mt-4 rounded-xl border border-gray-200 bg-white p-3">
                        {renderReplica(selectedRecord.id)}
                    </div>
                    <div className="mt-4">
                        <div className="text-xs font-semibold uppercase tracking-wide text-gray-500">Clickable focus points</div>
                        <div className="mt-2 flex flex-wrap gap-2">
                            {(selectedRecord.hotspots || []).map((hotspot) => {
                                const isActive = hotspot.id === selectedHotspot?.id;
                                return (
                                    <button
                                        key={hotspot.id}
                                        type="button"
                                        onClick={() => setSelectedHotspotId(hotspot.id)}
                                        className={`rounded-full border px-3 py-1.5 text-xs font-semibold ${isActive ? 'border-indigo-500 bg-indigo-600 text-white' : 'border-gray-200 bg-gray-50 text-gray-700 hover:bg-white'}`}
                                    >
                                        {hotspot.label}
                                    </button>
                                );
                            })}
                        </div>
                    </div>
                </div>

                <div className="rounded-xl border border-gray-200 bg-white p-4 space-y-4">
                    <div>
                        <div className="text-sm font-semibold text-gray-900">How this record fits in the cycle</div>
                        <div className="mt-2 rounded-xl border border-gray-200 bg-gray-50 p-3 text-sm text-gray-700">
                            {selectedRecord.purpose}
                        </div>
                    </div>

                    <div className="grid gap-3 md:grid-cols-2">
                        <div className="rounded-xl border border-gray-200 bg-white p-3">
                            <div className="text-xs font-semibold uppercase tracking-wide text-gray-500">Used when</div>
                            <div className="mt-2 text-sm text-gray-700">{selectedRecord.usedWhen}</div>
                        </div>
                        <div className="rounded-xl border border-gray-200 bg-white p-3">
                            <div className="text-xs font-semibold uppercase tracking-wide text-gray-500">Comes from</div>
                            <div className="mt-2 text-sm text-gray-700">{selectedRecord.comesFrom}</div>
                        </div>
                        <div className="rounded-xl border border-gray-200 bg-white p-3 md:col-span-2">
                            <div className="text-xs font-semibold uppercase tracking-wide text-gray-500">Flows to</div>
                            <div className="mt-2 text-sm text-gray-700">{selectedRecord.flowsTo}</div>
                        </div>
                    </div>

                    <div className="rounded-xl border border-indigo-100 bg-indigo-50/70 p-3">
                        <div className="text-xs font-semibold uppercase tracking-wide text-indigo-700">Selected area</div>
                        <div className="mt-1 text-sm font-semibold text-indigo-900">{selectedHotspot?.title || 'Choose a focus point'}</div>
                        <div className="mt-2 text-sm text-indigo-800">{selectedHotspot?.text || 'Click a focus point below the record replica to inspect how a learner should read it.'}</div>
                    </div>
                </div>

                <div className="rounded-xl border border-gray-200 bg-white p-4 space-y-4">
                    <div>
                        <div className="text-sm font-semibold text-gray-900">How to read it</div>
                        <div className="mt-2 space-y-2">
                            {selectedRecord.howToRead.map((item, index) => (
                                <div key={`${selectedRecord.id}-read-${index}`} className="rounded-lg border border-gray-200 bg-gray-50 p-3 text-sm text-gray-700">
                                    {index + 1}. {item}
                                </div>
                            ))}
                        </div>
                    </div>

                    <div>
                        <div className="text-sm font-semibold text-gray-900">What a learner can deduce</div>
                        <div className="mt-2 flex flex-wrap gap-2">
                            {selectedRecord.deductions.map((item, index) => (
                                <div key={`${selectedRecord.id}-deduce-${index}`} className="rounded-full border border-emerald-200 bg-emerald-50 px-3 py-1.5 text-xs font-semibold text-emerald-800">
                                    {item}
                                </div>
                            ))}
                        </div>
                    </div>

                    <div>
                        <div className="text-sm font-semibold text-gray-900">Common mistakes to avoid</div>
                        <div className="mt-2 space-y-2">
                            {selectedRecord.commonMistakes.map((item, index) => (
                                <div key={`${selectedRecord.id}-mistake-${index}`} className="rounded-lg border border-amber-200 bg-amber-50 p-3 text-sm text-amber-900">
                                    {item}
                                </div>
                            ))}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default AccountingRecordsMap;
export { AccountingRecordsMap };
