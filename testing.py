import pygame
import random

# Initialize Pygame
pygame.init()

# Set the width and height of the game window
WIDTH = 800
HEIGHT = 600

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Game")

# Load the player image
player_img = pygame.image.load("player.png")
player_width, player_height = player_img.get_width(), player_img.get_height()

# Load the obstacle image
obstacle_img = pygame.image.load("obstacle.png")
obstacle_width, obstacle_height = obstacle_img.get_width(), obstacle_img.get_height()

# Set the initial position of the player
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10

# Set the initial position and speed of the obstacle
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 5

# Set the player movement speed
player_speed = 5

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed

    # Update the position of the obstacle
    obstacle_y += obstacle_speed

    # Check for collision between the player and the obstacle
    if (
        player_x < obstacle_x + obstacle_width
        and player_x + player_width > obstacle_x
        and player_y < obstacle_y + obstacle_height
        and player_y + player_height > obstacle_y
    ):
        print("Game Over!")
        running = False

    # Render
    screen.fill(BLACK)
    screen.blit(player_img, (player_x, player_y))
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    # Update the game display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
