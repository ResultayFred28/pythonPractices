import turtle
import colorsys

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.width(2)

h = 0

for i in range(120):
  color = colorsys.hsv_to_rgb(h, 1, 1)
  t.pencolor(color)

  for _ in range(5):
    t.forward(i*2)
    t.right(144)

  t.right(8)
  h += 1/120

t.hideturtle()
turtle.done()