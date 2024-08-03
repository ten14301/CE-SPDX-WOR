# Use the official Python 3.7 image from the Docker Hub
FROM python:3.7

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Upgrade pip to the latest version
RUN pip install --upgrade pip

# Install the Python dependencies from requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV FLASK_RUN_HOST=0.0.0.0


EXPOSE 5000

CMD ["flask", "run"]
