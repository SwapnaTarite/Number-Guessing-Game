#Number Guessing Game
import random
counter=0
Number=random.randint(1,100)
while True:
    Guess=int(input("Guess the number (between 1 to 100) :"))
    counter=counter+1
    print(Number)
    if Guess==Number:
            print(f"Congratulations! You Guessed the number in {counter} attempts .")
            break
    elif Guess<Number:
            print("Too low!  Try again")
    elif Guess>Number:
            print("Too High! Try again")
    else:
        pass
            

          
