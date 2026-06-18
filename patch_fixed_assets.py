import sys

filepath = r'C:\Users\princ\fundile-tlassistant-vite\caps-ai-backend\app\utils\grade11_accounting\fixed_assets_generator.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()


# Fix 1: _make_fixed_assets_note_question
old_prompt_1 = """    prompt = f\"\"\"{business}

#### REQUIRED:
Complete the Fixed/Tangible Assets Note to the Financial Statements on {year_end}.

#### INFORMATION:
Use the balances and additional information provided to calculate depreciation, additions and disposals.\"\"\""""

new_prompt_1 = """    info_lines = [
        "Balances at the beginning of the year:",
        f"- Vehicles (Cost): R{vehicles_cost:,.2f}",
        f"- Vehicles (Accumulated depreciation): R{vehicles_acc:,.2f}",
        f"- Equipment (Cost): R{equip_cost:,.2f}",
        f"- Equipment (Accumulated depreciation): R{equip_acc:,.2f}",
        "",
        "Transactions and adjustments during the year:",
        f"- New equipment was purchased for R{equip_add:,.2f}.",
        f"- Vehicles with a carrying value of R{vehicles_disp_cv:,.2f} were disposed of.",
        f"- Total depreciation calculated for the year: Vehicles R{dep_veh:,.2f}, Equipment R{dep_equip:,.2f}."
    ]

    prompt = f\"\"\"{business}

#### REQUIRED:
Complete the Fixed/Tangible Assets Note to the Financial Statements on {year_end}.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_1, new_prompt_1)


# Fix 2: _make_asset_disposal_account_question
old_prompt_2 = """    prompt = f\"\"\"{business}

#### REQUIRED:
Prepare the Asset Disposal account in the General Ledger.

#### INFORMATION:
Use cost price, accumulated depreciation and proceeds to determine profit/loss.\"\"\""""

new_prompt_2 = """    info_lines = [
        f"- Original cost price of the asset sold: R{cost:,.2f}",
        f"- Accumulated depreciation on the asset to date of sale: R{acc:,.2f}",
        f"- Cash proceeds received from the sale: R{proceeds:,.2f}"
    ]

    prompt = f\"\"\"{business}

#### REQUIRED:
Prepare the Asset Disposal account in the General Ledger.

#### INFORMATION:
{chr(10).join(info_lines)}\"\"\""""

content = content.replace(old_prompt_2, new_prompt_2)


with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Patched fixed_assets_generator.py")
