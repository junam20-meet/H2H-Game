import turtle
from turtle import *



userTurtle = turtle.Turtle()
draw = turtle.Turtle()
scr = turtle.Screen()
wn = turtle.Screen()



def third_game():

    wn.title("Hell2Heaven Maze")
    turtle.register_shape("small_ghost.gif")
    userTurtle.shape("small_ghost.gif")

    def drawMaze():
        draw.pencolor("gold")
        draw.pensize(3)
        draw.penup()
        draw.goto(0,-180)
        draw.pendown()
        draw.speed(10)
        draw.setheading(180)
        draw.fd(180)
        draw.setheading(90)
        draw.fd(60)
        draw.setheading(0)
        draw.fd(120)
        draw.backward(120)
        draw.setheading(90)
        draw.fd(300)
        draw.setheading(0)
        draw.fd(120)
        draw.setheading(-90)
        draw.fd(120)
        draw.setheading(180)
        draw.fd(60)
        draw.setheading(90)
        draw.fd(60)
        draw.setheading(-90)
        draw.fd(120)
        draw.setheading(90)
        draw.fd(60)
        draw.setheading(0)
        draw.fd(120)
        draw.setheading(-90)
        draw.fd(60)
        draw.setheading(0)
        draw.fd(60)
        draw.setheading(-90)
        draw.fd(60)
        draw.backward(60)
        draw.setheading(0)
        draw.fd(60)
        draw.setheading(90)
        draw.fd(60)
        draw.penup()
        draw.setheading(180)
        draw.fd(60)
        draw.pendown()
        draw.setheading(90)
        draw.fd(60)
        draw.setheading(180)
        draw.fd(60)
        draw.setheading(90)
        draw.fd(60)
        draw.setheading(0)
        draw.fd(120)
        draw.setheading(-90)
        draw.fd(60)
        draw.backward(60)
        draw.setheading(0)
        draw.fd(60)
        draw.setheading(-90)
        draw.fd(240)
        draw.setheading(180)
        draw.fd(60)
        draw.setheading(-90)
        draw.fd(60)
        draw.setheading(180)
        draw.fd(120)
        draw.setheading(90)
        draw.fd(60)
        draw.setheading(180)
        draw.fd(60)
        draw.setheading(90)
        draw.fd(60)
        draw.backward(60)
        draw.setheading(180)
        draw.fd(60)
        draw.penup()
        draw.setheading(0)
        draw.fd(300)
        draw.pendown()
        draw.setheading(-90)
        draw.fd(120)
        draw.setheading(180)
        draw.fd(120)
        draw.ht()
        
        userTurtle.penup()
        userTurtle.goto(-30,180)
        userTurtle.setheading(-90)
        
    def mazeGame():
        scr.bgcolor("black")



    positions = [(-60.0,180.0),(-90.0,180.0),(-120.0,180.0),(-150.0,180.0),(-180.0,180.0),(-180.0,150.0),(-180.0,120.0),(-180.0,90.0),(-180.0,60.0),(-180.0,30.0),(-180.0,0.0),(-180.0,-30.0),(-180.0,-60.0),(-180.0,-90.0),(-180.00,-120.00),(-180.00,-150.00),(-180.00,-180.00),(-150.00,-180.00),(-120.00,-180.00),(-90.00,-180.00),(-60.00,-180.00),(-30.00,-180.00),(0.00,-180.00),(0.00,180.00),
    (0.00,150.00),
    (0.00,120.00),
    (30.00,120.00),
    (60.00,120.00),
    (60.00,90.00),
    (60.00,60.00),
    (60.00,90.00),
    (60.00,120.00),
    (-0.00,120.00),
    (-0.00,150.00),
    (-0.00,180.00),
    (30.00,180.00),
    (60.00,180.00),
    (90.00,180.00),
    (120.00,150.00),
    (120.00,120.00),
    (120.00,150.00),
    (120.00,180.00),
    (150.00,180.00),
    (180.00,180.00),
    (180.00,150.00),
    (180.00,120.00),
    (180.00,90.00),
    (180.00,60.00),
    (180.00,30.00),
    (180.00,0.00),
    (180.00,-30.00),
    (180.00,-90.00),
    (180.00,-120.00),
    (180.00,-150.00),
    (180.00,-180.00),
    (150.00,-180.00),
    (120.00,-180.00),
    (90.00,-180.00),
    (60.00,-180.00)]


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


    def win():
        px = userTurtle.xcor()
        py = userTurtle.ycor()
        if 10 < px < 50 and -240 < py < -180 :
            draw.hideturtle()
            draw.clear()
            userTurtle.hideturtle()
            turtle.bgpic("heaven_bg1.png")
            turtle.write("CONGRATS! YOU'VE MADE IT TO HEAVEN!!", align = "center", font = ("david", 30, "normal"))


    scr.onkeypress(m1, "Up")
    scr.onkeypress(m2, "Left")
    scr.onkeypress(m3, "Right")
    scr.onkeypress(m4, "Down")
        
    scr.listen()





    drawMaze()
    while True:
        mazeGame()
        win()
        for pos in positions:
            if pos[0] == userTurtle.pos()[0] and pos[1] == userTurtle.pos()[1]:
               print("Collision")
               turtle.bye()

