import random

from replit import clear
from art import blackjack
def deal_cards():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card=random.choice(cards)
  return card
def compare_scores(user_score,computer_score):
  if user_score==computer_score:
    return "It's a draw"
  elif computer_score==0:
    return "You lose"
  elif user_score==0:
    return "You win with a Blackjack"
  elif user_score>21:
    return "Your sum has crossed 21. You lose"
  elif computer_score>21:
    return "Your opponent sum has crossed 21. You win"
  elif user_score>computer_score:
    return "You win"
  elif computer_score>user_score:
    return "You lose"
def game():
  print(blackjack)
  user_cards=[]
  computer_cards=[]
  game_over=False
  for i in range(2):
    deal_cards()
    user_cards.append(deal_cards())
    deal_cards()
    computer_cards.append(deal_cards())
  # print(f"{user_cards} {computer_cards}")
  def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
      return 0
    if 11 in cards and sum(cards)>21:
      cards.remove(11)
      cards.append(1)
    return sum(cards)
  while not game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    print(f"User cards: {user_cards} Current score: {user_score}")
    print(f"Computer's first card is {computer_cards[0]}")
    if user_score==0 or computer_score==0 or user_score>21:
      game_over=True
    else:
      user_choice=input("Do you want to draw another card? Type 'y' or 'n'")
      if user_choice=="y":
        user_cards.append(deal_cards())
      else:
        game_over=True
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_cards())
    computer_score=calculate_score(computer_cards)
  
  print(f"Your final cards are {user_cards} and your final score is {user_score}")
  print(f"Computer's final cards are {computer_cards} and computer's final score is {computer_score}")
  final_result=compare_scores(user_score,computer_score)
  print(final_result)


while input("Do you want to play the game? Type 'y' or 'n'")=="y":
  clear()
  game()
