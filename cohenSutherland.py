import pygame
from pygame import gfxdraw
import sys
import math
import time

pygame.init()


screen = pygame.display.set_mode((640, 480))
color = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 0, 0), (255, 255, 255)]

screen.fill(color[4])

xwmin = 100
xwmax = 300

ywmin = 100
ywmax = 300

pygame.draw.lines(screen, (0, 0, 0), False, [
    (xwmin, ywmax), (xwmax, ywmax)], 1)
pygame.draw.lines(screen, (0, 0, 0), False, [
    (xwmax, ywmin), (xwmax, ywmax)], 1)
pygame.draw.lines(screen, (0, 0, 0), False, [
    (xwmin, ywmin), (xwmax, ywmin)], 1)
pygame.draw.lines(screen, (0, 0, 0), False, [
    (xwmin, ywmax), (xwmin, ywmin)], 1)


def dda(x1, y1, x2, y2):
    x, y = x1, y1
    xt, yt = x2, y2
    length = abs(x2-x1) if abs(x2-x1) > abs(y2-y1) else abs(y2-y1)
    dx = (x2-x1)/float(length)
    dy = (y2-y1)/float(length)
    
    for i in range(round(length/2)):
        x += dx
        y += dy
        xt = xt-dx
        yt = yt-dy
        code = 0
        codet = 0
        if((x < xwmin) & (y > ywmax)):
            code = 9
        elif((x < xwmin) & (y < ywmax) & (y > ywmin)):
            code = 1
        elif((x < xwmin) & (y < ywmin)):
            code = 5
        elif((x > xwmin) & (x < xwmax) & (y < ywmin)):
            code = 8
        elif((x > xwmin) & (x < xwmax) & (y > ywmax)):
            code = 4
        elif((x > xwmax) & (y < ywmin)):
            code = 10
        elif((x > xwmax) & (y < ywmax) & (y > ywmin)):
            code = 2
        elif((x > xwmax) & (y > ywmax)):
            code = 6

        if((xt < xwmin) & (yt > ywmax)):
            codet = 9
        elif((xt < xwmin) & (yt < ywmax) & (yt > ywmin)):
            codet = 1
        elif((xt < xwmin) & (yt < ywmin)):
            codet = 5
        elif((xt > xwmin) & (xt < xwmax) & (yt < ywmin)):
            codet = 8
        elif((xt > xwmin) & (xt < xwmax) & (yt > ywmax)):
            codet = 4
        elif((xt > xwmax) & (yt < ywmin)):
            codet = 10
        elif((xt > xwmax) & (yt < ywmax) & (yt > ywmin)):
            codet = 2
        elif((xt > xwmax) & (yt > ywmax)):
            codet = 6
        if(code==0):
            gfxdraw.pixel(screen, round(x), round(y), (0, 0, 0))
        if(codet==0):
            gfxdraw.pixel(screen, round(xt), round(yt), (0, 0, 0))
           
    pygame.display.flip()


x0=int(input())
y0=int(input())
x1=int(input())
y1=int(input())
dda(x0, y0, x1, y1)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
