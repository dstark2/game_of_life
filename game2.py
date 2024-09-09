import pygame
import numpy as np
import time

# Define the dimensions of the grid and colors
GRID_SIZE = 50
CELL_SIZE = 10
WINDOW_SIZE = GRID_SIZE * CELL_SIZE

# Define colors
BACKGROUND_COLOR = (30, 30, 60)  # Dark blue
CELL_COLOR_ALIVE = (100, 150, 255)  # Light blue
CELL_COLOR_DEAD = (30, 30, 60)     # Same as background for dead cells
GRID_COLOR = (80, 80, 120)         # Subtle grid color

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Conway's Game of Life")

def initialize_grid(size, prob_alive):
    """
    Initialize the grid with random alive or dead cells.
    
    Parameters:
        size (int): The size of the grid (size x size).
        prob_alive (float): The probability of a cell being alive initially.

    Returns:
        numpy.ndarray: A 2D array representing the initial state of the grid.
    """
    grid = np.random.choice([0, 1], size*size, p=[1-prob_alive, prob_alive]).reshape(size, size)
    return grid

def update_grid(grid):
    """
    Compute the next generation of the grid based on Conway's Game of Life rules.
    
    Parameters:
        grid (numpy.ndarray): The current state of the grid.

    Returns:
        numpy.ndarray: The next state of the grid.
    """
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            # Count the number of live neighbors
            total = (grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                     grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                     grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                     grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE])

            # Apply Conway's rules
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1

    return new_grid

def draw_grid(grid, screen):
    """
    Draw the grid and cells on the screen.

    Parameters:
        grid (numpy.ndarray): The current state of the grid.
        screen (pygame.Surface): The surface to draw on.
    """
    screen.fill(BACKGROUND_COLOR)
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            color = CELL_COLOR_ALIVE if grid[i, j] == 1 else CELL_COLOR_DEAD
            pygame.draw.rect(screen, color, pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE))
    
    # Draw grid lines
    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, WINDOW_SIZE), 1)
    for y in range(0, WINDOW_SIZE, CELL_SIZE):
        pygame.draw.line(screen, GRID_COLOR, (0, y), (WINDOW_SIZE, y), 1)
    
    pygame.display.flip()

def main():
    """
    Main function to run the Conway's Game of Life simulation.
    """
    prob_alive = 0.2
    generations = 10000
    grid = initialize_grid(GRID_SIZE, prob_alive)

    clock = pygame.time.Clock()
    running = True

    # Countdown before starting
    font = pygame.font.SysFont(None, 55)
    for i in range(10, 0, -1):
        screen.fill(BACKGROUND_COLOR)
        text = font.render(f'Starting in {i} seconds...', True, GRID_COLOR)
        screen.blit(text, (WINDOW_SIZE // 4, WINDOW_SIZE // 2))
        pygame.display.flip()
        pygame.time.wait(1000)

    # Start simulation
    stable_generation = None
    generation_count = 0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        grid = update_grid(grid)
        draw_grid(grid, screen)
        generation_count += 1

        if stable_generation is None and np.array_equal(grid, initialize_grid(GRID_SIZE, prob_alive)):
            stable_generation = generation_count
            print(f'Stable state reached at generation {stable_generation}.')
        
        clock.tick(10)  # Adjust frame rate for smoother transitions

    pygame.quit()

if __name__ == "__main__":
    main()
