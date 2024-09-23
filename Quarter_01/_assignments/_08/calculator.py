# this file contains the code of simple calculator
# assignment number 08


# calculator functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
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
    return input("Enter your choice. (1, 2, 3, 4) : ")

# function to get input
def get_input():
    a = float(input("Enter first number: "))
    b = float(input("Enter the second number: "))
    return a , b

# mian funtion
def main():
    while True:
        choice = get_operation_choice()
        # check if input of the operation is a valid
        if choice in ['1', '2', '3', '4']:
            a, b = get_input()

            if choice == "1":
                print(f"Result : {add(a, b)}")
            elif choice == "2":
                print(f"Result : {subtract(a, b)}")
            elif choice == "3":
                print(f"Result : {multiply(a, b)}")
            elif choice == "4":
                print(f"Result : {divide(a, b)}")
        else:
            print("Invalid input: Enter a valid operator.")

        # ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes / no) :").lower()
        if another_calculation != "yes":
            print("Exiting the calculator.")
            break


# calling main function
main()