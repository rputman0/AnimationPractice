import pygame, sys, time
from pygame.locals import *

pygame.init()

#set up the window
width,height = 300,300;
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Draw Concentric Squares')

#set color constants
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]
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
    drawRect(red,TOPRIGHT)
    drawRect(green,BOTRIGHT)
    drawRect(pink,BOTLEFT)

length = 1

def animate(length):
    for i in range(0,100):
        drawRect(blue, (TOPLEFT[0],TOPLEFT[1]+ (i*length) ) )
        drawRect(red, (TOPRIGHT[0]-(i*length),TOPRIGHT[1])  )
        drawRect(green, (BOTRIGHT[0],BOTRIGHT[1]- (i*length) ) )
        drawRect(pink, (BOTLEFT[0]+(i*length),BOTLEFT[1]) )

        time.sleep(0.01)
        pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(black)
    drawDefault()
    pygame.display.update()

    #start program when user presses 'space'
    if(event.type == pygame.KEYDOWN):
           if(event.key == pygame.K_SPACE):
               #draw the squares while within the screen
               iterator = 0
               while(BOTRIGHT[0] < width and BOTRIGHT[1] < height):
                   animate(length)
                   #create new squares that are separated from each other
                   TOPLEFT = (TOPLEFT[0]-20,TOPLEFT[1]-20)
                   TOPRIGHT = (TOPRIGHT[0]+20,TOPRIGHT[1]-20)
                   BOTRIGHT = (BOTRIGHT[0]+20,BOTRIGHT[1]+20)
                   BOTLEFT = (BOTLEFT[0]-20,BOTLEFT[1]+20)
                   length += .4
                   iterator += 1
               break
