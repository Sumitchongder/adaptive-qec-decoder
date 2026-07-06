"""
Training history.
"""

from pathlib import Path
import pandas as pd


class TrainingHistory:

    def __init__(self):

        self.records = []

    def add(

        self,

        epoch,

        train_loss,

        train_accuracy,

        validation_loss,

        validation_accuracy,

    ):

        self.records.append({

            "epoch": epoch,

            "train_loss": train_loss,

            "train_accuracy": train_accuracy,

            "validation_loss": validation_loss,

            "validation_accuracy": validation_accuracy,

        })

    def save(

        self,

        filename,

    ):

        filename = Path(filename)

        filename.parent.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(self.records)

        df.to_csv(filename, index=False)
