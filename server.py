import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
FORMAT = "utf-8"
DSC_MESSAGE = "!Disconnected"


#Handles individual connections
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} has connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DSC_MESSAGE:
                connected = False
            print(f"[{addr}]: {msg}")
    conn.close()

#Start server and handle connections
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active connections] {threading.active_count() - 1}")

print("[STARTING] Server is starting...")
start()