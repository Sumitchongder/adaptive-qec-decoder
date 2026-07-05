#!/bin/bash
#SBATCH --job-name=qec_decoder
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
#SBATCH --time=00:05:00
#SBATCH --output=logs/setup/decoder_%j.out
#SBATCH --error=logs/setup/decoder_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

python scripts/test_decoder.py
