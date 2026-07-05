"""
Syndrome Generator
==================

Samples detector events and logical observables from a Stim circuit.
"""

from __future__ import annotations

import numpy as np
import stim


class SyndromeGenerator:
    """Generate syndrome samples from a Stim circuit."""

    def __init__(self, circuit: stim.Circuit):
        self.circuit = circuit
        self.sampler = circuit.compile_detector_sampler()

    def sample(self, shots: int = 1000):
        """
        Sample detector events and logical observables.

        Parameters
        ----------
        shots : int
            Number of samples.

        Returns
        -------
        tuple[np.ndarray, np.ndarray]
            (detector_events, observable_flips)
        """
        detector_events, observable_flips = self.sampler.sample(
            shots=shots,
            separate_observables=True,
        )

        return detector_events, observable_flips
