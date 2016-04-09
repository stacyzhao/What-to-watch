class Rating():

    def __init__(self, row):
        self.user = int(row["user_id"])
        self.item_id = row["item_id"]
        self.rating = int(row["user_rating"])

    def __str__(self):
        # return "{} : {}".format(self.user, self.rating)
        return "{} : {} : {}".format(self.item_id, self.rating, self.user)
