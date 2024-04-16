fruits = ["apple", "orange", "banana", "apple", "grape", "orange", "kiwi", "apple"]


def sort_fruits(fruitlist):
    apple_list = []
    orange_list = []
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
