import colorgram
import turtle
import random

## Process for obtaining colors used from the famous painting
# colors = colorgram.extract('image.jpg', 15)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

colours = [(30, 32, 166), (8, 15, 55), (65, 90, 227), (50, 93, 162), (100, 165, 218), (9, 27, 19), (195, 245, 221), (119, 186, 153), (37, 23, 9), (214, 235, 77), (46, 39, 237), (63, 114, 90), (178, 228, 247), (138, 226, 184), (122, 94, 46)]

turtle.colormode(255)
jacen = turtle.Turtle()
jacen.shape("turtle")
jacen.color("green")
jacen.speed("fastest")
jacen.hideturtle()
def paint():
    dots = 0
    while dots < 10:
        jacen.setheading(0)
        jacen.forward(20)
        jacen.dot(20, random.choice(colours))
        jacen.forward(20)
        dots +=1
def move():
    jacen.penup()
    jacen.setheading(225)
    jacen.forward(200)
    rows = 0
    while rows < 10:
        paint()
        jacen.right(180)
        jacen.forward(400)
        jacen.setheading(90)
        jacen.forward(40)
        rows += 1
move()

screen = turtle.Screen()
screen.exitonclick()