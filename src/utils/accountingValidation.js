// Accounting Validation Engine and Functions

/**
 * Main accounting validation engine that routes validation to appropriate functions
 * @param {string} validationType - Type of validation to perform
 * @param {Object} data - Data to validate
 * @param {Object} options - Validation options
 * @returns {Object} Validation result with success status and errors
 */
export const accountingValidationEngine = (validationType, data, options = {}) => {
  switch (validationType) {
    case 'cash_receipts':
      return validateCashReceipts(data, options);
    case 'cash_payments':
      return validateCashPayments(data, options);
    case 'trial_balance':
      return validateTrialBalance(data, options);
    case 'debtors_ledger':
      return validateDebtorsLedger(data, options);
    case 'creditors_ledger':
      return validateCreditorsLedger(data, options);
    default:
      return {
        success: false,
        errors: [`Unknown validation type: ${validationType}`]
      };
  }
};

/**
 * Validate cash receipts journal entries
 * @param {Object} data - Cash receipts data
 * @param {Object} options - Validation options
 * @returns {Object} Validation result
 */
export const validateCashReceipts = (data, options = {}) => {
  const errors = [];
  
  if (!data || !data.rows || !Array.isArray(data.rows)) {
    errors.push('Invalid data structure for cash receipts');
    return { success: false, errors };
  }

  let totalDebit = 0;
  let totalCredit = 0;
  let bankTotal = 0;
  let incomeTotal = 0;

  data.rows.forEach((row, index) => {
    if (row.length < 4) {
      errors.push(`Row ${index + 1}: Insufficient columns`);
      return;
    }

    const [date, description, debit, credit] = row;
    
    if (!date || !description) {
      errors.push(`Row ${index + 1}: Date and description are required`);
    }

    const debitAmount = parseFloat(debit) || 0;
    const creditAmount = parseFloat(credit) || 0;

    if (debitAmount > 0 && creditAmount > 0) {
      errors.push(`Row ${index + 1}: Cannot have both debit and credit amounts`);
    }

    totalDebit += debitAmount;
    totalCredit += creditAmount;

    // Track bank and income totals for validation
    if (description.toLowerCase().includes('bank')) {
      bankTotal += debitAmount - creditAmount;
    }
    if (description.toLowerCase().includes('income') || description.toLowerCase().includes('sale')) {
      incomeTotal += creditAmount;
    }
  });

  // Validate double-entry principle
  if (Math.abs(totalDebit - totalCredit) > 0.01) {
    errors.push('Total debits must equal total credits');
  }

  // Validate bank equals income plus sundry (if enabled)
  if (options.validateBankBalance && Math.abs(bankTotal - incomeTotal) > 0.01) {
    errors.push('Bank balance should equal income plus sundry items');
  }

  return {
    success: errors.length === 0,
    errors,
    totals: { totalDebit, totalCredit, bankTotal, incomeTotal }
  };
};

/**
 * Validate cash payments journal entries
 * @param {Object} data - Cash payments data
 * @param {Object} options - Validation options
 * @returns {Object} Validation result
 */
export const validateCashPayments = (data, options = {}) => {
  const errors = [];
  
  if (!data || !data.rows || !Array.isArray(data.rows)) {
    errors.push('Invalid data structure for cash payments');
    return { success: false, errors };
  }

  let totalDebit = 0;
  let totalCredit = 0;
  let bankTotal = 0;
  let expensesTotal = 0;

  data.rows.forEach((row, index) => {
    if (row.length < 4) {
      errors.push(`Row ${index + 1}: Insufficient columns`);
      return;
    }

    const [date, description, debit, credit] = row;
    
    if (!date || !description) {
      errors.push(`Row ${index + 1}: Date and description are required`);
    }

    const debitAmount = parseFloat(debit) || 0;
    const creditAmount = parseFloat(credit) || 0;

    if (debitAmount > 0 && creditAmount > 0) {
      errors.push(`Row ${index + 1}: Cannot have both debit and credit amounts`);
    }

    totalDebit += debitAmount;
    totalCredit += creditAmount;

    // Track bank and expenses totals for validation
    if (description.toLowerCase().includes('bank')) {
      bankTotal += debitAmount - creditAmount;
    }
    if (description.toLowerCase().includes('expense') || description.toLowerCase().includes('purchase')) {
      expensesTotal += debitAmount;
    }
  });

  // Validate double-entry principle
  if (Math.abs(totalDebit - totalCredit) > 0.01) {
    errors.push('Total debits must equal total credits');
  }

  // Validate bank equals expenses plus sundry (if enabled)
  if (options.validateBankBalance && Math.abs(bankTotal - expensesTotal) > 0.01) {
    errors.push('Bank balance should equal expenses plus sundry items');
  }

  return {
    success: errors.length === 0,
    errors,
    totals: { totalDebit, totalCredit, bankTotal, expensesTotal }
  };
};

