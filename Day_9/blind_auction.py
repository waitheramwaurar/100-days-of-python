from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)
print("Welcome to the blind auction!")
bidders = {}

def winning_bid(bidders):
  highest_bid = 0
  winner = ""
  
  for bidder in bidders:
    bid = bidders[bidder]
    if bid > highest_bid:
      highest_bid = bid
      winner = bidder
  print(f"The winner is {winner} with ${highest_bid}") 

continue_bid = True
while continue_bid:
  name = input("What is your name? ")
  bid_amount = int(input("What is your bid? $"))

  bidders[name] = bid_amount

  other_bidders = input("Is there any other bidder? yes or no\n")

  if other_bidders == "yes":
    continue_bid = True
    clear()
  elif other_bidders == "no":
    continue_bid = False
    #print(bidders)
    winning_bid(bidders)
   