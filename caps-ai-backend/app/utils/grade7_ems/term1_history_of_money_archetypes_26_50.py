"""
Grade 7 EMS — Term 1: History of Money — Semantic Archetypes 26–50.
Grounded strictly in curriculum_docs_auto/EMS_Gr7/Term 1/01. History of money.md.
"""
from __future__ import annotations

import datetime
import random
from typing import Any, Callable, Dict, List

from ..ems_namelist import TUCKSHOP_ITEMS
from .term1_history_of_money_archetypes_01_25 import (
    _escape,
    _fmt_rand,
    _mcq,
    _pick_person,
    _pick_place,
    _pick_two_people,
    _q,
    _svg_timeline,
    _svg_two_way_flow,
    _svg_wrap,
    _table_q,
)


def _svg_promissory_note(
    place: str,
    issue_date: str,
    principal: int,
    maker: str,
    payee: str,
    due_date: str,
    rate_pct: int,
) -> Dict[str, Any]:
    amt_str = _fmt_rand(principal)
    body = (
        f'<rect x="28" y="44" width="584" height="178" rx="8" fill="#fffef2" stroke="#1e293b" stroke-width="2"/>'
        f'<text x="46" y="70" font-family="Arial, sans-serif" font-size="12" fill="#334155">Place: {_escape(place)}</text>'
        f'<text x="420" y="70" font-family="Arial, sans-serif" font-size="12" fill="#334155">Date: {_escape(issue_date)}</text>'
        f'<rect x="420" y="84" width="170" height="32" rx="5" fill="#eff6ff" stroke="#2563eb"/>'
        f'<text x="505" y="105" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" font-weight="bold" fill="#1e3a8a">{_escape(amt_str)}</text>'
        f'<text x="46" y="106" font-family="Arial, sans-serif" font-size="13" fill="#0f172a">I, {_escape(maker)} (Issuer), promise to pay</text>'
        f'<text x="46" y="134" font-family="Arial, sans-serif" font-size="13" fill="#0f172a">to {_escape(payee)} (Payee) the sum of {_escape(amt_str)}</text>'
        f'<text x="46" y="162" font-family="Arial, sans-serif" font-size="12.5" fill="#0f172a">on {_escape(due_date)} with interest at {rate_pct}% per annum.</text>'
        f'<line x1="410" y1="196" x2="585" y2="196" stroke="#64748b" stroke-width="1.5"/>'
        f'<text x="498" y="212" text-anchor="middle" font-family="Arial, sans-serif" font-size="11" fill="#475569">Signed: {_escape(maker)}</text>'
    )
    return _svg_wrap(640, 238, "Promissory Note", body)


def _svg_price_board(shop: str, items: List[tuple[str, int]]) -> Dict[str, Any]:
    rows_svg: List[str] = ['<rect x="44" y="46" width="552" height="148" rx="8" fill="#f0fdf4" stroke="#15803d" stroke-width="2"/>']
    for idx, (label, price) in enumerate(items):
        y = 76 + idx * 32
        rows_svg.append(
            f'<text x="72" y="{y}" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#0f172a">{_escape(label)}</text>'
        )
        rows_svg.append(
            f'<text x="560" y="{y}" text-anchor="end" font-family="Arial, sans-serif" font-size="13" font-weight="bold" fill="#166534">{_escape(_fmt_rand(price))}</text>'
        )
        if idx < len(items) - 1:
            rows_svg.append(f'<line x1="68" y1="{y + 10}" x2="572" y2="{y + 10}" stroke="#bbf7d0" stroke-width="1"/>')
    return _svg_wrap(640, 210, f"{shop} — Unit of Account Price Board", "".join(rows_svg))


def _svg_five_stages(amount: int) -> Dict[str, Any]:
    stages = [
        ("1. Barter", "Direct swap"),
        ("2. Commodity", "Shells / cattle"),
        ("3. Coins", "Stamped metal"),
        ("4. Paper", "Banknotes & IOUs"),
        ("5. EFT", f"{_fmt_rand(amount)} instant"),
    ]
    parts: List[str] = []
    for idx, (head, sub) in enumerate(stages):
        x = 24 + idx * 120
        parts.append(f'<rect x="{x}" y="58" width="108" height="74" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>')
        parts.append(f'<text x="{x + 54}" y="86" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" font-weight="bold" fill="#1e3a8a">{_escape(head)}</text>')
        parts.append(f'<text x="{x + 54}" y="110" text-anchor="middle" font-family="Arial, sans-serif" font-size="10.5" fill="#334155">{_escape(sub)}</text>')
        if idx < len(stages) - 1:
            parts.append(f'<line x1="{x + 108}" y1="95" x2="{x + 120}" y2="95" stroke="#0f766e" stroke-width="2"/>')
    return _svg_wrap(640, 154, "Five Stages of the Evolution of Money", "".join(parts))


# ---------------------------------------------------------------------------
# Archetypes 26 – 50
# ---------------------------------------------------------------------------

