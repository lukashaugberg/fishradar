from fastapi import FastAPI

from app.middleware.db_session import DBSessionMiddleWare
from app.api import router as api_router


def create_api_app() -> FastAPI:
    api_app = FastAPI(
        title="Fish Radar API",
        docs_url="/docs",
        openapi_url="/openapi.json"
    )

    # DB session middleware only for this API app
    api_app.add_middleware(DBSessionMiddleWare)

    # All API routes live here (starting at /auth, /users, etc.)
    api_app.include_router(api_router)

    return api_app


api_app = create_api_app()
