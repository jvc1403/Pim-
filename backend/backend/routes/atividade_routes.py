from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_database
from models.atividade_model import Atividade
from typing import List
from pydantic import BaseModel
from datetime import datetime

class AtividadeResponse(BaseModel):
    id: str
    titulo: str
    descricao: str = None
    aula_id: str
    tipo: str
    pontuacao_maxima: float = None
    prazo: datetime = None
    created_at: datetime = None
    updated_at: datetime = None

router = APIRouter()

@router.get("/", response_model=List[AtividadeResponse])
async def get_atividades(db=Depends(get_database)):
    atividades = await db.atividades.find().to_list(1000)
    return atividades

@router.post("/", response_model=AtividadeResponse)
async def create_atividade(atividade: AtividadeResponse, db=Depends(get_database)):
    result = await db.atividades.insert_one(atividade.dict())
    atividade.id = str(result.inserted_id)
    return atividade

@router.get("/{atividade_id}", response_model=AtividadeResponse)
async def get_atividade(atividade_id: str, db=Depends(get_database)):
    atividade = await db.atividades.find_one({"_id": atividade_id})
    if not atividade:
        raise HTTPException(status_code=404, detail="Atividade not found")
    return atividade

@router.put("/{atividade_id}", response_model=AtividadeResponse)
async def update_atividade(atividade_id: str, atividade: AtividadeResponse, db=Depends(get_database)):
    result = await db.atividades.update_one({"_id": atividade_id}, {"$set": atividade.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Atividade not found")
    return atividade

@router.delete("/{atividade_id}")
async def delete_atividade(atividade_id: str, db=Depends(get_database)):
    result = await db.atividades.delete_one({"_id": atividade_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Atividade not found")
    return {"message": "Atividade deleted"}
