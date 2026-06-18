#!/usr/bin/env python3
"""
API Endpoint Test for Grade 11 and Grade 12 Accounting archetypes.
Tests that the Flask API endpoints work correctly.
"""

import requests
import json
import sys

BASE_URL = "http://localhost:5000"  # Adjust if your Flask runs on different port

def test_endpoint(endpoint, payload, description):
    """Test a single API endpoint."""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n{'='*60}")
    print(f"Testing: {description}")
    print(f"Endpoint: {endpoint}")
    print(f"Payload: {json.dumps(payload, indent=2)}")
    print(f"{'='*60}")
    
    try:
        response = requests.post(url, json=payload, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get('success'):
                questions = data.get('questions', [])
                print(f"✓ SUCCESS - Generated {len(questions)} question(s)")
                if questions:
                    q = questions[0]
                    print(f"  → Question type: {q.get('question_type', 'N/A')}")
                    print(f"  → Has meta: {'meta' in q}")
                    if 'meta' in q:
                        archetype_key = q['meta'].get('archetype_key', 'N/A')
                        print(f"  → Archetype key: {archetype_key}")
                    if 'cell_hints' in q:
                        hints_count = len(q['cell_hints']) if q['cell_hints'] else 0
                        print(f"  → Cell hints: {hints_count}")
                return True
            else:
                print(f"✗ FAILED - API returned success=False")
                print(f"  Error: {data.get('error', 'Unknown error')}")
                return False
        else:
            print(f"✗ FAILED - HTTP {response.status_code}")
            print(f"  Response: {response.text[:200]}")
            return False
    except requests.exceptions.ConnectionError:
        print(f"✗ FAILED - Could not connect to {url}")
        print(f"  Make sure Flask server is running on {BASE_URL}")
        return False
    except Exception as e:
        print(f"✗ FAILED - Exception: {e}")
        return False

def main():
    """Run all API tests."""
    print("\n" + "="*60)
    print("API ENDPOINT TEST - Accounting Archetypes")
    print("="*60)
    
    results = []
    
    # Grade 11 tests
    results.append(test_endpoint(
        "/api/accounting/grade11/accounting/generate",
        {"subskill": "controlled-test", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G11 Controlled Test (CRJ/CPJ/Fixed Assets)"
    ))
    
    results.append(test_endpoint(
        "/api/accounting/grade11/accounting/generate",
        {"subskill": "reconciliation", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G11 Bank Reconciliation"
    ))
    
    # Grade 12 tests
    results.append(test_endpoint(
        "/api/accounting/grade12/accounting/financial-statements-notes/generate",
        {"subskill": "income_statement", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G12 Income Statement"
    ))
    
    results.append(test_endpoint(
        "/api/accounting/grade12/accounting/financial-statements-notes/generate",
        {"subskill": "retained_income", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G12 Retained Income Note"
    ))
    
    results.append(test_endpoint(
        "/api/accounting/grade12/accounting/financial-statements-notes/generate",
        {"subskill": "balance_sheet", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G12 Balance Sheet"
    ))
    
    results.append(test_endpoint(
        "/api/accounting/grade12/accounting/cash-flow/generate",
        {"subskill": "mixed", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G12 Cash Flow Statement"
    ))
    
    results.append(test_endpoint(
        "/api/accounting/grade12/accounting/cash-flow/generate",
        {"subskill": "dividends_paid", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G12 Dividends Paid Note"
    ))
    
    results.append(test_endpoint(
        "/api/accounting/grade12/accounting/cash-flow/generate",
        {"subskill": "taxation_paid", "difficulty": "medium", "count": 1, "seed": 42, "mode": "scaffold"},
        "G12 Taxation Paid Note"
    ))
    
    # Summary
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All API endpoints working!")
        return 0
    else:
        print(f"✗ {total - passed} endpoint(s) failed")
        return 1

if __name__ == "__main__":
    sys.exit(main())
