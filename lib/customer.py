class Customer:
    all_customers = []
    
#It also creates an empty _reviews list for the customer 
# and adds the customer instance to the all_customers list.

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        self._reviews = []
        Customer.all_customers.append(self)


#The given_name, family_name, and full_name methods are getter 
# methods that return the corresponding attributes of a customer object.
    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return f"{self._given_name} {self._family_name}"

    def num_reviews(self):
        return len(self._reviews)


#The find_by_name class method takes a name parameter and searches 
# for a customer with a matching full name in the all_customers list. If found, it returns the customer object; otherwise, it returns None.
    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

#The find_all_by_given_name class method takes a name parameter and
# searches for all customers with a matching given name in the all_customers list. It returns a list of matching customer objects.
    @classmethod
    def find_all_by_given_name(cls, name):
        customers = []
        for customer in cls.all_customers:
            if customer.given_name() == name:
                customers.append(customer)
        return customers


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all_reviews.append(self)
        customer._reviews.append(self)

    def rating(self):
        return self._rating

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.all_reviews

    def __str__(self):
        return f"Review by {self._customer.full_name()} for {self._restaurant.name()}: Rating {self._rating}"


class Restaurant:
    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


# Create customer and restaurant instances
customer = Customer("Morgan", "Jason")
restaurant = Restaurant("The KENYAN FRIED CHICKEN")

# Create a review instance
review = Review(customer, restaurant, 9.5)

#The rating() method of the review object is called 
# to retrieve the rating value and print it.
# Access the review's rating
print(review.rating()) 


#The rating() method of the review object is called to retrieve 
# the rating value and print it.
# Get all reviews
all_reviews = Review.all()
for review in all_reviews:
    print(review)

# Testing additional functionalities

# Test num_reviews()
print(customer.num_reviews())  
found_customer = Customer.find_by_name("Morgan Jason")
if found_customer:
    print(found_customer.full_name())  
else:
    print("Customer not found.")
# Test find_all_by_given_name()
matching_customers = Customer.find_all_by_given_name("Morgan")
for customer in matching_customers:
    print(customer.full_name())  