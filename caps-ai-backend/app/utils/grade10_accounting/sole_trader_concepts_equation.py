from __future__ import annotations

import random
from typing import Any, Dict, List, Optional

from ..sole_trader.core import calc_cost_price_from_selling_price_and_margin as _calc_cost_price_from_selling_price_and_margin
from ..sole_trader.core import calc_selling_price_from_cost_price_and_margin as _calc_selling_price_from_cost_price_and_margin
from ..sole_trader.core import fmt_money as _fmt_money
from ..sole_trader.core import make_calc as _make_calc
from ..sole_trader.core import make_inline_fill as _make_inline_fill
from ..sole_trader.core import make_match as _make_match
from ..sole_trader.core import make_mcq as _make_mcq
from ..sole_trader.core import make_typed as _make_typed
from ..sole_trader.core import make_word_bank as _make_word_bank
from ..sole_trader.core import round_money as _round_money


def make_unified_concepts_question(*, r: random.Random) -> Dict[str, Any]:
    tf_pool = [
        {"q": "According to historical cost principle, goods purchased must be recorded at cost price.", "a": True},
        {"q": "When a debtor has a credit limit of R10 000, it means that R10 000 is the maximum amount he can spend on goods and services on credit.", "a": False, "cf": "It is the maximum outstanding balance, not maximum spend."},
        {"q": "The prudence principle applies when the business provides for known expenses or losses to avoid the overstating of profit.", "a": True},
        {"q": "To evaluate the debtor's credit worthiness before goods are sold on credit is a good internal control measure that a business applies.", "a": True},
        {"q": "When the total assets of a business exceed its total liabilities, the business is considered insolvent.", "a": False, "cf": "By definition, if assets exceed liabilities, the business is solvent."},
        {"q": "Businesses should always aim to keep their operating expenses as a percentage of turnover as high as possible.", "a": False, "cf": "Businesses aim to keep operating expenses as low as possible to maximize profit."},
        {"q": "The percentage return on owner's equity indicates the owner's return on his investment.", "a": True},
        {"q": "Current assets include items that are expected to be converted into cash within one year.", "a": True},
        {"q": "Non-current liabilities contain debts that will be settled within one year.", "a": False, "cf": "Non-current liabilities are settled over a period longer than one year."},
        {"q": "Creditors for salaries and SARS (PAYE) will be shown under current assets.", "a": False, "cf": "They are current liabilities as they are owed by the business."},
        {"q": "The profitability of a business indicates how efficient the business is.", "a": True},
        {"q": "The main reason why operating profit decreases is interest income.", "a": False, "cf": "Interest income increases profit; rising operating expenses are the main cause of decreasing operating profit."},
        {"q": "Gross profit on cost of sales is calculated to verify the mark-up percentage.", "a": True},
        {"q": "A sole trader business can have more than one owner.", "a": False, "cf": "A sole trader (sole proprietor) is a one-person business with a single owner."},
        {"q": "The financial affairs of the business must be kept separately from the financial affairs of the owners.", "a": True},
        {"q": "Fixed assets are purchased by the business with the aim of reselling them within one year.", "a": False, "cf": "Fixed assets are purchased for use in the business for longer than one year, not for resale."},
        {"q": "Installation costs are part of the cost price of equipment.", "a": True},
        {"q": "A bank overdraft is classified as a non-current liability.", "a": False, "cf": "A bank overdraft is a current liability as it is usually repayable within one year."},
        {"q": "Trading stock is always entered in the books at selling price.", "a": False, "cf": "Trading stock is always entered at cost price."},
        {"q": "Drawings decrease the owner's equity.", "a": True},
        {"q": "Income increases the owner's equity.", "a": True},
        {"q": "Operating expenses are part of the daily transactions that happen in the business.", "a": True},
        {"q": "Interest on a fixed deposit is classified as an operating income.", "a": False, "cf": "Interest on a fixed deposit is not part of the daily activities and is therefore not an operating income."},
        {"q": "A journal is known as the book of first entry because it is the first place a transaction is recorded from a source document.", "a": True},
        {"q": "The going concern concept means that the business will continue to exist for the foreseeable future.", "a": True},
        {"q": "The matching principle states that income and expenses incurred during a financial period must be recorded in that period, regardless of when cash is received or paid.", "a": True},
    ]

    mcq_pool = [
        {
            "q": "An example of a non-current asset is:",
            "options": ["Trading stock", "Bank", "Debtors", "Fixed Deposit"],
            "ans": 3
        },
        {
            "q": "A summary of balances and totals extracted from all the ledger accounts of a business is known as:",
            "options": ["Balance Sheet", "Income Statement", "Trial Balance", "General Ledger"],
            "ans": 2
        },
        {
            "q": "Assets that are convertible into cash within a period of 12 months are defined as:",
            "options": ["Current Assets", "Property, Plant & Equipment", "Equity", "Liabilities"],
            "ans": 0
        },
        {
            "q": "Commonly accepted guidelines that are followed when financial records are prepared for reporting are:",
            "options": ["IFRS", "Internal Control", "Historical Cost", "GAAP"],
            "ans": 3
        },
        {
            "q": "Owner's equity is defined as the:",
            "options": ["Total assets minus current liabilities", "Owner's net investment in the business", "Total liabilities", "Profit made during the year"],
            "ans": 1
        },
        {
            "q": "The historical cost principle dictates that:",
            "options": ["Fixed assets purchased are recorded at their cost price", "Financial statements are prepared in a conservative manner", "All expenses are subtracted from income", "Only historical events are recorded"],
            "ans": 0
        },
        {
            "q": "A bank overdraft occurs when:",
            "options": ["More money is withdrawn than is available", "The bank refuses to clear a cheque", "The business invests in a fixed deposit", "A client bounces a cheque"],
            "ans": 0
        },
        {
            "q": "A Credit term is:",
            "options": ["The maximum amount a debtor is allowed to buy", "The amount of time a debtor is allowed to take to pay off their account", "The interest charged on a debt", "A credit card limit"],
            "ans": 1
        },
        {
            "q": "A Credit limit is:",
            "options": ["The limit a bank places on an overdraft", "The time limit applied to a debt payment", "The maximum amount a debtor is allowed to buy goods on credit", "The minimum cash holding allowed"],
            "ans": 2
        },
        {
            "q": "The document attached to the document used to pay a supplier using money in the business bank account:",
            "options": ["Debit note", "Receipt", "Invoice", "Cheque counterfoil"],
            "ans": 3
        },
        {
            "q": "Money the owner gives to start the business is called:",
            "options": ["Drawings", "Loans", "Income", "Capital"],
            "ans": 3
        },
        {
            "q": "Basic salary plus birthday bonus equates to:",
            "options": ["Net salary", "PAYE", "Gross salary", "Deductions"],
            "ans": 2
        },
        {
            "q": "Telephone is classified as a/an … account.",
            "options": ["Balance sheet", "Asset", "Expense", "Income"],
            "ans": 2
        },
        {
            "q": "People who owe the business money are known as:",
            "options": ["Debtors", "Creditors", "Bankers", "Wholesalers"],
            "ans": 0
        },
        {
            "q": "Which of the following is NOT a non-current asset?",
            "options": ["Land and buildings", "Trading stock", "Vehicles", "Equipment"],
            "ans": 1
        },
        {
            "q": "Profits generated by the business will always increase:",
            "options": ["Owner's equity", "Assets only", "Creditors", "Cash only"],
            "ans": 0
        },
        {
            "q": "Which source document is used to record goods purchased on credit?",
            "options": ["Original invoice", "Duplicate invoice", "Receipt", "Cheque counterfoil"],
            "ans": 0
        },
        {
            "q": "An example of a current asset is:",
            "options": ["Vehicles", "Land and buildings", "Trading stock", "Equipment"],
            "ans": 2
        },
        {
            "q": "The management should report all relevant information honestly and on time. This principle is called:",
            "options": ["Accountability", "Transparency", "Prudence", "Materiality"],
            "ans": 1
        },
        {
            "q": "Debts that are repayable within a period of 12 months are classified as:",
            "options": ["Non-current liabilities", "Current liabilities", "Owner's equity", "Non-current assets"],
            "ans": 1
        },
        {
            "q": "Investments such as a fixed deposit at 8% p.a. interest over 5 years is classified as:",
            "options": ["Current asset", "Non-current asset", "Current liability", "Owner's equity"],
            "ans": 1
        },
        {
            "q": "A mortgage bond to finance the purchase of new property is classified as:",
            "options": ["Current liability", "Non-current liability", "Non-current asset", "Owner's equity"],
            "ans": 1
        },
        {
            "q": "The source document used when goods are returned to a supplier is:",
            "options": ["Credit note", "Debit note", "Receipt", "Invoice"],
            "ans": 1
        },
        {
            "q": "The action taken by the business to prevent fraud, losses and to ensure that the business achieves its aims and goals is called:",
            "options": ["GAAP", "Internal control", "Prudence", "Audit"],
            "ans": 1
        },
        {
            "q": "The employer must deduct income tax from employees' salaries. This deduction is known as:",
            "options": ["UIF", "PAYE", "VAT", "Drawings"],
            "ans": 1
        },
        {
            "q": "The discount allowed to a debtor for early payment is classified as:",
            "options": ["Income", "An expense", "A liability", "An asset"],
            "ans": 1
        },
        {
            "q": "Other businesses to which the business owes money for purchasing stock are called:",
            "options": ["Debtors", "Creditors", "Shareholders", "Partners"],
            "ans": 1
        },
        {
            "q": "Assets that have a reasonably long life span are called:",
            "options": ["Current assets", "Financial assets", "Fixed assets", "Intangible assets"],
            "ans": 2
        },
        {
            "q": "A deduction offered by a supplier to promote bulk purchases is called:",
            "options": ["Cash discount", "Trade discount", "Settlement discount", "Quantity rebate"],
            "ans": 1
        },
        {
            "q": "Where transactions are recorded before they are posted to the General Ledger:",
            "options": ["Trial Balance", "Financial Statements", "Subsidiary Journals", "Source Documents"],
            "ans": 2
        },
        {
            "q": "A record of items that are bought for a small amount of money is kept in the:",
            "options": ["General Journal", "Cash Payments Journal", "Petty Cash Journal", "Cash Receipts Journal"],
            "ans": 2
        },
        {
            "q": "Money withdrawn by the owner from the business for personal use is called:",
            "options": ["Capital", "Drawings", "Expenses", "Income"],
            "ans": 1
        },
        {
            "q": "Serves as a source of information when preparing financial records:",
            "options": ["Trial Balance", "Ledger account", "Source document", "Financial Statements"],
            "ans": 2
        },
        {
            "q": "Money borrowed in order to purchase a property is called a:",
            "options": ["Fixed deposit", "Mortgage loan", "Bank overdraft", "Capital contribution"],
            "ans": 1
        },
        {
            "q": "For every debit there is a corresponding credit. This is known as the:",
            "options": ["Matching principle", "Going concern concept", "Double entry principle", "Prudence principle"],
            "ans": 2
        },
        {
            "q": "Money tied up for a period of time in order to earn a higher return is known as:",
            "options": ["Savings account", "Bank overdraft", "Investments (Fixed deposit)", "Trading stock"],
            "ans": 2
        },
        {
            "q": "The owner uses a business cheque to pay his personal insurance expense. This transaction is classified as:",
            "options": ["Capital", "Drawings", "Operating expense", "Current liability"],
            "ans": 1
        },
        {
            "q": "Equipment purchased for use in the business is classified as:",
            "options": ["Current asset", "Non-current asset", "Current liability", "Operating expense"],
            "ans": 1
        },
        {
            "q": "The owner invests additional funds to run the business. This is classified as:",
            "options": ["Income", "Drawings", "Capital", "Loan"],
            "ans": 2
        },
    ]

    typed_pool = [
        {
            "p": "Explain the term 'Credit term'.",
            "sa": "The amount of time a debtor is allowed to take to pay off his/her account."
        },
        {
            "p": "Explain the term 'Credit limit'.",
            "sa": "The maximum amount a debtor is allowed to buy goods on credit, or the maximum outstanding balance permitted."
        },
        {
            "p": "Define the term 'GAAP' (Generally Accepted Accounting Practice).",
            "sa": "GAAP is a collection of rules, procedures and guidelines for accountants to follow when recording and reporting financial information, ensuring that financial statements are accurate, relevant and reliable."
        },
        {
            "p": "Explain the historical cost principle.",
            "sa": "The historical cost principle states that assets purchased by a business must be recorded in the books at cost price (purchased price), not at their current market value."
        },
        {
            "p": "Explain the prudence (conservatism) principle.",
            "sa": "The prudence principle states that accountants should be conservative when preparing financial statements and should take care not to overstate assets or income and not to understate liabilities and expenses."
        },
        {
            "p": "Explain the business entity rule.",
            "sa": "The business entity rule states that the financial affairs of the business must be kept separately from the financial affairs of the owners. The business is treated as a separate entity."
        },
        {
            "p": "Explain the going concern concept.",
            "sa": "The going concern concept means that the financial statements of a business are prepared based on the assumption that the business will continue to operate for the foreseeable future."
        },
        {
            "p": "Explain the matching principle.",
            "sa": "The matching principle states that income and expenses incurred during a certain financial period must be recorded in that period, regardless of when cash is received or paid."
        },
        {
            "p": "Explain the materiality principle.",
            "sa": "The materiality principle states that all important (significant) transactions and events should be indicated separately in the Financial Statements as these may influence decision-making. Insignificant amounts may be grouped together."
        },
        {
            "p": "What is the difference between a sole trader and a partnership?",
            "sa": "A sole trader is a one-person business where the owner has full control and receives all profits. A partnership has 2 to 20 partners who share control and split profits amongst themselves."
        },
        {
            "p": "What is the difference between a service business and a retailing business?",
            "sa": "A service business earns income by providing services (e.g. doctors, plumbers). A retailing business buys finished products, adds a profit margin, and sells them to customers (e.g. grocery store)."
        },
        {
            "p": "Explain what 'owner's equity' means.",
            "sa": "Owner's equity is the money or capital invested in the business by the owner. It represents the owner's interest in the business and is calculated as total assets minus total liabilities."
        },
        {
            "p": "Explain what 'drawings' means in accounting.",
            "sa": "Drawings refers to money, fixed assets, or trading stock withdrawn by the owner from the business for personal use. Drawings decrease the owner's equity."
        },
        {
            "p": "What is a fixed deposit?",
            "sa": "A fixed deposit is money invested at a financial institution for a certain period at a fixed interest rate. The original amount is classified as a financial asset (non-current asset)."
        },
        {
            "p": "What is internal control?",
            "sa": "Internal control refers to the policies and procedures a business implements to prevent fraud, reduce losses, and ensure that the business achieves its aims and goals."
        },
        {
            "p": "What is credit control?",
            "sa": "Credit control refers to the policies and procedures aimed at controlling and managing the granting of credit to debtors, including setting credit limits and credit terms."
        },
        {
            "p": "Name and explain three examples of current assets.",
            "sa": "1) Trading stock – goods acquired for resale. 2) Debtors – people who owe money to the business for goods sold on credit. 3) Bank – money in the business's bank account (favourable/debit balance)."
        },
        {
            "p": "Name and explain two examples of current liabilities.",
            "sa": "1) Creditors – suppliers to whom the business owes money for goods bought on credit. 2) Bank overdraft – when the business has withdrawn more than the available balance, making the bank a liability."
        },
    ]

    full_cycle_steps = [
        "Transactions take place",
        "Source documents are created",
        "Record transactions in subsidiary journals",
        "Post from journals to ledgers",
        "Prepare a trial balance",
        "Prepare financial statements",
    ]

    gaap_scenario_pool = [
        {"q": "Vehicles are kept at original cost price in the general ledger. Which GAAP principle applies?", "sa": "Historical Cost Concept"},
        {"q": "Incomes and expenses incurred for a particular year must be shown in the same financial year. Which GAAP principle applies?", "sa": "Matching Concept"},
        {"q": "Bank charges and interest on bank overdraft are shown separately in the financial statements. Which GAAP principle applies?", "sa": "Materiality Concept"},
        {"q": "Stock for the owner's personal use is shown as drawings. Which GAAP principle applies?", "sa": "Business Entity Rule"},
        {"q": "Money lost due to theft of stock is written off, even though there is a possibility it may be recovered. Which GAAP principle applies?", "sa": "Prudence Concept"},
        {"q": "Business letterheads printed for two years in advance are recorded as consumable stores on hand. Which GAAP principle applies?", "sa": "Going Concern Concept"},
        {"q": "Property is recorded at R5 million in the financial statements, but the market value is R7.5 million. Which GAAP principle applies?", "sa": "Historical Cost Concept"},
        {"q": "The owner's fuel costs are paid by the business but recorded as drawings. Which GAAP principle applies?", "sa": "Business Entity Rule"},
        {"q": "A tenant paid R39 000 for rent, which includes one month of the following year. Only R36 000 is recorded in the Profit and Loss Account. Which GAAP principle applies?", "sa": "Matching Concept"},
        {"q": "Consumable stores worth R7 500 are written off because they cannot be found in the storeroom. Which GAAP principle applies?", "sa": "Prudence Concept"},
    ]

    classification_pool = [
        {"q": "Classify 'Vehicles' in the financial statements.", "sa": "Fixed asset (non-current asset)"},
        {"q": "Classify 'Capital' in the financial statements.", "sa": "Owner's equity"},
        {"q": "Classify 'Cost of sales' in the financial statements.", "sa": "Expense"},
        {"q": "Classify 'Bank overdraft' in the financial statements.", "sa": "Current liability"},
        {"q": "Classify 'Fixed deposit' in the financial statements.", "sa": "Financial asset (non-current asset)"},
        {"q": "Classify 'Equipment' in the financial statements.", "sa": "Fixed asset (non-current asset)"},
        {"q": "Classify 'Loan' in the financial statements.", "sa": "Non-current liability"},
        {"q": "Classify 'Sales' in the financial statements.", "sa": "Income"},
        {"q": "Classify 'Interest on fixed deposit' in the financial statements.", "sa": "Income"},
        {"q": "Classify 'Creditors' control' in the financial statements.", "sa": "Current liability"},
        {"q": "Classify 'Debtors' control' in the financial statements.", "sa": "Current asset"},
        {"q": "Classify 'Trading stock' in the financial statements.", "sa": "Current asset"},
        {"q": "Classify 'Interest on loan' in the financial statements.", "sa": "Expense"},
        {"q": "Classify 'Stationery' in the financial statements.", "sa": "Expense"},
        {"q": "Classify 'Packing material' in the financial statements.", "sa": "Expense"},
    ]

    fill_blank_pool = [
        {"parts": ["Trading stock is always entered in the books at ", "."], "blanks": ["cost price"]},
        {"parts": ["Land and buildings will be shown in the books at the purchased price. This principle is called ", "."], "blanks": ["historical cost"]},
        {"parts": ["Income and expenses have an influence on the ", " of the business."], "blanks": ["equity", "owner's equity"]},
        {"parts": ["Persons to whom the business owes money are known as ", "."], "blanks": ["creditors"]},
        {"parts": ["An asset purchased by the business with the aim of converting it into cash within one year is a ", " asset."], "blanks": ["current"]},
        {"parts": ["If the bank balance is overdrawn, it is classified as a ", "."], "blanks": ["current liability"]},
        {"parts": ["'The bookkeeping of the business and that of the owner should be kept strictly separate.' This principle is called the ", "."], "blanks": ["business entity rule"]},
        {"parts": ["The aim of any business is to make ", "."], "blanks": ["profit"]},
        {"parts": ["A business that buys finished products, adds a profit and sells them to make a profit is called a ", " business."], "blanks": ["retail", "retailing"]},
        {"parts": ["Non-current assets consist of ", " assets and ", " assets."], "blanks": ["tangible", "financial"]},
    ]

    match_pool = [
        [
            {"left": "An example of a non-current asset: ", "right": "Fixed Deposit"},
            {"left": "Management should treat employees equally regardless of positions: ", "right": "Fairness"},
            {"left": "A summary of balances extracted from all the ledger accounts: ", "right": "Trial Balance"},
            {"left": "Assets convertible to cash within 12 months: ", "right": "Current Assets"},
            {"left": "Commonly accepted guidelines for reporting: ", "right": "GAAP"}
        ],
        [
            {"left": "Historical cost principle", "right": "Fixed assets purchased are recorded at their cost price"},
            {"left": "Owner's equity", "right": "Owner's net investment in the business"},
            {"left": "Prudence principle", "right": "Financial statements are prepared in a conservative manner"},
            {"left": "Bank overdraft", "right": "When more money is withdrawn than is available in the bank account"},
            {"left": "PAYE", "right": "A payment made to the South African Revenue Service"}
        ],
        [
            {"left": "Cheque counterfoil", "right": "Used to make payments from the business bank account"},
            {"left": "Receipt", "right": "Issued when money is received from a tenant"},
            {"left": "Original invoice", "right": "Received from a creditor for purchase of goods on credit"},
            {"left": "Duplicate invoice", "right": "Record of the sales of goods on credit to a debtor"},
            {"left": "Debit note", "right": "Issued when goods are returned to a supplier"}
        ]
    ]

    calc_pool = [
        {"type": "sp_from_cp_margin"},
        {"type": "cp_from_sp_margin"}
    ]

    word_bank_pool = [
        {
            "parts": [
                "The ", " principle requires that assets be recorded at their original purchase price. Providing for known expenses or losses to avoid overstating profit is an example of the ", " principle. If we make sure to keep the owner's personal expenses out of the business books, we are following the ", " rule."
            ],
            "blanks": ["historical cost", "prudence", "business entity"],
            "distractors": ["materiality", "going concern", "matching"]
        },
        {
            "parts": [
                "The basic accounting equation states that ", " equals total ", " plus total ", "."
            ],
            "blanks": ["Assets", "Owner's Equity", "Liabilities"],
            "distractors": ["Income", "Expenses", "Drawings"]
        }
    ]

    q_choice = r.choices(
        ["mcq", "tf", "typed", "gaap_scenario", "classification", "fill_blank", "cycle_order", "match", "word_bank", "calc"],
        weights=[15, 10, 5, 5, 5, 10, 5, 10, 10, 25],
        k=1,
    )[0]

    if q_choice == "mcq":
        item = r.choice(mcq_pool)
        options = item["options"][:]
        correct_opt = options[item["ans"]]
        r.shuffle(options)
        new_ans_idx = options.index(correct_opt)
        return _make_mcq(prompt=item["q"], options=options, correct_index=new_ans_idx, explanation="")

    elif q_choice == "tf":
        item = r.choice(tf_pool)
        return _make_mcq(
            prompt="True or False? " + item["q"],
            options=["True", "False"],
            correct_index=0 if item["a"] else 1,
            explanation=item.get("cf", "")
        )

    elif q_choice == "gaap_scenario":
        item = r.choice(gaap_scenario_pool)
        return _make_typed(prompt=item["q"], sample_answer=item["sa"])

    elif q_choice == "classification":
        item = r.choice(classification_pool)
        return _make_typed(prompt=item["q"], sample_answer=item["sa"])

    elif q_choice == "fill_blank":
        item = r.choice(fill_blank_pool)
        return _make_inline_fill(
            prompt="Fill in the missing word(s):",
            text_parts=item["parts"],
            blanks=item["blanks"]
        )

    elif q_choice == "cycle_order":
        num_steps = r.choice([4, 5, 6])
        selected = full_cycle_steps[:num_steps]
        shuffled = selected[:]
        r.shuffle(shuffled)
        prompt_lines = "Put these steps of the accounting cycle in the correct order (write them as a numbered list):\n\n"
        prompt_lines += "\n".join(f"- {s}" for s in shuffled)
        answer_lines = "\n".join(f"{i+1}) {s}" for i, s in enumerate(selected))
        return _make_typed(prompt=prompt_lines, sample_answer=answer_lines)

    elif q_choice == "calc":
        item = r.choice(calc_pool)
        margin = r.choice([20, 25, 33.33, 50, 60, 100])
        val = float(r.randint(8, 60)) * 1000

        if item["type"] == "sp_from_cp_margin":
            cp = val
            sp = _calc_selling_price_from_cost_price_and_margin(cp=cp, profit_margin_pct=margin)
            prompt = f"If a business purchases goods for R{cp:,.0f} and the profit margin is {margin:g}%, calculate the selling price."
            d_val = f"Cost Price = R{cp:,.0f}\nMark-up = {margin:g}%\nSelling Price = R{cp:,.0f} x (1 + {margin:g}/100) = R{sp:,.0f}"
            return _make_calc(prompt=prompt, correct_value=sp, unit="R", derivation_map={"value": d_val})
        else:
            sp = val
            cp = _calc_cost_price_from_selling_price_and_margin(sp=sp, profit_margin_pct=margin)
            prompt = f"If a business sells goods for R{sp:,.0f} and the profit margin is {margin:g}%, determine the cost price."
            d_val = f"Selling Price = R{sp:,.0f}\nMark-up = {margin:g}%\nCost Price = R{sp:,.0f} x 100 / (100 + {margin:g}) = R{cp:,.0f}"
            return _make_calc(prompt=prompt, correct_value=cp, unit="R", derivation_map={"value": d_val})

    elif q_choice == "match":
        pairs_list = r.choice(match_pool)
        r.shuffle(pairs_list)
        subset = pairs_list[:4]
        return _make_match(prompt="Match the items in Column A with the correct description in Column B by clicking to link them.", pairs=subset)

    elif q_choice == "word_bank":
        item = r.choice(word_bank_pool)
        all_words = item["blanks"] + item["distractors"]
        r.shuffle(all_words)
        return _make_word_bank(
            prompt="Fill in the blanks using the word bank provided.",
            text_parts=item["parts"],
            blanks=item["blanks"],
            word_bank=all_words
        )

    else:
        item = r.choice(typed_pool)
        return _make_typed(prompt=item["p"], sample_answer=item["sa"])


