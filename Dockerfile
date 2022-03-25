FROM python:3.9-slim-buster

RUN mkdir -p /usr/src/app/

WORKDIR /usr/src/app/

COPY . /usr/src/app/

RUN apt-get update

RUN apt-get -y install libxml2-dev libxslt-dev python-dev

COPY requirements.txt /usr/src/app/requirements.txt

RUN python3 -m pip install -r /usr/src/app/requirements.txt

CMD ["python", "app.py"]