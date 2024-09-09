import pygame
import sys
import random

# Initialize PyGame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Chemical Tube Game')

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SPLASH_COLOR = (255, 0, 0)  # Splash color (lighter green)

# Tube dimensions
TUBE_WIDTH = 60
TUBE_HEIGHT = 400
TUBE_X = (WIDTH - TUBE_WIDTH) // 2
TUBE_Y = HEIGHT - TUBE_HEIGHT - 50

# Liquid properties
liquid_height = TUBE_HEIGHT
liquid_fall_speed = 10  # Increased fall speed
liquid_fall_interval = 5  # Faster fall interval
liquid_rise_speed = 5  # Small rise speed
fall_counter = 0

# Splash properties
splashes = []

# Font for text
font = pygame.font.Font(None, 36)

def create_splash(x, y):
    """Create a splash effect at the given coordinates."""
    splash_size = random.randint(5, 15)
    splash_speed = random.randint(1, 5)
    splashes.append((x, y, splash_size, splash_speed))

def update_splashes():
    """Update splash effects."""
    global splashes
    new_splashes = []
    for x, y, size, speed in splashes:
        new_size = size - speed
        if new_size > 0:
            new_splashes.append((x, y, new_size, speed))
    splashes = new_splashes

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # When any key is pressed, add a small amount of water
            if liquid_height < TUBE_HEIGHT:
                liquid_height = min(liquid_height + liquid_rise_speed, TUBE_HEIGHT)

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw the chemical tube
    pygame.draw.rect(screen, WHITE, (TUBE_X, TUBE_Y, TUBE_WIDTH, TUBE_HEIGHT), 2)

    # Handle liquid falling
    fall_counter += 1
    if fall_counter >= liquid_fall_interval:
        fall_counter = 0
        if liquid_height > 0:
            liquid_height -= liquid_fall_speed
        if liquid_height <= 0:
            liquid_height = 0  # Prevent the liquid height from going negative
            # Create splash effects when overflow occurs
            for _ in range(random.randint(5, 15)):
                splash_x = random.randint(TUBE_X, TUBE_X + TUBE_WIDTH)
                splash_y = HEIGHT - TUBE_Y // 4
                create_splash(splash_x, splash_y)

    # Determine the color of the liquid based on its height
    if liquid_height < (1 / 3) * TUBE_HEIGHT:
        liquid_color = RED
    elif liquid_height < (2 / 3) * TUBE_HEIGHT:
        liquid_color = YELLOW
    else:
        liquid_color = GREEN

    # Draw the liquid
    pygame.draw.rect(screen, liquid_color, (TUBE_X, TUBE_Y + TUBE_HEIGHT - liquid_height, TUBE_WIDTH, liquid_height))

    # Draw splashes
    update_splashes()
    for x, y, size, _ in splashes:
        pygame.draw.circle(screen, SPLASH_COLOR, (x, y), size)

    # Draw bottom alert message
    if liquid_height <= 0:
        bottom_text = font.render('Oh!', True, WHITE)
        screen.blit(bottom_text, (WIDTH // 2 - bottom_text.get_width() // 2, HEIGHT // 2 - bottom_text.get_height() // 2))

    # Update the display
    pygame.display.flip()

    # Frame rate
    pygame.time.Clock().tick(30)
