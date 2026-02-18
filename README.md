# COVID-19 Data Analysis & Visualization

Exploratory Data Analysis (EDA) on COVID-19 datasets — cases, recoveries, and vaccinations.

## Quick Start (PyCharm)

1. Open this folder as a project in PyCharm.
2. Open the Terminal (`View > Tool Windows > Terminal`).
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Download the dataset from:
   ```
   https://covid.ourworldindata.org/data/owid-covid-data.csv
   ```
   Place it in: `data/raw/owid-covid-data.csv`

5. Run the pipeline:
   ```
   python main.py
   ```

## Outputs

| Type | Location |
|------|----------|
| Cleaned data | `data/processed/cleaned_covid.csv` |
| Line plots / heatmaps | `outputs/figures/` |
| Interactive HTML charts | `outputs/html/` |

## Project Structure

```
covid19_analysis/
├── data/raw/              ← Place downloaded CSV here
├── data/processed/        ← Auto-generated cleaned data
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── analyzer.py
│   ├── visualizer.py
│   └── interactive.py
├── outputs/
│   ├── figures/
│   └── html/
├── main.py
├── requirements.txt
└── README.md
```

## Libraries Used

- **pandas** — data loading and manipulation
- **numpy** — numerical operations
- **matplotlib** — static line plots, bar charts
- **seaborn** — correlation heatmaps
- **plotly** — interactive HTML charts
