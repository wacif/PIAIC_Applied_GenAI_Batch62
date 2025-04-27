# this is assignmet-3 solution file

# 1. Simple Message
message_1 = "Hello! I,m a variable."
print(message_1)

# 2. Simple Messages
message_2 = "This is message 2."
print(message_2)

message_2 = "This is updated message."
print(message_2)

# 3. Personal Message
student_name = "Jhon"
print(f'Hello {student_name}, shall we study togather?')

# 4. Name Cases
person_1 = "smith"
print(f'This is Uppercase: {person_1.upper()}')
print(f'This is Lowercase: {person_1.lower()}')
print(f'This is title case: {person_1.title()}')

# 5. Famous Quote
quote = '''Quote from Mawlana Jalal-al-Din Rumi, "What you seek is seeking you."'''
print(quote)

# 6. Famous Quote 2
famous_person = "Rumi"
message = '''"I am smiling at myself today.
            There's no wish left in this heart.
            Or perhaps there is no heart left.
            Free from all desire, I sit quietly like Earth."'''
print(f'Quote from {famous_person}, {message}')

# 7. Stripping Names
person_2 = " \t\n   Jackson\t     Smith    \n"
print(person_2)
print(f'This is strip: {person_2.strip()}')
print(f'This is rstrip: {person_2.rstrip()}')
print(f'This is lstrip: {person_2.lstrip()}')

# 8. Variable Sum
x = 5
y = 10
z = 15
print(x + y + z)

# 9. Variable Swap
a = "Hello"
b = "Cat"
print(f'Varibles before swap: a = {a} , b = {b}')

a, b = b, a
print(f'Varibles after swap: a = {a} , b = {b}')

# 10. Favorite Color
favorite_color = "Black"
print(favorite_color)

new_color = favorite_color
print(new_color)

# 11. Changing Pet Name
pet_name = "Buddy"
pet_name = "Max"
print(pet_name)

# 12. Observing Name Error
sunshine = True
#print(sunrise)
#it will give us NameError

# 13. Reassigning Score
score = 100
print(score)
score = 85
print(score)

# 14. City Name
city : str = "Karachi"
print(city)

# 15. Title Case Text
text = "python programming"
print(text.title())

# 16. Lowercase Conversion
sample_text = "PhySics is tHE Branch of NatuRal Science."
print(sample_text.lower())

# 17. Uppercase Conversion
print(sample_text.upper())

# 18. Current Temperature
temperature = 25
print(f'The current temperature is {temperature} degrees.')

# 19. Printing a Poem
poem = """Before I saw her with lipstick
I thought makeup was pointless
but I was wrong..."""
print(poem)
