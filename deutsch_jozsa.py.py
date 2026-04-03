from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
def constant_oracle(n):
    qc = QuantumCircuit(n + 1)
    return qc
def balanced_oracle(n):
    qc = QuantumCircuit(n + 1)
    for i in range(n):
        qc.cx(i, n)
    return qc
def deutsch_jozsa(oracle, n):
    qc = QuantumCircuit(n + 1, n)

    qc.x(n)
    qc.h(n)
    for i in range(n):
        qc.h(i)

    qc = qc.compose(oracle)

    for i in range(n):
        qc.h(i)
    
    for i in range(n):
        qc.measure(i, i)

    return qc
n = 4
oracle = constant_oracle(n)  
dj = deutsch_jozsa(oracle, n)
backend = Aer.get_backend("qasm_simulator")
job = backend.run(transpile(dj, backend), shots=1024)
result = job.result().get_counts()
print(result)
plot_histogram(result)
plt.show()