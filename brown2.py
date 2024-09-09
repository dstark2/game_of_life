import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Parameters
grid_size = 500  # Size of the grid in pixels
num_particles = 100  # Number of particles
num_iterations = 10000  # Number of iterations
diffusion_coefficient = 1.0  # Diffusion coefficient (controls step size)
collision_radius = 5  # Radius within which collisions are considered
trace_length = 30  # Number of frames to keep trace

# Initialize display
screen = pygame.display.set_mode((grid_size, grid_size))
pygame.display.set_caption("Brownian Motion with Collisions")

# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Particle class
class Particle:
    def __init__(self, x, y):
        self.positions = [(x, y)]
        self.color = BLUE

    def move(self, displacement):
        new_x = np.clip(self.positions[-1][0] + displacement[0], 0, grid_size - 1)
        new_y = np.clip(self.positions[-1][1] + displacement[1], 0, grid_size - 1)
        self.positions.append((new_x, new_y))
        if len(self.positions) > trace_length:
            self.positions.pop(0)
    
    def draw(self, surface):
        for i in range(len(self.positions) - 1):
            pygame.draw.line(surface, self.color, self.positions[i], self.positions[i + 1], 2)

# Initialize particles
particles = [Particle(np.random.randint(0, grid_size), np.random.randint(0, grid_size)) for _ in range(num_particles)]

# Function to update particles and handle collisions
def update_particles(particles):
    std_dev = np.sqrt(2 * diffusion_coefficient)
    
    for i, p1 in enumerate(particles):
        displacement = np.random.normal(loc=0.0, scale=std_dev, size=2)
        p1.move(displacement)
    
    # Detect collisions
    to_remove = set()
    for i in range(len(particles)):
        if i in to_remove:
            continue
        for j in range(i + 1, len(particles)):
            if j in to_remove:
                continue
            distance = np.linalg.norm(np.array(particles[i].positions[-1]) - np.array(particles[j].positions[-1]))
            if distance < collision_radius:
                to_remove.add(i)
                to_remove.add(j)
                particles[i].color = RED
                particles[j].color = RED
    
    # Remove collided particles
    return [p for idx, p in enumerate(particles) if idx not in to_remove]

# Main loop
running = True
clock = pygame.time.Clock()
iteration = 0

while running and iteration < num_iterations:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Update particles
    particles = update_particles(particles)
    
    # Clear screen
    screen.fill(BLACK)
    
    # Draw particles
    for particle in particles:
        particle.draw(screen)
    
    # Display metrics
    font = pygame.font.SysFont(None, 36)
    text = font.render(f"Iteration: {iteration} | Particles Remaining: {len(particles)}", True, WHITE)
    screen.blit(text, (10, 10))
    
    # Update display
    pygame.display.flip()
    
    # Frame rate
    clock.tick(30)
    
    iteration += 1

pygame.quit()
