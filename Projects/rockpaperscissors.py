# a game of rock paper scissors with the computer, my way
import random

userscore = 0
compscore = 0
# tracking the scores

while userscore != 3 and compscore != 3:
# looping the code as long as the user or computer don't reach a score of 3
    user_choice = input('Pick between rock, paper, and scissors: ')
    choices = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(choices)
    if user_choice not in choices:
# a condition to check for coconut heads
        print("That's not an option, you no de read instructions!?")
        break
    else:
# the game code itself
        print("You picked " + user_choice + ", and the computer picked " + comp_choice)
        if user_choice == comp_choice:
            print("It's a tie!")
        elif user_choice == 'rock':
            if comp_choice == 'paper':
                compscore += 1
                print('Oops!')
            else:
                userscore += 1
                print('Yaay!')
        elif user_choice == 'paper':
            if comp_choice == 'rock':
                userscore += 1
                print('Yaay!')
            else:
                compscore += 1
                print('Oops!')
        elif user_choice == 'scissors':
            if comp_choice == 'rock':
                compscore += 1
                print('Oops!')
            else:
                userscore += 1
                print('Yaay!')

        print("User: " + str(userscore) + "\nComputer: " + str(compscore))

# checking whether the user or the computer got to 3 first
        if userscore == 3:
            print("You won the best out of 3")
            break
        elif compscore == 3:
            print("You lost the best out of 3")
            break
        else:
            playagain = input('Do you want to play again? y/n ')
            if playagain == 'y':
                userscore = userscore
                compscore = compscore
            else:
                break