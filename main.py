from turtle import Turtle, Screen
import random
from random import randrange

tim = Turtle()


colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

'''def random_walk(number_steps):
    for _ in range(number_steps):
        select_color = random.choice(colors)
        tim.color(select_color)
        coin = random.randrange(0,2)
        if coin == 0:
            tim.left(90)
        else:
            tim.right(90)

        tim.forward(20)

random_walk(100)'''
directions = [0,90,180,270]
tim.speed("fastest")
tim.pensize(15)
for _ in range(150):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))#better for rotation

screen = Screen()
screen.exitonclick()
