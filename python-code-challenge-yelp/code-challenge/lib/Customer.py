from Review import Review
#Initializers, Readers, and Writers

class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.reviews_list = []
        Customer.all_customers.append(self)

    def given_name(self):
        return self.given_name

    def family_name(self):
        return self.family_name

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers
#Testing Code

dyphnah = Customer("Dyphnah", "Nyamongo")
caro = Customer("Caro", "James")
stella = Customer("Stella", "Kemmy")

print(dyphnah.full_name())
print(caro.full_name())

# Printing all customers
for customer in Customer.all():
    print(customer.full_name())



    # def add_review(self, restaurant, rating):
    #     review = Review(self, restaurant, rating)
    #     self.reviews_list.append(review)

    # def restaurants(self):
    #     restaurants = []
    #     for review in self.reviews_list:
    #         restaurants.append(review.restaurant)
    #     return list(set(restaurants))

    # def num_reviews(self):
    #     return len(self.reviews_list)

    # @classmethod
    # def find_by_name(cls, name):
    #     for customer in cls.all_customers:
    #         if customer.full_name() == name:
    #             return customer

    # @classmethod
    # def find_all_by_given_name(cls, name):
    #     return [customer for customer in cls.all_customers if customer.given_name == name]
