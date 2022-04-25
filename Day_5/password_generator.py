#This is a program that creates a random password based on the number of letters, numbers and symbols the user specifies

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = ""
for n in range(nr_letters):
  random_letters += random.choice(letters)
#print(random_letters)
random_symbols = ""
for n in range(nr_symbols):
  random_symbols += random.choice(symbols)
#print(random_symbols)
random_numbers = ""
for n in range(nr_numbers):
  random_numbers += random.choice(numbers) 
#print(random_numbers)  
random_password = random_letters + random_symbols + random_numbers 

#Prints the random password in order i.e letters then symbols then numbers
#print(random_password)

#Prints the random password in a random order
password = list(random_password)
random.shuffle(password)
print("".join(password))