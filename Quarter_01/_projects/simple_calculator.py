# this file contains the code of simple calculator

# getting input form the user and store it into a variable

num1 = float(input("Please enter first Number : "))
num2 = float(input("PLease enter second Number : "))
operation = input("Enter the operation(+,-,*,/) : ")

if operation == "+":
    print(num1+num2)
elif operation == "-":
    print(num1-num2)
elif operation == "*":
    print(num1*num2)
elif operation == "/":
    print(num1/num2)
else:
    print("Enter valid operation.")
