
import numpy as np
import pandas as pd

np.random.seed(42)

from src.data_loader import load_csv
from src.preprocessor import clean_data
from src.analyzer import (
    compute_rolling_average,
    compute_vaccination_coverage,
    compute_correlation_matrix,
)
from src.visualizer import (
    plot_cases_trend,
    plot_vaccination_rate,
    plot_correlation_heatmap,
    plot_top_countries,
)
from src.interactive import (
    interactive_cases_trend,
    interactive_scatter,
)

DATA_URL = "https://covid.ourworldindata.org/data/owid-covid-data.csv"
DATA_PATH = "data/raw/owid-covid-data.csv"
COUNTRIES = ["United States", "India", "Brazil", "United Kingdom", "Germany"]
def main():
    print("=" * 60)
    print("  COVID-19 Data Analysis Pipeline")
    print("=" * 60)
    print("\n[1/5] Loading data...")
    try:
        df = load_csv(DATA_PATH)
        print(f"      Loaded {len(df):,} rows from local file.")
    except FileNotFoundError:
        print(f"      Local file not found. Download from:\n      {DATA_URL}")
        print("      Place it in:  data/raw/owid-covid-data.csv")
        return
    print("[2/5] Cleaning and preprocessing...")
    df = clean_data(df, countries=COUNTRIES)
    df.to_csv("data/processed/cleaned_covid.csv", index=False)
    print(f"      Cleaned data saved → data/processed/cleaned_covid.csv")
    print("[3/5] Analysing...")
    df = compute_rolling_average(df, column="new_cases", window=7)
    df = compute_vaccination_coverage(df)
    corr = compute_correlation_matrix(df)
    print("[4/5] Generating static visualizations...")
    plot_cases_trend(df, countries=COUNTRIES)
    plot_vaccination_rate(df, countries=COUNTRIES)
    plot_correlation_heatmap(corr)
    plot_top_countries(df, n=10)
    print("      Figures saved → outputs/figures/")
    print("[5/5] Generating interactive Plotly charts...")
    interactive_cases_trend(df, countries=COUNTRIES)
    interactive_scatter(df)
    print("      HTML files saved → outputs/html/")

    print("\nPipeline complete! Open outputs/ to view your results.")
    print("=" * 60)


if __name__ == "__main__":
    main()
