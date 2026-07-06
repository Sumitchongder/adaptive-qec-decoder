#!/bin/bash
#SBATCH --job-name=distance_sweep
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16gb
#SBATCH --time=02:00:00
#SBATCH --output=logs/experiments/distance_%j.out
#SBATCH --error=logs/experiments/distance_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

export PYTHONPATH=$(pwd)

python scripts/run_distance_sweep.py
