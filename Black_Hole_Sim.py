import pygame
import pygame_widgets

pygame.init()

WIN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Black Hole Simulator")

clock = pygame.time.Clock()
on = True
FPS = 165

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            on = False
            break

    print("askdasd")
    clock.tick(FPS)