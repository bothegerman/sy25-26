
import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

score = 0
game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # --- BUG 1: Movement Logic ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 8  # Should move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 8  # Should move right

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- BUG 2: Resetting the Enemy ---
    if enemy_pos[1] > HEIGHT:
        # The enemy should go back to the top with a new X position
        # but the code below is missing something to make it "restart"
        score += 1
        print(f"Score: {score}")
        enemy_pos[1] = 0  # Move back to the top
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)

    # --- BUG 3: Collision Detection ---
    # This logic is mathematically incorrect for rectangular collision
    if (enemy_pos[0] == player_pos[0]) and (enemy_pos[1] == player_pos[1]):
        print("Game Over!")
        game_over = True
    
    if (player_pos[0] < enemy_pos[0] + enemy_size and player_pos[0] + player_size > enemy_pos[0] and 
        player_pos[1] < enemy_pos[1] + enemy_size and player_pos[1] + player_size > enemy_pos[1]):
        print("Game Over!")
        game_over = True



    # Drawing
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, RED, (enemy_pos[0], enemy_pos[1], enemy_size, enemy_size))
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()