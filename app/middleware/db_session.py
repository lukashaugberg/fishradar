from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

from app.db.session import SessionLocal


class DBSessionMiddleWare(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> Response:
        # create one session per request
        db = SessionLocal()
        request.state.db = db  # attach it to the request object

        try:
            response = await call_next(request)  # let the route run
            db.commit()  # commit whatever the route did with it
            return response
        except Exception:
            db.rollback()  # rollback on error
            raise
        finally:
            db.close()  # always close the session
