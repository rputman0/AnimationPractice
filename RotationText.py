import sys, pygame
from pygame.locals import *

pygame.init()
size = width, height = 300,100
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Font")
myfont = pygame.font.SysFont("sans-serif",48)

WHITE = (255,255,255)
BLACK = (0,0,0)

text = "Hello World "

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    txtScreen = myfont.render(text,1,BLACK)
    text = text[len(text) - 1]+ text[0:len(text) - 1]
    txtRot = myfont.render(text,1,WHITE)
    
    screen.blit(txtScreen, (5,10))
    screen.blit(txtRot, (5,10))
    
    pygame.time.wait(600)

    #make rotating animation
    #by putting the last character at the begging of the word
        #rotate -> erotat -> terota ->
