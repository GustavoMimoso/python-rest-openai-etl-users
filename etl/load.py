import pandas as pd
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_to_csv(df: pd.DataFrame, file_name: str = "users_transformed.csv") -> None:
    DATA_DIR.mkdir(exist_ok=True)
    file_path = DATA_DIR / file_name
    df.to_csv(file_path, index=False)
