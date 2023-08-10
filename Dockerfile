# Use an official Python runtime as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.5.1

# get portaudio and ffmpeg
RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

# Install poetry
RUN pip install "poetry==$POETRY_VERSION"

# Set the working directory in Docker
WORKDIR /app

# Copy the `pyproject.toml` and `poetry.lock` to install dependencies
COPY pyproject.toml poetry.lock /app/

# Copy the content of the local directory to the working directory
COPY . /app/

# Install project dependencies
RUN poetry install --no-interaction --no-ansi

EXPOSE 3000
# Specify the command to run on container start
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]