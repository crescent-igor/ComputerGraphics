import pygame
import sys
import math
import time

pygame.init()


screen=pygame.display.set_mode((640,480))
color=[(255,0,0),(0,255,0),(0,0,255),(0,0,0),(255,255,255)]

screen.fill(color[4])

xwmin=100
xwmax=300

ywmin=100
ywmax=300

pygame.draw.lines(screen, (0,0,0), False, [(xwmin,ywmax),(xwmax,ywmax)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(xwmax,ywmin),(xwmax,ywmax)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(xwmin,ywmin),(xwmax,ywmin)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(xwmin,ywmax),(xwmin,ywmin)], 1)



def liangBanskyClip(x0,y0,x1,y1):
    dx=x1-x0
    dy=y1-y0
    q1=x0-xwmin
    q2=xwmax-x0
    q3=y0-ywmin
    q4=ywmax-y0

    p1=-1*dx
    p2=dx
    p3=-1*dy
    p4=dy

    umin=1
    umax=0

    u1=q1/p1
    u2=q2/p2
    u3=q3/p3
    u4=q4/p4

    if(u1>0 and u1<1):
        if(umin>u1):
            umin=u1
        if(umax<u1):
            umax=u1    
        
    if(u2>0 and u2<1):
        if(umin>u2):
            umin=u2
        if(umax<u2):
            umax=u2    
    if(u3>0 and u3<1):
        if(umin>u3):
            umin=u3
        if(umax<u3):
            umax=u3    
    if(u4>0 and u4<1):
        if(umin>u4):
            umin=u4
        if(umax<u4):
            umax=u4  
    print("umin"+str(umin))
    print("umax"+str(umax))         
    if(umin<umax):
        print("dx"+str(dx))
        print("dy"+str(dy))
        # print()
        # print()
        
        xmin=x0+(umin*(dx))
        ymin=y0+(umin*(dy))
        xmax=x0+(umax*(dx))
        ymax=y0+(umax*(dy))
        print(xmin)
        print(ymin)
        print(xmax)
        print(ymax)
        pygame.draw.lines(screen, (0,0,0), False, [(xmin,ymin),(xmax,ymax)], 1)         
        
    


x0=int(input())
y0=int(input())
x1=int(input())
y1=int(input())

liangBanskyClip(x0,y0,x1,y1)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    
