# a while loop is used to loop through a set condition. python will check the condition, and if
# it's true, it'll loop throughout the code

i = 1
while i <= 10:
    print(i)
    i += 1
# this loop first checks if i is greater or equal to 10, then prints the value of i, and increments it to 2
# python then loops through the code again, this time i = 2, it still fulfills the condition, so the same
# thing happens and the value of i is now 3. this repeats itself until i = 11, where it does not satisfy
# the condition again, so the loop is broken and the code moves on to the next line

print("you're done with the loop")