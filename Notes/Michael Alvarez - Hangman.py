import random
word_list = ['sphinx', 'concatenation', 'pharaoh', 'liaison', 'nugget',
             'yacht', 'conscience', 'playwright', 'nightmare', 'handkerchief']
word = random.choice(word_list)
print(word)
output = []
length = (len(word))
for i in range(length):
    output.append('_')
    print(output)
letters_guessed = []
guesses = 8
while guesses > 0:

    # Ask for input
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)

# Check to see if the letter is in the word
    if guess in word:
        print("I FOUND ONE!!!!!")
    else:
        guesses -= 1
    print("You have %s guesses left" % guesses)

print("GAME OVER")
