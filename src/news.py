# --------------------------------------------------
# News data preparation
# --------------------------------------------------

# This script merges several processed GDELT files related to feral cats in Australia and creates a yearly aggregated news dataset.

# Input files:
# - article counts related to feral cats
# - total monitored articles
# - average tone of coverage
# - volume intensity of the topic
# Output:
# A final yearly dataset with the following variables:
# - article_count: total number of articles about feral cats in a given year
# - tone_weighted: weighted average tone, using article count as weights
# - volume_intensity_mean: mean of volume intensity values within each year
# - volume_intensity: share of feral-cat-related articles relative to all monitored articles

import pandas as pd
import numpy as np
from functools import reduce

# Read raw GDELT-based files
news_number = pd.read_csv("raw data/GDELT (feral cat + Australia number).csv")
news_tone = pd.read_csv("raw data/GDELT (feral cat + Australia tone timeline).csv")
news_volume = pd.read_csv("raw data/GDELT (feral cat + Australia volume).csv")

# Keep total number of monitored articles and rename the value column
news_total = (
    news_number[news_number["Series"] == "Total Monitored Articles"]
    .drop(["Series"], axis=1)
    .rename(columns={"Value": "all_articles"})
)

# Keep only article counts related to feral cats
news_number = (
    news_number[news_number["Series"] == "Article Count"]
    .drop(["Series"], axis=1)
    .rename(columns={"Value": "article_count_raw"})
)

# Prepare tone data
news_tone = (
    news_tone.drop(["Series"], axis=1)
    .rename(columns={"Value": "average_tone"})
)

# Prepare volume intensity data
news_volume = (
    news_volume.drop(["Series"], axis=1)
    .rename(columns={"Value": "volume_intensity_raw"})
)

# Merge all news-related datasets by date
news = [news_number, news_total, news_tone, news_volume]
news_all = reduce(lambda l, r: l.merge(r, on="Date", how="outer"), news)

# Convert date column to datetime and extract year
news_all["Date"] = pd.to_datetime(news_all["Date"])
news_all["year"] = news_all["Date"].dt.year

# Aggregate data at the yearly level
news_all = (
    news_all.groupby("year", as_index=False)
    .apply(lambda g: pd.Series({
        # Total number of feral-cat-related articles in the year
        "article_count": g["article_count_raw"].sum(),

        # Weighted average tone using article counts as weights
        "tone_weighted": np.average(
            g["average_tone"],
            weights=g["article_count_raw"]
        ) if g["article_count_raw"].sum() > 0 else np.nan,

        # Total number of all monitored articles in the year
        "all_articles": g["all_articles"].sum(),

        # Average volume intensity across observations in the year
        "volume_intensity_mean": g["volume_intensity_raw"].mean(),
    }))
    .reset_index(drop=True)
)

# Compute yearly share of feral-cat-related articles in the overall news flow
news_all["volume_intensity"] = news_all["article_count"] / news_all["all_articles"]

# Drop intermediate helper column
news_all.drop("all_articles", axis=1, inplace=True)

# Save the final aggregated dataset
news_all.to_csv("datasets/news.csv", index=False)