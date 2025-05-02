import pygame
import sys


# Initialize Pygame
pygame.init()


# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple 2D Platformer")
clock = pygame.time.Clock()


# Player properties
player_size = (50, 50)
player_pos = [100, 500]
player_vel = [0, 0]
gravity = 0.5
jump_strength = -10
on_ground = False


# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(200, 450, 200, 20),
    pygame.Rect(500, 350, 200, 20)
]


# Player rect
player_rect = pygame.Rect(player_pos[0], player_pos[1], *player_size)


# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(WHITE)


    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    # Key state
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_vel[0] = -5
    elif keys[pygame.K_RIGHT]:
        player_vel[0] = 5
    else:
        player_vel[0] = 0


    if keys[pygame.K_SPACE] and on_ground:
        player_vel[1] = jump_strength
        on_ground = False


    # Apply gravity
    player_vel[1] += gravity


    # Move the player
    player_rect.x += player_vel[0]
    player_rect.y += player_vel[1]


    # Collision detection
    on_ground = False
    for platform in platforms:
        if player_rect.colliderect(platform):
            # From top
            if player_vel[1] > 0 and player_rect.bottom - player_vel[1] <= platform.top:
                player_rect.bottom = platform.top
                player_vel[1] = 0
                on_ground = True


    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, GREEN, platform)


    # Draw player
    pygame.draw.rect(screen, BLUE, player_rect)


    # Update display
    pygame.display.flip()


pygame.quit()
sys.exit()
