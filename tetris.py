import pygame
from random import choice

pygame.init()
main_surface = pygame.display.set_mode((700, 670))
clock = pygame.time.Clock()


info_font = pygame.font.Font("./assets/pixelify.ttf", 40)
game_over_img = pygame.image.load("assets/game_over.png")


lshape = (
    (1, 0),
    (1, 0),
    (1, 1),
)

oshape = (
    (2, 2),
    (2, 2),
)

zshape = (
    (3, 3, 0),
    (0, 3, 3),
)

jshape = (
    (0, 4),
    (0, 4),
    (4, 4),
)

ishape = (
    (5, ),
    (5, ),
    (5, ),
    (5, ),
)

sshape = (
    (0, 6, 6),
    (6, 6, 0),
)

tshape = (
    (0, 7, 0),
    (7, 7, 7),
)

pallete = {
    1: (252, 186, 3),
    2: (235, 64, 52),
    3: (195, 69, 237),
    4: (224, 123, 57),
    5: (68, 188, 216),
    6: (245, 66, 215),
    7: (209, 245, 66),
}


all_shapes = lshape, oshape, zshape, jshape, ishape, sshape, tshape

score = 0

board = []
for i in range(20):
    row = []
    for j in range(10):
        row.append(0)
    board.append(row)


current_shape = choice(all_shapes)
new_shape = choice(all_shapes)
current_shape_pos = [4, 0]
frame_counter = 0
game_over = False

window_height = main_surface.get_height()
game_surface_height = window_height - 20
game_surface = pygame.Surface((game_surface_height/2, game_surface_height))
cell_size = game_surface_height / 20

info_surface = pygame.Surface((300, 200))
new_shape_surface = pygame.Surface((300, 200))


def draw_matrix(matrix, offset, target_surface=game_surface):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            value = matrix[i][j]
            if value == 0:
                continue
            x = (j + offset[0]) * cell_size + 2
            y = (i + offset[1]) * cell_size + 2
            pygame.draw.rect(target_surface, pallete[value], (x, y, cell_size - 4, cell_size - 4))


def transfer_values(dest_matrix, source_matrix, pos):
    for i in range(len(source_matrix)):
        for j in range(len(source_matrix[0])):
            value = source_matrix[i][j]
            if value == 0:
                continue
            x = pos[0] + j
            y = pos[1] + i
            dest_matrix[y][x] = value


def is_valid_pos(pos=None, shape=None):
    if pos is None:
        pos = current_shape_pos
    if shape is None:
        shape = current_shape

    if pos[0] < 0:
        return False

    if pos[0] > 10 - len(shape[0]):
        return False

    if pos[1] > 20 - len(shape):
        return False

    for i in range(len(shape)):
        for j in range(len(shape[0])):
            value = shape[i][j]
            if value == 0:
                continue
            board_j = pos[0] + j
            board_i = pos[1] + i
            if board[board_i][board_j] != 0:
                return False

    return True


def rotate_shape(source):
    result = []
    for j in range(len(source[0])):
        row = []
        for i in range(len(source) - 1, -1, -1):
            row.append(source[i][j])
        result.append(tuple(row))
    return tuple(result)


def get_hard_drop_position():
    y = current_shape_pos[1]
    while is_valid_pos(pos=(current_shape_pos[0], y + 1)):
        y += 1
    return [current_shape_pos[0], y]


def draw_info():
    score_img = info_font.render(f"Score: {score}", True, (255, 255, 255))
    info_surface.blit(score_img, (10, 10))


def remove_lines():
    global score
    counter = 0
    for line in board:
        if 0 not in line:
            board.remove(line)
            board.insert(0, [0] * 10)
            counter += 1
    score += (0, 100, 300, 550, 800)[counter]


def draw_new_shape():
    shape_width = len(new_shape[0])
    shape_height = len(new_shape)
    offset_x = new_shape_surface.get_width() / 2 / cell_size - shape_width/2
    offset_y = new_shape_surface.get_height() / 2 / cell_size - shape_height/2
    draw_matrix(new_shape, (offset_x, offset_y), new_shape_surface)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_a:
                next_pos = [current_shape_pos[0] - 1, current_shape_pos[1]]
                if is_valid_pos(next_pos):
                    current_shape_pos = next_pos
            if event.key == pygame.K_d:
                next_pos = [current_shape_pos[0] + 1, current_shape_pos[1]]
                if is_valid_pos(next_pos):
                    current_shape_pos = next_pos
            if event.key == pygame.K_w:
                next_shape = rotate_shape(current_shape)
                if is_valid_pos(shape=next_shape):
                    current_shape = next_shape
            if event.key == pygame.K_SPACE:
                current_shape_pos = get_hard_drop_position()

    main_surface.fill((255, 255, 255))
    game_surface.fill((0, 0, 0))
    info_surface.fill((0, 0, 0))
    new_shape_surface.fill((0, 0, 0))
    draw_matrix(board, (0, 0))
    draw_matrix(current_shape, current_shape_pos)
    draw_info()
    draw_new_shape()
    main_surface.blit(game_surface, (10, 10))
    main_surface.blit(info_surface, (350, 10))
    main_surface.blit(new_shape_surface, (350, 220))

    if game_over:
        main_surface.blit(game_over_img, (0, 0))

    pygame.display.update()

    if frame_counter == 40 and not game_over:
        next_pos = [current_shape_pos[0], current_shape_pos[1] + 1]
        if is_valid_pos(next_pos):
            current_shape_pos = next_pos
        else:
            transfer_values(board, current_shape, current_shape_pos)
            current_shape_pos = [4, 0]
            current_shape = new_shape
            if not is_valid_pos([4, 0], new_shape):
                game_over = True
            new_shape = choice(all_shapes)
        frame_counter = 0
        remove_lines()
    frame_counter += 1

    clock.tick()
