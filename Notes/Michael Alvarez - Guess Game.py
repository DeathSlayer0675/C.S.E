import random

myname = input('Hello, what is your name?')
print('Well', myname, 'am thinking of a number between 1 and 50')
number = random.randint(1, 50)
guess = 0
while guess < 4:
      guess_number = int(input('Enter a number:'))
      guess += 1
if guess_number < number:
 print("Your guess is too low")

if guess_number > number:
 print("Your guess is too high")

if guess_number == number:
 print("Your guess is correct the number is", (number))

if guess == 4:
 print("The number I was thinking of is", (number))