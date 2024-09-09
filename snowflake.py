import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Natural Snowfall Simulation")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Snowflake class
class Snowflake(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.size = random.randint(5, 10)
        self.original_image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
        self.draw_snowflake(self.original_image, WHITE)
        self.image = self.original_image.copy()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = random.uniform(1, 3)  # Initial falling speed
        self.wind = random.uniform(-0.5, 0.5)  # Initial wind effect
        self.gravity = 0.05  # Gravity effect
        self.wind_amplitude = random.uniform(1, 3)
        self.wind_frequency = random.uniform(0.01, 0.05)
        self.time = 0
        self.change_time = None
        self.original_y = y  # For sway calculation

    def draw_snowflake(self, surface, color):
        surface.fill((0, 0, 0, 0))  # Clear the surface
        num_branches = random.randint(6, 12)
        branch_length = random.randint(self.size, self.size * 2)
        
        for i in range(num_branches):
            angle = i * (360 / num_branches)
            x1 = self.size + branch_length * math.cos(math.radians(angle))
            y1 = self.size + branch_length * math.sin(math.radians(angle))
            
            pygame.draw.line(surface, color, (self.size, self.size), (x1, y1), 2)
            
            # Add branch decorations
            decoration_length = random.randint(self.size // 2, self.size)
            for j in range(3):
                offset_angle = angle + random.randint(-15, 15)
                dx = decoration_length * math.cos(math.radians(offset_angle))
                dy = decoration_length * math.sin(math.radians(offset_angle))
                pygame.draw.line(surface, color, (x1, y1), (x1 + dx, y1 + dy), 1)

    def update(self):
        if self.change_time:
            if pygame.time.get_ticks() - self.change_time > 1000:
                self.kill()  # Remove the snowflake after 1 second
                return

        # Simulate gravity
        self.speed += self.gravity
        self.rect.y += self.speed
        
        # Simulate wind sway
        self.time += 0.1
        sway = self.wind_amplitude * math.sin(self.wind_frequency * self.time)  # Periodic sway
        self.rect.x += sway
        
        # Reset position if falling out of the screen
        if self.rect.y > HEIGHT:
            self.rect.y = -self.size  # Start from above the screen
            self.rect.x = random.randint(0, WIDTH)
            self.speed = random.uniform(1, 3)  # Reset speed for a natural effect

        # Reset position if moving out of the screen horizontally
        if self.rect.x > WIDTH:
            self.rect.x = -self.size
        elif self.rect.x < -self.size:
            self.rect.x = WIDTH

    def handle_collision(self):
        if not self.change_time:
            self.change_time = pygame.time.get_ticks()
            self.image = pygame.Surface((self.size * 2, self.size * 2), pygame.SRCALPHA)
            self.draw_snowflake(self.image, BLUE)

# Create sprite groups
all_sprites = pygame.sprite.Group()
snowflakes = pygame.sprite.Group()

# Create a larger number of snowflakes for a heavier snowfall
for _ in range(300):  # Increased number of snowflakes
    snowflake = Snowflake(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    all_sprites.add(snowflake)
    snowflakes.add(snowflake)

# Clock and wind variables
clock = pygame.time.Clock()
wind_direction = 1
wind_change_interval = 3000  # milliseconds
last_wind_change = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Check for collisions
    for snowflake1 in snowflakes:
        for snowflake2 in snowflakes:
            if snowflake1 != snowflake2 and pygame.sprite.collide_rect(snowflake1, snowflake2):
                snowflake1.handle_collision()
                snowflake2.handle_collision()

    # Update snowflakes
    all_sprites.update()

    # Change wind direction periodically
    now = pygame.time.get_ticks()
    if now - last_wind_change > wind_change_interval:
        wind_direction *= -1
        last_wind_change = now
        for snowflake in snowflakes:
            if not snowflake.change_time:  # Only update wind if the snowflake is not changing color
                snowflake.wind_amplitude = random.uniform(1, 5) * wind_direction
                snowflake.wind_frequency = random.uniform(0.01, 0.05)

    # Draw everything
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