/**
 * Validate trial balance
 * @param {Object} data - Trial balance data
 * @param {Object} options - Validation options
 * @returns {Object} Validation result
 */
export const validateTrialBalance = (data, options = {}) => {
  const errors = [];
  
  if (!data || !data.rows || !Array.isArray(data.rows)) {
    errors.push('Invalid data structure for trial balance');
    return { success: false, errors };
  }

  let totalDebits = 0;
  let totalCredits = 0;

  data.rows.forEach((row, index) => {
    if (row.length < 3) {
      errors.push(`Row ${index + 1}: Insufficient columns (need account, debit, credit)`);
      return;
    }

    const [account, debit, credit] = row;
    
    if (!account) {
      errors.push(`Row ${index + 1}: Account name is required`);
    }

    const debitAmount = parseFloat(debit) || 0;
    const creditAmount = parseFloat(credit) || 0;

    if (debitAmount > 0 && creditAmount > 0) {
      errors.push(`Row ${index + 1}: Account cannot have both debit and credit balances`);
    }

    totalDebits += debitAmount;
    totalCredits += creditAmount;
  });

  // Validate trial balance equality
  if (Math.abs(totalDebits - totalCredits) > 0.01) {
    errors.push('Total debits must equal total credits in trial balance');
  }

  return {
    success: errors.length === 0,
    errors,
    totals: { totalDebits, totalCredits }
  };
};

/**
 * Validate debtors ledger
 * @param {Object} data - Debtors ledger data
 * @param {Object} options - Validation options
 * @returns {Object} Validation result
 */
export const validateDebtorsLedger = (data, options = {}) => {
  const errors = [];
  
  if (!data || !data.rows || !Array.isArray(data.rows)) {
    errors.push('Invalid data structure for debtors ledger');
    return { success: false, errors };
  }

  let runningBalance = 0;

  data.rows.forEach((row, index) => {
    if (row.length < 4) {
      errors.push(`Row ${index + 1}: Insufficient columns (need date, description, debit, credit, balance)`);
      return;
    }

    const [date, description, debit, credit, balance] = row;
    
    if (!date || !description) {
      errors.push(`Row ${index + 1}: Date and description are required`);
    }

    const debitAmount = parseFloat(debit) || 0;
    const creditAmount = parseFloat(credit) || 0;
    const expectedBalance = parseFloat(balance) || 0;

    // Calculate running balance
    runningBalance += debitAmount - creditAmount;

    // Validate balance calculation
    if (Math.abs(runningBalance - expectedBalance) > 0.01) {
      errors.push(`Row ${index + 1}: Balance calculation error. Expected: ${expectedBalance}, Calculated: ${runningBalance.toFixed(2)}`);
    }
  });

  return {
    success: errors.length === 0,
    errors,
    finalBalance: runningBalance
  };
};

/**
 * Validate creditors ledger
 * @param {Object} data - Creditors ledger data
 * @param {Object} options - Validation options
 * @returns {Object} Validation result
 */
export const validateCreditorsLedger = (data, options = {}) => {
  const errors = [];
  
  if (!data || !data.rows || !Array.isArray(data.rows)) {
    errors.push('Invalid data structure for creditors ledger');
    return { success: false, errors };
  }

  let runningBalance = 0;

  data.rows.forEach((row, index) => {
    if (row.length < 4) {
      errors.push(`Row ${index + 1}: Insufficient columns (need date, description, debit, credit, balance)`);
      return;
    }

    const [date, description, debit, credit, balance] = row;
    
    if (!date || !description) {
      errors.push(`Row ${index + 1}: Date and description are required`);
    }

    const debitAmount = parseFloat(debit) || 0;
    const creditAmount = parseFloat(credit) || 0;
    const expectedBalance = parseFloat(balance) || 0;

    // Calculate running balance (creditors are liabilities, so credit increases balance)
    runningBalance += creditAmount - debitAmount;

    // Validate balance calculation
    if (Math.abs(runningBalance - expectedBalance) > 0.01) {
      errors.push(`Row ${index + 1}: Balance calculation error. Expected: ${expectedBalance}, Calculated: ${runningBalance.toFixed(2)}`);
    }
  });

  return {
    success: errors.length === 0,
    errors,
    finalBalance: runningBalance
  };
};
