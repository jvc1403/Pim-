from sqlalchemy import Column, String, DateTime, Float, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Atividade(Base):
    __tablename__ = "atividades"

    id = Column(String, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String, nullable=True)
    aula_id = Column(String, ForeignKey("aulas.id"))
    tipo = Column(String)  # e.g., "exercicio", "prova", "trabalho"
    pontuacao_maxima = Column(Float, nullable=True)
    prazo = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    aula = relationship("Aula", back_populates="atividades")
    notas = relationship("Nota", back_populates="atividade")
