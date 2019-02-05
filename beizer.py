import sys
import pygame
from pygame import gfxdraw


A = [[0, 0, 0, 0]]
B = [[-1, 3, -3, 1],
     [3, -6, 3, 0],
     [-3, 3, 0, 0],
     [1, 0, 0, 0]]
Cx = [[50], [50], [80], [80]]
Cy = [[35], [70], [40], [80]]


def mul(A, B):
    result = [[0, 0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.flip()

white = (255, 255, 255)


t = 0
while(t < 1):
    A[0][0] = t*t*t
    A[0][1] = t*t
    A[0][2] = t
    A[0][3] = 1
    C = mul(A, B)
    D1 = mul(C, Cx)
    D2 = mul(C, Cy)
    gfxdraw.pixel(screen, round(D1[0][0]), round(D2[0][0]), (0, 0, 0))
    t = t+0.005
pygame.display.update()


while 1:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
