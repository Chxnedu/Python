# started out as a simple friendly addition calculator project
# time to update the calculator to run other math functions

# collecting input from the user
num_1 = input("The first number___")
num_2 = input("The second number___")

# collecting the operator
print("I can do the basic 4 mathematical operations; + - * and /")
sign = input("So which operator would you like to use?")

if sign == "+":
    sum = float(num_1) + float(num_2)
    print(sum)
elif sign == "-":
    difference = float(num_1) - float(num_2)
    print(difference)
elif sign == "*":
    product = float(num_1) * float(num_2)
    print(product)
elif sign == "/":
    quotient = float(num_1) / float(num_2)
    print(quotient)
else: print("You wan blow my head!??")


# sum = float(num_1) + float(num_2)
# we use the float() function when we want to convert input to numbers or decimals.
# you can also use int() but note that it does not take decimals

