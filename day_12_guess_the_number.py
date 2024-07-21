EASY=10
HARD=5


def verify(user_guess,answer,turns):
  if user_guess<answer:
    print("Too low.\nGuess again.")
    return turns - 1
  elif user_guess>answer:
    print("Too high.\nGuess again.")
    return turns -1
  else:
    print(f"You got it! The answer was {answer}.")

def set_difficulty():
  difficulty=input("Choose a difficulty. Type 'easy' or 'hard':")
  if difficulty=="easy":
    return EASY
  else:
    return HARD

def game():
  print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
  import random
  answer=random.randint(1,100)
  turns=set_difficulty()
  
  user_guess=0
  while user_guess!=answer:
    print(f"You have {turns} attempts remaining to guess the number.")
    user_guess=int(input("Make a guess: "))
    turns=verify(user_guess,answer,turns)
    if turns==0:
      print(f"Game over.The answer was {answer}")
      return
from art import guessnumber
print(guessnumber)
game()
