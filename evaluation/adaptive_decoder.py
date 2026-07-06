from pathlib import Path

import pandas as pd


class AdaptiveDecoder:

    def __init__(self, csv_file):

        self.df = pd.read_csv(csv_file)

    def evaluate(self, threshold):

        routed_neural = self.df["confidence"] >= threshold

        neural_correct = (
            routed_neural
            &
            (self.df["correct"] == 1)
        ).sum()

        routed_matching = (~routed_neural).sum()

        total_correct = neural_correct + routed_matching

        accuracy = total_correct / len(self.df)

        return {

            "threshold": threshold,

            "neural_fraction":
                routed_neural.mean(),

            "matching_fraction":
                1 - routed_neural.mean(),

            "accuracy":
                accuracy,

        }
