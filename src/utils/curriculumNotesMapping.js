// Curriculum NOTES mapping for archetype help system
// Each archetype_key maps to relevant curriculum notes content

export const curriculumNotesMapping = {
  // Grade 11 Controlled Test
  'g11_ct1_q1_accdep_vehicles_timeline': {
    title: 'Fixed Assets - Depreciation Calculation',
    notes: [
      'Depreciation is the systematic allocation of the cost of a fixed asset over its useful life.',
      'Diminishing balance method applies the percentage to the carrying value (cost minus accumulated depreciation).',
      'When an asset is purchased mid-year, calculate depreciation proportionally for the months in use.',
      'Formula: Depreciation = Cost × Rate% × (Months in use / 12)',
    ],
  },
  'g11_ct1_q2_crj_format': {
    title: 'Cash Receipts Journal (CRJ)',
    notes: [
      'The CRJ records all cash received by the business.',
      'Source documents: CRR (Cash Register Roll) for cash sales; Receipts for other income.',
      'Analysis of receipts column shows the breakdown of where cash came from.',
      'Bank column shows total cash deposited.',
      'Cost of sales is recorded at the same time as sales (to maintain gross profit relationship).',
    ],
  },
  'g11_ct1_q2_cpj_format': {
    title: 'Cash Payments Journal (CPJ)',
    notes: [
      'The CPJ records all cash payments made by the business.',
      'Cheque numbers are used as source documents.',
      'Trading Stock column records cash purchases of inventory.',
      'Wages column records employee wage payments.',
      'Creditors Control records payments to suppliers, with Discount Received shown separately.',
    ],
  },
  'g11_ct1_q2_brs_statement': {
    title: 'Bank Reconciliation Statement',
    notes: [
      'The BRS explains the difference between the bank statement balance and the bank account balance.',
      'Outstanding deposits: recorded in CRJ but not yet on bank statement (add to bank balance).',
      'Outstanding cheques: recorded in CPJ but not yet cleared by bank (subtract from bank balance).',
      'Errors and dishonoured cheques must be corrected in the cash journals.',
      'Favourable balance = positive (credit); Unfavourable/overdraft = negative (debit).',
    ],
  },
  'g11_ct1_q3_accdep_taccount': {
    title: 'Accumulated Depreciation T-account',
    notes: [
      'Accumulated Depreciation is a contra-asset account (negative asset).',
      'It has a credit balance because it reduces the carrying value of the asset.',
      'Opening balance (Balance b/d) appears on the credit side.',
      'Current year depreciation is recorded on the credit side (GJ - General Journal).',
      'Closing balance (Balance c/d) is on the smaller side (debit in this case).',
      'Total of both sides must be equal after balancing.',
    ],
  },
  'g11_ct1_q4_asset_disposal': {
    title: 'Asset Disposal Account',
    notes: [
      'The Asset Disposal account is a temporary account to record asset disposals.',
      'Debit: Cost price of asset being removed (from Asset account).',
      'Credit: Accumulated depreciation of the disposed asset (from Acc Dep account).',
      'Credit: Amount received from sale (Bank or Debtors).',
      'Difference = Profit (if credit > debit) or Loss (if debit > credit) on sale.',
      'Profit on sale goes to Profit/Loss; Loss is an expense.',
    ],
  },
  'g11_ct1_q5_fixed_assets_note': {
    title: 'Fixed Assets Note',
    notes: [
      'Fixed/Tangible Assets Note shows cost, accumulated depreciation, and carrying value.',
      'Carrying Value = Cost - Accumulated Depreciation.',
      'Land & Buildings are not depreciated.',
      'Vehicles: Depreciation can be on cost or diminishing balance.',
      'Equipment: Usually depreciated on cost price.',
      'Show opening balance, movements (additions, disposals, depreciation), and closing balance.',
    ],
  },
  'g11_ct1_q6_internal_control': {
    title: 'Internal Control - Vehicle Misuse',
    notes: [
      'Internal controls safeguard assets and prevent fraud.',
      'Logbook system: Record all trips with date, destination, purpose, and mileage.',
      'Fuel limits: Set monthly allowance based on business needs.',
      'GPS tracking: Monitor vehicle location and usage.',
      'Authorized drivers only: Only designated employees may use the vehicle.',
      'Mileage reconciliation: Compare odometer with logbook entries.',
    ],
  },
  'g11_ct1_q2_bank_ledger': {
    title: 'Bank Ledger Account',
    notes: [
      'The Bank account is an asset account in the General Ledger.',
      'Debit side (left): Opening balance, Cash receipts (CRJ total).',
      'Credit side (right): Cash payments (CPJ total).',
      'Balance c/d: Closing balance carried down to next period.',
      'Total debits must equal total credits.',
    ],
  },

  // Grade 11 Concepts (Partnerships, Ethics, GAAP)
  'g11_concepts_partnerships': {
    title: 'Partnerships - Key Concepts',
    notes: [
      'Partnership: Business owned by 2-20 partners (except professional partnerships).',
      'Partnership Agreement: Written agreement covering profit sharing, capital contributions, drawings limits.',
      'Current Account: Tracks profit share, salaries, interest on capital, drawings.',
      'Appropriation Account: Distributes net profit to partners.',
      'Unlimited liability: Partners personally liable for business debts.',
    ],
  },
  'g11_concepts_ethics': {
    title: 'Ethics in Accounting',
    notes: [
      'Integrity: Honest and straightforward in all professional relationships.',
      'Objectivity: No bias, conflict of interest, or undue influence.',
      'Professional competence: Maintain knowledge and skill at required level.',
      'Confidentiality: Respect confidentiality of information.',
      'Professional behaviour: Comply with laws and avoid discrediting the profession.',
    ],
  },
  'g11_concepts_gaap': {
    title: 'GAAP Principles',
    notes: [
      'Historical cost: Assets recorded at original purchase price.',
      'Matching principle: Expenses matched to revenue in same period.',
      'Prudence/conservatism: Do not overstate income or assets.',
      'Consistency: Same methods used from year to year.',
      'Going concern: Business will continue operating in foreseeable future.',
    ],
  },

  // Grade 12 Financial Statements
  'g12_fs_income_statement_basic': {
    title: 'Income Statement Format',
    notes: [
      'Sales - Cost of Sales = Gross Profit',
      'Gross Profit + Other Operating Income = Gross Operating Income',
      'Gross Operating Income - Operating Expenses = Operating Profit',
      'Operating Profit + Interest Income - Interest Expense = Profit Before Tax',
      'Profit Before Tax - Income Tax = Net Profit After Tax',
      'Expenses are shown in brackets to indicate subtraction.',
    ],
  },
  'g12_fs_retained_income_note_buyback': {
    title: 'Retained Income Note',
    notes: [
      'Balance at beginning of year + Net Profit After Tax = Total available',
      'Less: Dividends (ordinary share dividends)',
      'Less: Share buyback premium (repurchase price - average issue price)',
      'Balance at end of year',
      'The buyback premium reduces retained income because the company paid more than the average issue price.',
    ],
  },
  'g12_fs_balance_sheet_companies': {
    title: 'Balance Sheet (Statement of Financial Position)',
    notes: [
      'ASSETS = EQUITY + LIABILITIES',
      'Non-current assets: Fixed/Tangible assets at carrying value (cost - accumulated depreciation)',
      'Current assets: Inventories + Trade and Other Receivables + Cash and Cash Equivalents',
      'Shareholders Equity: Ordinary Share Capital + Retained Income',
      'Non-current liabilities: Long-term loans (less current portion)',
      'Current liabilities: Trade and Other Payables + Current portion of loan + Shareholders for dividends + SARS income tax',
    ],
  },
  'g12_fs_trade_receivables_note': {
    title: 'Trade and Other Receivables Note',
    notes: [
      'Trade debtors (gross amount customers owe)',
      'Less: Provision for bad debts (estimated uncollectible amounts)',
      '= Net trade debtors',
      'Add: SARS (income tax receivable/overpaid)',
      'Add: Prepaid expenses (paid in advance)',
      'Add: Accrued income (earned but not yet received)',
      '= Trade and Other Receivables',
    ],
  },

  // Grade 12 Analysis & Interpretation
  'g12_ai_ratio_calculations': {
    title: 'Financial Ratio Calculations',
    notes: [
      'Current ratio = Current Assets : Current Liabilities (measures liquidity)',
      'Acid-test ratio = (Current Assets - Inventory) : Current Liabilities (strict liquidity test)',
      'Debt-equity ratio = Non-current Liabilities : Shareholders Equity (measures gearing/risk)',
      'Return on Shareholders Equity (ROSHE) = (Net Profit After Tax / Shareholders Equity) × 100',
      'Earnings Per Share (EPS) = (Net Profit After Tax / Number of shares) × 100 (in cents)',
      'Debtors Collection Period = (Average Debtors / Credit Sales) × 365 days',
      'Stock Turnover Rate = Cost of Sales / Average Stock',
    ],
  },
  'g12_ai_q1_profitability_expense_management': {
    title: 'Profitability Analysis',
    notes: [
      '% Operating expenses on sales = (Operating expenses / Sales) × 100',
      '% Operating profit on sales = (Operating profit / Sales) × 100',
      'Compare trends year-on-year to assess expense control.',
      'If % operating expenses decreases while % operating profit increases, expenses are well controlled.',
      'Always quote TWO indicators with figures and trends.',
    ],
  },
  'g12_ai_q1_dividend_payout_policy': {
    title: 'Dividend Pay-out Policy',
    notes: [
      'Dividend Pay-out Rate (DPR) = (Total Dividends / Net Profit After Tax) × 100',
      'High DPR: Most profit distributed to shareholders (low retention).',
      'Low DPR: Profit retained for business expansion/growth.',
      'Policy change reasons: Expansion plans, cash flow needs, shareholder expectations.',
      'Compare DPR between years to identify policy shifts.',
    ],
  },
  'g12_ai_q4_liquidity_support_indicators': {
    title: 'Liquidity Analysis',
    notes: [
      'Stock turnover rate: How quickly inventory is sold (higher is generally better).',
      'Debtors collection period: Average days to collect from customers (shorter is better).',
      'Acid-test ratio: Immediate ability to pay debts (exclude inventory).',
      'Benchmarks: Stock turnover days vary by industry; Debtors should ideally be 30-60 days.',
      'Liquidity problems: High inventory + slow collections = cash flow pressure.',
    ],
  },
  'g12_ai_q4_loan_repayment_decision': {
    title: 'Loan Repayment and Gearing',
    notes: [
      'Positive gearing: ROTCE > Interest rate (benefits shareholders to keep loan).',
      'Negative gearing: ROTCE < Interest rate (repay to reduce losses).',
      'Debt-equity ratio indicates financial risk - lower is generally safer.',
      'Repaying loans: Improves future borrowing capacity, reduces interest burden.',
      'Consider both financial indicators and strategic implications.',
    ],
  },
  'g12_ai_q5_value_shares_buyback_ethics': {
    title: 'Share Buyback Ethics',
    notes: [
      'NAV per share = Shareholders Equity / Number of shares.',
      'Market price may differ from NAV based on demand and expectations.',
      'Buyback below NAV: Shareholders lose value (selling below book value).',
      'Buyback below market price: Unfair to shareholders.',
      'Ethical concerns: Insider trading, conflict of interest, exploiting information advantage.',
    ],
  },
  'g12_ai_q1_earnings_returns_eps_roshe': {
    title: 'Earnings and Returns (EPS & ROSHE)',
    notes: [
      'EPS = Earnings Per Share (profit per share in cents).',
      'ROSHE = Return on Shareholders Equity (% return on investment).',
      'Compare ROSHE to alternative investments (e.g., fixed deposit rate).',
      'ROSHE > alternative rate = Shareholders satisfied.',
      'Always quote figures and compare year-on-year.',
    ],
  },
  'g12_ai_q2_liquidity_position_comment': {
    title: 'Liquidity Position Comment',
    notes: [
      'Current ratio = Current Assets : Current Liabilities (measures ability to pay short-term debts).',
      'Acid-test ratio = (Current Assets - Inventory) : Current Liabilities (strict liquidity test).',
      'Ideal current ratio: 2:1; Ideal acid-test: 1:1.',
      'Quote TWO indicators with figures when commenting on liquidity.',
      'Compare to previous year to identify trends.',
    ],
  },
  'g12_ai_q3_risk_gearing_loan_objection': {
    title: 'Risk and Gearing - Loan Decision',
    notes: [
      'Debt-equity ratio = Non-current Liabilities : Shareholders Equity.',
      'ROTCE = Return on Total Capital Employed.',
      'Positive gearing: ROTCE > Interest rate (keep the loan).',
      'Negative gearing: ROTCE < Interest rate (repay the loan).',
      'Higher debt-equity = Higher financial risk.',
    ],
  },
  'g12_ai_q4_shareholder_satisfaction_market_price': {
    title: 'Shareholder Satisfaction',
    notes: [
      'Compare market price to NAV per share.',
      'Market price > NAV: Shares trading at premium.',
      'Market price < NAV: Shares trading at discount.',
      'Consider EPS growth and DPS trends.',
      'Shareholders want: Good returns (ROSHE), growing dividends, fair share price.',
    ],
  },
  'g12_ai_q4_shareholding_coalition_voting_power': {
    title: 'Shareholding Coalition',
    notes: [
      'Calculate combined shareholding percentage.',
      'Majority control: >50% of voting shares.',
      'Significant influence: 20-50% of shares.',
      'Concerns: Loss of control, voting power concentration, minority shareholder protection.',
    ],
  },
  'g12_ai_q5_liquidity_strategies_working_capital': {
    title: 'Liquidity Strategies',
    notes: [
      'Improve stock turnover: Reduce inventory levels, discount slow-moving stock.',
      'Improve debtors collection: Stricter credit terms, discounts for early payment.',
      'Negotiate better payment terms with suppliers.',
      'Reduce unnecessary expenses.',
      'Short-term financing options.',
    ],
  },

  // Grade 12 Company General Ledger
  'g12_company_gl_ordinary_share_capital': {
    title: 'Ordinary Share Capital Ledger',
    notes: [
      'Ordinary Share Capital account tracks shares issued and repurchased.',
      'Credit side: Opening balance, additional shares issued.',
      'Debit side: Shares repurchased at average price.',
      'Calculate average price: Total capital / Number of shares.',
    ],
  },
  'g12_ct1_appropriation_account_working': {
    title: 'Appropriation Account',
    notes: [
      'The Appropriation Account shows distribution of net profit.',
      'Debit: Dividends on ordinary shares (interim + final).',
      'Debit: Retained income (amount kept in the business).',
      'Credit: Net profit after tax from Profit and Loss.',
      'Total debits must equal total credits.',
    ],
  },

  // Grade 12 Companies Concepts
  'g12_concepts_companies': {
    title: 'Companies - Key Concepts',
    notes: [
      'Company: Legal entity separate from its owners (shareholders).',
      'Limited liability: Shareholders liable only for amount invested.',
      'MOI (Memorandum of Incorporation): Governs company operations.',
      'Board of Directors: Elected by shareholders to manage company.',
      'Share capital: Funds raised by issuing shares.',
      'Dividends: Profit distributed to shareholders (interim and final).',
    ],
  },
  'g12_concepts_audits_governance': {
    title: 'Audits and Corporate Governance',
    notes: [
      'Audit: Independent examination of financial statements.',
      'Unqualified audit: Financial statements fairly presented.',
      'Qualified audit: Exceptions or limitations found.',
      'Corporate governance: System of rules and practices for company control.',
      'King Code: South African corporate governance guidelines.',
      'Stakeholders: Shareholders, employees, customers, community, government.',
    ],
  },

  // Grade 12 Cash Flow Statement
  'g12_cf_reconciliation_note': {
    title: 'Reconciliation of Net Profit to Cash Generated',
    notes: [
      'Start with: Net profit before taxation',
      'Add back: Depreciation (non-cash expense)',
      'Adjust for: Changes in working capital (inventory, receivables, payables)',
      'Increase in current assets → Subtract (cash used)',
      'Decrease in current assets → Add (cash released)',
      'Increase in current liabilities → Add (cash retained)',
      'Decrease in current liabilities → Subtract (cash used)',
      '= Cash generated from operations',
    ],
  },
  'g12_cf_dividends_paid_note': {
    title: 'Dividends Paid Note',
    notes: [
      'Dividends payable at beginning of year',
      'Add: Dividends declared during the year (interim + final)',
      'Less: Dividends payable at end of year',
      '= Dividends paid in cash',
      'OR: Use ledger approach - Dividends on Ordinary Shares account analysis.',
    ],
  },
  'g12_cf_taxation_paid_note': {
    title: 'Taxation Paid Note',
    notes: [
      'SARS (Income tax) at beginning of year (opening balance)',
      'Add: Income tax expense for the year',
      'Less: SARS (Income tax) at end of year (closing balance)',
      '= Taxation paid in cash',
      'Provisional tax payments reduce the amount owed.',
    ],
  },
};

// Helper function to get notes for an archetype key
export const getCurriculumNotes = (archetypeKey) => {
  if (!archetypeKey) return null;
  return curriculumNotesMapping[archetypeKey] || null;
};

// Helper to get notes by question type if archetype key not available
export const getNotesByQuestionType = (questionType, journalType) => {
  const mapping = {
    'retained_income_note': 'g12_fs_retained_income_note_buyback',
    'balance_sheet': 'g12_fs_balance_sheet_companies',
    'income_statement': 'g12_fs_income_statement_basic',
    'bank_reconciliation_statement': 'g11_ct1_q2_brs_statement',
    'crj_format': 'g11_ct1_q2_crj_format',
    'cpj_format': 'g11_ct1_q2_cpj_format',
  };
  
  const key = mapping[journalType] || mapping[questionType];
  return key ? curriculumNotesMapping[key] : null;
};
