import pygame, sys, time
from pygame.locals import *
from random import *

pygame.init()

width,height = 200,200
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Neon')

black = [0,0,0]
blue = [0,0,255]
lightBlue = [65,105,255]

#draw the big square, automatically in the center of the screen
(widthCenter,heightCenter) = (width/2,height/2)

TOPLEFT = [widthCenter-50,heightCenter-50]
TOPRIGHT =  [widthCenter+50,heightCenter-50]
BOTLEFT =  [widthCenter-50,heightCenter+50]
BOTRIGHT = [widthCenter+50,heightCenter+50]

def point(x,y):
    return (x,y)

def drawRect(color,point):
    pygame.draw.rect(screen,color,[point[0],point[1],10,10],0)

def drawDefault():
    drawRect(blue,TOPLEFT)
    drawRect(blue,TOPRIGHT)
    drawRect(blue,BOTRIGHT)
    drawRect(blue,BOTLEFT)

length = 1

def drawBigBox(length):
    for i in range(0,100):
        drawRect(blue, (TOPLEFT[0],TOPLEFT[1]+ (i*length) ) )
        drawRect(blue, (TOPRIGHT[0]-(i*length),TOPRIGHT[1])  )
        drawRect(blue, (BOTRIGHT[0],BOTRIGHT[1]- (i*length) ) )
        drawRect(blue, (BOTLEFT[0]+(i*length),BOTLEFT[1]) )

def animate(length):
    for i in range(0,100):
        drawRect(lightBlue, (TOPLEFT[0],TOPLEFT[1]+ (i*length) ) )
        time.sleep(0.01)
        pygame.display.update()

        drawRect(blue, (TOPLEFT[0],TOPLEFT[1]+ (i*length) ) )
        time.sleep(0.04)
        pygame.display.update()

    for i in range(0,100):
        drawRect(lightBlue, (BOTLEFT[0]+(i*length),BOTLEFT[1]) )
        time.sleep(0.01)
        pygame.display.update()

        drawRect(blue, (BOTLEFT[0]+(i*length),BOTLEFT[1]) )
        time.sleep(0.04)
        pygame.display.update()

    for i in range(0,100):
        drawRect(lightBlue, (BOTRIGHT[0],BOTRIGHT[1]- (i*length) ) )
        time.sleep(0.01)
        pygame.display.update()

        drawRect(blue, (BOTRIGHT[0],BOTRIGHT[1]- (i*length) ) )
        time.sleep(0.04)
        pygame.display.update()

    for i in range(0,100):
        drawRect(lightBlue, (TOPRIGHT[0]-(i*length),TOPRIGHT[1])  )
        time.sleep(0.01)
        pygame.display.update()

        drawRect(blue, (TOPRIGHT[0]-(i*length),TOPRIGHT[1])  )
        time.sleep(0.04)
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)

    drawBigBox(length)
    pygame.display.update()

    animate(length)

pygame.exitonclose()