def _b26(rng: random.Random) -> Dict[str, Any]:
    maker, payee = _pick_two_people(rng)
    city = _pick_place(rng, rural=False)
    principal = rng.choice([1200, 1800, 2400, 3500])
    rate = rng.choice([8, 10, 12])
    issue_date = rng.choice(["14 March 2025", "02 May 2025", "18 August 2025"])
    due_date = rng.choice(["14 September 2025", "02 November 2025", "18 February 2026"])
    diag = _svg_promissory_note(city, issue_date, principal, maker, payee, due_date, rate)
    prompt = (
        f"Refer to the promissory note diagram issued in {city} for {_fmt_rand(principal)}. "
        f"Identify (a) the issuer (maker), (b) the payee, and (c) explain which party is legally obliged to pay on {due_date}."
    )
    sample = (
        f"(a) Issuer (maker): {maker}; (b) Payee: {payee}; (c) {maker} must pay {_fmt_rand(principal)} plus {rate}% "
        f"interest to {payee} on {due_date} because {maker} signed the unconditional written promise."
    )
    worked = (
        f"1. **Issuer / Maker [1]:** **{maker}** (the borrower who signs the note).\n"
        f"2. **Payee [1]:** **{payee}** (the party entitled to receive payment).\n"
        f"3. **Legal obligation [1]:** **{maker}** is legally obliged to repay {_fmt_rand(principal)} plus {rate}% annual interest on {due_date}."
    )
    return _q(
        rng,
        "26_promissory_note_elements_diagram",
        prompt,
        sample,
        worked,
        "Every valid promissory note states the maker, payee, principal amount, issue/due dates, interest rate, and signature.",
        {
            "tier_1": "Look closely at who signs 'I, ..., promise to pay' versus who is named to receive payment.",
            "tier_2": "Distinguish the borrower (maker/issuer) from the lender/supplier (payee).",
            "tier_3": f"Name {maker} as issuer, {payee} as payee, and explain {maker}'s repayment duty.",
        },
        ["swaps_maker_and_payee_roles"],
        [
            {"criterion": f"Identifies issuer/maker: {maker}", "marks": 1},
            {"criterion": f"Identifies payee: {payee}", "marks": 1},
            {"criterion": f"Explains {maker}'s legal obligation to pay on {due_date}", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b27(rng: random.Random) -> Dict[str, Any]:
    maker, payee = _pick_two_people(rng)
    amt = rng.choice([900, 1500, 2200])
    city = _pick_place(rng, rural=False)
    pool = [
        {"cells": [f"'{maker}' (the debtor signing the promise)", None], "expected": ["Issuer / Maker"], "cell_hints": ["Party making the written promise to pay."]},
        {"cells": [f"'{payee}' (the supplier receiving payment)", None], "expected": ["Payee"], "cell_hints": ["Party to whom the money must be paid."]},
        {"cells": [f"'{_fmt_rand(amt)}' (exact sum borrowed)", None], "expected": ["Principal amount"], "cell_hints": ["Original Rand face amount before interest."]},
        {"cells": ["'10% per year' (cost of borrowing)", None], "expected": ["Interest rate"], "cell_hints": ["Percentage fee charged for credit over time."]},
        {"cells": [f"'{city}, 10 April' (where and when signed)", None], "expected": ["Place and date issued"], "cell_hints": ["Establishes legal start date and jurisdiction."]},
        {"cells": ["'30 October' (final settlement deadline)", None], "expected": ["Maturity / Due date"], "cell_hints": ["Exact date when repayment is legally due."]},
    ]
    chosen = rng.sample(pool, 4)
    return _table_q(
        rng,
        "27_promissory_note_seven_elements_table",
        "Identify the correct mandatory element of a promissory note for each document entry in the table below.",
        ["Promissory Note Entry", "Mandatory Element"],
        chosen,
        "A legal promissory note requires clear identification of the maker, payee, principal amount, place/date issued, maturity date, interest rate, and signature.",
        {
            "tier_1": "Review the seven formal components that make a promissory note legally enforceable.",
            "tier_2": "Match people (debtor vs creditor), Rand sums, % charge, and calendar dates to their formal labels.",
            "tier_3": "Use terms: Issuer / Maker, Payee, Principal amount, Interest rate, Place and date issued, Maturity / Due date.",
        },
        ["confuses_promissory_note_elements"],
    )


def _b28(rng: random.Random) -> Dict[str, Any]:
    maker, payee = _pick_two_people(rng)
    city = _pick_place(rng, rural=False)
    principal = rng.choice([1000, 1500, 2000, 3000, 4000, 5000])
    rate = rng.choice([6, 8, 10, 12])
    months = rng.choice([6, 12])
    term_lbl = "6 months (0,5 year)" if months == 6 else "1 year"
    due = "01 September 2025" if months == 6 else "01 March 2026"
    interest = (principal * rate * months) // 1200
    total = principal + interest
    diag = _svg_promissory_note(city, "01 March 2025", principal, maker, payee, due, rate)
    prompt = (
        f"Refer to the promissory note diagram issued on 01 March 2025. {maker} promises to pay {payee} "
        f"{_fmt_rand(principal)} plus simple interest at {rate}% per annum after {term_lbl} on {due}. "
        f"Calculate the total Rand amount {maker} must pay on {due}."
    )
    worked = (
        f"1. **Interest for {term_lbl} [2]:** {_fmt_rand(principal)} x {rate}% x ({months}/12) = **{_fmt_rand(interest)}**.\n"
        f"2. **Total repayment [1]:** {_fmt_rand(principal)} + {_fmt_rand(interest)} = **{_fmt_rand(total)}**."
    )
    return _q(
        rng,
        "28_promissory_note_interest_repayment",
        prompt,
        _fmt_rand(total),
        worked,
        "Promissory notes earn simple interest over their duration; total repayment equals principal plus accrued interest.",
        {
            "tier_1": "Calculate the interest charge first, then add it to the original principal amount.",
            "tier_2": f"Multiply {_fmt_rand(principal)} by {rate}/100" + (" and halve it for 6 months." if months == 6 else "."),
            "tier_3": f"Add the calculated interest ({_fmt_rand(interest)}) to {_fmt_rand(principal)}.",
        },
        ["forgets_to_add_principal_or_ignores_6_months_fraction"],
        [
            {"criterion": f"Calculates simple interest = {_fmt_rand(interest)}", "marks": 2},
            {"criterion": f"Adds principal to get total repayment = {_fmt_rand(total)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b29(rng: random.Random) -> Dict[str, Any]:
    issuer, payee = _pick_two_people(rng)
    start_options = [
        datetime.date(2025, 3, 10),
        datetime.date(2025, 5, 5),
        datetime.date(2025, 7, 12),
        datetime.date(2025, 9, 4),
    ]
    start = rng.choice(start_options)
    term_days = rng.choice([30, 60, 90])
    due = start + datetime.timedelta(days=term_days)
    start_str = start.strftime("%d %B %Y").lstrip("0")
    due_str = due.strftime("%d %B %Y").lstrip("0")
    prompt = (
        f"{issuer} signs a {term_days}-day promissory note in favour of {payee} dated {start_str}. "
        f"Remembering exact calendar day counts (April, June, September, November have 30 days; March, May, July, "
        f"August, October, December have 31 days), determine the exact maturity date."
    )
    worked = (
        f"1. **Start date [1]:** {start_str}.\n"
        f"2. **Count {term_days} calendar days forward [1]:** Adding {term_days} days reaches **{due_str}**."
    )
    return _q(
        rng,
        "29_promissory_note_maturity_days",
        prompt,
        due_str,
        worked,
        "Promissory notes with fixed day terms require exact calendar-day counting across 30- and 31-day months.",
        {
            "tier_1": "Count how many days remain in the issuing month first, then carry remaining days into the following months.",
            "tier_2": "Do not assume every month has 30 days; check whether each crossed month has 30 or 31 days.",
            "tier_3": f"Subtract remaining days in the start month from {term_days}, then advance through complete months.",
        },
        ["assumes_all_months_have_30_days"],
        [
            {"criterion": "Correctly applies month lengths (30 vs 31 days)", "marks": 1},
            {"criterion": f"Exact maturity date: {due_str}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="hard",
        cognitive_level="Complex Procedures",
        marks=2,
    )


def _b30(rng: random.Random) -> Dict[str, Any]:
    student = _pick_person(rng)
    tradition = rng.choice(["Tang Dynasty Chinese 'flying money' (feiqian)", "early Arab merchant credit bills (suftaja)"])
    prompt = (
        f"While reading history notes, {student} learns about {tradition}. "
        f"Why did long-distance merchants rely on these early paper credit notes?"
    )
    return _mcq(
        rng,
        "30_tang_flying_money_arab_suftaja",
        prompt,
        "Merchants deposited coins in one city and redeemed written credit notes safely at distant cities",
        [
            "Rulers forced farmers to print notes at home to replace sheep and grain",
            "Paper notes could be eaten as emergency rations during desert crossings",
            "Electronic satellite networks scanned barcodes on wooden tallies",
        ],
        "Early Chinese feiqian and Arab suftaja operated like proto-promissory notes, letting merchants deposit "
        "heavy metal coins locally and cash a paper document securely at distant hubs.",
        {
            "tier_1": "Think of the biggest danger of carrying tons of bronze, silver, or gold coins over thousands of kilometres.",
            "tier_2": "Identify how depositing money at origin and presenting a written certificate at destination helped trade.",
            "tier_3": "Pick the option explaining coin deposit and distant redemption without physical coin haulage.",
        },
        ["misunderstands_early_paper_credit_origins"],
    )


def _b31(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    amt = rng.choice([250, 420, 680])
    item = rng.choice(["school uniforms", "printing paper", "calculator sets"])
    prompt = (
        f"{p1} pays {_fmt_rand(amt)} cash immediately for {item} and gets a slip stamped 'PAID', whereas {p2} buys "
        f"{item} on credit and signs a document promising to pay {_fmt_rand(amt)} in 60 days. "
        f"Identify which document each person received or signed, and explain the key difference between them."
    )
    sample = (
        f"{p1} received a cash receipt (proof that payment has already been made), while {p2} signed a promissory note "
        f"(an unconditional written promise to pay a specified sum in the future)."
    )
    worked = (
        f"1. **{_escape(p1) if False else p1}'s document [1]:** **Receipt** — written proof confirming payment of {_fmt_rand(amt)} has already happened.\n"
        f"2. **{p2}'s document [1]:** **Promissory note** — legally binding promise to pay {_fmt_rand(amt)} at a future date.\n"
        f"3. **Key difference [1]:** A receipt records a completed payment; a promissory note creates a future credit obligation."
    )
    return _q(
        rng,
        "31_receipts_vs_promissory_notes",
        prompt,
        sample,
        worked,
        "Receipts document past completed payments, whereas promissory notes bind a debtor to future repayment.",
        {
            "tier_1": "Compare when the money actually leaves the buyer's pocket in each transaction.",
            "tier_2": "One slip says 'PAID' (past action); the other promises payment in 60 days (future obligation).",
            "tier_3": f"Name receipt for {p1} and promissory note for {p2}, stating past proof vs future promise.",
        },
        ["treats_receipt_and_promissory_note_as_identical"],
        [
            {"criterion": f"Identifies {p1}'s slip as a receipt (past payment proof)", "marks": 1},
            {"criterion": f"Identifies {p2}'s document as a promissory note (future payment promise)", "marks": 1},
            {"criterion": "Explains completed payment vs future obligation", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b32(rng: random.Random) -> Dict[str, Any]:
    depositor = _pick_person(rng)
    coins = rng.randint(30, 90)
    prompt = (
        f"Historically, traders like {depositor} stored {coins} gold coins in a secure goldsmith's vault and received "
        f"a signed paper deposit note in return. Explain how goldsmith deposit receipts eventually evolved into "
        f"everyday circulating paper banknotes."
    )
    sample = (
        f"Because traders trusted that the goldsmith held the {coins} gold coins safely and would redeem the receipt "
        f"on demand, buyers and sellers started handing over the paper deposit receipts directly to pay debts instead "
        f"of withdrawing heavy gold every time."
    )
    worked = (
        f"1. **Trust in backing [1]:** Merchants knew the paper note represented real {coins} gold coins locked in the vault.\n"
        f"2. **Direct circulation [1]:** Paying with the paper claim itself was lighter and faster than withdrawing coins repeatedly, turning receipts into representative paper money."
    )
    return _q(
        rng,
        "32_paper_money_origin_goldsmith_notes",
        prompt,
        sample,
        worked,
        "Public trust in vault reserves allowed paper deposit claims to circulate as money themselves.",
        {
            "tier_1": "Ask why a seller would accept a vault receipt instead of asking the buyer to fetch physical gold coins.",
            "tier_2": "Think about trust in the goldsmith's vault plus the convenience of handing over lightweight paper.",
            "tier_3": "Explain that confidence in coin redemption enabled deposit receipts to circulate directly as paper money.",
        },
        ["misses_link_between_vault_receipts_and_banknotes"],
        [
            {"criterion": "Explains public trust that vault holds gold backing the receipt", "marks": 1},
            {"criterion": "Explains convenience of circulating paper claims instead of withdrawing coins", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=2,
    )


def _b33(rng: random.Random) -> Dict[str, Any]:
    researcher = _pick_person(rng)
    denom = rng.choice([50, 100, 250, 500])
    diag = _svg_timeline(
        f"SA Paper Money Timeline — {researcher}",
        [
            ("1782", f"Lombaard {denom} rixdaalders"),
            ("1800s", "Commercial bank notes"),
            ("1921", "SA Reserve Bank sole issuer"),
            ("1962", "Security-printed Rand notes"),
        ],
    )
    prompt = (
        f"Refer to the timeline of South African paper money reviewed by {researcher} (noting early {denom}-rixdaalder issues). "
        f"What notable feature characterised South Africa's very first paper currency issued in 1782?"
    )
    return _mcq(
        rng,
        "33_sa_paper_money_lombaard_bank",
        prompt,
        "Early Cape notes were handwritten and numbered by the Lombaard Bank due to scarce printing presses",
        [
            "Notes were etched onto solid copper slabs by commercial cellphone companies",
            "Each 1782 note displayed a digital QR code linking to Pretoria",
            "The South African Reserve Bank printed R200 plastic cards in 1782",
        ],
        f"In 1782, Governor Van Plettenberg introduced paper riksdaalder notes (such as {denom}-rixdaalder issues) through the Lombaard Bank in the Cape; "
        f"because printing facilities were scarce, notes were initially written and numbered by hand.",
        {
            "tier_1": "Look at the 1782 milestone on the timeline.",
            "tier_2": "Eliminate anachronisms mentioning digital QR codes, cellphones, or 20th-century institutions in 1782.",
            "tier_3": "Choose the statement describing handwritten Lombaard Bank notes in the Cape.",
        },
        ["anachronistic_view_of_1782_cape_notes"],
        diagram_spec=diag,
    )


def _b34(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    note_amt = rng.choice([50, 100, 200])
    prompt = (
        f"{learner} compares an old gold-backed certificate with a modern South African {_fmt_rand(note_amt)} banknote "
        f"that cannot be exchanged for gold at the bank. Distinguish between **representative money** and **fiat money**."
    )
    sample = (
        f"Representative money (like the old certificate) is paper money backed by and redeemable for a physical commodity "
        f"such as gold or silver, whereas fiat money (like today's {_fmt_rand(note_amt)} Rand note) has no intrinsic commodity "
        f"value and is accepted because government law declares it legal tender and people trust it."
    )
    worked = (
        f"1. **Representative money [2]:** Paper currency directly backed by physical reserves (gold/silver) that holders could redeem.\n"
        f"2. **Fiat money [2]:** Modern currency like the {_fmt_rand(note_amt)} note declared legal tender by government decree, deriving value from public trust and scarcity rather than metal backing."
    )
    return _q(
        rng,
        "34_representative_vs_fiat_money",
        prompt,
        sample,
        worked,
        "Modern Rand banknotes are fiat money supported by central bank management, legal tender law, and public confidence.",
        {
            "tier_1": "Focus on what backs each currency type: physical metal vaults versus government decree and trust.",
            "tier_2": "Connect 'representative' with representing stored gold/silver, and 'fiat' with legal tender trust.",
            "tier_3": f"Contrast gold-backed redeemable certificates against modern {_fmt_rand(note_amt)} legal tender notes.",
        },
        ["thinks_modern_rands_are_backed_by_gold_reserves"],
        [
            {"criterion": "Defines representative money as backed by physical gold/silver reserves", "marks": 2},
            {"criterion": f"Defines fiat money ({_fmt_rand(note_amt)} note) as government legal tender backed by trust", "marks": 2},
        ],
        cognitive_level="Complex Procedures",
        marks=4,
    )


def _b35(rng: random.Random) -> Dict[str, Any]:
    face_val = rng.choice([50, 100, 200])
    prod_cost = rng.choice([2, 3, 4])
    diff = face_val - prod_cost
    buyer = _pick_person(rng)
    prompt = (
        f"A crisp {_fmt_rand(face_val)} South African banknote held by {buyer} costs approximately {_fmt_rand(prod_cost)} "
        f"in cotton-paper and security ink to manufacture. Calculate the Rand difference between its face value and its "
        f"physical production cost."
    )
    worked = (
        f"1. **Face value [1]:** {_fmt_rand(face_val)} (official purchasing power printed on the note).\n"
        f"2. **Intrinsic / production cost [1]:** {_fmt_rand(prod_cost)}.\n"
        f"3. **Difference [1]:** {_fmt_rand(face_val)} - {_fmt_rand(prod_cost)} = **{_fmt_rand(diff)}** (demonstrating fiat trust)."
    )
    return _q(
        rng,
        "35_face_value_vs_intrinsic_value",
        prompt,
        _fmt_rand(diff),
        worked,
        "Fiat money's purchasing power (face value) far exceeds the material value of the paper and ink used to print it.",
        {
            "tier_1": "Subtract the physical printing cost from the official Rand value printed on the banknote.",
            "tier_2": f"Compute {_fmt_rand(face_val)} minus {_fmt_rand(prod_cost)}.",
            "tier_3": f"State the difference in Rands: {_fmt_rand(diff)}.",
        },
        ["confuses_face_value_with_material_value"],
        [
            {"criterion": f"Correct subtraction {_fmt_rand(face_val)} - {_fmt_rand(prod_cost)}", "marks": 1},
            {"criterion": f"Final answer {_fmt_rand(diff)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b36(rng: random.Random) -> Dict[str, Any]:
    student = _pick_person(rng)
    era = rng.choice(["1816 to 1971", "19th and mid-20th centuries"])
    prompt = (
        f"During {era}, major economies operated under the Gold Standard, which {student} is studying in EMS. "
        f"What was the core rule of the Gold Standard?"
    )
    return _mcq(
        rng,
        "36_gold_standard_rise_and_end",
        prompt,
        "A nation's currency value was legally tied to a fixed weight of gold held by its central bank",
        [
            "Every worker was paid wages directly in raw unrefined gold ore bars",
            "Gold could only be owned by farmers and never used in jewellery or trade",
            "Banks destroyed all coins made of silver, nickel, or copper immediately",
        ],
        "Under the Gold Standard, paper notes were fixed to a set quantity of gold, giving exchange-rate stability "
        "until rising global trade led countries to abandon it by 1971 in favour of flexible fiat money.",
        {
            "tier_1": "Consider how paper currency linked its value to gold reserves between 1816 and 1971.",
            "tier_2": "Distinguish pegging currency value to a gold reserve from literally paying grocery bills in raw ore.",
            "tier_3": "Select the statement linking currency value to a fixed weight of central bank gold.",
        },
        ["misinterprets_gold_standard_as_barter"],
    )


def _b37(rng: random.Random) -> Dict[str, Any]:
    cashier = _pick_person(rng)
    note_val = rng.choice([50, 100, 200])
    shop = _pick_place(rng, rural=False)
    prompt = (
        f"Working at a busy supermarket till in {shop}, {cashier} is handed a {_fmt_rand(note_val)} banknote and wants "
        f"to check that it is genuine rather than counterfeit. Name and briefly describe THREE authentic security "
        f"features on South African banknotes."
    )
    sample = (
        f"(1) Watermark: holding the {_fmt_rand(note_val)} note to light reveals an embedded image; "
        f"(2) Security thread: a metallic strip woven through the paper shows currency details; "
        f"(3) Raised intaglio printing (or colour-shifting ink / micro-printing): textured ink on main portraits and numerals can be felt by touch."
    )
    worked = (
        f"1. **Watermark [1]:** Translucent portrait/animal watermark visible when held toward light.\n"
        f"2. **Security thread [1]:** Embedded metallic strip running vertically through the paper.\n"
        f"3. **Raised print / Colour-shifting ink / Micro-printing [1]:** Tactile intaglio ink and optically variable numerals verify authenticity."
    )
    return _q(
        rng,
        "37_security_features_sa_banknotes",
        prompt,
        sample,
        worked,
        "South African Reserve Bank notes combine visual, tactile, and optical security features to protect public trust against forgery.",
        {
            "tier_1": "Think of checks a cashier can perform by feeling the paper, tilting the note, and holding it up to light.",
            "tier_2": "Recall three real features: hidden light images, embedded metallic strips, and raised ink or colour shifts.",
            "tier_3": "Describe watermark, windowed security thread, and raised intaglio print (or colour-shifting ink).",
        },
        ["cannot_name_banknote_security_features"],
        [
            {"criterion": "Feature 1: Watermark visible against light", "marks": 1},
            {"criterion": "Feature 2: Embedded metallic security thread", "marks": 1},
            {"criterion": "Feature 3: Raised print / colour-shifting ink / micro-printing", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b38(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    amt = rng.choice([850, 1450, 2900, 4200])
    prompt = (
        f"{p1} opens a banking app on a smartphone and transfers {_fmt_rand(amt)} directly from a cheque account "
        f"into {p2}'s bank account without handling notes or coins. Which payment method was used?"
    )
    return _mcq(
        rng,
        "38_electronic_banking_eft_definition",
        prompt,
        "Electronic Funds Transfer (EFT)",
        ["Silent commodity barter", "Handwritten promissory IOU", "Gold-standard coin redemption"],
        "Electronic Funds Transfer (EFT) moves money digitally between bank accounts via computer networks, "
        "cellphone apps, or internet banking without physical cash.",
        {
            "tier_1": "Notice no physical cash, gold, or paper note was handed over.",
            "tier_2": "Identify the bank-to-bank digital payment acronym used on banking apps.",
            "tier_3": "Select Electronic Funds Transfer (EFT).",
        },
        ["confuses_eft_with_cash_payment"],
    )


def _b39(rng: random.Random) -> Dict[str, Any]:
    owner = _pick_person(rng)
    town = _pick_place(rng, rural=False)
    supplier_amt = rng.choice([3500, 5200, 7800])
    prompt = (
        f"{owner} runs a small catering business in {town} and pays suppliers {_fmt_rand(supplier_amt)} using EFT "
        f"instead of keeping large cash drawers on site. Explain THREE advantages electronic banking gives {owner}'s business."
    )
    sample = (
        f"(1) Security: avoids keeping {_fmt_rand(supplier_amt)} cash on site, lowering robbery risk; "
        f"(2) Speed and 24/7 convenience: payments can be sent anytime without travelling to queues; "
        f"(3) Digital audit trail: bank statements automatically record dates and references for bookkeeping."
    )
    worked = (
        f"1. **Safety [1]:** Eliminates carrying or storing {_fmt_rand(supplier_amt)} physical cash, reducing theft risk.\n"
        f"2. **24/7 Speed & convenience [1]:** Instant online transfers save travel time and bank-queue fees.\n"
        f"3. **Automatic recordkeeping [1]:** Electronic statements provide proof of payment for accounting."
    )
    return _q(
        rng,
        "39_electronic_banking_advantages",
        prompt,
        sample,
        worked,
        "Electronic banking lowers cash-handling risk, cuts travel time, and produces accurate accounting trails.",
        {
            "tier_1": "Compare holding cash in a till against sending digital bank payments from an office or phone.",
            "tier_2": "Consider safety from theft, time saved outside bank queues, and accounting records.",
            "tier_3": "State three distinct points: lower theft risk, 24/7 convenience/speed, and automatic bank statement records.",
        },
        ["only_lists_convenience_without_security_or_records"],
        [
            {"criterion": "Lower cash theft/robbery risk", "marks": 1},
            {"criterion": "24/7 speed and convenience without travelling", "marks": 1},
            {"criterion": "Digital audit trail / automatic recordkeeping", "marks": 1},
        ],
        cognitive_level="Routine Procedures",
        marks=3,
    )


def _b40(rng: random.Random) -> Dict[str, Any]:
    user = _pick_person(rng)
    channel = rng.choice(["fake banking SMS asking for a PIN", "suspicious email link mimicking a South African bank", "unfamiliar caller requesting a One-Time PIN (OTP)"])
    prompt = (
        f"{user} receives a {channel}. Identify ONE electronic banking security risk illustrated here and explain "
        f"TWO precautions customers should follow to protect their money online."
    )
    sample = (
        f"Risk: Phishing / social engineering fraud attempting to steal login credentials or OTPs. "
        f"Precautions: (1) Never share PINs, passwords, or OTP codes with anyone via SMS, email, or phone; "
        f"(2) Verify official banking apps/URLs directly and enable two-factor authentication or transaction alerts."
    )
    worked = (
        f"1. **Security risk [1]:** **Phishing** (or credential theft / digital fraud) tricking {user} into exposing private banking access.\n"
        f"2. **Precaution 1 [1]:** Never disclose PINs, passwords, or OTPs to links, emails, or callers.\n"
        f"3. **Precaution 2 [1]:** Use official banking apps/secure connections only and review SMS/app notifications immediately."
    )
    return _q(
        rng,
        "40_electronic_banking_risks_phishing",
        prompt,
        sample,
        worked,
        "Digital banking reduces physical robbery risk but introduces cyber threats like phishing, requiring strict PIN/OTP hygiene.",
        {
            "tier_1": "Name the cyber scam where fraudsters pretend to be your bank to steal secret login details.",
            "tier_2": "Think about how to handle OTPs/PINs and suspicious links safely.",
            "tier_3": "Identify phishing/fraud and state two concrete rules: keep PINs/OTPs secret and use official banking channels.",
        },
        ["thinks_banks_ask_for_pins_by_sms"],
        [
            {"criterion": "Identifies phishing / online fraud / credential theft risk", "marks": 1},
            {"criterion": "Precaution 1: Never share PIN, password, or OTP", "marks": 1},
            {"criterion": "Precaution 2: Use official bank app/URL or enable alerts", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b41(rng: random.Random) -> Dict[str, Any]:
    p1, p2 = _pick_two_people(rng)
    amt = rng.choice([25, 40, 60])
    prompt = (
        "Complete the table matching each everyday transaction to the most appropriate historical or modern payment method."
    )
    row_specs = [
        {
            "cells": [f"{p1} swaps a bag of homegrown lemons for {p2}'s repaired cricket bat", None],
            "expected": ["Barter"],
            "cell_hints": ["Direct swap of goods with zero currency."],
        },
        {
            "cells": [f"Paying {_fmt_rand(amt)} at a school tuckshop counter with notes and coins", None],
            "expected": ["Cash (Coins and Banknotes)"],
            "cell_hints": ["Physical legal tender used immediately over the counter."],
        },
        {
            "cells": ["Signing a legal paper promise to pay a hardware supplier R3 000 in 60 days", None],
            "expected": ["Promissory Note"],
            "cell_hints": ["Written future payment commitment bearing maturity date."],
        },
        {
            "cells": ["Paying school fees online straight from one bank account to the school's account", None],
            "expected": ["EFT / Electronic Banking"],
            "cell_hints": ["Bank-to-bank digital transfer."],
        },
    ]
    return _table_q(
        rng,
        "41_payment_methods_comparison_table",
        prompt,
        ["Transaction Scenario", "Payment Method"],
        row_specs,
        "Different eras and transaction types rely on barter, physical cash, credit promises (promissory notes), or electronic transfers.",
        {
            "tier_1": "Check whether money is absent, physical cash, a written future promise, or a bank-to-bank digital move.",
            "tier_2": "Distinguish immediate cash at a counter from 60-day written credit and online account transfers.",
            "tier_3": "Match each row to Barter, Cash (Coins and Banknotes), Promissory Note, or EFT / Electronic Banking.",
        },
        ["confuses_promissory_note_with_eft"],
    )


def _b42(rng: random.Random) -> Dict[str, Any]:
    seller, buyer = _pick_two_people(rng)
    item = rng.choice(["fresh bread", "stationery packs", "bicycle tyres", "school jerseys"])
    price = rng.choice([45, 70, 95, 130])
    prompt = (
        f"{seller} sells {item} for {_fmt_rand(price)} and accepts Rands from {buyer} because {seller} knows every "
        f"wholesaler and landlord will also accept those Rands in trade. Which fundamental role of money does this demonstrate?"
    )
    return _mcq(
        rng,
        "42_role_medium_of_exchange",
        prompt,
        "Medium of exchange",
        ["Perishable barter standard", "Nomadic subsistence reserve", "Commodity rationing ticket"],
        "Money acts as a medium of exchange when buyers and sellers universally accept it in payment for goods and services, eliminating barter's double coincidence of wants.",
        {
            "tier_1": "Think of the four roles of money: medium of exchange, unit of account, store of value, standard of deferred payment.",
            "tier_2": "Here money sits in the middle between selling goods and buying later supplies.",
            "tier_3": "Pick 'Medium of exchange'.",
        },
        ["confuses_medium_of_exchange_with_store_of_value"],
    )


def _b43(rng: random.Random) -> Dict[str, Any]:
    sample_items = rng.sample(TUCKSHOP_ITEMS, 3)
    items_with_prices: List[tuple[str, int]] = []
    for item in sample_items:
        label = item["name"] if isinstance(item, dict) else str(item)
        price = rng.randint(8, 28)
        items_with_prices.append((label, price))
    total = sum(p for _, p in items_with_prices)
    shop = _pick_place(rng, rural=False)
    diag = _svg_price_board(f"{shop} Tuckshop", items_with_prices)
    desc = ", ".join(f"{lbl} ({_fmt_rand(pr)})" for lbl, pr in items_with_prices)
    prompt = (
        f"Refer to the price board diagram for {shop} Tuckshop displaying {desc}. "
        f"Using Rand prices as a **unit of account**, calculate the total cost if a learner buys one of each item."
    )
    add_expr = " + ".join(_fmt_rand(p) for _, p in items_with_prices)
    worked = (
        f"1. **Unit of account role [1]:** Every item is priced in a common Rand yardstick ({add_expr}).\n"
        f"2. **Total basket cost [1]:** {add_expr} = **{_fmt_rand(total)}**."
    )
    return _q(
        rng,
        "43_role_unit_of_account",
        prompt,
        _fmt_rand(total),
        worked,
        "Money functions as a unit of account (measure of value) so prices of different items can be compared and totalled directly.",
        {
            "tier_1": "Read the three Rand prices listed on the price board diagram.",
            "tier_2": f"Add the three prices together: {add_expr}.",
            "tier_3": f"Sum all three prices to find {_fmt_rand(total)}.",
        },
        ["omits_an_item_when_totalling_basket"],
        [
            {"criterion": "Correctly reads all three item prices from diagram", "marks": 1},
            {"criterion": f"Calculates exact total {_fmt_rand(total)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
        diagram_spec=diag,
    )


def _b44(rng: random.Random) -> Dict[str, Any]:
    saver = _pick_person(rng)
    saved = rng.choice([450, 600, 850, 1200])
    months = rng.randint(6, 10)
    prompt = (
        f"{saver} saves {_fmt_rand(saved)} in a bank savings account for {months} months to buy winter school shoes. "
        f"Identify which role of money this demonstrates, explain why money works better here than saving ripe fruit, "
        f"and name ONE economic factor that can quietly reduce the purchasing power of saved cash over time."
    )
    sample = (
        f"This demonstrates money's role as a **store of value**. Unlike ripe fruit that spoils within days, "
        f"{_fmt_rand(saved)} keeps its form over {months} months. However, **inflation** (rising prices) reduces what "
        f"{_fmt_rand(saved)} can buy later if interest earned is below the inflation rate."
    )
    worked = (
        f"1. **Role [1]:** **Store of value** (preserving purchasing power from present income to future spending).\n"
        f"2. **Advantage over fruit [1]:** Banked money does not rot or perish over {months} months.\n"
        f"3. **Threat to stored value [1]:** **Inflation** erodes real purchasing power if prices rise faster than savings interest."
    )
    return _q(
        rng,
        "44_role_store_of_value",
        prompt,
        sample,
        worked,
        "Money stores purchasing power across time far better than perishable goods, though inflation gradually erodes real value.",
        {
            "tier_1": "Recall which role of money allows people to postpone spending until a later month.",
            "tier_2": "Compare durability of cash against food, then ask why R100 today might buy less in two years.",
            "tier_3": "Name 'Store of value', contrast with spoiling fruit, and identify 'inflation' as the purchasing-power risk.",
        },
        ["ignores_inflation_risk_on_stored_money"],
        [
            {"criterion": "Identifies role: Store of value", "marks": 1},
            {"criterion": "Contrasts durable money with perishable fruit", "marks": 1},
            {"criterion": "Identifies inflation as eroding future purchasing power", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
    )


def _b45(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    item = rng.choice(["a bicycle", "a study tablet", "a school blazer and kit", "a sewing machine"])
    months = rng.choice([4, 5, 6])
    instalment = rng.choice([150, 200, 250, 300])
    deposit = rng.choice([200, 300, 400])
    total_price = deposit + months * instalment
    prompt = (
        f"Using money as a **standard of deferred payment**, {buyer} buys {item} priced at {_fmt_rand(total_price)} on lay-by, "
        f"paying a cash deposit of {_fmt_rand(deposit)} today and settling the remaining balance over {months} equal "
        f"monthly instalments. Calculate each monthly instalment in Rands."
    )
    balance = total_price - deposit
    worked = (
        f"1. **Remaining balance [1]:** {_fmt_rand(total_price)} - {_fmt_rand(deposit)} = {_fmt_rand(balance)}.\n"
        f"2. **Monthly instalment [1]:** {_fmt_rand(balance)} / {months} = **{_fmt_rand(instalment)}** per month."
    )
    return _q(
        rng,
        "45_role_standard_of_deferred_payment",
        prompt,
        _fmt_rand(instalment),
        worked,
        "A stable unit of money lets buyers and sellers agree cleanly on future debt instalments (standard of deferred payment).",
        {
            "tier_1": "First subtract the deposit already paid today from the total price.",
            "tier_2": f"Divide the remaining balance by {months} months.",
            "tier_3": f"Compute ({_fmt_rand(total_price)} - {_fmt_rand(deposit)}) / {months}.",
        },
        ["forgets_to_subtract_deposit_before_dividing"],
        [
            {"criterion": f"Calculates remaining balance = {_fmt_rand(balance)}", "marks": 1},
            {"criterion": f"Divides by {months} to get {_fmt_rand(instalment)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="medium",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b46(rng: random.Random) -> Dict[str, Any]:
    learner = _pick_person(rng)
    amt = rng.choice([45, 80, 120])
    prompt = "Match each everyday South African money action in the table to the exact role of money being fulfilled."
    row_specs = [
        {
            "cells": [f"{learner} hands {_fmt_rand(amt)} to a baker for loaves of bread", None],
            "expected": ["Medium of exchange"],
            "cell_hints": ["Money moves directly in trade for goods."],
        },
        {
            "cells": ["Comparing a R90 textbook price tag against a R30 notebook price tag", None],
            "expected": ["Unit of account"],
            "cell_hints": ["Money measures and compares values in Rands."],
        },
        {
            "cells": ["Putting R500 into a savings account for December holidays", None],
            "expected": ["Store of value"],
            "cell_hints": ["Money preserves wealth across time for later spending."],
        },
        {
            "cells": ["Agreeing to repay a R1 200 loan in four R300 monthly payments", None],
            "expected": ["Standard of deferred payment"],
            "cell_hints": ["Money settles debts scheduled for future dates."],
        },
    ]
    return _table_q(
        rng,
        "46_four_roles_of_money_table",
        prompt,
        ["Everyday Money Action", "Role of Money"],
        row_specs,
        "Money fulfils four core economic roles: medium of exchange, unit of account, store of value, and standard of deferred payment.",
        {
            "tier_1": "Keep the four distinct roles in mind: trade (medium), pricing (unit), saving (store), and credit (deferred).",
            "tier_2": "Match paying now->Medium, comparing price tags->Unit, saving for later->Store, monthly repayments->Deferred.",
            "tier_3": "Fill in Medium of exchange, Unit of account, Store of value, and Standard of deferred payment.",
        },
        ["confuses_four_roles_of_money"],
    )


def _b47(rng: random.Random) -> Dict[str, Any]:
    amt = rng.choice([200, 100])
    prompt = (
        "Complete the table linking each practical test or feature of good money to its core characteristic."
    )
    row_specs = [
        {
            "cells": ["Notes are printed on tough cotton-blend paper and alloy coins resist rust", None],
            "expected": ["Durability"],
            "cell_hints": ["Can survive repeated circulation without tearing or rotting."],
        },
        {
            "cells": [f"A {_fmt_rand(amt)} note can be broken down into R50, R20, R10, and coin change", None],
            "expected": ["Divisibility"],
            "cell_hints": ["Can represent both large and tiny exact prices."],
        },
        {
            "cells": ["Ten banknotes representing R2 000 fit easily inside a jacket pocket", None],
            "expected": ["Portability / Transportability"],
            "cell_hints": ["Lightweight and compact to carry between markets."],
        },
        {
            "cells": ["Central bank controls note issue and embeds security features", None],
            "expected": ["Scarcity and trust"],
            "cell_hints": ["Limited supply prevents easy counterfeiting and preserves confidence."],
        },
    ]
    return _table_q(
        rng,
        "47_characteristics_durable_divisible_transportable",
        prompt,
        ["Practical Money Test", "Characteristic of Money"],
        row_specs,
        "Effective money must be durable, divisible into smaller units, portable to carry, and scarce enough to maintain trust.",
        {
            "tier_1": "Think of why coins and notes replaced cows, grain, and fragile shells.",
            "tier_2": "Match lasting power->Durability, breaking change->Divisibility, fitting in a pocket->Portability, supply limits->Scarcity and trust.",
            "tier_3": "Assign Durability, Divisibility, Portability / Transportability, and Scarcity and trust.",
        },
        ["confuses_characteristics_with_roles_of_money"],
    )


def _b48(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    note_paid = rng.choice([100, 200])
    item1 = rng.randint(18, 39)
    item2 = rng.randint(24, 49)
    total_spent = item1 + item2
    change = note_paid - total_spent
    prompt = (
        f"Because modern money is divisible, {buyer} can buy two school items costing {_fmt_rand(item1)} and "
        f"{_fmt_rand(item2)} and pay with a single {_fmt_rand(note_paid)} banknote. Calculate the exact Rand change "
        f"{buyer} must receive back."
    )
    worked = (
        f"1. **Total purchase cost [1]:** {_fmt_rand(item1)} + {_fmt_rand(item2)} = {_fmt_rand(total_spent)}.\n"
        f"2. **Exact change [1]:** {_fmt_rand(note_paid)} - {_fmt_rand(total_spent)} = **{_fmt_rand(change)}**."
    )
    return _q(
        rng,
        "48_divisibility_change_calculation",
        prompt,
        _fmt_rand(change),
        worked,
        "Money's divisibility allows small exact purchases to be settled accurately with standard change denominations.",
        {
            "tier_1": "Add the prices of the two items first, then subtract from the note handed to the cashier.",
            "tier_2": f"Calculate {_fmt_rand(item1)} + {_fmt_rand(item2)}, then subtract from {_fmt_rand(note_paid)}.",
            "tier_3": f"Compute {_fmt_rand(note_paid)} - {_fmt_rand(total_spent)} = {_fmt_rand(change)}.",
        },
        ["subtracts_only_one_item_from_note_paid"],
        [
            {"criterion": f"Finds combined cost = {_fmt_rand(total_spent)}", "marks": 1},
            {"criterion": f"Calculates exact change = {_fmt_rand(change)}", "marks": 1},
        ],
        question_type="calculation",
        difficulty="easy",
        cognitive_level="Routine Procedures",
        marks=2,
    )


def _b49(rng: random.Random) -> Dict[str, Any]:
    town = _pick_place(rng, rural=False)
    spend = rng.choice([2400, 3200, 4500])
    wages = rng.choice([3000, 4000, 5500])
    diag = _svg_two_way_flow(
        f"Consumer Economy Flow — {town}",
        "Households (Consumers)",
        f"Monthly wages: {_fmt_rand(wages)}",
        "Local Businesses (Producers)",
        f"Monthly sales: {_fmt_rand(spend)}",
        f"Consumer spending {_fmt_rand(spend)}",
        f"Wages {_fmt_rand(wages)} & goods",
    )
    prompt = (
        f"Refer to the cash-flow diagram for {town} where households earn {_fmt_rand(wages)} and spend {_fmt_rand(spend)} "
        f"at local businesses. Define a **consumer economy** and explain what happens to local jobs and businesses if "
        f"household spending drops sharply."
    )
    sample = (
        f"A consumer economy is a society driven primarily by households spending money on consumer goods and services "
        f"rather than producing everything themselves. If household spending drops below {_fmt_rand(spend)}, business revenue "
        f"falls, firms produce less, and workers risk wage cuts or job losses."
    )
    worked = (
        f"1. **Definition [1]:** A consumer economy relies on private household consumption spending ({_fmt_rand(spend)}) to drive production and growth.\n"
        f"2. **Effect of spending drop [2]:** Lower sales reduce business revenue and profits, forcing firms to cut production, postpone hiring, or reduce household wages ({_fmt_rand(wages)})."
    )
    return _q(
        rng,
        "49_consumer_economy_spending_cycle",
        prompt,
        sample,
        worked,
        "In modern consumer economies, household spending and business wage payments reinforce each other in a continuous circular flow.",
        {
            "tier_1": "Look at both arrows in the diagram linking households and businesses.",
            "tier_2": f"Trace what happens to business sales ({_fmt_rand(spend)}) first, and then to worker wages ({_fmt_rand(wages)}).",
            "tier_3": "Define consumer economy and explain how falling sales force businesses to scale back jobs and output.",
        },
        ["disconnects_spending_from_employment"],
        [
            {"criterion": "Defines consumer economy (driven by household buying of goods/services)", "marks": 1},
            {"criterion": "Explains falling business sales/revenue", "marks": 1},
            {"criterion": "Explains knock-on cutbacks in production or worker jobs/wages", "marks": 1},
        ],
        cognitive_level="Complex Procedures",
        marks=3,
        diagram_spec=diag,
    )


def _b50(rng: random.Random) -> Dict[str, Any]:
    buyer = _pick_person(rng)
    amt = rng.choice([1500, 2800, 4600, 6200])
    diag = _svg_five_stages(amt)
    prompt = (
        f"Refer to the five-stage diagram tracing how {buyer} could settle a {_fmt_rand(amt)} purchase across history "
        f"from Stage 1 (Barter) to Stage 5 (EFT). Evaluate THREE major efficiency improvements gained between "
        f"Stage 1 (Barter) and Stage 5 (EFT / Electronic Banking)."
    )
    sample = (
        f"Moving from Barter to EFT for a {_fmt_rand(amt)} transaction delivered: (1) elimination of the double coincidence "
        f"of wants through universal monetary acceptance; (2) exact divisibility and pricing via standardised Rand units; "
        f"and (3) extreme portability, speed, and safety because {_fmt_rand(amt)} moves digitally without hauling heavy goods or coins."
    )
    worked = (
        f"1. **Universal exchange [1]:** Replaces slow double-coincidence-of-wants matching with instant nationwide acceptance.\n"
        f"2. **Exact pricing & divisibility [1]:** Measures exact {_fmt_rand(amt)} value down to single cents rather than indivisible animals.\n"
        f"3. **Speed, portability & physical safety [2]:** Transfers {_fmt_rand(amt)} across long distances in seconds without heavy cargo or highway cash robbery."
    )
    return _q(
        rng,
        "50_evolution_of_money_synthesis",
        prompt,
        sample,
        worked,
        "Each monetary innovation solved physical, matching, valuation, or security bottlenecks present in earlier stages.",
        {
            "tier_1": "Compare Stage 1 (bartering goods) directly with Stage 5 (instant digital EFT).",
            "tier_2": "Focus on matching trade partners, measuring/splitting exact prices, and weight/travel risk.",
            "tier_3": f"Explain three clear gains for settling {_fmt_rand(amt)}: universal acceptance, divisibility/unit pricing, and speed/portability.",
        },
        ["lists_stages_without_evaluating_efficiency_gains"],
        [
            {"criterion": "Solves double coincidence of wants / universal acceptance", "marks": 1},
            {"criterion": f"Exact divisibility & common unit of account ({_fmt_rand(amt)})", "marks": 1},
            {"criterion": "High portability, speed, and reduced physical transport/robbery risk", "marks": 2},
        ],
        cognitive_level="Problem Solving",
        marks=4,
        diagram_spec=diag,
    )


BUILDERS_26_50: Dict[str, Callable[[random.Random], Dict[str, Any]]] = {
    "26_promissory_note_elements_diagram": _b26,
    "27_promissory_note_seven_elements_table": _b27,
    "28_promissory_note_interest_repayment": _b28,
    "29_promissory_note_maturity_days": _b29,
    "30_tang_flying_money_arab_suftaja": _b30,
    "31_receipts_vs_promissory_notes": _b31,
    "32_paper_money_origin_goldsmith_notes": _b32,
    "33_sa_paper_money_lombaard_bank": _b33,
    "34_representative_vs_fiat_money": _b34,
    "35_face_value_vs_intrinsic_value": _b35,
    "36_gold_standard_rise_and_end": _b36,
    "37_security_features_sa_banknotes": _b37,
    "38_electronic_banking_eft_definition": _b38,
    "39_electronic_banking_advantages": _b39,
    "40_electronic_banking_risks_phishing": _b40,
    "41_payment_methods_comparison_table": _b41,
    "42_role_medium_of_exchange": _b42,
    "43_role_unit_of_account": _b43,
    "44_role_store_of_value": _b44,
    "45_role_standard_of_deferred_payment": _b45,
    "46_four_roles_of_money_table": _b46,
    "47_characteristics_durable_divisible_transportable": _b47,
    "48_divisibility_change_calculation": _b48,
    "49_consumer_economy_spending_cycle": _b49,
    "50_evolution_of_money_synthesis": _b50,
}
