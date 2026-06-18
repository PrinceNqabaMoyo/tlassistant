from typing import Dict, Any, Optional

# This defines the mappings from advanced High School subskills 
# down to their foundational Middle School precursors.

PROGRESSION_MAP = {
    # Business Studies Mappings
    "bs10_business_environments": "ems9_economic_systems",
    "bs10_business_functions": "ems8_business_functions",
    "bs10_business_sectors": "ems7_needs_and_wants",
    "bs11_business_sectors": "bs10_business_sectors",
    
    # Accounting Mappings
    "acct10_cash_receipts_journal": "ems8_crj_basics",
    "acct10_accounting_equation": "ems7_accounting_equation",
}

def handle_progression_drop(student_id: str, failed_generator_id: str, consecutive_failures: int) -> Optional[Dict[str, str]]:
    """
    Checks if a student should be dropped to a lower level based on consecutive failures.
    If so, returns the precursor generator ID and an intervention message.
    """
    THRESHOLD = 3
    
    if consecutive_failures >= THRESHOLD:
        precursor = PROGRESSION_MAP.get(failed_generator_id)
        if precursor:
            return {
                "action": "drop_level",
                "target_generator": precursor,
                "intervention_message": "It looks like you're struggling with this advanced topic. Let's quickly review the basics to bolster your understanding!"
            }
            
    return {"action": "continue"}

def process_student_success(student_id: str, current_generator_id: str, is_precursor: bool):
    """
    If the student was in a dropped precursor level and passed, 
    they are bumped back to their original grade level.
    """
    if is_precursor:
        # In a real app, update Firestore state to remove the precursor lock
        return {
            "action": "bump_level",
            "intervention_message": "Great job! You've mastered the basics. Let's go back to your current grade level."
        }
    return {"action": "continue"}
