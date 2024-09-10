
```markdown
# Number Exploration Tool

## Overview

This Python script is designed to engage users in a fun exploration of their favorite numbers. The script performs the following tasks:

1. Prompts the user to enter their name.
2. Collects three favorite numbers from the user.
3. Analyzes whether each number is even or odd.
4. Displays each number along with its square.
5. Calculates the sum of the three numbers.
6. Checks if the sum is a prime number and provides appropriate feedback.

## Code Explanation

### 1. User Input

The script starts by asking the user for their name and then requests three favorite numbers:

```python
# Ask for the user's name
name = input("Enter your name: ")

# Get three favorite numbers from the user
numbers = []
for i in range(1, 4):
    number = int(input(f"Enter your {i}{'st' if i == 1 else 'nd' if i == 2 else 'rd'} favorite number: "))
    numbers.append(number)
```

### 2. Greeting the User

Once the numbers are collected, the script greets the user and proceeds to analyze the numbers:

```python
# Greet the user
print(f"\nHello, {name}! Let's explore your favorite numbers:\n")
```

### 3. Even/Odd Analysis

The script determines if each number is even or odd and stores this information:

```python
# Create an empty list
even_odd_info = []

for num in numbers:
    if num % 2 == 0:
        even_odd_info.append((num, "even")) 
    else:
        even_odd_info.append((num, "odd"))
```

It then prints out the even/odd status of each number:

```python
# Display the even/odd info
for num, parity in even_odd_info:
    print(f"The number {num} is {parity}.")
```

### 4. Number and Square

The script calculates and displays each number along with its square:

```python
# Print the number and its square
print("\nHere are your numbers and their squares:")
for num in numbers:
    print(f"The number {num} and its square: ({num}, {num**2})")
```

### 5. Sum of Numbers

It computes the sum of the three numbers and prints it:

```python
# Calculate the sum of the numbers
total_sum = sum(numbers)
print(f"\nAmazing! The sum of your favorite numbers is: {total_sum}")
```

### 6. Prime Number Check

Finally, the script checks if the sum is a prime number:

```python
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
```

## How to Run

1. Save the script as `number_exploration_tool.py`.
2. Run the script using Python 3 by executing the command:

   ```bash
   python number_exploration_tool.py
   ```

3. Follow the on-screen prompts to enter your name and favorite numbers.

## Example Output

```
Enter your name: Alice
Enter your 1st favorite number: 7
Enter your 2nd favorite number: 14
Enter your 3rd favorite number: 21

Hello, Alice! Let's explore your favorite numbers:

The number 7 is odd.
The number 14 is even.
The number 21 is odd.

Here are your numbers and their squares:
The number 7 and its square: (7, 49)
The number 14 and its square: (14, 196)
The number 21 and its square: (21, 441)

Amazing! The sum of your favorite numbers is: 42
42 is not a prime number, but it's still a great number!
```
```