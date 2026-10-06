from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
from datetime import datetime

class CompetitorInfo(BaseModel):
    id: str
    name: str
    industry: str
    description: str
    tags: List[str] = []
    event_count: int = 0
    key_themes: List[str] = []

class CompetitiveEvent(BaseModel):
    id: Optional[str] = None
    competitor: str = Field(..., description="Stripe, Razorpay, PayPal, or custom competitor")
    category: str = Field(..., description="Pricing, Product, Marketing, Partnership, Hiring, Customer Reaction, Strategy, Other")
    date: str = Field(..., description="Formatted date string e.g. JAN 2026 or 2026-01-15")
    title: str = Field(..., description="Headline of the competitive event")
    description: str = Field(..., description="Detailed description of the competitive move")
    source: Optional[str] = Field("Industry Telemetry", description="Source or reference attribution")
    memory_id: Optional[str] = Field(None, description="Hindsight or persistent memory identifier")
    created_at: Optional[datetime] = None
    tags: List[str] = []

class MemoryRecallItem(BaseModel):
    id: str
    competitor: str
    category: str
    date: str
    title: str
    description: str
    relevance_score: float = 1.0
    source: Optional[str] = None
    memory_type: str = "observation"

class StrategicPattern(BaseModel):
    id: str
    competitor: str
    title: str
    description: str
    evidence_points: List[str] = []
    connected_memory_ids: List[str] = []
    move_count: int = 0
    confidence: str = "Medium"
    detected_at: Optional[str] = None

class AskRequest(BaseModel):
    question: str = Field(..., description="Question to ask the Competitive Intelligence Agent")
    competitor: Optional[str] = Field(None, description="Target competitor name (optional)")
    include_timeline: bool = True

class AskResponse(BaseModel):
    answer: str
    competitor: str
    memory_evidence: List[str] = []
    memories: List[MemoryRecallItem] = []
    pattern: str
    why_this_matters: str
    confidence: str = "Medium"
    timeline: List[CompetitiveEvent] = []
    strategic_insights: List[StrategicPattern] = []
    memory_connections: Dict[str, Any] = {}
    backend_mode: str = "Hindsight Persistent Memory (Ready)"

class IngestRequest(BaseModel):
    competitor: str
    category: str
    date: str
    title: str
    description: str
    source: Optional[str] = "Manual Ingestion"

class IngestResponse(BaseModel):
    success: bool
    message: str = "Memory stored successfully."
    memory_id: str
    event: CompetitiveEvent
    total_memories: int
    backend: str

class MemoryStats(BaseModel):
    total_memories: int
    total_recalled: int
    patterns_detected: int
    competitors_tracked: int
    backend_provider: str
    hindsight_bank: str
    is_live_hindsight: bool
    status: str = "● AI Memory Active"
    environment: str = "Demo Mode"

class HealthResponse(BaseModel):
    status: str
    app: str
    subtitle: str
    version: str = "1.0.0"
    hindsight_status: str
    llm_status: str
    environment: str
    total_memories: int
