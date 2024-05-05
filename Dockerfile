# Use the official Python 3.10 image as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define an environment variable for video path (default value: empty)
ENV VIDEO_PATH=""

# Command to run when the container starts
CMD ["python", "main.py"]
