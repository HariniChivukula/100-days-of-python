import random
from gamedata import data
from art import logo, vs
from replit import clear
#Display ART
print(logo)
score=0
continue_game=True
#Format the account data into printable format

def format_data(account):
  account_name=account["name"]
  account_descr=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
  if a_followers>b_follower_count:
    return user_guess=="a"
  else:
    return user_guess=="b"
  
account_b=random.choice(data)
#Generate a random account from the game data
while continue_game:
  account_a=account_b
  account_b=random.choice(data)
  if account_a==account_b:
    account_b=random.choice(data)
  
  print(f"Compare A:{format_data(account_a)}")
  print(vs)
  print(f"Against B:{format_data(account_b)}")
  
  #Ask user for a guess
  user_guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  #Check if user is correct
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  IsCorrect=check_answer(user_guess, a_follower_count, b_follower_count)
  clear()
  print(logo)
  #Give user feedback on their guess
  if IsCorrect:
    score+=1
    print(f"You're right! Current score: {score}")
    
  else:
    continue_game=False
    print(f"Sorry, that's wrong. Final score: {score}")