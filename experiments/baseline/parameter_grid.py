"""
Parameter Grid Generator
"""

from itertools import product

import yaml


class ParameterGrid:

    def __init__(self, config_path):

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

    def generate(self):

        distances = self.config["surface_code"]["distances"]

        probabilities = self.config["noise"]["probabilities"]

        parameters = []

        for d, p in product(distances, probabilities):

            parameters.append({

                "distance": d,

                "noise": p,

                "shots":
                    self.config["simulation"]["shots"]

            })

        return parameters
