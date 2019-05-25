#turtle is a canvas in python for drawing using turtle commands
#import the module turtle to use it
import turtle

#create an instance wn to display a screen area for drawing
wn=turtle.Screen()
#create instance of the class Turtle from the module turtle- named hunter
hunter=turtle.Turtle()
#setting properties of the screen instance "wn" -background color as blue
wn.bgcolor("blue")
#setting color property of hunter as white 
hunter.color("white")
#creating another instance named beast
beast=turtle.Turtle()
#set color of beast to red
beast.color("red")
#shape property sets the shape of the pointer used for drawing in the numbered shapes provided by python such as turtle,circle,arrow
beast.shape("turtle")
#lifts the  pen(tail) of the turtle, thus preventing it from drawing on the screen 
hunter.up()
#two variables x an y set to different values
x=10
y=5
#for loop to keep printing for numbered times
for _ in range(50):
	#since the pen was lifted this would print the hunter once
	hunter.stamp()
	#moves the object ahead x distance
	beast.forward(x)
	#same
	hunter.forward(y)
	#turns 30 degree left
	beast.left(30)
	hunter.left(30)
	#lifts up the pen of beast
	beast.up()
	x+=1
	y+=1
	
wn.exitonclick()