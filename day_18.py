import turtle
from turtle import Turtle, Screen
import colorgram
import random
colors = colorgram.extract('spot_painting.jpg',30)

tim = Turtle()
color_list = [(189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (64, 43, 43), (171, 183, 170), (136, 149, 69), (127, 160, 172), (101, 79, 89), (83, 133, 108), (108, 39, 44), (39, 61, 47), (45, 40, 41), (211, 196, 124), (174, 150, 152), (36, 71, 88), (179, 106, 80), (36, 67, 84), (207, 185, 181), (99, 140, 119), (184, 198, 181), (148, 116, 120), (180, 195, 200), (53, 69, 59), (122, 129, 135)]
turtle.colormode(255)
tim.pencolor(random.choice(color_list))
tim.penup()
tim.setpos(-200,250)
tim.speed("fastest")


def draw_dots():
    for n in range(10):
        tim.showturtle()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


def go_to_nextline():
    tim.hideturtle()
    tim.setx(-200)
    tim.right(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(0)


for n in range(10):
    draw_dots()
    go_to_nextline()

screen = Screen()
screen.exitonclick()