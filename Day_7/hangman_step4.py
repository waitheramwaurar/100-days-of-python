import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

display = []

for _ in chosen_word:
  display.append("_")

lives = 6  
  
while True:
  guess = input("Guess a letter: ").lower()
  
  for i in range(0,len(chosen_word)):
    letter = chosen_word[i]
    if letter == guess:
      display[i] = letter
  if guess not in chosen_word:
      lives -= 1
      print(stages[lives])
      if lives == 0:
        print("Game over")
        break
      
  print(f"{''.join(display)}")

  if "_" not in display:
    print("You win!")
    break
