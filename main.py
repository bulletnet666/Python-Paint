from turtle import *
import winsound

loading = Turtle()
loading.speed(0)
loading.penup()
loading.color("black")
loading.hideturtle()
loading.goto(0-1, -100-1)
loading.write("Loading..", font=('Courier', 20), align="center")
loading.goto(0-1, -120-1)
loading.write("don't click anything", font=('Courier', 20), align="center")
loading.color("crimson")
loading.goto(0, -100)
loading.write("Loading..", font=('Courier', 20), align="center")
loading.goto(0, -120)
loading.write("don't click anything", font=('Courier', 20), align="center")

status = Turtle()
status.speed(0)
status.penup()
status.hideturtle()
status.goto(0-1, -260-1)
status.color("black")
status.write("Pen status:On", font=('Courier', 10), align="center")
status.goto(0, -260)
status.color("dodgerblue")
status.write("Pen status:On", font=('Courier', 10), align="center")

p = Turtle()
p.penup()
p.speed(0)
p.left(90)
p.hideturtle()
p.goto(-50-1, -230-1)
p.color("black")
p.write("Pen", font=('Courier', 20), align="center")
p.goto(-50, -230)
p.color("dodgerblue")
p.write("Pen", font=('Courier', 20), align="center")
p.goto(20-1, -210-1)
p.color("black")
p.write("off", font=('Courier', 20))
p.goto(20, -210)
p.color("dodgerblue")
p.write("off", font=('Courier', 20))
p.goto(20-1, -245-1)
p.color("black")
p.write("on", font=('Courier', 20))
p.goto(20, -245)
p.color("dodgerblue")
p.write("on", font=('Courier', 20))


pu = Turtle()
pu.penup()
pu.speed(0)
pu.left(90)
pu.shape("triangle")
pu.goto(0, -200)
pu.color("dodgerblue")

ped = Turtle()
ped.penup()
ped.speed(0)
ped.right(90)
ped.shape("triangle")
ped.goto(0, -230)
ped.color("dodgerblue")

sz = Turtle()
sz.penup()
sz.speed(0)
sz.hideturtle()
sz.goto(0, 350-15)
sz.color("dodgerblue")
sz.write("1", font=('Courier', 15), align="center")

cred = Turtle()
cred.hideturtle()
cred.speed(0)
cred.penup()
cred.goto(-435-1, -380-1)
cred.color("black")
cred.write("by bulletnet666", font=('Courier', 10))
cred.goto(-435, -380)
cred.color("cadetblue")
cred.write("by bulletnet666", font=('Courier', 10))

clear = Turtle()
clear.speed(0)
clear.penup()
clear.color("black")
clear.shape("circle")
clear.goto(25, -350)
clear.write("<-Clear", font=('Courier', 20))
clear.goto(0, -350+15)

board = Turtle()
board.speed(0)
board.penup()
board.color("black")

red_c = Turtle()
red_c.speed(0)
red_c.penup()
red_c.color("brown")
red_c.shape("circle")

blue_c = red_c.clone()
blue_c.color("mediumblue")

white_c = red_c.clone()
white_c.color("grey")

green_c = red_c.clone()
green_c.color("green")

yellow_c = red_c.clone()
yellow_c.color("olive")

red_t = Turtle()
red_t.speed(0)
red_t.penup()
red_t.color("red")
red_t.shape("circle")

blue_t = red_t.clone()
blue_t.color("blue")

green_t = red_t.clone()
green_t.color("lime")

yellow_t = red_t.clone()
yellow_t.color("yellow")

white_t = red_t.clone()
white_t.color("white")

board.hideturtle()
board.goto(-425, 125)
board.pendown()
board.begin_fill()
board.forward(50)
board.right(90)
board.forward(25 * 10)
board.right(90)
board.forward(50)
board.right(90)
board.forward(25 * 10)
board.right(90)
board.end_fill()
board.penup()
board.left(90)
board.forward(25)
board.right(90)
board.pendown()
board.write("background", font=('Courier', 20))
board.penup()
board.goto(400-25, 125)
board.pendown()
board.begin_fill()
board.forward(50)
board.right(90)
board.forward(25 * 10)
board.right(90)
board.forward(50)
board.right(90)
board.forward(25 * 10)
board.right(90)
board.end_fill()
board.penup()
board.forward(50)
board.left(90)
board.forward(25)
board.left(90)
board.pendown()
board.write("colors", font=('Courier', 20), align="right")
board.penup()
board.hideturtle()
red_t.goto(-400, -50)
blue_t.goto(-400, -100)
white_t.goto(-400, 0)
green_t.goto(-400, 50)
yellow_t.goto(-400, 100)

