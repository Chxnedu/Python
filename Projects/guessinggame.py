# a basic guessing game where we specify a particular word and the user has to guess the word till
# they get the correct word
# now i update the guessing game to give the user a limit of 3 guesses

word = "goat"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
try_2 = 2
try_1 = 1
# created 3 variables

print("You have 3 guesses")
while guess != word and not(out_of_guesses):
# checks if both conditions are true
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
        if guess_count == 1 and guess != word:
            print("You have " + str(try_2) + " guesses left")
        elif guess_count == 2 and guess != word:
            print("You have " + str(try_1) + " guess left")
        elif guess_count == 3 and guess != word:
            print("You're out of guesses")
        else:
            print("")
# an if statement that checks if the guess count is less than the guess limit, then prompts the user and
# increments the guess count by 1
    else:
        out_of_guesses = True
# an else statement that triggers if the guess count is greater than or equal to the limit

# the while loop can be broken if the user gets the correct word before they are out of tries or if they
# run out of tries

if out_of_guesses:
    print(" You loose!")
else:
    print("You win!")
# if the user put the correct word, that means he did not run out of guesses and the if statement is false
# so the else statement triggers
