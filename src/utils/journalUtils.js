// Journal Conversion Functions
export const convertJournalToText = (journalData, journalType) => {
    switch (journalType) {
        case 'cash_receipts':
            return convertCashReceiptsToText(journalData);
        case 'cash_payments':
            return convertCashPaymentsToText(journalData);
        case 'debtors_journal':
            return convertDebtorsJournalToText(journalData);
        case 'creditors_journal':
            return convertCreditorsJournalToText(journalData);
        case 'general_ledger':
            return convertGeneralLedgerToText(journalData);
        case 'trial_balance':
            return convertTrialBalanceToText(journalData);
        case 'debtors_ledger':
            return convertDebtorsLedgerToText(journalData);
        case 'creditors_ledger':
            return convertCreditorsLedgerToText(journalData);
        case 'accounting_equation':
            return convertAccountingEquationToText(journalData);
        default:
            return JSON.stringify(journalData);
    }
};

export const convertCashReceiptsToText = (journalData) => {
    if (!journalData || !journalData.rows) return "No journal data available";
    
    let text = `Cash Receipts Journal for ${journalData.companyName || 'Company'} for ${journalData.month || 'Period'}\n\n`;
    
    journalData.rows.forEach((row, index) => {
        text += `Row ${index + 1}: Document ${row.doc || 'N/A'}, Day ${row.day || 'N/A'}, Details: ${row.details || 'N/A'}, `;
        text += `Analysis: R${row.analysis?.main || '0'}.${row.analysis?.cents || '00'}, `;
        text += `Bank: R${row.bank?.main || '0'}.${row.bank?.cents || '00'}, `;
        text += `Income: R${row.income?.main || '0'}.${row.income?.cents || '00'}, `;
        text += `Sales: R${row.sales?.main || '0'}.${row.sales?.cents || '00'}, `;
        text += `Cost of Sales: R${row.costOfSales?.main || '0'}.${row.costOfSales?.cents || '00'}, `;
        text += `Debtors Control: R${row.debtorsControl?.main || '0'}.${row.debtorsControl?.cents || '00'}, `;
        text += `Sundry: R${row.sundry_amount?.main || '0'}.${row.sundry_amount?.cents || '00'} (${row.sundry_details || 'N/A'})\n`;
    });
    
    // Calculate totals
    const totals = journalData.rows.reduce((acc, row) => {
        const analysis = parseFloat(row.analysis?.main || 0) + parseFloat(row.analysis?.cents || 0) / 100;
        const bank = parseFloat(row.bank?.main || 0) + parseFloat(row.bank?.cents || 0) / 100;
        const income = parseFloat(row.income?.main || 0) + parseFloat(row.income?.cents || 0) / 100;
        const sundry = parseFloat(row.sundry_amount?.main || 0) + parseFloat(row.sundry_amount?.cents || 0) / 100;
        
        return {
            analysis: acc.analysis + analysis,
            bank: acc.bank + bank,
            income: acc.income + income,
            sundry: acc.sundry + sundry
        };
    }, { analysis: 0, bank: 0, income: 0, sundry: 0 });
    
    text += `\nTotals: Analysis R${totals.analysis.toFixed(2)}, Bank R${totals.bank.toFixed(2)}, Income R${totals.income.toFixed(2)}, Sundry R${totals.sundry.toFixed(2)}`;
    
    const isBalanced = Math.abs(totals.bank - (totals.income + totals.sundry)) < 0.01;
    text += `\nBalancing Check: ${isBalanced ? '✓ Balanced' : '✗ Not balanced'}`;
    
    return text;
};

export const convertCashPaymentsToText = (journalData) => {
    if (!journalData || !journalData.rows) return "No journal data available";
    
    let text = `Cash Payments Journal for ${journalData.companyName || 'Company'} for ${journalData.month || 'Period'}\n\n`;
    
    journalData.rows.forEach((row, index) => {
        text += `Row ${index + 1}: Document ${row.doc || 'N/A'}, Day ${row.day || 'N/A'}, Payee: ${row.payee || 'N/A'}, `;
        text += `Bank: R${row.bank?.main || '0'}.${row.bank?.cents || '00'}, `;
        text += `Consumables: R${row.consumables?.main || '0'}.${row.consumables?.cents || '00'}, `;
        text += `Wages: R${row.wages?.main || '0'}.${row.wages?.cents || '00'}, `;
        text += `Trading Stock: R${row.tradingStock?.main || '0'}.${row.tradingStock?.cents || '00'}, `;
        text += `Creditors Control: R${row.creditorsControl?.main || '0'}.${row.creditorsControl?.cents || '00'}, `;
        text += `Sundry: R${row.sundry_amount?.main || '0'}.${row.sundry_amount?.cents || '00'} (${row.sundry_details || 'N/A'})\n`;
    });
    
    // Calculate totals
    const totals = journalData.rows.reduce((acc, row) => {
        const bank = parseFloat(row.bank?.main || 0) + parseFloat(row.bank?.cents || 0) / 100;
        const consumables = parseFloat(row.consumables?.main || 0) + parseFloat(row.consumables?.cents || 0) / 100;
        const wages = parseFloat(row.wages?.main || 0) + parseFloat(row.wages?.cents || 0) / 100;
        const sundry = parseFloat(row.sundry_amount?.main || 0) + parseFloat(row.sundry_amount?.cents || 0) / 100;
        
        return {
            bank: acc.bank + bank,
            consumables: acc.consumables + consumables,
            wages: acc.wages + wages,
            sundry: acc.sundry + sundry
        };
    }, { bank: 0, consumables: 0, wages: 0, sundry: 0 });
    
    text += `\nTotals: Bank R${totals.bank.toFixed(2)}, Consumables R${totals.consumables.toFixed(2)}, Wages R${totals.wages.toFixed(2)}, Sundry R${totals.sundry.toFixed(2)}`;
    
    const isBalanced = Math.abs(totals.bank - (totals.consumables + totals.wages + totals.sundry)) < 0.01;
    text += `\nBalancing Check: ${isBalanced ? '✓ Balanced' : '✗ Not balanced'}`;
    
    return text;
};

