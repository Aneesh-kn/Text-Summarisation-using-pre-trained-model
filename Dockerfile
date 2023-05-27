FROM ucmercedandeslab/tinyos_debian:latest
FROM continuumio/anaconda3:4.4.0
FROM python:3.10.10
COPY . /usr/app/
EXPOSE 5000
WORKDIR /usr/app/
RUN pip install --upgrade pip
RUN pip install --ignore-installed PyYAML
RUN pip install --ignore-installed packaging
RUN pip install -r requirements.txt
CMD python app.py

