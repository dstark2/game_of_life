import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Natural Rain Effect")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Raindrop properties
NUM_RAINDROPS = 100
RAINDROP_WIDTH = 2
RAINDROP_HEIGHT = 10

# Raindrop class
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(5, 15)
    
    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-20, -1)
            self.x = random.randint(0, WIDTH)
            self.speed = random.randint(5, 15)

    def draw(self, surface):
        pygame.draw.line(surface, WHITE, (self.x, self.y), (self.x, self.y + RAINDROP_HEIGHT), RAINDROP_WIDTH)

def main():
    clock = pygame.time.Clock()
    raindrops = [Raindrop() for _ in range(NUM_RAINDROPS)]
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(BLACK)
        
        for raindrop in raindrops:
            raindrop.fall()
            raindrop.draw(screen)
        
        pygame.display.flip()
        clock.tick(60)  # Frame rate

    pygame.quit()

if __name__ == "__main__":
    main()
