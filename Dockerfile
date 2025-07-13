# Simple Dockerfile for Flask app
FROM python:3.8-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install Python packages
RUN pip install -r requirements.txt

# Copy all your code
COPY . .

# Create artifacts folder
RUN mkdir -p artifacts

# Tell Docker which port your app uses
EXPOSE 5000

# Command to run your app
CMD ["python", "app.py"]