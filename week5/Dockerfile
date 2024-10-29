# Start from the prepared image
FROM svizor/zoomcamp-model:3.11.5-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python 3.12
RUN wget -O python3.12.tgz https://www.python.org/ftp/python/3.12.0/Python-3.12.0.tgz && \
    tar -xzf python3.12.tgz && \
    cd Python-3.12.0 && \
    ./configure --enable-optimizations && \
    make altinstall && \
    cd .. && \
    rm -rf Python-3.12.0 python3.12.tgz

# Install pipenv
RUN curl -sSL https://bootstrap.pypa.io/get-pip.py | python3.12 && \
    pip install pipenv

# Copy Pipfile and Pipfile.lock to install dependencies
COPY Pipfile Pipfile.lock ./

# Install dependencies
RUN pipenv install --deploy --ignore-pipfile

# Copy your Flask script (replace 'app.py' with your actual Flask script filename)
COPY app.py .

# Expose the port that your Flask app runs on
EXPOSE 8000

# Run the Flask app using Gunicorn
CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:8000", "app:app"]
