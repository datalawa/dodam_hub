FROM python:3.9.14

WORKDIR /datalawa
COPY . .
#WORKDIR /JGW_hub
#RUN echo "is_debug = 0" > debug.py

#WORKDIR ..
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENV TEST_DB_NAME datalawa_test_docker
#RUN python manage.py runserver

EXPOSE 40050
ENTRYPOINT python ./testproject/manage.py runserver 0.0.0.0:40050