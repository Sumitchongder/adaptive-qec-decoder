from experiments.framework.experiment_runner import ExperimentRunner

runner = ExperimentRunner(
    "configs/default.yaml"
)

result = runner.repeat(

    distance=3,

    noise=0.001,

    shots=1000,

    repeats=3,

)

print()

for k, v in result.items():

    print(f"{k:20s} {v}")
