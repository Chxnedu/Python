from restaurantclass import Restaurant
# now to make an instance using the class

restaurant = Restaurant("Crunchies", "FastFood")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()
