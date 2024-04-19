# Complete the following questions. This assignment must be submitted
# on Monday April 15th, 2024, by 11:59pm to recieve full credit. 

#1. Look up and read about the Range keyword on W3 schools. 
# Do the "try now" example provided on the article page and in your async document, 
# in your own words, describe what the range() function does.  
"The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number."
# Prompt # 1 
# Create a python list of fruits. 
# Your list of fruits should contain mainly apples, organges,
# and a few other random fruits of your choice. 
# Once you have your list, create a python function that 
# uses a python For loop to go through the fruit list. 
# If the loop runs into a fruit with the value of apple, send 
# that value to a new list variable called apple list. If the loop encounter 
# a fruit with the value of orange, it should move the item to 
# a new list variable called orange list. Else, if the loop encounters
# any other fruit, it should move that item to a list called unsorted fruits.
# Creating a list of fruits
fruits = ["apple", "orange", "banana", "apple", "grape", "orange", "kiwi", "apple"]


def sort_fruits(fruitlist):
    applelist = []
    orangelist = []
    unsortedfruits = []
    for fruit in fruitlist:
        if fruit == "apple":
            applelist.append(fruit)
        elif fruit == "orange":
            orangelist.append(fruit)
        else:
            unsortedfruits.append(fruit)

    return applelist, orangelist, unsortedfruits
applelist, orangelist, unsortedfruits = sort_fruits(fruits)

print("List of Apples:", applelist)
print("List of Oranges:", orangelist)
print("Unsorted Fruits:", unsortedfruits)

# Note: In order to recieve the minimum amount of credit, 
# write down any clues or keywords that you recognize in the prompt 
# and describe how you would solve this problem if you get stuck. 