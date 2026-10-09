"""Grade 10 Accounting deterministic 6-pillar generators."""
from app.utils.grade10_accounting.fixed_assets_depreciation_generator import (
    generate as generate_fixed_assets,
)
from app.utils.grade10_accounting.inventory_cost_of_sales_generator import (
    generate as generate_inventory,
)
from app.utils.grade10_accounting.gaap_generator import (
    generate_grade10_gaap_questions as generate_gaap,
)
from app.utils.grade10_accounting.ethics_generator import (
    generate_questions as generate_ethics,
)
from app.utils.grade10_accounting.internal_control_generator import (
    generate_questions as generate_internal_control,
)
from app.utils.grade10_accounting.sole_trader_generator import (
    generate_questions as generate_sole_trader,
)

__all__ = [
    "generate_fixed_assets",
    "generate_inventory",
    "generate_gaap",
    "generate_ethics",
    "generate_internal_control",
    "generate_sole_trader",
]
