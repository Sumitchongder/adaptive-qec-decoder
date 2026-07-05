"""
Central experiment configuration.

All experiments should import this file so that every
benchmark uses the same parameter values.
"""

# Surface-code distances
DISTANCES = [
    3,
    5,
    7,
    9,
    11,
    13,
    15,
    17,
    19,
    21,
]

# Physical depolarizing error probabilities
NOISE_LEVELS = [
    1e-4,
    2e-4,
    5e-4,
    1e-3,
    2e-3,
    5e-3,
    1e-2,
    2e-2,
]

# Number of shots
SHOTS = 10000

# Random seed
SEED = 42
