FROM python:3.9.14

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENV TEST_DB_NAME datalawa_test_docker

EXPOSE 40050
ENTRYPOINT python ./testproject/manage.py runserver 0.0.0.0:40050 --noreload