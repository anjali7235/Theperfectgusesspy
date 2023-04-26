import random

randNumber = random.randint(1, 100)

userGuess = None
Guesses = 0

while (userGuess != randNumber):
    userGuess = int(input("Enter your Guess "))
    Guesses+=1
    if(userGuess==randNumber):
        print("You guessed the Right Number")
    else:
        if(userGuess > randNumber):
            print("You guessed the larger Number, please guess the smaller Number ")
        else:
            print("You guessed the smaller Number, please guess the larger Number ")

print(f"You guess the number in {Guesses} guesses")
