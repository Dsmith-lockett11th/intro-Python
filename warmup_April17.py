# Warm up Tuesday April 17th, 2024.

import random

# 1. In your own words, explain the difference between an Python For Loop and a
# Python While Loop.
'A for loop is used for iterating over a sequence and With the while loop we can execute a set of statements as long as a condition is true.'
# 2. Create a loop that will iterate over a list of numbers. For evey number in your loop,
# it should multiply that number by 3. 
numberlist = [1,2,3,4,5,6,7]
for number in numberlist:
    print(number *3)
# 3. Use the following code snippet below to create a guessing game function. 
# The code below will generate a random number for you. You must write a loop that will
# ask the user to input their guess, if they guess incorrectly, the program will repeat 
# itself and ask the user to guess again. The program should continue to ask them to
# guess until they've gotten it correctly. Once they guess the correct number the program
# will congratulate them and the loop will stop. 

# generates a random number between 1 and 10
def gussingGame:
randomNumber = random.randint(1, 10)
print(f'Random number value is: {randomNumber}')
i = int(input('please guss a number:'))
if i == randomNumber:
    print('you won the game')

gussingGame()