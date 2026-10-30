# ---------------------------------------------------------------------------
# Inventory Management System - INF1103 DevOps Labs
# ---------------------------------------------------------------------------
FROM python:3.12-slim

LABEL org.opencontainers.image.title="inventory-management-system" \
      org.opencontainers.image.description="Command-line OOP Inventory Management System (INF1103 DevOps Labs)" \
      org.opencontainers.image.authors="Brandon Poon" \
      org.opencontainers.image.source="https://github.com/brandonpxw/inf1103-labs"

# Don't write .pyc files, and flush output straight to the terminal
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Run as an unprivileged user instead of root
RUN useradd --create-home --uid 1000 appuser

# Copy the application source and seed data (see .dockerignore for exclusions)
COPY --chown=appuser:appuser *.py ./
COPY --chown=appuser:appuser data/ ./data/

USER appuser

# Inventory changes are saved here; mount a volume to keep them between runs
VOLUME ["/app/data"]

# Interactive app - start with: docker run -it --rm inf1103/inventory-system
CMD ["python", "oop_inventory_system.py"]
