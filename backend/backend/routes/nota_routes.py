from fastapi import APIRouter, Depends, HTTPException
from database.connection import get_database
from models.nota_model import Nota
from typing import List
from pydantic import BaseModel
from datetime import datetime

class NotaResponse(BaseModel):
    id: str
    aluno_id: str
    atividade_id: str
    valor: float
    comentario: str = None
    created_at: datetime = None
    updated_at: datetime = None

router = APIRouter()

@router.get("/", response_model=List[NotaResponse])
async def get_notas(db=Depends(get_database)):
    notas = await db.notas.find().to_list(1000)
    return notas

@router.post("/", response_model=NotaResponse)
async def create_nota(nota: NotaResponse, db=Depends(get_database)):
    result = await db.notas.insert_one(nota.dict())
    nota.id = str(result.inserted_id)
    return nota

@router.get("/{nota_id}", response_model=NotaResponse)
async def get_nota(nota_id: str, db=Depends(get_database)):
    nota = await db.notas.find_one({"_id": nota_id})
    if not nota:
        raise HTTPException(status_code=404, detail="Nota not found")
    return nota

@router.put("/{nota_id}", response_model=NotaResponse)
async def update_nota(nota_id: str, nota: NotaResponse, db=Depends(get_database)):
    result = await db.notas.update_one({"_id": nota_id}, {"$set": nota.dict()})
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Nota not found")
    return nota

@router.delete("/{nota_id}")
async def delete_nota(nota_id: str, db=Depends(get_database)):
    result = await db.notas.delete_one({"_id": nota_id})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Nota not found")
    return {"message": "Nota deleted"}
