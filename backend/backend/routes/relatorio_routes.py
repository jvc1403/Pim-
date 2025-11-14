from fastapi import APIRouter, Depends, HTTPException
from core.pdf_utils import generate_pdf_report
from typing import Dict, Any

router = APIRouter()

@router.get("/gerar", response_model=Dict[str, Any])
async def generate_report():
    try:
        report = generate_pdf_report()
        return {"message": "Relatório gerado com sucesso", "report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
