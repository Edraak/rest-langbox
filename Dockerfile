FROM java:8

RUN mkdir /code/

WORKDIR /code/

RUN apt-get update -y

RUN apt-get install -y python-pip

ADD requirements.txt /code/
RUN pip install -r requirements.txt

RUN mkdir /rest-javac/

ADD app_tests.py app.py /code/
ADD fixtures /code/fixtures
