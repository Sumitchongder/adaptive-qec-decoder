"""
Experiment Runner
=================

Centralized experiment execution engine.

Every experiment in the project should use this class.

Author:
NVIDIA_QEC_Project
"""

from time import perf_counter

from simulator.circuit_generator import CircuitGenerator
from simulator.syndrome_generator import SyndromeGenerator

from decoder.pymatching.decoder import PyMatchingDecoder

from evaluation.logical_error import LogicalErrorEvaluator


class ExperimentRunner:

    def __init__(self):
        self.evaluator = LogicalErrorEvaluator()

    def run(
        self,
        distance,
        rounds,
        noise_probability,
        shots,
    ):
        """
        Executes one complete experiment.

        Returns
        -------
        dict
            Dictionary containing all measured metrics.
        """

        generator = CircuitGenerator(
            distance=distance,
            rounds=rounds,
            noise_probability=noise_probability,
        )

        circuit = generator.generate()

        dem = circuit.detector_error_model()

        syndrome_generator = SyndromeGenerator(circuit)

        detectors, observables = syndrome_generator.sample(
            shots
        )

        decoder = PyMatchingDecoder(dem)

        start = perf_counter()

        predictions = decoder.decode(detectors)

        runtime = perf_counter() - start

        results = self.evaluator.evaluate(
            predictions,
            observables,
        )

        results["distance"] = distance
        results["rounds"] = rounds
        results["noise_probability"] = noise_probability
        results["runtime_seconds"] = runtime
        results["throughput"] = shots / runtime

        return results
