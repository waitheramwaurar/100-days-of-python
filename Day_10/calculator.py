#This is a calculator program
from art import logo
#Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2

# Divide 
def divide(n1, n2):
  return n1/n2

signs = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  should_continue = True
  
  num1 = float(input("What's the first number? "))
  for symbol in signs:
      print(symbol)
  while should_continue:
    operation = input("Pick an operator: ")
    next_num = float(input("What's the next number? "))
    
    calc_function = signs[operation]
    answer = calc_function(num1, next_num)
    print(f"{num1} {operation} {next_num} = {answer}")
    to_proceed = input("Enter 'y' to continue with current calculation, and 'n' to start new calculation: ")
    if to_proceed == 'y':
      num1 = answer
    elif to_proceed == 'n':
      should_continue = False
      calculator()
   
calculator()
  
  