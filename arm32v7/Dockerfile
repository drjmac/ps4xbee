FROM arm32v7/python

WORKDIR /ps4xbee

COPY . /ps4xbee

RUN apt-get update && apt-get install -y python3-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev   libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev

RUN pip3 install -r requirements.txt

CMD ["python3", "ps4xbee.py"]
