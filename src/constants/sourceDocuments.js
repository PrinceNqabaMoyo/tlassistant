// Source Documents Repository
export const fallbackSourceDocuments = {
    CPJ: {
        name: "Cash Payments Journal",
        description: "Record all cash payments made by the business",
        columns: ["Date", "Details", "Fol.", "Amount"]
    },
    CRJ: {
        name: "Cash Receipts Journal", 
        description: "Record all cash receipts received by the business",
        columns: ["Date", "Details", "Fol.", "Amount"]
    },
    DJ: {
        name: "Debtors Journal",
        description: "Record all credit sales to customers",
        columns: ["Date", "Customer", "Details", "Fol.", "Amount"]
    },
    CJ: {
        name: "Creditors Journal",
        description: "Record all credit purchases from suppliers",
        columns: ["Date", "Supplier", "Details", "Fol.", "Amount"]
    },
    GL: {
        name: "General Ledger",
        description: "Master record of all accounts with running balances",
        columns: ["Date", "Details", "Fol.", "Debit", "Credit", "Balance"]
    },
    DL: {
        name: "Debtors Ledger",
        description: "Individual customer accounts showing amounts owed",
        columns: [
            "Date",
            "Details/Document no.",
            "Fol.",
            "Debit (+)",
            "Credit (-)",
            "Balance"
        ]
    },
    CL: {
        name: "Creditors Ledger", 
        description: "Individual supplier accounts showing amounts owed",
        columns: [
            "Date",
            "Details/Document no.",
            "Fol.",
            "Debit (-)",
            "Credit (+)",
            "Balance"
        ]
    },
    TB: {
        name: "Trial Balance",
        description: "Summary of all account balances to check for errors",
        columns: ["Account", "Fol.", "Debit", "Credit"]
    },
    DS: {
        name: "Deposit Slip",
        description: "Bank deposit slip for depositing cash and cheques",
        type: "deposit_slip",
        columns: ["Date", "Bank", "Account Number", "Cash Amount", "Cheque Details"]
    },
    CH: {
        name: "Cheque",
        description: "Cheque/cheque counterfoil for making payments",
        type: "cheque",
        columns: ["Date", "Pay To", "Amount", "Bank", "Account Holder"]
    },
    RCPT: {
        name: "Receipt",
        description: "Receipt for payment received",
        type: "receipt",
        columns: ["Receipt No", "Date", "Received From", "Amount", "In Payment Of", "Received By"]
    },
    CASH_INV: {
        name: "Cash Invoice",
        description: "Cash invoice for goods or services purchased",
        type: "cash_invoice",
        columns: ["Invoice No", "Date", "To", "Bought From", "Items", "Total"]
    },
    INC_STMT: {
        name: "Income Statement",
        description: "Income statement for a services business",
        type: "income_statement",
        columns: ["Business Name", "Year Ended", "Income", "Expenses", "Net Profit"]
    },
    TRADING_INC_STMT: {
        name: "Trading Income Statement",
        description: "Income statement for a trading business",
        type: "trading_income_statement",
        columns: ["Business Name", "Year Ended", "Sales", "Cost of Sales", "Net Profit"]
    }
};

// Firebase Configuration
export const firebaseConfig = {
    apiKey: "AIzaSyB1TOAe3SRf9lJRs6R4sjkVBteeXID-Pgg",
    authDomain: "caps-ai-math-assistant-app.firebaseapp.com",
    projectId: "caps-ai-math-assistant-app",
    storageBucket: "caps-ai-math-assistant-app.firebasestorage.app",
    messagingSenderId: "526445100690",
    appId: "1:526445100690:web:add22f0690ebf1d266b04b",
    measurementId: "G-34HG8NYE07"
};

// App Configuration
export const appId = 'fundile-tlassistant-vite';
