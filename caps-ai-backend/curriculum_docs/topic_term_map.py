import os
import re
import json
import difflib
from pathlib import Path
try:
    import pymupdf
except ImportError:
    pymupdf = None
from collections import defaultdict

# Static CAPS Term Allocations Fallback Table with Ordered Main Topics
CAPS_FALLBACK_MAP = {
    "Mathematics": {
        "Gr7": {
            "Term 1": ["Whole numbers", "Exponents", "Construction of geometric figures", "Geometry of 2D shapes"],
            "Term 2": ["Fractions", "Decimal fractions", "Functions and relationships", "Algebraic expressions", "Algebraic equations"],
            "Term 3": ["Surface area and volume", "Geometry of 3D objects", "Data handling", "Transformational geometry"],
            "Term 4": ["Perimeter and area", "Probability", "Revision"]
        },
        "Gr8": {
            "Term 1": ["Whole numbers", "Integers", "Exponents", "Numeric and geometric patterns", "Functions and relationships"],
            "Term 2": ["Algebraic expressions", "Algebraic equations", "Geometry of straight lines", "Geometry of 2D shapes"],
            "Term 3": ["Construction of geometric figures", "Geometry of 3D objects", "Theorem of Pythagoras", "Area and perimeter"],
            "Term 4": ["Surface area and volume", "Data handling", "Probability"]
        },
        "Gr9": {
            "Term 1": ["Whole numbers", "Integers", "Exponents", "Numeric and geometric patterns", "Functions and relationships", "Algebraic expressions"],
            "Term 2": ["Algebraic equations", "Graphs", "Geometry of straight lines", "Geometry of 2D shapes"],
            "Term 3": ["Construction of geometric figures", "Theorem of Pythagoras", "Area and perimeter", "Surface area and volume"],
            "Term 4": ["Geometry of 3D objects", "Data handling", "Probability"]
        },
        "Gr10": {
            "Term 1": ["Algebraic expressions", "Exponents", "Patterns and Sequences", "Equations and inequalities", "Trigonometry"],
            "Term 2": ["Functions", "Analytical Geometry"],
            "Term 3": ["Finance and growth", "Statistics", "Trigonometry 2D", "Euclidean Geometry"],
            "Term 4": ["Measurement", "Probability", "Geometric Studio", "Probability Studio"]
        },
        "Gr11": {
            "Term 1": ["Exponents and surds", "Equations and inequalities", "Number patterns", "Trigonometry"],
            "Term 2": ["Functions and graphs", "Analytical geometry"],
            "Term 3": ["Finance growth and decay", "Probability", "Euclidean geometry"],
            "Term 4": ["Statistics", "Measurement"]
        },
        "Gr12": {
            "Term 1": ["Sequences and series", "Functions and inverse", "Polynomials", "Calculus", "Trigonometry"],
            "Term 2": ["Financial mathematics", "Analytical geometry", "Euclidean geometry"],
            "Term 3": ["Statistics", "Probability", "Counting principles"],
            "Term 4": ["Revision"]
        }
    },
    "PhysicalSciences": {
        "Gr10": {
            "Term 1": ["Skills for science", "Classification of matter", "States of matter and the kinetic theory molecular theory", "The atom", "The periodic table", "Chemical bonding", "Transverse pulses", "Transverse waves", "Longitudinal waves", "Sound", "Electromagnetic radiation"],
            "Term 2": ["The particles that substances are made of", "Physical and Chemical Changes", "Chemical equations", "Magnetism", "Electrostatics", "Electric circuits"],
            "Term 3": ["Reaction in aqeuous solution", "Quantitative aspects of chemical change", "Vectors and scalars", "Motion in one dimension", "Mechanical energy"],
            "Term 4": ["The hydrosphere", "Units of measurement applied"]
        },
        "Gr11": {
            "Term 1": ["Vectors in two dimensions", "Atomic combinations", "Intermolecular forces", "Ideal gases"],
            "Term 2": ["Newton's laws", "Geometrical optics", "2D and 3D wavefronts", "Electrostatics", "Electromagnetism"],
            "Term 3": ["Electric circuits", "Energy and chemical change", "Types of reaction", "Quantitative aspects of chemical change"],
            "Term 4": ["The lithosphere", "Units applied"]
        },
        "Gr12": {
            "Term 1": ["Momentum and Impulse", "Vertical projectile motion in one dimension", "Work energy and power", "Organic molecules"],
            "Term 2": ["Rate and Extent of Reaction", "Chemical equilibrium", "Acids and bases", "The Doppler effect"],
            "Term 3": ["Electrodynamics", "Electric circuits", "Optical phenomena and properties of matter", "Electrochemical reactions", "The chemical industry"],
            "Term 4": ["Skills for science", "Revision"]
        }
    },
    "LifeSciences": {
        "Gr10": {
            "Term 1": ["Molecules of life", "Cell structure", "Mitosis"],
            "Term 2": ["Plant tissues", "Animal tissues", "Organs", "Support and transport in plants", "Support system in animals"],
            "Term 3": ["Biosphere to ecosystems", "Biodiversity and classification"],
            "Term 4": ["Fossil record", "Geological timescale", "Biomes of South Africa"]
        },
        "Gr11": {
            "Term 1": ["Microorganisms", "Biodiversity of plants", "Biodiversity of animals"],
            "Term 2": ["Photosynthesis", "Animal nutrition", "Cellular respiration"],
            "Term 3": ["Gaseous exchange", "Excretion in humans", "Population ecology"],
            "Term 4": ["Water resources", "Biodiversity", "Food security", "Waste management"]
        },
        "Gr12": {
            "Term 1": ["DNA code of life", "RNA and protein synthesis", "Meiosis", "Genetics and inheritance"],
            "Term 2": ["Human reproduction", "Nervous system", "Senses eye and ear", "Endocrine system"],
            "Term 3": ["Homeostasis in humans", "Evolution by natural selection", "Human evolution"],
            "Term 4": ["Revision"]
        }
    },
    "EMS": {
        "Gr7": {
            "Term 1": ["History of money", "Needs and wants", "Goods and services"],
            "Term 2": ["Accounting concepts", "Income and expenses", "Budgets"],
            "Term 3": ["Entrepreneurial skills", "Businesses", "Starting a business"],
            "Term 4": ["Savings", "Inequality and poverty", "Revision"]
        },
        "Gr8": {
            "Term 1": ["Government", "National budget", "Standard of living"],
            "Term 2": ["Accounting concepts", "Source documents", "Cash Receipts Journal", "Cash Payments Journal"],
            "Term 3": ["Forms of ownership", "Levels and functions of management"],
            "Term 4": ["Financial literacy", "Markets", "Factor and Goods markets"]
        },
        "Gr9": {
            "Term 1": ["Economic systems", "Circular flow", "Price theory Demand and Supply"],
            "Term 2": ["Sectors of economy", "Cash Receipts Journal and Cash Payments Journal", "General Ledger", "Trial Balance"],
            "Term 3": ["Credit transactions Debtors Journal", "Debtors Ledger"],
            "Term 4": ["Creditors Journal", "Creditors Ledger", "Combined Trial Balance", "Functions of a business"]
        }
    },
    "NaturalSciences": {
        "Gr7": {
            "Term 1": ["Biosphere", "Biodiversity", "Sexual reproduction in angiosperms", "Human reproduction"],
            "Term 2": ["Properties of materials", "Separating mixtures", "Acids bases and neutrals", "Introduction to Periodic Table"],
            "Term 3": ["Sources of energy", "Potential and kinetic energy", "Heat transfer", "Insulation and energy saving", "National electricity grid"],
            "Term 4": ["Relationship of Moon to Earth", "Historical development of astronomy"]
        },
        "Gr8": {
            "Term 1": ["Photosynthesis and respiration", "Interactions and interdependence in ecosystems"],
            "Term 2": ["Atoms", "Particle model of matter", "Chemical reactions"],
            "Term 3": ["Static electricity", "Energy and change", "Electric circuits", "Visible light"],
            "Term 4": ["The Solar System", "Beyond the Solar System", "Looking into space"]
        },
        "Gr9": {
            "Term 1": ["Cells as the basic units of life", "Systems in the human body", "Human reproduction", "Circulatory and respiratory systems"],
            "Term 2": ["Compounds and chemical reactions", "Reactions of metals with oxygen", "Reactions of non metals with oxygen", "Acids and bases", "Reactions of acids with bases"],
            "Term 3": ["Forces", "Electric circuits", "Safety with electricity", "Energy and the national electricity grid"],
            "Term 4": ["The Earth as a system", "Lithosphere", "Mining of mineral resources", "Atmosphere"]
        }
    },
    "Geography": {
        "Gr10": {
            "Term 1": ["Composition and structure of atmosphere", "Heating of atmosphere", "Moisture in atmosphere"],
            "Term 2": ["Plate tectonics", "Folding and faulting", "Earthquakes and volcanoes"],
            "Term 3": ["Population structure", "Population movement", "Mortality and HIV AIDS"],
            "Term 4": ["Water resources in South Africa", "Oceans and rivers", "Water management"]
        },
        "Gr11": {
            "Term 1": ["Global air circulation", "Synoptic weather maps", "Climate of Africa"],
            "Term 2": ["Topography associated with inclined strata", "Slopes", "Mass movements"],
            "Term 3": ["Development concepts", "Frameworks and trade", "Globalisation"],
            "Term 4": ["Soil resources", "Energy resources", "Renewable and non-renewable energy"]
        },
        "Gr12": {
            "Term 1": ["Mid-latitude cyclones", "Tropical cyclones", "Subtropical anticyclones", "Valley and city climates"],
            "Term 2": ["Drainage systems", "Fluvial processes", "Catchment and river management"],
            "Term 3": ["Rural settlement", "Urban settlement", "Land use zones", "Urban issues"],
            "Term 4": ["Agriculture", "Mining", "Secondary and tertiary sectors in South Africa"]
        }
    },
    "BusinessStudies": {
        "Gr10": {
            "Term 1": ["Micro-environment", "The market environment", "The macro-environment", "The interrelationship of the micro market & macro environments", "Business sectors"],
            "Term 2": ["Contemporary socio-economic issues", "Social responsibility", "Forms of ownership", "Business opportunities & related factors", "Business location decisions"],
            "Term 3": ["Creative thinking and problem solving", "Business functions & the activities of business", "The concept of quality"],
            "Term 4": ["Presentation of business information", "Understanding business plans & implications", "Self-management", "Relationships & team performance", "Contracts", "Entrepreneurial qualities"]
        },
        "Gr11": {
            "Term 1": ["Influencies on business environments", "The challenges of the business environments", "Adapting to challenges in the business environment", "Contemporary socio-economic factors & businesses", "Business sectors"],
            "Term 2": ["Benefits of a company over other forms of ownership", "Avenues of acquiring businesses", "Creative thinking & problem solving", "Stress crisis & change management", "Professionalism & ethics"],
            "Term 3": ["Transformation of a business plan into an action plan", "A business venture based on a business plan", "The presentation of business information", "Introduction to the human resources function", "The marketing function", "The production function"],
            "Term 4": ["Team dynamics & conflict management", "Citizenship & responsibilities", "Assessment of enterpreneural qualities in business"]
        },
        "Gr12": {
            "Term 1": ["Impact of recent legislation on businesses", "Human rights inclusivity & environmental issues", "Macro-environment Business strategies", "Business sectors & their environments"],
            "Term 2": ["Creative thinking & problem solving", "Ethics and professionalism", "Management & leadership", "Forms of ownership Success & failure in business", "Quality of performance"],
            "Term 3": ["Investments Insurance", "Investement Securities", "Presentations & data responses", "Human resources function"],
            "Term 4": ["Team performance assessment & conflict management"]
        }
    },
    "TechnicalMathematics": {
        "Gr10": {
            "Term 1": ["Introduction", "Number Systems", "Algebraic expressions", "Exponents", "Equalities and inequalities", "Trigonometry"],
            "Term 2": ["Functions and graphs", "Analytical Geometry"],
            "Term 3": ["Circles angles and angular Movement", "Finance and Growth", "Geometry"],
            "Term 4": ["Mensuration"]
        },
        "Gr11": {
            "Term 1": ["Exponents and surds", "Logarithms", "Equations", "Trigonometry"],
            "Term 2": ["Functions and graphs", "Analytical geometry"],
            "Term 3": ["Circles angles and angular movement", "Finance growth and decays", "Euclidean geometry"],
            "Term 4": ["Mensuration"]
        },
        "Gr12": {
            "Term 1": ["Complex numbers", "Polynomials", "Differentiation", "Integration", "Trigonometry"],
            "Term 2": ["Financial mathematics", "Analytical geometry", "Euclidean Geometry Proportionality and similarity"],
            "Term 3": ["Circles angles and angular movement", "Mensuration"],
            "Term 4": ["Revision"]
        }
    },
    "MathematicalLiteracy": {
        "Gr10": {
            "Term 1": ["Conversions and time", "Banking interest and taxation"],
            "Term 2": ["Data handling", "Assembly diagrams floor plans and packaging"],
            "Term 3": ["Measurement", "Maps plans and other representations"],
            "Term 4": ["Finance", "Probability"]
        },
        "Gr11": {
            "Term 1": ["Conversions and time", "Finance"],
            "Term 2": ["Data handling", "Maps and plans"],
            "Term 3": ["Measurement", "Income and expenditure"],
            "Term 4": ["Probability"]
        },
        "Gr12": {
            "Term 1": ["Finance", "Measurement"],
            "Term 2": ["Maps plans and other representations", "Data handling"],
            "Term 3": ["Taxation", "Probability"],
            "Term 4": ["Revision"]
        }
    }
}

