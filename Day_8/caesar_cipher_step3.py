#Caesar Cipher - Step 3
#Putting encode and decode in one function

#Repeating the alphabet for when the shift is greater than the length of the array
import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

print(art.logo)

def caesar(user_text, letter_shift, c_direction):
  cipher_text = []
  for letter in text:
    if c_direction == "encode":
      new_pos = alphabet.index(letter) + shift
      # if (new_pos > len(alphabet)):
      #   remainder = new_pos - len(alphabet)
      #cipher_text.append(alphabet[remainder]) 
    elif c_direction == "decode":
      new_pos = alphabet.index(letter) - shift
    else:
      print("Enter a valid choice.") 
    cipher_text.append(alphabet[new_pos])      
  print(f"The {c_direction}d text is {''.join(cipher_text)}")

caesar(user_text=text, letter_shift=shift, c_direction=direction)