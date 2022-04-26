#This program checks whether a number is a prime number

def prime_checker(number):
  is_Prime = True

  for i in (2, number - 1):
    if number % i == 0:
      is_Prime = False   
  if is_Prime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")
      
n = int(input("Check this number: "))
prime_checker(number=n)