def make_transaction_analysis_template_text(
    *,
    name: str,
    rows: List[Dict[str, Any]],
    markup_pct: float,
    debtor: str,
    creditor: str,
) -> str:
    first = rows[0] if rows else {}
    second = rows[1] if len(rows) > 1 else {}
    amount0 = float(first.get("amount") or 0.0)
    amount1 = float(second.get("amount") or 0.0)
    sub_dr0 = str(first.get("sub_dr") or "").strip()
    sub_cr0 = str(first.get("sub_cr") or "").strip()

    if name in {"cash_sales_crj", "cash_sales_cost"}:
        return f"Sold goods for cash according to the cash register roll. The cost price was R{_fmt_money(amount1)} and the business applies a mark-up of {int(markup_pct)}% on cost."
    if name == "credit_sales_dj":
        return f"Sold goods on credit for R{_fmt_money(amount0)}. The cost price of the goods sold was R{_fmt_money(amount1)}."
    if name in {"debtor_settlement_crj", "debtor_settlement_discount_source"}:
        owed = _round_money(amount0 + amount1)
        return f"Received R{_fmt_money(amount0)} from a debtor in settlement of an account of R{_fmt_money(owed)} after allowing a discount of R{_fmt_money(amount1)}."
    if name == "creditor_payment_cpj":
        owed = _round_money(amount0 + amount1)
        return f"Paid a creditor R{_fmt_money(amount0)} in settlement of an account of R{_fmt_money(owed)} after receiving a discount of R{_fmt_money(amount1)}."
    if name in {"bank_charges_cpj", "bank_charges_source"}:
        return f"The bank statement reflected bank charges of R{_fmt_money(amount0)}."
    if name == "interest_income_crj":
        return f"The bank statement reflected interest income of R{_fmt_money(amount0)}."
    if name in {"rent_received_crj", "rent_received_eft"}:
        return f"Received rent income of R{_fmt_money(amount0)}."
    if name == "fee_income_credit":
        return f"Charged a debtor fee income of R{_fmt_money(amount0)} on credit."
    if name in {"loan_received_crj", "loan_received_source"}:
        return f"Received a loan of R{_fmt_money(amount0)} from the bank."
    if name == "insurance_accrued_gj":
        return f"Insurance of R{_fmt_money(amount0)} is owing and must be accrued."
    if name == "interest_overdue_debtor_gj":
        return f"Charged interest on an overdue debtor account amounting to R{_fmt_money(amount0)}."
    if name == "bad_debt_writeoff_gj":
        return f"Wrote off a debtor's account as bad debts, R{_fmt_money(amount0)}."
    if name == "bad_debt_recovered_crj":
        return f"Received R{_fmt_money(amount0)} from a debtor whose account had previously been written off as bad debts."
    if name == "drawings_stock_gj":
        return f"The owner withdrew trading stock for personal use at cost price R{_fmt_money(amount0)}."
    if name == "petty_cash_on_behalf_debtor":
        return f"Paid R{_fmt_money(amount0)} out of petty cash on behalf of debtor {first.get('debtor_name') or debtor}; the amount must be debited to the debtor's account."
    if name == "capital_contribution_crj":
        return f"The owner increased capital by depositing R{_fmt_money(amount0)} into the business bank account."
    if name == "rd_cheque_gj":
        total = _round_money(amount0 + amount1)
        return f"An R/D cheque for R{_fmt_money(total)} previously received from a debtor was returned by the bank."
    if name == "interest_overdue_creditor_gj":
        return f"A creditor charged interest on the overdue account amounting to R{_fmt_money(amount0)}."
    if name == "loan_repayment_interest_cpj":
        total = _round_money(amount0 + amount1)
        return f"Paid a loan instalment of R{_fmt_money(total)}, which included interest of R{_fmt_money(amount1)}."
    if name == "purchase_credit_cj":
        return f"Purchased trading stock on credit for R{_fmt_money(amount0)} after trade discount."
    if name == "purchase_cheque_cpj":
        return f"Purchased trading stock by cheque for R{_fmt_money(amount0)} after trade discount."
    if name == "debtor_allowance_daj":
        return f"Issued a credit note to a debtor for goods returned. The selling price was R{_fmt_money(amount0)} and the cost price was R{_fmt_money(amount1)}."
    if name == "creditor_allowance_caj":
        return f"Returned goods to a creditor and received an allowance of R{_fmt_money(amount0)}."
    if name in {"equipment_credit_cj", "equipment_credit"}:
        return f"Purchased equipment on credit for R{_fmt_money(amount0)}."
    if name == "equipment_cash_cpj":
        return f"Issued a cheque for the purchase of equipment, R{_fmt_money(amount0)}."
    if name == "petty_cash_transfer":
        return f"Issued a cheque for R{_fmt_money(amount0)} to increase petty cash."
    if name == "wages_eft_internal":
        return f"Paid wages of R{_fmt_money(amount0)} via EFT."
    if name == "rent_debit_order_internal":
        return f"Paid rent of R{_fmt_money(amount0)} by debit order."
    if name == "insurance_stop_order_internal":
        return f"Paid insurance of R{_fmt_money(amount0)} by stop order."
    if name == "stock_credit_with_delivery_subledger":
        supplier_name = sub_cr0 or creditor
        return f"Purchased trading stock on credit from {supplier_name} for R{_fmt_money(amount0)}, including delivery charges where applicable."
    if name == "credit_sale_subledger":
        debtor_name = sub_dr0 or debtor
        return f"Sold goods on credit to {debtor_name} for R{_fmt_money(amount0)}."
    if name == "stationery_error_correction":
        return f"Correct an error where stationery of R{_fmt_money(amount0)} had been posted to Trading stock."
    if name == "equipment_return_damaged":
        return f"Returned damaged equipment bought on credit for R{_fmt_money(amount0)}."
    if name == "consumable_petty_cash":
        return f"Bought consumable stores for R{_fmt_money(amount0)} and paid from petty cash."
    if name == "insolvent_debtor_dividend_writeoff":
        owed0 = float(first.get("owed") or 0.0)
        cents0 = float(first.get("cents_in_rand") or 0.0)
        return f"A debtor owing R{_fmt_money(owed0)} was declared insolvent. The business received {cents0:g} cents in the rand as a final dividend and the balance must be written off as bad debts."
    if name == "debtor_settlement_discount_unfavourable":
        owed = _round_money(amount0 + amount1)
        return f"Received R{_fmt_money(amount0)} from a debtor in settlement of an account of R{_fmt_money(owed)} after allowing a discount of R{_fmt_money(amount1)}. The bank balance is unfavourable for this transaction."
    if name == "overdraft_interest":
        return f"The bank statement reflected interest on overdraft of R{_fmt_money(amount0)}."

    dr0 = str(first.get("dr") or "").strip()
    cr0 = str(first.get("cr") or "").strip()
    return f"Analyse a transaction affecting {dr0} and {cr0} for R{_fmt_money(amount0)}."


