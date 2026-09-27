#!/usr/bin/env python3
"""
AST Purity Linter for Fundile Question Generators
Ensures 100% deterministic Python execution and zero LLM/network dependencies in generator modules.
"""

import ast
import os
import sys
from pathlib import Path

# Force utf-8 encoding on standard streams if supported
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

FORBIDDEN_IMPORTS = {
    # LLM SDKs and Orchestration
    "openai",
    "google.generativeai",
    "google.ai",
    "groq",
    "anthropic",
    "langchain",
    "langchain_core",
    "langchain_google_genai",
    "langchain_community",
    "transformers",
    "huggingface_hub",
    "app.services.llm_provider",
    "llm_provider",
    
    # Network HTTP clients (generators must be offline/deterministic)
    "requests",
    "urllib.request",
    "httpx",
    "aiohttp",
    "socket",
}

FORBIDDEN_MODULE_PREFIXES = (
    "openai",
    "groq",
    "anthropic",
    "langchain",
    "google.generativeai",
)

class GeneratorPurityVisitor(ast.NodeVisitor):
    def __init__(self, filename: str):
        self.filename = filename
        self.violations = []

    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            name = alias.name
            if name in FORBIDDEN_IMPORTS or any(name.startswith(p) for p in FORBIDDEN_MODULE_PREFIXES):
                self.violations.append(
                    f"{self.filename}:{node.lineno} - Forbidden import '{name}': Generators must be 100% deterministic zero-LLM code."
                )
        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        mod = node.module or ""
        if mod in FORBIDDEN_IMPORTS or any(mod.startswith(p) for p in FORBIDDEN_MODULE_PREFIXES):
            self.violations.append(
                f"{self.filename}:{node.lineno} - Forbidden from-import from '{mod}': Generators must be 100% deterministic zero-LLM code."
            )
        self.generic_visit(node)


def scan_directory(target_dir: Path) -> list[str]:
    all_violations = []
    
    if not target_dir.exists():
        return all_violations

    for root, _, files in os.walk(target_dir):
        # Exclude tests, __pycache__, and venvs
        if any(ignored in root for ignored in ["__pycache__", "venv", ".venv", "tests"]):
            continue
            
        for file in files:
            if file.endswith("_generator.py") or "generators" in root or file.startswith("generator"):
                filepath = Path(root) / file
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        tree = ast.parse(f.read(), filename=str(filepath))
                    visitor = GeneratorPurityVisitor(str(filepath))
                    visitor.visit(tree)
                    all_violations.extend(visitor.violations)
                except SyntaxError as se:
                    all_violations.append(f"{filepath}:{se.lineno} - Syntax Error during AST parse: {se}")
                except Exception as e:
                    all_violations.append(f"{filepath} - Parse Error: {e}")

    return all_violations


def main():
    backend_root = Path(__file__).resolve().parent.parent
    utils_dir = backend_root / "app" / "utils"
    generators_dir = backend_root / "generators"

    print("=" * 70)
    print("[AST LINTER] Running AST Purity Check on Question Generators...")
    print(f"Scanning: {utils_dir} & {generators_dir}")
    print("=" * 70)

    violations = []
    violations.extend(scan_directory(utils_dir))
    if generators_dir.exists():
        violations.extend(scan_directory(generators_dir))

    if violations:
        print(f"\n[FAIL] Found {len(violations)} purity violation(s):")
        for v in violations:
            print(f"  * {v}")
        sys.exit(1)
    else:
        print("\n[PASS] 100% AST Purity. All generator modules are deterministic and zero-LLM.")
        sys.exit(0)


if __name__ == "__main__":
    main()
