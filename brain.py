import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
FPS = 10

# Colors
COLOR_ON = (255, 255, 255)
COLOR_OFF = (0, 0, 0)
COLOR_FLICKER = (128, 128, 128)

def initialize_grid():
    """Initialize the grid with random states."""
    return np.random.randint(0, 3, (GRID_WIDTH, GRID_HEIGHT))

def update_grid(grid):
    """Update the grid according to Brian's Brain rules."""
    new_grid = np.zeros_like(grid)
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            state = grid[x, y]
            neighbors = [grid[(x-1) % GRID_WIDTH, (y-1) % GRID_HEIGHT],
                         grid[(x) % GRID_WIDTH, (y-1) % GRID_HEIGHT],
                         grid[(x+1) % GRID_WIDTH, (y-1) % GRID_HEIGHT],
                         grid[(x-1) % GRID_WIDTH, (y) % GRID_HEIGHT],
                         grid[(x+1) % GRID_WIDTH, (y) % GRID_HEIGHT],
                         grid[(x-1) % GRID_WIDTH, (y+1) % GRID_HEIGHT],
                         grid[(x) % GRID_WIDTH, (y+1) % GRID_HEIGHT],
                         grid[(x+1) % GRID_WIDTH, (y+1) % GRID_HEIGHT]]
            
            count_on = np.sum([1 for n in neighbors if n == 1])
            
            if state == 1:  # On
                new_grid[x, y] = 2  # Flicker
            elif state == 2:  # Flicker
                new_grid[x, y] = 0  # Off
            else:  # Off
                if count_on == 2:
                    new_grid[x, y] = 1  # Turn on

    return new_grid

def draw_grid(screen, grid):
    """Draw the grid to the screen."""
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = COLOR_OFF
            if grid[x, y] == 1:
                color = COLOR_ON
            elif grid[x, y] == 2:
                color = COLOR_FLICKER

            pygame.draw.rect(screen, color,
                             pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def count_states(grid):
    """Count the number of cells in each state."""
    return np.bincount(grid.flatten(), minlength=3)

def average_active_neighbors(grid):
    """Compute the average number of active neighbors."""
    total_neighbors = 0
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            neighbors = [grid[(x-1) % GRID_WIDTH, (y-1) % GRID_HEIGHT],
                         grid[(x) % GRID_WIDTH, (y-1) % GRID_HEIGHT],
                         grid[(x+1) % GRID_WIDTH, (y-1) % GRID_HEIGHT],
                         grid[(x-1) % GRID_WIDTH, (y) % GRID_HEIGHT],
                         grid[(x+1) % GRID_WIDTH, (y) % GRID_HEIGHT],
                         grid[(x-1) % GRID_WIDTH, (y+1) % GRID_HEIGHT],
                         grid[(x) % GRID_WIDTH, (y+1) % GRID_HEIGHT],
                         grid[(x+1) % GRID_WIDTH, (y+1) % GRID_HEIGHT]]
            total_neighbors += np.sum([1 for n in neighbors if n == 1])
    return total_neighbors / (GRID_WIDTH * GRID_HEIGHT)

def entropy(grid):
    """Calculate the entropy of the grid."""
    values, counts = np.unique(grid, return_counts=True)
    probabilities = counts / counts.sum()
    return -np.sum(probabilities * np.log2(probabilities + np.finfo(float).eps))

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brian's Brain")
    clock = pygame.time.Clock()

    grid = initialize_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(COLOR_OFF)
        draw_grid(screen, grid)
        grid = update_grid(grid)

        # Metrics calculations
        state_counts = count_states(grid)
        total_cells = GRID_WIDTH * GRID_HEIGHT
        percentages = (state_counts / total_cells) * 100
        avg_neighbors = average_active_neighbors(grid)
        grid_entropy = entropy(grid)
        flickering_count = np.sum(grid == 2)

        # Print metrics
        print(f"On: {state_counts[1]}, Off: {state_counts[0]}, Flickering: {state_counts[2]}")
        print(f"Percentage On: {percentages[1]:.2f}%, Off: {percentages[0]:.2f}%, Flickering: {percentages[2]:.2f}%")
        print(f"Average Number of Active Neighbors: {avg_neighbors:.2f}")
        print(f"Grid Entropy: {grid_entropy:.2f}")
        print(f"Total Flickering Cells: {flickering_count}")
        print("-" * 40)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
