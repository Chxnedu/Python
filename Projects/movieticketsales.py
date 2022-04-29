# a small project to test what I have learned so far
# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3,
# the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12,
# the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie
# ticket.

ticket_prices = ["free", "$10", "$15"]
# age = input("How old are you? ")

# first solution using if statements and lists

# if int(age) < 3:
#    print("Your ticket is " + ticket_prices[0])
# elif 3 <= int(age) <= 12:
#    print("Your ticket is " + ticket_prices[1])
# elif int(age) > 12:
#    print("Your ticket is " + ticket_prices[2])

# second solution using while loops
active = True

while active:
    age = input("How old are you? ")

    if int(age) < 3:
        print("Your ticket is " + ticket_prices[0])
    elif 3 <= int(age) <= 12:
        print("Your ticket is " + ticket_prices[1])
    elif int(age) > 12:
        print("Your ticket is " + ticket_prices[2])
    else:
        active = False








