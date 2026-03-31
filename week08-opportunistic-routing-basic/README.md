# Week 8 – Opportunistic Routing

## Description
This project implements opportunistic routing using delivery probability.
Messages are forwarded only when the probability exceeds a threshold.

## Features
- Delivery probability table
- Opportunistic forwarding
- Message queue for failed delivery

---

## Configuration

Edit `config.py` before running each node.

Example:

Node A:
BASE_PORT = 9000
PEER_PORTS = [9001, 9002]

Node B:
BASE_PORT = 9001
PEER_PORTS = [9000]

Node C:
BASE_PORT = 9002
PEER_PORTS = [9000]

⚠️ Important:
- Each node must use a different BASE_PORT
- Ports must not be duplicated

---

## Run Instructions

1. Open 3 terminals

2. In each terminal:
python node.py

3. Before running each terminal, update `config.py` with a different port

---

## Test Scenario

1. Start all nodes
2. Observe messages being sent
3. Stop one node → messages should be queued
4. Restart node → queued messages should be forwarded

---

## Expected Behavior

- Messages are forwarded based on probability
- Messages are stored if delivery fails
- Messages are retried periodically