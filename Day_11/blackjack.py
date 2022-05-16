from art import logo
from replit import clear
import random

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
# print(deal_card())  

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
def calculate_score(cards_list):
  score = sum(cards_list)

  if score == 21 and len(cards_list) == 2:
    return 0
  elif 11 in cards_list:
    cards_list.remove(11)
    cards_list.append(1)
  return score 
  
def compare(comp_score, user_score):
    if comp_score == 0:
      print("Computer wins")
    elif comp_score == user_score:
      print("Draw")
    elif user_score == 0:
      print("You win!!")
    elif user_score > 21:
      print("You lose")
    elif comp_score > 21:
      print("Computer loses")
    else:
      if user_score > comp_score:
        print("You win")
      else:
        print("Computer wins")  

def play_game():        
  print(logo)
  
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  # print(f"User: {user_cards}")
  # print(f"Computer: {computer_cards}")
  restart_game = True
  while not restart_game:
    print(logo)
    draw_again = True
    while draw_again:
      user_score = calculate_score(user_cards)
      comp_score = calculate_score(computer_cards)
      print(f"Your cards: {user_cards}\nYour score: {user_score}")
      print(f"Computer's cards: {computer_cards[0]}")
    #Hint 6: Create a function called calculate_score() that takes a List of cards as input 
    #and returns the score. 
    #Look up the sum() function to help you do this.
    
      if user_score == 0 or comp_score == 0 or user_score > 21:
        #print("Game over!")
        draw_again = False
      else:
        draw = input("Do you want to draw another card? 'y' or 'n'? ")
        if draw == 'y':
          user_cards.append(deal_card())
        else:
          draw_again = False
          
    while comp_score != 0 and comp_score < 17:
      computer_cards.append(deal_card())
      comp_score = calculate_score(computer_cards)
    print(f"Computer score: {comp_score}")  
    
    compare(comp_score, user_score)

while input("Do you want to play Black Jack? 'y' or 'n': ") == "y":
  clear()
  play_game()
