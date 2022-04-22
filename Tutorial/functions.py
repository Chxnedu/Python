# here we learn how to create functions. they're like scripts in bash.
# to declare a function, use def name_of_function():

# def welcome_users():
#    name = input("Hello, what is your name?")
#    print("Welcome, " + name )

# to call a function, just use the name_of_function()
# welcome_users()

# you can also specify a parameter or parameters everytime you call a function
# def hello_users(name, age):
#    print("Hello " + name +"," " You are " + str(age))
#  or this  print("Hello " + name + "," " You are " + age)

# hello_users("Chxnedu", 20)

# you can use the return statement with functions. it returns the value back to the caller
def cube(num):
    return num*num*num

print(cube(4))