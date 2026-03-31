# Week 9 – Bio-Inspired Routing

## Description
This project simulates routing behavior based on pheromone reinforcement,
inspired by ant colony optimization.

## Features
- Pheromone reinforcement on success
- Pheromone decay over time
- Adaptive routing decisions

---

## Configuration

Edit `config.py` before running each node.

Example:

Node A:
BASE_PORT = 10000
PEER_PORTS = [10001, 10002]

Node B:
BASE_PORT = 10001
PEER_PORTS = [10000]

Node C:
BASE_PORT = 10002
PEER_PORTS = [10000]

⚠️ Important:
- Each node must use a unique port
- Do not reuse the same port

---

## Run Instructions

1. Open 3 terminals

2. In each terminal:
python node.py

3. Change `BASE_PORT` before running each node

---

## Test Scenario

1. Start all nodes
2. Observe message forwarding
3. Successful routes increase pheromone
4. Wait to observe pheromone decay
5. Routing paths should adapt over time

---

## Expected Behavior

- Frequently used paths become stronger
- Unused paths decay
- Routing decisions improve dynamically