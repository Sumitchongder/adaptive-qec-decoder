"""
Benchmark neural decoder throughput.
"""

import time
from pathlib import Path

import pandas as pd
import torch

from decoder.neural.dataset import QECDataset
from decoder.neural.model import SyndromeDecoder


DATASET = "datasets/processed/surface_d7_r7_p1e-03_50000shots.npz"
MODEL = "checkpoints/neural/d7/best_model.pt"


def benchmark(batch_size):

    dataset = QECDataset(DATASET)

    x = torch.tensor(dataset.syndromes)

    device = torch.device(
        "cuda"
        if torch.cuda.is_available()
        else "cpu"
    )

    model = SyndromeDecoder(
        input_dim=x.shape[1],
        output_dim=2,
    ).to(device)

    checkpoint = torch.load(
        MODEL,
        map_location=device,
    )

    model.load_state_dict(
        checkpoint["model_state_dict"]
    )

    model.eval()

    x = x.to(device)

    start = time.perf_counter()

    with torch.no_grad():

        for i in range(0, len(x), batch_size):

            model(x[i:i+batch_size])

    elapsed = time.perf_counter() - start

    throughput = len(x) / elapsed

    latency = elapsed / len(x) * 1e6

    memory_mb = 0

    if device.type == "cuda":

        memory_mb = (
            torch.cuda.max_memory_allocated(device)
            / 1024**2
        )

    return {

        "batch_size": batch_size,
        "device": device.type.upper(),
        "samples": len(x),
        "throughput": throughput,
        "latency_us": latency,
        "memory_mb": memory_mb,

    }


rows = []

for bs in [

    1,
    8,
    16,
    32,
    64,
    128,
    256,
    512,

]:

    rows.append(
        benchmark(bs)
    )

df = pd.DataFrame(rows)

Path("results/throughput").mkdir(
    parents=True,
    exist_ok=True,
)

df.to_csv(

    "results/throughput/throughput.csv",

    index=False,

)

print(df)
