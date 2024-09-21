# this file contains the code of simple calculator
# assignment number 08


# calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b);
    if b == 0:
        return "Error: Division by 0 is not allowed."
    else:
        return a / b
    

# function to get user input for operation
def get_operation_choice():
    print(f"""\nPlease Select operation:
                1. Add
                2. Subtract
                3. Multiply
                4. Divide""")
    return input(int("Enter your choice. (1, 2, 3, 4)"))