def sanitize_subject_key(subject):
    sub = subject.replace(" ", "").replace("-", "").replace("_", "")
    if sub in ["PhysicalScience", "PhysicalSciences", "PhySci", "PhysSci"]:
        return "PhysicalSciences"
    elif sub in ["LifeScience", "LifeSciences", "LS"]:
        return "LifeSciences"
    elif sub in ["BusinessStudy", "BusinessStudies", "BS"]:
        return "BusinessStudies"
    elif sub in ["TechnicalMaths", "TechnicalMathematics", "TechMaths"]:
        return "TechnicalMathematics"
    elif sub in ["MathLiteracy", "MathematicalLiteracy", "MathLit"]:
        return "MathematicalLiteracy"
    elif sub in ["Math", "Maths", "Mathematics"]:
        return "Mathematics"
    elif sub in ["EMS", "EconomicAndManagementSciences", "EconomicManagementSciences"]:
        return "EMS"
    elif sub in ["NaturalScience", "NaturalSciences", "NS"]:
        return "NaturalSciences"
    elif sub in ["Geography", "Geo"]:
        return "Geography"
    return subject

def normalize_text(text):
    """Normalize text for fuzzy string matching (strip non-alphanumeric, lowercase)."""
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

_SYLLABUS_CACHE = {}
_MANUAL_CACHE = {}

