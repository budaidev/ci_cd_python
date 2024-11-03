# Use slim Python image for smaller size
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies and poetry
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry==1.5.1

# Copy project files
COPY pyproject.toml poetry.lock ./
COPY src/ src/

# Install dependencies and the package
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --only main \
    && apt-get purge -y build-essential curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Create a directory for input files
RUN mkdir /data

# Set the default command
ENTRYPOINT ["charcount"]
CMD ["/data/input.txt"]
