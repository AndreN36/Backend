FROM python:3.12-slim

WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy dependency files
COPY pyproject.toml poetry.lock* ./

# Poetry install
RUN poetry install --no-root --no-interaction --no-ansi

# Copy application code
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run the application
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]