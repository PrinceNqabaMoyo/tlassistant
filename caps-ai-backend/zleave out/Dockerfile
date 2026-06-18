# Use an official Python runtime as a parent image
# python:3.11-slim is a great choice for small images.
FROM python:3.11-slim

# Install necessary build tools and a C++ compiler.
# This is required to build packages like chroma-hnswlib from source.
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt.
# This step should now succeed with the build tools installed.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code
COPY . .

# Expose port 8080 for the application to listen on
EXPOSE 8080

# Define the command to run your app using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "MainApp:app"]
