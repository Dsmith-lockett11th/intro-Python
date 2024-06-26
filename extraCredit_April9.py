# Prompt #1. 
#Create a function that will count the number of characters in a string
# that is passed in by a user. The string value can be passed in either as 
# a paramter or by using the input function.
def countnumbers(string):
    return len(string)
user = input('enter a string?')
print('number of characters:',
      countnumbers(user))
# Prompt #2.
# You have been hired by an amusement park to develop a function
# that allows users to access their roller coasters by entering their age
# and height. Your program should take the user's height and age as parameters.
# Your client has very specific requirements for thier guests 
# to ride their roller coasters and have provided you with the following 
# conditions that they would like your program to check for. 

# user must be atleast 5.2 or taller and atleast 14 years old or older 
# in order to ride roller coaster 1. 

# if the user is shorter than 5.2 but at least 14 years of age or older,
# they can ride the roller coaster 2.

# if the user is shorter than 5.2 and also younger than 14 years of age,
# they can ride roller coaster 3. 

# if the user enters information incorrectly, give them an error message
# and tell them that they entered their information incorrectly. 
def roller_coaster_access(age, height):
    if height >= 5.2:
        if age >= 14:
            print("You are eligible to ride Roller Coaster 1.")
        else:
            print("You are eligible to ride Roller Coaster 2.")
    elif age >= 14:
        print("You are eligible to ride Roller Coaster 2.")
    else:
        print("You are eligible to ride Roller Coaster 3.")

def checkout_scanner():
    cart = []
    total_price = 0
    
    while True:
        item_name = input("Enter the name of the item: ")
        item_price_str = input("Enter the price of the item: ")
        
        try:
            item_price = float(item_price_str)
        except ValueError:
            print("Error: Please enter a valid price.")
            continue
        
        cart.append((item_name, item_price))
        total_price += item_price
        
        choice = input("Would you like to continue shopping? (y/n): ")
        if choice.lower() != 'y':
            break
    
    print("\nYour cart:")
    for item in cart:
        print(f"{item[0]} - ${item[1]}")
    print(f"Total price: ${total_price}")

age = int(input("Enter your age: "))
height = float(input("Enter your height (in feet): "))
roller_coaster_access(age, height)

checkout_scanner()

# Prompt # 3.
# You have been hired as an engineer to develop a checkout scanner system.
# when a user puts in a name of an item and the price of the item it gets added to their cart.
# your function to loop/ repeat and ask the user if they are done shopping or would like to continue
# if the enter 'y' for yes, continue the loop and allow the user to put in another
# item name and item price. If they enter 'n' for no, calculate the total price of items as
# well as print the all the item names.

# bonus for prompt # 3.
# create a discount system where, when the user enters 'y' for being done shopping,
# ask the user if they have a discount code. Depending on the code they enter they will
# recieve 10%, 25%, or 50% off of their total purchase.

def checkout_scanner():
    cart = []
    total_price = 0
    
    while True:
        item_name = input("Enter the name of the item: ")
        item_price_str = input("Enter the price of the item: ")
        
        try:
            item_price = float(item_price_str)
        except ValueError:
            print("Error: Please enter a valid price.")
            continue
        
        cart.append((item_name, item_price))
        total_price += item_price
        
        choice = input("Would you like to continue shopping? (y/n): ")
        if choice.lower() != 'y':
            break
    
    print("\nYour cart:")
    for item in cart:
        print(f"{item[0]} - ${item[1]}")
    print(f"Total price: ${total_price}")

checkout_scanner()
