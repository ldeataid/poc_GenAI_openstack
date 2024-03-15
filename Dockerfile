# Use an appropriate base image for Python
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY ./requirements.txt .

# Install the Python dependencies
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copy src folder into /app
COPY ./src/* ./

# Copy /sdk into /app/sdk
RUN mkdir sdk
COPY ./src/sdk/* ./sdk

# Specify PYTHONPATH so modules can be found
RUN export PYTHONPATH=/app

# Specify the command to run when the container starts
CMD ["python", "main.py"]

# Expose the port that the server will be listening to
EXPOSE 2000
