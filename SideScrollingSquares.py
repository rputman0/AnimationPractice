from turtle import *
import random
title('Side Scroller')
setup(400, 200, 0, 0)

#hideturtle()
penup()
setx(-155)
sety(-50)
pendown()

def makeSquare(square,path):
    forward(path)
    left(90)
    forward(square)
    right(90)
    forward(square)
    right(90)
    forward(square)
    left(90)
    forward(path)

while True:
    makeSquare(random.randint(5,100),10)

