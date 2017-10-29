import pygame, time, sys
from pygame.locals import *
from random import *

pygame.init()

#set up the window
width,height = (200,200);
screen = pygame.display.set_mode( (width,height) )
pygame.display.set_caption('')

#start with blue color, and change every time it hits a wall
randomColor = [0,0,255]
black =[0,0,0]

#get random starting position, and starting direction
xValue = randint(0,width-20)
yValue = randint(0,height-20)

speedX = random()
speedY = random()

def random():
    return (1 or -1)

def drawRect(color,xValue,yValue):
    pygame.draw.rect(screen,color,[xValue,yValue,10,10])

def withinWindow(value,total):
    return (value > (total-10) or value < 0)

#create an infinte loop of the moving square
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #draw over the old square, and then draw a new one
    drawRect(black,xValue,yValue) 
    xValue += speedX
    yValue += speedY
    drawRect(randomColor,xValue,yValue)

    #if it hits a wall go in opposite direction
    if(withinWindow(yValue,height)):
        speedY *= -1
        randomColor = [randint(0,255),randint(0,255),randint(0,255)]
        
    if(withinWindow(xValue,width)):
        speedX *= -1
        randomColor = [randint(0,255),randint(0,255),randint(0,255)]
    
    pygame.display.update()
    time.sleep(0.01)
