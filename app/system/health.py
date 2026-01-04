from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health() -> dict[str, str]:
    """
    Simple health endpoint.

    Returns:
        dict: A dictionary, which FastAPI serializes into a JSON response.
    """
    return {"status": "ok"}
