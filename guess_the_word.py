# Dayton Schultz
# CIS256 Spring '26
# Exercise 4
# guess_the_word.py

import random

# words for hangman
WORD_LIST = ["python", "computer", "keyboard", "developer", "hangman"]

# select random word from WORD_LIST
def choose_word():
    return random.choice(WORD_LIST)

# display word with guessed letters revealed
def display_word(word, guessed_letters):
    display = ""

    #loop through each letter
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_"
    return display.strip()

# process user's guess
def process_guess(word, guess, guessed_letters):
    guessed_letters.add(guess)
    if guess in word:
        return True
    else:
        return False
# Main function
def play_game():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print ("Welcome to Hangman!")

    # Game loop
    while attempts > 0:
        print("\nCurrent word:", display_word(word, guessed_letters))
        guess = input("Enter a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Enter only one letter.")
            continue
        if guess in guessed_letters:
            print("Already guessed.")
            continue
        if process_guess(word, guess, guessed_letters):
            print("Correct guess!")
        else:
            print("Wrong guess!")
            attempts -= 1
            print("Attempts left:", attempts)
        if all(letter in guessed_letters for letter in word):
            print("\nYou Win! Word:", word)
            return
    print("\nGame Over! Word:", word)
if __name__ == "__main__":
    play_game()
    
