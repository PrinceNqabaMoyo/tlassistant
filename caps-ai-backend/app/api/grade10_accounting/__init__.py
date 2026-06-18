from fastapi import APIRouter
from .marker import router as marker_router

router = APIRouter()
router.include_router(marker_router, prefix="/mark", tags=["Grade 10 Accounting Marking"])
