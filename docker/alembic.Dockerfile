FROM base AS alembic

# Working dir should contain alembic.ini and migrations/ directory
WORKDIR /app

# Default to a harmless command; override in compose/CI as needed.
# Typical commands:
#   alembic upgrade head
#   alembic revision --autogenerate -m "message"
CMD ["alembic", "upgrade", "head"]