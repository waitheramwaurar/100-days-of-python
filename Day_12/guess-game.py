#This is the guess game 
import random

generated_number = random.randint(1,100)
print("This is the guessing game.\nI'm thinking of a number between 1 and 100.\nCan you guess?")
level = input("Do you want to play the 'easy' or 'hard' level? ").lower()

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




#Angela's code
# from random import randint
# from art import logo

# EASY_LEVEL_TURNS = 10
# HARD_LEVEL_TURNS = 5

# #Function to check user's guess against actual answer.
# def check_answer(guess, answer, turns):
#   """checks answer against guess. Returns the number of turns remaining."""
#   if guess > answer:
#     print("Too high.")
#     return turns - 1
#   elif guess < answer:
#     print("Too low.")
#     return turns - 1
#   else:
#     print(f"You got it! The answer was {answer}.")

# #Make function to set difficulty.
# def set_difficulty():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == "easy":
#     return EASY_LEVEL_TURNS
#   else:
#     return HARD_LEVEL_TURNS

# def game():
#   print(logo)
#   #Choosing a random number between 1 and 100.
#   print("Welcome to the Number Guessing Game!")
#   print("I'm thinking of a number between 1 and 100.")
#   answer = randint(1, 100)
#   print(f"Pssst, the correct answer is {answer}") 

#   turns = set_difficulty()
#   #Repeat the guessing functionality if they get it wrong.
#   guess = 0
#   while guess != answer:
#     print(f"You have {turns} attempts remaining to guess the number.")

#     #Let the user guess a number.
#     guess = int(input("Make a guess: "))

#     #Track the number of turns and reduce by 1 if they get it wrong.
#     turns = check_answer(guess, answer, turns)
#     if turns == 0:
#       print("You've run out of guesses, you lose.")
#       return
#     elif guess != answer:
#       print("Guess again.")


# game()