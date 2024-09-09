import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + 1j * Y
    output = np.zeros(C.shape, dtype=float)
    for i in range(width):
        for j in range(height):
            output[j, i] = mandelbrot(C[j, i], max_iter)
    return output

def plot_mandelbrot(output, xmin, xmax, ymin, ymax, iteration):
    plt.figure(figsize=(10, 10))
    plt.imshow(output, extent=(xmin, xmax, ymin, ymax), cmap='inferno', aspect='auto')
    plt.colorbar(label='Iterations')
    plt.title(f'Mandelbrot Set - Iteration {iteration}')
    plt.xlabel('Re')
    plt.ylabel('Im')
    plt.show()

def mandelbrot_growth_simulation(initial_xlim, initial_ylim, zoom_factor, num_iterations, width=800, height=800, max_iter=256):
    xmin, xmax = initial_xlim
    ymin, ymax = initial_ylim
    
    for iteration in range(num_iterations):
        print(f"Iteration {iteration + 1}")
        print(f"Current bounds: X: [{xmin}, {xmax}], Y: [{ymin}, {ymax}]")
        
        output = compute_mandelbrot(xmin, xmax, ymin, ymax, width, height, max_iter)
        plot_mandelbrot(output, xmin, xmax, ymin, ymax, iteration + 1)
        
        # Update the bounds for the next iteration
        width_delta = (xmax - xmin) * zoom_factor
        height_delta = (ymax - ymin) * zoom_factor
        xmin += width_delta / 2
        xmax -= width_delta / 2
        ymin += height_delta / 2
        ymax -= height_delta / 2

        print(f"Updated bounds: X: [{xmin}, {xmax}], Y: [{ymin}, {ymax}]")
        print(f"Zoom factor: {zoom_factor}\n")

# Parameters for the simulation
initial_xlim = (-2.0, 1.0)
initial_ylim = (-1.5, 1.5)
zoom_factor = 0.5  # Zoom in factor (reduce the bounds by this factor each iteration)
num_iterations = 5  # Number of iterations to run

# Run the simulation
mandelbrot_growth_simulation(initial_xlim, initial_ylim, zoom_factor, num_iterations)
