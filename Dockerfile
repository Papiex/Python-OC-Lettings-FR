# Dockerfile
FROM python:3.7

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . code
WORKDIR /code

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
