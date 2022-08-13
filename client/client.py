from pynput.keyboard import *
import socket
import os
import json

print("Welcome to the Robot client!\n")
while True:
    empcheck = open("data.json", "r")
    dod = json.loads(empcheck.read())
    empcheck.close()
    if dod["ip"] == "":
        rpi_ip = input("Enter the local ip of the Robot: ")
        response = os.system(f"ping -n 1 {rpi_ip}")
        if response == 0:
            SERVER = rpi_ip
            ask_save = input("Would you like to save this in a data file? [y/n]")
            if ask_save == "y":
                with open("data.json", "w") as add_ip:
                    data = {"ip":rpi_ip}
                    jdata = json.dumps(data)
                    add_ip.write(jdata)
                print("Ip written to [data.json] file")
                break
            elif ask_save == "n":
                print("Ok!")
                break
            else:
                print("Thats not a valid option. Please enter: [y/n]")
        else:
            print("The IP that you entered is not valid!")
    else:
        print("Ip already detected in [data.json]. Using that ip to connect.")
        break

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

print("\n***Press 'h' to view the controls!***")

def motor_move(direction):
    message = direction.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

def press_on(key):
    if hasattr(key, "char"):
        if key.char == ("h"):
            print("\n**Controls**:\nh - Shows this menu\nw - Moves robot forwards\ns - Moves robot backwards\na - Turns the robot to the left\nd - Turns the robot to the right\nesc - quits this program\n")
        elif key.char == ("w"):
            motor_move("w")
        elif key.char == ("s"):
            motor_move("s")
        elif key.char == ("a"):
            motor_move("a")
        elif key.char == ("d"):
            motor_move("d")
        elif key.char == ("q"):
            motor_move("q")
        else:
            pass
    else:
        pass


def press_off(key):
    if key == Key.esc:
        motor_move(DISCONNECT_MESSAGE)
        return False


with Listener(on_press=press_on, on_release=press_off) as listener:
    listener.join()
