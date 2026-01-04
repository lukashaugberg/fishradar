FROM base as api

# Environment can be ovverridden by docker-compose
ENV APP_ENV=prod

# Default command: run the HTTP API
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]