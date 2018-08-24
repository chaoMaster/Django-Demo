FROM 172.21.0.24/chaochaoregistry/django:v1
RUN mkdir /webapps
ADD . /webapps/
EXPOSE 8000