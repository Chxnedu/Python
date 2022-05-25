# a small 'test your knowledge' type project to help me familiarize with classes

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.restaurant_name +
              ' and they specialize in ' + self.cuisine_type )


    def open_restaurant(self):
        print(self.restaurant_name + ' is now Open!')

    def set_number_served(self, no_of_customers):
        self.number_served = no_of_customers
        print('They have served ' + self.number_served + ' customers')

    def increment_number_served(self, served_today):
        self.number_served += served_today


class User:
    def __init__(self, first_name, last_name, age, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.hobby = hobby
        self.login_attempts = 0

    def describe_user(self):
        print('My name is ' + self.first_name + " " + self.last_name)
        print('I am ' + self.age + ' years old')
        print('My hobby is ' + self.hobby )

    def greet_user(self):
        print('Good Day ' + self.first_name + " " + self.last_name )

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class IceCreamStand(Restaurant):
# a new class inheriting from the restaurant class

    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry'] # a new attribute for icecreamstand


    def display_flavors(self):
        print("The flavors available are: " + str(self.flavors))
    # a method exclusive to only the icecreamstand class


class Privileges():

    def __init__(self):
        self.user_privileges = ['can create post', 'can delete post', 'can edit profile']

    def show_privileges(self):
        print('This user has the following priveleges: ' + str(self.user_privileges))




class Admin(User):
# a new class inheriting from the user class

    def __init__(self, first_name, last_name, age, hobby):
        super().__init__(first_name, last_name, age, hobby)
        self.privileges = Privileges()











