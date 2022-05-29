FROM ubuntu:22.04

ADD src /opt/sir_model_calculator
COPY requirements.txt /opt/sir_model_calculator
WORKDIR  /opt/sir_model_calculator

RUN apt update && apt install -y python3 python3-pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "-m", "main"]

