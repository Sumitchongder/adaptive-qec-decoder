"""
Production Experiment Runner

Runs every parameter combination and stores the results.

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path
import sys

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

from decoder.pymatching.decoder import PyMatchingDecoder

from evaluation.logical_error import LogicalErrorEvaluator


class ExperimentRunner:

    def __init__(self):

        self.evaluator = LogicalErrorEvaluator()

    def run_single(
        self,
        distance,
        noise,
        shots,
    ):

        generator = CircuitGenerator(
            "configs/default.yaml"
        )

        generator.config["surface_code"]["distance"] = distance

        generator.config["surface_code"]["rounds"] = distance

        generator.config["noise"][
            "depolarizing_probability"
        ] = noise

        generator.config["experiment"]["shots"] = shots

        circuit = generator.generate()

        syndrome_generator = SyndromeGenerator(
            circuit
        )

        detectors, observables = syndrome_generator.sample(
            shots
        )

        dem = circuit.detector_error_model()

        decoder = PyMatchingDecoder(
            dem
        )

        predictions = decoder.decode(
            detectors
        )

        results = self.evaluator.evaluate(
            predictions,
            observables,
        )

        results["distance"] = distance

        results["noise"] = noise

        return results

    def run_grid(
        self,
        parameters,
    ):

        rows = []

        total = len(parameters)

        for index, p in enumerate(parameters, start=1):

            print()

            print("=" * 70)

            print(
                f"Experiment {index}/{total}"
            )

            print("=" * 70)

            print(
                f"Distance : {p['distance']}"
            )

            print(
                f"Noise    : {p['noise']}"
            )

            print(
                f"Shots    : {p['shots']}"
            )

            result = self.run_single(
                p["distance"],
                p["noise"],
                p["shots"],
            )

            rows.append(result)

            print()

            print(result)

        dataframe = pd.DataFrame(rows)

        return dataframe
