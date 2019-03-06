import turtle
import time
from personal_project_ball import *
import random
import math

#def GHOST ():

    # ghost = Ball(0, 0,3, 1, "blue", 70, True)

    # turtle.register_shape("small_ghost.gif")
    # ghost.shape("small_ghost.gif")

def first_game():
    go = turtle.clone()
    #again = turtle.Turtle()
    go.hideturtle()

    turtle.colormode(1)

    turtle.tracer(0)
    turtle.hideturtle() 

    running = True
    screen_width = turtle.getcanvas().winfo_width()/2
    screen_height = turtle.getcanvas().winfo_height()/2




    ghost = Ball(0, 0,3, 1, "blue", 70, True)

    turtle.register_shape("small_ghost.gif")
    ghost.shape("small_ghost.gif")





    number_of_balls = 9
    minimum_ball_radius = 10
    maximum_ball_radius = 100
    minimum_ball_dx = -5
    maximum_ball_dx = 5
    minimum_ball_dy = -5
    maximum_ball_dy = 5

    turtle.register_shape("flying_keys.gif")

    BALLS = []
    FIRES = []

    for i in range (number_of_balls) :
        x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
        y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
        dx = random.randint(minimum_ball_dx, maximum_ball_dx)
        dy = random.randint(minimum_ball_dy, maximum_ball_dy)
        r = random.randint(minimum_ball_radius, maximum_ball_radius)
        color = (random.random(), random.random(), random.random())

        new_balls = Ball(x, y, dx, dy, color, 20, True)
        new_balls.shape("flying_keys.gif")
        BALLS.append(new_balls)





        x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
        y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
        dx = random.randint(minimum_ball_dx, maximum_ball_dx)
        dy = random.randint(minimum_ball_dy, maximum_ball_dy)
        r = random.randint(minimum_ball_radius, maximum_ball_radius)
        color = (random.random(), random.random(), random.random())


        new_fires = Ball(x, y, dx, dy, color, 20, False)
        FIRES.append(new_fires)






# def arrow_keys_moving():
#     setup(500, 500)
#     Screen()
#     title("Turtle Keys")

#     def k1():
#         ghost.forward(10)

#     def k2():
#         ghost.left(90)

#     def k3():
#         ghost.right(90)


#     onkey(k1, "Up")
#     onkey(k2, "Left")
#     onkey(k3, "Right")


















    #def move_all_balls():
        #for b in BALLS:
          #  b.move(screen_width, screen_height)

    def collide(ball_a, ball_b):
        if (ball_a == ball_b):
            return False

        distance = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(), 2) + math.pow(ball_a.ycor() - ball_b.ycor(), 2))
        if ball_a.r + ball_b.r >= distance:
            return True

        else:
            return False


    #distance_ab = math.sqrt(math.pow(ball_a.xcor() - ball_b.xcor(), 2) + math.pow(ball_a.ycor() - ball_b.ycor(), 2))

    def check_all_balls_collision():
        global running
        all_balls = []
        all_fires = []
        all_balls.append(ghost)
        
        for ball in BALLS:
            all_balls.append(ball)
        for ball in FIRES:
            all_balls.append(ball)
        for ball_a in all_balls :
            for ball_b in all_balls :
                if (collide(ball_a, ball_b)):
                    r1 = ball_a.r
                    r2 = ball_b.r
                    if ball_a.CanBeEaten:
                        if ball_a != ghost:
                            ball_a.ht()
                    if ball_b.CanBeEaten:
                        if ball_b != ghost:
                            ball_b.ht()
                    if ball_a.CanBeEaten == False:
                        if ball_a != ghost:
                            quit()
                    if ball_b.CanBeEaten == False:
                        if ball_b != ghost:
                            quit()





                    x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
                    y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
                    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
                    dy = random.randint(minimum_ball_dy, maximum_ball_dy)
                    while (dx == 0 and dy ==0):
                        dx = random.randint(minimum_ball_dx, maximum_ball_dx)
                        dy = random.randint(minimum_ball_dy, maximum_ball_dy)
                    r = random.randint(minimum_ball_radius, maximum_ball_radius)
                    color = (random.random(), random.random(), random.random())

                    if  (r1<r2):
                        ball_a.ht()
                    else:
                        ball_b.ht()
                    #if (my_ball == ball_a and r1<r2 or my_ball == ball_b and r1>r2):
                     #   running = False
                       # go.write( "Game Over!",move=False, align="center", font=("Comic Sans MS", 40, "normal"))



    def movearound():
        x=turtle.getcanvas().winfo_pointerx() - screen_width*2

        y = screen_height*1.5 - turtle.getcanvas().winfo_pointery()

        ghost.goto(x, y)

                    
    running = True 
    while running:
        
        screen_width = turtle.getcanvas().winfo_width()/2
        screen_height = turtle.getcanvas().winfo_height()/2


        movearound()
        #arrow_keys_moving()
        #move_all_balls()
        # turtle.update()
        # time.sleep(2)
        check_all_balls_collision()

        time.sleep(.1)
        #GHOST()

        turtle.update()
        


#first_game()