red_c.goto(400, -50)
blue_c.goto(400, -100)
white_c.goto(400, 0)
green_c.goto(400, 50)
yellow_c.goto(400, 100)


def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10


scr = red_t.getscreen()


def setRed(x, y):
    scr.bgcolor("red")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def setBlue(x, y):
    scr.bgcolor("blue")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def setGreen(x, y):
    scr.bgcolor("lime")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def setYellow(x, y):
    scr.bgcolor("yellow")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def setWhite(x, y):
    scr.bgcolor("white")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def cRed(x, y):
    cursor.color("brown")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def cBlue(x, y):
    cursor.color("mediumblue")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def cGreen(x, y):
    cursor.color("green")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def cYellow(x, y):
    cursor.color("olive")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def cWhite(x, y):
    cursor.color("grey")
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)


def snap(x, y):
    winsound.PlaySound("snap.wav", winsound.SND_ASYNC)


def unsnap(x, y):
    winsound.PlaySound("unsnap.wav", winsound.SND_ASYNC)


def move(x, y):
    cursor.goto(x, y)


def clean(x, y):
    cursor.penup()
    cursor.clear()
    cursor.goto(0, 0)
    cursor.pendown()
    if penstatus == 0:
        cursor.penup()
    winsound.PlaySound("clear.wav", winsound.SND_ASYNC)


SC = 1


def SCsmall(x, y):
    global SC
    if SC == 1:
        SCs.hideturtle()
    else:
        SC = SC-1
        SCb.showturtle()
        sz.clear()
        sz.color("dodgerblue")
        sz.write(str(SC), font=('Courier', 15), align="center")
        cursor.pensize(SC)
        winsound.PlaySound("SC.wav", winsound.SND_ASYNC)
        if SC == 1:
            SCs.hideturtle()


def SCbig(x, y):
    global SC
    if SC == 25:
        SCb.hideturtle()
    else:
        SC = SC+1
        SCs.showturtle()
        sz.clear()
        sz.color("dodgerblue")
        sz.write(str(SC), font=('Courier', 15), align="center")
        cursor.pensize(SC)
        winsound.PlaySound("SC.wav", winsound.SND_ASYNC)
        if SC == 25:
            SCb.hideturtle()

penstatus = 1

def penup(x, y):
    global penstatus
    cursor.penup()
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)
    status.clear()
    penstatus = 0
    status.goto(0 - 1, -260 - 1)
    status.color("black")
    status.write("Pen status:Off", font=('Courier', 10), align="center")
    status.goto(0, -260)
    status.color("dodgerblue")
    status.write("Pen status:Off", font=('Courier', 10), align="center")


def pendown(x, y):
    global penstatus
    cursor.pendown()
    winsound.PlaySound("untitled.wav", winsound.SND_ASYNC)
    status.clear()
    penstatus = 1
    status.goto(0 - 1, -260 - 1)
    status.color("black")
    status.write("Pen status:On", font=('Courier', 10), align="center")
    status.goto(0, -260)
    status.color("dodgerblue")
    status.write("Pen status:On", font=('Courier', 10), align="center")


cursor = red_t.clone()
cursor.pendown()
cursor.color("grey")

cursor.penup()
cursor.goto(0, 0)
cursor.pendown()

cursor.ondrag(move)
cursor.onclick(snap)
cursor.onrelease(unsnap)
red_t.onclick(setRed)
blue_t.onclick(setBlue)
green_t.onclick(setGreen)
yellow_t.onclick(setYellow)
white_t.onclick(setWhite)

pu.onclick(penup)
ped.onclick(pendown)

red_c.onclick(cRed)
blue_c.onclick(cBlue)
green_c.onclick(cGreen)
yellow_c.onclick(cYellow)
white_c.onclick(cWhite)

clear.onclick(clean)

SCs = Turtle()
SCs.penup()
SCs.speed(0)
SCs.left(180)
SCs.shape("triangle")
SCs.color("dodgerblue")
SCs.goto(-25, 350)
SCs.onclick(SCsmall)
SCs.hideturtle()

SCb = Turtle()
SCb.penup()
SCb.speed(0)
SCb.shape("triangle")
SCb.color("dodgerblue")
SCb.goto(25, 350)
SCb.onclick(SCbig)

SCi = Turtle()
SCi.penup()
SCi.speed(0)
SCi.hideturtle()
SCi.goto(0, 320)
SCi.color("dodgerblue")
SCi.write("Brush size", font=('Courier', 10), align="center")

cursor.clear()
loading.clear()
winsound.PlaySound("LD.wav", winsound.SND_ASYNC)

done()