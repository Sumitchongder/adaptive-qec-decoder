"""
Logical Error Evaluation
========================

Computes logical error rate of a decoder.

Author:
NVIDIA_QEC_Project
"""

import numpy as np


class LogicalErrorEvaluator:

    def __init__(self):
        pass

    def evaluate(
        self,
        predictions,
        observables,
    ):

        predictions = np.asarray(predictions).astype(bool)

        observables = np.asarray(observables).astype(bool)

        total_shots = len(observables)

        correct = np.sum(
            np.all(predictions == observables, axis=1)
        )

        incorrect = total_shots - correct

        logical_error_rate = incorrect / total_shots

        accuracy = correct / total_shots

        return {
            "shots": int(total_shots),
            "correct": int(correct),
            "incorrect": int(incorrect),
            "logical_error_rate": float(logical_error_rate),
            "accuracy": float(accuracy),
        }
