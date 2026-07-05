#!/bin/bash
#SBATCH --job-name=qec_syndrome
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:10:00
#SBATCH --output=logs/setup/syndrome_%j.out
#SBATCH --error=logs/setup/syndrome_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

python scripts/test_syndrome_generator.py
