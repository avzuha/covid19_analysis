from typing import List

import pandas as pd
def compute_rolling_average(
    df: pd.DataFrame,
    column: str = "new_cases",
    window: int = 7,
    group_col: str = "location",
) -> pd.DataFrame:
    new_col = f"{column}_rolling_{window}d"
    df[new_col] = (
        df.groupby(group_col)[column]
        .transform(lambda x: x.rolling(window, min_periods=1).mean())
    )
    return df
def compute_vaccination_coverage(
    df: pd.DataFrame,
    vaccinated_col: str = "people_vaccinated",
    population_col: str = "population",
) -> pd.DataFrame:
    if vaccinated_col in df.columns and population_col in df.columns:
        df["vaccination_pct"] = (
            df[vaccinated_col] / df[population_col] * 100
        ).clip(0, 100)
    else:
        print(f"      Warning: columns '{vaccinated_col}' or '{population_col}' not found.")
        df["vaccination_pct"] = float("nan")
    return df
def compute_correlation_matrix(
    df: pd.DataFrame,
    columns: List[str] = None,
) -> pd.DataFrame:
    if columns is None:
        columns = df.select_dtypes("number").columns.tolist()
        # Keep only the most meaningful columns if available
        preferred = [
            "new_cases", "new_deaths", "new_vaccinations",
            "people_vaccinated", "icu_patients", "hosp_patients",
        ]
        columns = [c for c in preferred if c in columns] or columns[:8]
    return df[columns].corr()
def find_peak_dates(
    df: pd.DataFrame,
    column: str = "new_cases",
    group_col: str = "location",
) -> pd.DataFrame:
    idx = df.groupby(group_col)[column].idxmax()
    peaks = df.loc[idx, [group_col, "date", column]].copy()
    peaks.columns = [group_col, "date_of_peak", "peak_value"]
    peaks.reset_index(drop=True, inplace=True)
    return peaks
