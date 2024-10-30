FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client libpq-dev gcc

COPY requirements.txt /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./ /app

EXPOSE 8000

CMD ["sh", "-c", "aerich upgrade && uvicorn app.app:app --host 0.0.0.0 --port 8000 --reload"]
