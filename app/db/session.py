from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config

engine = create_engine(
    config.db_url,
    pool_pre_ping=True,
    connect_args={
        # psycopg connect timeout
        "connect_timeout": 3,
        # Applies per-connection (guardrail for probes and queries)
        "options": "-c statement_timeout=4000"
    }
)

SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )
