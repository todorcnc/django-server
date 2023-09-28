# Use the official Python image from the DockerHub, based on Alpine Linux with Python 3.11.4
FROM python:3.11.4-alpine

# Set the environment variable PYTHONDONTWRITEBYTECODE to 1.
# This means Python won't try to write .pyc files which are bytecode for modules.
# This is often done to keep the image clean, especially if the code may change frequently.
ENV PYTHONDONTWRITEBYTECODE 1

# Set the environment variable PYTHONUNBUFFERED to 1.
# This ensures that Python's output (e.g., print statements) and log messages appear immediately 
# in the Docker logs. It prevents Python from buffering outputs.
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container to /usr/src/app.
# Any subsequent commands that are run will be executed in this directory.
WORKDIR /usr/src/app

# Copy the current directory contents from the host machine into the container at /usr/src/app.
# This is often your application source code.
COPY . .

# Make the start_server.sh script inside the container executable.
# This is necessary if you want to run this script as an entry point or command later on.
RUN chmod +x start_worker.sh

RUN pip install --upgrade pip

# Execute a command inside the container, which in this case, 
# installs the required Python packages specified in the requirements.txt file.
RUN pip install -r requirements.txt