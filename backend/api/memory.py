from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query
from backend.models import (
    IngestRequest,
    IngestResponse,
    CompetitiveEvent,
    MemoryStats,
    MemoryRecallItem
)
from backend.services.memory_service import memory_service

router = APIRouter(prefix="/api/memory", tags=["memory"])

@router.post("/ingest", response_model=IngestResponse)
def ingest_event(req: IngestRequest):
    """
    Ingest a new competitive event into persistent memory.
    """
    if not req.title.strip() or not req.description.strip():
        raise HTTPException(status_code=400, detail="Title and description cannot be empty.")

    event = CompetitiveEvent(
        competitor=req.competitor.strip(),
        category=req.category.strip(),
        date=req.date.strip(),
        title=req.title.strip(),
        description=req.description.strip(),
        source=req.source.strip() if req.source else "Manual Ingestion",
        tags=[req.competitor.lower(), req.category.lower()]
    )

    result = memory_service.store_memory(event)
    stats = memory_service.get_memory_stats()

    return IngestResponse(
        success=True,
        message="Memory stored successfully.",
        memory_id=result["memory_id"],
        event=result["event"],
        total_memories=stats.total_memories,
        backend=result["backend"]
    )

@router.get("/stats", response_model=MemoryStats)
def get_memory_stats():
    """Get system-wide memory telemetry."""
    return memory_service.get_memory_stats()

@router.get("/search", response_model=List[MemoryRecallItem])
def search_memories(
    query: str = Query(..., description="Search query across competitive memories"),
    competitor: Optional[str] = Query(None, description="Optional competitor filter"),
    limit: int = Query(8, ge=1, le=50)
):
    """Search and recall relevant competitive memories."""
    return memory_service.search_memory(query=query, competitor=competitor, limit=limit)
