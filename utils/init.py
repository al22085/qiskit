# First, import all the necessary python modules
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Math
from scipy.optimize import minimize, Bounds
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister, transpile
from qiskit.visualization import plot_distribution, plot_histogram
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as IBMSampler
from qiskit_ibm_runtime.accounts import AccountNotFoundError
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import SamplerV2 as LocalSampler
# qc_workbook is the original module written for this workbook
# If you encounter an ImportError, edit the environment variable PYTHONPATH or sys.path
from external.qc_workbook.source.qc_workbook.utils import operational_backend, find_best_chain
from external.qc_workbook.source.qc_workbook.show_state import statevector_expr
from external.qc_workbook.source.qc_workbook.optimized_additions import optimized_additions

print('notebook ready')

from utils.init_token import service
print('token ready')

simulator = AerSimulator()
sampler = LocalSampler()
print('local simulator ready')
print(simulator.name)