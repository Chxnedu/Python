from classfile import User
from classfile import Restaurant
from classfile import IceCreamStand
from classfile import Admin
# now to make an instance using the class

restaurant = Restaurant("Cruchies", "FastFood")

restaurant.number_served = 12


restaurant.increment_number_served(89)

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
# restaurant.set_number_served('17')
print(restaurant.number_served)

restaurant.describe_restaurant()
restaurant.open_restaurant()


chxnedu = User("Chinedu", "Oji", "20", "Playing video games")
kachi = User("Kachi", "Ochemba", "21", "Coding")

chxnedu.describe_user()
kachi.greet_user()

chxnedu.increment_login_attempts()
chxnedu.increment_login_attempts()
chxnedu.increment_login_attempts()
chxnedu.increment_login_attempts()
chxnedu.increment_login_attempts()
chxnedu.increment_login_attempts()

print(chxnedu.login_attempts)

chxnedu.reset_login_attempts()

print(chxnedu.login_attempts)

mynewbusiness = IceCreamStand('HawkerHQ', 'Ice-Cream')
mynewbusiness.describe_restaurant()
mynewbusiness.display_flavors()

chibuike = Admin('chibuike', 'egwu', '19', 'grinding')
chibuike.describe_user()
chibuike.privileges.show_privileges()

collins = Admin('collins', 'egwu', '21', 'influencing')
collins.describe_user()
collins.privileges.show_privileges()