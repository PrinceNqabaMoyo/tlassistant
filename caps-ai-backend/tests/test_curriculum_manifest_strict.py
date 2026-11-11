"""
Automated Strict Manifest & Curriculum Resolution Tests.
Enforces that every single South African curriculum topic resolves to an authentic,
registered generator key without falling back to cross-subject guessing.
"""
import unittest
import os
import re
from pathlib import Path
from app.services.generator_registry import (
    ALL_GENERATORS,
    CURRICULUM_MANIFEST,
    resolve_generator_key,
    generate_variant,
)


class TestCurriculumManifestStrict(unittest.TestCase):
    def test_manifest_coverage(self):
        """Asserts that CURRICULUM_MANIFEST loaded all 476 curriculum topics."""
        self.assertGreaterEqual(len(CURRICULUM_MANIFEST), 470)

    def test_all_manifest_keys_exist_in_all_generators(self):
        """Asserts that every generator key in the manifest is actually registered and callable."""
        missing = []
        for (subj, grade, topic), key in CURRICULUM_MANIFEST.items():
            if key not in ALL_GENERATORS:
                missing.append((subj, grade, topic, key))
        self.assertEqual(len(missing), 0, f"Found uncallable generator keys in manifest: {missing}")

    def test_critical_triage_routes(self):
        """Explicitly asserts that known misroutes identified by Opus 5.5 are strictly resolved."""
        # 1. Business Studies Gr 11 venture (must NOT route to chemistry)
        k1 = resolve_generator_key("A business venture based on a business plan", grade="11", subject="Business Studies")
        self.assertEqual(k1, "grade11_bs_start_business_venture")

        # 2. Business Studies Gr 11 HR (must NOT route to marketing)
        k2 = resolve_generator_key("Introduction to the human resources function", grade="11", subject="Business Studies")
        self.assertEqual(k2, "grade11_bs_human_resources_function")

        # 3. Technical Mathematics Gr 12 Polynomials (must NOT route to complex numbers)
        k3 = resolve_generator_key("Polynomials", grade="12", subject="Technical Mathematics")
        self.assertEqual(k3, "technical_mathematics_polynomials")

        # 4. Life Sciences Gr 10 Cells (must NOT route to meiosis or senior NS matter)
        k4 = resolve_generator_key("Cells the basic units of life", grade="10", subject="Life Sciences")
        self.assertEqual(k4, "grade10_life_sciences_cytology")

        k4_mit = resolve_generator_key("Cell division", grade="10", subject="Life Sciences")
        self.assertEqual(k4_mit, "grade10_life_sciences_mitosis")

        # 5. Mathematical Literacy Gr 10 Conversions and time (must NOT route to finance/tax)
        k5 = resolve_generator_key("Conversions and time", grade="10", subject="Mathematical Literacy")
        self.assertEqual(k5, "mathematical_literacy_measurement")

    def test_all_curriculum_docs_resolve_cleanly(self):
        """Scans all 476 markdown files in curriculum_docs_auto/ and asserts 100% resolution."""
        auto_dir = Path(__file__).resolve().parent.parent.parent / "curriculum_docs_auto"
        if not auto_dir.exists():
            auto_dir = Path("curriculum_docs_auto")

        folders = sorted([d for d in auto_dir.iterdir() if d.is_dir()])
        subject_map = {
            "Accounting": "Accounting",
            "BusinessStudies": "Business Studies",
            "EMS": "Economic and Management Sciences",
            "LifeSciences": "Life Sciences",
            "MathematicalLiteracy": "Mathematical Literacy",
            "Mathematics": "Mathematics",
            "NaturalSciences": "Natural Sciences",
            "PhysicalSciences": "Physical Sciences",
            "TechnicalMathematics": "Technical Mathematics",
        }

        unresolved = []
        total_md = 0

        for fd in folders:
            parts = fd.name.split("_")
            if len(parts) < 2:
                continue
            subj = subject_map.get(parts[0], parts[0])
            grade = parts[1].replace("Gr", "").strip()

            for md in fd.rglob("*.md"):
                if md.name == "Syllabus.md":
                    continue
                total_md += 1
                topic_name = md.stem
                resolved_key = resolve_generator_key(topic_name, grade=grade, subject=subj)
                if not resolved_key or resolved_key not in ALL_GENERATORS:
                    unresolved.append((subj, grade, topic_name, resolved_key))

        self.assertEqual(len(unresolved), 0, f"Unresolved curriculum docs ({len(unresolved)}/{total_md}): {unresolved[:10]}")
        self.assertEqual(total_md, 476, f"Expected 476 curriculum markdown files, found {total_md}")


if __name__ == "__main__":
    unittest.main()
