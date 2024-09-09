import pygame
import numpy as np
import random

# Constants
WIDTH, HEIGHT = 800, 600
SCALE = 10  # Scale for mapping the attractor coordinates
DOT_RADIUS = 5  # Radius of the dots
FPS = 60
FADE_AMOUNT = 5  # Amount of fading (number of frames)
COLOR_CHANGE_INTERVAL = 20  # Change color every 20 steps

# Lorenz system parameters
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lorenz Attractor with Periodic Color Change")
clock = pygame.time.Clock()

# Create a surface for fading effect
background = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)  # Use SRCALPHA for transparency

def lorenz_system(x, y, z, dt):
    dx = sigma * (y - x)
    dy = x * (rho - z) - y
    dz = x * y - beta * z
    x += dx * dt
    y += dy * dt
    z += dz * dt
    return x, y, z

def generate_random_color():
    """ Generate a random color. """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def draw_fading_trace(surface, x, y, radius, color, fade_amount):
    """ Draw fading traces with a given color and fade amount. """
    for i in range(fade_amount):
        alpha = int(255 * (1 - (i / fade_amount)))
        surface.set_alpha(alpha)
        pygame.draw.circle(surface, color, (x, y), radius - i)
    surface.set_alpha(255)  # Reset alpha after drawing

def main():
    running = True
    dt = 0.01
    x, y, z = 0.0, 1.0, 1.0
    step_count = 0
    color = generate_random_color()  # Initial color
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Compute new Lorenz system values
        x, y, z = lorenz_system(x, y, z, dt)
        
        # Map Lorenz system values to screen coordinates
        screen_x = WIDTH // 2 + int(x * SCALE)
        screen_y = HEIGHT // 2 - int(y * SCALE)

        # Draw fading traces on the background surface
        draw_fading_trace(background, screen_x, screen_y, DOT_RADIUS, color, FADE_AMOUNT)
        
        # Update the screen
        screen.blit(background, (0, 0))
        pygame.display.flip()
        screen.fill((0, 0, 0))  # Clear screen for next frame
        
        # Increment the step counter
        step_count += 1
        
        # Change color every COLOR_CHANGE_INTERVAL steps
        if step_count % COLOR_CHANGE_INTERVAL == 0:
            color = generate_random_color()
        
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
