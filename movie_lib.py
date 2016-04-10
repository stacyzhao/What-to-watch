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
# print (str(movies["95"]))

movie_ratings = []
# user_ratings = {}

with open("u.data.csv", encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=["user_id", "movie_id", "user_rating"], delimiter='\t')
    for row in reader:
        rating = Rating(row)
        # user_ratings[row["user_id"]] = rating
        movie_ratings.append(rating)

for rating in movie_ratings:
    movie = movies[rating.movie_id]
    movie.add_rating(rating)

movies_list = [movies[key] for key in movies]


# def all_ratings_by_movie_id(ratings):
#     for rating in ratings:
#         movie = movies[rating.item_id]
#         movie.add_rating(rating)
#
# print (all_ratings_by_movie_id(movies, movie_id))
# print(all_ratings_by_movie_id(movie_ratings, movie.id))

# Find all ratings for a user - returns a list of ratings by user id
def all_ratings_by_user(ratings, user_id):
    return [rating for rating in ratings if rating.user == user_id]
    # all_ratings = []
    # for rating in ratings:
    #     if rating.user == user_id:
    #         all_ratings.append(rating)
    # return all_ratings

# print (all_ratings_by_user(movie_ratings, 885))

def get_movies_list_by_user_id(movies, user_id):
    return [movies[rating.movie_id] for rating in all_ratings_by_user(movie_ratings, user_id)]
#     user_movies =[]
#     for rating in all_ratings_by_user(movie_ratings, user_id):
#         user_movies.append(movies[rating.movie_id])
#     return user_movies
# print (get_movies_list_by_user_id(movies, 885))

def not_rated_movie_list_by_user(movies, user_movie_list):
    not_rated_movies = {}
    for movie_id, movie in movies.items():
        if movie not in user_movie_list:
            not_rated_movies[movie_id] = movie
    return not_rated_movies
# print (not_rated_movie_list_by_user(movies, get_movies_list_by_user_id(movies, 885)))
# Find the average rating for a movie by id - an average rating of a movie by id

# def average_rating(ratings):
#     sum_of_rating = 0
# # ratings_per_movie = all_ratings_by_movie_id(movie_ratings, "333")
#     for rating in ratings:
#         sum_of_rating += rating.rating
#     average_rating = sum_of_rating/len(ratings)
#     return average_rating

# print (average_rating(sevenfiveseven))

# Find the name of a movie by id: returns title
# movie_id = input("whats the movie id?")
def name_of_movie_by_id(movie_id):
    return movies[movie_id].title
# print (name_of_movie_by_id(movie_id))

# keep movies with more than 200 ratings: returns movie_id:movie object
def filter_movies(movies):
    filtered_movies = {}
    for movie_id, movie in movies.items():
        if len(movie.ratings) > 200:
            filtered_movies[movie_id] = movie
    return filtered_movies
# print (filter_movies(not_rated_movie_list_by_user(movies, get_movies_list_by_user_id(movies, 885) )))

# def avg_rating_by_movie(movies):
#     movie_avg_rating = {}
#     for movie_id, movie in movies.items():
#         ratings = all_ratings_by_movie_id(movie_ratings, movie_id)
#         average = average_rating(ratings)
#         movie_avg_rating[movie_id] = round(average,2)
#     return movie_avg_rating
# print (avg_rating_by_movie(filter_movies))

# get avg rating by movie: returns movie_id:avg rating
def avg_rating_by_movie(movies):
    filtered_movies = filter_movies(movies)
    movie_avg_rating = {}
    for movie_id, movie in movies.items():
        ratings = round(movie.average_rating(),2)
        if movie_id in filtered_movies:
            movie_avg_rating[movie_id] = ratings
    return movie_avg_rating
# print (avg_rating_by_movie(filter_movies(not_rated_movie_list_by_user(movies, get_movies_list_by_user_id(movies, 885)))))

avg_ratings = avg_rating_by_movie(filter_movies(not_rated_movie_list_by_user(movies, get_movies_list_by_user_id(movies, 885))))

# get top x  movies with more than 4 rating returns movie_id:title
def top_movies_list(avg_rating, movies):
    top_movie_list = {}
    for movie_id, avg in avg_rating.items():
        if len(top_movie_list) < 20:
            top_movie_list[avg] = movies[movie_id].title
    for key in reversed(sorted(top_movie_list)):
        print ("%s: %s" % (top_movie_list[key], key))
    return top_movie_list


print (top_movies_list(avg_ratings, movies))
# top_movies_list(avg_rating_by_movie(movies),movies)
# print name_of_movie_by_id()



def main():
    pass


# def get_min_rating(movies):
#     min_rating_movie = {}
#     for movie_id, movie in movies.items():
#         print(movie_id, movie)
#         ratings = all_ratings_by_movie_id(movie_ratings, movie_id)
#         for rating in ratings:
#             if len(ratings) > 20:
#                 min_rating_movie[movie_id].append(rating.rating)
#     return min_rating_movie
# print(get_min_rating(movie_ratings))
