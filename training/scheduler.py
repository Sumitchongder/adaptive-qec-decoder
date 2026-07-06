"""
Learning-rate scheduler.
"""

from torch.optim.lr_scheduler import ReduceLROnPlateau


def build_scheduler(optimizer):

    return ReduceLROnPlateau(

        optimizer,

        mode="min",

        factor=0.5,

        patience=5,

        min_lr=1e-6,

    )
