FROM python:3.8.7-slim

# set work directory
WORKDIR /remove-link

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . .

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]