import sys, json, hashlib
sys.path.insert(0, ".")

SEEDS = 500  # test across 500 seeds

def fingerprint(q):
    """Hash the correct_map or correct_value to detect unique questions."""
    cm = q.get("correct_map", {})
    cv = q.get("correct_value", None)
    parts = q.get("parts", [])
    bits = []
    if cm:
        for k in sorted(cm.keys()):
            bits.append(f"{k}={cm[k]}")
    if cv is not None:
        bits.append(f"cv={cv}")
    for p in parts:
        pcm = p.get("correct_map", {})
        pcv = p.get("correct_value", None)
        for k in sorted(pcm.keys()):
            bits.append(f"p_{k}={pcm[k]}")
        if pcv is not None:
            bits.append(f"pcv={pcv}")
    return hashlib.md5("|".join(bits).encode()).hexdigest()

def audit_generator(name, gen_fn):
    """Audit a generator for determinism and variety."""
    # 1. Determinism: same seed -> same output
    deterministic = True
    for seed in [0, 42, 99]:
        q1 = gen_fn(seed=seed, count=1, mode="scaffold")[0]
        q2 = gen_fn(seed=seed, count=1, mode="scaffold")[0]
        if fingerprint(q1) != fingerprint(q2):
            deterministic = False
            break

    # 2. Variety: different seeds -> different outputs
    fps = set()
    for seed in range(SEEDS):
        q = gen_fn(seed=seed, count=1, mode="scaffold")[0]
        fps.add(fingerprint(q))

    unique = len(fps)
    variety_pct = (unique / SEEDS) * 100

    # 3. Check if values use r.choice with small pools (limited combos)
    status = "OK" if deterministic and unique > 20 else "WARN"
    if not deterministic:
        status = "FAIL-DET"
    elif unique <= 10:
        status = "LOW-VAR"
    elif unique <= 50:
        status = "MED-VAR"

    print(f"  {name:<55} Det={deterministic}  Unique={unique:>4}/{SEEDS}  ({variety_pct:5.1f}%)  [{status}]")
    return deterministic, unique

# ===== GRADE 11 =====
print("=" * 90)
print("GRADE 11 ACCOUNTING GENERATORS")
print("=" * 90)

from app.utils.grade11_accounting.income_statement_generator import generate_questions as g11_is
audit_generator("income_statement_generator", g11_is)

from app.utils.grade11_accounting.reconciliation_generator import generate_questions as g11_recon
audit_generator("reconciliation_generator", g11_recon)

from app.utils.grade11_accounting.partnership_balance_sheet_generator import generate_questions as g11_pbs
audit_generator("partnership_balance_sheet_generator", g11_pbs)

from app.utils.grade11_accounting.fixed_assets_generator import generate_questions as g11_fa
audit_generator("fixed_assets_generator", g11_fa)

from app.utils.grade11_accounting.concepts_generator import generate_questions as g11_concepts
audit_generator("concepts_generator", g11_concepts)

from app.utils.grade11_accounting.controlled_test_generator import generate_questions as g11_ct
audit_generator("controlled_test_generator", g11_ct)

from app.utils.grade11_accounting.partnership_ledger_generator import generate_questions as g11_pl
audit_generator("partnership_ledger_generator", g11_pl)

# ===== GRADE 12 =====
print()
print("=" * 90)
print("GRADE 12 ACCOUNTING GENERATORS")
print("=" * 90)

from app.utils.grade12_accounting.financial_statements_notes_generator import generate_questions as g12_fsn
audit_generator("financial_statements_notes_generator", g12_fsn)

from app.utils.grade12_accounting.company_general_ledger_generator import generate_questions as g12_cgl
audit_generator("company_general_ledger_generator", g12_cgl)

from app.utils.grade12_accounting.cash_flow_generator import generate_questions as g12_cf
audit_generator("cash_flow_generator", g12_cf)

from app.utils.grade12_accounting.analysis_interpretation_generator import generate_questions as g12_ai
audit_generator("analysis_interpretation_generator", g12_ai)

from app.utils.grade12_accounting.concepts_generator import generate_questions as g12_concepts
audit_generator("concepts_generator", g12_concepts)

from app.utils.grade12_accounting.audits_governance_shareholding_generator import generate_questions as g12_ags
audit_generator("audits_governance_shareholding_generator", g12_ags)

# ===== GRADE 10 =====
print()
print("=" * 90)
print("GRADE 10 SOLE TRADER GENERATOR")
print("=" * 90)

try:
    from app.utils.grade10_sole_trader_generator import generate_questions as g10_st
    audit_generator("grade10_sole_trader_generator", g10_st)
except Exception as e:
    print(f"  grade10_sole_trader_generator: IMPORT ERROR: {e}")

print()
print("LEGEND: Det=Deterministic (same seed=same Q), Unique=distinct questions out of {SEEDS} seeds")
print("  OK=good, MED-VAR=moderate variety (>50 combos needed), LOW-VAR=very few combos, FAIL-DET=not deterministic")
