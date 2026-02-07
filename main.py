from turtle import * 
from random import randint
t = Turtle()
t.color('blue')
t.width(5)
t.shape('circle')
t.pendown()
t.speed(3)


def draw(x, y):
    t.goto(x, y)

t.ondrag(draw)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
def setGreen():
    t.color('green')
scr = t.getscreen()

scr.listen()
scr.onkey(setGreen, 'g')

def setRed():
    t.color('red')
scr = t.getscreen()

scr.listen()
scr.onkey(setRed, 'r')

def setBlue():
    t.color('blue')
scr = t.getscreen()

def random_color():
    colors = ['red', 'green', 'blue', 'yellow', 'orange','purple', 'pink', 'cyan', 'magenta','black', 'white', 'gray', 'brown' ]
    rand_num = randint(0,len(colors)-1)
    t.color(colors[rand_num])
def stepRight():
    random_color()
    t.goto(t.xcor()+ randint(0,20), t.ycor())
    
scr = t.getscreen()
scr.listen()
scr.onkey(stepRight, 'Right')

def stepUp():
    random_color()
    t.goto(t.xcor(), t.ycor() + randint(0,20))

scr = t.getscreen()
scr.listen()
scr.onkey(stepUp, 'Up')

def stepLeft():
    random_color()
    t.goto(t.xcor()- randint(0,20), t.ycor())

scr = t.getscreen()
scr.listen()
scr.onkey(stepLeft, 'Left')

def stepDown():
    random_color()
    t.goto(t.xcor(), t.ycor()- randint(0,20) )



scr = t.getscreen()
scr.listen()
scr.onkey(stepDown, 'Down')


scr.listen()
scr.onkey(setBlue, 'b')

scr = t.getscreen()
scr.onscreenclick(move)

t.ondrag(draw)


while True:
    r_num = randint(0,3)
    if r_num == 0:
        stepDown()
    if r_num == 1:
        stepLeft()
    if r_num == 2:
        stepRight()
    if r_num == 3:  
        stepUp()

