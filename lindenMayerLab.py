import turtle
import sys


def square(turtle):
    for i in range(0, 6):
        turtle.forward(20)
        turtle.right(60)


def lindenMayer(turtle, iter, angle, len):
    # turtle.goto(x,y)
    i = 0
    while(i < iter):
        turtle.forward(len)
        turtle.right(90)
        square(turtle)
        # turtle.forward(50)
        turtle.right(90)
        turtle.forward(len)
        turtle.right(angle)
        i = i+1


def newFig(turtle, iter):
    for i in range(0, iter):
        turtle.forward(50)
        turtle.backward(25)
        turtle.left(90)
        turtle.forward(25)
        turtle.right(60)


wn = turtle.Screen()
wn.bgcolor("light green")
wn.title("Turtle")
skk = turtle.Turtle()


# for i in range(0, 4):
#     lindenMayer(skk, 12, 150, 50+(i*20))
newFig(skk, 20)

turtle.done()
sys.exit()
