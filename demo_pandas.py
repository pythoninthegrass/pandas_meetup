#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
from icecream import ic
from pathlib import Path

# determine the path to the data file
csv_path = Path("csv")
filename = "dataset-of-10s.csv"
abs_path = csv_path / filename

# read data from csv
df = pd.read_csv(abs_path)
ic(type(df))
ic(df.shape)
ic(df.head(10))

# rename duration_ms to duration_min
df.rename(columns={"duration_ms": "duration_min"}, inplace=True)

# convert column duration_ms to duration_min
df["duration_min"] = df["duration_min"] / 60000

# round duration_min to 2 decimal places
df["duration_min"] = df["duration_min"].round(2)
ic(df.head(5))

# find isna values
ic(df.isna().sum())

# fill na values
df.fillna(0, inplace=True)
ic(df.isna().sum())

# drop na values
df.dropna(inplace=True)
ic(df.isna().sum())

# loc and iloc
ic(df.loc[0:5, "duration_min"])
ic(df.iloc[0:5, 0:2])

# select artist, group by track, artist, danceability, and loudness
df_grouped = df[(df["artist"] == "Katy Perry") & (df["danceability"] > 0.5)].groupby(
    ["track", "artist", "danceability", "loudness"],
    sort=False
)

# print grouped data with track, artist, danceability, and loudness columns
ic(df_grouped)

# plot grouped data
# df_grouped.plot()

# unique artists (return last 10)
ic(df["artist"].unique()[-10:])
