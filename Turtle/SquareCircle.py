import turtle

def draw_square(a_turtle):
	for i in range(1,5):
		a_turtle.forward(100)
		a_turtle.right(90)
		
def draw_shape():
	window = turtle.Screen()
	window.bgcolor("blue")
	
	#Create turtle - Square
	square = turtle.Turtle()
	square.shape("turtle")
	square.color("green")
	square.speed(2)
	for i in range(1,37):
		draw_square(square)
		square.right(10)
		
	
	window.exitonclick()
	
draw_shape()