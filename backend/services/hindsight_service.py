"""
Hindsight by Vectorize Integration Layer.
Handles communication with Hindsight persistent memory service (Cloud or Docker).
Provides graceful fallback detection if Hindsight is not running.
"""
import logging
import httpx
from typing import List, Dict, Any, Optional
from backend.config import settings

logger = logging.getLogger("agent.hindsight")

class HindsightService:
    def __init__(self):
        self.base_url = settings.HINDSIGHT_BASE_URL.rstrip("/")
        self.api_key = settings.HINDSIGHT_API_KEY
        self.bank_id = settings.HINDSIGHT_BANK_ID
        self._last_check_time = 0
        self._cached_available = False

    def is_available(self) -> bool:
        """
        Check if the Hindsight API server is reachable.
        Cached with 20-second TTL to avoid redundant network roundtrips.
        """
        if settings.FORCE_LOCAL_MEMORY:
            return False

        import time
        now = time.time()
        if now - self._last_check_time < 20.0:
            return self._cached_available

        self._last_check_time = now

        try:
            headers = {}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            # Quick ping to Hindsight health or config endpoint with a 300ms timeout
            with httpx.Client(timeout=0.3) as client:
                res = client.get(f"{self.base_url}/health", headers=headers)
                self._cached_available = (res.status_code < 500)
                return self._cached_available
        except Exception:
            self._cached_available = False
            return False

    def retain(
        self,
        content: str,
        competitor: str,
        category: str,
        date: str,
        metadata: Optional[Dict[str, Any]] = None,
        tags: Optional[List[str]] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Retain competitive event into Hindsight memory bank.
        """
        if not self.is_available():
            return None

        try:
            url = f"{self.base_url}/v1/default/banks/{self.bank_id}/retain"
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            all_tags = [competitor.lower(), category.lower()]
            if tags:
                all_tags.extend(tags)

            meta = {
                "competitor": competitor,
                "category": category,
                "event_date": date
            }
            if metadata:
                meta.update(metadata)

            payload = {
                "content": content,
                "metadata": meta,
                "tags": all_tags,
                "context": f"Competitive Intelligence observation for {competitor}"
            }

            with httpx.Client(timeout=4.0) as client:
                res = client.post(url, json=payload, headers=headers)
                if res.status_code in (200, 201):
                    return res.json()
                logger.warning(f"Hindsight retain returned status {res.status_code}: {res.text}")
                return None
        except Exception as e:
            logger.error(f"Hindsight retain exception: {e}")
            return None

    def recall(
        self,
        query: str,
        competitor: Optional[str] = None,
        limit: int = 8
    ) -> Optional[List[Dict[str, Any]]]:
        """
        Recall relevant memories from Hindsight bank using multi-strategy search.
        """
        if not self.is_available():
            return None

        try:
            url = f"{self.base_url}/v1/default/banks/{self.bank_id}/recall"
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            tags = [competitor.lower()] if competitor else []
            payload = {
                "query": query,
                "tags": tags,
                "budget": "mid",
                "limit": limit
            }

            with httpx.Client(timeout=4.0) as client:
                res = client.post(url, json=payload, headers=headers)
                if res.status_code == 200:
                    data = res.json()
                    results = data.get("results", [])
                    memories = []
                    for item in results:
                        memories.append({
                            "id": item.get("id", "hindsight-mem"),
                            "content": item.get("text", item.get("content", "")),
                            "score": item.get("score", 0.9),
                            "metadata": item.get("metadata", {})
                        })
                    return memories
                return None
        except Exception as e:
            logger.error(f"Hindsight recall exception: {e}")
            return None

    def reflect(
        self,
        query: str,
        competitor: Optional[str] = None
    ) -> Optional[Dict[str, Any]]:
        """
        Reflect across memories to synthesize higher-level strategic patterns.
        """
        if not self.is_available():
            return None

        try:
            url = f"{self.base_url}/v1/default/banks/{self.bank_id}/reflect"
            headers = {"Content-Type": "application/json"}
            if self.api_key:
                headers["Authorization"] = f"Bearer {self.api_key}"

            payload = {
                "query": f"Analyze competitive trajectory and strategic shifts for {competitor or 'all competitors'}: {query}",
                "tags": [competitor.lower()] if competitor else []
            }

            with httpx.Client(timeout=5.0) as client:
                res = client.post(url, json=payload, headers=headers)
                if res.status_code == 200:
                    return res.json()
                return None
        except Exception as e:
            logger.error(f"Hindsight reflect exception: {e}")
            return None

hindsight_service = HindsightService()
