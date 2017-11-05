import pygame, sys

pygame.init()

#set up the window
width,height = 300,300
screen = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('Draw Pentagon')

#have the default values be offscreen
vertices = [(-10,-10),(-10,-10),(-10,-10),(-10,-10),(-10,-10)]

iter = 0
screen.fill((255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    #ask the user for five input points to draw a polygon
    if(event.type == pygame.MOUSEBUTTONDOWN and iter < 5):
        #click the window at five random locations on the screen
            point = pygame.mouse.get_pos()
            vertices[iter] = point
            pygame.draw.circle(screen,(0,0,255),point,5,0)
            pygame.display.update()
            #ask user for different inputs, rather than checking whenever the screen refreshes
            pygame.time.wait(300)
            iter += 1
    #draw the polygon
    elif(iter >= 5):
        pygame.draw.polygon(screen,(255,165,0),vertices,0)
        pygame.display.update()
    
    pygame.display.update()
 
pygame.exitonclose()
