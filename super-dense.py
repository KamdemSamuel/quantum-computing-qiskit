import qiskit as q
from qiskit_aer import QasmSimulator

simulator = QasmSimulator()

#B) Construction du circuit
circuit = q.QuantumCircuit(2,2)

#B.1) preparation de l'etat de BEll
circuit.h(0)
circuit.cx(0,1)

message_alice = '01' #message de alice

#B.2) porte d'alice selon le message transmise
if message_alice == '00':
    circuit.iden(0) #identiter
elif message_alice == '01':
    circuit.z(0) #porte Z
elif message_alice == '10':
    circuit.x(0) #porte X (NOT)
elif message_alice == '11':
    circuit.x(0)
    circuit.z(0)

#B.3) decodage
circuit.cx(0,1)
circuit.h(0)

#B.4) mesures
circuit.measure([0,1], [0,1])

print(circuit.draw(output='text'))

#C)execution
#lancer la simulation de 1000
tcircuit = q.transpile(circuit, simulator)
job = simulator.run(tcircuit, shots=1000)

#D) resulat

result = job.result()

#comptage
counts = result.get_counts(tcircuit)
print("Nombre de '00, '01' '10' '11' :", counts)

circuit.draw(output='mpl').savefig('circuit_teleportation.png')
