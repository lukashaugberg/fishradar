from fastapi import APIRouter, HTTPException, status

from app.system.readiness import is_database_reachable, current_alembic_revision

router = APIRouter()


@router.get("/health", status_code=status.HTTP_200_OK)
def health() -> dict[str, str]:
    """
    Simple health endpoint.

    Returns:
        dict: A dictionary, which FastAPI serializes into a JSON response.
    """
    return {"status": "ok"}


@router.get("/ready", status_code=status.HTTP_200_OK)
def ready() -> dict[str, str]:
    """
    Verifies that the database is reachable and that Alembic migrations
    have been applied. Returns 503 if the service is not ready to receive traffic.
    """
    if not is_database_reachable():
        raise HTTPException(status_code=503, detail="Database not reachable")

    revision = current_alembic_revision()
    if not revision:
        raise HTTPException(status_code=503, detail="Migrations not applied")

    return {
        "status": "ready",
        "db": "up",
        "alembic_revision": revision
    }
