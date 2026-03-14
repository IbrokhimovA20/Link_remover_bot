FROM python:3.8.7-slim

# set work directory
WORKDIR /remove-link

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies first (for faster builds)
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the code
COPY . .

CMD ["python", "main.py"]