import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Constants
WINDOW_SIZE = 600
CUBE_SIZE = 3
FACE_SIZE = WINDOW_SIZE // CUBE_SIZE
FPS = 60

# Colors
COLORS = {
    'W': (255, 255, 255),  # White
    'R': (255, 0, 0),      # Red
    'B': (0, 0, 255),      # Blue
    'O': (255, 165, 0),    # Orange
    'G': (0, 255, 0),      # Green
    'Y': (255, 255, 0)     # Yellow
}

# Cube data structure
# A cube consists of 6 faces, each face is a 3x3 grid of colors
def initialize_cube():
    return {
        'U': np.full((CUBE_SIZE, CUBE_SIZE), 'W'),  # Up
        'D': np.full((CUBE_SIZE, CUBE_SIZE), 'Y'),  # Down
        'L': np.full((CUBE_SIZE, CUBE_SIZE), 'O'),  # Left
        'R': np.full((CUBE_SIZE, CUBE_SIZE), 'R'),  # Right
        'F': np.full((CUBE_SIZE, CUBE_SIZE), 'G'),  # Front
        'B': np.full((CUBE_SIZE, CUBE_SIZE), 'B')   # Back
    }

def draw_face(surface, face, position):
    x, y = position
    for i in range(CUBE_SIZE):
        for j in range(CUBE_SIZE):
            color = COLORS[face[i, j]]
            pygame.draw.rect(surface, color, pygame.Rect(x + j * FACE_SIZE, y + i * FACE_SIZE, FACE_SIZE, FACE_SIZE))

def draw_cube(surface, cube):
    positions = {
        'U': (1 * FACE_SIZE, 0 * FACE_SIZE),
        'D': (1 * FACE_SIZE, 2 * FACE_SIZE),
        'L': (0 * FACE_SIZE, 1 * FACE_SIZE),
        'R': (2 * FACE_SIZE, 1 * FACE_SIZE),
        'F': (1 * FACE_SIZE, 1 * FACE_SIZE),
        'B': (3 * FACE_SIZE, 1 * FACE_SIZE)
    }
    for face, pos in positions.items():
        draw_face(surface, cube[face], pos)

def main():
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
    pygame.display.set_caption('Rubik\'s Cube Simulator')
    clock = pygame.time.Clock()

    cube = initialize_cube()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((0, 0, 0))  # Clear screen with black
        draw_cube(screen, cube)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
