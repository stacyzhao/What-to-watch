class Movie():
    def __init__(self, movie_id, title):
        self.id = movie_id
        self.title = title

    def __str__(self):
        return "{} : {}", self.id, self.title
