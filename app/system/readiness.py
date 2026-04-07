import logging

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import engine

logger = logging.getLogger(__name__)

_PING_SQL = text("SELECT 1")
_REVISON_SQL = text("SELECT version_num FROM alembic_version")


def is_database_reachable() -> bool:
    """
    Return True if the DB is reachable and can execute a trivial query.
    """
    try:
        with engine.connect() as conn:
            conn.execute(_PING_SQL)
        return True
    except SQLAlchemyError as exc:
        logger.warning("Database not reachable: %s", exc)
        return False


def current_alembic_revision() -> str | None:
    """
    Return current alembic revision in DB (alembic_version table) if present,
    else None.
    """
    try:
        with engine.connect() as conn:
            row = conn.execute(_REVISON_SQL).scalar_one_or_none()
            return row
    except SQLAlchemyError as exc:
        logger.warning("Could not read alembic revision: %s", exc)
        return None
