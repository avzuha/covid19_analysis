import os
from typing import List

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
OUTPUT_DIR = "outputs/html"
os.makedirs(OUTPUT_DIR, exist_ok=True)
def interactive_cases_trend(
    df: pd.DataFrame,
    countries: List[str],
    column: str = "new_cases_rolling_7d",
    date_col: str = "date",
    location_col: str = "location",
    filename: str = "cases_trend_interactive.html",
) -> None:
    subset = df[df[location_col].isin(countries)].copy()
    fig = px.line(
        subset,
        x=date_col,
        y=column,
        color=location_col,
        title="COVID-19 Daily New Cases — 7-Day Rolling Average (Interactive)",
        labels={
            column: "New Cases (7-day avg)",
            date_col: "Date",
            location_col: "Country",
        },
        template="plotly_white",
    )
    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeslider=dict(visible=True),
            type="date",
        ),
        hovermode="x unified",
        legend=dict(orientation="h", y=1.05),
    )
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.write_html(out_path, include_plotlyjs="cdn")
    print(f"      Saved: {out_path}")
def interactive_scatter(
    df: pd.DataFrame,
    x_col: str = "vaccination_pct",
    y_col: str = "new_deaths",
    color_col: str = "location",
    date_col: str = "date",
    filename: str = "scatter_interactive.html",
) -> None:
    latest = df.sort_values(date_col).groupby(color_col).last().reset_index()
    latest = latest.dropna(subset=[x_col, y_col])
    fig = px.scatter(
        latest,
        x=x_col,
        y=y_col,
        color=color_col,
        size="population" if "population" in latest.columns else None,
        hover_name=color_col,
        title="Vaccination Coverage vs. New Deaths (Latest Date)",
        labels={
            x_col: "Population Vaccinated (%)",
            y_col: "New Deaths",
        },
        template="plotly_white",
    )
    fig.update_layout(hovermode="closest")
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.write_html(out_path, include_plotlyjs="cdn")
    print(f"      Saved: {out_path}")
def animated_bar_race(
    df: pd.DataFrame,
    column: str = "total_cases",
    location_col: str = "location",
    date_col: str = "date",
    top_n: int = 10,
    filename: str = "bar_race.html",
) -> None:
    df_monthly = df.copy()
    df_monthly["month"] = df_monthly[date_col].dt.to_period("M").dt.to_timestamp()
    monthly = df_monthly.groupby([location_col, "month"])[column].max().reset_index()
    fig = px.bar(
        monthly,
        x=column,
        y=location_col,
        color=location_col,
        animation_frame=monthly["month"].dt.strftime("%Y-%m"),
        orientation="h",
        title=f"Top Countries by Total COVID-19 Cases Over Time",
        labels={column: "Total Cases", location_col: "Country"},
        template="plotly_white",
    )
    fig.update_layout(showlegend=False)
    out_path = os.path.join(OUTPUT_DIR, filename)
    fig.write_html(out_path, include_plotlyjs="cdn")
    print(f"      Saved: {out_path}")
