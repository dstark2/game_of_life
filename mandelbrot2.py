import pygame
import numpy as np

# Constants
WIDTH, HEIGHT = 800, 600
MAX_ITER = 100
RE_START, RE_END = -2.0, 1.0
IM_START, IM_END = -1.5, 1.5

# Initialize PyGame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mandelbrot Set")

def mandelbrot(c):
    z = c
    for n in range(MAX_ITER):
        if abs(z) > 2:
            return n
        z = z*z + c
    return MAX_ITER

def mandelbrot_set(width, height):
    pixels = np.zeros((width, height))
    for x in range(width):
        for y in range(height):
            re = RE_START + (RE_END - RE_START) * x / width
            im = IM_START + (IM_END - IM_START) * y / height
            c = complex(re, im)
            color_value = mandelbrot(c)
            pixels[x, y] = color_value
    return pixels

def render(pixels):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            color = int(pixels[x, y] * 255 / MAX_ITER)
            screen.set_at((x, y), (color, color, color))

def main():
    running = True
    pixels = mandelbrot_set(WIDTH, HEIGHT)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        render(pixels)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
