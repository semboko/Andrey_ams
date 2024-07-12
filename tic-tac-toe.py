import turtle

SIZE = 200
TURN = True
LOCK = False
OCCUPIED_CELLS = dict()
GAME_OVER = False

turtle.speed(0)
turtle.width(10)


def draw_line(start_x, start_y, length):
    turtle.penup()
    turtle.goto(start_x, start_y)
    turtle.pendown()
    turtle.forward(length)


turtle.color("#b0b0b0")
draw_line(-1.5 * SIZE, 0.5 * SIZE, 3 * SIZE)
draw_line(-1.5 * SIZE, -0.5 * SIZE, 3 * SIZE)

turtle.right(90)

draw_line(-0.5 * SIZE, 1.5 * SIZE, 3 * SIZE)
draw_line(0.5 * SIZE, 1.5 * SIZE, 3 * SIZE)

turtle.left(90)


def draw_cross(x, y):
    turtle.color("#ff3b55")
    width = 0.8 * SIZE
    turtle.right(45)
    draw_line(x - width / 2, y + width / 2, 1.41 * width)
    turtle.right(90)
    draw_line(x + width / 2, y + width / 2, 1.41 * width)
    turtle.left(135)


def draw_circle(x, y):
    turtle.color("#5064fa")
    width = 0.8 * SIZE
    turtle.penup()
    turtle.goto(x, y - width / 2)
    turtle.pendown()
    turtle.circle(width / 2)


def is_outside(x, y):
    if x > 1.5 * SIZE:
        return True
    if x < -1.5 * SIZE:
        return True
    if y > 1.5 * SIZE:
        return True
    if y < -1.5 * SIZE:
        return True


def get_vertical(x):
    if x < -0.5 * SIZE:
        return -1
    if x > 0.5 * SIZE:
        return 1
    return 0


def get_horizontal(y):
    if y < -0.5 * SIZE:
        return -1
    if y > 0.5 * SIZE:
        return 1
    return 0


def detect_winner():

    global GAME_OVER

    row = -1
    while row <= 1:
        line = (
            OCCUPIED_CELLS.get((-1, row)),
            OCCUPIED_CELLS.get((0, row)),
            OCCUPIED_CELLS.get((1, row)),
        )

        if None not in line and line[0] == line[1] == line[2]:
            draw_line(-1.5 * SIZE, row * SIZE, 3 * SIZE)
            GAME_OVER = True
        row = row + 1

    col = -1
    while col <= 1:
        line = (
            OCCUPIED_CELLS.get((col, -1)),
            OCCUPIED_CELLS.get((col, 0)),
            OCCUPIED_CELLS.get((col, 1)),
        )

        if None not in line and line[0] == line[1] == line[2]:
            turtle.right(90)
            draw_line(col * SIZE, 1.5 * SIZE, 3 * SIZE)
            turtle.left(90)
            GAME_OVER = True
        col = col + 1

    left_diag = (OCCUPIED_CELLS.get((-1, 1)), OCCUPIED_CELLS.get((0, 0)), OCCUPIED_CELLS.get((1, -1)))

    if None not in left_diag and len(set(left_diag)) == 1:
        turtle.right(45)
        draw_line(-1.5 * SIZE, 1.5 * SIZE, 1.41 * 3 * SIZE)
        turtle.left(45)
        GAME_OVER = True

    right_diag = (
        OCCUPIED_CELLS.get((1, 1)),
        OCCUPIED_CELLS.get((0, 0)),
        OCCUPIED_CELLS.get((-1, -1)),
    )

    if None not in right_diag and len(set(right_diag)) == 1:
        turtle.right(135)
        draw_line(1.5 * SIZE, 1.5 * SIZE, 1.41 * 3 * SIZE)
        turtle.left(135)
        GAME_OVER = True


def click_handler(x, y):
    global TURN
    global LOCK

    if GAME_OVER is True:
        return
    if is_outside(x, y):
        return
    if LOCK is True:
        return

    v = get_vertical(x)
    h = get_horizontal(y)

    cell = (v, h)  # tuple of coordinates

    if cell in OCCUPIED_CELLS:
        return

    OCCUPIED_CELLS[cell] = TURN
    print(OCCUPIED_CELLS)

    LOCK = True
    if TURN is True:
        draw_cross(v * SIZE, h * SIZE)
    else:
        draw_circle(v * SIZE, h * SIZE)
    TURN = not TURN
    detect_winner()
    LOCK = False


turtle.onscreenclick(click_handler)
turtle.done()
