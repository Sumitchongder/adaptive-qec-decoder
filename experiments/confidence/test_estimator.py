import numpy as np

from decoder.confidence.estimator import ConfidenceEstimator

rng = np.random.default_rng(42)

detectors = rng.integers(

    0,

    2,

    size=(1000, 120),

    dtype=np.uint8,

)

estimator = ConfidenceEstimator()

confidence = estimator.confidence(detectors)

print()

print("First 20 confidence values")

print(confidence[:20])

print()

print("Summary")

print(estimator.summary(detectors))
