FROM python:3:13-slim AS base

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m appuser
WORKDIR /app

# Leverage Docker layer caching: copy only requirements first
COPY requirements.txt ./

# Use BuildKit cache to speed up pip installs
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-compile --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensure files owned by non-root
RUN chown -R appuser:appuser /app
USER appuser

# Set a minimal, safe runtime env (override via compose)
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Expose is documentation only; API service will bind to 8000
EXPOSE 8000