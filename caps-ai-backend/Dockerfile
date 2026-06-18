FROM python:3.11-slim

WORKDIR /code

# Install build dependencies for ChromaDB and other packages that require compilation
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install dependencies
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Ensure python output is sent straight to terminal
ENV PYTHONUNBUFFERED=1

# Copy all your backend code into the container
COPY . .

# Start the Flask app using Gunicorn with access logs enabled
CMD ["gunicorn", "--access-logfile", "-", "-b", "0.0.0.0:7860", "run:app"]
