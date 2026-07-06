from simulator.dataset_builder import DatasetBuilder
from training.trainer import Trainer
import yaml

with open("configs/experiments/d3.yaml") as f:
    cfg = yaml.safe_load(f)

builder = DatasetBuilder("configs/experiments/d3.yaml")
dataset_path = builder.build_dataset(
    output_directory="datasets/processed",
)

trainer = Trainer(
    dataset_path=str(dataset_path),
    batch_size=cfg["training"]["batch_size"],
    epochs=cfg["training"]["epochs"],
    learning_rate=cfg["training"]["learning_rate"],
)

trainer.train()
