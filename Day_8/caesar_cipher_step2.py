#Caesar Cipher - Step 2
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(user_text, letter_shift):
  cipher_text = []
  new_pos = 0
  for letter in text:
    new_pos = alphabet.index(letter) + shift
    if (new_pos > len(alphabet)):
      #if the new position is greater than the total number of the alphabet
      remainder = new_pos - len(alphabet)
      cipher_text.append(alphabet[remainder])
    else:  
      cipher_text.append(alphabet[new_pos])
  print(f"The encoded text is {''.join(cipher_text)}")


def decrypt(user_text, letter_shift):
  decipher = []
  for letter in user_text:
    original_pos = alphabet.index(letter) - shift
    decipher.append(alphabet[original_pos])  
  print(f"The encoded text is {''.join(decipher)}")
  
if direction == "encode":
  encrypt(user_text=text, letter_shift=shift)
else:
  decrypt(user_text=text, letter_shift=shift)