"""FastAPI Endpoint for Unified Question Generation: POST /api/generate
Connects client requests (practice, assessment, mock exams) to deterministic generators.
Adheres to Systems Security rules: CPU offloading to worker threads with 2.5s timeout.
"""
from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Optional
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field

from app.services.generator_registry import generate_variant, resolve_generator_key

router = APIRouter(tags=["Question Generation"])


class GenerateRequest(BaseModel):
    subject: str = Field(default="Mathematics", description="Subject name e.g. Mathematics, Accounting, Business Studies")
    grade: str = Field(default="10", description="Grade string 7 through 12")
    topic: str = Field(..., description="Topic name, slug, or slice alias")
    subskill: Optional[str] = Field(default="mixed", description="Target subskill parameter")
    difficulty: Optional[str] = Field(default="medium", description="easy | medium | hard")
    mode: Optional[str] = Field(default="compound", description="compound | elementary_<subskill>")
    seed: Optional[int] = Field(default=None, description="Deterministic integer seed")
    count: Optional[int] = Field(default=1, ge=1, le=50, description="Number of questions to generate")
    exam_type: Optional[str] = Field(default=None, description="topic | term | mock")
    paper: Optional[int] = Field(default=1, description="Paper 1 or Paper 2 for mock exams")
    term: Optional[int] = Field(default=1, ge=1, le=4, description="CAPS school calendar term (1..4)")


class GenerateResponse(BaseModel):
    success: bool
    questions: List[Dict[str, Any]]
    metadata: Dict[str, Any]


@router.post("/generate", response_model=GenerateResponse)
@router.post("/api/generate", response_model=GenerateResponse)
async def generate_questions(req: GenerateRequest):
    """Generates seeded questions deterministically using the 6-pillar generator registry."""
    extra_config = {
        "mode": req.mode,
        "exam_type": req.exam_type,
        "paper": req.paper,
        "term": req.term,
    }

    try:
        # Offload CPU-bound SymPy calculations to a worker thread with 2.5s hard timeout
        # (systems_security_architect rule to prevent event loop blocking)
        questions = await asyncio.wait_for(
            asyncio.to_thread(
                generate_variant,
                topic=req.topic,
                subskill=req.subskill or "mixed",
                difficulty=req.difficulty or "medium",
                count=req.count or 1,
                seed=req.seed,
                grade=req.grade,
                subject=req.subject,
                extra_config=extra_config,
            ),
            timeout=2.5,
        )

        return GenerateResponse(
            success=True,
            questions=questions,
            metadata={
                "subject": req.subject,
                "grade": req.grade,
                "topic": req.topic,
                "resolved_key": resolve_generator_key(req.topic, grade=req.grade, subject=req.subject),
                "seed": req.seed,
                "total_questions": len(questions),
            }
        )

    except asyncio.TimeoutError:
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Question generation computation exceeded 2.5s timeout",
        )
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal generator error: {str(e)}",
        )
