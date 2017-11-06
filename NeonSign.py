import pygame, sys, time
from pygame.locals import *
from random import *

pygame.init()

#set up the window
width,height = 420,420#randint(100,900),randint(100,900); #create random screen size
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Draw Concentric Squares')

#set color constants
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]
lightBlue = [65,105,255]
green = [0,255,0]
pink = [255,0,255]

#draw the squares in the middle of the screen
(widthCenter,heightCenter) = (width/2,height/2)

TOPLEFT = [widthCenter-50,heightCenter-50] #blue
TOPRIGHT =  [widthCenter+50,heightCenter-50] #red
BOTLEFT =  [widthCenter-50,heightCenter+50] #pink
BOTRIGHT = [widthCenter+50,heightCenter+50] #green

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
        #time.sleep(0.01)
        #pygame.display.update()#display each update to animate


##def animate(length,argument):
##    for i in range(0,100):
##        drawRect(lightBlue,argument)
##        time.sleep(0.01)
##        pygame.display.update()
##
##        drawRect(blue,argument)
##        time.sleep(0.01)
##        pygame.display.update()


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
    #drawDefault()
    #pygame.display.update()

    drawBigBox(length)
    pygame.display.update()

    #TODO: add font
    animate(length)
##    animate(length,(TOPLEFT[0],TOPLEFT[1]+(i*length)))
##    animate(length,(BOTLEFT[0]+(i*length),BOTLEFT[1]))
##    animate(length,(BOTRIGHT[0],BOTRIGHT[1]-(i*length)))
##    animate(length,(TOPRIGHT[0]-(i*length),TOPRIGHT[1]))
##





               
