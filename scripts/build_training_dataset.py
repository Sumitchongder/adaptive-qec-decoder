from simulator.dataset_builder import DatasetBuilder

builder = DatasetBuilder()

builder.build_dataset(
    output_directory="datasets/processed",
    dataset_name="surface_train",
)
