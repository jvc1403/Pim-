from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_database
from models.presenca_model import Presenca
from typing import List
from pydantic import BaseModel
from datetime import datetime

class PresencaResponse(BaseModel):
    id: str
    aluno_id: str
    aula_id: str
    presente: bool
    data: datetime
    comentario: str = None
    created_at: datetime = None
    updated_at: datetime = None

router = APIRouter()

@router.get("/", response_model=List[PresencaResponse])
async def get_presencas(db=Depends(get_database)):
    presencas = await db.presencas.find().to_list(1000)
    return presencas

@router.post("/", response_model=PresencaResponse)
async def create_presenca(presenca: PresencaResponse, db=Depends(get_database)):
    result = await db.presencas.insert_one(presenca.dict())
    presenca.id = str(result.inserted_id)
    return presenca

@router.get("/{presenca_id}", response_model=PresencaResponse)
async def get_presenca(presenca_id: str, db=Depends(get_database)):
    presenca = await db.presencas.find_one({"_id": presenca_id})
    if not presenca:
        raise HTTPException(status_code=404, detail="Presenca not found")
    return presenca

@router.put("/{presenca_id}", response_model=PresencaResponse)
async def update_presenca(presenca_id: str, presenca: PresencaResponse, db=Depends(get_database)):
    result = await db.presencas.update_one({"_id": presenca_id}, {"$set": presenca.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Presenca not found")
    return presenca

@router.delete("/{presenca_id}")
async def delete_presenca(presenca_id: str, db=Depends(get_database)):
    result = await db.presencas.delete_one({"_id": presenca_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Presenca not found")
    return {"message": "Presenca deleted"}
