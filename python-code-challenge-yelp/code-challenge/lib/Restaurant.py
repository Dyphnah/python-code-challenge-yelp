
class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.NAME = name
        self.reviews_list = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.NAME

    @classmethod
    def all(cls):
        return cls.all_restaurants

    def reviews(self):
        return self.reviews_list

    def customers(self):
        customers = []
        for review in self.reviews_list:
            customers.append(review.customer)
        return list(set(customers))

    def average_star_rating(self):
        if not self.reviews_list:
            return 0
        total_rating = sum(review.rating for review in self.reviews_list)
        return total_rating / len(self.reviews_list)
# Check Code


taste_haven = Restaurant("Taste Haven")
print(taste_haven.NAME)

# customer_reviews =
