import pygame, sys, time
from pygame.locals import *

pygame.init()

#set up window
width,height = 300,300;
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Draw Repeating Squares')

#set colors
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]
green = [0,255,0]
pink = [255,0,255]

def point(x,y):
    return (x,y)

def drawRect(color,point):
    pygame.draw.rect(screen,color,[point[0],point[1],10,10],0)

TOPLEFT = [100,80]
TOPRIGHT = [200,80]
BOTLEFT = [101,179]
BOTRIGHT = [200,179]

def drawDefault():
    drawRect(blue,TOPLEFT)
    drawRect(red,TOPRIGHT)
    drawRect(green,BOTRIGHT)
    drawRect(pink,BOTLEFT)

first = 1
second = 1

def animate(horz,vert,first,second):
    for i in range(0,100):
        drawRect(blue, (TOPLEFT[0],TOPLEFT[1]+ (i*second) ) )
        drawRect(red, (TOPRIGHT[0]-(i*second),TOPRIGHT[1])  )
        drawRect(green, (BOTRIGHT[0],BOTRIGHT[1]- (i*second) ) )
        drawRect(pink, (BOTLEFT[0]+(i*second),BOTLEFT[1]) )
                    
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

    if(event.type == pygame.KEYDOWN):
           if(event.key == pygame.K_SPACE):
               #while within the screen
               i = 0
               while(BOTRIGHT[0] < width and BOTRIGHT[1] < height):                    
                    animate(i,i,first,second)
                    TOPLEFT = (TOPLEFT[0]-20,TOPLEFT[1]-20)
                    TOPRIGHT = (TOPRIGHT[0]+20,TOPRIGHT[1]-20)
                    BOTRIGHT = (BOTRIGHT[0]+20,BOTRIGHT[1]+20)
                    BOTLEFT = (BOTLEFT[0]-20,BOTLEFT[1]+20)
                    first += .5
                    second += .4
                    i += 1
               break
            
