import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Simple Password Generator!")
letters_num = int(input("How many letters would you like? "))
symbols_num = int(input(f"How many symbols would you like? "))
numbers_num = int(input(f"How many numbers would you like? "))

# Compute password
password_list = []
for char in range(0, letters_num + 1):
  password_list.append(random.choice(letters))

for char in range(0, symbols_num + 1):
  password_list += random.choice(symbols)

for char in range(0, numbers_num + 1):
  password_list += random.choice(numbers)

# Output password
random.shuffle(password_list)
password = "".join(password_list)
print(f"Your password is: {password}")