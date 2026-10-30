FROM python:3.12-slim
WORKDIR /app
COPY inventory_auditor.py .
CMD ["python", "inventory_auditor.py"]