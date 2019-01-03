import pygame
import sys
import math
import time

pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
    screen=pygame.display.set_mode((640,480))
    color=[(255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,255,255)]

    screen.fill(color[4])

    #face

    pygame.draw.lines(screen, (0,0,0), False, [(200,270),(100,350)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(180,206),(45,314)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(100,350),(45,314)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(180,206),(200,270)], 1)
    
    #horn
    pygame.draw.lines(screen, (0,0,0), False, [(45,314),(20,260)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(50,310),(20,260)], 1)
    
    
    #body
    pygame.draw.rect(screen, (0,0,0), (200,200,150,150), 1)
    pygame.draw.rect(screen, (0,0,0), (350,215,120,130), 1)
    
    #fore legs
    pygame.draw.lines(screen, (0,0,0), False, [(260,350),(265,370)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(330,350),(325,370)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(265,370),(325,370)], 1)

    pygame.draw.rect(screen, (0,0,0), (285,370,40,70), 1)
    
    pygame.draw.lines(screen, (0,0,0), False, [(285,439),(270,439)], 1)
    
    pygame.draw.lines(screen, (0,0,0), False, [(285,425),(270,439)], 1)
    

    
    #hind legs
    pygame.draw.lines(screen, (0,0,0), False, [(470,345),(465,370)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(400,345),(405,370)], 1)
    pygame.draw.lines(screen, (0,0,0), False, [(465,370),(405,370)], 1)
    
    pygame.draw.rect(screen, (0,0,0), (425,370,40,70), 1)
    
    pygame.draw.lines(screen, (0,0,0), False, [(425,439),(410,439)], 1)
    
    pygame.draw.lines(screen, (0,0,0), False, [(425,425),(410,439)], 1)



    

    # pygame.draw.lines(screen, (0,0,0), False, [(1,1),(100,100)], 1)

    # pygame.draw.circle(screen, (255,0,255), (300,300), 10, 0)
    # pygame.draw.arc(screen, (0,0,0), (60,60,60,60),0.2, 3, 0)



    pygame.display.update()

