def caeser(cipher_text,cipher_shift,cipher_direction):

  final_result=""
  for char in cipher_text:
    if char in alphabet:
      x = alphabet.index(char)
      if cipher_direction=="encode":
        new_index=x+cipher_shift
        if new_index>=len(alphabet):
          new_index=abs(len(alphabet) - new_index)
      elif cipher_direction=="decode":
        new_index=x-cipher_shift
      cipher_letter=alphabet[new_index]
      final_result+=cipher_letter
    else:
      final_result+=char
  print(f"The {direction}d text is {final_result}")
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ShouldContinue=True
while ShouldContinue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction=="encode" or direction=="decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caeser(cipher_text=text,cipher_shift=shift,cipher_direction=direction)
  else:
    print("You have entered an invalid option.")
  result=input("Do you want to continue? Type 'yes' or 'no'.\n").lower()
  if result=="no":
    ShouldContinue=False
    print("Goodbye!")