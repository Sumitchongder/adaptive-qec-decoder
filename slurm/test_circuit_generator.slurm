#!/bin/bash
#SBATCH --job-name=qec_circuit_test
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G
#SBATCH --time=00:05:00
#SBATCH --output=logs/setup/circuit_%j.out
#SBATCH --error=logs/setup/circuit_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

python scripts/test_circuit_generator.py
