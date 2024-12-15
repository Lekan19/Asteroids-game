import pygame
from constants import *

def main():
    pygame.init()
    isInit = pygame.get_init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True

    while running:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with black
        screen.fill((0, 0, 0)) 
        # pygame.time.wait(2000)
        
        print(f"Is pygame initialized: {isInit}")
        print("Starting Asteroid Game")
        print (f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        pygame.display.flip()

if __name__ == "__main__":
    main()