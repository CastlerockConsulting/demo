FROM python:3.9
RUN apt-get update
RUN pip install Flask boto3 python-decouple
ADD . /opt/webapp/
WORKDIR /opt/webapp
ENV FLASK_APP=hello.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]