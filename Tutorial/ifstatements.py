# if statements work like normal. you give a condition and you give a command

# name = input("What is your name?")
# name = name.title()
# here, I got the name from the user, and capitalized the first letter with the .title function

# age = input("How old are you?")

# you can also use the and statement in place of or. both statements have to be
# if name == "Chxnedu" and str(age) > str(15):
#    print("You are welcome, Master " + name)

# the elif statement stands for else if. its used to check another pair of statements
# elif name == "Chxnedu" and str(age) == str(14):
#    print("Welcome " + name + ", You are of age")
# else:
#   print("Getat! You no be my Master and you're underage")

# you can use if statements to check if a value is in a list
available_games = ["tlou2","god of war", "bloodborne", "spiderman", "control"]

game = input("Which game would you like to get?")

if game in available_games:
    print("it's available!")
else:
    print("sorry, we dont have it")


