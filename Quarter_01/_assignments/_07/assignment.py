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

# Create an empty list
even_odd_info = []

for num in numbers:
    if num % 2 == 0:
        even_odd_info.append((num, "even")) 
    else:
        even_odd_info.append((num, "odd"))

 # Display the even/odd info
    for num, parity in even_odd_info:
        print(f"The number {num} is {parity}.")

# Print the number and its square
    print("\nHere are your numbers and their squares:")
    for num in numbers:
        print(f"The number {num} and its square: ({num}, {num**2})")
