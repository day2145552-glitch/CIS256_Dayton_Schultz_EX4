# Dayton Schultz
# CIS256 Spring '26
# Exercise 4
# test_guess_the_word.py

from guess_the_word import choose_word, process_guess, WORD_LIST

# test selected word
def test_choose_word():
    word = choose_word()
    assert word in WORD_LIST

# test that correct letters return TRUE
def test_correct_guess():
    word = "python"
    guessed_letters = set()
    result = process_guess(word, "p", guessed_letters)
    assert result == True
    assert "p" in guessed_letters

# test that wrong letter returns FALSE
def test_incorrect_guess():
    word = "python"
    guessed_letters = set()
    result = process_guess(word, "z", guessed_letters)
    assert result == False
    
