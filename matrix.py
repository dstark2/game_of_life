import pygame
import random

# Initialize PyGame
pygame.init()

# Define constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)  # Black background
TEXT_COLOR = (0, 255, 0)  # Green text
FONT_SIZE = 20
NUM_COLUMNS = WIDTH // FONT_SIZE
NUM_ROWS = HEIGHT // FONT_SIZE
FPS = 30

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Matrix Green Screen")

# Set up font
font = pygame.font.Font(None, FONT_SIZE)

# Define a function to create random characters
def get_random_char():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]{};:,./<>?`~"
    return random.choice(chars)

# Main loop
clock = pygame.time.Clock()
running = True

# Initialize columns with random characters
matrix_columns = [[get_random_char() for _ in range(NUM_ROWS)] for _ in range(NUM_COLUMNS)]

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with background color
    screen.fill(BACKGROUND_COLOR)

    # Draw the matrix effect
    for x in range(NUM_COLUMNS):
        for y in range(NUM_ROWS):
            char = matrix_columns[x][y]
            text_surface = font.render(char, True, TEXT_COLOR)
            screen.blit(text_surface, (x * FONT_SIZE, y * FONT_SIZE))
            # Move characters down
            if random.random() < 0.1:  # Adjust the speed here
                matrix_columns[x][y] = get_random_char()
    
    # Update the display
    pygame.display.flip()
    
    # Cap the frame rate
    clock.tick(FPS)

pygame.quit()
