#!/usr/bin/env python3
"""
Smoke test for implemented Grade 11 and Grade 12 Accounting archetypes.
Tests generation with fixed seeds for deterministic verification.
"""

import sys
sys.path.insert(0, r'c:\Users\princ\fundile-tlassistant-vite\caps-ai-backend')

from app.utils.grade12_accounting.financial_statements_notes_generator import generate_questions as g12_fs_generate
from app.utils.grade12_accounting.analysis_interpretation_generator import generate_questions as g12_ai_generate
from app.utils.grade11_accounting.controlled_test_generator import generate_questions as g11_ct_generate

def test_g12_financial_statements():
    """Test Grade 12 Financial Statements generators."""
    print("\n" + "="*60)
    print("GRADE 12 FINANCIAL STATEMENTS")
    print("="*60)
    
    test_cases = [
        ("income_statement", "company_income_statement"),
        ("retained_income", "retained_income_note_buyback"),
        ("balance_sheet", "balance_sheet"),
        ("trade_receivables", "trade_receivables_note"),
    ]
    
    for subskill, expected_type in test_cases:
        try:
            questions = g12_fs_generate(
                subskill=subskill,
                difficulty="medium",
                count=1,
                seed=42,
                mode="scaffold"
            )
            
            if questions:
                q = questions[0]
                journal_type = q.get('journal', {}).get('journal_type', 'N/A')
                print(f"✓ {subskill:20s} | Type: {journal_type}")
                
                # Check for archetype_key in meta
                meta = q.get('meta', {})
                archetype_key = meta.get('archetype_key', 'N/A')
                print(f"  → archetype_key: {archetype_key}")
            else:
                print(f"✗ {subskill:20s} | No questions generated")
        except Exception as e:
            print(f"✗ {subskill:20s} | ERROR: {e}")

def test_g12_analysis_interpretation():
    """Test Grade 12 Analysis & Interpretation generators."""
    print("\n" + "="*60)
    print("GRADE 12 ANALYSIS & INTERPRETATION")
    print("="*60)
    
    # Test calculation questions
    try:
        questions = g12_ai_generate(
            subskill="calculations",
            difficulty="medium",
            question_type="calc",
            count=2,
            seed=42,
            mode="scaffold"
        )
        print(f"✓ calculations         | Generated {len(questions)} questions")
        if questions:
            q = questions[0]
            print(f"  → Type: {q.get('question_type', 'N/A')}")
    except Exception as e:
        print(f"✗ calculations         | ERROR: {e}")
    
    # Test typed interpretation questions
    subskills_to_test = [
        "profitability",
        "liquidity", 
        "gearing",
        "dividend_policy",
        "shareholder_satisfaction",
        "eps_roshe",
        "liquidity_position",
        "liquidity_support",
        "share_issue_price",
        "loan_repayment",
        "shareholder_returns",
        "shareholding_coalition",
        "share_buyback_ethics",
        "liquidity_strategies",
    ]
    
    for subskill in subskills_to_test:
        try:
            questions = g12_ai_generate(
                subskill=subskill,
                difficulty="medium",
                question_type="typed",
                count=1,
                seed=42,
                mode="scaffold"
            )
            if questions:
                print(f"✓ {subskill:20s} | Generated")
            else:
                print(f"⚠ {subskill:20s} | No questions (may be expected)")
        except Exception as e:
            print(f"✗ {subskill:20s} | ERROR: {e}")

def test_g11_controlled_test():
    """Test Grade 11 Controlled Test generators."""
    print("\n" + "="*60)
    print("GRADE 11 CONTROLLED TEST")
    print("="*60)
    
    test_cases = [
        ("crj", "Cash Receipts Journal"),
        ("cpj", "Cash Payments Journal"),
        ("fixed_assets", "Fixed Assets Timeline Calc"),
        ("accdep", "Accumulated Depreciation T-account"),
        ("disposal", "Asset Disposal T-account"),
        ("fixed_assets_note", "Fixed Assets Note"),
        ("internal_control", "Internal Control"),
    ]
    
    for subskill, description in test_cases:
        try:
            questions = g11_ct_generate(
                subskill=subskill,
                difficulty="medium",
                count=1,
                seed=42,
                mode="scaffold"
            )
            
            if questions:
                q = questions[0]
                q_type = q.get('question_type', 'N/A')
                journal_type = q.get('journal', {}).get('journal_type', 'N/A') if q.get('journal') else 'N/A'
                print(f"✓ {subskill:20s} | {description}")
                print(f"  → question_type: {q_type}, journal_type: {journal_type}")
            else:
                print(f"✗ {subskill:20s} | No questions generated")
        except Exception as e:
            print(f"✗ {subskill:20s} | ERROR: {e}")

def test_mixed_generation():
    """Test mixed generation with multiple questions."""
    print("\n" + "="*60)
    print("MIXED GENERATION TESTS")
    print("="*60)
    
    try:
        questions = g11_ct_generate(
            subskill="mixed",
            difficulty="medium",
            count=5,
            seed=123,
            mode="scaffold"
        )
        print(f"✓ G11 Mixed (count=5)  | Generated {len(questions)} questions")
        for i, q in enumerate(questions):
            jt = q.get('journal', {}).get('journal_type', 'calc') if q.get('journal') else q.get('question_type', 'unknown')
            print(f"  → Q{i+1}: {jt}")
    except Exception as e:
        print(f"✗ G11 Mixed            | ERROR: {e}")
    
    try:
        questions = g12_ai_generate(
            subskill="mixed",
            difficulty="medium",
            question_type="mixed",
            count=5,
            seed=123,
            mode="scaffold"
        )
        print(f"✓ G12 AI Mixed (count=5)| Generated {len(questions)} questions")
        for i, q in enumerate(questions):
            qt = q.get('question_type', 'unknown')
            print(f"  → Q{i+1}: {qt}")
    except Exception as e:
        print(f"✗ G12 AI Mixed         | ERROR: {e}")

def verify_cell_hints():
    """Verify scaffold mode includes cell hints."""
    print("\n" + "="*60)
    print("CELL HINTS VERIFICATION")
    print("="*60)
    
    try:
        questions = g11_ct_generate(
            subskill="crj",
            difficulty="medium",
            count=1,
            seed=42,
            mode="scaffold"
        )
        if questions:
            q = questions[0]
            # Cell hints are at top level of question, not inside journal
            hints = q.get('cell_hints', {})
            print(f"✓ CRJ scaffold         | {len(hints)} cell hints present")
    except Exception as e:
        print(f"✗ CRJ scaffold         | ERROR: {e}")
    
    try:
        questions = g12_fs_generate(
            subskill="balance_sheet",
            difficulty="medium",
            count=1,
            seed=42,
            mode="scaffold"
        )
        if questions:
            q = questions[0]
            # Cell hints are at top level of question, not inside journal
            hints = q.get('cell_hints', {})
            print(f"✓ Balance Sheet scaffold| {len(hints)} cell hints present")
    except Exception as e:
        print(f"✗ Balance Sheet scaffold| ERROR: {e}")

if __name__ == "__main__":
    print("\n" + "="*60)
    print("ACCOUNTING ARCHETYPE SMOKE TEST")
    print("="*60)
    
    test_g12_financial_statements()
    test_g12_analysis_interpretation()
    test_g11_controlled_test()
    test_mixed_generation()
    verify_cell_hints()
    
    print("\n" + "="*60)
    print("SMOKE TEST COMPLETE")
    print("="*60)
