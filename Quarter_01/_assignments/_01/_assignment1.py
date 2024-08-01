#   1-Basic Printing
print("Hello, World!")
print("Wasif")

#   2-Printing Multiple Items
first_name = "Wasif"
last_name = "Nawaz"
print(first_name, last_name)

num1 = 1
num2 = 2
num3 = 3
print(num1, num2, num3)

#   3-Printing Special Characters
print("Hello \nWorld!")     # new line character
print("Hello \tWorld!")     # tab character

#   4-Using the "sep" Parameters
fruit_1 = "apple"
fruit_2 = "banana"
fruit_3 = "cherry"
print(fruit_1, fruit_2, fruit_3, sep = ",")   # seperated by comma
print(num1, num2, num3, sep = "-")  # seperated by hyphen

#   5-Using the end parameter
print("Hello","World!", end=" \n")
print(num1,num2, end="")

#   6-Escape Characters
print(f'\nHe said, "He is okay."')
print("This is a backslash:\\")

#   7-Combining Text & Numbers
my_age = 24
print(f"I,m {my_age} years old.")
print(f"I love {fruit_3}, and it is at number {num1} in my favorite list.")

#   8-Basic Loop for printing
for i in range(1, 6):
    print(i)
