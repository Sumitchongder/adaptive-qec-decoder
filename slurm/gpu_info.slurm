#!/bin/bash
#SBATCH --job-name=gpu_info
#SBATCH --partition=dgx
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --time=00:02:00
#SBATCH --output=../logs/gpu_info_%j.out
#SBATCH --error=../logs/gpu_info_%j.err

echo "Hostname:"
hostname

echo
echo "GPU Information:"
nvidia-smi

echo
echo "CUDA Compiler:"
which nvcc || true

echo
nvcc --version || true
