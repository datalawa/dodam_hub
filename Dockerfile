FROM python:3.9.14
ENV PYTHONUNBUFFERED=1
ENV TEST_DB_NAME datalawa_test_docker

COPY . .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 40050
WORKDIR testproject/
ENTRYPOINT gunicorn --bind=0.0.0.0:40050 config.wsgi:application