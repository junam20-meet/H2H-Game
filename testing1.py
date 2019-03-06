import turtle
from turtle import *


scr = turtle.Screen() 

def m1():
    userTurtle.setheading(90)
    userTurtle.fd(30)
    userTurtle.pos()
    for pos in positions:
        if pos[0] == userTurtle.pos()[0] and pos[1] == userTurtle.pos()[1]:
            print("Collision")
            turtle.bye()
    print(str(userTurtle.pos()) + ",")

def m2():
    userTurtle.setheading(180)
    userTurtle.fd(30)
    userTurtle.pos()
    for pos in positions:
        if pos[0] == userTurtle.pos()[0] and pos[1] == userTurtle.pos()[1]:
            print("Collision")
            turtle.bye()
    print(str(userTurtle.pos()) + ",")

def m3():
    userTurtle.setheading(360)
    userTurtle.fd(30)
    userTurtle.pos()
    for pos in positions:
        if pos[0] == userTurtle.pos()[0] and pos[1] == userTurtle.pos()[1]:
            print("Collision")
            turtle.bye()
    print(str(userTurtle.pos()) + ",")

def m4():
    userTurtle.setheading(-90)
    userTurtle.fd(30)
    userTurtle.pos()
    for pos in positions:
        if pos[0] == userTurtle.pos()[0] and pos[1] == userTurtle.pos()[1]:
            print("Collision")
            turtle.bye()
    print(str(userTurtle.pos()) + ",")

scr.onkeypress(m1, "Up")
scr.onkeypress(m2, "Left")
scr.onkeypress(m3, "Right")
scr.onkeypress(m4, "Down")
    
scr.listen()