# Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding for the Rotated Surface Code

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-green.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
[![arXiv](https://img.shields.io/badge/arXiv-coming%20soon-b31b1b.svg)]()

Official implementation accompanying the paper:

> **Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding for the Rotated Surface Code**

**Author:** Sumit Chongder  
Department of Physics  
Indian Institute of Technology Jodhpur, India

---

# Overview

This repository contains the complete implementation of an adaptive confidence-gated neural decoder for quantum error correction (QEC) using the rotated surface code.

The framework combines

- Fast neural-network syndrome decoding
- Confidence-based routing
- Minimum-Weight Perfect Matching (MWPM) refinement
- Stim-based circuit-level syndrome simulation
- Latency and throughput benchmarking
- Resource scaling analysis
- Reproducible evaluation pipeline

The objective is to improve logical decoding accuracy while maintaining low inference latency suitable for real-time fault-tolerant quantum computing.

---

# Features

- Adaptive confidence-gated decoding
- Feed-forward neural decoder
- MWPM refinement stage
- Rotated surface code benchmark
- Circuit-level depolarising noise
- Stim simulator integration
- PyMatching decoder
- Training and inference scripts
- Benchmark generation
- CPU throughput measurements
- Resource scaling analysis
- Fully reproducible experiments

---

# Repository Structure

```text
adaptive-qec-decoder/
│
├── data/
│   ├── training/
│   ├── testing/
│   └── benchmarks/
│
├── models/
│   ├── trained_models/
│   └── checkpoints/
│
├── src/
│   ├── simulator/
│   ├── decoder/
│   ├── neural/
│   ├── mwpm/
│   ├── evaluation/
│   └── utils/
│
├── scripts/
│
├── figures/
│
├── notebooks/
│
├── paper/
│
├── requirements.txt
├── LICENSE
└── README.md
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/Sumitchongder/adaptive-qec-decoder.git

cd adaptive-qec-decoder
```

Create a virtual environment

```bash
python -m venv venv
```

Activate

Linux/macOS

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

- Python 3.10+
- NumPy
- SciPy
- PyTorch
- Stim
- PyMatching
- NetworkX
- Matplotlib
- Pandas
- Scikit-learn
- tqdm

---

# Running Experiments

## Generate syndrome data

```bash
python scripts/generate_dataset.py
```

## Train the neural decoder

```bash
python scripts/train.py
```

## Evaluate the adaptive decoder

```bash
python scripts/evaluate.py
```

## Benchmark latency

```bash
python scripts/benchmark.py
```

---

# Experimental Configuration

Surface code distances

```
d = {3, 5, 7, 9, 11}
```

Noise model

```
Circuit-level depolarising noise
```

Decoder

- Feed-forward Neural Network
- Confidence Gate
- MWPM Refinement

Simulator

- Stim

Matching Backend

- PyMatching

---

# Results

The adaptive decoder

- Routes only **3.3%–6.2%** of syndromes to MWPM refinement.
- Improves logical decoding accuracy from **99.21%** to **99.81%**.
- Achieves throughput of approximately **4.6 × 10⁵ samples/s** on commodity CPU hardware.
- Provides bounded latency while maintaining high logical performance.

---

# Reproducibility

This repository contains

- Source code
- Training scripts
- Evaluation scripts
- Benchmark scripts
- Trained models
- Raw benchmark data
- Figure generation scripts

to enable complete reproduction of the experiments reported in the paper.

---

# Citation

If you use this work, please cite

```bibtex
@article{chongder2026adaptive,
  author  = {Sumit Chongder},
  title   = {Latency-Constrained Hardware-Aware Quantum Error Correction Co-Design with Adaptive Confidence-Gated Neural Decoding for the Rotated Surface Code},
  journal = {arXiv preprint},
  year    = {2026},
  archivePrefix = {arXiv},
  primaryClass = {quant-ph}
}
```

(Update the BibTeX entry after the arXiv identifier becomes available.)

---

# Future Work

Planned extensions include

- GPU-accelerated decoding
- Hardware-aware code discovery
- Reinforcement learning for code optimisation
- Non-Pauli and correlated noise models
- QLDPC and color-code benchmarks
- Multi-objective hardware-aware optimisation

---

# License

This repository is released under the **Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)** License.

---

# Contact

**Sumit Chongder**

Department of Physics  
Indian Institute of Technology Jodhpur  
Jodhpur, Rajasthan 342030, India

Email: **sumitchongder960@gmail.com**

GitHub: https://github.com/Sumitchongder

---

## Acknowledgements

This work was carried out at the **Department of Physics, Indian Institute of Technology Jodhpur**. The authors acknowledge the open-source quantum computing ecosystem, including **Stim**, **PyMatching**, and the broader quantum error correction community, whose software and research have enabled reproducible benchmarking and accelerated progress in fault-tolerant quantum computing.
