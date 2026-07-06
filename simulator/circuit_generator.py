"""
Stim Circuit Generator

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

import yaml
import stim


class CircuitGenerator:

    def __init__(self, config_path="configs/default.yaml"):

        self.config_path = Path(config_path)

        with open(self.config_path) as f:

            self.config = yaml.safe_load(f)

    def generate(

        self,

        distance=None,

        rounds=None,

        noise=None,

    ):

        if distance is None:

            distance = self.config["surface_code"]["distance"]

        if rounds is None:

            rounds = self.config["surface_code"]["rounds"]

        if noise is None:

            noise = self.config["noise"]["depolarizing_probability"]

        circuit = stim.Circuit.generated(

            "surface_code:rotated_memory_x",

            distance=distance,

            rounds=rounds,

            after_clifford_depolarization=noise,

        )

        return circuit

    def detector_error_model(

        self,

        distance=None,

        rounds=None,

        noise=None,

    ):

        return self.generate(

            distance,

            rounds,

            noise,

        ).detector_error_model()
