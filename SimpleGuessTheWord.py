import random

#   You can also just replace the input() with a string list of words
words = input("Give a list of words (Separate with space): ")

wordList = words.split(" ")
word = random.choice(wordList)  #   Word to guess
hiddenWord = []                 #   Hidden version of word
for letter in word:
    hiddenWord.append("_")

lives = 8 

while True:
    print(f"Guesses left: {lives}")
    print(hiddenWord)
    guess = input("Guess a letter: ")

    if len(guess) != 1 or guess == "" or guess == " ":
        print("Invalid input, try again\n")
    elif guess not in word:
        print("Incorrect.\n")
        lives -= 1
    else:
        print("Correct.\n")
        for i in range(len(word)):      #   Adds the letter to hiddenWord, if correct
            if(word[i] == guess ):
                hiddenWord[i] = guess

    if "_" not in hiddenWord:         #   If all letters are correctly guessed, you win.
        print(f"You guessed the word correctly: {word}\nYou won.\n") 
        break

    if lives == 0: 
        print(f"Your guesses ran out. The word was {word}\nYou lost.\n")
        break

print("The End.")
# T H E  E N D