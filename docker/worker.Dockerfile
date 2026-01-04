FROM base AS worker

# Example: Celery/RQ workers may need extra deps (if not already in requirements)
# RUN --mount=type=cache,target=/root/.cache/pip pip install celery[redis]

ENV APP_ENV=prod

# Start background worker
# Celery example
# CMD ["celery", "-A", "app.worker:celery_app", "worker", "-Q", "default", "--loglevel", "INFO"]

# RQ example:
# CMD ["rq", "worker", "-u", "redis://redis:6379/0", "default"]

# Or maybe a custom python script
# CMD ["python", "-m", "app.worker"]