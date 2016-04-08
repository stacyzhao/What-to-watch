import csv

class User():

    def __init__(self, row):
        self.user_id = row["user_id"]
        self.age = row["age"]
        self.zipcode = row["zipcode"]

user_info = {}

with open("u.user.csv") as f:
    reader = csv.DictReader(f, fieldnames=["user_id", "age", "", "", "zipcode"], delimiter='|')
    for row in reader:
        user_info[row["user_id"]] = User(row)

for key in user_info:
    user = user_info[key]
    print(user.user_id, user.age, user.zipcode)


class Movie():

    def __init__(self, row):
        self.id = row["movie_id"]
        self.title = row["movie_title"]

movies = {}

with open('u.item.csv', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=["movie_id", "movie_title"], delimiter='|')
    for row in reader:
        movies[row["movie_id"]] = Movie(row)

for key in movies:
    movie = movies[key]
    print (movie.id + " " + movie.title)


class Rating():

    def __init__(self, row):
        self.user = row["user_id"]
        self.rating = row["user_rating"]

ratings = {}

with open("u.data.csv", encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=["user_id", "", "user_rating"], delimiter='\t')
    for row in reader:
        ratings[row["user_id"]] = Rating(row)

for key in ratings:
    rate = ratings[key]
    print (rate.user + " " + rate.rating)