def extract_syllabus_text(curriculum_docs_dir, subject, grade):
    """Extracts raw text from Syllabus_<Subject>_<Grade>.pdf if available, with memoization."""
    sub_key = sanitize_subject_key(subject)
    gr_num = re.sub(r'\D', '', grade)
    cache_key = (sub_key, gr_num)
    if cache_key in _SYLLABUS_CACHE:
        return _SYLLABUS_CACHE[cache_key]

    docs_dir = Path(curriculum_docs_dir).resolve()
    pattern = f"Syllabus_*{sub_key}*Gr{gr_num}*.pdf"
    syllabus_files = list(docs_dir.glob(pattern))
    if not syllabus_files:
        syllabus_files = list(docs_dir.glob(f"Syllabus_*Gr{gr_num}*.pdf"))

    for pdf_path in syllabus_files:
        try:
            doc = pymupdf.open(str(pdf_path))
            full_text = ""
            for page in doc:
                full_text += page.get_text("text") + "\n"
            doc.close()
            _SYLLABUS_CACHE[cache_key] = full_text
            return full_text
        except Exception:
            pass
    _SYLLABUS_CACHE[cache_key] = ""
    return ""

def get_term_and_topic_info(subject, grade, topic_filename, curriculum_docs_dir=None):
    """
    Given a subject, grade, and textbook topic filename, performs fuzzy matching to determine:
    1. Target Term (Term 1, Term 2, Term 3, Term 4)
    2. Position number (01, 02, 03...) within that Term
    3. Formatted filename (e.g. "01. Chemical bonding.md")
    4. Relevant CAPS syllabus context for Qwen Vision
    """
    sub_key = sanitize_subject_key(subject)
    gr_key = grade if grade.startswith("Gr") else f"Gr{grade}"

    clean_topic = topic_filename
    clean_topic = re.sub(r'^(?:Textbook|StudyGuide)_[A-Za-z]+_Gr\d+_', '', clean_topic)
    clean_topic = re.sub(r'\.pdf$', '', clean_topic)
    clean_topic = clean_topic.replace('-', ' ').replace('_', ' ').strip()

    norm_target = normalize_text(clean_topic)

    best_term = "Term 1"
    best_pos = 1
    highest_ratio = 0.0

    if sub_key in CAPS_FALLBACK_MAP and gr_key in CAPS_FALLBACK_MAP[sub_key]:
        terms = CAPS_FALLBACK_MAP[sub_key][gr_key]
        for term_name, topic_list in terms.items():
            for idx, candidate in enumerate(topic_list, 1):
                norm_cand = normalize_text(candidate)
                
                if norm_target in norm_cand or norm_cand in norm_target:
                    ratio = 0.95
                else:
                    ratio = difflib.SequenceMatcher(None, norm_target, norm_cand).ratio()

                if ratio > highest_ratio:
                    highest_ratio = ratio
                    best_term = term_name
                    best_pos = idx

    if highest_ratio < 0.4:
        best_term = "Term 1"
        best_pos = 1

    pos_str = f"{best_pos:02d}"
    formatted_filename = f"{pos_str}. {clean_topic}.md"

    syllabus_context = f"CAPS Curriculum Context for {subject} {grade} ({best_term}, Topic {pos_str}: {clean_topic})."
    if curriculum_docs_dir:
        syl_text = extract_syllabus_text(curriculum_docs_dir, subject, grade)
        if syl_text:
            lines = syl_text.split('\n')
            relevant_lines = [l.strip() for l in lines if normalize_text(clean_topic) in normalize_text(l) or any(w in l.lower() for w in clean_topic.lower().split() if len(w)>3)]
            if relevant_lines:
                syllabus_snippet = " | ".join(relevant_lines[:5])
                syllabus_context += f" Syllabus Scope: {syllabus_snippet}"

    return {
        "term": best_term,
        "pos": best_pos,
        "pos_str": pos_str,
        "clean_topic": clean_topic,
        "formatted_filename": formatted_filename,
        "syllabus_context": syllabus_context
    }

