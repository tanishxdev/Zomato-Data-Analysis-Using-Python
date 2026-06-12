# src/load_data.py

import pandas as pd


def load_dataset(file_path):
    """
    Load CSV dataset and return DataFrame.
    """

    df = pd.read_csv(file_path)

    return df