"""Geometric abstract art with stars, spirographs, and triangular spirals."""


__author__ = "730388033"


from turtle import colormode, Turtle, done, tracer, update
from random import randint
colormode(255)
star_pen: Turtle = Turtle()
triangle_pen: Turtle = Turtle()
square_pen: Turtle = Turtle()
spiral_pen: Turtle = Turtle()
MAX_SPEED: int = 0
side_length: float = 100.0


def draw_star() -> None:
    """Draws a simple star with random colours."""
    a: int = randint(0, 255)
    b: int = randint(0, 255)
    c: int = randint(0, 255)
    side: int = 25
    angle: int = 145
    star_pen.color(a, b, c)
    star_pen.speed(MAX_SPEED)
    star_pen.hideturtle()
    star_pen.begin_fill()
    i: int = 6
    while i > 0:
        star_pen.forward(side)
        star_pen.right(angle)
        i -= 1
    star_pen.end_fill()


# def draw_triangle() -> None:
#     """Draws a simple triangle with random colours."""
#     a: int = randint(0, 255)
#     b: int = randint(0, 255)
#     c: int = randint(0, 255)
#     triangle_pen.color(a, b, c)
#     triangle_pen.speed(MAX_SPEED)
#     triangle_pen.hideturtle()
#     triangle_pen.begin_fill()
#     i: int = 0
#     while i != 3:
#         triangle_pen.forward(side_length)
#         triangle_pen.right(120)
#         i += 1
#     triangle_pen.end_fill()


def draw_spirograph() -> None:
    """Draws a square circled about a point with random colours."""
    a: int = randint(0, 255)
    b: int = randint(0, 255)
    c: int = randint(0, 255)
    square_pen.color(a, b, c)
    square_pen.speed(MAX_SPEED)
    square_pen.hideturtle()
    # square_pen.begin_fill()
    i: int = 0
    # sides: int = 0
    # while i < 5:
    #     square_pen.left(12)
    #     while sides < 5:
    #         square_pen.forward(side_length)
    #         square_pen.right(90)
    #         sides += 1
    #     i += 1
    for i in range(100):
        square_pen.left(12)
        square_pen.forward(50)
        square_pen.left(90)
        square_pen.forward(50)
        square_pen.left(90)
        square_pen.forward(50)
        square_pen.left(90)
        square_pen.forward(50)
        square_pen.left(90)
    # square_pen.end_fill()


def draw_spiral() -> None:
    """Draws a triangular spiral."""
    a: int = randint(0, 255)
    b: int = randint(0, 255)
    c: int = randint(0, 255)
    i: int = 0
    side_length: float = 100.0
    spiral_pen.speed(MAX_SPEED)
    spiral_pen.hideturtle()
    spiral_pen.pencolor(a, b, c)
    while i < 150:
        spiral_pen.forward(side_length)
        spiral_pen.right(122.5)
        side_length *= 0.96
        i += 1


def number_star(a: int) -> None:
    """When given a number, the turtle will make the corresponding number of shapes at a random coordinate on plane."""
    wanted_shapes: int = 0
    while wanted_shapes < a:
        x: int = randint(-500, 500)
        y: int = randint(-500, 500)
        draw_star()
        star_pen.penup()
        star_pen.goto(x, y)
        star_pen.pendown()
        wanted_shapes += 1
    wanted_shapes = 0


# def number_triangle(b: int) -> None:
#     """When given a number, the turtle will make the corresponding number of shapes at a random coordinate on plane."""
#     wanted_shapes: int = 0
#     while wanted_shapes < b:
#         x: int = randint(-500, 500)
#         y: int = randint(-500, 500)
#         draw_triangle()
#         triangle_pen.penup()
#         triangle_pen.goto(x, y)
#         triangle_pen.pendown()
#         wanted_shapes += 1
#     wanted_shapes = 0


def number_spiro(c: int) -> None:
    """When given a number, the turtle will make the corresponding number of shapes at a random coordinate on plane."""
    wanted_shapes: int = 0
    while wanted_shapes < c:
        x: int = randint(-500, 500)
        y: int = randint(-500, 500)
        draw_spirograph()
        square_pen.penup()
        square_pen.goto(x, y)
        square_pen.pendown()
        wanted_shapes += 1
    wanted_shapes = 0


def number_spiral(d: int) -> None:
    """When given a number, the turtle will make the corresponding number of shapes at a random coordinate on plane."""
    wanted_shapes: int = 0
    while wanted_shapes < d:
        x: int = randint(-500, 500)
        y: int = randint(-500, 500)
        draw_spiral()
        spiral_pen.penup()
        spiral_pen.goto(x, y)
        spiral_pen.pendown()
        wanted_shapes += 1
    wanted_shapes = 0


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    a: int = 300
    # b: int = 50
    c: int = 45
    d: int = 15
    # a = int(input("Enter 1st number: "))
    # b = int(input("Enter 2nd number: "))
    # c = int(input("Enter 3rd number: "))
    # d = int(input("Enter 4th number: "))
    number_star(a)
    # number_triangle(b)
    number_spiro(c)
    number_spiral(d)
    update()
    done()


if __name__ == "__main__":
    main()