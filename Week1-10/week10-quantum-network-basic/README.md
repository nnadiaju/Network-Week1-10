# Week 10 – Quantum-Inspired Networking

## Description
This system simulates quantum-inspired message behavior using tokens.

## Features
- Messages represented as tokens
- Tokens can be read only once
- Token expiration mechanism

## Configuration
Each node uses a different port:

- nodeA → 11000
- nodeB → 11001
- nodeC → 11002

## Run Instructions

1. Open 3 terminals

Terminal 1:
cd nodeA
python node.py

Terminal 2:
cd nodeB
python node.py

Terminal 3:
cd nodeC
python node.py

## Test Scenario

1. Start all nodes
2. Observe token transmission
3. Token can be read only once
4. Attempt to reuse token (should fail)
5. Wait for token expiration

## Expected Behavior
- Tokens are consumed after reading
- Messages cannot be duplicated
- Expired tokens are discarded