
from turtle import Turtle, Screen
import random

screen = Screen()
colors = ['red','green','blue','yellow','pink','purple']
# to change the size of  the screen
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle race",prompt="Who do you bet will win the race?ENTER A COLOR:")
a=-50
all_turtles=[]

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=a)
    a=a+30
    all_turtles.append(new_turtle)

is_race_on= False
if user_bet:
    is_race_on=True
while is_race_on:
    for t in all_turtles:
        if t.xcor()>230:
            is_race_on = False
            win=t.pencolor()
            if win==user_bet:
                print(f"You've won the turtle race , {win} tutle is the winner")

            else:
                print(f"You've lost the turtle race , {win} tutle is the winner")
                is_race_on=False
        random_distance = random.randint(0,10)
        t.forward(random_distance)





screen.exitonclick()