from pathlib import Path
import json
import numpy as np

dataset = Path("datasets/processed/surface_d3_r3_p1e-03_100shots.npz")

data = np.load(dataset, allow_pickle=True)

print("="*70)
print("DATASET INSPECTION")
print("="*70)

print()

for key in data.files:
    print(key)

print()

print("Syndromes Shape")
print(data["syndromes"].shape)

print()

print("Labels Shape")
print(data["labels"].shape)

print()

print("Observables Shape")
print(data["observables"].shape)

print()

metadata = json.loads(str(data["metadata"]))

print("Metadata")

for k, v in metadata.items():
    print(f"{k:20s}: {v}")
