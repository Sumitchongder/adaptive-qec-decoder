from torch.utils.data import DataLoader

from decoder.neural.dataset import QECDataset

dataset = QECDataset(
    "datasets/processed/surface_d3_r3_p1e-03_100shots.npz"
)

print(dataset.metadata)

loader = DataLoader(
    dataset,
    batch_size=8,
    shuffle=True,
)

x, y = next(iter(loader))

print()

print("Batch X")

print(x.shape)

print()

print("Batch Y")

print(y.shape)
