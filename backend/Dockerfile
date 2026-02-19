FROM python:3.14-slim

RUN pip install --upgrade pip && pip install uv

WORKDIR /app

COPY . .

RUN uv pip install --system --no-cache-dir

EXPOSE 8001

# Start FastAPI app with uvicorn via uv
CMD ["uv", "icorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
