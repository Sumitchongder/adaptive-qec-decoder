from experiments.framework.result import ExperimentResult
from experiments.framework.result_writer import ResultWriter


writer = ResultWriter()

writer.add(

    ExperimentResult(

        distance=3,

        noise=0.001,

        runtime=0.50,

        throughput=10000,

        accuracy=0.999,

        logical_error=0.001,

        detectors=24,

        observables=1,

        operations=80,

        correct=4995,

        incorrect=5,

    )

)

writer.save("test.csv")