def transaction_rows_compatible(
    *,
    rows: List[Dict[str, Any]],
    requires_source: bool,
    requires_journal: bool,
    requires_internal: bool,
    requires_subledger: bool,
    has_amount: bool,
) -> bool:
    if requires_source and not any(str(t.get("source") or "").strip() for t in rows):
        return False
    if requires_journal and not any(str(t.get("journal") or "").strip() for t in rows):
        return False
    if requires_internal and not any(str(t.get("internal") or "").strip() for t in rows):
        return False
    if requires_subledger and not any(str(t.get("sub_dr") or "").strip() or str(t.get("sub_cr") or "").strip() for t in rows):
        return False
    if has_amount and not any(t.get("amount") is not None for t in rows):
        return False
    return True


def _transaction_analysis_effect_hint(component_label: str, display_value: str, t: Dict[str, Any]) -> str:
    disp0 = str(display_value or "").strip()
    dr0 = str(t.get("dr") or "").strip()
    cr0 = str(t.get("cr") or "").strip()
    a0 = float(t.get("a") or 0.0)
    o0 = float(t.get("o") or 0.0)
    l0 = float(t.get("l") or 0.0)
    comp_norm = component_label.strip().lower()
    if comp_norm == "assets":
        pos_reason = dr0
        neg_reason = cr0
        raw_value = a0
    elif comp_norm == "owner's equity":
        pos_reason = cr0
        neg_reason = dr0
        raw_value = o0
    else:
        pos_reason = cr0
        neg_reason = dr0
        raw_value = l0
    if not disp0 or disp0 == "0":
        return f"{component_label}: no change for this row."
    if any(tok in disp0 for tok in ["+/-", "-/+", "±"]):
        inc_reason = pos_reason or dr0 or "one account"
        dec_reason = neg_reason or cr0 or "another account"
        return f"{component_label} show {disp0} because {inc_reason} increases while {dec_reason} decreases in the same row."
    if disp0.startswith("+") or raw_value > 0:
        why0 = pos_reason or "the related account"
        return f"{component_label} increase on this row because {why0} increases."
    if disp0.startswith("-") or raw_value < 0:
        why0 = neg_reason or "the related account"
        return f"{component_label} decrease on this row because {why0} decreases."
    return f"Enter the {component_label.lower()} effect exactly as {disp0}."


