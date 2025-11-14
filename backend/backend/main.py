from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler

from core.config import settings, close_client
from core.limiter import limiter

from routes import (
    auth_routes, turma_routes, aula_routes, atividade_routes,
    nota_routes, presenca_routes, ia_routes, relatorio_routes
)

app = FastAPI(title="Sistema Acadêmico com IA", version="2.0")

# Configuração do Rate Limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclusão das rotas
app.include_router(auth_routes.router, prefix="/api/auth", tags=["Auth"])
app.include_router(turma_routes.router, prefix="/api/turmas", tags=["Turmas"])
app.include_router(aula_routes.router, prefix="/api/aulas", tags=["Aulas"])
app.include_router(atividade_routes.router, prefix="/api/atividades", tags=["Atividades"])
app.include_router(nota_routes.router, prefix="/api/notas", tags=["Notas"])
app.include_router(presenca_routes.router, prefix="/api/presencas", tags=["Presenças"])
app.include_router(ia_routes.router, prefix="/api/ia", tags=["IA"])
app.include_router(relatorio_routes.router, prefix="/api/relatorios", tags=["Relatórios"])

@app.on_event("shutdown")
async def shutdown():
    await close_client()

@app.get("/")
async def root():
    return {"message": "🚀 API do Sistema Acadêmico com IA ativa!"}
