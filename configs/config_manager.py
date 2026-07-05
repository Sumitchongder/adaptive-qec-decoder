"""
Configuration Manager
=====================

Loads, validates, updates and saves YAML configurations.

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path
import copy
import yaml


class ConfigManager:

    def __init__(self, config_path):

        self.config_path = Path(config_path)

        with open(self.config_path, "r") as f:
            self._config = yaml.safe_load(f)

    def get_config(self):
        return copy.deepcopy(self._config)

    def update(
        self,
        distance=None,
        rounds=None,
        noise=None,
        shots=None,
    ):

        config = self.get_config()

        if distance is not None:
            config["surface_code"]["distance"] = distance

        if rounds is not None:
            config["surface_code"]["rounds"] = rounds

        if noise is not None:
            config["noise"]["depolarizing_probability"] = noise

        if shots is not None:
            config["experiment"]["shots"] = shots

        return config

    def save(self, config, output_file):

        output_file = Path(output_file)

        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        with open(output_file, "w") as f:
            yaml.safe_dump(
                config,
                f,
                sort_keys=False,
            )

        return output_file
