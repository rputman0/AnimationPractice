$use turtle graphics to draw a random skyline

from turtle import *
import random

title('Random Skyline')
setup(400,200,00,0)

penup()
setx(-185)
sety(-50)
pendown()

def drawBuilding(square,path):
    forward(path)
    left(90)
    forward(square)
    right(90)
    forward(square)
    right(90)
    forward(square)
    left(90)
    forward(path)

#keep the buildings within the size of the screen
x = 0
while(x < 5):
    drawBuilding(random.randint(5,100),10)
    x += 1
