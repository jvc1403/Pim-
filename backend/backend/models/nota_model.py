from sqlalchemy import Column, String, Float, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Nota(Base):
    __tablename__ = "notas"

    id = Column(String, primary_key=True, index=True)
    aluno_id = Column(String, ForeignKey("users.id"))
    atividade_id = Column(String, ForeignKey("atividades.id"))
    valor = Column(Float)
    comentario = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    aluno = relationship("User", back_populates="notas")
    atividade = relationship("Atividade", back_populates="notas")
