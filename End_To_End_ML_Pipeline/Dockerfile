#  1. Python runtime image
FROM python:3.9.6-slim

# 2. Set the working directory
WORKDIR .

# 3. Copy the project specific required packages into the container
COPY requirements.txt .

# 4. Install the project-specific packages
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the current directory into the container
COPY . .

# 6. Run Command to start the file
CMD ["python","Hello_World.py"]
