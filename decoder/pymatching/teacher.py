"""
PyMatching Teacher
==================
"""

from .decoder import PyMatchingDecoder


class PyMatchingTeacher:

    def __init__(self, detector_error_model):

        self.decoder = PyMatchingDecoder(detector_error_model)

    def decode(self, detector_samples):

        return self.decoder.decode(detector_samples)
