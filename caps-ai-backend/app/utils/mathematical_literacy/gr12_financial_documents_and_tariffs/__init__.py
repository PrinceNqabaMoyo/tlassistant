"""Grade 12 Mathematical Literacy: FINANCIAL DOCUMENTS AND TARIFF SYSTEMS.
Covers 52 distinct subskill archetypes strictly aligned with CAPS Grade 12 Paper 1 Finance:
Water & Sanitation Tariffs, Electricity & Incline Block Tariffs, Telecommunications & Data Tariffs,
Public Transport & Logistics Economics, Banking Fee Structures, Small Business Costing & Break-Even,
and Budgets / Financial Statements.
"""
from __future__ import annotations

import random
from typing import Any, Callable, Dict, List

from .water_sanitation_tariffs import (
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
)
from .electricity_tariffs import (
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
)
from .telecoms_tariffs import (
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
)
from .transport_tariffs import (
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
)
from .banking_fees import (
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
)
from .small_business_costing_breakeven import (
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
)
from .budgets_financial_statements import (
    gen_subskill_47,
    gen_subskill_48,
    gen_subskill_49,
    gen_subskill_50,
    gen_subskill_51,
    gen_subskill_52,
)

_RAW_FUNCS = [
    gen_subskill_01,
    gen_subskill_02,
    gen_subskill_03,
    gen_subskill_04,
    gen_subskill_05,
    gen_subskill_06,
    gen_subskill_07,
    gen_subskill_08,
    gen_subskill_09,
    gen_subskill_10,
    gen_subskill_11,
    gen_subskill_12,
    gen_subskill_13,
    gen_subskill_14,
    gen_subskill_15,
    gen_subskill_16,
    gen_subskill_17,
    gen_subskill_18,
    gen_subskill_19,
    gen_subskill_20,
    gen_subskill_21,
    gen_subskill_22,
    gen_subskill_23,
    gen_subskill_24,
    gen_subskill_25,
    gen_subskill_26,
    gen_subskill_27,
    gen_subskill_28,
    gen_subskill_29,
    gen_subskill_30,
    gen_subskill_31,
    gen_subskill_32,
    gen_subskill_33,
    gen_subskill_34,
    gen_subskill_35,
    gen_subskill_36,
    gen_subskill_37,
    gen_subskill_38,
    gen_subskill_39,
    gen_subskill_40,
    gen_subskill_41,
    gen_subskill_42,
    gen_subskill_43,
    gen_subskill_44,
    gen_subskill_45,
    gen_subskill_46,
    gen_subskill_47,
    gen_subskill_48,
    gen_subskill_49,
    gen_subskill_50,
    gen_subskill_51,
    gen_subskill_52,
]

SUBSKILLS: List[str] = [f"tariff_gr12_{i:02d}" for i in range(1, 53)]

BUILDERS: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {}
DISPATCH_TABLE: Dict[Any, Callable[[random.Random], Dict[str, Any]]] = {}

for idx, fn in enumerate(_RAW_FUNCS, start=1):
    key = f"tariff_gr12_{idx:02d}"
    alt_key = f"gr12_tariffs_subskill_{idx:02d}"
    alt_key_single = f"gr12_tariffs_subskill_{idx}"
    BUILDERS[key] = fn
    DISPATCH_TABLE[key] = fn
    DISPATCH_TABLE[alt_key] = fn
    DISPATCH_TABLE[alt_key_single] = fn
    DISPATCH_TABLE[idx] = fn
    DISPATCH_TABLE[str(idx)] = fn

