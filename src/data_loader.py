
import pandas as pd
def load_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)
    print(f"      Loaded CSV: {path} ({df.shape[0]} rows, {df.shape[1]} columns)")
    return df
def load_json(path: str) -> pd.DataFrame:
    df = pd.read_json(path)
    print(f"      Loaded JSON: {path} ({df.shape[0]} rows, {df.shape[1]} columns)")
    return df
def fetch_owid_data(
    url: str = "https://covid.ourworldindata.org/data/owid-covid-data.csv",
) -> pd.DataFrame:
    print(f"      Fetching data from: {url}")
    df = pd.read_csv(url, low_memory=False)
    print(f"      Downloaded {df.shape[0]:,} rows.")
    return df
