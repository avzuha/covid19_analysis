import os
from typing import List

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import seaborn as sns

plt.style.use("seaborn-v0_8-whitegrid")
OUTPUT_DIR = "outputs/figures"
os.makedirs(OUTPUT_DIR, exist_ok=True)
def plot_cases_trend(
    df: pd.DataFrame,
    countries: List[str],
    column: str = "new_cases_rolling_7d",
    date_col: str = "date",
    location_col: str = "location",
    filename: str = "cases_trend.png",
) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for country in countries:
        subset = df[df[location_col] == country]
        ax.plot(subset[date_col], subset[column], label=country, linewidth=2)
    ax.set_title("COVID-19 Daily New Cases — 7-Day Rolling Average", fontsize=15, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("New Cases (7-day avg)")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.xticks(rotation=45)
    ax.legend(loc="upper right")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"      Saved: {out_path}")
def plot_vaccination_rate(
    df: pd.DataFrame,
    countries: List[str],
    column: str = "vaccination_pct",
    date_col: str = "date",
    location_col: str = "location",
    filename: str = "vax_rate.png",
) -> None:
    fig, ax = plt.subplots(figsize=(12, 6))
    for country in countries:
        subset = df[df[location_col] == country]
        ax.plot(subset[date_col], subset[column], label=country, linewidth=2)
    ax.set_title("COVID-19 Vaccination Coverage by Country", fontsize=15, fontweight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Population Vaccinated (%)")
    ax.set_ylim(0, 100)
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
    plt.xticks(rotation=45)
    ax.legend(loc="upper left")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"      Saved: {out_path}")
def plot_correlation_heatmap(
    corr: pd.DataFrame,
    filename: str = "heatmap.png",
) -> None:
    fig, ax = plt.subplots(figsize=(10, 8))
    mask = np.triu(np.ones_like(corr, dtype=bool))  # Hide upper triangle
    sns.heatmap(
        corr,
        mask=mask,
        annot=True,
        fmt=".2f",
        cmap="RdBu_r",
        center=0,
        vmin=-1,
        vmax=1,
        linewidths=0.5,
        ax=ax,
    )
    ax.set_title("Feature Correlation Matrix", fontsize=15, fontweight="bold")
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"      Saved: {out_path}")
def plot_top_countries(
    df: pd.DataFrame,
    n: int = 10,
    column: str = "total_cases",
    location_col: str = "location",
    filename: str = "top_countries.png",
) -> None:
    top = (
        df.groupby(location_col)[column]
        .max()
        .nlargest(n)
        .sort_values()
    )
    fig, ax = plt.subplots(figsize=(10, 6))
    colors = plt.cm.Blues(np.linspace(0.4, 0.9, len(top)))
    ax.barh(top.index, top.values, color=colors)
    ax.set_title(f"Top {n} Countries by Total COVID-19 Cases", fontsize=15, fontweight="bold")
    ax.set_xlabel("Total Cases")
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x/1e6:.1f}M"))
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"      Saved: {out_path}")
