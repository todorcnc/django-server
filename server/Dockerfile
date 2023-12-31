# Use an official NVIDIA CUDA runtime as a parent image
FROM nvidia/cuda:11.8.0-devel-ubuntu22.04

# Set environment variables
# Set the environment variable PYTHONDONTWRITEBYTECODE to 1.
# This means Python won't try to write .pyc files which are bytecode for modules.
# This is often done to keep the image clean, especially if the code may change frequently.
ENV PYTHONDONTWRITEBYTECODE 1

# Set the environment variable PYTHONUNBUFFERED to 1.
# This ensures that Python's output (e.g., print statements) and log messages appear immediately 
# in the Docker logs. It prevents Python from buffering outputs.
ENV PYTHONUNBUFFERED=1

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and pip
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Create symbolic links for Python and pip
RUN ln -sf /usr/bin/python3.10 /usr/bin/python \
    && ln -sf /usr/bin/python3.10 /usr/bin/python3 \
    && ln -sf /usr/bin/pip3 /usr/bin/pip


# Set the working directory inside the container to /usr/src/app.
# Any subsequent commands that are run will be executed in this directory.
WORKDIR /usr/src/app

# Copy the current directory contents from the host machine into the container at /usr/src/app.
# This is often your application source code.
COPY . .

# Make the start_server.sh script inside the container executable.
# This is necessary if you want to run this script as an entry point or command later on.
RUN chmod +x start_server.sh

RUN pip install --upgrade pip

# Execute a command inside the container, which in this case, 
# installs the required Python packages specified in the requirements.txt file.
RUN pip install -r requirements.txt
# Install diffusers library needed for SDXL. 
# It has different dependancies on WIndows and Linux
RUN pip install diffusers["torch"] transformers