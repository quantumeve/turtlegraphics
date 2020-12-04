import turtle

turtle.title("My Turtle Drawing")
turtle.bgcolor("blue")
turtle.setup(900, 900)
turtle.shape("turtle")

screen = turtle.Screen()

Impa = turtle.Turtle()

def triangle(length, color):
  Impa.fillcolor(color)
  Impa.begin_fill()

  x = 0
  while x < 3:
    Impa.forward(int(length))
    Impa.right(120)
    x = x + 1
  Impa.end_fill()

def circle(length, color):
  Impa.fillcolor(color)
  Impa.begin_fill()

  x = 0
  while x < 75:
    Impa.forward(10)
    Impa.right(5)
    x = x + 1
  Impa.end_fill()

def star(length, color):
  Impa.fillcolor(color)
  Impa.begin_fill()

  x = 0
  while x < 5:
    Impa.forward(int(length))
    Impa.right(145)
    x = x + 1
  Impa.end_fill()

input_shape = input("What shape do you want to draw? ")
input_length = input("How big do you want your shape? ")
input_color = input("What color would you like your shape? ")

if input_shape == 'triangle':
    triangle(input_length, input_color)
elif input_shape == 'circle':
    circle(input_length, input_color)
elif input_shape == 'star':
    star(input_length, input_color)

turtle.done()