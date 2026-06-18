from __future__ import annotations

import importlib.util
from pathlib import Path

_LEGACY_PATH = Path(__file__).resolve().parent.parent / "final_accounts_generator.py"
_LEGACY_SPEC = importlib.util.spec_from_file_location(
    "app.utils.grade10_accounting.term2._legacy_final_accounts_generator",
    _LEGACY_PATH,
)
if _LEGACY_SPEC is None or _LEGACY_SPEC.loader is None:
    raise ImportError("Could not load the legacy Final Accounts generator module.")

_legacy_module = importlib.util.module_from_spec(_LEGACY_SPEC)
_LEGACY_SPEC.loader.exec_module(_legacy_module)

for _name in dir(_legacy_module):
    if _name.startswith("__"):
        continue
    globals()[_name] = getattr(_legacy_module, _name)

__all__ = [name for name in dir(_legacy_module) if not name.startswith("__")]
