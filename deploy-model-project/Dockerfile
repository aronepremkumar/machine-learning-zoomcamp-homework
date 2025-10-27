FROM agrigorev/zoomcamp-model:2025
# Set working directory
WORKDIR /code
# Install uv
RUN pip install uv
# Copy pyproject.toml to install dependencies
COPY pyproject.toml .
# Install dependencies from pyproject.toml using uv
RUN uv pip install --system -r pyproject.toml
# Copy the FastAPI script
COPY app.py .
# Expose the port for FastAPI
EXPOSE 8000
# Run the FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]