SUBSKILLS_METADATA: List[Dict[str, Any]] = [
    {"id": 1, "key": "tariff_gr12_01", "name": "Interpreting Municipal Residential Water Sliding Scale Blocks", "category": "Water & Sanitation"},
    {"id": 2, "key": "tariff_gr12_02", "name": "Calculating Monthly Water Cost within Block 2 with VAT", "category": "Water & Sanitation"},
    {"id": 3, "key": "tariff_gr12_03", "name": "Multi-Tier Water Charges across Three Stepped Blocks", "category": "Water & Sanitation"},
    {"id": 4, "key": "tariff_gr12_04", "name": "Sanitation and Sewerage Percentage Surcharge Calculation", "category": "Water & Sanitation"},
    {"id": 5, "key": "tariff_gr12_05", "name": "Water Leak Detection via Meter Readings and Financial Penalty", "category": "Water & Sanitation"},
    {"id": 6, "key": "tariff_gr12_06", "name": "Comparative Water Tariffs between Two South African Metros", "category": "Water & Sanitation"},
    {"id": 7, "key": "tariff_gr12_07", "name": "Reverse Tariff Problem: Finding Volume Consumed from Final Bill", "category": "Water & Sanitation"},
    {"id": 8, "key": "tariff_gr12_08", "name": "Drought Restriction Penalty Tariff on High-Volume Consumption", "category": "Water & Sanitation"},
    {"id": 9, "key": "tariff_gr12_09", "name": "Interpreting Domestic Incline Block Tariff (IBT) Structure", "category": "Electricity Tariffs"},
    {"id": 10, "key": "tariff_gr12_10", "name": "Calculating Monthly Prepaid Electricity Cost across Two Blocks", "category": "Electricity Tariffs"},
    {"id": 11, "key": "tariff_gr12_11", "name": "Conventional Post-Paid Electricity Bill with Fixed Network Fee", "category": "Electricity Tariffs"},
    {"id": 12, "key": "tariff_gr12_12", "name": "Cost Comparison: Prepaid Meter vs Conventional Meter with Fixed Fee", "category": "Electricity Tariffs"},
    {"id": 13, "key": "tariff_gr12_13", "name": "Time-of-Use (TOU) Commercial Electricity Tariff Billing", "category": "Electricity Tariffs"},
    {"id": 14, "key": "tariff_gr12_14", "name": "Reverse Calculation: Determining kWh from a Prepaid Receipt", "category": "Electricity Tariffs"},
    {"id": 15, "key": "tariff_gr12_15", "name": "Domestic Appliance Running Cost (kW x Hours x Tariff)", "category": "Electricity Tariffs"},
    {"id": 16, "key": "tariff_gr12_16", "name": "Percentage Increase in Electricity Bill following NERSA Hike", "category": "Electricity Tariffs"},
    {"id": 17, "key": "tariff_gr12_17", "name": "Prepaid Voice Calls: Per-Second Billing vs Per-Minute Rounding", "category": "Telecommunications"},
    {"id": 18, "key": "tariff_gr12_18", "name": "Contract Monthly Fee with Inclusive Minutes and Out-of-Bundle Rates", "category": "Telecommunications"},
    {"id": 19, "key": "tariff_gr12_19", "name": "Mobile Data Bundles: 30-Day Recurring vs Out-of-Bundle Penalty", "category": "Telecommunications"},
    {"id": 20, "key": "tariff_gr12_20", "name": "Comparative Cellular Contracts for a Specified Usage Profile", "category": "Telecommunications"},
    {"id": 21, "key": "tariff_gr12_21", "name": "Finding Break-Even Call Minutes between Two Contract Options", "category": "Telecommunications"},
    {"id": 22, "key": "tariff_gr12_22", "name": "Home Fibre Broadband: Uncapped Flat Rate vs Capped with Top-Ups", "category": "Telecommunications"},
    {"id": 23, "key": "tariff_gr12_23", "name": "Total Cost of 24-Month Smartphone Contract with Device Insurance", "category": "Telecommunications"},
    {"id": 24, "key": "tariff_gr12_24", "name": "International Roaming Data and Voice Call Charges Calculation", "category": "Telecommunications"},
    {"id": 25, "key": "tariff_gr12_25", "name": "Minibus Taxi vs Municipal Bus Monthly Commuter Fare Comparison", "category": "Transport Tariffs"},
    {"id": 26, "key": "tariff_gr12_26", "name": "Bus Ticket Pricing: Single Tickets vs 10-Trip Weekly Clipcard", "category": "Transport Tariffs"},
    {"id": 27, "key": "tariff_gr12_27", "name": "Break-Even Commuter Trips to Justify Unlimited Monthly Pass", "category": "Transport Tariffs"},
    {"id": 28, "key": "tariff_gr12_28", "name": "E-Hailing Metered Taxi Fare Calculation with Surge Multiplier", "category": "Transport Tariffs"},
    {"id": 29, "key": "tariff_gr12_29", "name": "Vehicle Operating Cost per Kilometre (Fuel, Maintenance, Toll)", "category": "Transport Tariffs"},
    {"id": 30, "key": "tariff_gr12_30", "name": "Volumetric Dimensional Courier Weight vs Actual Mass Tariff", "category": "Transport Tariffs"},
    {"id": 31, "key": "tariff_gr12_31", "name": "Highway Toll Plaza Return Route Cumulative Fee Calculation", "category": "Transport Tariffs"},
    {"id": 32, "key": "tariff_gr12_32", "name": "Delivery Logistics: Fixed Vehicle Lease vs Third-Party Contractor", "category": "Transport Tariffs"},
    {"id": 33, "key": "tariff_gr12_33", "name": "Itemised Pay-As-You-Transact (PAYT) Bank Statement Fee Audit", "category": "Banking Fees"},
    {"id": 34, "key": "tariff_gr12_34", "name": "ATM Cash Withdrawal Fee Formula: Base Fee + Rate per R100", "category": "Banking Fees"},
    {"id": 35, "key": "tariff_gr12_35", "name": "Own-Bank ATM vs Saswitch Interbank Network Withdrawal Fees", "category": "Banking Fees"},
    {"id": 36, "key": "tariff_gr12_36", "name": "Fixed Bundled Account Fee vs PAYT Monthly Cost Comparison", "category": "Banking Fees"},
    {"id": 37, "key": "tariff_gr12_37", "name": "Penalty Fees: Dishonoured Debit Order Charge and Failed Payment", "category": "Banking Fees"},
    {"id": 38, "key": "tariff_gr12_38", "name": "Point-of-Sale Card Swipe Efficiency vs Cash Withdrawal", "category": "Banking Fees"},
    {"id": 39, "key": "tariff_gr12_39", "name": "Credit Card Minimum Monthly Payment Due Calculation", "category": "Banking Fees"},
    {"id": 40, "key": "tariff_gr12_40", "name": "Annual Banking Fee Audit across Different Cheque Accounts", "category": "Banking Fees"},
    {"id": 41, "key": "tariff_gr12_41", "name": "Classifying Small Business Cost Categories (Start-up, Fixed, Variable)", "category": "Small Business Costing"},
    {"id": 42, "key": "tariff_gr12_42", "name": "Unit Cost of Production from Batch Ingredients and Packaging", "category": "Small Business Costing"},
    {"id": 43, "key": "tariff_gr12_43", "name": "Determining Selling Price from Unit Cost and Target Markup %", "category": "Small Business Costing"},
    {"id": 44, "key": "tariff_gr12_44", "name": "Break-Even Quantity Determination Using Contribution Margin", "category": "Small Business Costing"},
    {"id": 45, "key": "tariff_gr12_45", "name": "Net Profit Calculation at a Specified Monthly Sales Volume", "category": "Small Business Costing"},
    {"id": 46, "key": "tariff_gr12_46", "name": "Required Sales Volume to Achieve a Specific Target Net Profit", "category": "Small Business Costing"},
    {"id": 47, "key": "tariff_gr12_47", "name": "Monthly Income-and-Expenditure Statement: Net Surplus / Deficit", "category": "Budgets & Statements"},
    {"id": 48, "key": "tariff_gr12_48", "name": "Budget Variance Analysis: Favourable vs Unfavourable Classification", "category": "Budgets & Statements"},
    {"id": 49, "key": "tariff_gr12_49", "name": "Percentage Variance Relative to Budgeted Expenditure", "category": "Budgets & Statements"},
    {"id": 50, "key": "tariff_gr12_50", "name": "National Budget Speech: Percentage Allocation to Priority Sector", "category": "Budgets & Statements"},
    {"id": 51, "key": "tariff_gr12_51", "name": "National Budget Deficit Shortfall and Borrowing Requirements", "category": "Budgets & Statements"},
    {"id": 52, "key": "tariff_gr12_52", "name": "Two-Month Cash Flow Budget Projection and Net Closing Balance", "category": "Budgets & Statements"},
]
