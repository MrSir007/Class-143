import csv
import pandas as pd
import numpy as np

raw = pd.read_csv("final.csv")

C = raw["vote_average"].mean()
m = raw["vote_count"].quantile(0.9)
q_movies = raw.copy().loc[raw["vote_count"] >= m]

def weighted_rating (x, m=m, C=C) :
  v = x["vote_count"]
  R = x["vote_average"]
  return (v / (v + m) * R) + (m / (v + m) * C)

q_movies["score"] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values("score", ascending=False)
output = q_movies[["title", "vote_count", "vote_average", "poster_link"]].head(20).values.tolist()