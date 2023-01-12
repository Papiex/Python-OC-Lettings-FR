# Dockerfile
FROM python:3.10

ENV PYTHONUNBUFFERED=1

# Copies the dependencies file inside the container + upgrade pip + install all dependencies
RUN mkdir /code
WORKDIR /code
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copies the rest of the source code
COPY . /code/

ENV PORT=8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]
