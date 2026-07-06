#!/bin/bash
#SBATCH --job-name=train_decoder
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=8gb
#SBATCH --time=00:30:00
#SBATCH --output=logs/training/train_%j.out
#SBATCH --error=logs/training/train_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

export PYTHONPATH=$(pwd)

python scripts/train_neural_decoder.py
