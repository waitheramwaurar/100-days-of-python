#Chooses heads or tails at random (just like a coin flip)
import random

coin_toss = random.randint(0,2)
if (coin_toss == 0):
  print("Tails")
else:
  print("Heads")