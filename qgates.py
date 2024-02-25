from qiskit import QuantumCircuit
#Added Classical Gate OR, AND and XOR using Quantum Gates

def qnot(qc,input_registers):
  qc.x(input_register)

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
