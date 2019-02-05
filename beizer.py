import pygame
import sys
import math
import time
from pygame import gfxdraw


B = [[-1, 3, -3, 1], 
    [3, -6, 3, 0], 
    [-3, 3, 0, 0], 
    [1, 0, 0,0]] 
      
C1=[[5],[5],[8],[8]]
C2=[[3.5],[7],[4],[8]]



def mul1(A,B):
    result = [[0, 0, 0, 0]] 
  
    for i in range(len(A)):  
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
  
    for r in result:
    return r     


def mul2(A,B):
    result = [[0, 0, 0, 0]] 
  
    for i in range(len(A)):  
        for j in range(len(B[0])): 
            for k in range(len(B)): 
                result[i][j] += A[i][k] * B[k][j] 
  
    return result[0][0]


pygame.init()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()


     
    screen=pygame.display.set_mode((640,480))
    color=[(255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,255,255)]

    screen.fill(color[4])
    t=0
    tx=0
    ty=0

    while(t!=1):
        A=[[t*t*t,t*t,t,1]]
        r1=mul1(A,B)
        
        gfxdraw.pixel(screen,round(tx) , round(ty), (0, 0, 0))
        t=t+0.1
        tx=tx+0.1
        ty=ty+0.1

        

    

    pygame.display.update()
