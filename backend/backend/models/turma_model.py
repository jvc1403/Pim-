from sqlalchemy import Column, String, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Turma(Base):
    __tablename__ = "turmas"

    id = Column(String, primary_key=True, index=True)
    nome = Column(String)
    descricao = Column(String, nullable=True)
    professor_id = Column(String, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    professor = relationship("User", back_populates="turmas")
    aulas = relationship("Aula", back_populates="turma")
