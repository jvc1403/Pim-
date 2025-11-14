from fastapi import APIRouter, Depends, HTTPException
from utils.feedback_ai import generate_feedback
from typing import Dict, Any

router = APIRouter()

@router.post("/feedback", response_model=Dict[str, Any])
async def get_ai_feedback(data: Dict[str, Any]):
    try:
        feedback = generate_feedback(data)
        return {"feedback": feedback}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
