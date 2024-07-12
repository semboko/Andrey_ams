import turtle as t
from itertools import pairwise


corners = (
    (-200, -5),
    (-100, -5),
    (-100, -100),
    (30, -100),
    (30, -10),
    (35, -10),
    (35, -100),
    (200, -100),
    (200, 5),
    (100, 5),
    (100, 100),
    (35, 100),
    (35, 10),
    (30, 10),
    (30, 100),
    (-200, 100),
)
STEP_SIZE = 10
VISITED = set()


wall_drawer = t.Turtle()
wall_drawer.speed(0)
wall_drawer.hideturtle()

robot = t.Turtle()


def draw_walls():
    wall_drawer.penup()
    wall_drawer.goto(corners[0])
    wall_drawer.pendown()
    for coord in corners[1:]:
        wall_drawer.goto(coord)
    wall_drawer.goto(corners[0])


def is_outside(x, y):
    xs, ys = [], []
    for c in corners:
        xs.append(c[0])
        ys.append(c[1])

    if x > max(xs):
        return True
    if x < min(xs):
        return True
    if y > max(ys):
        return True
    if y < min(ys):
        return True

    return False


# def orientation(p, q, r):
#     dx1 = q[0] - p[0]
#     dy1 = q[1] - p[1]
#     slope1 = dy1 / (dx1 + 0.00000000000000000001)
#     dx2 = r[0] - q[0]
#     dy2 = r[1] - q[1]
#     slope2 = dy2 / (dx2 + 0.00000000000000000001)

#     if slope2 > slope1:
#         return -1
#     if slope2 < slope1:
#         return 1
#     return 0


def orientation(p, q, r):
    px, py = p
    qx, qy = q
    rx, ry = r

    ratio_diff = (qy - py) * (rx - qx) - (ry - qy) * (qx - px)

    if ratio_diff < 0:
        return -1
    if ratio_diff > 0:
        return 1
    return 0


def intersect(r1, r2, c1, c2):
    case1 = orientation(r1, r2, c1) != orientation(r1, r2, c2)
    case2 = orientation(c1, c2, r1) != orientation(c1, c2, r2)
    return case1 and case2


def is_outside2(r1, r2):
    for c1, c2 in pairwise(corners + (corners[0],)):
        if intersect(r1, r2, c1, c2):
            return True
    return False


def get_next_pos():
    pos = robot.position()
    angle = robot.heading()
    if angle == 0:
        return pos[0] + STEP_SIZE, pos[1]
    if angle == 90:
        return pos[0], pos[1] + STEP_SIZE
    if angle == 180:
        return pos[0] - STEP_SIZE, pos[1]
    if angle == 270:
        return pos[0], pos[1] - STEP_SIZE


def clean():
    robot.color("blue")
    robot.penup()
    while True:
        pos = get_next_pos()
        if is_outside(pos[0], pos[1]) or pos in VISITED:
            robot.right(90)
        robot.dot(7)
        robot.forward(STEP_SIZE)
        VISITED.add(pos)


def clean2():
    robot.penup()
    robot.speed(0)
    stack = [(0, 0)]
    while len(stack) > 0:
        next_pos = stack.pop()

        angle = robot.towards(next_pos)
        robot.setheading(angle)
        robot.goto(next_pos)

        robot.dot(7)
        VISITED.add(next_pos)
        x, y = next_pos
        neighbors = (
            (x, y + 10),
            (x - 10, y),
            (x, y - 10),
            (x + 10, y),
        )
        for nghbr in neighbors:
            if not is_outside2(next_pos, nghbr) and nghbr not in VISITED and nghbr not in stack:
                stack.append(nghbr)


draw_walls()
clean2()
t.done()
