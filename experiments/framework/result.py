from dataclasses import dataclass


@dataclass
class ExperimentResult:

    distance: int
    noise: float

    runtime: float
    throughput: float

    accuracy: float
    logical_error: float

    detectors: int
    observables: int
    operations: int

    correct: int
    incorrect: int
