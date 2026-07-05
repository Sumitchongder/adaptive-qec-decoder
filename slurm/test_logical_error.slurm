#!/bin/bash
#SBATCH --job-name=qec_logic
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=00:05:00
#SBATCH --output=logs/setup/logical_%j.out
#SBATCH --error=logs/setup/logical_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

python scripts/test_logical_error.py
