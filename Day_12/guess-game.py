#This is the guess game 
import random

generated_number = random.randint(1,100)
print("This is the guessing game.\nI'm thinking of a number between 1 and 100.\nCan you guess?")
level = input("Do you want to play the 'easy' or 'hard' level? ").lower()
#guessed_number = int(input("Make a guess: "))

def easy_level():
  easy_attempts = 10
  while easy_attempts != 0:
    guessed_number = int(input("Make a guess: "))
    if guessed_number != generated_number:
      if guessed_number < generated_number:
        print("Too low!\nGuess again")
      elif guessed_number > generated_number:
        print("Too high!\nGuess again")
      easy_attempts -= 1
      if easy_attempts == 0:
        print(f"You have run out of attempts, you lose.\nThe correct number was {generated_number}")
      else:
        print(f"You have {easy_attempts} attempts remaining.")
    else:
      print("You guessed the right number!!")
      return
      
def hard_level():
  hard_attempts = 5
  while hard_attempts != 0:
    guessed_number = int(input("Make a guess: "))
    if guessed_number != generated_number:
      if guessed_number < generated_number:
        print("Too low!\nGuess again")
      elif guessed_number > generated_number:
        print("Too high!\nGuess again")
      hard_attempts -= 1
      if hard_attempts == 0:
        print(f"You have run out of attempts, you lose.\nThe correct number was {generated_number}")
      else:
        print(f"You have {hard_attempts} attempts remaining.")
    else:
      print("You guessed the right number!!")
      return        
if level == "easy":
  print("You have 10 attempts.")
  easy_level()
else:
  print("You have 10 attempts.")
  hard_level()