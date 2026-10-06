import logging
from fastapi import APIRouter, HTTPException
from backend.models import AskRequest, AskResponse
from backend.services.memory_service import memory_service
from backend.services.ai_service import ai_service

router = APIRouter(prefix="/api/ask", tags=["ask"])
logger = logging.getLogger("agent.api.ask")

@router.post("", response_model=AskResponse)
def ask_agent(req: AskRequest):
    """
    Query the Competitive Intelligence Agent using persistent memory recall and reasoning.
    """
    question = req.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Question cannot be empty.")

    # Determine competitor from request or question text
    competitor = req.competitor
    if not competitor:
        q_lower = question.lower()
        if "stripe" in q_lower:
            competitor = "Stripe"
        elif "razorpay" in q_lower:
            competitor = "Razorpay"
        elif "paypal" in q_lower:
            competitor = "PayPal"
        else:
            competitor = "Stripe"

    # 1. Contextual memory recall
    recalled_memories = memory_service.search_memory(
        query=question,
        competitor=competitor,
        limit=8
    )

    # 2. Historical patterns reflection
    patterns = memory_service.reflect_patterns(
        competitor=competitor,
        query=question
    )

    # 3. Retrieve chronological timeline
    timeline = memory_service.get_timeline(competitor) if req.include_timeline else []

    # 4. Synthesize strategic analysis
    response = ai_service.answer_question(
        question=question,
        competitor=competitor,
        memories=recalled_memories,
        patterns=patterns,
        timeline=timeline
    )

    return response
