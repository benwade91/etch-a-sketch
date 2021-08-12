from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="enter the turtle color you think will win:")

colors = ["red", "yellow", "blue", "green", "orange", "pink"]

for i in colors:
    tim = Turtle(shape="turtle")
    tim.color('black', i)
    tim.name = i
    tim.penup()
    tim.goto(-200, (150 - (50 * colors.index(i))))

screen.exitonclick()
