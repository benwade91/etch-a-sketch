from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(height=400, width=600)
user_bet = screen.textinput(title="Make your bet", prompt="red, yellow, blue, green, orange, or pink?")

colors = ["red", "yellow", "blue", "green", "orange", "pink"]
all_turtles = []
start_race = False

for i in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color('black', i)
    new_turtle.penup()
    new_turtle.goto(-270, (150 - (50 * colors.index(i))))
    all_turtles.append(new_turtle)

if user_bet:
    start_race = True

while start_race:
    for turtle in all_turtles:
        rand_distance = random.randint(5, 10)
        turtle.forward(rand_distance)
        if turtle.pos()[0] > 273:
            start_race = False
            winner = turtle.color()[1]
            if user_bet.lower() == winner:
                print(f"You win! the winner was {winner}")
            else:
                print(f"You lose! The winner was {winner}")
            break





screen.exitonclick()
