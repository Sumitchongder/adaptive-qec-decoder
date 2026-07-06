"""
Generic Experiment Runner

Runs one complete decoding experiment.

Author:
NVIDIA_QEC_Project
"""

from __future__ import annotations

import time
import statistics

import yaml

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

from decoder.pymatching.decoder import PyMatchingDecoder

from evaluation.logical_error import LogicalErrorEvaluator

from experiments.framework.result import ExperimentResult


class ExperimentRunner:

    def __init__(self, config_file):

        self.config_file = config_file

    def update_yaml(
        self,
        distance,
        noise,
        shots,
    ):

        with open(self.config_file, "r") as f:

            cfg = yaml.safe_load(f)

        cfg["surface_code"]["distance"] = distance
        cfg["surface_code"]["rounds"] = distance

        cfg["noise"]["depolarizing_probability"] = noise

        cfg["experiment"]["shots"] = shots

        with open(self.config_file, "w") as f:

            yaml.safe_dump(cfg, f)

    def single_run(
        self,
        distance,
        noise,
        shots,
    ):

        self.update_yaml(
            distance,
            noise,
            shots,
        )

        generator = CircuitGenerator(self.config_file)

        circuit = generator.generate()

        syndrome = SyndromeGenerator(circuit)

        dem = generator.detector_error_model()

        decoder = PyMatchingDecoder(dem)

        evaluator = LogicalErrorEvaluator()

        start = time.perf_counter()

        detectors, observables = syndrome.sample(shots)

        prediction = decoder.decode(detectors)

        runtime = time.perf_counter() - start

        metrics = evaluator.evaluate(
            prediction,
            observables,
        )

        throughput = shots / runtime

        return ExperimentResult(

            distance=distance,

            noise=noise,

            runtime=runtime,

            throughput=throughput,

            accuracy=metrics["accuracy"],

            logical_error=metrics["logical_error_rate"],

            detectors=circuit.num_detectors,

            observables=circuit.num_observables,

            operations=len(str(circuit).splitlines()),

            correct=metrics["correct"],

            incorrect=metrics["incorrect"],
        )

    def repeat(
        self,
        distance,
        noise,
        shots,
        repeats,
    ):

        runs = []

        for _ in range(repeats):

            runs.append(

                self.single_run(
                    distance,
                    noise,
                    shots,
                )

            )

        runtime = statistics.mean(
            r.runtime for r in runs
        )

        runtime_std = statistics.stdev(
            r.runtime for r in runs
        )

        accuracy = statistics.mean(
            r.accuracy for r in runs
        )

        accuracy_std = statistics.stdev(
            r.accuracy for r in runs
        )

        logical = statistics.mean(
            r.logical_error for r in runs
        )

        logical_std = statistics.stdev(
            r.logical_error for r in runs
        )

        throughput = statistics.mean(
            r.throughput for r in runs
        )

        throughput_std = statistics.stdev(
            r.throughput for r in runs
        )

        return {

            "distance": distance,

            "noise": noise,

            "shots": shots,

            "mean_runtime": runtime,

            "std_runtime": runtime_std,

            "mean_accuracy": accuracy,

            "std_accuracy": accuracy_std,

            "mean_logical_error": logical,

            "std_logical_error": logical_std,

            "mean_throughput": throughput,

            "std_throughput": throughput_std,

            "detectors": runs[0].detectors,

            "observables": runs[0].observables,

            "operations": runs[0].operations,

        }
