#!/bin/bash
#SBATCH --job-name=qec_env_test
#SBATCH --partition=test
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=00:05:00
#SBATCH --output=../logs/qec_env_test_%j.out
#SBATCH --error=../logs/qec_env_test_%j.err

cd /scratch/data/m25iqt013/NVIDIA_QEC_Project

source .venv/bin/activate

echo "========================================"
echo "NVIDIA QEC Environment Test"
echo "========================================"

echo "Hostname:"
hostname

echo
echo "Working Directory:"
pwd

echo
echo "Python:"
python --version

echo
echo "Python Executable:"
which python

echo
echo "NumPy Version:"
python -c "import numpy; print(numpy.__version__)"

echo
echo "Current Time:"
date

echo
echo "Environment Test Completed Successfully"
