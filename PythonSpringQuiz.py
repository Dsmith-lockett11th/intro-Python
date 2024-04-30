# 1. What is a while loop, what is a for loop, and what is the difference between the two.
# Please write your response using complete sentences. 
'A for loop is used for iterating over a sequence and With the while loop we can execute a set of statements as long as a condition is true.'
# 2. Name and describe three python operator families. Plese write your response using complete
# sentences.
'Comparison, Logical, Arithmetic '
# 3. Create a function that will accept 3 arguements. 
# This function should multiply the first 2 arguments and then
# subtract the last argument from the sum of the first 2. 
numberlist = [1,2,3]
for number in numberlist:
    print(number *2)
# 4. Research the range() function. Then create a function that takes 2 arguements. 
# Your function should take the range of the first argument and multiply those numbers by the second 
# argument. 
x = range(3, 5, 2)
for n in x:
  print(n *2)
# 5. Create a function that will ask the user guess the correct number.
# Your function should take a user input which will be their guess. Your function should 
# generate a random number between 1 and 5. If the user guesses the number correctly, the program
# will inform the user they guessed correctly and end the game. If the user guesses incorrectly, they
# will be informed their guess is incorrect and to guess again. The user should only be able to guess
# incorrectly 3 times. If they get the 3rd attempt wrong, the program should inform they user they have lost
# the game.

#Create a function
#ask the user guess the correct number
#take a user input
#Your function should generate a random number between 1 and 5
#If the user guesses the number correctly, the program will inform the user they guessed correctly
def gussingGame()
randomNumber = random.randint(1, 5)
print(f'Random number value is: {randomNumber}')
i = int(input('please guss a number:'))
if i == randomNumber:
    print('You have correctly guessed')

gussingGame()
# 6. Create a function that will act as a deposit this week calculator. Your function should take several inputs from
# the user. Your program should ask the user what they are saving up for, how much does it cost, and how much 
# they want to deposit this week. Your program should repeat asking the user how much would they like to
# save this week, until the goal amount has been satisfied. Each time the user makes a deposit, your
# program should inform them how many weeks they have left, how much money they have deposited, and how
# much money their is remaining to reach their goal. 

#Create a function that will act as a saving calculator
#inputs from the user
#ask the user what they are saving up for and how much it is
#should ask how much they want to deposit this week


# Ex. if my goal is to save $500, and deposit $20 dollars for that week, it should tell me that 
# It will take me 25 weeks to reach my goal based on the 20 dollar deposit, I have $20 saved,
# and that I need $480 more dollars.

# If I deposit $40 dollars the next week it should tell me
# it will take 10 weeks to reach my goal based on the $40 dollar deposit, I have $60 saved, and that I need 
# $440 more dollars to reach my goal.