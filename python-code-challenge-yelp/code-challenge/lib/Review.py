class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        restaurant.reviews_list.append(self)
        customer.add_review(restaurant, rating)

    def rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews

    def review_customer(self):
        return self.review_customer

    def review_restaurant(self):
        return self.review_restaurant
