import sys
import pygame
from pygame import gfxdraw
import math


def mul(A, B):
    result = [[0, 0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def project(x1, y1, z1, a, b, c):
    dx = x1-a
    dy = y2-b
    dz = z1-c

    dist =math.sqrt((dx**2)+(dy**2)+(dz**2))

    x=dx/(1+(dz/dist))
    y=dy/(1+(dz/dist))
    return x,y

pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.flip()

x1 = 180
y1 = 200
z1 = 50
x2 = 300
y2 = 200
z2 = 50
x3 = 300
y3 = 270
z3 = 50
x4 = 180
y4 = 270
z4 = 50



pygame.draw.lines(screen, (0,0,0), False, [(x1,y1),(x2,y2)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(x2,y2),(x3,y3)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(x3,y3),(x4,y4)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(x4,y4),(x1,y1)], 1)



x1,y1=project(x1,y1,z1,40,30,30)
x2,y2=project(x2,y2,z2,40,30,30)
x3,y3=project(x3,y3,z3,40,30,30)
x4,y4=project(x4,y4,z4,40,30,30)



print(x1,y1)
print(x2,y2)
print(x3,y3)
print(x4,y4)

pygame.draw.lines(screen, (0,0,0), False, [(x1,y1),(x2,y2)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(x2,y2),(x3,y3)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(x3,y3),(x4,y4)], 1)
pygame.draw.lines(screen, (0,0,0), False, [(x4,y4),(x1,y1)], 1)


pygame.display.update()


while 1:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
