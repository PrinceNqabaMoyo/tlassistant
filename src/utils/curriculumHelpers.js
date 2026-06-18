// Curriculum Helper Functions for Question Generation and Customization

/**
 * Journal question template structure
 */
export const journalQuestionTemplate = {
  cash_receipts: {
    type: "journal_entry",
    journal: "cash_receipts",
    scenario: "business_transaction",
    required_entries: [
      { type: "cash_sale", amount: "R500.00", details: "Sale of goods" },
      { type: "bank_deposit", amount: "R500.00", details: "Deposit to bank" }
    ],
    validation_rules: {
      total_debit_equals_total_credit: true,
      bank_equals_income_plus_sundry: true
    }
  },
  cash_payments: {
    type: "journal_entry",
    journal: "cash_payments",
    scenario: "business_expense",
    required_entries: [
      { type: "cash_payment", amount: "R300.00", details: "Purchase of supplies" },
      { type: "bank_withdrawal", amount: "R300.00", details: "Cash withdrawal" }
    ],
    validation_rules: {
      total_debit_equals_total_credit: true,
      bank_equals_expenses_plus_sundry: true
    }
  },
  trial_balance: {
    type: "trial_balance",
    scenario: "end_of_period",
    required_accounts: [
      { name: "Cash", type: "asset", balance: "debit" },
      { name: "Accounts Receivable", type: "asset", balance: "debit" },
      { name: "Accounts Payable", type: "liability", balance: "credit" }
    ],
    validation_rules: {
      total_debits_equal_total_credits: true
    }
  },
  debtors_ledger: {
    type: "ledger_account",
    scenario: "customer_transactions",
    required_entries: [
      { type: "sale", amount: "R1000.00", effect: "increase_debit" },
      { type: "payment", amount: "R600.00", effect: "decrease_debit" }
    ],
    validation_rules: {
      running_balance_correct: true,
      final_balance_accurate: true
    }
  },
  creditors_ledger: {
    type: "ledger_account",
    scenario: "supplier_transactions",
    required_entries: [
      { type: "purchase", amount: "R800.00", effect: "increase_credit" },
      { type: "payment", amount: "R400.00", effect: "decrease_credit" }
    ],
    validation_rules: {
      running_balance_correct: true,
      final_balance_accurate: true
    }
  }
};

/**
 * Question bank for different subjects and topics
 */
export const questionBank = {
  accounting: {
    journals: [
      "Prepare a cash receipts journal for the following transactions...",
      "Record the following cash payments in the cash payments journal...",
      "Post the following transactions to the general journal..."
    ],
    ledgers: [
      "Prepare a debtors ledger account for customer ABC Ltd...",
      "Create a creditors ledger for supplier XYZ Corp...",
      "Post the following transactions to the general ledger..."
    ],
    financial_statements: [
      "Prepare an income statement for the year ended...",
      "Create a balance sheet as at...",
      "Prepare a cash flow statement for..."
    ]
  },
  business_studies: {
    marketing: [
      "Analyze the marketing mix for a new product launch...",
      "Evaluate the effectiveness of different pricing strategies...",
      "Design a marketing campaign for..."
    ],
    management: [
      "Discuss the leadership styles in the following scenario...",
      "Analyze the organizational structure of...",
      "Evaluate the decision-making process for..."
    ],
    entrepreneurship: [
      "Develop a business plan for a new venture...",
      "Analyze the feasibility of starting a business in...",
      "Evaluate the risks and opportunities for..."
    ]
  },
  mathematics: {
    algebra: [
      "Solve the quadratic equation: x² + 5x + 6 = 0",
      "Factorize the expression: 2x² - 7x + 3",
      "Find the roots of the equation: 3x² - 12x + 9 = 0"
    ],
    geometry: [
      "Calculate the area of a circle with radius 5cm",
      "Find the volume of a cylinder with height 10cm and radius 3cm",
      "Determine the perimeter of a rectangle with length 8cm and width 6cm"
    ],
    statistics: [
      "Calculate the mean, median, and mode for the dataset...",
      "Find the standard deviation of the following values...",
      "Create a frequency table for the given data..."
    ]
  }
};

/**
 * Customize a question based on parameters
 * @param {string} baseQuestion - Base question template
 * @param {Object} parameters - Parameters to customize the question
 * @returns {string} Customized question
 */
export const customizeQuestion = (baseQuestion, parameters = {}) => {
  let customizedQuestion = baseQuestion;
  
  // Replace placeholders with actual values
  Object.entries(parameters).forEach(([key, value]) => {
    const placeholder = `{${key}}`;
    customizedQuestion = customizedQuestion.replace(new RegExp(placeholder, 'g'), value);
  });
  
  // Add random variations if specified
  if (parameters.randomize) {
    customizedQuestion = addRandomVariations(customizedQuestion, parameters);
  }
  
  return customizedQuestion;
};

