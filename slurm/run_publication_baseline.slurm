#!/bin/bash
#SBATCH --job-name=qec_publication
#SBATCH --output=logs/publication/publication_%j.out
#SBATCH --error=logs/publication/publication_%j.err

############################################
# Resources
############################################

#SBATCH --partition=test

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4

#SBATCH --mem=16G

#SBATCH --time=04:00:00

############################################

echo "========================================"
echo "Publication Baseline Experiment"
echo "========================================"

echo
echo "Hostname:"
hostname

echo
echo "Date:"
date

echo
echo "Working Directory:"
pwd

echo
echo "Python:"
which python

echo
echo "Python Version:"
python --version

echo
echo "Starting experiment..."
echo

python experiments/publication/run_publication_baseline.py

EXIT_CODE=$?

echo
echo "========================================"
echo "Experiment Finished"
echo "Exit Code: ${EXIT_CODE}"
echo "========================================"

date
