"""
PyMatching Decoder
==================
"""

import pymatching


class PyMatchingDecoder:
    """
    Baseline PyMatching decoder.
    """

    def __init__(self, detector_error_model):

        self.matcher = pymatching.Matching.from_detector_error_model(
            detector_error_model
        )

    def decode(self, detector_samples):

        predictions = self.matcher.decode_batch(detector_samples)

        return predictions
