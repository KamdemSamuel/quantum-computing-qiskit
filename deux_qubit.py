"""
Bell State Circuit Implementation
Demonstrates quantum entanglement using two qubits
"""

import qiskit as q
from qiskit_aer import QasmSimulator
import matplotlib.pyplot as plt

def create_bell_state_circuit():
    """
    Create a Bell state (maximally entangled state).
    
    The circuit creates the Bell state |Φ+⟩ = (|00⟩ + |11⟩) / √2
    
    Circuit operations:
    1. H(q0) - Hadamard gate on first qubit (creates superposition)
    2. CX(q0, q1) - CNOT gate (creates entanglement)
    3. Measure both qubits
    
    Expected Results:
    - 50% |00⟩ (both qubits 0)
    - 50% |11⟩ (both qubits 1)
    - Never |01⟩ or |10⟩ (demonstrates entanglement!)
    
    Returns:
        QuantumCircuit: A Bell state circuit with measurements
    """
    simulator = QasmSimulator()
    
    # Create quantum circuit with 2 qubits and 2 classical bits
    circuit = q.QuantumCircuit(2, 2)
    
    # Apply Hadamard to first qubit (create superposition)
    circuit.h(0)
    
    # Apply CNOT gate (create entanglement)
    circuit.cx(0, 1)
    
    # Measure both qubits
    circuit.measure([0, 1], [0, 1])
    
    return circuit, simulator


def run_bell_state():
    """
    Run the Bell state circuit and display results.
    """
    # Create circuit
    circuit, simulator = create_bell_state_circuit()
    
    # Display circuit
    print("="*60)
    print("BELL STATE CIRCUIT")
    print("="*60)
    print(circuit.draw(output='text'))
    print("\n")
    
    # Transpile and execute circuit
    tcircuit = q.transpile(circuit, simulator)
    job = simulator.run(tcircuit, shots=1000)
    
    # Get results
    result = job.result()
    counts = result.get_counts(tcircuit)
    
    # Display measurement results
    print("Measurement Results (1000 shots):")
    print("-" * 40)
    for state in ['00', '01', '10', '11']:
        count = counts.get(state, 0)
        percentage = 100 * count / 1000
        print(f"  |{state}⟩: {count:4d} counts ({percentage:5.1f}%)")
    
    print("\n" + "="*60)
    print("ANALYSIS")
    print("="*60)
    print("✓ Expected: ~50% |00⟩ and ~50% |11⟩")
    print("✓ Measurements are perfectly correlated!")
    print("✓ This demonstrates QUANTUM ENTANGLEMENT")
    print("="*60 + "\n")
    
    # Visualize histogram
    print("Generating histogram visualization...")
    q.visualization.plot_histogram(counts)
    plt.title("Bell State Measurement Results (1000 shots)")
    plt.xlabel("Measurement Outcome")
    plt.ylabel("Count")
    plt.savefig('Figure_2.png', dpi=150, bbox_inches='tight')
    print("✓ Histogram saved as 'Figure_2.png'")
    
    # Save circuit diagram
    print("Generating circuit diagram...")
    circuit.draw(output='mpl').savefig('circuit_bell_state.png', dpi=150, bbox_inches='tight')
    print("✓ Circuit diagram saved as 'circuit_bell_state.png'")
    
    plt.show()


if __name__ == '__main__':
    run_bell_state()
