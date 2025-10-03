'''Add a feature that keeps track of the fewest attempts it took to guess the
number correctly. The program should display this "best score" at the end of
each game
. '''

import random
bestscore=0
while True:
        counter=0
        Number=random.randint(1,50)
        i=5
        while i>=1:
            print("Guess the number (between 1-50 ) in", i , "attempts :")
            Guess=int(input())
            counter=counter+1
            if Guess==Number:
                    print(f"Congratulations! You Guessed the number in {counter} attempts .")
                    bestscore=counter
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
        res=input("Do you want to play again ?(y/n) :").lower()
        if res=='y':
            if counter<bestscore:
                bestscore=counter
        else:
            print("The best score is :",bestscore)
            break



