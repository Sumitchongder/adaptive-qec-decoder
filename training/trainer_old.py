"""
Neural decoder trainer.
"""

from pathlib import Path

import torch
from torch.utils.data import DataLoader, random_split

from decoder.neural.dataset import QECDataset
from decoder.neural.model import SyndromeDecoder

from training.metrics import classification_accuracy
from training.history import TrainingHistory
from training.checkpoint import CheckpointManager
from training.scheduler import build_scheduler
from training.early_stopping import EarlyStopping


class Trainer:

    def __init__(
        self,
        dataset_path,
        batch_size=64,
        epochs=20,
        learning_rate=1e-3,
        checkpoint_directory="checkpoints/neural",
        history_file="results/training/history.csv",
    ):

        self.device = torch.device(
            "cuda" if torch.cuda.is_available() else "cpu"
        )

        self.dataset = QECDataset(dataset_path)

        train_size = int(0.8 * len(self.dataset))
        validation_size = len(self.dataset) - train_size

        train_dataset, validation_dataset = random_split(
            self.dataset,
            [train_size, validation_size],
        )

        self.train_loader = DataLoader(
            train_dataset,
            batch_size=batch_size,
            shuffle=True,
        )

        self.validation_loader = DataLoader(
            validation_dataset,
            batch_size=batch_size,
            shuffle=False,
        )

        input_dim = self.dataset.syndromes.shape[1]
        output_dim = 2

        self.model = SyndromeDecoder(
            input_dim=input_dim,
            output_dim=output_dim,
        ).to(self.device)

        self.loss_fn = torch.nn.CrossEntropyLoss()

        self.optimizer = torch.optim.Adam(
            self.model.parameters(),
            lr=learning_rate,
        )

        self.scheduler = build_scheduler(self.optimizer)

        self.history = TrainingHistory()

        self.checkpoints = CheckpointManager(
            directory=checkpoint_directory,
        )

        self.early_stopping = EarlyStopping()

        self.epochs = epochs

        self.history_file = history_file

    def train(self):

        best_loss = float("inf")

        for epoch in range(self.epochs):

            #############################
            # Training
            #############################

            self.model.train()

            train_loss = 0.0
            train_acc = 0.0

            for x, y in self.train_loader:

                x = x.to(self.device)
                y = y.squeeze().to(self.device)

                logits = self.model(x)

                loss = self.loss_fn(logits, y)

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                train_loss += loss.item()

                train_acc += classification_accuracy(
                    logits,
                    y,
                )

            train_loss /= len(self.train_loader)
            train_acc /= len(self.train_loader)

            #############################
            # Validation
            #############################

            self.model.eval()

            val_loss = 0.0
            val_acc = 0.0

            with torch.no_grad():

                for x, y in self.validation_loader:

                    x = x.to(self.device)
                    y = y.squeeze().to(self.device)

                    logits = self.model(x)

                    loss = self.loss_fn(logits, y)

                    val_loss += loss.item()

                    val_acc += classification_accuracy(
                        logits,
                        y,
                    )

            val_loss /= len(self.validation_loader)
            val_acc /= len(self.validation_loader)

            self.scheduler.step(val_loss)

            self.history.add(
                epoch=epoch,
                train_loss=train_loss,
                train_accuracy=train_acc,
                validation_loss=val_loss,
                validation_accuracy=val_acc,
            )

            print(
                f"Epoch {epoch+1:3d} | "
                f"Train Loss {train_loss:.4f} | "
                f"Val Loss {val_loss:.4f} | "
                f"Train Acc {train_acc:.4f} | "
                f"Val Acc {val_acc:.4f}"
            )

            if val_loss < best_loss:

                best_loss = val_loss

                self.checkpoints.save(
                    self.model,
                    self.optimizer,
                    epoch,
                    val_loss,
                )

            if self.early_stopping.step(val_loss):

                print("\nEarly stopping")
                break

        self.history.save(
            self.history_file,
        )
