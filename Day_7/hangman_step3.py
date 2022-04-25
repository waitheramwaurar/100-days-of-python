import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in chosen_word:
  display.append("_")
  
while True:
  guess = input("Guess a letter: ").lower()
  
  for i in range(0,len(chosen_word)):
    if chosen_word[i] == guess:
      display[i] = chosen_word[i]
      
  print(display)

  if "_" not in display:
    print("You win!")
    break

