from typing import List, Optional

import numpy as np
import pandas as pd
def clean_data(
    df: pd.DataFrame,
    countries: Optional[List[str]] = None,
    date_col: str = "date",
    location_col: str = "location",
) -> pd.DataFrame:
    if countries:
        df = df[df[location_col].isin(countries)].copy()
        print(f"      Filtered to {len(countries)} countries: {df.shape[0]:,} rows remain.")

    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    df.sort_values([location_col, date_col], inplace=True)

    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    df[numeric_cols] = (
        df.groupby(location_col)[numeric_cols]
        .transform(lambda x: x.ffill().bfill())
        .fillna(0)
    )
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)

    print(f"      Cleaning complete: {df.shape[0]:,} rows, {df.shape[1]} columns.")
    return df
def normalize_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    col_min = df[column].min()
    col_max = df[column].max()
    if col_max == col_min:
        df[f"{column}_normalized"] = 0.0
    else:
        df[f"{column}_normalized"] = (df[column] - col_min) / (col_max - col_min)
    return df

def flag_outliers(df: pd.DataFrame, column: str, z_threshold: float = 3.0) -> pd.DataFrame:
    mean = df[column].mean()
    std = df[column].std()
    if std == 0:
        df[f"{column}_outlier"] = False
    else:
        z_scores = (df[column] - mean) / std
        df[f"{column}_outlier"] = z_scores.abs() > z_threshold
    return df
