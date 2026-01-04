from fastapi import FastAPI

from app.api_app import api_app
from app.system.health import router as health_router

app = FastAPI()


def create_main_app() -> FastAPI:
    app = FastAPI(
        title="Fish Radar",
        docs_url="/docs",
        openapi_url="/openapi.json"
    )

    # Mount the API app under /api -> sub-application
    app.mount("/api", api_app)

    # System-level endpoints (no DB middleware)
    app.include_router(health_router)

    return app


app = create_main_app()