/**
 * Generate a journal question based on type and difficulty
 * @param {string} journalType - Type of journal (cash_receipts, cash_payments, etc.)
 * @param {string} difficulty - Difficulty level (easy, medium, hard)
 * @returns {Object} Generated question with data and validation
 */
export const generateJournalQuestion = (journalType, difficulty = 'medium') => {
  const template = journalQuestionTemplate[journalType];
  if (!template) {
    throw new Error(`Unknown journal type: ${journalType}`);
  }
  
  // Generate sample data based on difficulty
  const sampleData = generateSampleData(journalType, difficulty);
  
  return {
    question: `Prepare a ${journalType.replace('_', ' ')} journal for the following transactions:`,
    template,
    sampleData,
    difficulty,
    validationRules: template.validation_rules
  };
};

/**
 * Generate a business scenario for questions
 * @param {string} subject - Subject area (accounting, business_studies, etc.)
 * @param {string} topic - Specific topic within the subject
 * @param {string} difficulty - Difficulty level
 * @returns {Object} Business scenario with context and questions
 */
export const generateBusinessScenario = (subject, topic, difficulty = 'medium') => {
  const scenarios = {
    accounting: {
      cash_management: {
        easy: "A small retail store has daily cash transactions including sales and purchases.",
        medium: "A medium-sized business manages cash flow with multiple bank accounts and regular reconciliations.",
        hard: "A large corporation handles complex cash management with international transactions and multiple currencies."
      },
      financial_reporting: {
        easy: "Prepare basic financial statements for a sole proprietorship.",
        medium: "Create financial reports for a partnership with multiple revenue streams.",
        hard: "Develop comprehensive financial statements for a corporation with subsidiaries."
      }
    },
    business_studies: {
      marketing: {
        easy: "A local business wants to increase sales in their community.",
        medium: "A regional company is expanding to new markets and needs a marketing strategy.",
        hard: "A multinational corporation is launching a new product line globally."
      },
      operations: {
        easy: "A small restaurant needs to improve their daily operations.",
        medium: "A manufacturing company wants to optimize their production process.",
        hard: "A logistics company needs to redesign their supply chain network."
      }
    }
  };
  
  const subjectScenarios = scenarios[subject];
  if (!subjectScenarios) {
    return {
      scenario: "General business scenario for analysis and problem-solving.",
      difficulty,
      subject,
      topic
    };
  }
  
  const topicScenarios = subjectScenarios[topic];
  if (!topicScenarios) {
    return {
      scenario: `General ${topic} scenario for ${subject} analysis.`,
      difficulty,
      subject,
      topic
    };
  }
  
  return {
    scenario: topicScenarios[difficulty] || topicScenarios.medium || topicScenarios.easy,
    difficulty,
    subject,
    topic
  };
};

/**
 * Helper function to add random variations to questions
 * @param {string} question - Base question
 * @param {Object} parameters - Variation parameters
 * @returns {string} Question with random variations
 */
const addRandomVariations = (question, parameters) => {
  // Add random amounts, dates, or other variables
  if (parameters.includeRandomAmounts) {
    const amounts = ['R100.00', 'R250.00', 'R500.00', 'R750.00', 'R1000.00'];
    const randomAmount = amounts[Math.floor(Math.random() * amounts.length)];
    question = question.replace('{amount}', randomAmount);
  }
  
  if (parameters.includeRandomDates) {
    const currentYear = new Date().getFullYear();
    const randomMonth = Math.floor(Math.random() * 12) + 1;
    const randomDay = Math.floor(Math.random() * 28) + 1;
    const randomDate = `${randomDay.toString().padStart(2, '0')}/${randomMonth.toString().padStart(2, '0')}/${currentYear}`;
    question = question.replace('{date}', randomDate);
  }
  
  return question;
};

/**
 * Helper function to generate sample data for journal questions
 * @param {string} journalType - Type of journal
 * @param {string} difficulty - Difficulty level
 * @returns {Object} Sample data structure
 */
const generateSampleData = (journalType, difficulty) => {
  const baseData = {
    cash_receipts: {
      headers: ['Date', 'Description', 'Debit', 'Credit'],
      rows: [
        ['01/01/2024', 'Cash sales', 'R500.00', ''],
        ['01/01/2024', 'Bank deposit', '', 'R500.00']
      ]
    },
    cash_payments: {
      headers: ['Date', 'Description', 'Debit', 'Credit'],
      rows: [
        ['01/01/2024', 'Purchase of supplies', 'R300.00', ''],
        ['01/01/2024', 'Bank withdrawal', '', 'R300.00']
      ]
    }
  };
  
  const data = baseData[journalType];
  if (!data) {
    return { headers: [], rows: [] };
  }
  
  // Add complexity based on difficulty
  if (difficulty === 'hard') {
    data.rows.push(['02/01/2024', 'Sundry items', 'R100.00', 'R100.00']);
  }
  
  return data;
};
