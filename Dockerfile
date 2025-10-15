# Use official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (replace libatlas-base-dev with libopenblas-dev)
RUN apt-get update && apt-get install -y \
    libopenblas-dev \
    && pip install --no-cache-dir -r requirements.txt

# Install Streamlit and MongoDB dependencies
RUN pip install streamlit pymongo==4.6.1 bson toml

# Expose the port streamlit runs on
EXPOSE 8501

# Set the environment variable for MongoDB connection string
# ENV MONGO_CONNECTION_STRING=mongodb://your_mongo_connection_string

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
