from time import time
import RPi.GPIO as GPIO
import socket
import threading

in1 = 24
in2 = 23
enA = 25

in3 = 17
in4 = 27
enB = 22

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)

pA=GPIO.PWM(enA,1000)
pB=GPIO.PWM(enB,1000)

pA.start(25)
pB.start(25)

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
print(SERVER)
def handle_client(conn, addr):
    print(f"[SERVER]: NEW CONNECTON - {addr} -")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == "w":
                print("w")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)

            elif msg == "s":
                print("s")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                GPIO.output(in3,GPIO.HIGH)
                GPIO.output(in4,GPIO.LOW)

            elif msg == "a":
                print("a")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.LOW)

            elif msg == "d":
                print("d")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.HIGH)

            elif msg == "q":
                print("q")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                GPIO.output(in3,GPIO.LOW)
                GPIO.output(in4,GPIO.LOW)
            else:
                pass
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[CLIENT]: {addr} - DISCONNECTED -")
def start():
    server.listen()
    print(f"[SERVER]: Server IS RUNNING ON - {SERVER} -")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

print("[SERVER]: Server is starting!")
start()