import csv
from flask import Flask, jsonify

all_movies = []
with open ("movies.csv") as raw :
  rawRead = csv.reader(raw)
  rawlist = list(rawRead)
  all_movies = rawlist[1:]

liked_movies = []
unliked_movies = []
unwatched_movies = []

app = Flask(__name__)
@app.route("/get-movie")
def get_movie () :
  return jsonify({
    "data": all_movies[0],
    "status": "success"
  })

@app.route("/liked-movie", methods=["POST"])
def liked_movie () :
  movie = all_movies[0]
  all_movies = all_movies[1:]
  liked_movies.append(movie)
  return jsonify({
    "status": "success"
  }), 201

@app.route("/unliked-movie", methods=["POST"])
def unliked_movie () :
  movie = all_movies[0]
  all_movies = all_movies[1:]
  unliked_movies.append(movie)
  return jsonify({
    "status": "success"
  }), 201

@app.route("/unwatched-movie", methods=["POST"])
def unwatched_movie () :
  movie = all_movies[0]
  all_movies = all_movies[1:]
  unwatched_movies.append(movie)
  return jsonify({
    "status": "success"
  }), 201

if __name__ == "__main__" :
  app.run()