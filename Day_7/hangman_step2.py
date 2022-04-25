#Step 2
import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

guess = input("Guess a letter: ").lower() 

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in chosen_word:
  display.append("_")

for i in range(0,len(chosen_word)):
  if chosen_word[i] == guess:
    display[i] = chosen_word[i]
  # else:
  #   display[i] = "_"
print(display)