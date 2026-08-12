"""Reusable tabular dataset helpers."""

from pathlib import Path

import pandas as pd


def load_tabular_dataset(path: str | Path) -> pd.DataFrame:
    """Load a CSV dataset and provide a useful error when it is absent."""
    dataset_path = Path(path)
    if not dataset_path.exists():
        raise FileNotFoundError(
            f"Dataset not found at {dataset_path}. Add it there or override the Hydra data config."
        )
    return pd.read_csv(dataset_path)


def split_features_and_target(
    frame: pd.DataFrame, target_column: str
) -> tuple[pd.DataFrame, pd.Series]:
    """Separate a dataframe into features and its configured target."""
    if target_column not in frame.columns:
        raise ValueError(f"Target column '{target_column}' is missing from the dataset.")
    return frame.drop(columns=[target_column]), frame[target_column]
