import pygame, sys, time
from pygame.locals import *

pygame.init()

#set up window
screen = pygame.display.set_mode((300, 300), 0, 32)
pygame.display.set_caption('Draw Squares Animation')

#set colors
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]

def point(x,y):
    return (x,y)

def drawRect(color,point):
    pygame.draw.rect(screen,color,[point[0],point[1],25,25],0)

# run the game loop
while True:
    # check for the QUIT event
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #fill the screen to black
    screen.fill(black)

    j = 0
    for i in range(0,101):
        drawRect(blue, point(200,80+i) )
        drawRect(blue, point(75,80+i) )
        drawRect(red, point(200-i,80) )
        drawRect(red, point(101+i,180) )
        time.sleep(0.02)

        j += 2.53 #double the length
        drawRect(red, point(10,10+j) )
        drawRect(red, point(265,10+j) )
        drawRect(blue, point(10+j,10) )
        drawRect(blue, point(265-j,265) )
        pygame.display.update()
        time.sleep(0.02)

    break
