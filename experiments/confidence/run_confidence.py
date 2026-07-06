"""
Confidence Experiment
=====================

Generates confidence statistics for every decoded syndrome.

Outputs

results/confidence/confidence.csv

Author:
NVIDIA_QEC_Project
"""

from __future__ import annotations

import os
import time

import numpy as np
import pandas as pd

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

from decoder.pymatching.decoder import PyMatchingDecoder
from decoder.confidence.estimator import ConfidenceEstimator

from evaluation.logical_error import LogicalErrorEvaluator


OUTPUT_DIR = "results/confidence"


def ensure_directory():

    os.makedirs(

        OUTPUT_DIR,

        exist_ok=True,

    )


def main():

    ensure_directory()

    print("=" * 60)
    print("Confidence Experiment")
    print("=" * 60)

    generator = CircuitGenerator(

        "configs/default.yaml"

    )

    circuit = generator.generate()

    syndrome_generator = SyndromeGenerator(

        circuit

    )

    detector_error_model = generator.detector_error_model()

    decoder = PyMatchingDecoder(

        detector_error_model

    )

    estimator = ConfidenceEstimator()

    evaluator = LogicalErrorEvaluator()

    shots = generator.config["experiment"]["shots"]

    print(f"Shots : {shots}")

    print()

    start = time.perf_counter()

    detectors, observables = syndrome_generator.sample(

        shots

    )

    predictions = decoder.decode(

        detectors

    )

    runtime = time.perf_counter() - start

    metrics = evaluator.evaluate(

        predictions,

        observables,

    )

    confidence = estimator.confidence(

        detectors

    )

    weights = estimator.confidence(detectors)

    density = detectors.mean(axis=1)

    entropy = estimator.summary(detectors)

    correctness = np.all(

        predictions == observables,

        axis=1,

    ).astype(int)

    df = pd.DataFrame(

        {

            "confidence": confidence,

            "weight": detectors.sum(axis=1),

            "normalized_weight":

                detectors.sum(axis=1)

                / detectors.shape[1],

            "density": density,

            "correct": correctness,

        }

    )

    csv_file = os.path.join(

        OUTPUT_DIR,

        "confidence.csv",

    )

    df.to_csv(

        csv_file,

        index=False,

    )

    summary = pd.DataFrame(

        {

            "shots": [shots],

            "runtime": [runtime],

            "accuracy": [metrics["accuracy"]],

            "logical_error": [

                metrics["logical_error_rate"]

            ],

            "mean_confidence": [

                confidence.mean()

            ],

            "std_confidence": [

                confidence.std()

            ],

        }

    )

    summary.to_csv(

        os.path.join(

            OUTPUT_DIR,

            "confidence_summary.csv",

        ),

        index=False,

    )

    print()

    print("Saved")

    print(csv_file)

    print()

    print(summary)


if __name__ == "__main__":

    main()
