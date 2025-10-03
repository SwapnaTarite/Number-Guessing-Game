'''Implement a feature that limits the number of guesses a player can make. If
the player runs out of attempts, the game should end, and the correct number
should be revealed. '''

import random
counter=0
Number=random.randint(1,50)
i=5
while i>=1:
    print("Guess the number (between 1-50 ) in", i , "attempts :")
    Guess=int(input())
    counter=counter+1
    if Guess==Number:
            print(f"Congratulations! You Guessed the number in {counter} attempts .")
            break
    elif Guess<Number:
            print("Too low!  Try again")
    elif Guess>Number:
            print("Too High! Try again")
    else:
        pass
    i=i-1
else:
    print(f"Oops! You Run out of attempts and The correct number is {Number}")
