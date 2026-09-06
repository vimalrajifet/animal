FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY best_animal_model.keras ./animal_model.keras
COPY classes.json .
COPY animal_data.py .
COPY server.py .
COPY index.html .
COPY style.css .
COPY script.js .
COPY web/ ./web/

# Hugging Face Spaces uses port 7860 by default; Render uses $PORT
ENV PORT=7860
EXPOSE 7860

CMD ["sh", "-c", "uvicorn server:app --host 0.0.0.0 --port ${PORT:-7860}"]