export const convertDebtorsJournalToText = (journalData) => {
    if (!journalData || !journalData.rows) return "No journal data available";
    
    let text = `Debtors Journal for ${journalData.companyName || 'Company'}\n\n`;
    
    journalData.rows.forEach((row, index) => {
        text += `Row ${index + 1}: Document ${row.docNo || 'N/A'}, Day ${row.day || 'N/A'}, Debtor: ${row.debtor || 'N/A'}, `;
        text += `Sales: R${row.sales || '0.00'}, Cost of Sales: R${row.costOfSales || '0.00'}\n`;
    });
    
    // Calculate totals
    const totals = journalData.rows.reduce((acc, row) => {
        const sales = parseFloat(row.sales) || 0;
        const costOfSales = parseFloat(row.costOfSales) || 0;
        return { sales: acc.sales + sales, costOfSales: acc.costOfSales + costOfSales };
    }, { sales: 0, costOfSales: 0 });
    
    text += `\nTotals: Sales R${totals.sales.toFixed(2)}, Cost of Sales R${totals.costOfSales.toFixed(2)}`;
    
    return text;
};

export const convertCreditorsJournalToText = (journalData) => {
    if (!journalData || !journalData.rows) return "No journal data available";
    
    let text = `Creditors Journal for ${journalData.companyName || 'Company'}\n\n`;
    
    journalData.rows.forEach((row, index) => {
        text += `Row ${index + 1}: Document ${row.docNo || 'N/A'}, Day ${row.day || 'N/A'}, Creditor: ${row.creditor || 'N/A'}, `;
        text += `Purchases: R${row.purchases || '0.00'}, Cost of Sales: R${row.costOfSales || '0.00'}\n`;
    });
    
    // Calculate totals
    const totals = journalData.rows.reduce((acc, row) => {
        const purchases = parseFloat(row.purchases) || 0;
        const costOfSales = parseFloat(row.costOfSales) || 0;
        return { purchases: acc.purchases + purchases, costOfSales: acc.costOfSales + costOfSales };
    }, { purchases: 0, costOfSales: 0 });
    
    text += `\nTotals: Purchases R${totals.purchases.toFixed(2)}, Cost of Sales R${totals.costOfSales.toFixed(2)}`;
    
    return text;
};

export const convertGeneralLedgerToText = (journalData) => {
    if (!journalData || !journalData.tables) return "No ledger data available";
    
    let text = `General Ledger for ${journalData.companyName || 'Company'}\n\n`;
    
    journalData.tables.forEach((table) => {
        text += `Account: ${table.accountName || 'N/A'}\n`;
        table.rows.forEach((row, rowIndex) => {
            text += `Row ${rowIndex + 1}: Date ${row.date || 'N/A'}, Details: ${row.details || 'N/A'}, `;
            text += `Debit: R${row.debit || '0.00'}, Credit: R${row.credit || '0.00'}, Balance: R${row.balance || '0.00'}\n`;
        });
        text += `\n`;
    });
    
    return text;
};

export const convertTrialBalanceToText = (journalData) => {
    if (!journalData || !journalData.accounts) return "No trial balance data available";
    
    let text = `Trial Balance for ${journalData.businessName || 'Company'} on ${journalData.date || 'Date'}\n\n`;
    
    journalData.accounts.forEach((account, index) => {
        text += `Account ${index + 1}: ${account.account || 'N/A'}, Debit: R${account.debit || '0.00'}, Credit: R${account.credit || '0.00'}\n`;
    });
    
    // Calculate totals
    const totals = journalData.accounts.reduce((acc, account) => {
        const debit = parseFloat(account.debit) || 0;
        const credit = parseFloat(account.credit) || 0;
        return { totalDebit: acc.totalDebit + debit, totalCredit: acc.totalCredit + credit };
    }, { totalDebit: 0, totalCredit: 0 });
    
    text += `\nTotals: Debit R${totals.totalDebit.toFixed(2)}, Credit R${totals.totalCredit.toFixed(2)}`;
    
    const isBalanced = Math.abs(totals.totalDebit - totals.totalCredit) < 0.01;
    text += `\nBalancing Check: ${isBalanced ? '✓ Balanced' : '✗ Not balanced'}`;
    
    return text;
};

