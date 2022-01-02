import csv
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer as cv
from sklearn.metrics.pairwise import cosine_similarity as cos

raw = pd.read_csv("final.csv")
raw = raw[raw["soup"].notna()]
count =  cv(stop_words="english")
count_matrix = count.fit_transform(raw["soup"])
cosine = cos(count_matrix, count_matrix)
raw = raw.reset_index()
indices = pd.Series(raw.index, index=raw["title"])

def get_recommendation (title) :
  idx = indices[title]
  scores = list(enumerate(cosine[idx]))
  scores = sorted(scores, key=lambda x: x[1], reverse=True)
  scores = scores[1:11]
  movie_indices = [i[0] for i in scores]
  return raw[["title", "vote_count", "vote_average", "poster_link"]].head(20).values.tolist()