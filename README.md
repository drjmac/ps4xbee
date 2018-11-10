# ps4xbee
Control an Arbotix Hexapod using a PS4 controller connected to a Raspberry Pi


### Installing
- pipenv install (reads from requirements.txt to build pipfile and lock file)
- to get access to /dev/ttyUSB0:
- `sudo chmod 666 /dev/ttyUSB0` (adding user to dialout didn't work for whatever reason: e.g. `sudo usermod -a -G tty ${USER}` then log out and in again)

### Run
- pipenv run python3 ps4xbee.py

### Docker
##### To build (for amd64, while in ps4xbee directory):
- ```docker build -t ps4xbee:amd64 -f amd64/Dockerfile .```

##### To build (for arm32v7):
- ```docker build -t ps4xbee:arm32v7 -f arm32v7/Dockerfile .```

##### Multi-architecture images
- created using the instructions at: https://medium.com/@mauridb/docker-multi-architecture-images-365a44c26be6

##### To run:
- ```docker run -t --device=/dev/ttyUSB0 --privileged ps4xbee```
