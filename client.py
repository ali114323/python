import socket, sys

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DSC_MESSAGE = "Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def chatbox(msg2):
    message = msg2.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

send("Type in \"Disconnect\" to disconnect")
alive = True
while True:
    msg2 = input("What would you like to send?")
    chatbox(msg2)
    if msg2 == DSC_MESSAGE:
        client.remove(client)