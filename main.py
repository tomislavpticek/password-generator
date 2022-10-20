import randomletters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



easy_password = []

if(nr_letters > 0):
  for var in range(nr_letters):
    easy_password.append(letters[random.randint(0,len(letters)-1)])

if(nr_symbols > 0):
  for var in range(nr_symbols):
    easy_password.append(symbols[random.randint(0,len(symbols)-1)])

if(nr_numbers > 0):
  for var in range(nr_numbers):
    easy_password.append(numbers[random.randint(0,len(numbers)-1)])

easy_password_string = ""

for character in easy_password:
  easy_password_string += character

print("Here is your easy password: {}".format(easy_password_string))

hard_password = ""

for number in range(len(easy_password)):
  hard_password += easy_password.pop(random.randint(0,len(easy_password)-1))

print("Here is your hard password: {}".format(hard_password))
