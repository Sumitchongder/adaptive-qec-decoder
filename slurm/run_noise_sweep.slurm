#!/bin/bash
#SBATCH --job-name=noiseSweep
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=04:00:00

#SBATCH --output=logs/simulation/noise_%j.out
#SBATCH --error=logs/simulation/noise_%j.err

cd /scratch/data/$USER/NVIDIA_QEC_Project

source .venv/bin/activate

python experiments/noise_sweep/run_noise_sweep.py
