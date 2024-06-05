import turtle


from turtle import Turtle,Screen
from random import choice
turtle.colormode(255)
t=Turtle()
t.speed(0)

color_list=[(213, 211, 210), (207, 215, 210), (199, 163, 119), (216, 209, 212), (210, 213, 218), (165, 187, 163), (38, 95, 116)]


def line():
    for i in range(10):

        t.pendown()
        color = choice(color_list)
        t.dot(20, color)
        t.penup()
        t.forward(50)

for i in range(1,11):
    line()
    t.goto(0,-(i)*50)
    # t.sety(-(i)*50)
    # t.setx(0)

s=Screen()
s.exitonclick()