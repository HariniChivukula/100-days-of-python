print("Welcome to the tip calculator")
x=input("What was the total bill?\n")
x=int(x)
y=input("How much percentage tip would you like to give? 10, 12 or 15?\n")
y=float(y)/100
z=input("How many people will split the bill?\n")
z=int(z)
bill_per_person=((x*y)+x)/z
tip_per_person=round(bill_per_person,2)
print(f"Each person should pay: ${bill_per_person}")