import pygame, sys, time
from pygame.locals import *

pygame.init()

#set up window
screen = pygame.display.set_mode((300, 300), 0, 32)
pygame.display.set_caption('Draw Repeating Squares')

#set colors
black = [0,0,0]
red = [255,0,0]
blue = [0,0,255]

def point(x,y):
    return (x,y)

def drawRect(color,point):
    pygame.draw.rect(screen,color,[point[0],point[1],10,10],0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #fill the screen to black
    screen.fill(black)

    drawRect(blue, point(200,80) )
    drawRect(blue, point(100,80) )
    drawRect(red, point(200,80) )
    drawRect(red, point(101,179) )

    pygame.display.update()
    
    if(event.type == pygame.KEYDOWN):
           #start animation when user presses zero
           if(event.key == pygame.K_SPACE):
                #repeat pattern until it reaches the end of the screen
                #change position of the square to 20 pos away from x and y
                #change colors of the side of the squares
                #wait for 0.05s
                for i in range(0,100):
                    drawRect(blue, point(200,80+i) )
                    drawRect(blue, point(100,80+i) )
                    drawRect(red, point(200-i,80) )
                    drawRect(red, point(101+i,179) )

                    time.sleep(0.01)
                    pygame.display.update()
                    
                for i in range(0,100):
                    drawRect(red, point(80,60+(i*1.5) ) )
                    drawRect(red, point(220,60+(i*1.5) ) )
                    drawRect(blue, point(220-(i*1.4),60 ) )
                    drawRect(blue, point(81+(i*1.4),208 ) )

                    time.sleep(0.02)
                    pygame.display.update()

                for i in range(0,100):
                    drawRect(blue, point(60,40+(i*2) ) )
                    drawRect(blue, point(240,40+(i*2) ) )
                    drawRect(red, point(240-(i*1.8),40 ) )
                    drawRect(red, point(61+(i*1.8),237 ) )

                    time.sleep(0.03)
                    pygame.display.update()

                for i in range(0,100):
                    drawRect(red, point(40,20+(i*2.5) ) )
                    drawRect(red, point(260,20+(i*2.5) ) )
                    drawRect(blue, point(260-(i*2.2),20 ) )
                    drawRect(blue, point(41+(i*2.2),266 ) )

                    time.sleep(0.04)
                    pygame.display.update()

                for i in range(0,100):
                    drawRect(blue, point(20,0+(i*3) ) )
                    drawRect(blue, point(280,0+(i*3) ) )
                    drawRect(red, point(280-(i*2.6),0 ) )
                    drawRect(red, point(21+(i*2.6),295 ) )
                    
                    time.sleep(0.05)
                    pygame.display.update()

                break
