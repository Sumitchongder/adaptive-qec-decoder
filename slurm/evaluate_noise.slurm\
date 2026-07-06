#!/bin/bash
#SBATCH --job-name=noise_eval
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=16G
#SBATCH --time=00:30:00
#SBATCH --output=logs/evaluation/noise_%j.out
#SBATCH --error=logs/evaluation/noise_%j.err

cd /scratch/data/$USER/NVIDIA_QEC_Project

source .venv/bin/activate

export PYTHONPATH=$(pwd)

python scripts/run_noise_evaluation.py
