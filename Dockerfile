FROM python:3.12-slim
WORKDIR /app
COPY *.py ./
COPY data ./data
# Default: run the Inventory Management System (use: docker run -it <image>)
CMD ["python", "oop_inventory_system.py"]
