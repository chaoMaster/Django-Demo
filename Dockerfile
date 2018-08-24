FROM 172.21.0.24/chaochaoregistry/python:3.6
RUN mkdir /webapps
ADD . /webapps/
RUN pip install -U pip setuptools && pip install -r /webapps/requirements.txt
EXPOSE 8000