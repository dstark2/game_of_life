import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the dimensions of the grid
GRID_SIZE = 50

# Probability of a cell being alive initially
PROB_ALIVE = 0.2

# Number of generations to simulate
GENERATIONS = 1000

def initialize_grid(size, prob_alive):
    grid = np.random.choice([0, 1], size*size, p=[1-prob_alive, prob_alive]).reshape(size, size)
    return grid

def update_grid(grid):
    new_grid = grid.copy()
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            total = (grid[i, (j-1)%GRID_SIZE] + grid[i, (j+1)%GRID_SIZE] +
                     grid[(i-1)%GRID_SIZE, j] + grid[(i+1)%GRID_SIZE, j] +
                     grid[(i-1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i-1)%GRID_SIZE, (j+1)%GRID_SIZE] +
                     grid[(i+1)%GRID_SIZE, (j-1)%GRID_SIZE] + grid[(i+1)%GRID_SIZE, (j+1)%GRID_SIZE])

            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = -1  # Mark cells that are about to die
            else:
                if total == 3:
                    new_grid[i, j] = 2  # Mark cells that are about to be born

    new_grid[new_grid == -1] = 0  # Dead cells
    new_grid[new_grid == 2] = 1   # New born cells
    return new_grid

def run_simulation(grid_size, prob_alive, generations):
    grid = initialize_grid(grid_size, prob_alive)
    previous_grid = None  # To check for stability
    stable_generation = None  # To store the generation number when stability is reached

    fig, ax = plt.subplots(figsize=(10, 10))
    img = ax.imshow(grid, interpolation='nearest', cmap='viridis', vmin=-1, vmax=2)
    
    # Text objects for metrics
    generation_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, color='white', fontsize=14, fontweight='bold')
    alive_text = ax.text(0.02, 0.90, '', transform=ax.transAxes, color='white', fontsize=12)
    density_text = ax.text(0.02, 0.85, '', transform=ax.transAxes, color='white', fontsize=12)
    stability_text = ax.text(0.02, 0.80, '', transform=ax.transAxes, color='white', fontsize=12)

    def update(frame):
        nonlocal grid, previous_grid, stable_generation

        # Check for stability
        if previous_grid is not None and np.array_equal(grid, previous_grid):
            if stable_generation is None:
                stable_generation = frame
                print(f'Stable state reached at generation {stable_generation}.')
            stability_text.set_text('Stable: Yes')
        else:
            stability_text.set_text('Stable: No')

        # Stop incrementing the generation text once stability is reached
        if stable_generation is None:
            generation_text.set_text(f'Generation: {frame}')
        else:
            generation_text.set_text(f'Stable at Generation: {stable_generation}')

        previous_grid = grid.copy()
        grid = update_grid(grid)
        
        alive_count = np.sum(grid == 1)
        density = alive_count / grid.size

        img.set_data(grid)
        alive_text.set_text(f'Alive Cells: {alive_count}')
        density_text.set_text(f'Population Density: {density:.2f}')
        
        return img, generation_text, alive_text, density_text, stability_text

    ani = animation.FuncAnimation(fig, update, frames=generations, blit=True)
    plt.show()

if __name__ == "__main__":
    run_simulation(GRID_SIZE, PROB_ALIVE, GENERATIONS)
