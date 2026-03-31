# Run Instructions – Week 10 Quantum-Inspired Networking

## Setup
1. Open multiple terminals
2. Edit config.py:
   - Assign different BASE_PORT (11000, 11001, 11002)
   - Set PEER_PORTS

## Run
python node.py

## Test Scenario
1. Run all nodes
2. Observe token messages being sent and received
3. Each token should be readable only once
4. Attempt to reuse token → should fail
5. Wait for token expiry → expired tokens should not work

## Expected Behavior
- Tokens are consumed after one read
- Messages cannot be duplicated
- Expired tokens are discarded