x=input("Where do you want to go? Left or Right?").lower()

if x=="left":
  y=input("Do you want to swim or wait?").lower()
  if y=="swim":
    print("You got attacked by a trout. Game over")
  if y=="wait":
    z=input("Which door do you want to open? Red, Blue or Yellow?").lower()
    if z=="yellow":
      print("You win!")
    elif z=="red":
      print("You were burnt by fire. Game over.")
    elif z=="blue":
      print("You wer eaten by beasts. Game over.")
    else:
      print("Game over.")
else:
  print("You fell into a hole. Game over")