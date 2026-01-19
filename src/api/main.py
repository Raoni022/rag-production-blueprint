from fastapi import FastAPI
from src.api.routes import router as api_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="RAG Production Blueprint",
        version="0.1.0",
        description="RAG MVP com foco em produção (qualidade, custo, rastreabilidade)"
    )

    # Rotas
    app.include_router(api_router, prefix="/api")

    # Healthcheck (boa prática)
    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()
