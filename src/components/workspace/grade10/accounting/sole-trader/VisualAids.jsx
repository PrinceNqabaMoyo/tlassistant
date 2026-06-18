import React from 'react';
import AccountingRecordsMap from './visual-aids/AccountingRecordsMap';

export const Grade10SoleTraderVisualAids = ({ visualAidsTab, setVisualAidsTab, setVisualAidsOpen, currentSubskill }) => {
    return (
        <div className="p-4">
            <div className="flex items-center justify-between mb-3">
                <div className="font-bold text-gray-900">Sole trader • Visual aids</div>
                <button
                    onClick={() => setVisualAidsOpen(false)}
                    className="px-3 py-1.5 bg-gray-100 hover:bg-gray-200 text-gray-800 rounded-lg font-medium"
                >
                    Close
                </button>
            </div>

            <div className="flex flex-wrap gap-2 mb-4">
                <button
                    onClick={() => setVisualAidsTab('overview')}
                    className={`px-3 py-1.5 rounded-lg border text-sm font-semibold ${visualAidsTab === 'overview' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'}`}
                >
                    Overview
                </button>
                <button
                    onClick={() => setVisualAidsTab('cycle')}
                    className={`px-3 py-1.5 rounded-lg border text-sm font-semibold ${visualAidsTab === 'cycle' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'}`}
                >
                    Cycle
                </button>
                <button
                    onClick={() => setVisualAidsTab('journals')}
                    className={`px-3 py-1.5 rounded-lg border text-sm font-semibold ${visualAidsTab === 'journals' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'}`}
                >
                    Journals
                </button>
                <button
                    onClick={() => setVisualAidsTab('equation')}
                    className={`px-3 py-1.5 rounded-lg border text-sm font-semibold ${visualAidsTab === 'equation' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'}`}
                >
                    Equation
                </button>
                <button
                    onClick={() => setVisualAidsTab('records_map')}
                    className={`px-3 py-1.5 rounded-lg border text-sm font-semibold ${visualAidsTab === 'records_map' ? 'bg-indigo-600 text-white border-indigo-600' : 'bg-white text-gray-700 border-gray-200 hover:bg-gray-50'}`}
                >
                    Records map
                </button>
            </div>

            {visualAidsTab === 'overview' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Sole proprietor (sole trader)</div>
                        <div className="text-sm text-gray-700 mt-1">
                            One person owns and controls the business. The owner receives all profits and carries all losses.
                        </div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Business entity principle</div>
                        <div className="text-sm text-gray-700 mt-1">
                            The owner and the business are separate entities. Do not record personal expenses as business expenses.
                        </div>
                    </div>
                </div>
            )}

            {visualAidsTab === 'cycle' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Accounting cycle (overview)</div>
                        <div className="text-sm text-gray-700 mt-1">
                            A transaction starts a repeatable process: record it, post it, summarise it, adjust it, then report it.
                        </div>
                    </div>

                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Cycle steps</div>
                        <div className="mt-3 space-y-2">
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">1. Source documents</div>
                                <div className="text-xs text-gray-700 mt-0.5">Invoice, receipt, cheque counterfoil, etc.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">2. Subsidiary journals</div>
                                <div className="text-xs text-gray-700 mt-0.5">CRJ, CPJ, DJ, CJ, etc.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">3. Ledger posting</div>
                                <div className="text-xs text-gray-700 mt-0.5">Post totals/amounts to ledger accounts.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">4. Trial balance</div>
                                <div className="text-xs text-gray-700 mt-0.5">Check total debits = total credits.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">5. Adjustments</div>
                                <div className="text-xs text-gray-700 mt-0.5">Accruals, prepaid expenses, depreciation, etc.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">6. Financial statements</div>
                                <div className="text-xs text-gray-700 mt-0.5">Report performance and position for the period.</div>
                            </div>
                        </div>
                    </div>

                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Key idea</div>
                        <div className="text-sm text-gray-700 mt-1">
                            Journals are used to record transactions FIRST; the ledger is used to classify them into accounts.
                        </div>
                    </div>
                </div>
            )}

            {visualAidsTab === 'records_map' && (
                <AccountingRecordsMap currentSubskill={currentSubskill} />
            )}

            {visualAidsTab === 'equation' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Accounting equation</div>
                        <div className="text-sm text-gray-700 mt-1">Assets = Owner’s equity + Liabilities</div>
                        <div className="text-sm text-gray-700">Owner’s equity = Assets − Liabilities</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Assets</div>
                        <div className="text-sm text-gray-700 mt-1">
                            Things the business owns/controls that have value (e.g. Bank, Trading stock, Debtors control, Equipment).
                        </div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Owner’s equity</div>
                        <div className="text-sm text-gray-700 mt-1">
                            The owner’s claim on the assets. It increases with incomes (e.g. Sales, Rent income, Interest income) and
                            decreases with expenses (e.g. Wages, Bank charges, Interest on overdraft) and drawings.
                        </div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Liabilities</div>
                        <div className="text-sm text-gray-700 mt-1">
                            Amounts the business owes (e.g. Creditors control, Loans). If liabilities increase, the business owes more.
                        </div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">How transaction analysis works (the workflow)</div>
                        <div className="text-sm text-gray-700 mt-1">
                            Start from the source document, decide which journal it belongs to, then identify the General Ledger accounts
                            to debit/credit, then show the effect on the accounting equation.
                        </div>
                        <div className="mt-3 space-y-2">
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">1. Source document</div>
                                <div className="text-xs text-gray-700 mt-0.5">Bank statement, cheque counterfoil, invoice, receipt, journal voucher, etc.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">2. Subsidiary journal (where it would be recorded)</div>
                                <div className="text-xs text-gray-700 mt-0.5">CRJ/CPJ for cash, DJ/CJ for credit, DAJ/CAJ for returns, PCJ for petty cash, GJ for adjustments.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">3. General Ledger accounts (double entry)</div>
                                <div className="text-xs text-gray-700 mt-0.5">Choose the account debited and the account credited.</div>
                            </div>
                            <div className="text-xs text-gray-500">↓</div>
                            <div className="p-2 rounded-lg border border-gray-200 bg-gray-50">
                                <div className="text-sm font-semibold text-gray-800">4. Effect on the accounting equation (A, OE, L)</div>
                                <div className="text-xs text-gray-700 mt-0.5">
                                    Use + for an increase, - for a decrease and 0 for no change. A favourable bank balance means Bank is a positive asset;
                                    an overdraft means Bank behaves like a liability.
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Quick check</div>
                        <div className="text-sm text-gray-700 mt-1">
                            If liabilities increase and assets stay the same, owner’s equity must decrease.
                        </div>
                    </div>
                </div>
            )}

            {visualAidsTab === 'journals' && (
                <div className="space-y-3">
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">CRJ (Cash Receipts Journal)</div>
                        <div className="text-sm text-gray-700 mt-1">Record money received. Bank is the total received per transaction/day.</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">CPJ (Cash Payments Journal)</div>
                        <div className="text-sm text-gray-700 mt-1">Record money paid by cheque. Bank is the cheque amount.</div>
                    </div>
                    <div className="bg-white border border-gray-200 rounded-xl p-3">
                        <div className="font-semibold text-gray-900">Sundry columns</div>
                        <div className="text-sm text-gray-700 mt-1">Use Sundry when no specific analysis column exists.</div>
                    </div>
                </div>
            )}
        </div>
    );
};
