# Async work Monday March 18th, 2024.

#1. Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.
def count_characters(word):
    print(len(word))

    

# You must be write down and explain how your program 
# works in complete sentences in order to get full credit. 

# 2. Use your notes, W3schools, and what we have learned in class to develop
# a simple rock, paper, scissors game. Your game should allow the user to enter a letter
# that will represent the values rock, paper, and scissors (ex. r = rock, p = paper, s= scissors).
import random

def game():
    choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
    user_choice = input("Enter your choice (r for rock, p for paper, s for scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please enter 'r', 'p', or 's'.")
        return
    computer_choice = random.choice(list(choices.keys()))
    print("Your choice:", choices[user_choice])
    print("Computer's choice:", choices[computer_choice])
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'r' and computer_choice == 's') or \
         (user_choice == 'p' and computer_choice == 'r') or \
         (user_choice == 's' and computer_choice == 'p'):
        print("You win!")
    else:
        print("Computer wins!")
game()




# EXTREMELY IMPORTANT NOTE
# at the top of you page write import random
# use the random.randrange(1,3) function to develop your random value logic 
# for your rock, paper, scissor game. 

# Please describe the steps you took, or if you weren't able to complete this activity,
# the steps you would've taken to solve this problem in complete sentences. 
# This must be completed in order to get full credit.  