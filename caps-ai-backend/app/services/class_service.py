"""
Teacher LMS Cockpit & Class Service (Layer D — Phase D4)
Generates 6-character uppercase join codes, manages classes, student rosters,
and Firestore classes/{classId} records.
"""

import random
import string
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Tuple

def _get_firestore_client():
    try:
        from app.utils.firebase_admin_client import get_firestore_client
        return get_firestore_client()
    except Exception:
        return None

# Characters for unambiguous 6-char join codes (excluding 0, O, 1, I, L)
CODE_CHARS = "23456789ABCDEFGHJKMNPQRSTUVWXYZ"

# In-memory fallback registry for dev/testing when Firestore is unreachable
_MEMORY_CLASSES_DB: Dict[str, Dict[str, Any]] = {}
_MEMORY_JOIN_CODE_INDEX: Dict[str, str] = {}


def generate_join_code(subject: str = "") -> str:
    """Generates an unambiguous, easy-to-read 6-character code (e.g. 'M8X42K')."""
    random_part = "".join(random.choices(CODE_CHARS, k=6))
    return random_part


def create_class(
    teacher_id: str,
    teacher_name: str,
    class_name: str,
    subject: str,
    grade: str,
    school_id: Optional[str] = None,
    firestore_client: Any = None,
) -> Dict[str, Any]:
    """
    Creates a new class, generates its unique join code, and persists in classes/{classId}.
    """
    join_code = generate_join_code(subject)
    class_id = f"cls_{grade}_{subject.lower().replace(' ', '_')}_{join_code}"
    
    class_doc = {
        "classId": class_id,
        "name": class_name,
        "subject": subject,
        "grade": str(grade),
        "teacherId": teacher_id,
        "teacherName": teacher_name,
        "schoolId": school_id,
        "joinCode": join_code,
        "studentCount": 0,
        "students": [],
        "createdAt": datetime.now(timezone.utc).isoformat(),
    }

    # Store in memory cache
    _MEMORY_CLASSES_DB[class_id] = class_doc
    _MEMORY_JOIN_CODE_INDEX[join_code] = class_id

    # Store in Firestore if available
    db = firestore_client or _get_firestore_client()
    if db is not None:
        try:
            db.collection("classes").document(class_id).set(class_doc)
        except Exception as e:
            print(f"[class_service] Firestore write fallback to memory: {e}")

    return class_doc


def join_class_by_code(
    student_id: str,
    student_name: str,
    join_code: str,
    firestore_client: Any = None,
) -> Tuple[bool, Dict[str, Any]]:
    """
    Looks up class by join code and enrolls the student.
    Returns (success: bool, class_info_or_error: dict).
    """
    normalized_code = join_code.strip().upper()
    db = firestore_client or _get_firestore_client()
    class_doc = None
    class_id = None

    # Try memory cache first
    if normalized_code in _MEMORY_JOIN_CODE_INDEX:
        class_id = _MEMORY_JOIN_CODE_INDEX[normalized_code]
        class_doc = _MEMORY_CLASSES_DB.get(class_id)

    # Try Firestore query if not in memory
    if not class_doc and db is not None:
        try:
            query = db.collection("classes").where("joinCode", "==", normalized_code).limit(1).stream()
            for doc in query:
                class_doc = doc.to_dict()
                class_id = doc.id
                break
        except Exception as e:
            print(f"[class_service] Firestore query error: {e}")

    if not class_doc or not class_id:
        return False, {
            "error": "INVALID_JOIN_CODE",
            "message": f"No class found with join code '{normalized_code}'. Please double check the code with your teacher.",
        }

    # Check if student is already enrolled
    students = class_doc.get("students", [])
    if any(s.get("studentId") == student_id for s in students):
        return True, {
            "message": "Already enrolled in this class",
            "class": class_doc,
            "already_enrolled": True,
        }

    new_student = {
        "studentId": student_id,
        "studentName": student_name,
        "joinedAt": datetime.now(timezone.utc).isoformat(),
    }
    students.append(new_student)
    class_doc["students"] = students
    class_doc["studentCount"] = len(students)

    # Update memory
    _MEMORY_CLASSES_DB[class_id] = class_doc
    _MEMORY_JOIN_CODE_INDEX[normalized_code] = class_id

    # Update Firestore
    if db is not None:
        try:
            db.collection("classes").document(class_id).update({
                "students": students,
                "studentCount": len(students),
            })
            # Also append classId to student's enrolledClasses
            db.collection("students").document(student_id).collection("profile").document("current").set(
                {"enrolledClasses": [class_id]}, merge=True
            )
        except Exception as e:
            print(f"[class_service] Firestore update error: {e}")

    return True, {
        "message": f"Successfully joined {class_doc['name']}!",
        "class": class_doc,
        "already_enrolled": False,
    }


def list_classes_for_teacher(teacher_id: str, firestore_client: Any = None) -> List[Dict[str, Any]]:
    """Returns all classes created by a teacher."""
    db = firestore_client or _get_firestore_client()
    results = []

    if db is not None:
        try:
            query = db.collection("classes").where("teacherId", "==", teacher_id).stream()
            for doc in query:
                results.append(doc.to_dict())
            if results:
                return results
        except Exception:
            pass

    # Fallback to memory
    return [c for c in _MEMORY_CLASSES_DB.values() if c.get("teacherId") == teacher_id]


def get_class_roster(class_id: str, firestore_client: Any = None) -> Optional[Dict[str, Any]]:
    """Fetches full roster and metadata for a given class ID."""
    db = firestore_client or _get_firestore_client()

    if db is not None:
        try:
            doc = db.collection("classes").document(class_id).get()
            if doc.exists:
                return doc.to_dict()
        except Exception:
            pass

    return _MEMORY_CLASSES_DB.get(class_id)
