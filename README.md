# Quantum Computing Circuits with Qiskit

This repository contains quantum circuits implemented with IBM Qiskit as part of a university course on quantum computing.

## Files

- `deux_qubit.py` – Creates a two-qubit Bell state and measures it. Outputs a histogram of results.
- `super-dense.py` – Implements the superdense coding protocol (teleportation) to send a 2-bit message using one entangled qubit.
- `circuit_bell_state.png` – Circuit diagram for the Bell state.
- `circuit_teleportation.png` – Circuit diagram for the teleportation protocol.
- `Figure_2.png` – Histogram of measurement results from the Bell state circuit.

## Requirements

Install the following packages:
pip install qiskit qiskit-aer matplotlib

text

## How to Run
python deux_qubit.py
python super-dense.py

text

## Results

The Bell state circuit produces approximately 50% |00> and 50% |11> as shown in Figure_2.png. The superdense coding circuit transmits the message stored in `message_alice` (currently set to '01').

## Author

Samuel Yedidya Tchuengue Kamdem
GitHub: https://github.com/KamdemSamuel
LinkedIn: https://www.linkedin.com/in/samuel-yedidya/

## License

MIT
