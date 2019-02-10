import sys
import pygame
from pygame import gfxdraw


def mul(A, B):
    result = [[0, 0, 0, 0]]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result


def beizer(Cx, Cy):
    B = [[-1, 3, -3, 1], [3, -6, 3, 0], [-3, 3, 0, 0], [1, 0, 0, 0]]
    t = 0
    A = [[0, 0, 0, 0]]
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


pygame.init()
screen = pygame.display.set_mode((640, 480))
screen.fill((255, 255, 255))
pygame.display.flip()

white = (255, 255, 255)
# left neck
Cx = [[90], [100], [100], [90]]
Cy = [[20], [40], [60], [80]]
beizer(Cx, Cy)
# right neck
Cx = [[130], [120], [120], [130]]
Cy = [[20], [40], [60], [80]]
beizer(Cx, Cy)
# top
Cx = [[90], [110], [110], [130]]
Cy = [[20], [25], [25], [20]]
beizer(Cx, Cy)
# left body
Cx = [[90], [60], [60], [100]]
Cy = [[80], [110], [140], [170]]
beizer(Cx, Cy)
# right body
Cx = [[130], [160], [160], [120]]
Cy = [[80], [110], [140], [170]]
beizer(Cx, Cy)
# bottom
Cx = [[100], [105], [115], [120]]
Cy = [[170], [170], [170], [170]]
beizer(Cx, Cy)


pygame.display.update()


while 1:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()
