import qiskit as q
from qiskit_aer import QasmSimulator
import matplotlib.pyplot as plt
import numpy as np

simulator = QasmSimulator()

circuit = q.QuantumCircuit(2,2)

circuit.h(0)
circuit.x(1)
circuit.cx(0,1)
circuit.h(1)
circuit.measure([0,1], [0,1])

#Affichage graphique du circuit
img_circuit = circuit.draw(output='mpl')
img_circuit.show()

#execution
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit, shots=1000)

#resultat et visualization
result = job.result()
counts = result.get_counts(tcircuit)
print("Nombre de '00', '01', '10', '11' :", counts)

#Diagramme en barre
q.visualization.plot_histogram(counts)
plt.show()

circuit.draw(output='mpl').savefig('circuit_bell_state.png')
