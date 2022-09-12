FROM python:latest
RUN apt update
RUN apt upgrade -y
RUN git clone https://github.com/Red-Umsalud/SistemaAtlasHistologia
WORKDIR SistemaAtlasHistologia
RUN pip install -r requirements.txt
EXPOSE 5000