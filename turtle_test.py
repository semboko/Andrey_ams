import turtle
from random import randint

turtle.shape("circle")
turtle.shapesize(0.2)
turtle.color("red", "blue")
turtle.speed(0)


def draw_nshape(x, y, corners):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

    counter = 0
    turtle.begin_fill()
    while counter < corners:
        turtle.forward(100)
        turtle.left(360 / corners)
        counter += 1
    turtle.end_fill()


counter = 0
while counter < 5:
    random_x = randint(-400, 400)
    random_y = randint(-400, 400)
    draw_nshape(random_x, random_y, 5)
    counter += 1


turtle.mainloop()
