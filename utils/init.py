# First, import all the necessary python modules
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize, Bounds
from qiskit import QuantumCircuit, transpile
from qiskit.visualization import plot_distribution
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as IBMSampler
from qiskit_ibm_runtime.accounts import AccountNotFoundError
from qiskit_aer import AerSimulator
from qiskit_aer.primitives import SamplerV2 as LocalSampler
# qc_workbook is the original module written for this workbook
# If you encounter an ImportError, edit the environment variable PYTHONPATH or sys.path
from external.qc_workbook.source.qc_workbook.utils import operational_backend
print('notebook ready')

from utils.init_token import service
print('token ready')

simulator = AerSimulator()
sampler = LocalSampler()
print('local simulator ready')
print(simulator.name)