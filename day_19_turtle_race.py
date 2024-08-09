import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win "
                                                          "the race? Enter a color.")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

y = [-70, -40, -10, 20, 50, 80]
turtles = []
for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230, y[index])
    turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if user_bet.lower() == winner.lower():
                print(f"You've won! The {winner} turtle is the winner!")
            else:
                print(f"You've lost! The {winner} turtle is the winner!")

            break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()