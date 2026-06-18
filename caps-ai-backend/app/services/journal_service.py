def validate_cash_receipts_journal(journal_data: dict) -> str:
    """Validates a Cash Receipts Journal for accounting accuracy and completeness."""
    try:
        if not journal_data or 'rows' not in journal_data:
            return "Error: Invalid journal data structure."
        
        rows = journal_data.get('rows', [])
        if not rows:
            return "Error: No journal entries found."
        
        total_analysis = 0
        total_bank = 0
        total_income = 0
        total_sundry = 0
        errors = []
        
        for i, row in enumerate(rows, 1):
            # Calculate row totals
            analysis = float(row.get('analysis', {}).get('main', 0) or 0) + float(row.get('analysis', {}).get('cents', 0) or 0) / 100
            bank = float(row.get('bank', {}).get('main', 0) or 0) + float(row.get('bank', {}).get('cents', 0) or 0) / 100
            income = float(row.get('income', {}).get('main', 0) or 0) + float(row.get('income', {}).get('cents', 0) or 0) / 100
            sundry = float(row.get('sundry_amount', {}).get('main', 0) or 0) + float(row.get('sundry_amount', {}).get('cents', 0) or 0) / 100
            
            total_analysis += analysis
            total_bank += bank
            total_income += income
            total_sundry += sundry
            
            # Check for required fields
            if not row.get('doc'):
                errors.append(f"Row {i}: Missing document number")
            if not row.get('day'):
                errors.append(f"Row {i}: Missing day")
            if not row.get('details'):
                errors.append(f"Row {i}: Missing details")
        
        # Check balancing
        if abs(total_bank - (total_income + total_sundry)) > 0.01:
            errors.append(f"Journal not balanced: Bank ({total_bank:.2f}) ≠ Income ({total_income:.2f}) + Sundry ({total_sundry:.2f})")
        
        if errors:
            return f"Validation failed:\n" + "\n".join(errors)
        else:
            return f"Journal is valid and balanced.\nTotals: Analysis={total_analysis:.2f}, Bank={total_bank:.2f}, Income={total_income:.2f}, Sundry={total_sundry:.2f}"
            
    except Exception as e:
        return f"Error validating journal: {str(e)}"

def validate_cash_payments_journal(journal_data: dict) -> str:
    """Validates a Cash Payments Journal for accounting accuracy and completeness."""
    try:
        if not journal_data or 'rows' not in journal_data:
            return "Error: Invalid journal data structure."
        
        rows = journal_data.get('rows', [])
        if not rows:
            return "Error: No journal entries found."
        
        total_bank = 0
        total_consumables = 0
        total_wages = 0
        total_sundry = 0
        errors = []
        
        for i, row in enumerate(rows, 1):
            # Calculate row totals
            bank = float(row.get('bank', {}).get('main', 0) or 0) + float(row.get('bank', {}).get('cents', 0) or 0) / 100
            consumables = float(row.get('consumables', {}).get('main', 0) or 0) + float(row.get('consumables', {}).get('cents', 0) or 0) / 100
            wages = float(row.get('wages', {}).get('main', 0) or 0) + float(row.get('wages', {}).get('cents', 0) or 0) / 100
            sundry = float(row.get('sundry_amount', {}).get('main', 0) or 0) + float(row.get('sundry_amount', {}).get('cents', 0) or 0) / 100
            
            total_bank += bank
            total_consumables += consumables
            total_wages += wages
            total_sundry += sundry
            
            # Check for required fields
            if not row.get('doc'):
                errors.append(f"Row {i}: Missing document number")
            if not row.get('day'):
                errors.append(f"Row {i}: Missing day")
            if not row.get('payee'):
                errors.append(f"Row {i}: Missing payee name")
        
        # Check balancing
        if abs(total_bank - (total_consumables + total_wages + total_sundry)) > 0.01:
            errors.append(f"Journal not balanced: Bank ({total_bank:.2f}) ≠ Consumables ({total_consumables:.2f}) + Wages ({total_wages:.2f}) + Sundry ({total_sundry:.2f})")
        
        if errors:
            return f"Validation failed:\n" + "\n".join(errors)
        else:
            return f"Journal is valid and balanced.\nTotals: Bank={total_bank:.2f}, Consumables={total_consumables:.2f}, Wages={total_wages:.2f}, Sundry={total_sundry:.2f}"
            
    except Exception as e:
        return f"Error validating journal: {str(e)}"

def extract_totals_from_validation(validation_text: str) -> dict:
    """Extracts totals from validation text."""
    totals = {}
    lines = validation_text.split('\n')
    for line in lines:
        if '=' in line and ':' in line:
            try:
                key, value = line.split(':', 1)
                key = key.strip().lower().replace(' ', '_')
                value = float(value.strip().split('=')[1].strip())
                totals[key] = value
            except:
                continue
    return totals

