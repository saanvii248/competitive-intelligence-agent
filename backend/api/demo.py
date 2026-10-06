from fastapi import APIRouter
from backend.services.memory_service import memory_service
from backend.models import MemoryStats

router = APIRouter(prefix="/api/demo", tags=["demo"])

@router.post("/seed", response_model=MemoryStats)
def seed_demo_data():
    """Populate baseline demonstration events for Stripe, Razorpay, and PayPal."""
    memory_service.seed_demo_memory(force=False)
    return memory_service.get_memory_stats()

@router.post("/reset", response_model=MemoryStats)
def reset_demo_data():
    """Reset all memories and restore initial baseline demo dataset."""
    memory_service.clear_memory()
    memory_service.seed_demo_memory(force=True)
    return memory_service.get_memory_stats()
