import socket
import threading
import time
from config import *
from pheromone_table import PheromoneTable

pheromone_table = PheromoneTable()
message_queue = []

def send_message(peer_port, message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, peer_port))
        s.sendall(message.encode())
        s.close()
        pheromone_table.reinforce(peer_port, REINFORCEMENT)
        print(f"[{BASE_PORT}] Sent -> {peer_port}")
        return True
    except:
        return False

def forward_loop():
    while True:
        pheromone_table.decay()
        candidates = pheromone_table.get_best_candidates(FORWARD_THRESHOLD)

        for msg in message_queue[:]:
            for peer in candidates:
                if send_message(peer, msg):
                    message_queue.remove(msg)
                    break

        time.sleep(UPDATE_INTERVAL)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, BASE_PORT))
    server.listen()

    print(f"[{BASE_PORT}] Listening...")

    while True:
        conn, _ = server.accept()
        data = conn.recv(BUFFER_SIZE).decode()
        print(f"[{BASE_PORT}] Received: {data}")
        message_queue.append(data)
        conn.close()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    threading.Thread(target=forward_loop, daemon=True).start()

    for peer in PEER_PORTS:
        pheromone_table.reinforce(peer, INITIAL_PHEROMONE)

    while True:
        msg = f"Bio message from {BASE_PORT}"
        message_queue.append(msg)
        time.sleep(10)