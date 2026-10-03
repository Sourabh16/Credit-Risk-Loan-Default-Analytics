import pandas as pd

from src.config import RAW_FILE


def load_raw_data(path=RAW_FILE) -> pd.DataFrame:
    """Read the raw credit risk CSV into a DataFrame."""
    if not path.exists():
        raise FileNotFoundError(
            f"{path} not found. Download it from Kaggle into data/raw/ (see README)."
        )
    return pd.read_csv(path)