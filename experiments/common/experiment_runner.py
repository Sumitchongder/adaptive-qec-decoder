"""
Generic Experiment Runner
=========================

Reusable experiment runner for all publication experiments.

This module executes

- circuit generation
- syndrome sampling
- decoding
- evaluation
- runtime measurement

Author:
NVIDIA_QEC_Project

"""
from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))

import copy
import time

import numpy as np
import pandas as pd
import yaml

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator
from decoder.pymatching.decoder import PyMatchingDecoder
from evaluation.logical_error import LogicalErrorEvaluator

class ExperimentRunner:

    def __init__(

        self,

        config_path="configs/default.yaml",

    ):

        self.config_path = Path(config_path)

        with open(self.config_path) as f:

            self.base_config = yaml.safe_load(f)

    def create_config(

        self,

        distance,

        noise,

        shots,

    ):

        config = copy.deepcopy(self.base_config)

        config["surface_code"]["distance"] = distance

        config["surface_code"]["rounds"] = distance

        config["noise"]["depolarizing_probability"] = noise

        config["experiment"]["shots"] = shots

        return config

    def run_once(

        self,

        distance,

        noise,

        shots,

    ):

        """
        Execute one experiment.

        Returns
        -------
        dict
            Metrics for one experiment.
        """

        config = self.create_config(

            distance=distance,

            noise=noise,

            shots=shots,

        )

        temporary_config = Path("configs/_temporary_publication.yaml")

        with open(temporary_config, "w") as f:

            yaml.safe_dump(config, f)

        generator = CircuitGenerator(str(temporary_config))

        circuit = generator.generate()

        dem = circuit.detector_error_model()

        syndrome_generator = SyndromeGenerator(circuit)

        decoder = PyMatchingDecoder(dem)

        evaluator = LogicalErrorEvaluator()

        detectors = circuit.num_detectors

        observables = circuit.num_observables

        operations = len(str(circuit).splitlines())

        start = time.perf_counter()

        detector_events, logical_values = syndrome_generator.sample(

            shots

        )

        predictions = decoder.decode(detector_events)

        runtime = time.perf_counter() - start

        throughput = shots / runtime

        results = evaluator.evaluate(

            predictions,

            logical_values,

        )

        results["distance"] = distance

        results["noise"] = noise

        results["runtime"] = runtime

        results["throughput"] = throughput

        results["detectors"] = detectors

        results["observables"] = observables

        results["operations"] = operations

        return results



