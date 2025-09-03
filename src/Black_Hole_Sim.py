import pygame
import pygame_widgets

def main() -> None:
    pygame.init()

    WIN = pygame.display.set_mode((800, 600))
    ICON = pygame.image.load("icon.png")
    
    pygame.display.set_caption("Black Hole Simulator")
    pygame.display.set_icon(ICON)
    
    clock = pygame.time.Clock()
    on = True
    FPS = 165
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
                break
            
        clock.tick(FPS)

if __name__ == "__main__":
    main()