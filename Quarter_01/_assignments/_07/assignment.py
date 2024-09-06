# This file contains the solution of 7th assignment 
# Python Programming Assignment: Number Exploration Tool

# Ask for the user's name
name = input("Enter your name: ")
    
# Get three favorite numbers from the user
numbers = []
for i in range(1, 4):
    number = int(input(f"Enter your {i}
                       {'st' if i == 1 else 'nd' if i == 2 else 'rd'} 
                       favorite number: "))
    numbers.append(number)
    
# Greet the user
print(f"\nHello, {name}! Let's explore your favorite numbers:\n")


