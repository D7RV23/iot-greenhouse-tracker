FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy script and .env into the container
COPY db_connect_select.py .
COPY .env .

# Install libraries
RUN pip install psycopg2-binary python-dotenv

# Run script when container starts
CMD ["python", "db_connect_select.py"]
