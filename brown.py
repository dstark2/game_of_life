import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
grid_size = 50  # Size of the grid
num_particles = 100  # Initial number of particles
num_iterations = 10000  # Number of iterations
diffusion_coefficient = 1.0  # Diffusion coefficient (controls step size)
collision_radius = 1.5  # Radius within which collisions are considered

# Initialize particles' positions
positions = np.random.randint(0, grid_size, (num_particles, 2))

# Function to update particle positions and handle collisions
def update_particles_and_handle_collisions(positions):
    # Calculate displacements
    std_dev = np.sqrt(2 * diffusion_coefficient)
    displacements = np.random.normal(loc=0.0, scale=std_dev, size=(positions.shape[0], 2))
    new_positions = positions + displacements

    # Ensure particles stay within grid boundaries
    new_positions = np.clip(new_positions, 0, grid_size - 1)

    # Detect collisions
    keep_particles = np.ones(len(new_positions), dtype=bool)
    for i in range(len(new_positions)):
        if not keep_particles[i]:
            continue
        for j in range(i + 1, len(new_positions)):
            if not keep_particles[j]:
                continue
            distance = np.linalg.norm(new_positions[i] - new_positions[j])
            if distance < collision_radius:
                keep_particles[i] = False
                keep_particles[j] = False
    
    # Keep only particles that did not collide
    return new_positions[keep_particles]

# Set up the figure and axis for plotting
fig, ax = plt.subplots()
scat = ax.scatter(positions[:, 0], positions[:, 1], c='blue', s=10)

# Initialize text element for metrics
metrics_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, fontsize=12,
                       verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

# Function to update the plot
def update(frame):
    global positions
    
    # Update positions and handle collisions
    positions = update_particles_and_handle_collisions(positions)
    
    # Update scatter plot
    scat.set_offsets(positions)
    
    # Calculate and print metrics
    num_remaining_particles = len(positions)
    metrics_text.set_text(f"Iteration: {frame}\nParticles Remaining: {num_remaining_particles}")
    
    # Set plot limits and title
    ax.set_xlim(0, grid_size)
    ax.set_ylim(0, grid_size)
    ax.set_aspect('equal')
    ax.set_title(f"Iteration {frame}")
    
    return scat, metrics_text

# Set up the animation
ani = animation.FuncAnimation(fig, update, frames=num_iterations, repeat=False, interval=50)

# Show the plot
plt.show()
