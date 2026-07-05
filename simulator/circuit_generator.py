"""
Circuit Generator
=================

Generates Stim surface-code memory circuits from a YAML configuration.

Author:
NVIDIA_QEC_Project

"""

from pathlib import Path
import yaml
import stim


class CircuitGenerator:
    """Generate surface-code circuits using Stim."""

    def __init__(self, config_path: str):

        self.config_path = Path(config_path)

        with open(self.config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def generate(self):

        distance = self.config["surface_code"]["distance"]
        rounds = self.config["surface_code"]["rounds"]
        p = self.config["noise"]["depolarizing_probability"]

        circuit = stim.Circuit.generated(
            "surface_code:rotated_memory_x",
            distance=distance,
            rounds=rounds,
            after_clifford_depolarization=p,
        )

        return circuit

    def detector_error_model(self):

        circuit = self.generate()

        return circuit.detector_error_model()

    def save_metadata(self):

        metadata = {
            "distance": self.config["surface_code"]["distance"],
            "rounds": self.config["surface_code"]["rounds"],
            "noise_probability": self.config["noise"]["depolarizing_probability"],
        }

        return metadata
