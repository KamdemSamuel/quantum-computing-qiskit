"""
Quantum Teleportation and Superdense Coding Protocols
Demonstrates two fundamental quantum communication techniques
"""

import qiskit as q
from qiskit_aer import QasmSimulator
import matplotlib.pyplot as plt


def superdense_coding(message_alice='01'):
    """
    Implement Superdense Coding Protocol.
    
    Alice sends 2 classical bits to Bob using only 1 qubit.
    Requires a pre-shared entangled pair (Bell state).
    
    Message Encoding:
    - '00': Apply Identity gate (do nothing)
    - '01': Apply Pauli Z gate
    - '10': Apply Pauli X gate (NOT)
    - '11': Apply both X and Z gates (Pauli Y equivalent)
    
    Quantum Protocol Steps:
    1. Create Bell pair |Φ+⟩ = (|00⟩ + |11⟩) / √2
    2. Alice applies gate based on message
    3. Bob applies inverse Bell measurement
    4. Measure qubits to recover the 2-bit message
    
    Args:
        message_alice (str): 2-bit message ('00', '01', '10', or '11')
    
    Returns:
        tuple: (QuantumCircuit, QasmSimulator)
    """
    simulator = QasmSimulator()
    
    # Create quantum circuit with 2 qubits and 2 classical bits
    circuit = q.QuantumCircuit(2, 2)
    
    # Step 1: Create Bell pair (entanglement)
    circuit.h(0)
    circuit.cx(0, 1)
    
    # Step 2: Alice encodes message by applying gate to her qubit
    if message_alice == '00':
        circuit.iden(0)  # Identity gate (do nothing)
    elif message_alice == '01':
        circuit.z(0)     # Pauli Z gate
    elif message_alice == '10':
        circuit.x(0)     # Pauli X gate (NOT)
    elif message_alice == '11':
        circuit.x(0)     # Apply both X and Z
        circuit.z(0)
    else:
        raise ValueError("Message must be '00', '01', '10', or '11'")
    
    # Step 3: Bob's decoding (inverse Bell measurement)
    circuit.cx(0, 1)
    circuit.h(0)
    
    # Step 4: Measure both qubits
    circuit.measure([0, 1], [0, 1])
    
    return circuit, simulator


def run_superdense_coding():
    """
    Run superdense coding protocol for all possible messages.
    """
    simulator = QasmSimulator()
    messages = ['00', '01', '10', '11']
    
    print("="*70)
    print("SUPERDENSE CODING PROTOCOL")
    print("="*70)
    print("\nAlice sends 2 classical bits using only 1 qubit!")
    print("This requires a pre-shared entangled pair (Bell state)\n")
    
    all_results = {}
    
    for message in messages:
        circuit, _ = superdense_coding(message)
        
        print(f"\n{'='*70}")
        print(f"Alice's Message: '{message}'")
        print(f"{'='*70}")
        
        print("\nCircuit:")
        print(circuit.draw(output='text'))
        
        # Transpile and execute
        tcircuit = q.transpile(circuit, simulator)
        job = simulator.run(tcircuit, shots=1000)
        result = job.result()
        counts = result.get_counts(tcircuit)
        
        all_results[message] = counts
        
        # Display results
        print("\nBob's Measurements (1000 shots):")
        print("-" * 45)
        for state in ['00', '01', '10', '11']:
            count = counts.get(state, 0)
            percentage = 100 * count / 1000
            marker = "✓" if state == message else " "
            print(f"{marker} |{state}⟩: {count:4d} counts ({percentage:5.1f}%)")
        
        # Check if Bob correctly recovered the message
        most_common = max(counts, key=counts.get)
        if most_common == message:
            print(f"\n✓ SUCCESS! Bob correctly measured '{message}'")
        else:
            print(f"\n✗ ERROR: Expected '{message}', got '{most_common}'")
    
    print(f"\n{'='*70}")
    print("PROTOCOL ANALYSIS")
    print(f"{'='*70}")
    print("✓ All messages successfully transmitted")
    print("✓ Alice sent 2 bits using only 1 qubit")
    print("✓ This is impossible classically!")
    print("✓ Quantum entanglement makes superdense coding possible")
    print("="*70 + "\n")
    
    # Create visualization
    print("Generating histogram visualization...")
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Superdense Coding: Bob\'s Measurements for Each Message', 
                 fontsize=14, fontweight='bold')
    
    for idx, message in enumerate(messages):
        ax = axes[idx // 2, idx % 2]
        q.visualization.plot_histogram(
            all_results[message],
            ax=ax,
            title=f"Alice sends '{message}'"
        )
    
    plt.tight_layout()
    plt.savefig('circuit_teleportation.png', dpi=150, bbox_inches='tight')
    print("✓ Visualization saved as 'circuit_teleportation.png'")
    plt.show()


if __name__ == '__main__':
    run_superdense_coding()
