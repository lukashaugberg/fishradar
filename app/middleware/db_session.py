from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.db.session import SessionLocal


class DBSessionMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        # create one session per request
        db = SessionLocal()
        # attach it to the request object
        request.state.db = db

        try:
            response = await call_next(request)  # let the route run
            db.commit()  # commit whatever the route did with it
            return response
        except Exception:
            db.rollback()  # rollback on error
            raise
        finally:
            db.close()  # always close the session
