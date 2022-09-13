FROM python:latest
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN apt update
RUN apt upgrade -y
RUN git clone https://github.com/Red-Umsalud/SistemaAtlasHistologia
WORKDIR /SistemaAtlasHistologia
RUN pip install -r requirements.txt
EXPOSE 5000
