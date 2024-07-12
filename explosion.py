import pygame

pygame.init()
main_surface = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

tile = pygame.image.load("./assets/Tile.png")


def crop_by_frame(n):
    col = n % 8
    row = n // 8
    return (col * 256, row * 256, 256, 256)


current_frame = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_frame = 0

    main_surface.fill((255, 255, 255))

    area = crop_by_frame(current_frame)
    main_surface.blit(tile, (0, 0), area)

    pygame.display.update()
    clock.tick()

    current_frame += 1
