import pygame
import sys
import random

# --- User Input ---
radius = int(input("Enter circle radius (e.g. 30): "))
speed = int(input("Enter movement speed (e.g. 5): "))

# --- Init ---
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Automated Moving Circle")

clock = pygame.time.Clock()

# Circle properties
x, y = width // 2, height // 2
color = (0, 255, 0)

# Random initial direction
dx = random.choice([-1, 1]) * speed
dy = random.choice([-1, 1]) * speed

running = True

# --- Game Loop ---
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            # Change color
            elif event.key == pygame.K_c:
                color = (random.randint(0,255),
                         random.randint(0,255),
                         random.randint(0,255))

    # --- AUTOMATIC MOVEMENT ---
    x += dx
    y += dy

    # Bounce off walls
    if x - radius <= 0 or x + radius >= width:
        dx *= -1
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    if y - radius <= 0 or y + radius >= height:
        dy *= -1
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    # Draw circle
    pygame.draw.circle(screen, color, (x, y), radius)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()