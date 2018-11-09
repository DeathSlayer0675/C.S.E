import random

n = random.randint(1, 10)
guess = int(raw_input("Enter an integer from 1 to 10: "))

while n != "Guess":

    raw_input = 
    if guess < n:
        print("Higher")
        guess = int(raw_input("Enter an integer from 1 to 10: "))
    elif guess > n:
        print("Lower")
        guess = int(raw_input("Enter an integer from 1 to 10: "))
    else:
        print("You guessed it!")