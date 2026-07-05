"""
Collect system information.

Author:
NVIDIA_QEC_Project
"""

import os
import platform
import socket
import sys


def get_system_info():

    return {

        "hostname": socket.gethostname(),

        "platform": platform.platform(),

        "python_version": platform.python_version(),

        "processor": platform.processor(),

        "cpu_count": os.cpu_count(),

        "python_executable": sys.executable,

        "slurm_job":

            os.environ.get(

                "SLURM_JOB_ID",

                "LOCAL"

            ),

        "slurm_node":

            os.environ.get(

                "SLURMD_NODENAME",

                "LOCAL"

            )

    }
