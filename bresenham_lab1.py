import sys,pygame
from pygame import gfxdraw

pygame.init()
screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255))
pygame.display.flip()
white = (0,0,0)

def bresenham(x1,y1,x2,y2):
	dx = x2-x1
	dy = y2-y1

	D = 2*dy - dx
	gfxdraw.pixel(screen,x1,y1,white)
	y = y1

	for x in range(x1+1,x2+1):
		if D > 0:
			y += 1
			gfxdraw.pixel(screen,x,y,white)
			D += (2*dy-2*dx)
		else:
			gfxdraw.pixel(screen,x,y,white)
			D += 2*dy
	pygame.display.flip()

bresenham(200,270,100,350)
bresenham(180,206,45,314)
bresenham(100,350,45,314)
bresenham(180,206,200,270)


pygame.draw.circle(screen, (0,0,0), (100,290), 7, 0)
pygame.draw.arc(screen, (0,0,0), (30,280,60,60),-1, 0, 2)

# pygame.draw.arc(screen, (0,0,0), (70,300,20,20),-2, 1.5, 2)

#horn
bresenham(45,314,20,260)
bresenham(70,294,20,260)
bresenham(70,294,60,270)
bresenham(90,278,60,270)


#body
pygame.draw.rect(screen, (0,0,0), (200,200,150,150), 1)
pygame.draw.rect(screen, (0,0,0), (350,215,120,130), 1)

#fore legs
bresenham(260,350,265,370)
bresenham(330,350,325,370)
bresenham(265,370,325,370)

pygame.draw.rect(screen, (0,0,0), (285,370,40,70), 1)

bresenham(285,439,270,439)

bresenham(285,425,270,439)



#hind legs
bresenham(470,345,465,370)
bresenham(400,345,405,370)
bresenham(465,370,405,370)

pygame.draw.rect(screen, (0,0,0), (425,370,40,70), 1)

bresenham(425,439,410,439)

bresenham(425,425,410,439)

#tail
pygame.draw.arc(screen, (0,0,0), (470,250,90,20),-3, -1, 1)






# bresenham(1,1),(100,100)

# pygame.draw.circle(screen, (0,0,0), (100,290), 7, 0)



pygame.display.update()


while 1:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()