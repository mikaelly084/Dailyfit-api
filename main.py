from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from database import Base, engine

from routes.pagina import router as pagina_router
from routes.usuarios import router as usuarios_router
from routes.refeicoes import router as refeicoes_router
from routes.resumo import router as resumo_router



# Cria as tabelas do banco
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Daily Diet API",
    description="API para controle de usuários e refeições",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Registra as rotas
app.include_router(pagina_router)
app.include_router(usuarios_router)
app.include_router(refeicoes_router)
app.include_router(resumo_router)