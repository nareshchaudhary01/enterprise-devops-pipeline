FROM python:3.10-slim

WORKDIR /app

# Dependency Caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Source Code
COPY . .

# Expose Service Port
EXPOSE 8000

# Production Execution using Gunicorn Multi-Worker
CMD ["gunicorn", "-w", "2", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]