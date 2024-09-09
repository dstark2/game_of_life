import pygame
import random
import math

# Initialize PyGame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Fireworks Display')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

# Firework class
class Firework:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []
        self.color = random.choice(COLORS)
        self.exploded = False

    def explode(self):
        num_particles = random.randint(50, 100)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            dx = speed * math.cos(angle)
            dy = speed * math.sin(angle)
            self.particles.append([self.x, self.y, dx, dy, self.color])

    def update(self):
        if not self.exploded:
            self.explode()
            self.exploded = True
        for particle in self.particles:
            particle[0] += particle[2]  # Update x position
            particle[1] += particle[3]  # Update y position
            particle[3] += 0.1  # Simulate gravity (slowly downward)

    def draw(self):
        for particle in self.particles:
            pygame.draw.circle(screen, particle[4], (int(particle[0]), int(particle[1])), 3)

# Main loop
clock = pygame.time.Clock()
fireworks = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)

    # Create a new firework at random intervals
    if random.random() < 0.02:
        x = random.randint(100, WIDTH - 100)
        y = random.randint(100, HEIGHT // 2)
        fireworks.append(Firework(x, y))

    # Update and draw fireworks
    for firework in fireworks:
        firework.update()
        firework.draw()

    # Remove finished fireworks
    fireworks = [fw for fw in fireworks if any(p[1] < HEIGHT for p in fw.particles)]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
