import csv
from movie import Movie
from rating import Rating
from user import User


users = {}

with open("u.user.csv") as f:
    reader = csv.DictReader(f, fieldnames=["user_id", "age", "", "", "zipcode"], delimiter='|')
    for row in reader:
        user = User(row["user_id"], row["age"], row["zipcode"])
        users[user.id] = user

    for key in users:
        user = users[key]

movies = {}

with open('u.item.csv', encoding='latin_1') as f:
    reader = csv.DictReader(f, fieldnames=["movie_id", "title"], delimiter='|')
    for row in reader:
        movie = Movie(row["movie_id"], row["title"])
        movies[movie.id] = movie

def get_movie_ratings():
    movie_ratings = []

    with open("u.data.csv", encoding='latin_1') as f:
        reader = csv.DictReader(f, fieldnames=["user_id", "movie_id", "user_rating"], delimiter='\t')
        for row in reader:
            rating = Rating(row)
            movie_ratings.append(rating)
        # user_ratings[row["user_id"]] = rating
        for rating in movie_ratings:
            movie = movies[rating.movie_id]
            movie.add_rating(rating)

    return movie_ratings


# Find all ratings for a user
def all_ratings_by_user(ratings, user_id):
    return [rating for rating in ratings if rating.user == user_id]

def all_ratings_by_movie_id(movies, movie_id):
    return [movie.ratings for movie_id, movie in movies.items() if movie_id == movie_id]
# print (all_ratings_by_user(movie_ratings, 885))

def get_movies_list_by_user_id(movies, user_id):
    return [movies[rating.movie_id] for rating in all_ratings_by_user(get_movie_ratings(), user_id)]
# print (get_movies_list_by_user_id(movies, 885))

def not_rated_movie_list_by_user(movies, user_movie_list):
    return [movie for movie_id, movie in movies.items() if movie not in user_movie_list]
    # not_rated_movies = []
    # for movie_id, movie in movies.items():
    #     if movie not in user_movie_list:
    #         not_rated_movies.append(movie)
    # return not_rated_movies
# print (not_rated)
# print (not_rated_movie_list_by_user(movies, get_movies_list_by_user_id(movies, 885)))

# Find the average rating for a movie by id - an average rating of a movie by id
def get_avg_rating_by_movie_id(movies, movie_id):
    return round(movies[movie_id].average_rating(),2)

# Find the name of a movie by id: returns title
def name_of_movie_by_id(movie_id):
    return movies[movie_id].title
# print (name_of_movie_by_id(movie_id))

# keep movies with more than 200 ratings: returns movie_id:movie object
def filter_movies(movies):
    return [movie for movie in movies if len(movie.ratings) > 200]

# get top x  movies with more than 4 rating returns movie_id:title
def top_movies_list(filtered_movies, movies):
    top_movie_list = []
    for movie in filtered_movies:
        if len(top_movie_list) < 20:
            top_movie_list.append(movie.title)
            print (movie.title, ":", round(movie.average_rating(),2))
    # for key in reversed(sorted(top_movie_list)):
    print ("\n ")
    #     print ("%s: %s" % (top_movie_list[key], key))
    return top_movie_list


def get_movie_id():
    user_movie_id = int(input("What's the movie ID? "))
    return user_movie_id

def options():
    while True:
        option = int(input("What would you like to know? \n \
        (1) Title of movie by ID \n \
        (2) Find average rating by movie ID  \n \
        (3) Find ratings by movie ID \n \
        (4) Find ratings by user ID \n \
        (5) Recommend top 20 movies by user ID\n "))
        if option == 1:
            print (name_of_movie_by_id(get_movie_id()))
            continue
        elif option == 2:
            print (get_avg_rating_by_movie_id(movies, get_movie_id()))
            continue
        elif option == 3:
            print ("There are {} ratings for this movie!. \n".format(len(all_ratings_by_movie_id(movies, get_movie_id()))))
        elif option == 4:
            get_user_id = int(input("What's the user ID? \n "))
            print("There are {} ratings by this user!. \n".format(len(all_ratings_by_user(movie_ratings, get_user_id))))
        elif option == 5:
            get_user_id = int(input("What's the user ID? \n "))
            not_rated = not_rated_movie_list_by_user(movies, get_movies_list_by_user_id(movies, get_user_id))
            not_rated = sorted(not_rated, key=lambda movie: movie.average_rating())
            top_movies_list(filter_movies(not_rated), movies)


def main():
    get_movie_ratings()
    options()



if __name__ == '__main__':
    main()
