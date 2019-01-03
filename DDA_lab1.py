import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))
pygame.display.flip()

white=(255,255,255)

def ROUND(n):
	return int(n+0.5)

def dda(x1,y1,x2,y2):
	x,y = x1,y1
	length = abs(x2-x1) if abs(x2-x1) > abs(y2-y1) else abs(y2-y1)
	dx = (x2-x1)/float(length)
	dy = (y2-y1)/float(length)
	gfxdraw.pixel(screen,ROUND(x),ROUND(y),white)

	for i in range(length):
		x+= dx
		y+= dy
		gfxdraw.pixel(screen,ROUND(x),ROUND(y),(0,0,0))
	pygame.display.flip()

# dda(10,10,50,50)




#face

dda(200,270,100,350)
dda(180,206,45,314)
dda(100,350,45,314)
dda(180,206,200,270)


pygame.draw.circle(screen, (0,0,0), (100,290), 7, 0)
pygame.draw.arc(screen, (0,0,0), (30,280,60,60),-1, 0, 2)

# pygame.draw.arc(screen, (0,0,0), (70,300,20,20),-2, 1.5, 2)

#horn
dda(45,314,20,260)
dda(70,294,20,260)
dda(70,294,60,270)
dda(90,278,60,270)


#body
pygame.draw.rect(screen, (0,0,0), (200,200,150,150), 1)
pygame.draw.rect(screen, (0,0,0), (350,215,120,130), 1)

#fore legs
dda(260,350,265,370)
dda(330,350,325,370)
dda(265,370,325,370)

pygame.draw.rect(screen, (0,0,0), (285,370,40,70), 1)

dda(285,439,270,439)

dda(285,425,270,439)



#hind legs
dda(470,345,465,370)
dda(400,345,405,370)
dda(465,370,405,370)

pygame.draw.rect(screen, (0,0,0), (425,370,40,70), 1)

dda(425,439,410,439)

dda(425,425,410,439)

#tail
pygame.draw.arc(screen, (0,0,0), (470,250,90,20),-3, -1, 1)






# dda(1,1),(100,100)

# pygame.draw.circle(screen, (0,0,0), (100,290), 7, 0)



pygame.display.update()


while 1:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()