"""
Offline Pack Service for South African CAPS Question Bundles.
Provides on-demand deterministic question packs for 30-day offline study
with pre-baked 3-tier hints, marking schemas, and cryptographic lease tokens.
Zero LLM cost — 100% deterministic SymPy and Python generation.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import time
from datetime import datetime, timezone, timedelta
from typing import Any, Dict, List, Optional

from app.services.generator_registry import generate_variant, resolve_generator_key

# Secret key for offline lease validation
OFFLINE_SECRET_KEY = b"fundile_caps_offline_lease_auth_v1"

# Standard CAPS Term Topic Taxonomies across all grades (7–12) and subjects
CAPS_TERM_TOPICS: Dict[str, Dict[str, Dict[int, List[str]]]] = {
    "mathematics": {
        "7": {
            1: ["Whole Numbers", "Exponents", "Geometry of 2D Shapes"],
            2: ["Fractions", "Decimal Fractions", "Functions and Relationships"],
            3: ["Integers", "Algebraic Expressions", "Geometry of 3D Objects"],
            4: ["Measurement", "Data Handling", "Probability"]
        },
        "8": {
            1: ["Whole Numbers", "Integers", "Exponents"],
            2: ["Numeric Patterns", "Functions and Relationships", "Algebraic Expressions"],
            3: ["Algebraic Equations", "Geometry of Straight Lines", "Theorem of Pythagoras"],
            4: ["Area and Perimeter", "Surface Area and Volume", "Data Handling"]
        },
        "9": {
            1: ["Whole Numbers", "Integers", "Exponents", "Numeric and Geometric Patterns"],
            2: ["Functions and Relationships", "Algebraic Expressions", "Algebraic Equations"],
            3: ["Geometry of Straight Lines", "Geometry of 2D Shapes", "Theorem of Pythagoras"],
            4: ["Area and Perimeter", "Surface Area and Volume", "Data Handling", "Probability"]
        },
        "10": {
            1: ["Algebraic Expressions", "Equations and Inequalities", "Exponents", "Number Patterns"],
            2: ["Functions and Graphs", "Trigonometry", "Euclidean Geometry"],
            3: ["Analytical Geometry", "Finance and Growth", "Statistics"],
            4: ["Measurement", "Probability", "Euclidean Geometry"]
        },
        "11": {
            1: ["Exponents and Surds", "Equations and Inequalities", "Number Patterns"],
            2: ["Analytical Geometry", "Functions and Graphs", "Trigonometry"],
            3: ["Trigonometry", "Euclidean Geometry", "Finance and Growth"],
            4: ["Statistics", "Probability", "Measurement"]
        },
        "12": {
            1: ["Sequences and Series", "Functions and Inverses", "Calculus"],
            2: ["Calculus", "Trigonometry", "Euclidean Geometry"],
            3: ["Analytical Geometry", "Statistics", "Finance and Growth"],
            4: ["Probability", "Exam Preparation"]
        }
    },
    "accounting": {
        "10": {
            1: ["Accounting Equation", "Sole Trader", "Cash Receipts Journal", "Cash Payments Journal"],
            2: ["Debtors Journal", "Creditors Journal", "General Ledger", "Internal Control"],
            3: ["Fixed Assets", "Partnerships", "Ethics and GAAP"],
            4: ["Financial Statements", "Analysis and Interpretation", "Budgets"]
        },
        "11": {
            1: ["Accounting Equation", "Fixed Assets", "Partnership Accounting"],
            2: ["General Ledger", "Bank Reconciliation", "Creditors Reconciliation"],
            3: ["Asset Disposal", "Ethics and Corporate Governance", "Inventory Valuation"],
            4: ["Financial Statements", "Cost Accounting", "Budgeting"]
        },
        "12": {
            1: ["Company Financial Statements", "Statement of Financial Position", "Audit Reports"],
            2: ["Cash Flow Statement", "Financial Ratio Analysis", "Share Capital"],
            3: ["Inventory Valuation (FIFO and Weighted Average)", "Cost Accounting (Manufacturing)"],
            4: ["Budgeting and Cash Budgets", "Corporate Governance and King IV"]
        }
    },
    "physical_sciences": {
        "10": {
            1: ["Waves, Sound and Light", "Matter and Materials"],
            2: ["Chemical Change", "Magnetism and Electrostatics"],
            3: ["Electric Circuits", "Motion in 1D"],
            4: ["Energy", "Hydrosphere"]
        },
        "11": {
            1: ["Vectors and Newton's Laws", "Intermolecular Forces"],
            2: ["Stoichiometry and Ideal Gases", "Geometrical Optics"],
            3: ["Electrostatics", "Electric Circuits", "Energy in Chemical Change"],
            4: ["Acids and Bases", "Lithosphere and Mining"]
        },
        "12": {
            1: ["Momentum and Impulse", "Vertical Projectile Motion", "Organic Chemistry"],
            2: ["Work, Energy and Power", "Doppler Effect", "Rate and Extent of Reaction"],
            3: ["Chemical Equilibrium", "Acids and Bases", "Electrodynamics"],
            4: ["Optical Phenomena and Photoelectric Effect", "Electrochemistry"]
        }
    },
    "life_sciences": {
        "10": {
            1: ["Chemistry of Life", "Cell Cytology", "Mitosis"],
            2: ["Plant and Animal Tissues", "Support and Transport Systems"],
            3: ["Transport in Mammals", "Biosphere to Ecosystems"],
            4: ["Biodiversity and Classification", "History of Life"]
        },
        "11": {
            1: ["Biodiversity of Microorganisms", "Biodiversity of Plants", "Animal Body Plans"],
            2: ["Photosynthesis", "Cellular Respiration", "Animal Nutrition"],
            3: ["Gaseous Exchange", "Excretion in Humans"],
            4: ["Population Ecology", "Human Impact on the Environment"]
        },
        "12": {
            1: ["DNA: The Code of Life", "RNA and Protein Synthesis", "Meiosis"],
            2: ["Reproduction in Vertebrates", "Human Reproduction", "Genetics and Inheritance"],
            3: ["Nervous System and Receptors", "Endocrine System and Homeostasis"],
            4: ["Evolution by Natural Selection", "Human Evolution"]
        }
    },
    "business_studies": {
        "10": {
            1: ["Micro Environment", "Market Environment", "Macro Environment", "Business Functions"],
            2: ["Forms of Ownership", "Creative Thinking", "Business Opportunities"],
            3: ["Business Plan", "Management and Leadership"],
            4: ["Self-Management", "Relationships and Team Performance"]
        },
        "11": {
            1: ["Influences of Business Environments", "Challenges of Environments", "Socio-Economic Issues"],
            2: ["Entrepreneurial Qualities", "Forms of Ownership", "Creative Thinking and Problem Solving"],
            3: ["Stress, Crisis and Change Management", "Transforming a Business Plan to Action"],
            4: ["Team Dynamics and Conflict Management", "Introduction to Human Resources"]
        },
        "12": {
            1: ["Impact of Recent Legislation", "Human Resources Function", "Ethics and Professionalism"],
            2: ["Creative Thinking and Problem Solving", "Business Strategies", "CSR and Corporate Citizenship"],
            3: ["Human Rights and Diversity", "Team Performance Assessment", "Investment and Securities"],
            4: ["Quality of Performance", "Insurance and Assurance"]
        }
    },
    "ems": {
        "7": {
            1: ["History of Money", "Needs and Wants", "Goods and Services"],
            2: ["Businesses", "Accounting Concepts", "Income and Expenses"],
            3: ["Budgets", "The Entrepreneur", "Starting a Business"],
            4: ["Poverty and Inequality", "Savings", "Production Process"]
        },
        "8": {
            1: ["Government", "National Budget", "Standard of Living"],
            2: ["Accounting Concepts", "Source Documents", "Cash Receipts Journal"],
            3: ["Factors of Production", "Forms of Ownership", "Levels and Functions of Management"],
            4: ["Cash Payments Journal", "The General Ledger", "Trial Balance"]
        },
        "9": {
            1: ["Economic Systems", "Circular Flow", "Price Theory"],
            2: ["Cash Receipts and Payments Journals", "General Ledger and Trial Balance"],
            3: ["Debtors Journal and Creditors Journal", "Trade Unions", "Business Functions"],
            4: ["Transactions with Credit", "The Business Plan", "Financial Statements"]
        }
    },
    "natural_sciences": {
        "7": {
            1: ["The Biosphere", "Biodiversity", "Angiosperm Reproduction"],
            2: ["Properties of Materials", "Separating Mixtures", "Acids, Bases and Neutrals"],
            3: ["Sources of Energy", "Potential and Kinetic Energy", "Heat Energy Transfer"],
            4: ["Relationship of the Sun, Earth and Moon", "Historical Astronomy"]
        },
        "8": {
            1: ["Photosynthesis and Respiration", "Interactions and Interdependence in Ecosystems"],
            2: ["Atoms and Subatomic Particles", "Particle Model of Matter", "Chemical Reactions"],
            3: ["Static Electricity", "Electric Circuits", "Cost of Electrical Energy"],
            4: ["The Solar System", "Beyond the Solar System", "Looking into Space"]
        },
        "9": {
            1: ["Cell Structure and Cytology", "Human Organ Systems"],
            2: ["Compounds and Chemical Reactions", "Acids and Bases and Reactions of Metals"],
            3: ["Forces and Electric Cells", "Electric Circuits", "Safety with Electricity"],
            4: ["The Earth as a System", "Lithosphere and Mining", "Atmosphere and Birth of Stars"]
        }
    }
}


def _normalize_subject(subject: str) -> str:
    s = (subject or "").lower().strip()
    if s in ("maths", "mathematics", "math"):
        return "mathematics"
    if s in ("accounting", "acct"):
        return "accounting"
    if s in ("physics", "physical_sciences", "physsci"):
        return "physical_sciences"
    if s in ("lifesci", "life_sciences", "biology"):
        return "life_sciences"
    if s in ("business", "business_studies", "bs"):
        return "business_studies"
    if s in ("ems", "economic_management_sciences"):
        return "ems"
    if s in ("natsci", "natural_sciences"):
        return "natural_sciences"
    return s


def create_lease_token(subject: str, grade: str, term: int, expires_at: str) -> str:
    """Signs an offline lease token using HMAC-SHA256."""
    payload = f"{subject}:{grade}:{term}:{expires_at}".encode("utf-8")
    return hmac.new(OFFLINE_SECRET_KEY, payload, hashlib.sha256).hexdigest()


def verify_lease_token(subject: str, grade: str, term: int, expires_at: str, token: str) -> bool:
    """Verifies HMAC signature of an offline lease."""
    expected = create_lease_token(subject, grade, term, expires_at)
    return hmac.compare_digest(expected, token)


def get_topics_for_pack(subject: str, grade: str, term: int) -> List[str]:
    """Retrieves standard CAPS topics for the given subject, grade, and term."""
    norm_subj = _normalize_subject(subject)
    grade_str = "".join(ch for ch in str(grade) if ch.isdigit()) or "10"
    
    subj_data = CAPS_TERM_TOPICS.get(norm_subj, {})
    grade_data = subj_data.get(grade_str, {})
    return grade_data.get(term, ["Comprehensive Term Assessment"])


def build_offline_study_pack(
    subject: str,
    grade: str = "10",
    term: int = 1,
    count_per_topic: int = 5,
    custom_topics: Optional[List[str]] = None,
    student_id: Optional[str] = None
) -> Dict[str, Any]:
    """Generates an offline study pack bundle for a single subject and term."""
    norm_subj = _normalize_subject(subject)
    grade_str = "".join(ch for ch in str(grade) if ch.isdigit()) or "10"
    term_num = int(term)

    topics = custom_topics if (custom_topics and len(custom_topics) > 0) else get_topics_for_pack(norm_subj, grade_str, term_num)

    all_questions = []
    base_seed = int(time.time()) % 1_000_000

    for topic_idx, topic in enumerate(topics):
        for q_idx in range(count_per_topic):
            seed = base_seed + (topic_idx * 100) + q_idx
            try:
                res = generate_variant(
                    topic=topic,
                    subskill="mixed",
                    difficulty="medium",
                    count=1,
                    seed=seed,
                    grade=grade_str,
                    subject=norm_subj,
                    extra_config={"term": term_num, "mode": "compound"}
                )
                if res and isinstance(res, list):
                    for q in res:
                        # Ensure offline identifying metadata
                        q["offline_pack_id"] = f"{norm_subj}_gr{grade_str}_t{term_num}"
                        q["topic"] = topic
                        q["term"] = term_num
                        all_questions.append(q)
            except Exception as e:
                # Log non-fatal error and continue packing other topics
                print(f"Warning: Failed to generate question for {topic} (seed={seed}): {e}")

    # Build 30-day lease metadata
    now_utc = datetime.now(timezone.utc)
    expires_utc = now_utc + timedelta(days=30)
    expires_str = expires_utc.isoformat()
    lease_token = create_lease_token(norm_subj, grade_str, term_num, expires_str)

    pack_id = f"pack_{norm_subj}_grade{grade_str}_term{term_num}"
    serialized_size = len(json.dumps(all_questions).encode("utf-8"))

    return {
        "success": True,
        "pack_id": pack_id,
        "subject": norm_subj,
        "subject_name": norm_subj.replace("_", " ").title(),
        "grade": grade_str,
        "term": term_num,
        "topics": topics,
        "total_questions": len(all_questions),
        "questions": all_questions,
        "lease": {
            "issued_at": now_utc.isoformat(),
            "expires_at": expires_str,
            "days_valid": 30,
            "signature": lease_token,
            "student_id": student_id or "local_learner"
        },
        "size_bytes": serialized_size,
        "size_kb": round(serialized_size / 1024, 1),
        "size_mb": round(serialized_size / (1024 * 1024), 2)
    }
