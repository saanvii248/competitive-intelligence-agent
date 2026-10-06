"""
Competitive Intelligence Agent
Main FastAPI Application Entrypoint.
"""
import logging
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from backend.config import settings
from backend.models import HealthResponse
from backend.services.memory_service import memory_service
from backend.services.ai_service import ai_service
from backend.api import (
    competitors_router,
    ask_router,
    memory_router,
    demo_router
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("agent.main")

app = FastAPI(
    title=settings.APP_NAME,
    description="An AI agent that remembers competitor moves and uncovers strategic patterns using persistent long-term memory (Hindsight by Vectorize).",
    version="1.0.0"
)

# CORS middleware for cross-origin local testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(competitors_router)
app.include_router(ask_router)
app.include_router(memory_router)
app.include_router(demo_router)

@app.get("/api/health", response_model=HealthResponse, tags=["health"])
def health_check():
    """Health check endpoint indicating memory layer and AI engine status."""
    stats = memory_service.get_memory_stats()
    return HealthResponse(
        status="healthy",
        app=settings.APP_NAME,
        subtitle=settings.APP_SUBTITLE,
        version="1.0.0",
        hindsight_status="Connected (Live)" if memory_service.is_hindsight_live() else "Local Fallback (Hindsight Ready)",
        llm_status=ai_service.get_provider_status(),
        environment="Live Hindsight" if memory_service.is_hindsight_live() else "Demo Mode",
        total_memories=stats.total_memories
    )

# Static files & single-page application delivery
FRONTEND_PATH = Path(__file__).resolve().parent.parent / "frontend"

if FRONTEND_PATH.exists():
    app.mount("/static", StaticFiles(directory=str(FRONTEND_PATH)), name="static")

    @app.get("/", include_in_schema=False)
    async def serve_index():
        return FileResponse(str(FRONTEND_PATH / "index.html"))

@app.on_event("startup")
async def on_startup():
    logger.info("=" * 65)
    logger.info(f"🎯 {settings.APP_NAME} Initialized")
    logger.info(f"Subtitle: '{settings.APP_SUBTITLE}'")
    logger.info(f"Memory Layer: {memory_service.get_provider_name()}")
    logger.info(f"AI Reasoning Engine: {ai_service.get_provider_status()}")
    logger.info(f"Memories Loaded: {len(memory_service.local_store.memories)}")
    logger.info("=" * 65)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host=settings.HOST, port=settings.PORT, reload=True)
