FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]