import csv
from rating import Rating
from user import User
from movie import Movie

users = {}

with open("u.user.csv") as f:
    reader = csv.DictReader(f, fieldnames=["user_id", "age", "", "", "zipcode"], delimiter='|')
    for row in reader:
        user = User(row["user_id"], row["age"], row["zipcode"])
        users[user.id] = user

for key in users:
    user = users[key]
    # print(user.id, user.age, user.zipcode)

movies = {}

with open('u.item.csv', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=["movie_id", "title"], delimiter='|')
    for row in reader:
        movie = Movie(row["movie_id"], row["title"])
        movies[movie.id] = movie

# movies_list = [movies[key] for key in movies]
# for row in reader:
#     movie = Movie(row["movie_id"], row["title"])
#     movies[movie.id] = movie
#
# movies_list = [movies[key] for key in movies]
# print (str(movies["95"]))

movie_ratings = []
# user_ratings = {}

with open("u.data.csv", encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=["user_id", "item_id", "user_rating"], delimiter='\t')
    for row in reader:
        rating = Rating(row)
        # user_ratings[row["user_id"]] = rating
        movie_ratings.append(rating)

movies_list = [movies[key] for key in movies]


# Find all ratings for a movie by id - returns a list of all ratings by movie id

def all_ratings_by_movie_id(ratings, movie_id):
    all_ratings = {}
    for rating in ratings:
        if rating.item_id == movie_id:
            all_ratings[movie.id].append(rating)
    return all_ratings
# print (all_ratings_by_movie_id(movie_ratings, "757"))
sevenfiveseven = all_ratings_by_movie_id(movie_ratings, "863")

# Find all ratings for a user - returns a list of ratings by user id

def all_ratings_by_user(ratings, user_id):
    all_ratings = []
    for rating in ratings:
        if rating.user == user_id:
            all_ratings.append(rating.rating)
    return all_ratings

# print (all_ratings_by_user(movie_ratings, 660))

# Find the average rating for a movie by id - an average rating of a movie by id

def average_rating(ratings):
    sum_of_rating = 0
# ratings_per_movie = all_ratings_by_movie_id(movie_ratings, "333")
    for rating in ratings:
        sum_of_rating += rating.rating
    average_rating = sum_of_rating/len(ratings)
    return average_rating

# print (average_rating(sevenfiveseven))

# Find the name of a movie by id

def name_of_movie_by_id(movie_id):
    return movies[movie_id].title

# print (name_of_movie_by_id(333))



def avg_rating_by_movie(movies):
    movie_avg_rating = {}
    for movie_id, movie in movies.items():
        ratings = all_ratings_by_movie_id(movie_ratings, movie_id)
        average = average_rating(ratings)
        movie_avg_rating[movie_id] = round(average,2)
    return movie_avg_rating

# print (avg_rating_by_movie(movies))
def get_min_rating(movies):
    min_rating_movie = {}
    for movie_id, movie in movies.items():
        ratings = all_ratings_by_movie_id(movie_ratings, movie_id)
        for rating in ratings:
            if len(ratings) > 20:
                min_rating_movie[movie_id].append(ratings)
    return min_rating_movie
#
print(get_min_rating(movies))
