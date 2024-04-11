# Async Activity April 8th, 2024

# 1. In your own words, describe what a while loop is?
'With the while loop we can execute a set of statements as long as a condition is true.'
#2. Create a function that uses a while loop to determine if a user has typed in 
# the the correct word guess. If the user types in the wrong word, your program 
# should inform them that their guess was inccorect and to try again, but if the
# user guesses the word correctly, your program shoul tell the user they have 
# guessed correctly and have won the game, stopping the loop.

def word_guess_game(correct_word):
    guessed_word = input("Guess the word: ")
    
    while guessed_word != correct_word:
        print("Incorrect guess. Try again.")
        guessed_word = input("Guess the word: ")
    
    print("Congratulations! You guessed the word correctly and won the game.")

# Example usage:
correct_word = "Cat"
word_guess_game(correct_word)