def _build_manual_files_index(docs_path):
    """Pre-indexes all existing manual markdown files once for fast lookups."""
    if "index" in _MANUAL_CACHE:
        return _MANUAL_CACHE["index"]

    index = defaultdict(list)
    for md_file in docs_path.glob("**/*.md"):
        if "curriculum_docs_auto" in str(md_file):
            continue
        rel = str(md_file.relative_to(docs_path)).lower()
        parts = rel.split(os.sep)
        if len(parts) < 2:
            continue
        folder = parts[0]
        fname_clean = md_file.stem.replace('-', ' ').replace('_', ' ').lower()
        norm_f = re.sub(r'[^a-zA-Z0-9]', '', fname_clean)
        words = set(w for w in fname_clean.split() if len(w) > 3)
        index[folder].append({
            "path": md_file,
            "norm": norm_f,
            "words": words,
            "stem": fname_clean
        })

    _MANUAL_CACHE["index"] = index
    return index

def find_existing_manual_file(curriculum_docs_dir, subject, grade, topic_name):
    """
    Checks if a manually authored markdown file already exists for this topic
    in the original subject directories using a pre-built index.
    """
    docs_path = Path(curriculum_docs_dir).resolve()
    index = _build_manual_files_index(docs_path)

    gr_num = re.search(r'\d+', grade).group(0) if re.search(r'\d+', grade) else ""
    sub_low = subject.lower().replace(" ", "").replace("_", "")

    clean_top = topic_name.replace('-', ' ').replace('_', ' ').lower()
    norm_top = re.sub(r'[^a-zA-Z0-9]', '', clean_top)
    top_words = set(w for w in clean_top.split() if len(w) > 3)

    best_file = None
    best_score = 0.0

    for folder_name, file_list in index.items():
        if gr_num not in folder_name:
            continue
        if not any(k in folder_name for k in [sub_low, 'accounting' if 'acc' in sub_low else '', 'physical' if 'phys' in sub_low else '', 'business' if 'bus' in sub_low else '', 'math' if 'math' in sub_low else '']):
            continue

        for item in file_list:
            norm_f = item["norm"]
            ratio = difflib.SequenceMatcher(None, norm_top, norm_f).ratio()
            if norm_top in norm_f or norm_f in norm_top:
                ratio = max(ratio, 0.85)

            if top_words and top_words.issubset(item["words"]):
                ratio = max(ratio, 0.9)

            if ratio > best_score:
                best_score = ratio
                best_file = item["path"]

    if best_score >= 0.55:
        return best_file
    return None


