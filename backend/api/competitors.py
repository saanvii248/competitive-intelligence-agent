from typing import List
from fastapi import APIRouter, HTTPException
from backend.models import CompetitorInfo, CompetitiveEvent
from backend.services.memory_service import memory_service

router = APIRouter(prefix="/api/competitors", tags=["competitors"])

@router.get("", response_model=List[CompetitorInfo])
def get_all_competitors():
    """List all tracked competitors with live memory counts."""
    return memory_service.get_competitors_list()

@router.get("/{competitor}", response_model=CompetitorInfo)
def get_competitor(competitor: str):
    """Get metadata for a specific competitor."""
    comp = memory_service.get_competitor_detail(competitor)
    if not comp:
        raise HTTPException(status_code=404, detail=f"Competitor '{competitor}' not found")
    return comp

@router.get("/{competitor}/timeline", response_model=List[CompetitiveEvent])
def get_competitor_timeline(competitor: str):
    """Retrieve chronologically ordered events stored in persistent memory for a competitor."""
    events = memory_service.get_timeline(competitor)
    if not events:
        # Check if competitor exists in metadata
        comp = memory_service.get_competitor_detail(competitor)
        if not comp:
            raise HTTPException(status_code=404, detail=f"Competitor '{competitor}' not found")
    return events
