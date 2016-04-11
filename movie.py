class Movie():
    def __init__(self, movie_id, title):
        self.id = int(movie_id)
        self.title = title
        self.ratings = []

    def __str__(self):
        return "{} : {}", self.id, self.title


    def add_rating(self, rating):
        self.ratings.append(rating)

    def average_rating(self):
        sum_of_rating = 0
        for rating in self.ratings:
            sum_of_rating += rating.score
        average_rating = sum_of_rating/len(self.ratings)
        return average_rating

    def __eq__(self, other):
        return self.id == other.id
