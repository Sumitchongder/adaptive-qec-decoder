"""
evaluation/evaluator.py

Evaluate a trained neural decoder.

Outputs:
    prediction
    confidence
    correctness
    inference latency

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path
import time

import pandas as pd
import torch
from torch.utils.data import DataLoader

from decoder.neural.dataset import QECDataset
from decoder.neural.model import SyndromeDecoder


class Evaluator:

    def __init__(
        self,
        dataset_path,
        checkpoint_path,
        batch_size=512,
    ):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.dataset = QECDataset(dataset_path)

        self.loader = DataLoader(
            self.dataset,
            batch_size=batch_size,
            shuffle=False,
        )

        input_dim = self.dataset.syndromes.shape[1]
        output_dim = 2

        self.model = SyndromeDecoder(
            input_dim=input_dim,
            output_dim=output_dim,
        ).to(self.device)

        checkpoint = torch.load(
            checkpoint_path,
            map_location=self.device,
        )

        self.model.load_state_dict(
            checkpoint["model_state_dict"]
        )

        self.model.eval()

    def evaluate(
        self,
        output_csv,
    ):

        records = []

        sample_index = 0

        with torch.no_grad():

            for x, y in self.loader:

                x = x.to(self.device)
                y = y.squeeze().to(self.device)

                start = time.perf_counter()

                logits = self.model(x)

                if self.device.type == "cuda":
                    torch.cuda.synchronize()

                elapsed = time.perf_counter() - start

                probabilities = torch.softmax(
                    logits,
                    dim=1,
                )

                confidence, prediction = torch.max(
                    probabilities,
                    dim=1,
                )

                latency_us = (
                    elapsed
                    * 1e6
                    / len(prediction)
                )

                for i in range(len(prediction)):

                    records.append({

                        "sample": sample_index,

                        "truth": int(y[i]),

                        "prediction": int(prediction[i]),

                        "confidence": float(confidence[i]),

                        "correct": int(
                            prediction[i] == y[i]
                        ),

                        "latency_us": latency_us,

                    })

                    sample_index += 1

        df = pd.DataFrame(records)

        output_csv = Path(output_csv)

        output_csv.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_csv(
            output_csv,
            index=False,
        )

        accuracy = df["correct"].mean()

        throughput = len(df) / (
            df["latency_us"].sum() / 1e6
        )

        summary = {

            "samples": len(df),

            "accuracy": accuracy,

            "avg_confidence": df["confidence"].mean(),

            "avg_latency_us": df["latency_us"].mean(),

            "throughput_samples_per_sec": throughput,

        }

        print()

        print("=" * 60)
        print("Evaluation Summary")
        print("=" * 60)

        for k, v in summary.items():
            print(f"{k:30s}: {v}")

        return df
