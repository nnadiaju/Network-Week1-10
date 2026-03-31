import socket
import threading
import time
from config import *
from token import Token

token_queue = []

def send_token(peer_port, token):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, peer_port))
        s.sendall(token.message.encode())
        s.close()
        print(f"[{BASE_PORT}] Sent token")
        return True
    except:
        return False

def forward_loop():
    while True:
        for token in token_queue[:]:
            for peer in PEER_PORTS:
                if send_token(peer, token):
                    token_queue.remove(token)
                    break
        time.sleep(UPDATE_INTERVAL)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, BASE_PORT))
    server.listen()

    print(f"[{BASE_PORT}] Listening...")

    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE).decode()

        token = Token(data)
        msg = token.read_token()

        if msg:
            print(f"[{BASE_PORT}] Received: {msg}")
            token_queue.append(token)
        else:
            print("Token invalid")

        conn.close()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    threading.Thread(target=forward_loop, daemon=True).start()

    token_queue.append(Token(f"Quantum msg from {BASE_PORT}"))

    while True:
        time.sleep(1)