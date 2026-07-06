"""
Training metrics.
"""

import torch


def classification_accuracy(logits, labels):

    prediction = torch.argmax(logits, dim=1)

    labels = labels.view(-1)

    return (prediction == labels).float().mean().item()
