"""
PyMatching Decoder
==================

Constructs a minimum-weight perfect matching decoder
from a Stim detector error model.

Author:
NVIDIA_QEC_Project
"""

import pymatching


class PyMatchingDecoder:

    def __init__(self, detector_error_model):

        self.detector_error_model = detector_error_model

        self.matching = pymatching.Matching.from_detector_error_model(
            detector_error_model
        )

    def decode(self, detector_samples):

        """
        detector_samples

        shape

        (shots, num_detectors)

        returns

        predicted observables

        shape

        (shots, num_observables)
        """

        predictions = self.matching.decode_batch(detector_samples)

        return predictions
