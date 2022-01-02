import csv

with open ("movies.csv") as movie_raw :
  rawReader = csv.reader(movie_raw)
  rawlist = list(rawReader)
  all_movies = rawlist[1:]
  header = rawlist[0]

header.append("poster_link")

with open ("final.csv", "a+") as all_raw :
  rawWriter = csv.writer(all_raw)
  rawWriter.writerow(header)

with open ("movie_links.csv") as link_raw :
  rawReader = csv.reader(link_raw)
  rawlist = list(rawReader)
  all_movie_links = rawlist[1:]

for i in all_movies :
  poster_check = any(i[8] in movie_link_item for movie_link_item in all_movie_links)
  if poster_check :
    for check in all_movie_links :
      if i[8] == check[0] :
        i.append(check[1])
        if len(i) == 28 :
          with open ("final.csv", "a+") as all_raw :
            rawWriter = csv.writer(all_raw)
            rawWriter.writerow(i)