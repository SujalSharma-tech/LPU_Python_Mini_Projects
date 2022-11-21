# Project 1

# Number predictor 1-6

import random

RED = '\033[31m'
WHITE = '\033[m'
GREEN = '\033[32m'
score = 0
while True:
    Num_IN = int(input("Enter a number between 1-6 : "))
    if 0 <= Num_IN <= 6:
        if random.randint(0, 6) == Num_IN:
            print(GREEN, "Well Done, Your guess was correct", WHITE)
            score += 1
            user = input("Press R to play again or X for exit: ")

            if user.upper() == 'R':
                continue
            elif user.upper() == 'X':
                break
            else:
                print(RED, "Invalid Input", WHITE)
        else:
            print(RED, "Not correct, Try again", WHITE)
            continue
    else:
        print(RED, "Enter a number Between 1-6!", WHITE)
        continue
print("Your Final Score is: ", score)
