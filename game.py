import pygame
import random
import sys

pygame.init()

# Game settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT // 2 - player_size // 2
player_speed = 10

ghost_sizes = [30, 40, 50]
num_ghosts = 5
ghosts = []

# Initialize ghosts
for _ in range(num_ghosts):
    ghost_size = random.choice(ghost_sizes)
    ghost_x = random.randint(WIDTH, WIDTH + 500)
    ghost_y = random.randint(0, HEIGHT - ghost_size)
    ghost_speed = random.randint(3, 8)
    ghosts.append([ghost_x, ghost_y, ghost_speed, ghost_size])

score = 0
font = pygame.font.Font(None, 24)  # Uses default Pygame font

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Avoid the Ghosts!")

clock = pygame.time.Clock()
running = True

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += player_speed
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    for ghost in ghosts:
        ghost[0] -= ghost[2]
        if ghost[0] < 0:
            ghost_size = random.choice(ghost_sizes)
            ghost[0] = random.randint(WIDTH, WIDTH + 500)
            ghost[1] = random.randint(0, HEIGHT - ghost_size)
            ghost[2] = random.randint(3, 8)
            score += 1

        pygame.draw.rect(screen, RED, (ghost[0], ghost[1], ghost[3], ghost[3]))

        # Collision detection
        if (player_x < ghost[0] + ghost[3] and
            player_x + player_size > ghost[0] and
            player_y < ghost[1] + ghost[3] and
            player_y + player_size > ghost[1]):
            running = False

    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_size, player_size))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
