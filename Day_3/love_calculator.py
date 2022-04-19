#The love calculator calculates whether two people are compatible with each other
#Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_count = 0
love_count = 0
lovers = (str(name1) + str(name2)).lower()
#print(lovers)
for i in "true":
  true_count += lovers.count(i)
for i in "love":
  love_count += lovers.count(i)
#print(true_count)
#print(love_count)

love_score = int(str(true_count) + str(love_count))
#print(love_score)

if (love_score < 10 or love_score > 90):
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score > 40 and love_score < 50):
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
  
  
  