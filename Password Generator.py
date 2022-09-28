# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
pw_letter = ""
pw_symbols = ""
pw_numbers = ""

for n in range(0, nr_letters):
    pw_letter = pw_letter + random.choice(letters)

for n in range(0, nr_symbols):
    pw_symbols = pw_symbols + random.choice(symbols)

for n in range(0, nr_numbers):
    pw_numbers = pw_numbers + random.choice(numbers)

ez_password = pw_letter + pw_symbols + pw_numbers
print(f"Your generated password is : {ez_password}")

# Hard Level - Order of characters randomised:
hard_pw = ""
to_be_randomized = list(ez_password)
random.shuffle(to_be_randomized)
for alphabet in to_be_randomized:
    hard_pw = hard_pw + alphabet

print(f"Your randomized password is : {hard_pw}")


# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
