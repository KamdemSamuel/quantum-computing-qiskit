# Quantum Computing Circuits with Qiskit

This repository contains quantum circuits implemented with IBM Qiskit as part of a university course on quantum computing.

## 📋 Overview

This project demonstrates fundamental quantum computing concepts through practical circuit implementations:

- **Bell States** - Understand quantum entanglement
- **Quantum Teleportation** - Send quantum information using classical bits
- **Superdense Coding** - Transmit classical information using entangled qubits

## 🎯 What Each Circuit Does

### Bell State (`deux_qubit.py`)

Creates a two-qubit entangled state and measures the results.

**Circuit Components:**
- Hadamard gate on first qubit (creates superposition)
- CNOT gate (creates entanglement)
- Measurement of both qubits

**Expected Results:**
- 50% probability of measuring |00⟩
- 50% probability of measuring |11⟩
- Never measures |01⟩ or |10⟩ (this demonstrates entanglement!)

**Run it:**
```bash
python deux_qubit.py
```

**Output:** Histogram showing measurement distribution (see `Figure_2.png`)

---

### Superdense Coding & Quantum Teleportation (`super-dense.py`)

Implements two important quantum protocols:

1. **Quantum Teleportation**
   - Sends quantum state of one qubit to another qubit
   - Uses 2 classical bits + 1 entangled pair
   - Demonstrates quantum information transfer

2. **Superdense Coding**
   - Alice sends 2 classical bits to Bob using only 1 qubit
   - Requires a pre-shared entangled pair
   - Message stored in `message_alice` variable (currently '01')

**Run it:**
```bash
python super-dense.py
```

---

## 📦 Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install qiskit==0.43.0 qiskit-aer==0.13.0 matplotlib==3.7.1
```

### Minimum Versions
- **Qiskit**: 0.43.0 or higher
- **Qiskit-Aer**: 0.13.0 or higher
- **Matplotlib**: 3.7.1 or higher
- **Python**: 3.8+

---

## 🚀 How to Run

### Prerequisites
Make sure you have Python 3.8+ and pip installed.

### Setup

```bash
# Clone the repository
git clone https://github.com/KamdemSamuel/quantum-computing-qiskit.git
cd quantum-computing-qiskit

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Examples

**Bell State Circuit:**
```bash
python deux_qubit.py
```

**Teleportation & Superdense Coding:**
```bash
python super-dense.py
```

Both scripts will:
- Create quantum circuits
- Display circuit diagrams
- Run simulations
- Show measurement results in histograms

---

## 📊 Circuit Diagrams

Circuit diagrams are saved as PNG images:

- **`circuit_bell_state.png`** - Visual representation of the Bell state circuit
- **`circuit_teleportation.png`** - Visual representation of the teleportation protocol
- **`Figure_2.png`** - Histogram of measurement results from Bell state circuit

---

## 📈 Results

### Bell State Results

The Bell state circuit produces approximately:
- **50% |00⟩** (both qubits measured as 0)
- **50% |11⟩** (both qubits measured as 1)

This is shown in the histogram `Figure_2.png`.

**Key Insight:** The measurements are perfectly correlated - if one qubit is 0, the other must be 0. If one is 1, the other must be 1. This is quantum entanglement!

### Teleportation Protocol

Sends the quantum state |ψ⟩ from Alice's qubit to Bob's qubit with 100% fidelity using classical communication.

### Superdense Coding

Alice can send 2 classical bits (00, 01, 10, or 11) to Bob by manipulating her qubit and sending it through the channel. Bob measures both qubits to recover the message.

---

## 🧠 Quantum Computing Concepts Covered

| Concept | Description | Circuit |
|---------|-------------|----------|
| **Superposition** | Qubit exists in multiple states simultaneously | Hadamard gate |
| **Entanglement** | Two qubits correlated such that measuring one affects the other | CNOT gate |
| **Quantum Measurement** | Observing a qubit collapses it to a definite state | Measurement |
| **Phase** | Relative phase between basis states affects probability | Pauli gates |
| **Quantum Information** | Information encoded in qubit states | All circuits |

---

## 📚 File Structure

```
quantum-computing-qiskit/
├── deux_qubit.py                # Bell state implementation
├── super-dense.py               # Teleportation & superdense coding
├── circuit_bell_state.png       # Bell circuit diagram
├── circuit_teleportation.png    # Teleportation circuit diagram
├── Figure_2.png                 # Measurement histogram
├── requirements.txt             # Python dependencies
├── LICENSE                      # MIT License
└── README.md                    # This file
```

---

## 🎓 Learning Resources

### Essential Reading
- IBM Qiskit Documentation: https://qiskit.org/documentation/
- Quantum Computing Basics: https://www.ibm.com/quantum/what-is-quantum-computing/

### Bell States
- Understanding Entanglement: https://en.wikipedia.org/wiki/Bell%27s_theorem

### Quantum Protocols
- Quantum Teleportation: https://en.wikipedia.org/wiki/Quantum_teleportation
- Superdense Coding: https://en.wikipedia.org/wiki/Superdense_coding

---

## 💡 Next Steps

To extend this project:

1. **Implement Quantum Error Correction** - Add noise and error correction codes
2. **Grover's Algorithm** - Implement quantum search
3. **Variational Quantum Algorithms** - Use hybrid quantum-classical approaches
4. **VQE (Variational Quantum Eigensolver)** - Solve molecular problems
5. **Run on Real Quantum Hardware** - Execute on IBM's quantum computers via cloud

---

## ⚠️ Troubleshooting

### Import Error: No module named 'qiskit'
```bash
pip install -r requirements.txt
```

### No module named 'qiskit_aer'
```bash
pip install qiskit-aer
```

### Circuit Diagrams Not Displaying
Make sure matplotlib is installed:
```bash
pip install matplotlib
```

### Slow Simulation
- Reduce the number of qubits or circuit depth
- Use `qasm_simulator` instead of `statevector_simulator` for larger circuits

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Samuel Yedidya Tchuengue Kamdem**
- GitHub: [KamdemSamuel](https://github.com/KamdemSamuel)
- LinkedIn: [samuel-yedidya](https://www.linkedin.com/in/samuel-yedidya/)

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/quantum-feature`)
3. Add tests and documentation
4. Submit a pull request

---

## 📞 Support

- 📖 Check the [Qiskit Documentation](https://qiskit.org/)
- 💬 Open an [Issue](https://github.com/KamdemSamuel/quantum-computing-qiskit/issues)
- 🌐 Join the [Qiskit Community](https://qiskit.org/community)

---

*Last Updated: May 2026*
