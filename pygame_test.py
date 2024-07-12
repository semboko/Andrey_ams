import pygame


pygame.init()

window_size = (500, 500)
main_surface = pygame.display.set_mode(window_size)
clock = pygame.time.Clock()

x = 250
y = 250

target_x, target_y = 250, 250

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                y -= 30
            if event.key == pygame.K_s:
                y += 30
            if event.key == pygame.K_a:
                x -= 30
            if event.key == pygame.K_d:
                x += 30
        if event.type == pygame.MOUSEMOTION:
            target_x, target_y = event.pos

    main_surface.fill("white")
    pygame.draw.circle(main_surface, "red", (x, y), 50)
    pygame.draw.circle(main_surface, "red", (target_x, target_y), 25, 1)
    pygame.draw.line(main_surface, "black", (x, y), (target_x, target_y))
    y = y + 1

    pygame.display.update()
    clock.tick(60)
