"""
Central experiment configuration.

Every experiment imports this file.
"""

from dataclasses import dataclass


@dataclass
class ExperimentConfig:

    distances = [3, 5, 7, 9, 11]

    noises = [
        1e-4,
        2e-4,
        5e-4,
        1e-3,
        2e-3,
        5e-3,
    ]

    shots = 5000

    repeats = 5

    random_seed = 42
