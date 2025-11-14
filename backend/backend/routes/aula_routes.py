from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_database
from models.aula_model import Aula
from typing import List
from pydantic import BaseModel
from datetime import datetime

class AulaResponse(BaseModel):
    id: str
    titulo: str
    descricao: str = None
    turma_id: str
    data: datetime
    duracao: int = None
    created_at: datetime = None
    updated_at: datetime = None

router = APIRouter()

@router.get("/", response_model=List[AulaResponse])
async def get_aulas(db=Depends(get_database)):
    aulas = await db.aulas.find().to_list(1000)
    return aulas

@router.post("/", response_model=AulaResponse)
async def create_aula(aula: AulaResponse, db=Depends(get_database)):
    result = await db.aulas.insert_one(aula.dict())
    aula.id = str(result.inserted_id)
    return aula

@router.get("/{aula_id}", response_model=AulaResponse)
async def get_aula(aula_id: str, db=Depends(get_database)):
    aula = await db.aulas.find_one({"_id": aula_id})
    if not aula:
        raise HTTPException(status_code=404, detail="Aula not found")
    return aula

@router.put("/{aula_id}", response_model=AulaResponse)
async def update_aula(aula_id: str, aula: AulaResponse, db=Depends(get_database)):
    result = await db.aulas.update_one({"_id": aula_id}, {"$set": aula.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Aula not found")
    return aula

@router.delete("/{aula_id}")
async def delete_aula(aula_id: str, db=Depends(get_database)):
    result = await db.aulas.delete_one({"_id": aula_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Aula not found")
    return {"message": "Aula deleted"}
