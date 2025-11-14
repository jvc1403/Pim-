from sqlalchemy import Column, String, Boolean, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Presenca(Base):
    __tablename__ = "presencas"

    id = Column(String, primary_key=True, index=True)
    aluno_id = Column(String, ForeignKey("users.id"))
    aula_id = Column(String, ForeignKey("aulas.id"))
    presente = Column(Boolean)
    data = Column(DateTime)
    comentario = Column(String, nullable=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

    # Relationships
    aluno = relationship("User", back_populates="presencas")
    aula = relationship("Aula", back_populates="presencas")
