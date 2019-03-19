FROM ubuntu:18.10

LABEL Author="Ramon Borges"
LABEL Description="Miner container"

RUN apt-get update -y && \
    apt-get install python3 python3-pip -y && \
    apt-get clean && \
    pip3 install PyPDF2 && \
    pip3 install nltk && \
    pip3 install requests

VOLUME ["/data"]
VOLUME ["/script"]

ENTRYPOINT ["python3", "/script/miner.py"]