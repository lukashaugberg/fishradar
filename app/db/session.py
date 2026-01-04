from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import config

engine = create_engine(
    config.db_url,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
        bind=engine,
        autoflush=False,
        autocommit=False
    )

# def get_session():
#     db = SessionLocal()
#     try:
#         yield db
#         db.commit()
#     except:
#         db.rollback()
#         raise
#     finally:
#         db.close()
