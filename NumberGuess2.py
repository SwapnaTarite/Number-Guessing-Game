'''Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level'''
import random
counter=0
Number=random.randint(25,50)
while True:
    Guess=int(input("Guess the number :\n min 25  and maximum 50 :"))
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



          

