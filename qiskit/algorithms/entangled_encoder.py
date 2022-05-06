from qiskit import QuantumCircuit
from qiskit import Aer
from copy import deepcopy

def encode(qc, msg):
    qc_alice = deepcopy(qc)
    
    # Alice entangling and encoding
    qc_alice.h(1)
    qc_alice.cx(1,0)
    if msg[0] == 1:
        qc_alice.z(1)
    if msg[1] == 1:
        qc_alice.x(1)
        
    # Bob decoding and untangling
    qc_bob = QuantumCircuit(2,2)
    qc_bob.cx(1,0)
    qc_bob.h(1)
    qc_bob.measure([0,1],[0,1])
    
    # Running the simulation
    backend = Aer.get_backend('aer_simulator')
    print(backend.run(qc_alice.compose(qc_bob)).result().get_counts())

if __name__=="__main__":
    # Let's build a quantum circuit first
    qc = QuantumCircuit(2,2)
    msg = ['00','01','10','11']
    for i in range(4):
        encode(qc, msg[i])