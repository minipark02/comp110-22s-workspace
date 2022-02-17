"""Setting up and doing Turtle."""


from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()

# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# leo.forward(300)
# leo.left(90)
# done()


# How to make a square using Turtle
# i: int = 0
# while (i < 4):
#     leo.forward(300)
#     leo.left(90)
#     i += 1

leo.penup()
leo.goto(-150, -100)  # Center of canvas
leo.pendown()


# Change the color of the pen and fill
leo.pencolor("blue")  # Just pen
leo.fillcolor(230, 164, 103)  # Just fill
leo.color(108, 189, 103)  # Both pen and fill


# Adjust speed of turtle
leo.speed(50)


# Hiding the turtle
leo.hideturtle()


# How to make a triangle and fill it with color
leo.begin_fill()
i: int = 0
side_length: float = 300.0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()


bob.pencolor(42, 74, 40)

bob.penup()
bob.goto(-150, -100)
bob.pendown()
bob.speed(100)

i = 0
while (i < 100):
    bob.forward(side_length)
    bob.left(122.5)
    side_length = side_length * 0.96
    i += 1


done()