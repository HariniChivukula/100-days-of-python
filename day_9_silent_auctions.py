from replit import clear
from art import logo1
print(logo1)
name=input("What is your name?")
bid=int(input("What is you bid in $?"))
Auction_details={}
Auction_details[name]=bid
flow=input("Are there any other bidders? Type 'yes' or 'no'.")
bid_list=[]
while flow=="yes":
             clear()
             name=input("What is your name?")
             bid=int(input("What is you bid in $?"))
             Auction_details[name]=bid
             flow=input("Are there any other bidders? Type 'yes' or 'no'.")
if flow=="no":
             for key in Auction_details:
                          bid_list.append(Auction_details[key])
             max=0
             for element in bid_list:
                          if element>max:
                                    max=element
             for name in Auction_details:
                          if Auction_details[name]==max:
                                       winner=name
print(f"The winner is {winner} with a bid of ${max}.")
