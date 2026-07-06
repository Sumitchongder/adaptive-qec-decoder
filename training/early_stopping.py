"""
Early stopping utility.
"""


class EarlyStopping:

    def __init__(

        self,

        patience=10,

        min_delta=1e-4,

    ):

        self.patience = patience

        self.min_delta = min_delta

        self.best_loss = float("inf")

        self.counter = 0

    def step(self, validation_loss):

        if validation_loss < self.best_loss - self.min_delta:

            self.best_loss = validation_loss

            self.counter = 0

            return False

        self.counter += 1

        return self.counter >= self.patience
