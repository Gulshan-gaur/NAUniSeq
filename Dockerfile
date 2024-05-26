# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

COPY test_data /app/test_data

RUN pip install --upgrade pip

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

