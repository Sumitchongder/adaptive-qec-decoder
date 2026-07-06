#!/bin/bash
#SBATCH --job-name=noise_data
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:30:00
#SBATCH --output=logs/training/noise_%j.out
#SBATCH --error=logs/training/noise_%j.err

cd /scratch/data/$USER/NVIDIA_QEC_Project

source .venv/bin/activate

export PYTHONPATH=$(pwd)

python scripts/build_noise_dataset.py
