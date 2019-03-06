import turtle
import time
from turtle import Screen
from turtle import *
#from agariogame import*
from trying2 import*


turtle.setup(width = 1920 , height = 1080)

#turtle.setup(width = 1920, height = 1080)
story = turtle.Turtle()
story1 = turtle.Turtle()
story2 = turtle.Turtle()
story3 = turtle.Turtle()
story4 = turtle.Turtle()


#turtle.hideturtle()

def Story():
	#this function writs the story on the first page.
	global story, story1, story2, story3, story4
	story.hideturtle()
	story.penup()
	story.left(90)
	story.forward(400)
	story.pendown()
	story.write("You suddenly died, and you went to hell." , align = "center" , font = ("david" , 30, "normal"))
	story.hideturtle()
	story1.left(90)
	story1.penup()
	story1.forward(300)
	story1.pendown()
	story1.write("You have been there for a thousand centuries," , align = "center" , font = ("david" , 30, "normal"))
	story1.hideturtle()
	story2.left(90)
	story2.penup()
	story2.forward(200)
	story2.pendown()
	story2.write("You have struggled, and you've had enough." , align = "center" , font = ("david" , 30, "normal"))
	story2.hideturtle()
	story3.left(90)
	story3.penup()
	story3.forward(100)
	story3.pendown()
	story3.write("So you decided to take the long, menacing way to heaven." , align = "center" , font = ("david" , 30, "normal"))
	story3.hideturtle()
	story4.write("Your journey begins here, SINNER!" , align = "center" , font = ("david" , 30, "normal"))
	story4.hideturtle()




# ghost = turtle.Turtle()
# # ghost.shape("circle")

# turtle.register_shape("small_ghost.gif")
# ghost.shape("small_ghost.gif")


# ghost.penup()
# ghost.hideturtle()
# def arrow_keys_moving():
# 	setup(500, 500)
# 	Screen()
# 	title("Turtle Keys")

# 	def k1():
# 	    ghost.forward(10)

# 	def k2():
# 	    ghost.left(90)

# 	def k3():
# 	    ghost.right(90)


# 	onkey(k1, "Up")
# 	onkey(k2, "Left")
# 	onkey(k3, "Right")





turtle.bgpic("heavenxhell.png")

play = turtle.Turtle()

def level1(x,y):
	#this function is the first level so its whats going to delete everything from the first page and make the game appear. 
	story.clear()
	story1.clear()
	story2.clear()
	story3.clear()
	story4.clear()
	play.hideturtle()
	turtle.bgpic("hellbg.png")
	first_game()
	# ghost.goto(0,300)
	# ghost.showturtle()
	#GHOST()




def play_button():
	turtle.register_shape("1play_button.gif")
	play.shape("1play_button.gif")
	play.penup()
	play.goto(0,-100)
	play.onclick(level1)




#print (play.pos())
Story()
play_button()
#level1(0,0)
#arrow_keys_moving()
turtle.listen()
turtle.mainloop()
