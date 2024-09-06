# This file contains the solution of 7th assignment 
# Python Programming Assignment: Number Exploration Tool

# Ask for the user's name
name = input("Enter your name: ")
    
# Get three favorite numbers from the user
numbers = []
for i in range(1, 4):
    number = int(input(f"Enter your {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd'} favorite number: "))
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

# Calculate the sum of the numbers
total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
    
# Check if the sum is a prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(total_sum):
    print(f"Wow, {total_sum} is a prime number!")
else:
    print(f"{total_sum} is not a prime number, but it's still a great number!")