def _transaction_analysis_journal_purpose_text(journal_code: str) -> str:
    code = str(journal_code or "").strip().upper()
    purposes = {
        "CRJ": "The Cash Receipts Journal records money received by the business.",
        "CPJ": "The Cash Payments Journal records payments made from the business bank account.",
        "DJ": "The Debtors Journal records credit sales to debtors.",
        "DAJ": "The Debtors Allowances Journal records returns and allowances granted to debtors.",
        "CJ": "The Creditors Journal records purchases on credit from suppliers.",
        "CAJ": "The Creditors Allowances Journal records returns and allowances received from creditors.",
        "GJ": "The General Journal records transactions that do not fit into the specialised journals, such as corrections and adjustments.",
        "PCJ": "The Petty Cash Journal records small payments made from petty cash.",
    }
    return purposes.get(code, f"{code} is the correct journal for this type of transaction." if code else "Use the journal that matches the type of transaction.")


def build_transaction_analysis_teaching_hint(
    *,
    header_label: str,
    value: Optional[str],
    t: Dict[str, Any],
    row_hint: str,
    transaction_line: str,
) -> Dict[str, str]:
    header0 = str(header_label or "").strip()
    header_norm = header0.lower()
    value0 = "" if value is None else str(value).strip()
    tx0 = str(transaction_line or "").strip()
    src0 = str(t.get("source") or "").strip()
    jr0 = str(t.get("journal") or "").strip()
    internal0 = str(t.get("internal") or "").strip()
    dr0 = str(t.get("dr") or "").strip()
    cr0 = str(t.get("cr") or "").strip()
    sub_dr0 = str(t.get("sub_dr") or "").strip()
    sub_cr0 = str(t.get("sub_cr") or "").strip()
    row_hint0 = str(row_hint or "").strip()

    role = ""
    evidence = f"Use the information in transaction {tx0}." if tx0 else "Use the information given in the transaction row."
    rule = ""
    method = row_hint0
    transfer_tip = ""

    if header_norm == "no.":
        role = "This cell labels the transaction number so you can match the table row to the correct transaction in the requirement."
        evidence = f"The transaction number is shown at the start of the transaction: {tx0}." if tx0 else evidence
        rule = "Copy the transaction number exactly so the analysis row matches the correct narrative item."
        method = f"Read the number attached to the transaction and enter that same number here. The correct number is {value0}." if value0 else method
        transfer_tip = "In similar questions, locate the transaction number first before filling the rest of the row."
    elif header_norm == "source document":
        role = "This cell identifies the source document from which the transaction is first recorded."
        evidence = f"The transaction describes an event supported by the source document {src0}." if src0 else evidence
        rule = "A source document is the proof of the transaction and is used before the transaction is entered in a journal."
        method = f"Ask which document would be issued or received for this event. For this row the correct source document is {src0}." if src0 else "Decide which document proves that the transaction took place, then enter that document name."
        transfer_tip = "In similar questions, identify whether the event was a cash receipt, payment, credit purchase, credit sale, return, or adjustment, then link it to its source document."
    elif header_norm == "subsidiary journal":
        role = "This cell shows which specialised journal should record the transaction before posting to the ledger."
        evidence = f"The transaction is of the type recorded in the {jr0}." if jr0 else evidence
        rule = _transaction_analysis_journal_purpose_text(jr0)
        method = f"Classify the transaction first, then select the journal used for that class of transaction. Here the correct journal is {jr0}." if jr0 else "Classify the transaction before choosing the correct journal."
        transfer_tip = "In similar questions, decide first whether the transaction is a receipt, payment, credit sale, credit purchase, allowance, or adjustment, then choose the journal."
    elif header_norm == "internal document":
        role = "This cell identifies the internal document or internal reference used inside the business for the transaction."
        evidence = f"The transaction itself points to the internal document {internal0 or src0}." if (internal0 or src0) else evidence
        rule = "Internal documents are created inside the business and can also be used as evidence for entries."
        method = f"Use the internal reference given in the transaction. Here it is {internal0 or src0}." if (internal0 or src0) else "Look for the internal document named in the transaction and copy it here."
        transfer_tip = "In similar questions, distinguish between documents received from outside parties and documents created inside the business."
    elif header_norm in {"account debited", "gl dr"}:
        role = "This cell names the General Ledger account that must be debited for this row."
        evidence = f"In transaction {tx0}, the account receiving the value or expense on this entry is {dr0}." if (tx0 and dr0) else evidence
        rule = "Debit the account that receives the benefit, asset, or expense on this specific entry."
        method = f"Ask what comes into the business, what expense is incurred, or which account must increase on the debit side. For this row that account is {dr0}. {row_hint0}".strip() if dr0 else method
        transfer_tip = "In similar questions, identify the two accounts first, then decide which one is the debit before writing the credit account."
    elif header_norm in {"account credited", "gl cr"}:
        role = "This cell names the General Ledger account that must be credited for this row."
        evidence = f"In transaction {tx0}, the account giving the value or creating the source of the entry is {cr0}." if (tx0 and cr0) else evidence
        rule = "Credit the account that gives value, reduces an asset, or increases income, equity, or liabilities on this specific entry."
        method = f"After identifying the debit account, decide which account is on the credit side of the same entry. For this row that account is {cr0}. {row_hint0}".strip() if cr0 else method
        transfer_tip = "In similar questions, never choose debit and credit in isolation; work them out as a pair from the same transaction."
    elif header_norm == "subsidiary dr":
        role = "This cell shows the subsidiary ledger account that must be debited."
        evidence = f"The named subsidiary ledger account affected on the debit side is {sub_dr0}." if sub_dr0 else "No specific subsidiary ledger debit account is named for this row."
        rule = "Use a subsidiary ledger name only when the question format asks for the debtor or creditor account affected."
        method = f"Identify the person or business whose personal account must be debited. Here it is {sub_dr0}." if sub_dr0 else "If no debtor or creditor account is affected on the debit side, leave this cell blank."
        transfer_tip = "In similar questions, write a subsidiary ledger name only when a specific debtor or creditor account is involved."
    elif header_norm == "subsidiary cr":
        role = "This cell shows the subsidiary ledger account that must be credited."
        evidence = f"The named subsidiary ledger account affected on the credit side is {sub_cr0}." if sub_cr0 else "No specific subsidiary ledger credit account is named for this row."
        rule = "Use a subsidiary ledger name only when the question format asks for the debtor or creditor account affected."
        method = f"Identify the person or business whose personal account must be credited. Here it is {sub_cr0}." if sub_cr0 else "If no debtor or creditor account is affected on the credit side, leave this cell blank."
        transfer_tip = "In similar questions, first decide whether the General Ledger control account alone is enough or whether the question also wants the personal account name."
    elif header_norm == "amount":
        role = "This cell records the Rand amount for this row of the analysis."
        evidence = f"The transaction narrative and row method point to the amount {value0 or 'for this entry'}." if tx0 else evidence
        rule = "Use the amount that belongs to this exact entry. If a discount, allowance, interest split, or mark-up applies, calculate the correct row amount before writing it."
        method = f"Work from the transaction information step by step until you reach the amount for this line. For this row the correct amount is {value0}. {row_hint0}".strip() if value0 else method
        transfer_tip = "In similar questions, separate multi-effect transactions into individual rows and calculate the amount for each row before filling the table."
    elif header_norm in {"a", "assets", "assets (effect)"}:
        role = "This cell shows how the transaction affects Assets in the accounting equation."
        evidence = f"Look at the accounts in transaction {tx0}: Assets are affected through {dr0 if float(t.get('a') or 0.0) > 0 else cr0 or dr0}." if tx0 else evidence
        rule = "Use + for an increase in Assets, - for a decrease in Assets, and 0 if Assets do not change."
        method = f"Translate the debit and credit accounts into their effect on Assets. {row_hint0}".strip()
        transfer_tip = "In similar questions, ask whether any asset account increases, decreases, or both change within the same transaction."
    elif header_norm in {"o", "equity", "owner's equity (effect)"}:
        role = "This cell shows how the transaction affects Owner's Equity in the accounting equation."
        evidence = f"Look at the income, expense, capital, or drawings effect in transaction {tx0}." if tx0 else evidence
        rule = "Income and capital increase Owner's Equity, while expenses and drawings decrease Owner's Equity. Use 0 when equity is unaffected."
        method = f"Identify whether the row contains income, expense, capital, or drawings, then convert that into +, -, or 0. {row_hint0}".strip()
        transfer_tip = "In similar questions, think of equity through profit and owner claims: income/capital push it up, expenses/drawings pull it down."
    elif header_norm in {"l", "liabilities", "liabilities (effect)"}:
        role = "This cell shows how the transaction affects Liabilities in the accounting equation."
        evidence = f"Look at whether a liability account such as Loan, Creditors Control, or overdraft changes in transaction {tx0}." if tx0 else evidence
        rule = "Use + for an increase in Liabilities, - for a decrease in Liabilities, and 0 if Liabilities do not change."
        method = f"Identify whether the liability on this row increases, decreases, or stays unchanged. {row_hint0}".strip()
        transfer_tip = "In similar questions, separate normal bank situations from overdraft situations because overdraft can make bank movements affect Liabilities instead of Assets."
    elif header_norm == "assets (reason)":
        role = "This cell names the account that explains why Assets change on this transaction."
        evidence = f"The account causing the asset-side effect on this row is {value0}." if value0 else "Assets do not change on this row, so no reason account is needed."
        rule = "Write the account name that causes the asset change, not just the sign."
        method = f"Identify which account is responsible for the asset increase or decrease. For this row it is {value0}." if value0 else "If Assets do not change, leave this reason cell blank."
        transfer_tip = "In similar questions, decide the sign first and then ask which account caused that sign in the equation."
    elif header_norm == "owner's equity (reason)":
        role = "This cell names the account that explains why Owner's Equity changes on this transaction."
        evidence = f"The account causing the equity-side effect on this row is {value0}." if value0 else "Owner's Equity does not change on this row, so no reason account is needed."
        rule = "Write the income, expense, capital, or drawings account that causes the equity effect."
        method = f"Identify which account explains the equity movement. For this row it is {value0}." if value0 else "If Owner's Equity does not change, leave this reason cell blank."
        transfer_tip = "In similar questions, connect equity changes to the type of account: income/capital versus expense/drawings."
    elif header_norm == "liabilities (reason)":
        role = "This cell names the account that explains why Liabilities change on this transaction."
        evidence = f"The account causing the liability-side effect on this row is {value0}." if value0 else "Liabilities do not change on this row, so no reason account is needed."
        rule = "Write the liability account that causes the liability movement."
        method = f"Identify which liability account increases or decreases on this row. For this row it is {value0}." if value0 else "If Liabilities do not change, leave this reason cell blank."
        transfer_tip = "In similar questions, identify the liability account first, then decide whether the transaction increases or decreases what is owed."
    else:
        role = f"This cell helps complete the {header0} part of the transaction analysis requirement."
        rule = "Match the cell to the exact information required by the heading."
        transfer_tip = "In similar questions, use the heading to decide what type of answer belongs in the cell before writing anything."

    out_hint = {
        "role_in_requirement": role,
        "evidence_from_question": evidence,
        "rule_or_principle": rule,
        "how_to_derive": method,
        "transfer_tip": transfer_tip,
    }
    return {k: str(v).strip() for k, v in out_hint.items() if str(v or "").strip()}


