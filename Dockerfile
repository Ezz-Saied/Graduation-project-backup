FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for psycopg
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy Pipfile for dependency installation
COPY Pipfile Pipfile.lock /app/

# Install pipenv and Python dependencies
RUN pip install --no-cache-dir pipenv
RUN pipenv install --system --deploy

# Copy the rest of the project (including credentials.json)
COPY . /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