export const convertDebtorsLedgerToText = (journalData) => {
    if (!journalData || !journalData.rows) return "No debtors ledger data available";
    
    let text = `Debtors Ledger for ${journalData.businessName || 'Company'}\n`;
    text += `Debtor: ${journalData.debtorName || 'N/A'}, Account No: ${journalData.accountNumber || 'N/A'}\n\n`;
    
    journalData.rows.forEach((row, index) => {
        text += `Row ${index + 1}: Date ${row.date || 'N/A'}, Details: ${row.details || 'N/A'}, `;
        text += `Folio: ${row.fol || 'N/A'}, Debit: R${row.debit || '0.00'}, Credit: R${row.credit || '0.00'}, Balance: R${row.balance || '0.00'}\n`;
    });
    
    // Calculate totals
    const totals = journalData.rows.reduce((acc, row) => {
        const debit = parseFloat(row.debit) || 0;
        const credit = parseFloat(row.credit) || 0;
        return { totalDebit: acc.totalDebit + debit, totalCredit: acc.totalCredit + credit };
    }, { totalDebit: 0, totalCredit: 0 });
    
    const finalBalance = totals.totalDebit - totals.totalCredit;
    text += `\nTotals: Debit R${totals.totalDebit.toFixed(2)}, Credit R${totals.totalCredit.toFixed(2)}, Final Balance: R${finalBalance.toFixed(2)}`;
    
    return text;
};

export const convertCreditorsLedgerToText = (journalData) => {
    if (!journalData || !journalData.rows) return "No creditors ledger data available";
    
    let text = `Creditors Ledger for ${journalData.businessName || 'Company'}\n`;
    text += `Creditor: ${journalData.creditorName || 'N/A'}, Account No: ${journalData.accountNumber || 'N/A'}\n\n`;
    
    journalData.rows.forEach((row, index) => {
        text += `Row ${index + 1}: Date ${row.date || 'N/A'}, Details: ${row.details || 'N/A'}, `;
        text += `Folio: ${row.fol || 'N/A'}, Debit: R${row.debit || '0.00'}, Credit: R${row.credit || '0.00'}, Balance: R${row.balance || '0.00'}\n`;
    });
    
    // Calculate totals
    const totals = journalData.rows.reduce((acc, row) => {
        const debit = parseFloat(row.debit) || 0;
        const credit = parseFloat(row.credit) || 0;
        return { totalDebit: acc.totalDebit + debit, totalCredit: acc.totalCredit + credit };
    }, { totalDebit: 0, totalCredit: 0 });
    
    const finalBalance = totals.totalCredit - totals.totalDebit;
    text += `\nTotals: Debit R${totals.totalDebit.toFixed(2)}, Credit R${totals.totalCredit.toFixed(2)}, Final Balance: R${finalBalance.toFixed(2)}`;
    
    return text;
};

export const convertAccountingEquationToText = (journalData) => {
    if (!journalData) return "No accounting equation data available";
    
    let text = `Accounting Equation for ${journalData.businessName || 'Company'} on ${journalData.date || 'Date'}\n\n`;
    
    // Assets
    text += `ASSETS:\n`;
    journalData.assets.forEach((asset, index) => {
        text += `Row ${index + 1}: Effect R${asset.effect || '0.00'}, Reason: ${asset.reason || 'N/A'}\n`;
    });
    
    // Owner's Equity
    text += `\nOWNER'S EQUITY:\n`;
    journalData.ownersEquity.forEach((equity, index) => {
        text += `Row ${index + 1}: Effect R${equity.effect || '0.00'}, Reason: ${equity.reason || 'N/A'}\n`;
    });
    
    // Liabilities
    text += `\nLIABILITIES:\n`;
    journalData.liabilities.forEach((liability, index) => {
        text += `Row ${index + 1}: Effect R${liability.effect || '0.00'}, Reason: ${liability.reason || 'N/A'}\n`;
    });
    
    // Calculate totals
    const assetsTotal = journalData.assets.reduce((sum, asset) => sum + (parseFloat(asset.effect) || 0), 0);
    const equityTotal = journalData.ownersEquity.reduce((sum, equity) => sum + (parseFloat(equity.effect) || 0), 0);
    const liabilitiesTotal = journalData.liabilities.reduce((sum, liability) => sum + (parseFloat(liability.effect) || 0), 0);
    
    text += `\nTotals: Assets R${assetsTotal.toFixed(2)}, Owner's Equity R${equityTotal.toFixed(2)}, Liabilities R${liabilitiesTotal.toFixed(2)}`;
    
    const isBalanced = Math.abs(assetsTotal - (equityTotal + liabilitiesTotal)) < 0.01;
    text += `\nBalancing Check: ${isBalanced ? '✓ Balanced' : '✗ Not balanced'}`;
    
    return text;
};
