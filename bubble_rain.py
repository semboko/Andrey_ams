import pygame
from random import randint

from dataclasses import dataclass


pygame.init()

pop_sound = pygame.mixer.Sound("./assets/pop.ogg")

bomb_img = pygame.image.load("./assets/bomb.png")
bomb_img = pygame.transform.scale(bomb_img, (60, 60))

medium_font = pygame.font.SysFont("Arial", 28, True)


balloon_images = []
balloon_colors = ("black", "green", "red", "blue")

for color_name in balloon_colors:
    img = pygame.image.load("./assets/balloon_" + color_name + ".png")
    img = pygame.transform.scale(img, (60, 72))
    balloon_images.append(img)


@dataclass
class Bubble:
    x: int
    y: int
    color: int


@dataclass
class ScoreEvent:
    x: int
    y: int
    img: pygame.Surface
    frames: int


def draw_bubble(surface: pygame.Surface, bubble: Bubble):
    img = balloon_images[bubble.color]
    surface.blit(img, (bubble.x, bubble.y))


def create_bubble():
    x = randint(0, 640)
    y = randint(-400, -50)
    color = randint(0, 3)
    return Bubble(x, y, color)


main_surface = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()

bubbles = []
i = 0
while i < 10:
    bubbles.append(create_bubble())
    i += 1

score = 0
score_events = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for b in bubbles:
                brect = pygame.Rect((b.x, b.y), (60, 72))
                if brect.collidepoint(event.pos):
                    bubbles.remove(b)
                    pop_sound.play()
                    score += 2
                    event_img = medium_font.render("+2", True, (0, 255, 0))
                    score_events.append(ScoreEvent(event.pos[0], event.pos[1], event_img, 120))

    main_surface.fill("#abcbff")
    for b in bubbles:
        draw_bubble(main_surface, b)
        b.y += 2
        if b.y > 470:
            score -= 10
            event_img = medium_font.render("-10", True, (255, 0, 0))
            score_events.append(ScoreEvent(b.x, b.y, event_img, 120))
            bubbles.remove(b)

    if randint(0, 59) == 0:
        bubbles.append(create_bubble())

    if randint(0, 119) == 0:
        pass

    score_img = medium_font.render("Score: " + str(score), True, (0, 0, 0))
    main_surface.blit(score_img, (10, 10))

    for e in score_events:
        main_surface.blit(e.img, (e.x, e.y))
        e.y -= 1
        e.frames -= 1
        if e.frames <= 0:
            score_events.remove(e)

    pygame.display.update()
    clock.tick(60)
