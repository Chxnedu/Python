# a small 'test your knowledge' type project to help me familiarize with classes

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print('The name of the restaurant is ' + self.restaurant_name +
              ' and they specialize in ' + self.cuisine_type )


    def open_restaurant(self):
        print(self.restaurant_name + ' is now Open!')