"""
Save experiment results.
"""

from pathlib import Path

import pandas as pd


class ResultSaver:

    def __init__(self, output_directory):

        self.output_directory = Path(output_directory)

        self.output_directory.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_csv(self, dataframe, filename):

        output_file = (
            self.output_directory / filename
        )

        dataframe.to_csv(
            output_file,
            index=False
        )

        print()

        print("Saved")

        print(output_file)

        return output_file
