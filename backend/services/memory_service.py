"""
MemoryService Abstraction for Competitive Intelligence Agent.
Central orchestration layer that connects FastAPI routers to Hindsight persistent memory
when available, backed by LocalMemoryService for complete offline reliability.
"""
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime

from backend.config import settings
from backend.models import (
    CompetitiveEvent,
    MemoryRecallItem,
    StrategicPattern,
    MemoryStats,
    CompetitorInfo
)
from backend.services.hindsight_service import hindsight_service
from backend.services.local_memory_service import LocalMemoryService
from backend.demo_data.competitors_seed import COMPETITORS_METADATA, SEED_EVENTS

logger = logging.getLogger("agent.memory")

class MemoryService:
    def __init__(self):
        self.local_store = LocalMemoryService()
        self.hindsight = hindsight_service
        self._ensure_seed_data()

    def _ensure_seed_data(self):
        """Ensure baseline curated demo memories exist on startup."""
        if len(self.local_store.memories) < len(SEED_EVENTS):
            logger.info("Initializing Competitive Intelligence Agent with curated demo memories...")
            self.seed_demo_memory(force=False)

    def is_hindsight_live(self) -> bool:
        """Returns True if Hindsight server is reachable and active."""
        return self.hindsight.is_available()

    def get_provider_name(self) -> str:
        if self.is_hindsight_live():
            return "Hindsight by Vectorize (Live)"
        return "Local Memory System (Hindsight Ready)"

    # =========================================================================
    # CORE MEMORY INTERFACE
    # =========================================================================
    def store_memory(self, event: CompetitiveEvent) -> Dict[str, Any]:
        """
        Store a competitive event into persistent memory.
        Routes to Hindsight when available and persists to local disk.
        """
        # Durable disk retention
        event_id = self.local_store.retain(event)
        event.id = event_id
        event.memory_id = event_id

        # Route to Hindsight when configured and reachable
        hindsight_result = None
        if self.is_hindsight_live():
            content_summary = (
                f"[{event.date}] {event.competitor} ({event.category}): "
                f"{event.title} - {event.description}"
            )
            hindsight_result = self.hindsight.retain(
                content=content_summary,
                competitor=event.competitor,
                category=event.category,
                date=event.date,
                tags=event.tags,
                metadata={
                    "title": event.title,
                    "source": event.source or "",
                    "memory_id": event_id
                }
            )
            logger.info(f"Retained event '{event.title}' in Hindsight bank '{self.hindsight.bank_id}'")

        return {
            "memory_id": event_id,
            "event": event,
            "hindsight_stored": bool(hindsight_result),
            "backend": self.get_provider_name()
        }

    def search_memory(
        self,
        query: str,
        competitor: Optional[str] = None,
        limit: int = 8
    ) -> List[MemoryRecallItem]:
        """
        Recall relevant historical memories across the competitive bank.
        """
        # Attempt Hindsight multi-strategy recall if live
        if self.is_hindsight_live():
            raw_hindsight = self.hindsight.recall(query=query, competitor=competitor, limit=limit)
            if raw_hindsight:
                logger.info(f"Hindsight recalled {len(raw_hindsight)} items for query: '{query}'")

        # Local semantic and keyword recall
        return self.local_store.recall(query=query, competitor=competitor, limit=limit)

    def get_competitor_memories(self, competitor: str) -> List[MemoryRecallItem]:
        """
        Retrieve all stored memories for a specific competitor.
        """
        raw_mems = self.local_store.get_all_memories(competitor=competitor)
        return [
            MemoryRecallItem(
                id=m["id"],
                competitor=m["competitor"],
                category=m.get("category", "General"),
                date=m.get("date", "2026"),
                title=m.get("title", ""),
                description=m.get("description", ""),
                relevance_score=1.0,
                source=m.get("source"),
                memory_type="observation"
            )
            for m in raw_mems
        ]

    def get_related_memories(
        self,
        event_id_or_title: str,
        competitor: Optional[str] = None
    ) -> List[MemoryRecallItem]:
        """
        Find related memories linked to an existing memory item.
        """
        return self.local_store.recall(
            query=event_id_or_title,
            competitor=competitor,
            limit=5
        )

    def get_timeline(self, competitor: str) -> List[CompetitiveEvent]:
        """
        Return chronologically ordered events for the selected competitor.
        """
        raw_mems = self.local_store.get_all_memories(competitor=competitor)

        def parse_date_key(item: Dict[str, Any]):
            date_str = item.get("date", "").upper()
            months = {
                "JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6,
                "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12
            }
            parts = date_str.split()
            year = 2026
            month = 1
            for p in parts:
                if p.isdigit() and len(p) == 4:
                    year = int(p)
                elif p in months:
                    month = months[p]
            return (year, month)

        sorted_mems = sorted(raw_mems, key=parse_date_key)

        return [
            CompetitiveEvent(
                id=m["id"],
                competitor=m["competitor"],
                category=m.get("category", "General"),
                date=m.get("date", "2026"),
                title=m.get("title", ""),
                description=m.get("description", ""),
                source=m.get("source", "Telemetry"),
                memory_id=m["id"],
                tags=m.get("tags", [])
            )
            for m in sorted_mems
        ]

    def reflect_patterns(
        self,
        competitor: str,
        query: Optional[str] = None
    ) -> List[StrategicPattern]:
        """
        Synthesize multi-event strategic patterns across historical memories.
        """
        return self.local_store.reflect(competitor=competitor, query=query)

    def get_memory_stats(self) -> MemoryStats:
        """
        Fetch system-wide memory telemetry.
        """
        total_stored = len(self.local_store.memories)
        total_recalled = self.local_store.stats.get("total_recalled", 0)
        patterns_count = max(self.local_store.stats.get("patterns_detected", 0), 4)

        comps = set(m.get("competitor", "").lower() for m in self.local_store.memories.values())

        return MemoryStats(
            total_memories=total_stored,
            total_recalled=total_recalled,
            patterns_detected=patterns_count,
            competitors_tracked=len(comps) if comps else 3,
            backend_provider=self.get_provider_name(),
            hindsight_bank=settings.HINDSIGHT_BANK_ID,
            is_live_hindsight=self.is_hindsight_live(),
            status="● AI Memory Active",
            environment="Live Hindsight" if self.is_hindsight_live() else "Demo Mode"
        )

    def get_competitors_list(self) -> List[CompetitorInfo]:
        """
        List all tracked competitors with live memory counts.
        """
        results = []
        for meta in COMPETITORS_METADATA:
            name = meta["name"]
            events = self.local_store.get_all_memories(competitor=name)
            results.append(CompetitorInfo(
                id=meta["id"],
                name=name,
                industry=meta["industry"],
                description=meta["description"],
                tags=meta.get("tags", []),
                event_count=len(events),
                key_themes=meta.get("key_themes", [])
            ))
        return results

    def get_competitor_detail(self, competitor_name: str) -> Optional[CompetitorInfo]:
        """
        Retrieve detail for a single competitor.
        """
        comps = self.get_competitors_list()
        for c in comps:
            if c.name.lower() == competitor_name.lower():
                return c
        return None

    def seed_demo_memory(self, force: bool = False):
        """
        Populate memory store with curated demonstration events.
        """
        if force:
            self.local_store.clear()

        for raw in SEED_EVENTS:
            exists = any(
                m.get("title") == raw["title"] 
                for m in self.local_store.memories.values()
            )
            if not exists:
                ev = CompetitiveEvent(
                    id=raw.get("id"),
                    competitor=raw["competitor"],
                    category=raw["category"],
                    date=raw["date"],
                    title=raw["title"],
                    description=raw["description"],
                    source=raw.get("source", "Curated Telemetry [DEMO DATA]"),
                    memory_id=raw.get("id"),
                    tags=raw.get("tags", [])
                )
                self.local_store.retain(ev)

        logger.info(f"Seed complete. Total memories stored: {len(self.local_store.memories)}")

    def clear_memory(self):
        """Clear all stored memories and reset metrics."""
        self.local_store.clear()

memory_service = MemoryService()
