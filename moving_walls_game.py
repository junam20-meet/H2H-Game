from turtle import  *
from personal_project_ball import *
from mazegame import *
import time
import random
import math
import turtle
import threading



ghost = turtle.clone()
go = turtle.clone()
#go.color("red")
door = turtle.clone()
right_wall = turtle.clone()


left_wall = turtle.clone()


rx = right_wall.xcor()

lx = left_wall.xcor()
temp=turtle.clone()
isSafe = True

def second_game():
    tracer(0)
    # ghost = turtle.clone()
    ghost.penup()

    # go = turtle.clone()
    go.ht()

    turtle.register_shape("small_ghost.gif")
    ghost.shape("small_ghost.gif")

    # door = turtle.clone()
    turtle.register_shape("Door.gif")
    door.shape("Door.gif")
    door.penup()
    door.goto(0, 325)

    ghost.goto(0,-400)

    turtle.ht()
    turtle.speed(0)


    # right_wall = turtle.clone()
    right_wall.color("red")
    right_wall.st()
    right_wall.penup()
    right_wall.shape("square")
    right_wall.speed(1000000)
    right_wall.shapesize(60)
    right_wall.goto(1000,0)


    # left_wall = turtle.clone()
    left_wall.color("red")
    left_wall.st()
    left_wall.penup()
    left_wall.shape("square")
    left_wall.speed(100000)
    left_wall.shapesize(60)
    left_wall.goto(-1000,0)

    # rx = right_wall.xcor()

    # lx = left_wall.xcor()

    isSafe = True
    #temp=turtle.clone()
    temp.st()
    temp.penup()
    temp.shape("square")
    temp.goto(0,0)

    def collide(ghost, left_wall, right_wall):
        global isSafe
        if (left_wall.xcor()+600) >= ghost.xcor() or (right_wall.xcor()-600) <= ghost.xcor() :
            print("collided")
            isSafe = False
            return True
        return False
            
    def col_with_door(ghost, door):
        if ghost == door:
            return False
        distance = math.sqrt(math.pow(ghost.xcor() - door.xcor(), 2) + math.pow(ghost.ycor() - door.ycor(), 2))
        if distance <= 30:
            return True
        else:
            return False

    def walls_move():
        global isSafe
        rx = right_wall.xcor()

        lx = left_wall.xcor()
        while isSafe:
            collide(ghost,left_wall,right_wall)
            right_wall.goto(rx,0)
            rx = rx - 1
            left_wall.goto(lx,0)
            lx = lx + 1
            ghost.clear()
            update()
            time.sleep(0.01)
            if collide(ghost, left_wall, right_wall):
                go.write("GAME OVER!!! TRY AGAIN IN 1000 YEARS!!!", align = "center", font = ("david", 30, "normal"))
                time.sleep(4)
                #print("Reached")
                quit()
            if col_with_door(ghost, door):
                #turtle.clearscreen()
                # turtle.bgpic("heaven_bg1.png")
                # turtle.write("CONGRATS! YOU'VE MADE IT TO HEAVEN!!", align = "center", font = ("david", 30, "normal"))
                isSafe = False
                ghost.hideturtle()
                door.hideturtle()
                left_wall.hideturtle()
                right_wall.hideturtle()
                third_game()


    # t = threading.Thread(name = 'walls', target = walls_move)
    #t.start()

    def key1():
        ghost.setheading(90)
        ghost.fd(4.5)
        update()
        

    def key2():
        ghost.setheading(180)
        ghost.fd(4.5)
        update()

    def key3():
        ghost.setheading(270)
        ghost.fd(4.5)
        update()

    def key4():
        ghost.setheading(360)
        ghost.fd(4.5)
        update()

    Screen().onkey(key1, "Up")
    Screen().onkey(key2, "Left")
    Screen().onkey(key3, "Down")
    Screen().onkey(key4, "Right")

    Screen().listen()

    walls_move()

#second_game()
