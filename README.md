# ps4xbee
Control an Arbotix Hexapod using a PS4 controller connected to a Raspberry Pi


### Installing
- pipenv install (reads from requirements.txt to build pipfile and lock file)
- to get access to /dev/ttyUSB0:
- `sudo chmod 666 /dev/ttyUSB0` (adding user to dialout didn't work for whatever reason: e.g. `sudo usermod -a -G tty ${USER}` then log out and in again)

### Run
- pipenv run python3 ps4xbee.py

### Docker
##### To build (while in ps4xbee directory):
- ```docker build -t ps4xbee .```

##### To run:
- ```docker run -t --device=/dev/ttyUSB0 --privileged ps4xbee```
