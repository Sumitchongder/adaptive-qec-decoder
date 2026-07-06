"""
Research Dataset Builder
========================

Generates supervised datasets for adaptive QEC decoding.

Outputs
-------
Compressed .npz dataset containing

    syndromes
    labels
    observables
    metadata

Author:
NVIDIA_QEC_Project
"""

from __future__ import annotations

from pathlib import Path
from datetime import datetime
import json

import numpy as np

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator
from decoder.pymatching import LabelGenerator


class DatasetBuilder:

    def __init__(self, config_path="configs/default.yaml"):

        self.generator = CircuitGenerator(config_path)
        self.config = self.generator.config

    def build_dataset(
        self,
        output_directory="datasets/processed",
        dataset_name=None,
        distance=None,
        rounds=None,
        noise=None,
        shots=None,
    ):

        cfg = self.config

        distance = (
            distance
            if distance is not None
            else cfg["surface_code"]["distance"]
        )

        rounds = (
            rounds
            if rounds is not None
            else cfg["surface_code"]["rounds"]
        )

        noise = (
            noise
            if noise is not None
            else cfg["noise"]["depolarizing_probability"]
        )

        # Support both "experiment.shots" and "dataset.shots"
        if shots is None:
            if "dataset" in cfg and "shots" in cfg["dataset"]:
                shots = cfg["dataset"]["shots"]
            else:
                shots = cfg["experiment"]["shots"]

        if dataset_name is None:
            dataset_name = (
                f"surface_d{distance}"
                f"_r{rounds}"
                f"_p{noise:.0e}"
                f"_{shots}shots"
            )

        print("=" * 72)
        print("Generating Supervised Dataset")
        print("=" * 72)
        print(f"Distance : {distance}")
        print(f"Rounds   : {rounds}")
        print(f"Noise    : {noise}")
        print(f"Shots    : {shots}")
        print()

        circuit = self.generator.generate(
	    distance=distance,
	    rounds=rounds,
	    noise=noise,
        )

        detector_error_model = circuit.detector_error_model()

        syndrome_generator = SyndromeGenerator(circuit)

        syndromes, observables = syndrome_generator.sample(shots)

        print("Generating teacher labels using PyMatching...")

        label_generator = LabelGenerator(detector_error_model)

        labels = label_generator.generate_labels(syndromes)

        output_directory = Path(output_directory)

        output_directory.mkdir(parents=True, exist_ok=True)

        dataset_file = output_directory / f"{dataset_name}.npz"

        metadata = {

            "distance": distance,

            "rounds": rounds,

            "noise": noise,

            "shots": shots,

            "num_detectors": int(syndromes.shape[1]),

            "num_observables": int(observables.shape[1]),

            "generator": "Stim",

            "teacher": "PyMatching",

            "created": datetime.now().isoformat(),

            "project": "Latency-Constrained QEC Co-Design",

            "version": "0.1.0",

        }

        np.savez_compressed(

            dataset_file,

            syndromes=syndromes.astype(np.uint8),

            labels=labels.astype(np.uint8),

            observables=observables.astype(np.uint8),

            metadata=json.dumps(metadata),

        )

        print()
        print("=" * 72)
        print("Dataset Successfully Generated")
        print("=" * 72)
        print(f"Saved : {dataset_file}")
        print()
        print(f"Samples          : {len(syndromes)}")
        print(f"Detectors/sample : {syndromes.shape[1]}")
        print(f"Observables      : {observables.shape[1]}")
        print(f"Label Shape      : {labels.shape}")
        print()

        return dataset_file
