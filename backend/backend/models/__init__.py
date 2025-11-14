from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Import all models to ensure they are registered with Base
from .user_model import User
from .turma_model import Turma
from .aula_model import Aula
from .atividade_model import Atividade
from .nota_model import Nota
from .presenca_model import Presenca
