# Run Instructions – Week 9 Bio-Inspired Routing

## Setup
1. Open multiple terminals
2. Edit config.py for each node:
   - Use different BASE_PORT (10000, 10001, 10002)
   - Set PEER_PORTS accordingly

## Run
python node.py

## Test Scenario
1. Run multiple nodes
2. Observe message forwarding between nodes
3. Successful transmissions increase pheromone values
4. Wait to observe pheromone decay over time
5. Routing decisions should adapt to better paths

## Expected Behavior
- Frequently used paths become stronger
- Less used paths decay over time
- Routing improves dynamically