from pathlib import Path
import pandas as pd


class ResultWriter:

    def __init__(self):

        self.rows = []

    def add(self, result):

        self.rows.append(result.__dict__)

    def save(self, filename):

        output = Path("results/csv")

        output.mkdir(parents=True, exist_ok=True)

        df = pd.DataFrame(self.rows)

        df.to_csv(output / filename, index=False)

        print(df.head())

        print()

        print("Saved")

        print(output / filename)
