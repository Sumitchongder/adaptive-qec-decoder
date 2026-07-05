import stim
import pymatching
import sinter
import qiskit
import qiskit_aer

print("=" * 60)
print("Quantum Error Correction Stack Verification")
print("=" * 60)

packages = [
    ("Stim", stim.__version__),
    ("PyMatching", pymatching.__version__),
    ("sinter", sinter.__version__),
    ("Qiskit", qiskit.__version__),
    ("Qiskit Aer", qiskit_aer.__version__),
]

for name, version in packages:
    print(f"{name:<20}: {version}")

print("\n✓ QEC stack installed successfully.")
