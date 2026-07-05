#!/bin/bash
#SBATCH --job-name=qec_baseline
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --time=01:00:00

#SBATCH --output=logs/experiments/baseline_%j.out
#SBATCH --error=logs/experiments/baseline_%j.err

cd $SLURM_SUBMIT_DIR

source .venv/bin/activate

python experiments/baseline/run_baseline.py
