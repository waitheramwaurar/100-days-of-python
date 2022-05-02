#Caesar Cipher - Complete

#Repeating the alphabet for when the shift is greater than the length of the array
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(art.logo)

def caesar(user_text, letter_shift, c_direction):
  cipher_text = []
  if c_direction == "decode":
    letter_shift *= -1
  for char in text:
    if char in alphabet:
      new_pos = alphabet.index(char) + letter_shift
      cipher_text.append(alphabet[new_pos])
    else:
      cipher_text.append(char)
  print(f"The {c_direction}d text is {''.join(cipher_text)}")

restart = "yes"

while (restart == "yes"):

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  if shift > 25:
    shift = shift % 25
  
  caesar(user_text=text, letter_shift=shift, c_direction=direction)
  restart = input("Type 'yes' if you want to continue running the cipher and 'no' if you want to quit the program:\n")
  if (restart == "no"):
    print("Byeee! Come back soon.")