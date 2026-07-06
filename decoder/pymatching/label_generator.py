"""
Generate labels using PyMatching.
"""

import numpy as np

from .teacher import PyMatchingTeacher


class LabelGenerator:

    def __init__(self, detector_error_model):

        self.teacher = PyMatchingTeacher(detector_error_model)

    def generate_labels(self, detector_events):

        labels = self.teacher.decode(detector_events)

        return np.asarray(labels, dtype=np.int8)
