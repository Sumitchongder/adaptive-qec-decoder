from pathlib import Path
import json
import numpy as np

import torch
from torch.utils.data import Dataset


class QECDataset(Dataset):

    def __init__(self, dataset_path):

        dataset_path = Path(dataset_path)

        data = np.load(dataset_path, allow_pickle=True)

        self.syndromes = data["syndromes"].astype(np.float32)
        self.labels = data["labels"].astype(np.int64)

        self.metadata = json.loads(str(data["metadata"]))

    def __len__(self):

        return len(self.syndromes)

    def __getitem__(self, idx):

        x = torch.tensor(self.syndromes[idx])

        y = torch.tensor(self.labels[idx])

        return x, y
