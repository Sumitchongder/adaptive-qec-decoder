"""
Experiment logger.

Author:
NVIDIA_QEC_Project
"""

from pathlib import Path

import json

from datetime import datetime


class ExperimentLogger:

    def __init__(

        self,

        output_directory="logs/experiments",

    ):

        self.output_directory = Path(

            output_directory

        )

        self.output_directory.mkdir(

            parents=True,

            exist_ok=True,

        )

    def write(

        self,

        filename,

        data,

    ):

        filename = self.output_directory / filename

        with open(filename, "w") as f:

            json.dump(

                data,

                f,

                indent=4,

            )

        return filename

    def timestamp(self):

        return datetime.now().isoformat()
