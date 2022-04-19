#Rock-paper-scissors game
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
comp_choice = random.randint(0,2)

if (user_choice > 2 and user_choice < 0):
  print("Please choose one of the numbers specified in the game i.e 0, 1 or 2.")
else:
  print(f"You chose:\n{game_images[user_choice]}")

print(f"Computer chose:\n{game_images[comp_choice]}")
if (user_choice == comp_choice):
  print("You have drawn.")
else:
  if (user_choice == 0):
    if (comp_choice == 1):
      print("Oh no!You lost.")
    else:
      print("You have won!!")
  elif (user_choice == 1):
    if (comp_choice == 2):
      print("Oh no!You lost.")
    else:
      print("You have won!!")
  elif (user_choice == 2):
    if (comp_choice == 0):
      print("Oh no!You lost.")
    else:
      print("You have won!!")   