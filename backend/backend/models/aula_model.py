from sqlalchemy import Column, String, DateTime, Integer, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Aula(Base):
    __tablename__ = "aulas"

    id = Column(String, primary_key=True, index=True)
    titulo = Column(String)
    descricao = Column(String, nullable=True)
    turma_id = Column(String, ForeignKey("turmas.id"))
    data = Column(DateTime)
    duracao = Column(Integer, nullable=True)  # em minutos
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    turma = relationship("Turma", back_populates="aulas")
    atividades = relationship("Atividade", back_populates="aula")
    presencas = relationship("Presenca", back_populates="aula")
