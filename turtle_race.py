from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="enter the turtle color you think will win:")
print(user_bet)

tim.goto(-200,0)

screen.exitonclick()
