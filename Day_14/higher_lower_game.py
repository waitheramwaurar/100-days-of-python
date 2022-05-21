#Higher Lower Game

#Import random module and the data
import random
from game_data import data
from replit import clear

#Generate random options
def choice_generator():
  r_option = random.choice(data)
  return r_option
#Function for comparing the followers
def compare(user_guess, follow_a, follow_b):
  if follow_a > follow_b:
    return user_guess == "A"
  else:
    return user_guess == "B"
    
def higher_lower_game():    
  game_not_over = True
  option_A = choice_generator()
  option_B = choice_generator()
  score = 0
  
  while game_not_over:
    option_A = option_B
    option_B = choice_generator()
  
    while option_A == option_B:
      option_B = choice_generator()
    
    user_guess = input("Compare A: "+ option_A["name"] + ", "+ option_A["description"]+ " from "+ option_A["country"] +"\nVs\nOption B: "+ option_B["name"] + ", "+ option_B["description"]+ " from "+ option_B["country"] + ": ").upper()
    follow_a = option_A["follower_count"]
    follow_b = option_B["follower_count"]
    is_right = compare(user_guess, follow_a, follow_b)
    clear()
    if is_right:
      score += 1
      print(f"You got that right, you're score is {score}")
    else:
      print(f"Sorry, you guessed wrong :(\nFinal score: {score}")
      game_not_over = False
    
higher_lower_game()