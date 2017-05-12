import turtle

def draw_square(a_turtle):
	for i in range(1, 5):
		a_turtle.forward(100)
		a_turtle.right(90)
		
def draw_shape():
	window = turtle.Screen()
	window.bgcolor("blue")
	
	#Create first turtle - square
	s = turtle.Turtle()
	s.shape("turtle")
	s.color("green")
	s.speed(2)
	draw_square(s)
	
	#Create second turtle - circle
	c = turtle.Turtle()
	c.shape("arrow")
	c.color("yellow")
	c.circle(100)
	
	window.exitonclick()
	
draw_shape()