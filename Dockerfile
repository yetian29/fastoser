# Stage 1: Builder
FROM python:3.12-slim-bullseye as builder

# Install Poetry
RUN pip install --upgrade pip
RUN pip install poetry-plugin-export

# Set the working directory
WORKDIR /tmp

# Copy dependency management files
COPY ./pyproject.toml ./poetry.lock* /tmp/

# Export all dependencies (including dev) to requirements.txt
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes --with dev 


# Stage 2: Development environment
FROM python:3.12-slim-bullseye as dev

# Set the working directory
WORKDIR /fastoser

# Copy requirements.txt from builder stage
COPY --from=builder /tmp/requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the source code and entrypoint script into the container
COPY ./src/ /fastoser/src
COPY ./entrypoint.sh /fastoser/entrypoint.sh
COPY ./example.env /fastoser/example.env
COPY ./Makefile  /fastoser/Makefile

# Make the entrypoint script executable
RUN chmod +x /fastoser/entrypoint.sh

# Define the entrypoint
ENTRYPOINT ["/fastoser/entrypoint.sh"]

