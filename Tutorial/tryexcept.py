# the try except block is used to account for errors in code. for example

# number = int(input('Enter a number: '))
# print(number)
# in this code, the user is supposed to enter a number as input. if the user has strong head and goes ahead to
# enter a string instead, the code breaks and throws an error. to account for that, we use a try except block

try:
    number = int(input('Enter a number: '))
    print(number)
#except:
#    print('Invalid Input! You think say you wise abi??')

# the best practice for using except is to specify the exact error. You can use that to specify different
# types of errors
except ValueError:
    print('Invalid Input! You think say you wise abi??')
