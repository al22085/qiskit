import os
from dotenv import load_dotenv
from qiskit_ibm_runtime import QiskitRuntimeService
load_dotenv()
service = QiskitRuntimeService(channel="ibm_quantum", token=os.getenv("IBM_QUANTUM_TOKEN"))