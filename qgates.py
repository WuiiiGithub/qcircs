from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Quantum AND gate
def qand(qc,input_registers,output_register):
    if isinstance(input_registers, int):
        input_registers=[input_registers]
    if isinstance(output_register, int): 
        output_register=[output_register]
    if isinstance(input_registers, range):
        input_registers=list(input_registers)
    if isinstance(output_register, range):
        output_register=list(output_register)
    if len(output_register)!=1:
        raise ValueError(f"Expected 1 output register. But, {len(output_register)} given.")
    qc.barrier()
    qc.mcx(input_registers,output_register)
    qc.barrier()

# Quantum OR Gate
def qor(qc,input_registers,output_register):
    if isinstance(input_registers, int):
        input_registers=[input_registers]
    if isinstance(output_register, int): 
        output_register=[output_register]
    if isinstance(input_registers, range):
        input_registers=list(input_registers)
    if isinstance(output_register, range):
        output_register=list(output_register)
    if len(output_register)!=1:
        raise ValueError(f"Expected 1 output register. But, {len(output_register)} given.")
    qc.barrier()
    qc.x(input_registers)
    qc.mcx(input_registers,output_register)
    qc.x(output_register)
    qc.barrier()

#Quantum XOR gate
def qxor(qc,input_registers,output_register):
    if isinstance(input_registers, int):
        input_registers=[input_registers]
    if isinstance(output_register, int): 
        output_register=[output_register]
    if isinstance(input_registers, range):
        input_registers=list(input_registers)
    if isinstance(output_register, range):
        output_register=list(output_register)
    if len(output_register)!=1:
        raise ValueError(f"Expected 1 output register. But, {len(output_register)} given.")
    qc.barrier()
    for i in input_registers:
        qc.cx(i,output_register)
    qc.barrier()

#Quantum Random Number Generator
def qrand(n):
    qc=QuantumCircuit(n,n)
    qc.h(range(n))
    qc.measure(range(n),range(n))
    return AerSimulator().run(qc,shots=1,memory=True).result().get_memory()[0]