def build_transaction_analysis_cell_hint(
    *,
    header_label: str,
    value: Optional[str],
    t: Dict[str, Any],
    row_hint: str,
) -> str:
    header0 = str(header_label or "").strip()
    header_norm = header0.lower()
    value0 = "" if value is None else str(value)
    nr0 = str(t.get("nr") or "").strip()
    src0 = str(t.get("source") or "").strip()
    jr0 = str(t.get("journal") or "").strip()
    internal0 = str(t.get("internal") or "").strip()
    dr0 = str(t.get("dr") or "").strip()
    cr0 = str(t.get("cr") or "").strip()
    sub_dr0 = str(t.get("sub_dr") or "").strip()
    sub_cr0 = str(t.get("sub_cr") or "").strip()
    row_hint0 = str(row_hint or "").strip()
    if header_norm == "no.":
        return f"Use transaction number {value0 or nr0}."
    if header_norm == "source document":
        if src0:
            return f"Source document: {src0}. This is the document that supports the transaction."
        return "No separate source document is required for this row."
    if header_norm == "subsidiary journal":
        if jr0:
            return f"Use {jr0}. This transaction is recorded in the {jr0}."
        return "No subsidiary journal label applies on this row."
    if header_norm == "internal document":
        if internal0 or src0:
            return f"Internal document: {internal0 or src0}. Use the internal reference given for this transaction."
        return "No internal document label applies on this row."
    if header_norm in {"account debited", "gl dr"}:
        if dr0:
            return f"General ledger debit entry: {dr0} is debited on this row."
        return "No general ledger debit account is entered on this row."
    if header_norm in {"account credited", "gl cr"}:
        if cr0:
            return f"General ledger credit entry: {cr0} is credited on this row."
        return "No general ledger credit account is entered on this row."
    if header_norm == "subsidiary dr":
        if sub_dr0:
            return f"Subsidiary ledger debit entry: {sub_dr0} is debited."
        return "Leave this subsidiary debit cell blank because no subsidiary ledger debit is affected."
    if header_norm == "subsidiary cr":
        if sub_cr0:
            return f"Subsidiary ledger credit entry: {sub_cr0} is credited."
        return "Leave this subsidiary credit cell blank because no subsidiary ledger credit is affected."
    if header_norm == "amount":
        if value0.strip():
            return f"Enter the amount for this row: {value0}. {row_hint0}".strip()
        return f"Leave the amount cell blank for this row. {row_hint0}".strip()
    if header_norm in {"a", "assets", "assets (effect)"}:
        return _transaction_analysis_effect_hint("Assets", value0, t)
    if header_norm in {"o", "equity", "owner's equity (effect)"}:
        return _transaction_analysis_effect_hint("Owner's Equity", value0, t)
    if header_norm in {"l", "liabilities", "liabilities (effect)"}:
        return _transaction_analysis_effect_hint("Liabilities", value0, t)
    if header_norm == "assets (reason)":
        if value0.strip():
            return f"Assets are affected through {value0}. This account explains the asset-side change."
        return "Leave this reason cell blank because Assets do not change on this row."
    if header_norm == "owner's equity (reason)":
        if value0.strip():
            return f"Owner's Equity is affected through {value0}. This account explains the equity-side change."
        return "Leave this reason cell blank because Owner's Equity does not change on this row."
    if header_norm == "liabilities (reason)":
        if value0.strip():
            return f"Liabilities are affected through {value0}. This account explains the liability-side change."
        return "Leave this reason cell blank because Liabilities do not change on this row."
    if value0.strip():
        return f"Enter {header0}: {value0}. {row_hint0}".strip()
    return row_hint0 or f"Leave {header0} blank on this row."


