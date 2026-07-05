import numpy
import scipy
import pandas
import matplotlib
import sklearn
import networkx
import h5py
import yaml
import joblib
import tqdm

print("=" * 60)
print("Scientific Stack Verification")
print("=" * 60)

packages = [
    ("NumPy", numpy.__version__),
    ("SciPy", scipy.__version__),
    ("Pandas", pandas.__version__),
    ("Matplotlib", matplotlib.__version__),
    ("Scikit-Learn", sklearn.__version__),
    ("NetworkX", networkx.__version__),
    ("H5Py", h5py.__version__),
    ("PyYAML", yaml.__version__),
    ("Joblib", joblib.__version__),
]

for name, version in packages:
    print(f"{name:<18}: {version}")

print("\n✓ Scientific stack installed successfully.")
