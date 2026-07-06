import numpy as np

from decoder.confidence.statistics import ConfidenceStatistics

rng = np.random.default_rng(42)

detectors = rng.integers(

    0,

    2,

    size=(10, 50),

    dtype=np.uint8,

)

print("Weight")

print(ConfidenceStatistics.syndrome_weight(detectors))

print()

print("Normalized")

print(ConfidenceStatistics.normalized_weight(detectors))

print()

print("Entropy")

print(ConfidenceStatistics.entropy(detectors))

print()

print("Complexity")

print(ConfidenceStatistics.syndrome_complexity(detectors))
