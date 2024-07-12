import pygame
from random import randint

pygame.init()
main_surface = pygame.display.set_mode((480, 640))
clock = pygame.time.Clock()


# Section 1: Loading Assets
bg = pygame.image.load("./assets/Background.png")
terrain = pygame.image.load("./assets/Terrain.png")
flappy = pygame.image.load("./assets/emblem_256.png")
flappy = pygame.transform.scale(flappy, (60, 60))
pipe1 = pygame.image.load("./assets/Pipe.png")
pipe2 = pygame.transform.flip(pipe1, flip_x=False, flip_y=True)
score_font = pygame.font.Font("./assets/pixelify.ttf", 55)

game_over_surface = pygame.Surface((480, 200), pygame.SRCALPHA)
game_over_surface.fill((0, 0, 0, 100))
game_img = score_font.render("GAME", True, (255, 255, 255))
over_img = score_font.render("OVER", True, (255, 255, 255))
game_over_surface.blit(game_img, (240 - game_img.get_width()/2, 0))
game_over_surface.blit(over_img, (240 - over_img.get_width()/2, 50))


# Section 2: Game Variables
terrain_x = 0
flappy_y = 260
flappy_y_vel = 0
pipe_coordinates = []
frame_counter = 160
score = 0
game_over = False


# Section 3: Utility Functions
def draw_pipes(pos, gap):
    x = pos[0] - pipe1.get_width() / 2
    y1 = pos[1] - gap/2 - pipe1.get_height()
    y2 = pos[1] + gap/2
    main_surface.blit(pipe1, (x, y1))
    main_surface.blit(pipe2, (x, y2))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            flappy_y_vel = -8
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_over:
                game_over = False
                flappy_y = 260
                pipe_coordinates = []
                score = 0
                terrain_x = 0
                flappy_y_vel = 0
                frame_counter = 160

    main_surface.blit(bg, (0, 0))
    terrain1_hitbox = main_surface.blit(terrain, (terrain_x, 565))
    terrain2_hitbox = main_surface.blit(terrain, (terrain_x + 480, 565))

    angle = 15
    if flappy_y_vel > 0:
        angle = -flappy_y_vel * 10
    if angle < -90:
        angle = -90
    rotated_flappy = pygame.transform.rotate(flappy, angle)
    dest = rotated_flappy.get_rect(center=(240, flappy_y))
    flappy_hitbox = main_surface.blit(rotated_flappy, dest)

    if flappy_hitbox.colliderect(terrain1_hitbox):
        game_over = True

    if flappy_hitbox.colliderect(terrain2_hitbox):
        game_over = True

    if not game_over:
        terrain_x -= 2
        flappy_y += flappy_y_vel
        flappy_y_vel += 0.28

    if terrain_x <= -480:
        terrain_x = 0

    frame_counter -= 1
    if frame_counter == 0:
        frame_counter = 160
        pipe_coordinates.append([520, randint(150, 415)])

    for coord in pipe_coordinates:
        draw_pipes(coord, 200)
        if not game_over:
            coord[0] -= 2
        if coord[0] < -50:
            pipe_coordinates.remove(coord)
        if coord[0] == 212:
            score += 1

    score_img = score_font.render(str(score), True, (255, 255, 255))
    main_surface.blit(score_img, (240 - score_img.get_width() / 2, 100))

    if game_over:
        main_surface.blit(game_over_surface, (0, 200))
    pygame.display.update()
    clock.tick(60)
