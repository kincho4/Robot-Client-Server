# Robot Documentation

![](https://img.shields.io/github/issues/kincho4/Robot) ![](https://img.shields.io/github/forks/kincho4/Robot) ![](https://img.shields.io/github/stars/kincho4/Robot) ![](https://img.shields.io/github/license/kincho4/Robot) ![](https://img.shields.io/github/contributors/kincho4/Robot)

**Table of contents**

- [Robot Documentation](#robot-documentation)
  * [Software Architecure](#software-architecure)
  * [Client installation](#client-installation)
    + [Windows](#windows)
    + [MacOS/Linux](#macos-linux)
  * [Server installation](#server-installation)
    + [Linux](#linux)

## Software Architecure
The software architecture for the robot code is fairly simple. The client side will enter the public/local ip address of the robot. The client will then perform 1 ping to check if the ip is online, if not it will ask for the ip again. If the ip is online it will attempt to connect to the robot using the python socket module. Once it connects to the server it can send commands for speed and movement.

![](https://github.com/kincho4/Robot/tree/master/images/diagram.png)

## Client installation
### Windows
```
# clone the repo
$ git clone https://github.com/kincho4/Robot.git

# change into the cloned directory
cd Robot

# change into the client directory
cd client

#install requirements
pip install -r reqscl.txt
```
### MacOS/Linux
```
# clone the repo
$ git clone https://github.com/kincho4/Robot.git

# change into the cloned directory
cd Robot

# change into the client directory
cd client

#install requirements
python3 -m pip install -r reqscl.txt
```

## Server installation
### Linux
```
#clone the repo
$ git clone https://github.com/kincho4/Robot.git
```
**OPTIONAL:** Start program on boot.
```
# Open a new unit file
sudo nano /lib/systemd/system/rbtserver.service

# Add content to file
[Unit]
Description=Python file to handle client commands
After=multi-user.target

[Service]
Type=idle

# Change the directory of the python file if needed
ExecStart=/usr/bin/python /home/pi/Robot/rpi/rpiserver.py

[Install]
WantedBy=multi-user.target

# Save file
Ctrl + O

# Exit file
Ctrl + X

# Enable it to run on boot
$ sudo systemctl daemon-reload
$ sudo systemctl enable sample.service
```
