from flask import Blueprint
 
accounting_bp = Blueprint('accounting', __name__)
 
from . import grade10_indigenous_bookkeeping_routes
from . import grade10_ethics_routes
from . import grade10_gaap_routes
from . import grade10_internal_control_routes
from . import grade10_sole_trader_routes
from . import grade10_routes
from . import grade11_concepts_routes
from . import grade11_fixed_assets_routes
from . import grade11_partnership_ledger_routes
from . import grade11_partnership_balance_sheet_routes
from . import grade11_reconciliation_routes
from . import grade11_income_statement_routes
from . import grade11_routes

from . import grade12_concepts_routes
from . import grade12_audits_governance_shareholding_routes
from . import grade12_company_general_ledger_routes
from . import grade12_financial_statements_routes
from . import grade12_cash_flow_routes
from . import grade12_analysis_interpretation_routes
from . import grade12_routes
