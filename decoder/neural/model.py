"""
decoder/neural/model.py

Feed-forward neural decoder for quantum error correction.

Author:
NVIDIA_QEC_Project
"""

from __future__ import annotations

import torch
import torch.nn as nn
import torch.nn.functional as F


class SyndromeDecoder(nn.Module):
    """
    Feed-forward syndrome decoder.

    Parameters
    ----------
    input_dim
        Number of detector bits.

    output_dim
        Number of recovery classes.

    hidden_dim
        Hidden layer width.

    dropout
        Dropout probability.
    """

    def __init__(
        self,
        input_dim: int,
        output_dim: int,
        hidden_dim: int = 256,
        dropout: float = 0.20,
    ):
        super().__init__()

        self.network = nn.Sequential(

            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),

            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),

            nn.Linear(hidden_dim, hidden_dim // 2),
            nn.ReLU(),

            nn.Linear(hidden_dim // 2, output_dim),

        )

        self._initialize_weights()

    def _initialize_weights(self):

        for module in self.modules():

            if isinstance(module, nn.Linear):

                nn.init.xavier_uniform_(module.weight)

                nn.init.zeros_(module.bias)

    def forward(self, syndrome):

        return self.network(syndrome)

    @torch.no_grad()
    def predict(self, syndrome):

        logits = self.forward(syndrome)

        return torch.argmax(logits, dim=1)

    @torch.no_grad()
    def predict_proba(self, syndrome):

        logits = self.forward(syndrome)

        return F.softmax(logits, dim=1)

    @torch.no_grad()
    def confidence(self, syndrome):

        probs = self.predict_proba(syndrome)

        confidence, prediction = torch.max(probs, dim=1)

        return prediction, confidence
