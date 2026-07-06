from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

import torch

from decoder.neural import SyndromeDecoder
from decoder.neural import predict

model = SyndromeDecoder(
    input_dim=24,
    output_dim=4,
)

x = torch.rand(8, 24)

result = predict(model, x)

print("Prediction:", result["prediction"])
print("Confidence:", result["confidence"])
