
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install flask gunicorn

CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]
