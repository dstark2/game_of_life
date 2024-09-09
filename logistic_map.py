import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
SCALE = 500
DOT_RADIUS = 2
FPS = 60

# Logistic Map parameters
r = 3.9  # Growth rate parameter
x0 = 0.5  # Initial value

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Logistic Map")
clock = pygame.time.Clock()

def logistic_map(x, r):
    return r * x * (1 - x)

def main():
    running = True
    x = x0
    prev_pos = (0, HEIGHT // 2)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute the next value in the logistic map
        x = logistic_map(x, r)
        
        # Map Logistic Map values to screen coordinates
        screen_x = int(WIDTH * np.random.rand())
        screen_y = HEIGHT // 2 - int(x * SCALE)  # Flip and scale to fit the screen

        # Draw a white circle (dot) at the current position
        pygame.draw.circle(screen, (255, 255, 255), (screen_x, screen_y), DOT_RADIUS)
        
        # Refresh the display
        pygame.display.flip()
        screen.fill((0, 0, 0))  # Clear screen
        
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
