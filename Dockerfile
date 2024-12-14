FROM python:3.11-slim

# Set the working directory
WORKDIR /src

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
#COPY ./app /app/app
COPY . .

# Expose port 8000
EXPOSE 8000

#CMD ["fastapi", "dev", "src/"] 


# Run the FastAPI app
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
