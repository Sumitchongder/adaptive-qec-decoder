"""
Checkpoint utilities.
"""

from pathlib import Path
import torch


class CheckpointManager:

    def __init__(self, directory="checkpoints/neural"):

        self.directory = Path(directory)

        self.directory.mkdir(parents=True, exist_ok=True)

    def save(

        self,

        model,

        optimizer,

        epoch,

        loss,

        filename="best_model.pt",

    ):

        torch.save(

            {

                "epoch": epoch,

                "model_state_dict": model.state_dict(),

                "optimizer_state_dict": optimizer.state_dict(),

                "loss": loss,

            },

            self.directory / filename,

        )
