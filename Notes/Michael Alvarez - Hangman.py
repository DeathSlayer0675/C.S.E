import random
import sys


word_list = ['sphinx', 'concatenation', 'pharaoh', 'liaison', 'nugget',
             'yacht', 'conscience', 'playwright', 'nightmare', 'handkerchief']
guesses = 8
guess_word = []
secretWord = random.choice(word_list)
length_word = len(secretWord)
alphabet = ("abcdefghijklmnopqrstuvwxyz")
letter_storage = []


def beginning():
    print("Hello Beaner!\n")

    while True:
        name = input("Please enter Your name\n").strip()

        if name == '':
            print("You can't do that! No blank lines")
        else:
            break


beginning()


def newfunc():
    print("Well, that's perfect moment to play some Hangman!\n")

    while True:
        gamechoice = input("Would You?\n").upper()

        if gamechoice == "YES" or gamechoice == "Y":
            break
        elif gamechoice == "NO" or gamechoice == "N":
            sys.exit("That's a shame! Have a nice day")
        else:
            print("Please Answer only Yes or No")
            continue


def change():

    for character in secretWord:
        guess_word.append("-")

    print("Ok, so the word You need to guess has", length_word, "characters")

    print("Be aware that You can enter only 1 letter from a-z\n\n")

    print(guess_word)


def guessing():
    guesses = 8

    while guesses > 0:

        guess = input("Pick a letter\n").lower()

        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else:

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for i in range(length_word):
                    if secretWord[i] == guess:
                        guess_word[i] = guess
                        print(guess_word)

                if '-' not in guess_word:
                    print("You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guesses -= 1
                print(guesses)
                if guesses < 1:
                    print(" Sorry Mate, You lost :<! The secret word was", secretWord)


change()
guessing()

print("Game Over!")
