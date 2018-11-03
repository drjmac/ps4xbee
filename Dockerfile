FROM python:3.7

WORKDIR /ps4xbee

COPY . /ps4xbee

RUN pip3 install -r requirements.txt

CMD ["python3", "ps4xbee.py"]
