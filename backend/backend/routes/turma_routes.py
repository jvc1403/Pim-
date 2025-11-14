from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_database
from models.turma_model import Turma
from typing import List
from pydantic import BaseModel

class TurmaResponse(BaseModel):
    id: str
    nome: str
    descricao: str = None
    professor_id: str
    created_at: str = None
    updated_at: str = None

router = APIRouter()

@router.get("/", response_model=List[TurmaResponse])
async def get_turmas(db=Depends(get_database)):
    turmas = await db.turmas.find().to_list(1000)
    return turmas

@router.post("/", response_model=TurmaResponse)
async def create_turma(turma: TurmaResponse, db=Depends(get_database)):
    result = await db.turmas.insert_one(turma.dict())
    turma.id = str(result.inserted_id)
    return turma

@router.get("/{turma_id}", response_model=TurmaResponse)
async def get_turma(turma_id: str, db=Depends(get_database)):
    turma = await db.turmas.find_one({"_id": turma_id})
    if not turma:
        raise HTTPException(status_code=404, detail="Turma not found")
    return turma

@router.put("/{turma_id}", response_model=TurmaResponse)
async def update_turma(turma_id: str, turma: TurmaResponse, db=Depends(get_database)):
    result = await db.turmas.update_one({"_id": turma_id}, {"$set": turma.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Turma not found")
    return turma

@router.delete("/{turma_id}")
async def delete_turma(turma_id: str, db=Depends(get_database)):
    result = await db.turmas.delete_one({"_id": turma_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Turma not found")
    return {"message": "Turma deleted"}