def build_transaction_analysis_row_hint(
    *,
    t: Dict[str, Any],
    current_tx: str,
    schema: str,
    markup_pct: float,
) -> str:
    nr0 = str(t.get("nr") or "")
    dr0 = str(t.get("dr") or "")
    cr0 = str(t.get("cr") or "")
    jr0 = str(t.get("journal") or "")
    sub_dr0 = str(t.get("sub_dr") or "")
    sub_cr0 = str(t.get("sub_cr") or "")
    tag0 = str(t.get("tag") or "")
    row_amount0 = float(t.get("amount") or 0.0)
    if nr0.strip():
        if tag0 == "insolvency_dividend":
            owed0 = float(t.get("owed") or 0.0)
            cents0 = float(t.get("cents_in_rand") or 0.0)
            return f"Insolvent debtor: Dividend = Amount owed × (cents in the rand ÷ 100) = {int(owed0)} × {cents0}/100. The balance is written off as bad debts (second row)."
        if tag0 == "cash_sales_main":
            cost0 = float(t.get("cost_price") or 0.0)
            sales0 = float(t.get("sales_amount") or row_amount0)
            markup0 = float(t.get("markup_pct") or markup_pct)
            return f"Cash sale: Sales = Cost × (1 + mark-up) = {cost0:g} × (1 + {markup0:g}/100) = {sales0:g}. Bank increases and Sales increases Owner's Equity."
        if tag0 == "credit_sales_main":
            cost0 = float(t.get("cost_price") or 0.0)
            sales0 = float(t.get("sales_amount") or row_amount0)
            markup0 = float(t.get("markup_pct") or markup_pct)
            return f"Credit sale: Sales = Cost × (1 + mark-up) = {cost0:g} × (1 + {markup0:g}/100) = {sales0:g}. Debtors Control increases and Sales increases Owner's Equity."
        if tag0 == "debtor_settlement_main":
            owed0 = float(t.get("owed") or 0.0)
            disc_pct0 = float(t.get("disc_pct") or 0.0)
            disc0 = float(t.get("discount_amount") or 0.0)
            bank0 = float(t.get("bank_amount") or 0.0)
            return f"Debtor settlement: Discount = {owed0:g} × {disc_pct0:g}/100 = {disc0:g}. Amount received = {owed0:g} - {disc0:g} = {bank0:g}. Bank increases while Debtors Control decreases, so Assets show +/-."
        if tag0 == "creditor_payment_main":
            owed0 = float(t.get("owed") or 0.0)
            disc_pct0 = float(t.get("disc_pct") or 0.0)
            disc0 = float(t.get("discount_amount") or 0.0)
            bank0 = float(t.get("bank_amount") or 0.0)
            return f"Creditor settlement: Discount received = {owed0:g} × {disc_pct0:g}/100 = {disc0:g}. Cash paid = {owed0:g} - {disc0:g} = {bank0:g}. Bank decreases and Creditors Control decreases."
        if tag0 == "interest_overdue_debtor":
            principal0 = float(t.get("principal") or 0.0)
            rate0 = float(t.get("rate_pct") or 0.0)
            months0 = int(t.get("months") or 0)
            interest0 = float(t.get("interest_amount") or row_amount0)
            return f"Interest on overdue debtor: Interest = Principal × Rate × Time = {principal0:g} × {rate0:g}/100 × {months0}/12 = {interest0:g}. Debtors Control increases and Interest income increases Owner's Equity."
        if tag0 == "interest_overdue_creditor":
            principal0 = float(t.get("principal") or 0.0)
            rate0 = float(t.get("rate_pct") or 0.0)
            months0 = int(t.get("months") or 0)
            interest0 = float(t.get("interest_amount") or row_amount0)
            return f"Interest on overdue creditor: Interest = Principal × Rate × Time = {principal0:g} × {rate0:g}/100 × {months0}/12 = {interest0:g}. Interest expense decreases Owner's Equity and Creditors Control increases."
        if tag0 == "loan_repayment_capital":
            repayment0 = float(t.get("repayment_total") or 0.0)
            rate0 = float(t.get("rate_pct") or 0.0)
            months0 = int(t.get("months") or 0)
            interest0 = float(t.get("interest_amount") or 0.0)
            capital0 = float(t.get("capital_amount") or row_amount0)
            return f"Loan repayment: Total payment = capital + interest. Interest = {repayment0:g} - {capital0:g} = {interest0:g}, based on {rate0:g}% for {months0} month(s). This first row reduces Bank and reduces the Loan balance."
        if tag0 == "rd_cheque_reversal":
            return "Returned cheque: the money previously received from the debtor is reversed. Debtors Control increases while Bank decreases, so Assets show +/-."
        if tag0 == "creditor_allowance_return":
            cost0 = float(t.get("cost_price") or 0.0)
            td_pct0 = float(t.get("td_pct") or 0.0)
            net0 = float(t.get("net_amount") or row_amount0)
            return f"Allowance from creditor: Net allowance = {cost0:g} × (1 - {td_pct0:g}/100) = {net0:g}. Trading stock decreases and Creditors Control decreases."
        if tag0 == "stationery_error_correction":
            return "Error correction: the amount was wrongly treated as Trading stock. Move it to Stationery expense, so Assets decrease and Owner's Equity decreases."
        if tag0 == "equipment_return_damaged":
            return "Returned damaged equipment to the creditor: Equipment decreases and Creditors Control decreases."
        if tag0 == "equipment_cash_asset_swap":
            return "Equipment bought for cash: Equipment increases while Bank decreases, so Assets show +/-. There is no net change in total assets."
        if tag0 == "petty_cash_transfer_asset_swap":
            return "Petty cash transfer: Petty Cash increases while Bank decreases, so Assets show +/-. There is no net change in total assets."
        if tag0 == "loan_received":
            return "Loan received: Bank increases because cash enters the business and Liabilities increase because the loan must be repaid."
        if tag0 == "interest_income_receipt":
            return "Interest received increases Bank and increases Owner's Equity because it is income earned by the business."
        if tag0 == "rent_received_income":
            return "Rent received increases Bank and increases Owner's Equity because rent income is earned by the business."
        if tag0 == "bank_charges_favourable":
            return "Bank charges are an expense. They decrease Bank (asset) and decrease Owner's Equity."
        if tag0 == "fee_income_credit":
            return "Fee income on credit: the debtor owes the business, so Debtors Control (asset) increases; Fee/Service income increases Owner's Equity."
        if tag0 == "bank_unfavourable_receipt":
            owed0 = float(t.get("owed") or 0.0)
            disc_pct0 = float(t.get("disc_pct") or 0.0)
            disc0 = float(t.get("discount_amount") or 0.0)
            bank0 = float(t.get("bank_amount") or 0.0)
            return f"Bank is unfavourable (overdraft): the receipt of {bank0:g} reduces the overdraft (Liabilities decrease). Discount = {owed0:g} × {disc_pct0:g}/100 = {disc0:g}."
        if tag0 == "bank_unfavourable_interest":
            return "Bank is unfavourable (overdraft): interest on overdraft increases Liabilities (overdraft) and decreases Owner's Equity (expense)."
        if tag0 == "fixed_deposit_investment":
            return "Fixed deposit investment: Asset swap from Bank to Fixed deposit. No net effect on A/O/L (0/0/0)."
        if tag0 == "petty_cash_imprest":
            return "Petty cash imprest restoration: Asset swap from Bank to Petty cash. No net effect on A/O/L (0/0/0)."
        if tag0 == "owner_taking_stock":
            return "Owner taking stock: Drawings increases, Trading stock decreases. Decreases Assets and Owner's Equity."
        if tag0 == "interest_current_account":
            return "Interest on current account: Bank increases, Interest income increases. Increases Assets and Owner's Equity."
        if tag0 == "vehicle_purchase_credit":
            return "Vehicle purchase on credit: Vehicles (asset) increases, Creditors control (liability) increases."
        if tag0 == "cash_handling_fee":
            return "Cash handling fee: Bank charges expense reduces Owner's Equity and Bank (asset)."
        if tag0 == "cash_withdrawal_bank_to_cash":
            return "Cash withdrawal for wages: Asset swap from Bank to Cash. No net effect on A/O/L (0/0/0)."
        if tag0 == "packing_materials_unfavourable":
            return "Packing materials (unfavourable): Expense reduces Owner's Equity; Bank is already overdrawn so Liabilities increase."
        if tag0 == "postage_paid":
            return "Postage paid: Postage expense reduces Owner's Equity and Petty cash (asset)."
        if jr0.strip() and schema == "journal_gl_amount_aol":
            return "Use the Subsidiary Journal (e.g. CRJ/CPJ/CJ/DJ) as the source for this transaction."
        if schema == "gl_subledger_amount_aol" and (sub_dr0.strip() or sub_cr0.strip()):
            return "Section 11 format: fill in the General Ledger accounts AND the Subsidiary Ledger account name (where applicable), then show the effect on A/O/L."
        return ""
    if tag0 == "insolvency_writeoff":
        return f"Second entry for transaction {current_tx}: write off the unrecovered balance as bad debts."
    if tag0 == "bank_unfavourable_discount":
        return f"Second entry for transaction {current_tx}: record Discount allowed (reduces Owner's Equity)."
    if tag0 == "cash_sales_cost":
        return f"Second entry for transaction {current_tx}: record Cost of sales. Trading stock decreases and Cost of sales reduces Owner's Equity."
    if tag0 == "credit_sales_cost":
        return f"Second entry for transaction {current_tx}: record Cost of sales. Trading stock decreases and Cost of sales reduces Owner's Equity."
    if tag0 == "discount_allowed_settlement":
        owed0 = float(t.get("owed") or 0.0)
        disc_pct0 = float(t.get("disc_pct") or 0.0)
        disc0 = float(t.get("discount_amount") or 0.0)
        return f"Second entry for transaction {current_tx}: Discount allowed = {owed0:g} × {disc_pct0:g}/100 = {disc0:g}. Discount allowed is an expense, so Owner's Equity decreases."
    if tag0 == "creditor_discount_received":
        owed0 = float(t.get("owed") or 0.0)
        disc_pct0 = float(t.get("disc_pct") or 0.0)
        disc0 = float(t.get("discount_amount") or 0.0)
        return f"Second entry for transaction {current_tx}: Discount received = {owed0:g} × {disc_pct0:g}/100 = {disc0:g}. Discount received increases Owner's Equity and further reduces Creditors Control."
    if tag0 == "rd_cheque_discount_reversal":
        return f"Second entry for transaction {current_tx}: reverse the discount previously allowed because the cheque was returned unpaid."
    if tag0 == "loan_repayment_interest":
        repayment0 = float(t.get("repayment_total") or 0.0)
        capital0 = float(t.get("capital_amount") or 0.0)
        interest0 = float(t.get("interest_amount") or amount)
        return f"Second entry for transaction {current_tx}: interest on loan = {repayment0:g} - {capital0:g} = {interest0:g}. Interest on loan is an expense, so Owner's Equity decreases."
    if tag0 == "bank_fee_service":
        return f"Bank fee breakdown for transaction {current_tx}: Service fee reduces Owner's Equity (expense) and increases Liabilities (overdraft)."
    if tag0 == "bank_fee_cash":
        return f"Second entry for transaction {current_tx}: Cash handling fee reduces Owner's Equity (expense)."
    if tag0 == "bank_fee_overdraft_int":
        return f"Third entry for transaction {current_tx}: Overdraft interest reduces Owner's Equity (expense)."
    if dr0.lower() == "interest on loan":
        return f"Second entry for transaction {current_tx}: record the interest portion of the repayment."
    if dr0.lower() == "cost of sales" and cr0.lower() == "trading stock":
        return f"Second entry for transaction {current_tx}: record Cost of sales."
    if dr0.lower() == "discount allowed" and cr0.lower() == "debtors control":
        return f"Second entry for transaction {current_tx}: record Discount allowed."
    if dr0.lower() == "creditors control" and cr0.lower() == "discount received":
        return f"Second entry for transaction {current_tx}: record Discount received."
    if dr0.lower() == "debtors control" and cr0.lower() == "discount allowed":
        return f"Second entry for transaction {current_tx}: reverse the discount allowed (R/D cheque)."
    if dr0.lower() == "trading stock" and cr0.lower() == "cost of sales":
        return f"Second entry for transaction {current_tx}: return stock to inventory (reverse Cost of sales)."
    return f"Second entry for transaction {current_tx}."
