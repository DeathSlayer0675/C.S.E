number = 7
guesses = 5
win = False

while guesses > 0:
    num = int(input("Pick a number between 1 and 10."))
    if num > 10:
        print("Your number is too high!")
    elif num > number:
        print("The number is lower!")
        guesses = guesses - 1
    elif num < number:
        print("the number is higher!")
        guesses = guesses - 1
    elif num == number:
        print("Correct! ")
        guesses = 0