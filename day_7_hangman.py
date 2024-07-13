
from hangman_art import stages
from replit import clear
from hangman_words import word_list
import random
chosen_word=random.choice(word_list)
print(chosen_word)
blanks=[]
for letter in chosen_word:
  blanks.append("_")
print(blanks)
def replaceblank():
  if guess in blanks:
    print (f"You have already guessed {guess}")
  for i in range(len(chosen_word)):
    if guess==chosen_word[i]:
      blanks[i]=guess
  print(blanks)
  
no_of_lives=6
from hangman_art import logo
print(logo)
while no_of_lives>0:
  guess=input("Guess a letter.").lower()
  clear()
  if guess in chosen_word:
    replaceblank()
    if "_" not in blanks:
      print("You won")
      break
  else:
    print(f"You already guessed {guess}, that's not in the word. You lose a life.")
    no_of_lives-=1
    print(stages[no_of_lives])
    if no_of_lives==0:
      print("You lost")
  



