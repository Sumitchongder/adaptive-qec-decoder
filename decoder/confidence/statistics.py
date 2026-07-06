"""
Confidence Statistics
=====================

Computes numerical confidence features from detector syndromes.

These features are later used by the adaptive decoder and for
publication-quality confidence analysis.

Author:
NVIDIA_QEC_Project
"""

from __future__ import annotations

import numpy as np


class ConfidenceStatistics:
    """
    Compute confidence-related statistics for syndrome patterns.
    """

    @staticmethod
    def syndrome_weight(detectors: np.ndarray) -> np.ndarray:
        """
        Number of fired detectors per shot.

        Returns
        -------
        ndarray
            Shape (shots,)
        """
        detectors = np.asarray(detectors, dtype=np.uint8)

        return detectors.sum(axis=1)

    @staticmethod
    def normalized_weight(detectors: np.ndarray) -> np.ndarray:
        """
        Fired detector ratio.
        """

        detectors = np.asarray(detectors)

        weight = ConfidenceStatistics.syndrome_weight(detectors)

        return weight / detectors.shape[1]

    @staticmethod
    def detector_density(detectors: np.ndarray) -> np.ndarray:
        """
        Density of active detectors.
        """

        detectors = np.asarray(detectors)

        return detectors.mean(axis=1)

    @staticmethod
    def entropy(detectors: np.ndarray) -> np.ndarray:
        """
        Binary entropy of detector activity.

        Higher entropy generally indicates
        more ambiguous syndrome patterns.
        """

        detectors = np.asarray(detectors, dtype=float)

        p = detectors.mean(axis=1)

        eps = 1e-12

        entropy = -(
            p * np.log2(p + eps)
            +
            (1.0 - p) * np.log2(1.0 - p + eps)
        )

        return entropy

    @staticmethod
    def syndrome_complexity(detectors: np.ndarray) -> np.ndarray:
        """
        Composite syndrome complexity score.

        Range:
            approximately 0–2
        """

        weight = ConfidenceStatistics.normalized_weight(detectors)

        entropy = ConfidenceStatistics.entropy(detectors)

        return weight + entropy
