"""
Confidence Estimator
====================

Transforms syndrome statistics into calibrated confidence scores.

Author:
NVIDIA_QEC_Project
"""

from __future__ import annotations

import numpy as np

from decoder.confidence.statistics import ConfidenceStatistics


class ConfidenceEstimator:
    """
    Estimate decoder confidence from syndrome statistics.

    Confidence ranges from

        0.0 (very uncertain)

    to

        1.0 (very confident)

    This implementation is intentionally modular so
    future work can replace the heuristic model with
    a learned confidence predictor.
    """

    def __init__(

        self,

        alpha=2.5,

        beta=1.2,

        gamma=2.0,

    ):

        self.alpha = alpha
        self.beta = beta
        self.gamma = gamma

    @staticmethod
    def sigmoid(x):

        return 1.0 / (

            1.0 +

            np.exp(-x)

        )

    def confidence(

        self,

        detectors,

    ):

        detectors = np.asarray(detectors)

        weight = ConfidenceStatistics.normalized_weight(detectors)

        density = ConfidenceStatistics.detector_density(detectors)

        entropy = ConfidenceStatistics.entropy(detectors)

        score = (

            self.alpha * (1.0 - weight)

            +

            self.beta * (1.0 - density)

            +

            self.gamma * (1.0 - entropy)

        )

        confidence = self.sigmoid(score)

        return np.clip(

            confidence,

            0.0,

            1.0,

        )

    def summary(

        self,

        detectors,

    ):

        confidence = self.confidence(detectors)

        return {

            "mean": float(np.mean(confidence)),

            "median": float(np.median(confidence)),

            "std": float(np.std(confidence)),

            "min": float(np.min(confidence)),

            "max": float(np.max(confidence)),

        }
