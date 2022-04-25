# a basic guessing game where we specify a particular word and the user has to guess the word till
# they get the correct word

word = "goat"
guess = ""
# created an empty variable, guess. this will contain the users guesses and check them against the word

while guess != word:
    guess = input("enter the correct word: ")
# the condition here is for guess to not be the word. as far as guess isn't the correct word, it'll keep
# prompting you to enter the correct word

print("You Win!")
# when you guess the correct word, the loop breaks and prints out you win.