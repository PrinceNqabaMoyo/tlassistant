"""
Socratic Shield Guardrail
Sanitizes LLM outputs to prevent accidental solution leaking or direct calculation authoring.
Ensures students receive conceptual scaffolding rather than ready-made answers.
"""

import re
from typing import List, Tuple, Dict, Any


class SocraticShield:
    """Regex-driven defense layer redacting target solution values from LLM responses."""

    def __init__(self, forbidden_terms: List[str] = None):
        self.forbidden_terms = forbidden_terms or []

    def sanitize(
        self,
        llm_response: str,
        target_solution_values: List[str],
    ) -> Tuple[str, bool]:
        """
        Scans llm_response for exact or near-exact occurrences of target_solution_values.
        Returns: (sanitized_response, is_redacted)
        """
        if not llm_response or not target_solution_values:
            return llm_response, False

        sanitized = llm_response
        is_redacted = False

        for target in target_solution_values:
            target_str = str(target).strip()
            if not target_str or len(target_str) < 2:
                continue

            # Escape target for regex
            escaped = re.escape(target_str)
            # Match word boundary or currency/symbol boundary
            pattern = rf"(?:\b|R\s*|x\s*=\s*){escaped}(?:\b|\.00)?"

            if re.search(pattern, sanitized, flags=re.IGNORECASE):
                is_redacted = True
                # Replace with Socratic placeholder
                sanitized = re.sub(
                    pattern,
                    "[calculate this value using the step above]",
                    sanitized,
                    flags=re.IGNORECASE
                )

        return sanitized, is_redacted


socratic_shield = SocraticShield()
