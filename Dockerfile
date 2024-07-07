# Use a Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP simwire.app
# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install pytest
RUN pip install pytest


# Copy the current directory contents into the container at /app
COPY . /app

# Run the tests using pytest
RUN pytest --disable-warnings

# Expose port 80 to the outside world
EXPOSE 80

# Command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]