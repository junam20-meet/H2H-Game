import turtle
import time
from personal_project_ball import *
import random
import math



def first_game ():
	go = turtle.clone()
	#again = turtle.Turtle()
	go.hideturtle()

	Door = turtle.clone()
	Door.ht()
	Door.penup()
	Door.goto(400, 400)


	turtle.colormode(1)

	turtle.tracer(0)
	turtle.hideturtle() 

	running = True
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2




	my_ball = Ball(0, 0, 3, 1, "blue", 15, True)

	turtle.register_shape("small_ghost.gif")
	my_ball.shape("small_ghost.gif")





	number_of_KEYS = 9
	minimum_ball_radius = 10
	maximum_ball_radius = 100
	minimum_ball_dx = -5
	maximum_ball_dx = 5
	minimum_ball_dy = -5
	maximum_ball_dy = 5

	turtle.register_shape("Door.gif")
	Door.shape("Door.gif")
	turtle.register_shape("flying_keys.gif")
	turtle.register_shape("fire.gif")
	KEYS = []
	FIRES = []

	for i in range (number_of_KEYS) :
	#   x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	#    y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	#    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	#    dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	#    r = random.randint(minimum_ball_radius, maximum_ball_radius)
	#    color = (random.random(), random.random(), random.random())

	    #flying_keys = Keys_Fires(x, y, dx, dy, 20, color, True)
	    #flying_keys.shape("flying_keys.gif")
	    #KEYS.append(flying_keys)





	    x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	    y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	    dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	    r = random.randint(minimum_ball_radius, maximum_ball_radius)
	    color = (random.random(), random.random(), random.random())

	    flying_keys = Ball(x, y, dx, dy,color,15, True)
	    flying_keys.shape("flying_keys.gif")
	    KEYS.append(flying_keys)
	    x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	    y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	    dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	    dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	    r = random.randint(minimum_ball_radius, maximum_ball_radius)
	    color = (random.random(), random.random(), random.random())
	    new_fires = Ball(x, y, dx, dy,color,15, False)
	    new_fires.shape("fire.gif")
	    FIRES.append(new_fires)



	#def move_all_KEYS():
	    #for b in KEYS:
	      #  b.move(screen_width, screen_height)

	def collide(my_ball, ball_b):
	    if my_ball == ball_b:
	        return False

	    distance = math.sqrt(math.pow(my_ball.xcor() - ball_b.xcor(), 2) + math.pow(my_ball.ycor() - ball_b.ycor(), 2))
	    if my_ball.r + ball_b.r >= distance:
	        return True

	    else:
	        return False

	def col_with_door(my_ball, Door):
	    if my_ball == Door:
	        return False
	    distance = math.sqrt(math.pow(my_ball.xcor() - Door.xcor(), 2) + math.pow(my_ball.ycor() - Door.ycor(), 2))
	    if distance <= 30:
	        return True
	    else:
	        return False
	#distance_ab = math.sqrt(math.pow(my_ball.xcor() - ball_b.xcor(), 2) + math.pow(my_ball.ycor() - ball_b.ycor(), 2))

	def check_all_KEYS_collision():
	    global running
	    all_KEYS = []
	    all_fires = []
	    # all_KEYS.append(my_ball)
	    
	    for ball in KEYS:
	        all_KEYS.append(ball)
	    for ball in FIRES:
	        all_KEYS.append(ball)
	    for ball_b in all_KEYS :
	        if (collide(my_ball, ball_b)):
	            r1 = my_ball.r
	            r2 = ball_b.r
	            if ball_b.CanBeEaten:
	                ball_b.ht()
	                KEYS.remove(ball_b)
	            if ball_b.CanBeEaten == False:
	                go.write("GAME OVER!!! TRY AGAIN IN A 1000 YEARS", align = "center", font = ("david", 25, "normal"))
	                time.sleep(5)
	                quit()
	    if col_with_door(my_ball, Door):
	     


	def level2 ():
		turtle.clearscreen()
		second_game()






	            # x = random.randint( -screen_width + maximum_ball_radius, screen_width - maximum_ball_radius)
	            # y = random.randint(-screen_height + maximum_ball_radius, screen_height - maximum_ball_radius)
	            # dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	            # dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	            # while (dx == 0 and dy ==0):
	            #     dx = random.randint(minimum_ball_dx, maximum_ball_dx)
	            #     dy = random.randint(minimum_ball_dy, maximum_ball_dy)
	            # r = random.randint(minimum_ball_radius, maximum_ball_radius)
	            # color = (random.random(), random.random(), random.random())
	            # if my_ball.CanBeEaten and ball_b.CanBeEaten:
	            #     if r1 > r2:
	            #         if my_ball == ball_b:
	            #             running = False
	            # if r2 > r1:
	            #     my_ball.new_Ball(x, y, dx, dy, r,color)
	            #     if my_ball == my_ball:
	            #         running = False  
	            #     if your_ball == my_ball:
	            #         running = False
	            #     if your_ball == ball_b:
	            #         your_ball.r = your_ball.r + 1
	            #         your_ball.shapesize(your_ball.r/10)


	def movearound():
	    x=turtle.getcanvas().winfo_pointerx() - screen_width*2

	    y = screen_height*1.5 - turtle.getcanvas().winfo_pointery()

	    my_ball.goto(x, y)

	                
	running = True 
	while running:
	    if len(KEYS) == 0:
	        Door.goto(350,350)
	        Door.showturtle()
	    screen_width = turtle.getcanvas().winfo_width()/2
	    screen_height = turtle.getcanvas().winfo_height()/2


	    movearound()
	    #move_all_KEYS()
	    # turtle.update()
	    # time.sleep(2)
	    check_all_KEYS_collision()

	    time.sleep(.1)

	    turtle.update()
    