def calculate_journal_marks(student_totals: dict, expected_totals: dict, journal_type: str) -> int:
    """Calculates marks for journal submission."""
    if journal_type.lower() == 'crj':
        key_fields = ['bank', 'income', 'sundry']
    else:  # CPJ
        key_fields = ['bank', 'consumables', 'wages', 'sundry']
    
    total_marks = 0
    max_marks = 100
    
    for field in key_fields:
        if field in student_totals and field in expected_totals:
            student_val = student_totals[field]
            expected_val = expected_totals[field]
            
            if abs(student_val - expected_val) < 0.01:
                total_marks += max_marks // len(key_fields)
            elif abs(student_val - expected_val) < expected_val * 0.1:  # Within 10%
                total_marks += (max_marks // len(key_fields)) // 2
    
    return min(total_marks, max_marks)

def generate_journal_feedback(student_totals: dict, expected_totals: dict, journal_type: str) -> str:
    """Generates detailed feedback for journal submission."""
    feedback = []
    
    if journal_type.lower() == 'crj':
        fields = [('bank', 'Bank'), ('income', 'Current Income'), ('sundry', 'Sundry Accounts')]
    else:  # CPJ
        fields = [('bank', 'Bank'), ('consumables', 'Consumables'), ('wages', 'Wages'), ('sundry', 'Sundry Accounts')]
    
    for field_key, field_name in fields:
        if field_key in student_totals and field_key in expected_totals:
            student_val = student_totals[field_key]
            expected_val = expected_totals[field_key]
            
            if abs(student_val - expected_val) < 0.01:
                feedback.append(f"✓ {field_name}: Correct (R{student_val:.2f})")
            elif abs(student_val - expected_val) < expected_val * 0.1:
                feedback.append(f"⚠ {field_name}: Close but incorrect (R{student_val:.2f} vs R{expected_val:.2f})")
            else:
                feedback.append(f"✗ {field_name}: Incorrect (R{student_val:.2f} vs R{expected_val:.2f})")
    
    return "\n".join(feedback)

def mark_journal_submission(question_text: str, student_journal: dict, expected_journal: dict, journal_type: str) -> str:
    """Marks a student's journal submission against the expected answer."""
    try:
        if journal_type.lower() == 'crj':
            student_validation = validate_cash_receipts_journal(student_journal)
            expected_validation = validate_cash_receipts_journal(expected_journal)
        elif journal_type.lower() == 'cpj':
            student_validation = validate_cash_payments_journal(student_journal)
            expected_validation = validate_cash_payments_journal(expected_journal)
        else:
            return f"Error: Unknown journal type '{journal_type}'. Supported types: CRJ, CPJ"
        
        # Check if student journal is valid
        if "Error" in student_validation or "failed" in student_validation.lower():
            return f"Student journal has errors:\n{student_validation}\n\nMark: 0/100"
        
        # Compare key totals
        student_totals = extract_totals_from_validation(student_validation)
        expected_totals = extract_totals_from_validation(expected_validation)
        
        if not student_totals or not expected_totals:
            return "Error: Could not extract totals for comparison."
        
        # Calculate marks based on accuracy
        marks = calculate_journal_marks(student_totals, expected_totals, journal_type)
        
        feedback = generate_journal_feedback(student_totals, expected_totals, journal_type)
        
        return f"Journal Marking Results:\n\n{feedback}\n\nFinal Mark: {marks}/100"
        
    except Exception as e:
        return f"Error marking journal: {str(e)}"

def get_available_journals() -> dict:
    """Returns available journal templates."""
    return {
        "CRJ": {
            "name": "Cash Receipts Journal",
            "description": "Record all cash received by the business",
            "columns": ["Doc. no.", "Day", "Details", "Fol.", "Analysis of receipts", "Bank", "Current income", "Sundry accounts"],
            "template": {
                "companyName": "",
                "month": "",
                "journalNumber": "",
                "rows": [{"doc": "", "day": "", "details": "", "fol": "", "analysis": {"main": "", "cents": ""}, "bank": {"main": "", "cents": ""}, "income": {"main": "", "cents": ""}, "sundry_amount": {"main": "", "cents": ""}, "sundry_fol": "", "sundry_details": ""}]
            }
        },
        "CPJ": {
            "name": "Cash Payments Journal", 
            "description": "Record all cash payments made by the business",
            "columns": ["Doc. no.", "Day", "Name of payee", "Fol.", "Bank", "Consumables", "Wages", "Sundry accounts"],
            "template": {
                "companyName": "",
                "month": "",
                "journalNumber": "",
                "rows": [{"doc": "", "day": "", "payee": "", "fol": "", "bank": {"main": "", "cents": ""}, "consumables": {"main": "", "cents": ""}, "wages": {"main": "", "cents": ""}, "sundry_amount": {"main": "", "cents": ""}, "sundry_fol": "", "sundry_details": ""}]
            }
        }
    }
