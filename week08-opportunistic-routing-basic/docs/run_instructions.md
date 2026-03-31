## Run Instructions

1. Open 3 terminals

2. Run each node in separate folders:

Terminal 1:
cd nodeA
python node.py

Terminal 2:
cd nodeB
python node.py

Terminal 3:
cd nodeC
python node.py

## Configuration

Each node uses a different port:

- nodeA → 9000
- nodeB → 9001
- nodeC → 9002

Ensure ports are not duplicated.

## Test Scenario

1. Start all nodes
2. Observe message forwarding
3. Stop one node
4. Messages should be stored in queue
5. Restart node and observe forwarding