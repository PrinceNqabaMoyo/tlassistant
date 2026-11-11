"""FastAPI Endpoint for Reference Atlas & Study Viewer: GET /api/diagram_study/{master}
Enforces Rule 0d-14 and GP-25:
- Structure names exist ONLY in the study viewer / reference atlas.
- Question payloads emitted by /api/generate contain ONLY opaque pins, NEVER structure names.
- This endpoint serves authentic scientific names when the learner explicitly opens the Reference Atlas or Study Viewer.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List, Optional
from fastapi import APIRouter, HTTPException, Query, status
from pydantic import BaseModel

router = APIRouter(prefix="/api/diagram_study", tags=["Diagram Study & Reference Atlas"])

DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "diagram_anchors"


class DiagramStudyResponse(BaseModel):
    success: bool
    master: str
    view: str
    viewBox: str
    labels: List[Dict[str, Any]]
    metadata: Dict[str, Any]


@router.get("/{master}", response_model=DiagramStudyResponse)
async def get_diagram_study_plate(
    master: str,
    grade: Optional[str] = Query(default="g8", description="Target grade scope filter e.g. g8, g10"),
    view: Optional[str] = Query(default="textbook", description="textbook | exam | schematic"),
):
    """Returns authoritative anatomical/scientific structure names and callout anchors for the Study Viewer."""
    # Normalize master name
    normalized_master = master.lower().replace("-", "_")
    anchor_file = DATA_DIR / f"{normalized_master}.json"

    if not anchor_file.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Diagram master '{master}' not found in authoritative diagram anchors.",
        )

    try:
        data = json.loads(anchor_file.read_text(encoding="utf-8"))
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to read diagram anchor manifest: {str(e)}",
        )

    anchors_raw = data.get("anchors", {})
    labels = []

    grade_key = f"g{grade}" if not grade.startswith("g") else grade

    for k, info in anchors_raw.items():
        allowed_grades = info.get("grades", [])
        # Include if no grade mask specified or if grade matches
        if not allowed_grades or grade_key in allowed_grades or "all" in allowed_grades:
            labels.append({
                "id": k,
                "name": info.get("name", k.replace("_", " ").title()),
                "anchor": info.get("anchor", [300, 240]),
                "default_box": info.get("default_box", [60, 240]),
                "side": info.get("side", "left"),
                "description": info.get("description", ""),
                "synonyms": info.get("synonyms", []),
            })

    return DiagramStudyResponse(
        success=True,
        master=normalized_master,
        view=view or data.get("view", "textbook"),
        viewBox=data.get("viewBox", "0 0 600 480"),
        labels=labels,
        metadata={
            "grade_filter": grade_key,
            "total_structures": len(labels),
            "master_source": str(anchor_file.name),
        }
    )
